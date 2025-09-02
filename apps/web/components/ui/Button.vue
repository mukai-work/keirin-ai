<script setup lang="ts">
const props = withDefaults(
  defineProps<{ disabled?: boolean; busy?: boolean; type?: 'button' | 'submit'; name?: string }>(),
  { type: 'button', name: undefined }
);
</script>
<template>
  <button
    :type="props.type"
    :aria-busy="props.busy ? 'true' : 'false'"
    :aria-disabled="props.disabled ? 'true' : 'false'"
    :disabled="props.disabled || props.busy"
    :name="props.name"
    class="px-4 py-2 rounded bg-blue-600 text-white disabled:opacity-50"
  >
    <slot />
  </button>
</template>
