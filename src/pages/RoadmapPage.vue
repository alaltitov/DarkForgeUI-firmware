<!-- src/pages/RoadmapPage.vue -->

<template>
  <v-container class="roadmap-page">
    <section class="roadmap-hero">
      <h1>{{ t('roadmap.title') }}</h1>

      <p>
        {{ t('roadmap.description') }}
      </p>
    </section>

    <v-card class="roadmap-shell">
      <v-timeline
        align="start"
        side="end"
        class="roadmap-timeline"
      >
        <v-timeline-item
          v-for="item in roadmapItems"
          :key="item.period"
          :dot-color="item.color"
          size="small"
        >
          <template #opposite>
            <div :class="`roadmap-period text-${item.color}`">
              {{ item.period }}
            </div>
          </template>

          <div class="roadmap-content">
            <div class="roadmap-content-header">
              <h2 :class="`text-${item.color}`">
                {{ item.title }}
              </h2>

              <v-chip
                :color="item.color"
                variant="tonal"
                size="small"
                class="status-chip"
              >
                {{ item.status }}
              </v-chip>
            </div>

            <p>
              {{ item.text }}
            </p>
          </div>
        </v-timeline-item>
      </v-timeline>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

type RoadmapItem = {
  period: string
  title: string
  text: string
  status: string
  color: string
}

const { t, tm } = useI18n()

const roadmapItems = computed<RoadmapItem[]>(() => tm('roadmap.items') as RoadmapItem[])
</script>

<style scoped>
.roadmap-page {
  min-height: calc(100vh - 76px);
  padding-top: 16px;
  padding-bottom: 72px;
}

.roadmap-hero {
  max-width: 820px;
  margin: 0 auto 16px;
  text-align: center;
}

.roadmap-hero h1 {
  margin: 0 0 0;
  color: #f8fafc;
  font-size: clamp(34px, 5vw, 58px);
  font-weight: 950;
  letter-spacing: -0.06em;
}

.roadmap-hero p {
  max-width: 680px;
  margin: 0 auto;
  color: #a8b4c3;
  font-size: 17px;
  line-height: 1.7;
}

.roadmap-shell {
  width: min(980px, 100%);
  margin: 0 auto;
  padding: clamp(18px, 3vw, 34px);
  background:
    linear-gradient(145deg, rgba(17, 24, 34, 0.92), rgba(13, 19, 28, 0.94)),
    radial-gradient(circle at top right, rgba(255, 122, 26, 0.12), transparent 34%);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.roadmap-timeline {
  width: 100%;
}

.roadmap-period {
  max-width: 220px;
  padding-top: 2px;
  font-size: 14px;
  font-weight: 950;
  line-height: 1.45;
  text-align: right;
}

.roadmap-content {
  width: 100%;
  max-width: 620px;
  padding-bottom: 28px;
}

.roadmap-content-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 10px;
}

.roadmap-content h2 {
  margin: -4px 0 0;
  font-size: 22px;
  font-weight: 950;
  line-height: 1.2;
  letter-spacing: -0.04em;
}

.status-chip {
  flex: 0 0 auto;
  font-weight: 900;
}

.roadmap-content p {
  max-width: 620px;
  margin: 0;
  color: #a8b4c3;
  font-size: 15px;
  line-height: 1.72;
}

/*
  Лёгкая стабилизация ширины правой части без жёсткого переписывания grid Vuetify.
*/
:deep(.v-timeline-item__body) {
  width: 100%;
}

:deep(.v-timeline-item__opposite) {
  min-width: 220px;
}

/*
  На мобильных датировку переносим внутрь потока:
  штатная opposite-колонка скрывается, чтобы ничего не ломалось.
*/
@media (max-width: 760px) {
  .roadmap-shell {
    padding: 20px 16px;
  }

  :deep(.v-timeline-item__opposite) {
    display: none;
  }

  .roadmap-content {
    max-width: 100%;
  }

  .roadmap-content::before {
    content: '';
    display: none;
  }

  .roadmap-content-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }

  .roadmap-content h2 {
    font-size: 20px;
  }
}
</style>
