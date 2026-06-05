<!-- src/pages/HomePage.vue -->

<template>
  <v-container class="home-page">
    <v-row align="center" class="hero-row">
      <v-col cols="12" md="6">
        <section class="hero-copy">
          <h1>{{ t('home.title') }}</h1>
          <div class="slogan">
            {{ t('home.slogan') }}
          </div>
          <p class="hero-description">
            {{ t('home.description') }}
          </p>

          <div class="hero-actions">
            <v-btn
              color="primary"
              size="large"
              variant="flat"
              rounded="lg"
              class="text-black font-weight-bold text-uppercase"
              to="/beta"
            >
              {{ t('home.primaryAction') }}
            </v-btn>

            <v-btn
              size="large"
              variant="tonal"
              rounded="lg"
              class="font-weight-bold text-uppercase"
              to="/info"
            >
              {{ t('home.secondaryAction') }}
            </v-btn>
          </div>
        </section>
      </v-col>

      <v-col cols="12" md="6">
        <v-card class="feature-panel">
          <div class="panel-glow" />

          <div class="device-preview">
            <div class="preview-dashboard">
              <div class="widget widget-light wide">
                <div class="widget-fill light-fill" />

                <div class="widget-left">
                  <div class="widget-icon light-icon">
                    <v-icon size="18">mdi-lightbulb</v-icon>
                  </div>

                  <div class="widget-text">
                    <div class="widget-title">{{ t('home.widgets.light.title') }}</div>
                    <div class="widget-subtitle">{{ t('home.widgets.light.subtitle') }}</div>
                  </div>
                </div>

                <div class="widget-value">72%</div>
              </div>

              <div class="widget widget-media wide">
                <div class="widget-fill media-fill" />

                <div class="widget-left">
                  <div class="widget-icon media-icon">
                    <v-icon size="18">mdi-music-note</v-icon>
                  </div>

                  <div class="widget-text">
                    <div class="widget-title">{{ t('home.widgets.media.title') }}</div>
                    <div class="widget-subtitle">{{ t('home.widgets.media.subtitle') }}</div>
                  </div>
                </div>

                <div class="widget-actions">
                  <div class="round-btn"><v-icon size="14">mdi-skip-previous</v-icon></div>
                  <div class="round-btn"><v-icon size="14">mdi-skip-next</v-icon></div>
                  <div class="round-btn primary-blue"><v-icon size="14">mdi-play</v-icon></div>
                </div>
              </div>

              <div class="widget widget-climate wide">
                <div class="widget-left">
                  <div class="widget-icon climate-icon">
                    <v-icon size="18">mdi-fire</v-icon>
                  </div>

                  <div class="widget-text">
                    <div class="widget-title">{{ t('home.widgets.climate.title') }}</div>
                    <div class="widget-subtitle">{{ t('home.widgets.climate.subtitle') }}</div>
                  </div>
                </div>

                <div class="temp-box">
                  <span>−</span>
                  <strong>24°</strong>
                  <span>+</span>
                </div>
              </div>

              <div class="widget widget-alarm wide">
                <div class="widget-left">
                  <div class="widget-icon alarm-icon">
                    <v-icon size="18">mdi-shield-off</v-icon>
                  </div>

                  <div class="widget-text">
                    <div class="widget-title">{{ t('home.widgets.alarm.title') }}</div>
                    <div class="widget-subtitle">{{ t('home.widgets.alarm.subtitle') }}</div>
                  </div>
                </div>

                <div class="widget-actions">
                  <div class="round-btn"><v-icon size="14">mdi-shield-home</v-icon></div>
                  <div class="round-btn"><v-icon size="14">mdi-shield-lock</v-icon></div>
                </div>
              </div>

              <div class="widget widget-cover wide">
                <div class="widget-fill cover-fill" />

                <div class="widget-left">
                  <div class="widget-icon cover-icon">
                    <v-icon size="18">mdi-window-shutter-open</v-icon>
                  </div>

                  <div class="widget-text">
                    <div class="widget-title">{{ t('home.widgets.cover.title') }}</div>
                    <div class="widget-subtitle">{{ t('home.widgets.cover.subtitle') }}</div>
                  </div>
                </div>

                <div class="widget-actions">
                  <div class="round-btn"><v-icon size="14">mdi-arrow-up</v-icon></div>
                  <div class="round-btn"><v-icon size="14">mdi-stop</v-icon></div>
                  <div class="round-btn"><v-icon size="14">mdi-arrow-down</v-icon></div>
                </div>
              </div>

              <div class="widget widget-vacuum">
                <div class="widget-fill vacuum-fill" />

                <div class="widget-left">
                  <div class="widget-icon vacuum-icon">
                    <v-icon size="18">mdi-robot-vacuum</v-icon>
                  </div>

                  <div class="widget-text">
                    <div class="widget-title">{{ t('home.widgets.vacuum.title') }}</div>
                    <div class="widget-subtitle">{{ t('home.widgets.vacuum.subtitle') }}</div>
                  </div>
                </div>
              </div>

              <div class="widget widget-sensor">
                <div class="widget-fill sensor-fill" />

                <div class="widget-left">
                  <div class="widget-icon sensor-icon">
                    <v-icon size="18">mdi-thermometer</v-icon>
                  </div>

                  <div class="widget-text">
                    <div class="widget-title">{{ t('home.widgets.temperature.title') }}</div>
                    <div class="widget-subtitle">{{ t('home.widgets.temperature.subtitle') }}</div>
                  </div>
                </div>
              </div>

              <div class="widget widget-sensor">
                <div class="widget-fill sensor-fill" />

                <div class="widget-left">
                  <div class="widget-icon sensor-icon">
                    <v-icon size="18">mdi-water-percent</v-icon>
                  </div>

                  <div class="widget-text">
                    <div class="widget-title">{{ t('home.widgets.humidity.title') }}</div>
                    <div class="widget-subtitle">{{ t('home.widgets.humidity.subtitle') }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<style scoped>
.home-page {
  padding-top: 72px;
  padding-bottom: 72px;
}

.hero-row {
  min-height: calc(100vh - 160px);
}

.hero-copy {
  max-width: 640px;
}

.slogan {
  max-width: 560px;
  margin-bottom: 22px;
  color: #ff9a3d;
  font-size: 17px;
  font-weight: 900;
  line-height: 1.45;
  letter-spacing: -0.02em;
}

h1 {
  margin: 0 0 22px;
  color: #f8fafc;
  font-size: clamp(44px, 6vw, 82px);
  font-weight: 950;
  line-height: 0.94;
  letter-spacing: -0.075em;
}

.hero-description {
  max-width: 600px;
  margin: 0;
  color: #a8b4c3;
  font-size: 18px;
  line-height: 1.72;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 34px;
}

.feature-panel {
  position: relative;
  overflow: hidden;
  padding: 18px;
  background:
    linear-gradient(145deg, rgba(17, 24, 39, 0.96), rgba(13, 19, 28, 0.96)),
    radial-gradient(circle at top right, rgba(255, 122, 26, 0.18), transparent 30%);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.panel-glow {
  position: absolute;
  inset: auto -80px -120px auto;
  width: 260px;
  height: 260px;
  border-radius: 999px;
  background: rgba(255, 122, 26, 0.20);
  filter: blur(60px);
}

.device-preview {
  position: relative;
  padding: 24px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 28px;
  background:
    linear-gradient(180deg, rgba(7, 11, 16, 0.88), rgba(14, 21, 31, 0.96)),
    radial-gradient(circle at top, rgba(96, 165, 250, 0.12), transparent 36%);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
}

.preview-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 18px;
  margin-bottom: 22px;
}

.preview-title {
  color: #f8fafc;
  font-size: 22px;
  font-weight: 950;
  letter-spacing: -0.04em;
}

.preview-subtitle {
  color: #94a3b8;
  font-size: 13px;
  margin-top: 4px;
}

.preview-dashboard {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.widget {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-width: 0;
  padding: 4px 10px;
  border-radius: 14px;
  box-sizing: border-box;
  border: 1px solid rgba(255, 255, 255, 0.055);
}

.widget.wide {
  grid-column: span 2;
}

.widget-fill {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.widget-left {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  min-width: 0;
  gap: 10px;
}

.widget-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
  color: #151515;
}

.widget-text {
  min-width: 0;
}

.widget-title {
  overflow: hidden;
  color: #ffffff;
  font-size: 11px;
  font-weight: 800;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.widget-subtitle {
  overflow: hidden;
  margin-top: 2px;
  font-size: 10px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.widget-value {
  position: relative;
  z-index: 1;
  margin-left: 8px;
  color: #ffd08a;
  font-size: 11px;
  font-weight: 800;
}

.widget-actions {
  position: relative;
  z-index: 1;
  display: flex;
  gap: 6px;
  margin-left: 8px;
}

.round-btn {
  display: flex;
  width: 24px;
  height: 24px;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: white;
  background: rgba(255, 255, 255, 0.18);
}

.primary-blue {
  color: #0e223d;
  background: #58a6ff;
}

.widget-light {
  background: #26211a;
}

.light-fill {
  inset: 0 auto 0 0;
  width: 72%;
  background: rgba(249, 115, 22, 0.24);
}

.light-icon {
  width: 34px;
  height: 34px;
  border-radius: 30%;
  background: #ff9a3d;
  color: #3a1607;
}

.widget-light .widget-subtitle {
  color: #ffc28d;
}

.widget-media {
  background: #1e1f23;
}

.media-fill {
  inset: 0 auto 0 0;
  width: 32%;
  background: rgba(88, 166, 255, 0.22);
}

.media-icon {
  width: 34px;
  height: 34px;
  border-radius: 30%;
  background: #58a6ff;
  color: #0e223d;
}

.widget-media .widget-subtitle {
  color: #a9ccf8;
}

.widget-climate {
  background: #2a201c;
}

.climate-icon {
  width: 34px;
  height: 34px;
  border-radius: 30%;
  background: #f09a62;
  color: #3a1607;
}

.widget-climate .widget-subtitle {
  color: #f2b08b;
}

.temp-box {
  position: relative;
  z-index: 1;
  display: flex;
  height: 38px;
  min-width: 92px;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  padding: 0 8px;
  border-radius: 16px;
  color: white;
  background: rgba(255, 255, 255, 0.08);
}

.temp-box span {
  display: grid;
  width: 22px;
  height: 22px;
  place-items: center;
  border-radius: 50%;
  background: #373a41;
}

.temp-box strong {
  font-size: 12px;
}

.widget-alarm {
  background: #1f3025;
}

.alarm-icon {
  width: 34px;
  height: 34px;
  border-radius: 30%;
  background: #6dd28b;
  color: #11261a;
}

.widget-alarm .widget-subtitle {
  color: #9ee0b4;
}

.widget-cover {
  background: rgba(102, 187, 106, 0.30);
}

.cover-fill {
  background: rgba(255, 255, 255, 0.06);
}

.cover-icon {
  width: 34px;
  height: 34px;
  border-radius: 30%;
  background: #66bb6a;
  color: white;
}

.widget-cover .widget-subtitle {
  color: #dadde4;
}

.widget-vacuum {
  background: rgba(76, 175, 80, 0.30);
}

.vacuum-fill {
  background: rgba(255, 255, 255, 0.06);
}

.vacuum-icon {
  width: 34px;
  height: 34px;
  border-radius: 30%;
  background: #4caf50;
  color: #151515;
}

.widget-vacuum .widget-subtitle {
  color: #dadde4;
}

.widget-sensor {
  background: rgba(38, 166, 154, 0.30);
}

.sensor-fill {
  background: rgba(255, 255, 255, 0.06);
}

.sensor-icon {
  width: 34px;
  height: 34px;
  border-radius: 30%;
  background: #26a69a;
  color: #06251f;
}

.widget-sensor .widget-subtitle {
  color: #b9fff5;
}

@media (max-width: 960px) {
  .home-page {
    padding-top: 40px;
  }

  .hero-row {
    min-height: auto;
  }

  .feature-panel {
    min-height: auto;
  }

  .device-preview {
    min-height: 500px;
  }
}

@media (max-width: 520px) {
  .preview-dashboard {
    grid-template-columns: 1fr;
  }

  .widget.wide {
    grid-column: span 1;
  }

  .feature-panel {
    padding: 18px;
  }

  .device-preview {
    padding: 18px;
  }
}
</style>
