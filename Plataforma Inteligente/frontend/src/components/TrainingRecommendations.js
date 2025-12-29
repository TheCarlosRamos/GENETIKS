import React, { useState, useEffect } from 'react';
import { trainingService } from '../services/api';
import './TrainingRecommendations.css';

function TrainingRecommendations({ athleteId }) {
  const [recommendations, setRecommendations] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadRecommendations();
  }, [athleteId]);

  const loadRecommendations = async () => {
    try {
      setLoading(true);
      const response = await trainingService.getRecommendations(athleteId);
      setRecommendations(response.data);
      setError(null);
    } catch (err) {
      setError('Erro ao carregar recomendações: ' + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Carregando recomendações...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  if (!recommendations || !recommendations.recommendations || recommendations.recommendations.length === 0) {
    return (
      <div className="card">
        <p>Nenhuma recomendação de treinamento disponível no momento.</p>
      </div>
    );
  }

  return (
    <div>
      <div className="card">
        <h3>Áreas de Desenvolvimento Identificadas</h3>
        <div className="development-areas">
          {recommendations.development_areas.map((area, idx) => (
            <span key={idx} className="area-tag">{area}</span>
          ))}
        </div>
      </div>

      {recommendations.recommendations.map((rec, idx) => (
        <div key={idx} className="card recommendation-card">
          <h3>{rec.deficiency}</h3>
          
          <div className="recommendation-section">
            <h4>Exercícios</h4>
            <ul className="exercise-list">
              {rec.exercises.map((exercise, i) => (
                <li key={i}>{exercise}</li>
              ))}
            </ul>
          </div>

          <div className="recommendation-section">
            <h4>Drills de Treinamento</h4>
            <ul className="drill-list">
              {rec.drills.map((drill, i) => (
                <li key={i}>{drill}</li>
              ))}
            </ul>
          </div>

          {rec.reference_players && rec.reference_players.length > 0 && (
            <div className="recommendation-section">
              <h4>Jogadores de Referência</h4>
              <div className="reference-players">
                {rec.reference_players.map((player, i) => (
                  <span key={i} className="player-tag">{player}</span>
                ))}
              </div>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

export default TrainingRecommendations;


