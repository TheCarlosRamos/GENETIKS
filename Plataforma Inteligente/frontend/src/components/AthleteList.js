import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { athleteService } from '../services/api';
import './AthleteList.css';

function AthleteList() {
  const [athletes, setAthletes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadAthletes();
  }, []);

  const loadAthletes = async () => {
    try {
      setLoading(true);
      const response = await athleteService.getAll();
      setAthletes(response.data);
      setError(null);
    } catch (err) {
      setError('Erro ao carregar atletas: ' + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Carregando atletas...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="athlete-list">
      <div className="page-header">
        <h2>Atletas Cadastrados</h2>
        <p>Lista completa de atletas na plataforma</p>
      </div>

      <Link to="/cadastro" className="btn btn-primary">
        + Cadastrar Novo Atleta
      </Link>

      {athletes.length === 0 ? (
        <div className="card">
          <p>Nenhum atleta cadastrado ainda. Comece cadastrando um novo atleta!</p>
        </div>
      ) : (
        <div className="athletes-grid">
          {athletes.map((athlete) => (
            <Link
              key={athlete.id}
              to={`/atleta/${athlete.id}`}
              className="athlete-card"
            >
              <div className="athlete-card-header">
                <h3>{athlete.name}</h3>
                <span className="badge">{athlete.primary_position || 'N/A'}</span>
              </div>
              <div className="athlete-card-body">
                <p><strong>Idade:</strong> {athlete.age} anos</p>
                {athlete.nationality && (
                  <p><strong>Nacionalidade:</strong> {athlete.nationality}</p>
                )}
                {athlete.height && (
                  <p><strong>Altura:</strong> {athlete.height} cm</p>
                )}
                {athlete.classification_data && (
                  <div className="compatibility-score">
                    <strong>Compatibilidade:</strong>{' '}
                    {Math.round(athlete.classification_data.compatibility_score * 100)}%
                  </div>
                )}
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}

export default AthleteList;


