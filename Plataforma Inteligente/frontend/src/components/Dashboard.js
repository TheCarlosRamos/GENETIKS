import React, { useState, useEffect } from 'react';
import { athleteService } from '../services/api';
import { Link } from 'react-router-dom';
import './Dashboard.css';

function Dashboard() {
  const [athletes, setAthletes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedAthlete, setSelectedAthlete] = useState(null);
  const [monitoring, setMonitoring] = useState(null);

  useEffect(() => {
    loadAthletes();
  }, []);

  useEffect(() => {
    if (selectedAthlete) {
      loadMonitoring(selectedAthlete);
    }
  }, [selectedAthlete]);

  const loadAthletes = async () => {
    try {
      const response = await athleteService.getAll();
      setAthletes(response.data);
      if (response.data.length > 0) {
        setSelectedAthlete(response.data[0].id);
      }
    } catch (err) {
      console.error('Erro ao carregar atletas:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadMonitoring = async (athleteId) => {
    try {
      const response = await athleteService.getMonitoring(athleteId);
      setMonitoring(response.data);
    } catch (err) {
      console.error('Erro ao carregar monitoramento:', err);
    }
  };

  if (loading) {
    return <div className="loading">Carregando dashboard...</div>;
  }

  return (
    <div className="dashboard">
      <div className="page-header">
        <h2>Dashboard de Monitoramento</h2>
        <p>Acompanhe a evolução e desempenho dos atletas</p>
      </div>

      {athletes.length === 0 ? (
        <div className="card">
          <p>Nenhum atleta cadastrado. <Link to="/cadastro">Cadastre um atleta</Link> para começar.</p>
        </div>
      ) : (
        <>
          <div className="card">
            <label>Selecione um atleta:</label>
            <select
              value={selectedAthlete || ''}
              onChange={(e) => setSelectedAthlete(parseInt(e.target.value))}
              className="athlete-select"
            >
              {athletes.map((athlete) => (
                <option key={athlete.id} value={athlete.id}>
                  {athlete.name} - {athlete.primary_position || 'N/A'}
                </option>
              ))}
            </select>
          </div>

          {monitoring && (
            <div>
              <div className="card">
                <h3>Resumo do Atleta</h3>
                <div className="summary-grid">
                  <div>
                    <strong>Nome:</strong> {monitoring.athlete.name}
                  </div>
                  <div>
                    <strong>Posição:</strong> {monitoring.athlete.position || 'N/A'}
                  </div>
                  {monitoring.classification && (
                    <>
                      <div>
                        <strong>Posição Recomendada:</strong>{' '}
                        {monitoring.classification.recommended_position}
                      </div>
                      <div>
                        <strong>Compatibilidade:</strong>{' '}
                        {Math.round(monitoring.classification.compatibility_score * 100)}%
                      </div>
                    </>
                  )}
                </div>
              </div>

              {monitoring.alerts && monitoring.alerts.length > 0 && (
                <div className="card">
                  <h3>Alertas</h3>
                  {monitoring.alerts.map((alert, idx) => (
                    <div key={idx} className={`alert alert-${alert.type === 'stagnation' ? 'warning' : 'info'}`}>
                      {alert.message}
                    </div>
                  ))}
                </div>
              )}

              {monitoring.evolution && Object.keys(monitoring.evolution).length > 0 && (
                <div className="card">
                  <h3>Evolução Recente</h3>
                  <div className="evolution-summary">
                    {Object.entries(monitoring.evolution)
                      .slice(0, 6)
                      .map(([skill, data]) => (
                        <div key={skill} className="evolution-item-small">
                          <div className="skill-name-small">
                            {skill.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                          </div>
                          <div className={`change-small ${data.change > 0 ? 'positive' : data.change < 0 ? 'negative' : 'neutral'}`}>
                            {data.change > 0 ? '+' : ''}{data.change.toFixed(1)}
                          </div>
                        </div>
                      ))}
                  </div>
                </div>
              )}

              <div className="card">
                <Link
                  to={`/atleta/${selectedAthlete}`}
                  className="btn btn-primary"
                >
                  Ver Detalhes Completos
                </Link>
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default Dashboard;


