<script setup lang="ts">
import { computed } from 'vue';
import type { RecommendedLine } from '@/types/domain';
const props = defineProps<{ lines: RecommendedLine[] }>();
const list = computed(() => [...props.lines].sort((a, b) => b.confidence - a.confidence));
</script>
<template>
  <ul>
    <li v-for="l in list" :key="l.name" class="mb-2">
      <div class="font-bold">
        {{ l.name }} <span class="ml-2">{{ Math.round(l.confidence * 100) }}%</span>
      </div>
      <div class="flex flex-wrap gap-1 mt-1">
        <span
          v-for="m in l.members"
          :key="m"
          class="px-2 py-1 bg-gray-200 rounded-full"
          >{{ m }}</span
        >
      </div>
    </li>
  </ul>
</template>
