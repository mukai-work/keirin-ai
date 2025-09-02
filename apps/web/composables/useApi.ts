import type {
  Venue,
  Race,
  PredictionResult,
  Rider,
  RiderPoint,
  RecommendedTicket,
  RecommendedLine,
} from '@/types/domain';

function mockVenues(): Venue[] {
  return Array.from({ length: 5 }, (_, i) => ({ id: `v${i + 1}`, name: `会場${i + 1}` }));
}

function mockRaces(params: { venueId: string }): Race[] {
  return Array.from({ length: 12 }, (_, i) => ({
    id: `${params.venueId}-r${i + 1}`,
    venueId: params.venueId,
    number: i + 1,
    name: `レース${i + 1}`,
  }));
}

function mockPrediction(p: { raceId: string }): PredictionResult {
  const riders: Rider[] = Array.from({ length: 7 + Math.floor(Math.random() * 3) }, (_, i) => ({
    id: `r${i + 1}`,
    name: `選手${i + 1}`,
  }));
  const riderPoints: RiderPoint[] = riders.map((r) => ({
    riderId: r.id,
    point: 40 + Math.floor(Math.random() * 56),
  }));
  const recommendedLines: RecommendedLine[] = Array.from({ length: 2 + Math.floor(Math.random() * 2) }, (_, i) => ({
    name: `ライン${i + 1}`,
    members: riders.slice(i * 3, i * 3 + 3).map((r) => r.name),
    confidence: Math.random(),
  }));
  const ticketTypes: RecommendedTicket['type'][] = ['単勝', '車連', '三連単'];
  const recommendedTickets: RecommendedTicket[] = ticketTypes.map((t) => ({
    type: t,
    selection: '1-2-3',
    confidence: Math.random(),
  }));
  return {
    raceId: p.raceId,
    riderPoints,
    recommendedTickets,
    recommendedLines,
  };
}

export function useApi() {
  if (process.env.MOCK === '1') {
    const venues = mockVenues();
    return {
      getVenues: async () => venues,
      getRaces: async (p: { date: string; venueId?: string }) =>
        p.venueId ? mockRaces({ venueId: p.venueId }) : [],
      postPredict: async (p: { date: string; venueId: string; raceId: string }) =>
        mockPrediction({ raceId: p.raceId }),
    };
  }
  const base = useRuntimeConfig().public.apiBaseUrl;
  const getVenues = () => $fetch<Venue[]>(`${base}/venues`);
  const getRaces = (p: { date: string; venueId?: string }) =>
    $fetch<Race[]>(`${base}/races`, { query: p });
  const postPredict = (p: { date: string; venueId: string; raceId: string }) =>
    $fetch<PredictionResult>(`${base}/predict`, { method: 'POST', body: p });
  return { getVenues, getRaces, postPredict };
}
