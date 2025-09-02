import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils';
import Select from '@/components/ui/Select.vue';

describe('Select', () => {
  it('v-model works', async () => {
    const wrapper = mount(Select, {
      props: {
        options: [
          { value: '1', label: 'one' },
          { value: '2', label: 'two' },
        ],
        modelValue: '1',
      },
    });
    await wrapper.find('select').setValue('2');
    expect(wrapper.emitted()['update:modelValue']?.[0]).toEqual(['2']);
  });
});
