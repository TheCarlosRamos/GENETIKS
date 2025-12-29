import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';

function PerformanceEvolution({ monitoring }) {
  if (!monitoring || !monitoring.performance_history || monitoring.performance_history.length === 0) {
    return (
      <div className="card">
        <p>Dados de evolução insuficientes. Registre novos desempenhos para visualizar a evolução.</p>
      </div>
    );
  }

  // Prepara dados para o gráfico
  const chartData = monitoring.performance_history.map((record, idx) => {
    const dataPoint = {
      date: new Date(record.date).toLocaleDateString('pt-BR'),
      index: idx,
    };
    
    // Adiciona algumas habilidades principais ao gráfico
    const skills = record.skills || {};
    const mainSkills = ['velocidade', 'passe', 'drible', 'finalizacao', 'marcacao'];
    
    mainSkills.forEach(skill => {
      if (skills[skill] !== undefined) {
        dataPoint[skill.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())] = skills[skill];
      }
    });
    
    return dataPoint;
  });

  const colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe'];

  return (
    <div>
      {monitoring.alerts && monitoring.alerts.length > 0 && (
        <div className="card">
          <h3>Alertas</h3>
          {monitoring.alerts.map((alert, idx) => (
            <div key={idx} className={`alert alert-${alert.type === 'stagnation' ? 'warning' : 'info'}`}>
              <strong>{alert.type === 'stagnation' ? '⚠️ Estagnação' : 'ℹ️ Aviso'}:</strong> {alert.message}
            </div>
          ))}
        </div>
      )}

      {monitoring.evolution && Object.keys(monitoring.evolution).length > 0 && (
        <div className="card">
          <h3>Evolução por Habilidade</h3>
          <div className="evolution-grid">
            {Object.entries(monitoring.evolution).map(([skill, data]) => (
              <div key={skill} className="evolution-item">
                <div className="evolution-header">
                  <span className="skill-name">{skill.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</span>
                  <span className={`evolution-change ${data.change > 0 ? 'positive' : data.change < 0 ? 'negative' : 'neutral'}`}>
                    {data.change > 0 ? '+' : ''}{data.change.toFixed(2)} ({data.percentage > 0 ? '+' : ''}{data.percentage.toFixed(1)}%)
                  </span>
                </div>
                <div className="evolution-values">
                  <span>Inicial: {data.old}</span>
                  <span>Atual: {data.new}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="card">
        <h3>Gráfico de Evolução</h3>
        <div style={{ width: '100%', height: 400, marginTop: 20 }}>
          <ResponsiveContainer>
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis domain={[0, 10]} />
              <Tooltip />
              <Legend />
              {chartData.length > 0 && Object.keys(chartData[0])
                .filter(key => key !== 'date' && key !== 'index')
                .map((skill, idx) => (
                  <Line
                    key={skill}
                    type="monotone"
                    dataKey={skill}
                    stroke={colors[idx % colors.length]}
                    strokeWidth={2}
                  />
                ))}
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

export default PerformanceEvolution;


