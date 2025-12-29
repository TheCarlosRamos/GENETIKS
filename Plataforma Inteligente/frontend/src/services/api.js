import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const athleteService = {
  getAll: () => api.get('/athletes/'),
  getById: (id) => api.get(`/athletes/${id}`),
  create: (data) => api.post('/athletes/', data),
  getClassification: (id) => api.get(`/athletes/${id}/classification`),
  recordPerformance: (id, technicalSkills, physicalMetrics = {}) =>
    api.post(`/athletes/${id}/performance`, {
      technical_skills: technicalSkills,
      physical_metrics: physicalMetrics,
    }),
  getPerformanceHistory: (id) => api.get(`/athletes/${id}/performance`),
  getMonitoring: (id) => api.get(`/athletes/${id}/monitoring`),
};

export const trainingService = {
  getRecommendations: (id) => api.get(`/training/${id}/recommendations`),
  getPlans: (id) => api.get(`/training/${id}/plans`),
  createPlan: (id, deficiency, plan) =>
    api.post(`/training/${id}/recommendations/${deficiency}`, plan),
};

export const matchService = {
  matchWithTeams: (id, teamStyle, system) =>
    api.get(`/match/${id}/teams`, { params: { team_style: teamStyle, system } }),
  matchWithPositions: (id) => api.get(`/match/${id}/positions`),
  matchWithTeammates: (id, position) =>
    api.get(`/match/${id}/teammates`, { params: { position } }),
};

export const reportsService = {
  getEvolution: (id, period) =>
    api.get(`/reports/${id}/evolution`, { params: { period } }),
  getComparative: (id) => api.get(`/reports/${id}/comparative`),
  getDevelopmentPlan: (id) => api.get(`/reports/${id}/development-plan`),
};

export default api;


