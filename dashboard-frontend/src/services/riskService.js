import api from "./api";

export const riskService = {
  list: () => api.get("/risk"),
  get: (roadId) => api.get(`/risk/${encodeURIComponent(roadId)}`),
};

