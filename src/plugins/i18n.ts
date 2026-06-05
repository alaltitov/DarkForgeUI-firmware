// src/plugins/i18n.ts

import { createI18n } from 'vue-i18n'

import en from '../i18n/en.json'
import ru from '../i18n/ru.json'
import de from '../i18n/de.json'
import fr from '../i18n/fr.json'
import es from '../i18n/es.json'
import pt from '../i18n/pt.json'
import it from '../i18n/it.json'

export type AppLocale = 'en' | 'ru' | 'de' | 'fr' | 'es' | 'pt' | 'it'

const savedLocale = localStorage.getItem('darkforge_locale') as AppLocale | null

const browserLocale = navigator.language.slice(0, 2) as AppLocale

const supportedLocales: AppLocale[] = ['en', 'ru', 'de', 'fr', 'es', 'pt', 'it']

const locale: AppLocale = savedLocale && supportedLocales.includes(savedLocale)
  ? savedLocale
  : supportedLocales.includes(browserLocale)
    ? browserLocale
    : 'en'

export default createI18n({
  legacy: false,
  locale,
  fallbackLocale: 'en',
  messages: {
    en,
    ru,
    de,
    fr,
    es,
    pt,
    it,
  },
})
