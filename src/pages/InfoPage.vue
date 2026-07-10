<!-- src/pages/InfoPage.vue -->

<template>
  <v-container class="info-page">
    <v-card class="info-card">
      <section class="info-hero">

        <h1>{{ t('info.hero.title') }}</h1>

        <div class="text-primary text-headline-medium pb-4">{{ t('info.hero.subtitle') }}</div>

        <p class="hero-lead">
          {{ t('info.hero.lead') }}
        </p>
      </section>

      <v-divider class="section-divider" />

      <section class="info-section">
        <div class="section-heading">
          <v-icon icon="mdi-star-four-points" />
          <h2>{{ t('info.benefits.title') }}</h2>
        </div>

        <div class="benefits-list">
          <div
            v-for="item in benefits"
            :key="item.title"
            class="benefit-item"
          >
            <div class="benefit-marker">
              <v-icon icon="mdi-check" size="18" />
            </div>

            <div class="benefit-content">
              <h3>{{ item.title }}</h3>
              <p>{{ item.text }}</p>
            </div>
          </div>
        </div>
      </section>

      <v-divider class="section-divider" />

      <section class="info-section">
        <div class="section-heading">
          <v-icon icon="mdi-home-assistant" />
          <h2>{{ t('info.domains.title') }}</h2>
        </div>

        <p class="section-text">
          {{ t('info.domains.description') }}
        </p>

        <div class="domain-list">
          <div
            v-for="group in domainGroups"
            :key="group.title"
            class="domain-row"
          >
            <div class="domain-title">
              {{ group.title }}
            </div>

            <div class="domain-chips">
              <v-chip
                v-for="domain in group.items"
                :key="domain"
                size="small"
                variant="tonal"
              >
                {{ domain }}
              </v-chip>
            </div>
          </div>
        </div>
      </section>

      <v-divider class="section-divider" />

      <section class="info-section">
        <div class="section-heading">
          <v-icon icon="mdi-palette" />
          <h2>{{ t('info.design.title') }}</h2>
        </div>

        <p class="section-text">
          {{ t('info.design.text') }}
        </p>
      </section>

      <v-divider class="section-divider" />

      <section class="info-section">
        <div class="section-heading">
          <v-icon icon="mdi-cog" />
          <h2>{{ t('info.spec.title') }}</h2>
        </div>

        <div class="spec-list">
          <div
            v-for="item in specs"
            :key="item.label"
            class="spec-row"
          >
            <span>{{ item.label }}</span>
            <strong>{{ item.value }}</strong>
          </div>
        </div>
      </section>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

type TextItem = {
  title: string
  text: string
}

type DomainGroup = {
  title: string
  items: string[]
}

type SpecItem = {
  label: string
  value: string
}

const { t, tm } = useI18n()

const benefits = computed<TextItem[]>(() => tm('info.benefits.items') as TextItem[])
const domainGroups = computed<DomainGroup[]>(() => tm('info.domains.groups') as DomainGroup[])
const specs = computed<SpecItem[]>(() => tm('info.spec.items') as SpecItem[])
</script>

<style scoped>
.info-page {
  min-height: calc(100vh - 76px);
  padding-top: 56px;
  padding-bottom: 72px;
}

.info-card {
  width: min(1080px, 100%);
  margin: 0 auto;
  padding: clamp(26px, 4vw, 48px);
  background:
    linear-gradient(145deg, rgba(17, 24, 34, 0.92), rgba(13, 19, 28, 0.94)),
    radial-gradient(circle at top right, rgba(255, 122, 26, 0.13), transparent 34%);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.info-hero {
  max-width: 920px;
}

.hero-chip {
  margin-bottom: 20px;
  font-weight: 900;
}

.info-hero h1 {
  margin: 0 0 22px;
  color: #f8fafc;
  font-size: clamp(38px, 6vw, 72px);
  font-weight: 950;
  line-height: 0.98;
  letter-spacing: -0.07em;
}

.hero-lead {
  max-width: 920px;
  margin: 0;
  color: #a8b4c3;
  font-size: 18px;
  line-height: 1.78;
}

.section-divider {
  margin: 34px 0;
  opacity: 0.5;
}

.info-section {
  max-width: 960px;
}

.section-heading {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 22px;
  color: #ff9a3d;
}

.section-heading h2 {
  margin: 0;
  color: #f8fafc;
  font-size: clamp(24px, 3vw, 34px);
  font-weight: 950;
  letter-spacing: -0.045em;
}

.section-text {
  max-width: 900px;
  margin: 0;
  color: #a8b4c3;
  font-size: 16px;
  line-height: 1.75;
}

.benefits-list {
  display: grid;
  gap: 18px;
}

.benefit-item {
  display: grid;
  grid-template-columns: 34px minmax(0, 1fr);
  gap: 14px;
}

.benefit-marker {
  display: grid;
  width: 34px;
  height: 34px;
  place-items: center;
  color: #102016;
  border-radius: 12px;
  background: linear-gradient(180deg, #4ade80, #22c55e);
  box-shadow: 0 10px 24px rgba(34, 197, 94, 0.18);
}

.benefit-content h3 {
  margin: 0 0 5px;
  color: #f8fafc;
  font-size: 16px;
  font-weight: 950;
}

.benefit-content p {
  margin: 0;
  color: #a8b4c3;
  font-size: 15px;
  line-height: 1.68;
}

.domain-list {
  display: grid;
  margin-top: 14px;
}

.domain-row {
  display: grid;
  grid-template-columns: minmax(180px, 260px) minmax(0, 1fr);
  gap: 14px;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}

.domain-row:last-child {
  border-bottom: none;
}

.domain-title {
  color: #f8fafc;
  font-size: 15px;
  font-weight: 950;
  line-height: 1.45;
}

.domain-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.spec-list {
  display: grid;
  max-width: 760px;
}

.spec-row {
  display: grid;
  grid-template-columns: minmax(160px, 260px) minmax(0, 1fr);
  gap: 18px;
  align-items: center;
  padding: 14px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}

.spec-row:last-child {
  border-bottom: none;
}

.spec-row span {
  color: #94a3b8;
  font-size: 15px;
}

.spec-row strong {
  color: #f8fafc;
  font-size: 15px;
  font-weight: 900;
}

@media (max-width: 760px) {
  .info-page {
    padding-top: 34px;
    padding-bottom: 48px;
  }

  .domain-row,
  .spec-row {
    grid-template-columns: 1fr;
    gap: 10px;
  }

  .benefit-item {
    grid-template-columns: 30px minmax(0, 1fr);
    gap: 12px;
  }

  .benefit-marker {
    width: 30px;
    height: 30px;
    border-radius: 10px;
  }
}
</style>
