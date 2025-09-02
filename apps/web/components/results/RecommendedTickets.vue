<script setup lang="ts">
import { ref, computed } from 'vue';
import type { RecommendedTicket } from '@/types/domain';
const props = defineProps<{ tickets: RecommendedTicket[] }>();
const filterType = ref<'all' | RecommendedTicket['type']>('all');
const types = computed(() => Array.from(new Set(props.tickets.map((t) => t.type))));
const list = computed(() => {
  const arr = [...props.tickets].sort((a, b) => b.confidence - a.confidence);
  return filterType.value === 'all' ? arr : arr.filter((t) => t.type === filterType.value);
});
</script>
<template>
  <div>
    <div class="mb-2">
      <label for="ticket-filter" class="mr-2">種別</label>
      <select id="ticket-filter" v-model="filterType" class="border rounded p-1">
        <option value="all">すべて</option>
        <option v-for="t in types" :key="t" :value="t">{{ t }}</option>
      </select>
    </div>
    <ul>
      <li v-for="t in list" :key="t.type + t.selection" class="mb-1">
        <span class="font-bold">{{ t.type }}</span> {{ t.selection }}
        <span class="ml-2">{{ Math.round(t.confidence * 100) }}%</span>
        <span v-if="t.expectedValue !== undefined" class="ml-2">EV: {{ t.expectedValue }}</span>
      </li>
    </ul>
  </div>
</template>
