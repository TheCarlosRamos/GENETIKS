import React, { useState, useEffect } from 'react';
import { athleteService, matchService } from '../services/api';
import './MatchAnalysis.css';

function MatchAnalysis() {
  const [athletes, setAthletes] = useState([]);
  const [selectedAthlete, setSelectedAthlete] = useState(null);
  const [teamCompatibility, setTeamCompatibility] = useState(null);
  const [positionCompatibility, setPositionCompatibility] = useState(null);
  const [teammates, setTeammates] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadAthletes();
  }, []);

  useEffect(() => {
    if (selectedAthlete) {
      loadMatchData();
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
    }
  };

  const loadMatchData = async () => {
    if (!selectedAthlete) return;
    
    setLoading(true);
    try {
      const [teamRes, positionRes, teammatesRes] = await Promise.all([
        matchService.matchWithTeams(selectedAthlete),
        matchService.matchWithPositions(selectedAthlete),
        matchService.matchWithTeammates(selectedAthlete),
      ]);
      setTeamCompatibility(teamRes.data);
      setPositionCompatibility(positionRes.data);
      setTeammates(teammatesRes.data);
    } catch (err) {
      console.error('Erro ao carregar dados de match:', err);
    } finally {
      setLoading(false);
    }
  };

  if (athletes.length === 0) {
    return (
      <div className="match-analysis">
        <div className="page-header">
          <h2>Análise de Compatibilidade</h2>
        </div>
        <div className="card">
          <p>Nenhum atleta cadastrado. Cadastre atletas para realizar análises de compatibilidade.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="match-analysis">
      <div className="page-header">
        <h2>Análise de Compatibilidade</h2>
        <p>Analise a compatibilidade de atletas com times, posições e companheiros</p>
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

      {loading && <div className="loading">Analisando compatibilidade...</div>}

      {positionCompatibility && (
        <div className="card">
          <h3>Compatibilidade com Posições</h3>
          <div className="position-compatibility">
            {Object.entries(positionCompatibility.position_scores || {})
              .sort((a, b) => b[1] - a[1])
              .map(([position, score]) => (
                <div key={position} className="compatibility-item">
                  <div className="compatibility-header">
                    <span className="position-name">{position}</span>
                    <span className="compatibility-score">{score}%</span>
                  </div>
                  <div className="compatibility-bar">
                    <div
                      className="compatibility-fill"
                      style={{ width: `${score}%` }}
                    />
                  </div>
                </div>
              ))}
          </div>
          {positionCompatibility.recommended_position && (
            <div className="recommendation-box">
              <strong>Posição Recomendada:</strong>{' '}
              {positionCompatibility.recommended_position}
            </div>
          )}
        </div>
      )}

      {teamCompatibility && (
        <div className="card">
          <h3>Compatibilidade com Estilos de Time</h3>
          <div className="team-compatibility">
            {Object.entries(teamCompatibility.compatibility || {})
              .sort((a, b) => b[1].score - a[1].score)
              .map(([style, data]) => (
                <div key={style} className="team-style-card">
                  <div className="style-header">
                    <h4>{style.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</h4>
                    <span className="style-score">{data.score}%</span>
                  </div>
                  <p className="style-description">{data.description}</p>
                  <div className="required-skills">
                    <strong>Habilidades necessárias:</strong>
                    <div className="skills-tags">
                      {data.required_skills.map((skill, idx) => (
                        <span key={idx} className="skill-tag">
                          {skill.replace('_', ' ')}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              ))}
          </div>
        </div>
      )}

      {teammates && teammates.compatible_teammates && teammates.compatible_teammates.length > 0 && (
        <div className="card">
          <h3>Companheiros Compatíveis</h3>
          <div className="teammates-grid">
            {teammates.compatible_teammates.map((teammate) => (
              <div key={teammate.athlete_id} className="teammate-card">
                <div className="teammate-header">
                  <h4>{teammate.name}</h4>
                  <span className="complementarity-score">
                    {teammate.complementarity_score}%
                  </span>
                </div>
                <p><strong>Posição:</strong> {teammate.position}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default MatchAnalysis;


