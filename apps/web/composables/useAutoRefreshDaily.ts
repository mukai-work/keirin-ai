import { onMounted } from 'vue';
import { useRaceStore } from '@/stores/useRaceStore';
import { todayJst } from '@/utils/date';

function msUntilNextRefresh(): number {
  const now = new Date();
  const jstNow = new Date(now.toLocaleString('en-US', { timeZone: 'Asia/Tokyo' }));
  const next = new Date(jstNow);
  next.setHours(0, 5, 0, 0);
  if (jstNow >= next) {
    next.setDate(next.getDate() + 1);
  }
  return next.getTime() - jstNow.getTime();
}

export function useAutoRefreshDaily() {
  const store = useRaceStore();
  onMounted(() => {
    setTimeout(() => {
      store.setDate(todayJst());
      store.loadRaces();
      setInterval(() => {
        store.setDate(todayJst());
        store.loadRaces();
      }, 24 * 60 * 60 * 1000);
    }, msUntilNextRefresh());
  });
}
