import { describe, it, expect, beforeEach } from 'vitest';
import { setActivePinia, createPinia } from 'pinia';
import { useRaceStore } from '@/stores/useRaceStore';

process.env.MOCK = '1';

describe('useRaceStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia());
  });

  it('init fetches venues and selects first', async () => {
    const store = useRaceStore();
    await store.init();
    expect(store.venues.length).toBeGreaterThan(0);
    expect(store.venueId).toBe(store.venues[0]?.id);
  });

  it('setDate loads races', async () => {
    const store = useRaceStore();
    await store.init();
    const racesBefore = store.races.length;
    await store.setDate(store.date);
    expect(store.races.length).toBeGreaterThan(0);
    expect(store.races.length).toBe(racesBefore); // same because mock
  });

  it('predict sets prediction', async () => {
    const store = useRaceStore();
    await store.init();
    await store.predict();
    expect(store.prediction).toBeTruthy();
  });
});
