// src/data/devices.ts

export type DeviceDefinition = {
  id: string
  name: string
  chip: string
  fullManifestUrl: string
  updateManifestUrl: string
  disabled?: boolean
}

export const devices: DeviceDefinition[] = [
  {
    id: 'guition-esp32-4848s040',
    name: 'Guition ESP32 4848S040',
    chip: 'ESP32-S3',
    fullManifestUrl: 'firmware/guition-esp32-4848s040/full/flash_args.json',
    updateManifestUrl: 'firmware/guition-esp32-4848s040/update/flash_args.json',
    disabled: true,
  },
  {
    id: 'guition-jc1060p470c',
    name: 'Guition JC1060P470C',
    chip: 'ESP32-P4',
    fullManifestUrl: 'firmware/guition-jc1060p470c/full/flash_args.json',
    updateManifestUrl: 'firmware/guition-jc1060p470c/update/flash_args.json',
  },
  {
    id: 'waveshare-p4-86-panel-eth-2ro',
    name: 'Waveshare P4 8.6 Panel ETH 2RO',
    chip: 'ESP32-P4',
    fullManifestUrl: 'firmware/waveshare-p4-86-panel-eth-2ro/full/flash_args.json',
    updateManifestUrl: 'firmware/waveshare-p4-86-panel-eth-2ro/update/flash_args.json',
  },
  {
    id: 'waveshare-p4-101-jd9365',
    name: 'Waveshare P4 10.1 JD9365',
    chip: 'ESP32-P4',
    fullManifestUrl: 'firmware/waveshare-p4-101-jd9365/full/flash_args.json',
    updateManifestUrl: 'firmware/waveshare-p4-101-jd9365/update/flash_args.json',
  },
]
