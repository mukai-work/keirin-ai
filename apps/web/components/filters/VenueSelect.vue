<script setup lang="ts">
import { computed } from 'vue';
import Select from '@/components/ui/Select.vue';
import type { Venue } from '@/types/domain';
const props = defineProps<{ modelValue?: string; options: Venue[] }>();
const emit = defineEmits<{ 'update:modelValue': [string] }>();
const id = 'venue-select';
const items = computed(() => props.options.map((v) => ({ value: v.id, label: v.name })));
</script>
<template>
  <label :for="id" class="flex flex-col">
    <span class="mb-1">競輪場</span>
    <Select
      :name="id"
      :options="items"
      :model-value="props.modelValue"
      @update:model-value="emit('update:modelValue', $event)"
    />
  </label>
</template>
