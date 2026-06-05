<!-- src/pages/InfoPage.vue -->

<template>
  <v-container class="info-page">
    <v-card class="info-card">
      <v-icon icon="mdi-information-outline" size="42" class="info-icon" />

      <h1>{{ t('info.title') }}</h1>

      <p>
        {{ t('info.placeholder') }}
      </p>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<style scoped>
.info-page {
  min-height: calc(100vh - 76px);
  display: grid;
  place-items: center;
  padding-top: 52px;
  padding-bottom: 72px;
}

.info-card {
  width: min(720px, 100%);
  padding: 42px;
  text-align: center;
  background: rgba(17, 24, 34, 0.82);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.info-icon {
  color: #ff7a1a;
  margin-bottom: 18px;
}

.info-card h1 {
  margin: 0 0 14px;
  color: #f8fafc;
  font-size: clamp(34px, 5vw, 56px);
  font-weight: 950;
  letter-spacing: -0.06em;
}

.info-card p {
  max-width: 520px;
  margin: 0 auto;
  color: #a8b4c3;
  font-size: 17px;
  line-height: 1.7;
}
</style>
