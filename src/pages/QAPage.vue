<!-- src/pages/QAPage.vue -->

<template>
  <v-container class="qa-page" fluid>
    <section class="qa-hero">
      <h1>{{ t('qa.title') }}</h1>

      <p>
        {{ t('qa.description') }}
      </p>
    </section>

    <div class="qa-layout">
      <aside class="qa-sidebar">
        <div class="sidebar-title">
          {{ t('qa.sectionsTitle') }}
        </div>

        <v-list class="section-list" density="comfortable" nav>
          <v-list-item
            v-for="(group, index) in questionGroups"
            :key="group.title"
            :active="selectedGroupIndex === index"
            class="section-item"
            rounded="lg"
            @click="selectedGroupIndex = index"
          >
            <template #prepend>
              <v-icon :icon="group.icon" size="20" />
            </template>

            <v-list-item-title>
              {{ group.title }}
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </aside>

      <main class="qa-content">
        <div class="group-heading">
          <div class="group-icon">
            <v-icon :icon="selectedGroup.icon" size="22" />
          </div>

          <div class="group-heading-text">
            <h2>{{ selectedGroup.title }}</h2>
            <p>{{ selectedGroup.description }}</p>
          </div>
        </div>

        <v-expansion-panels
          v-model="openedPanel"
          class="qa-panels"
          variant="accordion"
        >
          <v-expansion-panel
            v-for="item in selectedGroup.items"
            :key="item.question"
            class="qa-panel"
          >
            <v-expansion-panel-title>
              <span class="question-title">
                {{ item.question }}
              </span>
            </v-expansion-panel-title>

            <v-expansion-panel-text>
              <div class="answer-text">
                {{ item.answer }}
              </div>
            </v-expansion-panel-text>
          </v-expansion-panel>
        </v-expansion-panels>
      </main>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'

type QuestionItem = {
  question: string
  answer: string
}

type QuestionGroup = {
  title: string
  description: string
  icon: string
  items: QuestionItem[]
}

const { t, tm } = useI18n()

const selectedGroupIndex = ref(0)
const openedPanel = ref<number | undefined>()

const questionGroups = computed<QuestionGroup[]>(() => {
  return tm('qa.groups') as QuestionGroup[]
})

const selectedGroup = computed<QuestionGroup>(() => {
  return questionGroups.value[selectedGroupIndex.value] ?? {
    title: '',
    description: '',
    icon: 'mdi-help-circle-outline',
    items: [],
  }
})

watch(selectedGroupIndex, () => {
  openedPanel.value = undefined
})
</script>

<style scoped>
.qa-page {
  min-height: calc(100vh - 76px);
  padding-top: 24px;
  padding-right: clamp(20px, 4vw, 72px);
  padding-bottom: 72px;
  padding-left: clamp(12px, 2vw, 28px);
}

.qa-hero {
  max-width: 860px;
  margin: 0 auto 38px;
  text-align: center;
}

.qa-hero h1 {
  margin: 0 0 10px;
  color: #f8fafc;
  font-size: clamp(34px, 5vw, 58px);
  font-weight: 950;
  line-height: 1;
  letter-spacing: -0.06em;
}

.qa-hero p {
  max-width: 720px;
  margin: 0 auto;
  color: #a8b4c3;
  font-size: 17px;
  line-height: 1.7;
}

/*
  Главное:
  - меню уходит левее;
  - контент занимает максимум ширины;
  - minmax(0, 1fr) не даёт ответам растягивать grid.
*/
.qa-layout {
  display: grid;
  grid-template-columns: 250px minmax(0, 1fr);
  gap: clamp(22px, 3vw, 42px);
  width: 100%;
  max-width: 1440px;
  margin: 0 auto;
  align-items: start;
}

.qa-sidebar {
  position: sticky;
  top: 18px;
  min-width: 0;
  padding-left: 0;
}

.sidebar-title {
  padding: 0 10px 12px;
  color: #64748b;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.section-list {
  background: transparent;
  padding: 0;
}

.section-item {
  min-height: 44px;
  margin-bottom: 6px;
  color: #94a3b8;
  background: transparent !important;
}

.section-item:last-child {
  margin-bottom: 0;
}

.section-item :deep(.v-list-item__overlay) {
  background: transparent !important;
}

.section-item :deep(.v-list-item-title) {
  font-size: 14px;
  font-weight: 850;
  line-height: 1.35;
  white-space: normal;
}

.section-item :deep(.v-icon) {
  color: #ff9a3d;
  opacity: 0.82;
}

.section-item.v-list-item--active {
  color: #f8fafc;
  background: rgba(255, 122, 26, 0.10) !important;
}

.section-item.v-list-item--active :deep(.v-icon) {
  opacity: 1;
}

.qa-content {
  width: 100%;
  min-width: 0;
  max-width: none;
}

.group-heading {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  width: 100%;
  min-width: 0;
  margin-bottom: 20px;
}

.group-icon {
  display: grid;
  width: 42px;
  height: 42px;
  flex: 0 0 auto;
  place-items: center;
  color: #111827;
  border-radius: 15px;
  background: linear-gradient(180deg, #ff9a3d, #f97316);
  box-shadow: 0 12px 28px rgba(249, 115, 22, 0.18);
}

.group-heading-text {
  min-width: 0;
}

.group-heading h2 {
  margin: 0 0 5px;
  color: #f8fafc;
  font-size: 24px;
  font-weight: 950;
  line-height: 1.15;
  letter-spacing: -0.04em;
}

.group-heading p {
  max-width: 860px;
  margin: 0;
  color: #94a3b8;
  font-size: 14px;
  line-height: 1.55;
}

/*
  Панели на всю ширину правой области.
  Без общего фона-карточки.
*/
.qa-panels {
  width: 100%;
  min-width: 0;
  gap: 10px;
}

.qa-panel {
  width: 100%;
  min-width: 0;
}

/*
  Убираем “карточный” фон.
  Оставляем только тонкое разделение, чтобы вопросы читались.
*/
:deep(.v-expansion-panel) {
  width: 100%;
  min-width: 0;
  overflow: hidden;
  background: transparent !important;
  border: 1px solid rgba(255, 255, 255, 0.075);
  border-radius: 14px !important;
  box-shadow: none !important;
}

:deep(.v-expansion-panel::after) {
  display: none;
}

:deep(.v-expansion-panel-title) {
  min-height: 58px;
  width: 100%;
  min-width: 0;
  color: #f8fafc;
  font-size: 15px;
  font-weight: 900;
  line-height: 1.45;
  background: rgba(255, 255, 255, 0.08) !important;
}

:deep(.v-expansion-panel-title:hover) {
  background: rgba(255, 255, 255, 0.025) !important;
}

.question-title {
  display: block;
  width: 100%;
  min-width: 0;
  max-width: 100%;
  white-space: normal;
  overflow-wrap: anywhere;
  word-break: normal;
}

.answer-text {
  width: 100%;
  max-width: 100%;
  min-width: 0;
  white-space: pre-line;
  overflow-wrap: anywhere;
  word-break: normal;
}

@media (max-width: 960px) {
  .qa-page {
    padding-right: 20px;
    padding-left: 20px;
  }

  .qa-layout {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .qa-sidebar {
    position: static;
  }

  .section-list {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding-bottom: 4px;
  }

  .section-item {
    flex: 0 0 auto;
    min-width: max-content;
    margin-bottom: 0;
  }

  .section-item :deep(.v-list-item-title) {
    white-space: nowrap;
  }
}

@media (max-width: 720px) {
  .qa-page {
    padding-top: 20px;
    padding-bottom: 48px;
  }

  .group-heading {
    gap: 12px;
  }

  .group-icon {
    width: 38px;
    height: 38px;
    border-radius: 13px;
  }

  .group-heading h2 {
    font-size: 21px;
  }

  :deep(.v-expansion-panel-title) {
    min-height: 54px;
    font-size: 14px;
  }
}
</style>
