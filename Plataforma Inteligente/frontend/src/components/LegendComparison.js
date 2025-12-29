import React from 'react';
import './LegendComparison.css';

function LegendComparison({ legends }) {
  if (!legends || legends.length === 0) {
    return (
      <div className="card">
        <p>Nenhuma comparação disponível</p>
      </div>
    );
  }

  return (
    <div className="card">
      <h3>Jogadores Históricos Similares</h3>
      <div className="legends-grid">
        {legends.map((legend, idx) => (
          <div key={idx} className="legend-card">
            <div className="legend-header">
              <h4>{legend.name}</h4>
              <span className="similarity-badge">
                {legend.similarity}% similar
              </span>
            </div>
            <div className="legend-info">
              <p><strong>Posição:</strong> {legend.position}</p>
              <p><strong>Era:</strong> {legend.era}</p>
              <p><strong>Estilo:</strong> {legend.playing_style}</p>
            </div>
            {legend.distinctive_traits && (
              <div className="legend-traits">
                <strong>Características:</strong>
                <ul>
                  {legend.distinctive_traits.map((trait, i) => (
                    <li key={i}>{trait}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default LegendComparison;


