import React, { useState, useEffect } from 'react';
import { athleteService, reportsService } from '../services/api';
import './Reports.css';

function Reports() {
  const [athletes, setAthletes] = useState([]);
  const [selectedAthlete, setSelectedAthlete] = useState(null);
  const [evolutionReport, setEvolutionReport] = useState(null);
  const [comparativeReport, setComparativeReport] = useState(null);
  const [developmentPlan, setDevelopmentPlan] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeReport, setActiveReport] = useState('evolution');

  useEffect(() => {
    loadAthletes();
  }, []);

  useEffect(() => {
    if (selectedAthlete) {
      loadReports();
    }
  }, [selectedAthlete, activeReport]);

  const loadAthletes = async () => {
    try {
      const response = await athleteService.getAll();
      setAthletes(response.data);
      if (response.data.length > 0) {
        setSelectedAthlete(response.data[0].id);
      }
    } catch (err) {
      console.error('Erro ao carregar atletas:', err);
    }
  };

  const loadReports = async () => {
    if (!selectedAthlete) return;
    
    setLoading(true);
    try {
      if (activeReport === 'evolution') {
        const response = await reportsService.getEvolution(selectedAthlete);
        setEvolutionReport(response.data);
      } else if (activeReport === 'comparative') {
        const response = await reportsService.getComparative(selectedAthlete);
        setComparativeReport(response.data);
      } else if (activeReport === 'development') {
        const response = await reportsService.getDevelopmentPlan(selectedAthlete);
        setDevelopmentPlan(response.data);
      }
    } catch (err) {
      console.error('Erro ao carregar relatório:', err);
    } finally {
      setLoading(false);
    }
  };

  if (athletes.length === 0) {
    return (
      <div className="reports">
        <div className="page-header">
          <h2>Relatórios Inteligentes</h2>
        </div>
        <div className="card">
          <p>Nenhum atleta cadastrado. Cadastre atletas para gerar relatórios.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="reports">
      <div className="page-header">
        <h2>Relatórios Inteligentes</h2>
        <p>Análises detalhadas e planos de desenvolvimento</p>
      </div>

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

      <div className="report-tabs">
        <button
          className={activeReport === 'evolution' ? 'active' : ''}
          onClick={() => setActiveReport('evolution')}
        >
          Evolução
        </button>
        <button
          className={activeReport === 'comparative' ? 'active' : ''}
          onClick={() => setActiveReport('comparative')}
        >
          Comparativo
        </button>
        <button
          className={activeReport === 'development' ? 'active' : ''}
          onClick={() => setActiveReport('development')}
        >
          Plano de Desenvolvimento
        </button>
      </div>

      {loading && <div className="loading">Gerando relatório...</div>}

      {activeReport === 'evolution' && evolutionReport && (
        <div className="report-content">
          {evolutionReport.message ? (
            <div className="card">
              <p>{evolutionReport.message}</p>
            </div>
          ) : (
            <>
              <div className="card">
                <h3>Relatório de Evolução</h3>
                <div className="report-period">
                  <p><strong>Período:</strong> {evolutionReport.analysis_period?.days} dias</p>
                  <p><strong>De:</strong> {new Date(evolutionReport.analysis_period?.start).toLocaleDateString('pt-BR')}</p>
                  <p><strong>Até:</strong> {new Date(evolutionReport.analysis_period?.end).toLocaleDateString('pt-BR')}</p>
                </div>
              </div>

              {evolutionReport.top_improvements && evolutionReport.top_improvements.length > 0 && (
                <div className="card">
                  <h3>Maiores Melhorias</h3>
                  <div className="improvements-list">
                    {evolutionReport.top_improvements.map((item, idx) => (
                      <div key={idx} className="improvement-item">
                        <span className="skill-name">{item.skill}</span>
                        <span className="improvement-value positive">
                          +{item.change.toFixed(2)} ({item.percentage > 0 ? '+' : ''}{item.percentage.toFixed(1)}%)
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {evolutionReport.top_regressions && evolutionReport.top_regressions.length > 0 && (
                <div className="card">
                  <h3>Principais Regressões</h3>
                  <div className="regressions-list">
                    {evolutionReport.top_regressions.map((item, idx) => (
                      <div key={idx} className="regression-item">
                        <span className="skill-name">{item.skill}</span>
                        <span className="regression-value negative">
                          {item.change.toFixed(2)} ({item.percentage.toFixed(1)}%)
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </>
          )}
        </div>
      )}

      {activeReport === 'comparative' && comparativeReport && (
        <div className="report-content">
          <div className="card">
            <h3>Relatório Comparativo</h3>
            <p><strong>Atleta:</strong> {comparativeReport.athlete_name}</p>
            <p><strong>Posição:</strong> {comparativeReport.athlete_position}</p>
          </div>

          {comparativeReport.detailed_comparison && (
            <div className="card">
              <h3>Comparação Detalhada</h3>
              {comparativeReport.detailed_comparison.map((comparison, idx) => (
                <div key={idx} className="comparison-card">
                  <h4>{comparison.legend_name}</h4>
                  <p><strong>Similaridade:</strong> {comparison.similarity}%</p>
                  <p><strong>Estilo:</strong> {comparison.playing_style}</p>
                  <div className="skill-comparison">
                    {Object.entries(comparison.skill_comparison || {}).slice(0, 5).map(([skill, data]) => (
                      <div key={skill} className="comparison-item">
                        <span className="skill-label">{skill.replace('_', ' ')}</span>
                        <div className="comparison-values">
                          <span>Atleta: {data.athlete}</span>
                          <span>Lenda: {data.legend}</span>
                          <span className={data.difference > 0 ? 'positive' : 'negative'}>
                            {data.difference > 0 ? '+' : ''}{data.difference}
                          </span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {activeReport === 'development' && developmentPlan && (
        <div className="report-content">
          <div className="card">
            <h3>Plano de Desenvolvimento Personalizado</h3>
            <div className="plan-summary">
              <p><strong>Atleta:</strong> {developmentPlan.athlete_name}</p>
              <p><strong>Posição Atual:</strong> {developmentPlan.current_position}</p>
              <p><strong>Posição Recomendada:</strong> {developmentPlan.recommended_position}</p>
              <p><strong>Nível Atual:</strong> {developmentPlan.current_level?.average_skill?.toFixed(2)}/10</p>
            </div>
          </div>

          {developmentPlan.projection && (
            <div className="card">
              <h3>Projeção de Potencial</h3>
              <div className="projection-grid">
                {Object.entries(developmentPlan.projection).map(([term, data]) => (
                  <div key={term} className="projection-card">
                    <h4>{data.period}</h4>
                    <div className="projection-target">
                      <strong>Meta:</strong> {data.target_avg}/10
                    </div>
                    <div className="projection-areas">
                      <strong>Foco:</strong>
                      <ul>
                        {data.focus_areas.slice(0, 3).map((area, idx) => (
                          <li key={idx}>{area}</li>
                        ))}
                      </ul>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {developmentPlan.reference_players && developmentPlan.reference_players.length > 0 && (
            <div className="card">
              <h3>Jogadores de Referência</h3>
              <div className="reference-players-list">
                {developmentPlan.reference_players.map((player, idx) => (
                  <div key={idx} className="reference-player-card">
                    <h4>{player.name}</h4>
                    <p><strong>Posição:</strong> {player.position}</p>
                    <p><strong>Similaridade:</strong> {player.similarity}%</p>
                    <div className="traits">
                      <strong>Características a Emular:</strong>
                      <ul>
                        {player.traits_to_emulate.map((trait, i) => (
                          <li key={i}>{trait}</li>
                        ))}
                      </ul>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default Reports;


