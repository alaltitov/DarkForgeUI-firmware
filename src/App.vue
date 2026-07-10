<!-- src/App.vue -->

<template>
  <v-app>
    <div class="app-shell">
      <v-app-bar
        class="app-bar"
        height="76"
        flat
      >
        <v-container class="app-bar-container">
          <RouterLink class="brand" to="/">
            <div class="brand-mark">
              <v-icon icon="mdi-fire" size="24" />
            </div>

            <div>
              <div class="brand-title">DarkForge UI</div>
            </div>
          </RouterLink>

          <v-spacer />

          <div class="desktop-nav">
            <v-btn
              v-for="item in navItems"
              :key="item.to"
              class="nav-button"
              variant="text"
              :to="item.to"
            >
              {{ t(item.labelKey) }}
            </v-btn>
          </div>

          <v-menu location="bottom end">
            <template #activator="{ props }">
              <v-btn
                v-bind="props"
                class="mobile-nav-button"
                variant="tonal"
                icon="mdi-menu"
              />
            </template>

            <v-list class="language-list" density="comfortable">
              <v-list-item
                v-for="item in navItems"
                :key="item.to"
                :to="item.to"
              >
                <template #prepend>
                  <v-icon :icon="item.icon" />
                </template>

                <v-list-item-title>
                  {{ t(item.labelKey) }}
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

          <v-btn
            class="beta-button"
            color="primary"
            variant="flat"
            prepend-icon="mdi-flask"
            to="/beta"
          >
            {{ t('nav.beta') }}
          </v-btn>

          <v-menu location="bottom end">
            <template #activator="{ props }">
              <v-btn
                v-bind="props"
                class="language-button"
                variant="tonal"
              >
                <span class="flag">{{ currentLocale.flag }}</span>
                <span class="language-code">{{ currentLocale.code.toUpperCase() }}</span>
                <v-icon icon="mdi-chevron-down" size="18" />
              </v-btn>
            </template>

            <v-list class="language-list" density="comfortable">
              <v-list-item
                v-for="localeItem in locales"
                :key="localeItem.code"
                :active="locale === localeItem.code"
                @click="setLocale(localeItem.code)"
              >
                <template #prepend>
                  <span class="flag">{{ localeItem.flag }}</span>
                </template>

                <v-list-item-title>
                  {{ localeItem.name }}
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-container>
      </v-app-bar>

      <v-main class="app-main">
        <RouterView />
      </v-main>
    </div>
  </v-app>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useI18n } from 'vue-i18n'

type LocaleCode = 'en' | 'ru' | 'de' | 'fr' | 'es' | 'pt' | 'it'

type LocaleOption = {
  code: LocaleCode
  name: string
  flag: string
}

type NavItem = {
  to: string
  labelKey: string
  icon: string
}

const { t, locale } = useI18n()

const fallbackLocale: LocaleOption = {
  code: 'en',
  name: 'English',
  flag: '🇬🇧',
}

const locales: LocaleOption[] = [
  fallbackLocale,
  { code: 'ru', name: 'Русский', flag: '🇷🇺' },
  { code: 'de', name: 'Deutsch', flag: '🇩🇪' },
  { code: 'fr', name: 'Français', flag: '🇫🇷' },
  { code: 'es', name: 'Español', flag: '🇪🇸' },
  { code: 'pt', name: 'Português', flag: '🇵🇹' },
  { code: 'it', name: 'Italiano', flag: '🇮🇹' },
]

const navItems: NavItem[] = [
  {
    to: '/info',
    labelKey: 'nav.info',
    icon: 'mdi-information-outline',
  },
  {
    to: '/roadmap',
    labelKey: 'nav.roadmap',
    icon: 'mdi-map-clock',
  },
  {
    to: '/qa',
    labelKey: 'nav.qa',
    icon: 'mdi-help-circle-outline',
  },
  {
    to: '/donate',
    labelKey: 'nav.donate',
    icon: 'mdi-heart',
  },
]

const currentLocale = computed<LocaleOption>(() => {
  return locales.find((item) => item.code === locale.value) ?? fallbackLocale
})

function setLocale(code: LocaleCode): void {
  locale.value = code
  localStorage.setItem('darkforge_locale', code)
}
</script>

<style scoped>
:global(html, body, #app) {
  width: 100%;
  min-height: 100%;
  margin: 0;
}

:global(html) {
  overflow: hidden;
}

:global(body) {
  overflow: hidden;
}

:global(body) {
  background:
    radial-gradient(circle at 12% 10%, rgba(255, 122, 26, 0.18), transparent 24%),
    radial-gradient(circle at 88% 8%, rgba(96, 165, 250, 0.16), transparent 24%),
    radial-gradient(circle at 50% 100%, rgba(167, 139, 250, 0.12), transparent 28%),
    #070b10;
}

.app-shell {
  height: 100vh;
  min-height: 100vh;
  overflow: hidden;
  background:
    linear-gradient(180deg, rgba(7, 11, 16, 0.72), rgba(7, 11, 16, 1)),
    radial-gradient(circle at top, rgba(255, 122, 26, 0.08), transparent 28%);
}

.app-main {
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
}

.app-bar {
  background: rgba(7, 11, 16, 0.74) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(18px);
}

.app-bar-container {
  display: flex;
  align-items: center;
  width: 100%;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  color: inherit;
  text-decoration: none;
}

.brand-mark {
  display: grid;
  width: 44px;
  height: 44px;
  place-items: center;
  color: #111827;
  border-radius: 16px;
  background: linear-gradient(180deg, #ff9a3d, #f97316);
  box-shadow: 0 12px 30px rgba(249, 115, 22, 0.30);
}

.brand-title {
  color: #f8fafc;
  font-size: 18px;
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1.1;
}

.beta-button {
  margin-right: 12px;
  color: #111827 !important;
  font-weight: 900;
}

.language-button {
  min-width: 104px;
}

.flag {
  display: inline-flex;
  margin-right: 8px;
  font-size: 18px;
}

.language-code {
  margin-right: 4px;
  font-weight: 800;
}

.language-list {
  min-width: 220px;
  background: #111822 !important;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.desktop-nav {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-right: 12px;
}

.nav-button {
  color: #cbd5e1 !important;
  font-weight: 850;
  text-transform: none;
}

.nav-button:hover {
  color: #ffffff !important;
}

.mobile-nav-button {
  display: none;
  margin-right: 10px;
}

@media (max-width: 960px) {
  .desktop-nav {
    display: none;
  }

  .mobile-nav-button {
    display: inline-flex;
  }
}

@media (max-width: 640px) {
  .brand-title {
    display: none;
  }

  .beta-button {
    min-width: 44px;
    padding-inline: 12px;
  }

  .beta-button :deep(.v-btn__prepend) {
    margin-inline-end: 0;
  }

  .beta-button :deep(.v-btn__content) {
    display: none;
  }

  .language-code {
    display: none;
  }
}
</style>
