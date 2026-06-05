// src/plugins/vuetify.ts

import { createVuetify } from 'vuetify'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

const darkForgeTheme = {
  dark: true,
  colors: {
    background: '#070B10',
    surface: '#111822',
    'surface-bright': '#182231',
    'surface-light': '#202B3A',
    primary: '#FF7A1A',
    secondary: '#60A5FA',
    accent: '#FF7A1A',
    error: '#EF4444',
    info: '#38BDF8',
    success: '#22C55E',
    warning: '#F97316',
  },
}

export default createVuetify({
  theme: {
    defaultTheme: 'darkForgeTheme',
    themes: {
      darkForgeTheme,
    },
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
  defaults: {
    VBtn: {
      rounded: 'xl',
      elevation: 0,
    },
    VCard: {
      rounded: 'xl',
      elevation: 0,
    },
    VTextField: {
      variant: 'outlined',
      density: 'comfortable',
    },
    VSelect: {
      variant: 'outlined',
      density: 'comfortable',
    },
  },
})
