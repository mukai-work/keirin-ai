<script setup lang="ts">
import { computed } from 'vue';
import type { RiderPoint, Rider } from '@/types/domain';
const props = defineProps<{ points: RiderPoint[]; riders: Rider[] }>();
const rows = computed(() =>
  [...props.points].sort((a, b) => b.point - a.point || a.riderId.localeCompare(b.riderId))
);
const ridersMap = computed(() =>
  Object.fromEntries(props.riders.map((r) => [r.id, r.name])) as Record<string, string>
);
const stats = computed(() => {
  const pts = props.points.map((p) => p.point);
  const total = pts.length;
  const max = pts.length ? Math.max(...pts) : 0;
  const min = pts.length ? Math.min(...pts) : 0;
  const avg = pts.length ? pts.reduce((a, b) => a + b, 0) / pts.length : 0;
  return { total, max, min, avg };
});
</script>
<template>
  <table class="min-w-full border-collapse">
    <caption class="sr-only">選手ポイント</caption>
    <thead>
      <tr>
        <th scope="col" class="text-left">選手</th>
        <th scope="col" class="text-right">ポイント</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="p in rows" :key="p.riderId">
        <td>{{ ridersMap[p.riderId] || p.riderId }}</td>
        <td class="text-right">{{ p.point }}</td>
      </tr>
    </tbody>
    <tfoot>
      <tr><td>件数</td><td class="text-right">{{ stats.total }}</td></tr>
      <tr><td>最大</td><td class="text-right">{{ stats.max }}</td></tr>
      <tr><td>最小</td><td class="text-right">{{ stats.min }}</td></tr>
      <tr><td>平均</td><td class="text-right">{{ stats.avg.toFixed(1) }}</td></tr>
    </tfoot>
  </table>
</template>
