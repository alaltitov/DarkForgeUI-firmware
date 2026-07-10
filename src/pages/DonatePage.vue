<!-- src/pages/DonatePage.vue -->

<template>
  <v-container class="donate-page">
    <section class="donate-hero">
      <h1>{{ t('donate.title') }}</h1>

      <p>
        {{ t('donate.description') }}
      </p>
    </section>

    <section class="donate-content">
      <div class="notice-card">
        <v-icon icon="mdi-information-outline" size="24" />

        <p>
          {{ t('donate.notice') }}
        </p>
      </div>

      <div class="qr-grid">
        <article
          v-for="item in qrItems"
          :key="item.title"
          class="qr-card"
        >
          <h2>{{ item.title }}</h2>

          <div class="qr-image-wrap">
            <img
              :src="item.image"
              :alt="item.alt"
              class="qr-image"
            >
          </div>
        </article>
      </div>
    </section>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

import telegramQr from '../../public/assets/qr-codes/qr-code-telegram.png'
import boostyQr from '../../public/assets/qr-codes/qr-code-boosty.png'

type QrItem = {
  title: string
  image: string
  alt: string
}

const { t } = useI18n()

const qrItems = computed<QrItem[]>(() => [
  {
    title: 'Telegram',
    image: telegramQr,
    alt: t('donate.telegramAlt'),
  },
  {
    title: 'Boosty',
    image: boostyQr,
    alt: t('donate.boostyAlt'),
  },
])
</script>

<style scoped>
.donate-page {
  --qr-size: 280px;

  min-height: calc(100vh - 76px);
  padding-top: 56px;
  padding-bottom: 72px;
}

.donate-hero {
  max-width: 820px;
  margin: 0 auto 34px;
  text-align: center;
}

.page-icon {
  color: #ff7a1a;
  margin-bottom: 18px;
}

.donate-hero h1 {
  margin: 0 0 14px;
  color: #f8fafc;
  font-size: clamp(34px, 5vw, 58px);
  font-weight: 950;
  line-height: 1;
  letter-spacing: -0.06em;
}

.donate-hero p {
  max-width: 720px;
  margin: 0 auto;
  color: #a8b4c3;
  font-size: 17px;
  line-height: 1.7;
}

.donate-content {
  width: min(960px, 100%);
  margin: 0 auto;
}

.notice-card {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  max-width: 820px;
  margin: 0 auto 28px;
  padding: 18px 20px;
  color: #cbd5e1;
  border: 1px solid rgba(255, 122, 26, 0.20);
  border-radius: 22px;
  background:
    linear-gradient(145deg, rgba(17, 24, 34, 0.76), rgba(13, 19, 28, 0.84)),
    radial-gradient(circle at top right, rgba(255, 122, 26, 0.12), transparent 34%);
}

.notice-card .v-icon {
  flex: 0 0 auto;
  color: #ff9a3d;
  margin-top: 2px;
}

.notice-card p {
  margin: 0;
  color: #cbd5e1;
  font-size: 15px;
  line-height: 1.7;
}

.qr-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 24px;
}

.qr-card {
  padding: 24px;
  text-align: center;
  border-radius: 28px;
  background:
    linear-gradient(145deg, rgba(17, 24, 34, 0.86), rgba(13, 19, 28, 0.92)),
    radial-gradient(circle at top, rgba(255, 122, 26, 0.11), transparent 36%);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.qr-card h2 {
  margin: 0 0 18px;
  color: #f8fafc;
  font-size: 24px;
  font-weight: 950;
  line-height: 1.15;
  letter-spacing: -0.04em;
}

.qr-image-wrap {
  display: grid;
  place-items: center;
  width: 100%;
  padding: 0;
  border-radius: 0;
  background: transparent;
}

.qr-image {
  display: block;
  width: var(--qr-size);
  max-width: 100%;
  height: auto;
  object-fit: contain;
}

@media (max-width: 760px) {
  .donate-page {
    padding-top: 36px;
    padding-bottom: 52px;
  }

  .qr-grid {
    grid-template-columns: 1fr;
  }

  .notice-card {
    border-radius: 20px;
  }

  .qr-card {
    padding: 20px;
    border-radius: 24px;
  }

  .qr-card h2 {
    font-size: 22px;
  }
}
</style>
