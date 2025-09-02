import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils';
import RiderPointTable from '@/components/results/RiderPointTable.vue';

describe('RiderPointTable', () => {
  it('sorts by point desc then id asc', () => {
    const points = [
      { riderId: 'b', point: 50 },
      { riderId: 'a', point: 50 },
      { riderId: 'c', point: 70 },
    ];
    const wrapper = mount(RiderPointTable, { props: { points, riders: [] } });
    const rows = wrapper.findAll('tbody tr').map((tr) => tr.text());
    expect(rows[0]).toContain('c');
    expect(rows[1]).toContain('a');
    expect(rows[2]).toContain('b');
  });
});
