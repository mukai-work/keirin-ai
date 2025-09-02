<script setup lang="ts">
import { computed } from 'vue';
import Select from '@/components/ui/Select.vue';
import type { Race } from '@/types/domain';
const props = defineProps<{ modelValue?: string; options: Race[] }>();
const emit = defineEmits<{ 'update:modelValue': [string] }>();
const id = 'race-select';
const items = computed(() =>
  props.options.map((r) => ({ value: r.id, label: `${r.number}R｜${r.name}` }))
);
</script>
<template>
  <label :for="id" class="flex flex-col">
    <span class="mb-1">レース</span>
    <Select
      :name="id"
      :options="items"
      :model-value="props.modelValue"
      @update:model-value="emit('update:modelValue', $event)"
    />
  </label>
</template>
