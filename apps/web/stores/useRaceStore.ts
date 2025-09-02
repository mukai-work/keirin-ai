import { defineStore } from 'pinia';
import { todayJst } from '@/utils/date';
import { useApi } from '@/composables/useApi';
import type { Venue, Race, PredictionResult } from '@/types/domain';

export const useRaceStore = defineStore('race', {
  state: () => ({
    date: todayJst(),
    venues: [] as Venue[],
    venueId: undefined as string | undefined,
    races: [] as Race[],
    raceId: undefined as string | undefined,
    prediction: undefined as PredictionResult | undefined,
    loading: false,
    error: undefined as string | undefined,
  }),
  actions: {
    async init() {
      this.loading = true;
      this.error = undefined;
      try {
        const api = useApi();
        this.venues = await api.getVenues();
        this.venueId = this.venues[0]?.id;
        await this.loadRaces();
      } catch (e: unknown) {
        this.error = e instanceof Error ? e.message : String(e);
      } finally {
        this.loading = false;
      }
    },
    async loadRaces() {
      if (!this.date || !this.venueId) {
        this.races = [];
        this.raceId = undefined;
        return;
      }
      this.loading = true;
      this.error = undefined;
      try {
        const api = useApi();
        this.races = await api.getRaces({ date: this.date, venueId: this.venueId });
        this.raceId = this.races[0]?.id;
      } catch (e: unknown) {
        this.error = e instanceof Error ? e.message : String(e);
        this.races = [];
        this.raceId = undefined;
      } finally {
        this.loading = false;
      }
    },
    async predict() {
      if (!this.date || !this.venueId || !this.raceId) return;
      this.loading = true;
      this.error = undefined;
      try {
        const api = useApi();
        this.prediction = await api.postPredict({
          date: this.date,
          venueId: this.venueId,
          raceId: this.raceId,
        });
      } catch (e: unknown) {
        this.error = e instanceof Error ? e.message : String(e);
      } finally {
        this.loading = false;
      }
    },
    async setDate(d: string) {
      this.date = d;
      await this.loadRaces();
    },
    async setVenue(id: string) {
      this.venueId = id;
      await this.loadRaces();
    },
    setRace(id: string) {
      this.raceId = id;
    },
  },
});
