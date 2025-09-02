export type Venue = { id: string; name: string; prefecture?: string };
export type Race = {
  id: string;
  venueId: string;
  number: number; // レース番号
  name: string; // レース名
  startTime?: string; // ISO
};
export type Rider = {
  id: string;
  name: string;
  grade?: string; // S1 等
  line?: string; // 所属ライン識別
};
export type RiderPoint = { riderId: string; point: number };
export type RecommendedTicket = {
  type:
    | '単勝'
    | '複勝'
    | 'ワイド'
    | '枠連'
    | '車連'
    | '車単'
    | '三連複'
    | '三連単';
  selection: string; // 例 "1-3-5"
  confidence: number; // 0..1
  expectedValue?: number; // 期待値（任意）
};
export type RecommendedLine = { name: string; members: string[]; confidence: number };
export type PredictionResult = {
  raceId: string;
  riderPoints: RiderPoint[];
  recommendedTickets: RecommendedTicket[];
  recommendedLines: RecommendedLine[];
  modelVersion?: string;
};
export type RaceFilters = { date: string; venueId?: string; raceId?: string };
