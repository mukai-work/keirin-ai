<script setup lang="ts">
import { onMounted } from 'vue';
import Card from '@/components/ui/Card.vue';
import Button from '@/components/ui/Button.vue';
import DatePicker from '@/components/filters/DatePicker.vue';
import VenueSelect from '@/components/filters/VenueSelect.vue';
import RaceSelect from '@/components/filters/RaceSelect.vue';
import RiderPointTable from '@/components/results/RiderPointTable.vue';
import RecommendedTickets from '@/components/results/RecommendedTickets.vue';
import RecommendedLines from '@/components/results/RecommendedLines.vue';
import { useRaceStore } from '@/stores/useRaceStore';
import { useAutoRefreshDaily } from '@/composables/useAutoRefreshDaily';

const store = useRaceStore();

onMounted(async () => {
  await store.init();
  useAutoRefreshDaily();
});
</script>

<template>
  <div class="p-4 space-y-4">
    <header class="text-center">
      <h1 class="text-2xl font-bold">Keirin AI</h1>
      <p>本日: {{ store.date }}</p>
    </header>
    <Card>
      <div class="flex flex-col md:flex-row gap-4">
        <DatePicker :model-value="store.date" @update:model-value="store.setDate" />
        <VenueSelect :model-value="store.venueId" :options="store.venues" @update:model-value="store.setVenue" />
        <RaceSelect :model-value="store.raceId" :options="store.races" @update:model-value="store.setRace" />
      </div>
    </Card>
    <div class="flex items-center gap-4">
      <Button
        :disabled="!store.raceId || store.loading"
        :busy="store.loading"
        @click="store.predict"
      >予想開始</Button>
      <div v-if="store.loading">ロード中...</div>
      <div v-else-if="store.error" class="text-red-500">{{ store.error }}</div>
    </div>
    <div v-if="store.races.length === 0 && !store.loading" class="text-center">
      選択条件に合致するレースがありません
    </div>
    <div v-if="store.prediction" class="space-y-4">
      <Card>
        <RiderPointTable
          :points="store.prediction.riderPoints"
          :riders="store.prediction.riderPoints.map((p) => ({ id: p.riderId, name: p.riderId }))"
        />
      </Card>
      <Card>
        <RecommendedTickets :tickets="store.prediction.recommendedTickets" />
      </Card>
      <Card>
        <RecommendedLines :lines="store.prediction.recommendedLines" />
      </Card>
    </div>
  </div>
</template>
