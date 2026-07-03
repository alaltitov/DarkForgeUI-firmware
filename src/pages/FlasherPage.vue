<!-- src/pages/FlasherPage.vue -->

<template>
  <v-container class="flasher-page">
    <v-row class="flasher-layout">
      <v-col cols="12" lg="5" class="flasher-col">
        <v-card class="control-card">
          <div class="section-title">
            <v-icon icon="mdi-devices" />
            <span>{{ t('flasher.device.title') }}</span>
          </div>

          <v-select
            v-model="selectedDeviceId"
            :items="deviceItems"
            item-title="title"
            item-value="value"
            :item-props="getDeviceItemProps"
            :label="t('flasher.device.select')"
            :disabled="isBusy"
            hide-details
          />

          <div class="section-title mode-section-title">
            <v-icon icon="mdi-tune" />
            <span>{{ t('flasher.mode.title') }}</span>
          </div>

          <v-radio-group
            v-model="selectedFlashMode"
            :disabled="isBusy || !selectedDevice || selectedDevice.disabled"
            hide-details
            class="mode-radio-group"
          >
            <v-card
              class="mode-card"
              :class="{ active: selectedFlashMode === 'update' }"
              @click="!isBusy && selectedDevice && !selectedDevice.disabled && (selectedFlashMode = 'update')"
            >
              <div class="mode-content">
                <v-radio value="update" color="primary" />

                <div>
                  <div class="mode-title">{{ t('flasher.mode.updateTitle') }}</div>
                </div>
              </div>
            </v-card>

            <v-card
              class="mode-card mode-card-full"
              :class="{ active: selectedFlashMode === 'full' }"
              @click="!isBusy && selectedDevice && !selectedDevice.disabled && (selectedFlashMode = 'full')"
            >
              <div class="mode-content">
                <v-radio value="full" color="primary" />

                <div>
                  <div class="mode-title">{{ t('flasher.mode.fullTitle') }}</div>
                </div>
              </div>
            </v-card>
          </v-radio-group>

          <v-alert
            :type="selectedFlashMode === 'full' ? 'warning' : 'success'"
            variant="tonal"
            density="comfortable"
            rounded="lg"
            class="mode-warning"
          >
            {{
              selectedFlashMode === 'full'
                ? t('flasher.warning.full')
                : t('flasher.warning.update')
            }}
          </v-alert>

          <div class="actions">
            <v-btn
              color="primary"
              size="large"
              block
              :disabled="isBusy || !selectedDevice || selectedDevice.disabled"
              :loading="isBusy && ['connecting', 'loadingManifest', 'downloadingFiles', 'flashing'].includes(uiState)"
              prepend-icon="mdi-flash"
              @click="connectAndFlash(selectedFlashMode)"
            >
              {{
                selectedFlashMode === 'full'
                  ? t('flasher.actions.full')
                  : t('flasher.actions.update')
              }}
            </v-btn>

            <v-btn
              color="error"
              size="large"
              block
              variant="tonal"
              :disabled="isBusy || !selectedDevice || selectedDevice.disabled"
              :loading="isBusy && uiState === 'erasing'"
              prepend-icon="mdi-delete-alert"
              @click="eraseDeviceFlash"
            >
              {{ t('flasher.actions.erase') }}
            </v-btn>
          </div>
        </v-card>
      </v-col>

      <v-col cols="12" lg="7" class="flasher-col">
        <v-card class="status-card">
          <div class="status-panel" :class="stateClass(uiState)">
            <div class="status-dot" />

            <div>
              <div class="status-label">{{ t('flasher.status.label') }}</div>
              <div class="status-text">{{ statusText }}</div>
            </div>
          </div>

          <div v-if="progress > 0 || currentFileName" class="progress-area">
            <div class="progress-header">
              <span class="file-badge">{{ currentFileName || t('flasher.progress.preparing') }}</span>
              <span class="percent">{{ progress }}%</span>
            </div>

            <v-progress-linear
              :model-value="progress"
              color="primary"
              height="10"
              rounded
            />
          </div>

          <div v-if="logLines.length" class="log-box">
            <div class="log-header">
              <span>{{ t('flasher.log.title') }}</span>
              <span>{{ logLines.length }}</span>
            </div>

            <div ref="logBoxRef" class="log-list">
              <div
                v-for="(line, index) in logLines"
                :key="index"
                class="log-entry"
              >
                {{ line }}
              </div>
            </div>
          </div>

          <v-empty-state
            v-else
            class="empty-state"
            :title="t('flasher.log.emptyTitle')"
            :text="t('flasher.log.emptyText')"
          />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed, nextTick, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { CustomReset, ESPLoader, Transport } from 'esptool-js'

import { devices, type DeviceDefinition } from '../data/devices'

type FlashFileEntry = {
  path: string
  address: number
}

type FlashManifest = {
  flash_mode: string
  flash_freq: string
  flash_size: string
  files: FlashFileEntry[]
}

type FlashModeValues = 'qio' | 'qout' | 'dio' | 'dout' | 'keep'

type FlashFreqValues =
  | 'keep'
  | '80m'
  | '60m'
  | '48m'
  | '40m'
  | '30m'
  | '26m'
  | '24m'
  | '20m'
  | '16m'
  | '15m'
  | '12m'

type FlashSizeValues =
  | 'detect'
  | 'keep'
  | '256KB'
  | '512KB'
  | '1MB'
  | '2MB'
  | '4MB'
  | '8MB'
  | '16MB'
  | '32MB'
  | '64MB'
  | '128MB'

type FlashFile = {
  data: Uint8Array
  address: number
}

type UiState =
  | 'idle'
  | 'connecting'
  | 'loadingManifest'
  | 'downloadingFiles'
  | 'flashing'
  | 'erasing'
  | 'resetting'
  | 'success'
  | 'error'

type FlashMode = 'update' | 'full'

type DeviceSelectItem = {
  title: string
  value: string
  disabled: boolean
}

const { t } = useI18n()

const isBusy = ref(false)
const progress = ref(0)
const currentFileName = ref('')
const logLines = ref<string[]>([])
const uiState = ref<UiState>('idle')
const logBoxRef = ref<HTMLElement | null>(null)
const selectedFlashMode = ref<FlashMode>('update')

const selectedDeviceId = ref(
  devices.find((device) => !device.disabled)?.id ?? devices[0]?.id ?? '',
)

let esploader: ESPLoader | null = null
let transport: Transport | null = null

const selectedDevice = computed<DeviceDefinition | undefined>(() => {
  return devices.find((device) => device.id === selectedDeviceId.value)
})

const deviceItems = computed<DeviceSelectItem[]>(() => {
  return devices.map((device) => ({
    title: `${device.name} · ${device.chip}${device.disabled ? ` · ${t('flasher.device.comingSoon')}` : ''}`,
    value: device.id,
    disabled: Boolean(device.disabled),
  }))
})

const statusText = computed(() => {
  switch (uiState.value) {
    case 'idle':
      return t('flasher.status.idle')
    case 'connecting':
      return t('flasher.status.connecting')
    case 'loadingManifest':
      return t('flasher.status.loadingManifest')
    case 'downloadingFiles':
      return t('flasher.status.downloadingFiles')
    case 'flashing':
      return selectedFlashMode.value === 'update'
        ? t('flasher.status.flashingUpdate')
        : t('flasher.status.flashingFull')
    case 'erasing':
      return t('flasher.status.erasing')
    case 'resetting':
      return t('flasher.status.resetting')
    case 'success':
      return t('flasher.status.success')
    case 'error':
      return t('flasher.status.error')
    default:
      return t('flasher.status.ready')
  }
})

function getDeviceItemProps(item: DeviceSelectItem) {
  return {
    disabled: item.disabled,
  }
}

function stateClass(state: UiState): string {
  if (state === 'success') return 'is-success'
  if (state === 'error') return 'is-error'
  if (state === 'flashing' || state === 'erasing' || state === 'connecting') return 'is-active'
  return ''
}

function formatHex(address: number): string {
  return `0x${address.toString(16).toUpperCase()}`
}

function resolveAssetUrl(path: string): string {
  const base = import.meta.env.BASE_URL || '/'
  const normalizedBase = base.endsWith('/') ? base : `${base}/`
  const normalizedPath = path.startsWith('/') ? path.slice(1) : path

  return `${normalizedBase}${normalizedPath}`
}

function getManifestUrl(device: DeviceDefinition, mode: FlashMode): string {
  return resolveAssetUrl(mode === 'full' ? device.fullManifestUrl : device.updateManifestUrl)
}

function resolveFirmwareFileUrl(manifestUrl: string, filePath: string): string {
  const manifestBase = manifestUrl.slice(0, manifestUrl.lastIndexOf('/') + 1)
  return `${manifestBase}${filePath}`
}

async function scrollLogToBottom(): Promise<void> {
  await nextTick()

  if (logBoxRef.value) {
    logBoxRef.value.scrollTop = logBoxRef.value.scrollHeight
  }
}

function appendLog(message: string): void {
  logLines.value.push(message)
  console.log(message)
  void scrollLogToBottom()
}

function resetUiForOperation(): void {
  isBusy.value = true
  progress.value = 0
  currentFileName.value = ''
  logLines.value = []
  uiState.value = 'idle'
}

async function fetchJson<T>(url: string): Promise<T> {
  const response = await fetch(url, { cache: 'no-store' })

  if (!response.ok) {
    throw new Error(`${t('flasher.errors.json')} ${url}`)
  }

  return (await response.json()) as T
}

async function fetchBinary(url: string): Promise<Uint8Array> {
  const response = await fetch(url, { cache: 'no-store' })

  if (!response.ok) {
    throw new Error(`${t('flasher.errors.binary')} ${url}`)
  }

  const buffer = await response.arrayBuffer()

  return new Uint8Array(buffer)
}

async function openConnection(): Promise<void> {
  const nav = navigator as Navigator & {
    serial?: {
      requestPort: () => Promise<unknown>
    }
  }

  if (!nav.serial) {
    throw new Error(t('flasher.errors.webSerial'))
  }

  uiState.value = 'connecting'
  appendLog(t('flasher.log.requestPort'))

  const port = await nav.serial.requestPort()

  transport = new Transport(port as any, true)

  esploader = new ESPLoader({
    transport,
    baudrate: 460800,
    terminal: {
      clean: () => {},
      writeLine: (data: string) => appendLog(data),
      write: (data: string) => appendLog(data),
    },
  } as any)

  const chip = await (esploader as any).main()

  appendLog(`${t('flasher.log.connected')} ${chip}`)
}

async function closeConnection(): Promise<void> {
  if (transport) {
    appendLog(t('flasher.log.disconnecting'))
    await transport.disconnect().catch(() => {})
    transport = null
  }

  esploader = null
}

async function hardResetDevice(): Promise<void> {
  if (!transport) {
    return
  }

  uiState.value = 'resetting'
  appendLog(t('flasher.log.resetting'))

  const resetStrategy = new CustomReset(transport, 'D0|R1|W200|R0|W1000')
  await resetStrategy.reset()
}

async function eraseDeviceFlash(): Promise<void> {
  const device = selectedDevice.value

  if (!device || device.disabled) {
    return
  }

  try {
    resetUiForOperation()
    await openConnection()

    if (!esploader) {
      throw new Error('ESPLoader was not initialized.')
    }

    uiState.value = 'erasing'
    appendLog(t('flasher.log.eraseStart'))

    if (!(esploader as any).eraseFlash) {
      throw new Error(t('flasher.errors.eraseUnsupported'))
    }

    await (esploader as any).eraseFlash()

    appendLog(t('flasher.log.eraseDone'))

    progress.value = 100
    currentFileName.value = t('flasher.progress.erased')

    await hardResetDevice()

    uiState.value = 'success'
    appendLog(t('flasher.log.eraseSuccess'))
  } catch (error: unknown) {
    const message = error instanceof Error ? error.message : String(error)

    uiState.value = 'error'
    appendLog(`${t('flasher.log.error')} ${message}`)
    console.error(error)
  } finally {
    await closeConnection()
    isBusy.value = false
  }
}

async function connectAndFlash(mode: FlashMode): Promise<void> {
  const device = selectedDevice.value

  if (!device || device.disabled) {
    return
  }

  try {
    selectedFlashMode.value = mode
    resetUiForOperation()

    await openConnection()

    if (!esploader) {
      throw new Error('ESPLoader was not initialized.')
    }

    uiState.value = 'loadingManifest'

    const manifestUrl = getManifestUrl(device, mode)

    appendLog(`${t('flasher.log.readManifest')} ${manifestUrl}`)

    const manifest = await fetchJson<FlashManifest>(manifestUrl)

    if (!manifest.files.length) {
      throw new Error('Firmware manifest does not contain any files.')
    }

    uiState.value = 'downloadingFiles'
    appendLog(t('flasher.log.downloadFiles'))

    const fileArray: FlashFile[] = await Promise.all(
      manifest.files.map(async (file) => {
        const fileUrl = resolveFirmwareFileUrl(manifestUrl, file.path)

        appendLog(`${t('flasher.log.download')} ${file.path} → ${formatHex(file.address)}`)

        return {
          data: await fetchBinary(fileUrl),
          address: file.address,
        }
      }),
    )

    uiState.value = 'flashing'

    const eraseAll = mode === 'full'

    appendLog(
      eraseAll
        ? t('flasher.log.modeFull')
        : t('flasher.log.modeUpdate'),
    )

    appendLog(`eraseAll=${eraseAll}`)
    appendLog(
      `mode=${manifest.flash_mode}, freq=${manifest.flash_freq}, size=${manifest.flash_size}`,
    )

    appendLog(t('flasher.log.writeFlash'))

    await (esploader as any).writeFlash({
      fileArray,
      eraseAll,
      compress: true,
      flashMode: manifest.flash_mode as FlashModeValues,
      flashFreq: manifest.flash_freq as FlashFreqValues,
      flashSize: manifest.flash_size as FlashSizeValues,
      reportProgress: (fileIndex: number, written: number, total: number) => {
        if (manifest.files[fileIndex]) {
          const file = manifest.files[fileIndex]
          currentFileName.value = `${file.path} · ${formatHex(file.address)}`
        }

        progress.value = total > 0 ? Math.round((written / total) * 100) : 0
      },
    })

    appendLog(
      eraseAll
        ? t('flasher.log.fullDone')
        : t('flasher.log.updateDone'),
    )

    progress.value = 100
    currentFileName.value = t('flasher.progress.done')

    await hardResetDevice()

    uiState.value = 'success'
    appendLog(t('flasher.log.booted'))
  } catch (error: unknown) {
    const message = error instanceof Error ? error.message : String(error)

    uiState.value = 'error'
    appendLog(`${t('flasher.log.error')} ${message}`)
    console.error(error)
  } finally {
    await closeConnection()
    isBusy.value = false
  }
}
</script>

<style scoped>
.flasher-page {
  height: calc(100vh - 76px);
  max-height: calc(100vh - 76px);
  padding-top: 24px;
  padding-bottom: 24px;
  overflow: hidden;
}

.flasher-layout {
  height: 100%;
  overflow: hidden;
}

.flasher-col {
  height: 100%;
  min-height: 0;
}

.control-card,
.status-card {
  height: 100%;
  min-height: 0;
  padding: 22px;
  overflow: hidden;
  background: rgba(17, 24, 34, 0.82);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.status-card {
  display: flex;
  flex-direction: column;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
  color: #f8fafc;
  font-size: 15px;
  font-weight: 950;
}

.mode-section-title {
  margin-top: 24px;
}

.mode-radio-group {
  display: grid;
  gap: 12px;
}

.mode-card {
  display: flex;
  padding: 13px;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.035);
  border: 1px solid rgba(255, 255, 255, 0.08);
  transition:
    border-color 0.16s ease,
    background 0.16s ease;
}

.mode-card-full {
  margin-top: 12px;
}

.mode-card.active {
  border-color: rgba(255, 122, 26, 0.52);
  background: rgba(255, 122, 26, 0.10);
}

.mode-content {
  display: flex;
  align-items: center;
  gap: 10px;
}

.mode-title {
  color: #f8fafc;
  font-size: 14px;
  font-weight: 950;
}

.mode-warning {
  margin-top: 16px;
}

.actions {
  display: grid;
  gap: 12px;
  margin-top: 22px;
}

.status-panel {
  display: flex;
  align-items: center;
  flex: 0 0 auto;
  gap: 14px;
  padding: 16px 18px;
  margin-bottom: 18px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.035);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.status-panel.is-active {
  border-color: rgba(255, 122, 26, 0.42);
}

.status-panel.is-success {
  border-color: rgba(34, 197, 94, 0.42);
  background: rgba(34, 197, 94, 0.08);
}

.status-panel.is-error {
  border-color: rgba(239, 68, 68, 0.42);
  background: rgba(239, 68, 68, 0.08);
}

.status-dot {
  width: 12px;
  height: 12px;
  flex: 0 0 auto;
  border-radius: 999px;
  background: #64748b;
}

.status-panel.is-active .status-dot {
  background: #ff7a1a;
  box-shadow: 0 0 16px rgba(255, 122, 26, 0.52);
}

.status-panel.is-success .status-dot {
  background: #22c55e;
  box-shadow: 0 0 16px rgba(34, 197, 94, 0.45);
}

.status-panel.is-error .status-dot {
  background: #ef4444;
  box-shadow: 0 0 16px rgba(239, 68, 68, 0.45);
}

.status-label {
  color: #94a3b8;
  font-size: 12px;
  margin-bottom: 4px;
}

.status-text {
  color: #f8fafc;
  font-size: 15px;
  font-weight: 900;
}

.progress-area {
  flex: 0 0 auto;
  padding: 16px;
  margin-bottom: 18px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.035);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.progress-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 12px;
}

.file-badge {
  max-width: 78%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #ff9a3d;
  font-family: "JetBrains Mono", "Fira Code", monospace;
  font-size: 12px;
}

.percent {
  color: #f8fafc;
  font-weight: 900;
}

.log-box {
  display: flex;
  flex: 1 1 auto;
  min-height: 0;
  overflow: hidden;
  flex-direction: column;
  border-radius: 18px;
  background: rgba(7, 11, 16, 0.72);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.log-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex: 0 0 auto;
  min-height: 46px;
  padding: 0 16px;
  color: #cbd5e1;
  font-size: 12px;
  font-weight: 900;
  text-transform: uppercase;
  background: rgba(255, 255, 255, 0.04);
}

.log-list {
  flex: 1 1 auto;
  min-height: 0;
  overflow-y: auto;
  padding: 16px;
  scroll-behavior: smooth;
}

.log-entry {
  margin-bottom: 8px;
  color: #d6dee7;
  font-family: "JetBrains Mono", "Fira Code", monospace;
  font-size: 12px;
  line-height: 1.65;
  white-space: pre-wrap;
  word-break: break-word;
}

.log-entry:last-child {
  margin-bottom: 0;
}

.empty-state {
  flex: 1 1 auto;
  min-height: 0;
}

@media (max-width: 1279px) {
  .flasher-page {
    height: calc(100vh - 76px);
    max-height: calc(100vh - 76px);
    padding-top: 16px;
    padding-bottom: 16px;
  }

  .flasher-layout {
    overflow: hidden;
  }

  .control-card,
  .status-card {
    padding: 18px;
  }
}
</style>
