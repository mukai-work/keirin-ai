<script setup lang="ts">
interface Option {
  value: string;
  label: string;
}
const props = defineProps<{
  modelValue?: string;
  options: Option[];
  disabled?: boolean;
  name?: string;
}>();
const emit = defineEmits<{ 'update:modelValue': [string] }>();
function onChange(e: Event) {
  emit('update:modelValue', (e.target as HTMLSelectElement).value);
}
</script>
<template>
  <select
    :name="props.name"
    class="border rounded p-1"
    :value="props.modelValue"
    :disabled="props.disabled"
    @change="onChange"
  >
    <option v-for="o in props.options" :key="o.value" :value="o.value">{{ o.label }}</option>
  </select>
</template>
