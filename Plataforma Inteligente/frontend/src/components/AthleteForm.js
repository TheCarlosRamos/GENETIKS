import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { athleteService } from '../services/api';
import './AthleteForm.css';

const INITIAL_SKILLS = {
  velocidade: 5,
  resistencia: 5,
  forca: 5,
  agilidade: 5,
  passe: 5,
  drible: 5,
  finalizacao: 5,
  chute: 5,
  jogo_aereo: 5,
  visao_de_jogo: 5,
  posicionamento: 5,
  marcacao: 5,
  interceptacao: 5,
  reflexos: 5,
  jogo_com_os_pes: 5,
  disciplina_tatica: 5,
};

function AthleteForm() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    nationality: '',
    height: '',
    weight: '',
    body_type: '',
    dominant_foot: '',
    primary_position: '',
    secondary_position: '',
  });
  const [skills, setSkills] = useState(INITIAL_SKILLS);
  const [deficiencies, setDeficiencies] = useState([]);
  const [newDeficiency, setNewDeficiency] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSkillChange = (skill, value) => {
    setSkills((prev) => ({ ...prev, [skill]: parseFloat(value) }));
  };

  const addDeficiency = () => {
    if (newDeficiency.trim() && !deficiencies.includes(newDeficiency.trim())) {
      setDeficiencies([...deficiencies, newDeficiency.trim()]);
      setNewDeficiency('');
    }
  };

  const removeDeficiency = (deficiency) => {
    setDeficiencies(deficiencies.filter((d) => d !== deficiency));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const athleteData = {
        ...formData,
        age: parseInt(formData.age),
        height: formData.height ? parseFloat(formData.height) : null,
        weight: formData.weight ? parseFloat(formData.weight) : null,
        technical_skills: skills,
        deficiencies: deficiencies,
      };

      const response = await athleteService.create(athleteData);
      navigate(`/atleta/${response.data.id}`);
    } catch (err) {
      setError('Erro ao cadastrar atleta: ' + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="athlete-form">
      <div className="page-header">
        <h2>Cadastrar Novo Atleta</h2>
        <p>Preencha os dados do atleta para realizar a classificação inteligente</p>
      </div>

      {error && <div className="error">{error}</div>}

      <form onSubmit={handleSubmit} className="card">
        <h3>Dados Pessoais</h3>
        <div className="form-row">
          <div className="form-group">
            <label>Nome *</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Idade *</label>
            <input
              type="number"
              name="age"
              value={formData.age}
              onChange={handleInputChange}
              min="10"
              max="50"
              required
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Nacionalidade</label>
            <input
              type="text"
              name="nationality"
              value={formData.nationality}
              onChange={handleInputChange}
            />
          </div>
          <div className="form-group">
            <label>Altura (cm)</label>
            <input
              type="number"
              name="height"
              value={formData.height}
              onChange={handleInputChange}
              min="140"
              max="220"
            />
          </div>
          <div className="form-group">
            <label>Peso (kg)</label>
            <input
              type="number"
              name="weight"
              value={formData.weight}
              onChange={handleInputChange}
              min="40"
              max="120"
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Biotipo</label>
            <select
              name="body_type"
              value={formData.body_type}
              onChange={handleInputChange}
            >
              <option value="">Selecione...</option>
              <option value="Ectomorfo">Ectomorfo</option>
              <option value="Mesomorfo">Mesomorfo</option>
              <option value="Endomorfo">Endomorfo</option>
            </select>
          </div>
          <div className="form-group">
            <label>Pé Dominante</label>
            <select
              name="dominant_foot"
              value={formData.dominant_foot}
              onChange={handleInputChange}
            >
              <option value="">Selecione...</option>
              <option value="Destro">Destro</option>
              <option value="Canhoto">Canhoto</option>
              <option value="Ambidestro">Ambidestro</option>
            </select>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Posição Primária</label>
            <select
              name="primary_position"
              value={formData.primary_position}
              onChange={handleInputChange}
            >
              <option value="">Selecione...</option>
              <option value="Goleiro">Goleiro</option>
              <option value="Zagueiro">Zagueiro</option>
              <option value="Lateral">Lateral</option>
              <option value="Volante">Volante</option>
              <option value="Meia">Meia</option>
              <option value="Atacante">Atacante</option>
            </select>
          </div>
          <div className="form-group">
            <label>Posição Secundária</label>
            <select
              name="secondary_position"
              value={formData.secondary_position}
              onChange={handleInputChange}
            >
              <option value="">Selecione...</option>
              <option value="Goleiro">Goleiro</option>
              <option value="Zagueiro">Zagueiro</option>
              <option value="Lateral">Lateral</option>
              <option value="Volante">Volante</option>
              <option value="Meia">Meia</option>
              <option value="Atacante">Atacante</option>
            </select>
          </div>
        </div>

        <h3>Habilidades Técnicas (1-10)</h3>
        <div className="skills-section">
          {Object.entries(skills).map(([skill, value]) => (
            <div key={skill} className="skill-slider">
              <label>{skill.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</label>
              <input
                type="range"
                min="1"
                max="10"
                step="0.5"
                value={value}
                onChange={(e) => handleSkillChange(skill, e.target.value)}
              />
              <span className="skill-value">{value}</span>
            </div>
          ))}
        </div>

        <h3>Deficiências / Áreas de Melhoria</h3>
        <div className="deficiencies-section">
          <div className="deficiency-input">
            <input
              type="text"
              value={newDeficiency}
              onChange={(e) => setNewDeficiency(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && (e.preventDefault(), addDeficiency())}
              placeholder="Ex: Jogo aéreo, Finalização, etc."
            />
            <button type="button" onClick={addDeficiency} className="btn btn-secondary">
              Adicionar
            </button>
          </div>
          <div className="deficiencies-list">
            {deficiencies.map((deficiency) => (
              <span key={deficiency} className="deficiency-tag">
                {deficiency}
                <button
                  type="button"
                  onClick={() => removeDeficiency(deficiency)}
                  className="remove-btn"
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        </div>

        <div className="form-actions">
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? 'Cadastrando...' : 'Cadastrar e Classificar'}
          </button>
        </div>
      </form>
    </div>
  );
}

export default AthleteForm;


