import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { athleteService, trainingService } from '../services/api';
import SkillRadar from './SkillRadar';
import LegendComparison from './LegendComparison';
import TrainingRecommendations from './TrainingRecommendations';
import PerformanceEvolution from './PerformanceEvolution';
import './AthleteDetail.css';

function AthleteDetail() {
  const { id } = useParams();
  const [athlete, setAthlete] = useState(null);
  const [classification, setClassification] = useState(null);
  const [monitoring, setMonitoring] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('overview');

  useEffect(() => {
    loadAthleteData();
  }, [id]);

  const loadAthleteData = async () => {
    try {
      setLoading(true);
      const [athleteRes, monitoringRes] = await Promise.all([
        athleteService.getById(id),
        athleteService.getMonitoring(id),
      ]);
      setAthlete(athleteRes.data);
      setClassification(athleteRes.data.classification_data);
      setMonitoring(monitoringRes.data);
      setError(null);
    } catch (err) {
      setError('Erro ao carregar dados do atleta: ' + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Carregando dados do atleta...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  if (!athlete) {
    return <div className="error">Atleta não encontrado</div>;
  }

  return (
    <div className="athlete-detail">
      <div className="page-header">
        <Link to="/" className="back-link">← Voltar</Link>
        <h2>{athlete.name}</h2>
        <p>{athlete.primary_position || 'Posição não definida'}</p>
      </div>

      <div className="athlete-info-card card">
        <div className="info-grid">
          <div>
            <strong>Idade:</strong> {athlete.age} anos
          </div>
          {athlete.nationality && (
            <div>
              <strong>Nacionalidade:</strong> {athlete.nationality}
            </div>
          )}
          {athlete.height && (
            <div>
              <strong>Altura:</strong> {athlete.height} cm
            </div>
          )}
          {athlete.weight && (
            <div>
              <strong>Peso:</strong> {athlete.weight} kg
            </div>
          )}
          {athlete.body_type && (
            <div>
              <strong>Biotipo:</strong> {athlete.body_type}
            </div>
          )}
          {athlete.dominant_foot && (
            <div>
              <strong>Pé Dominante:</strong> {athlete.dominant_foot}
            </div>
          )}
        </div>
      </div>

      <div className="tabs">
        <button
          className={activeTab === 'overview' ? 'active' : ''}
          onClick={() => setActiveTab('overview')}
        >
          Visão Geral
        </button>
        <button
          className={activeTab === 'classification' ? 'active' : ''}
          onClick={() => setActiveTab('classification')}
        >
          Classificação
        </button>
        <button
          className={activeTab === 'training' ? 'active' : ''}
          onClick={() => setActiveTab('training')}
        >
          Treinamento
        </button>
        <button
          className={activeTab === 'evolution' ? 'active' : ''}
          onClick={() => setActiveTab('evolution')}
        >
          Evolução
        </button>
      </div>

      <div className="tab-content">
        {activeTab === 'overview' && (
          <div>
            {classification && (
              <div className="card">
                <h3>Classificação</h3>
                <div className="classification-summary">
                  <div className="recommended-position">
                    <strong>Posição Recomendada:</strong>{' '}
                    <span className="highlight">{classification.recommended_position}</span>
                  </div>
                  <div className="compatibility-score">
                    <strong>Score de Compatibilidade:</strong>{' '}
                    {Math.round(classification.compatibility_score * 100)}%
                  </div>
                </div>
                {athlete.technical_skills && (
                  <SkillRadar skills={athlete.technical_skills} />
                )}
              </div>
            )}

            {classification && classification.strengths && (
              <div className="card">
                <h3>Principais Forças</h3>
                <ul className="strengths-list">
                  {classification.strengths.map((strength, idx) => (
                    <li key={idx}>{strength}</li>
                  ))}
                </ul>
              </div>
            )}

            {classification && classification.development_areas && (
              <div className="card">
                <h3>Áreas de Desenvolvimento</h3>
                <ul className="development-list">
                  {classification.development_areas.map((area, idx) => (
                    <li key={idx}>{area}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}

        {activeTab === 'classification' && classification && (
          <div>
            <LegendComparison legends={classification.similar_legends} />
            <div className="card">
              <h3>Scores por Posição</h3>
              <div className="position-scores">
                {Object.entries(classification.position_scores || {}).map(([pos, score]) => (
                  <div key={pos} className="position-score-item">
                    <span className="position-name">{pos}</span>
                    <div className="score-bar">
                      <div
                        className="score-fill"
                        style={{ width: `${score * 100}%` }}
                      />
                      <span className="score-value">{Math.round(score * 100)}%</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'training' && (
          <TrainingRecommendations athleteId={id} />
        )}

        {activeTab === 'evolution' && monitoring && (
          <PerformanceEvolution monitoring={monitoring} />
        )}
      </div>
    </div>
  );
}

export default AthleteDetail;


