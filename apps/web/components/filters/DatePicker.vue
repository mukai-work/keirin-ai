<script setup lang="ts">
const props = defineProps<{ modelValue: string }>();
const emit = defineEmits<{ 'update:modelValue': [string] }>();
const id = 'date-picker';
</script>
<template>
  <label :for="id" class="flex flex-col">
    <span class="mb-1">日付</span>
    <input
      :id="id"
      type="date"
      class="border rounded p-1"
      :value="props.modelValue"
      @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    >
  </label>
</template>
