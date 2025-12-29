import React from 'react';
import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
} from 'recharts';

function SkillRadar({ skills }) {
  const data = Object.entries(skills).map(([skill, value]) => ({
    skill: skill.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase()),
    value: value,
    fullMark: 10,
  }));

  return (
    <div style={{ width: '100%', height: 400, marginTop: 20 }}>
      <ResponsiveContainer>
        <RadarChart data={data}>
          <PolarGrid />
          <PolarAngleAxis dataKey="skill" />
          <PolarRadiusAxis angle={90} domain={[0, 10]} />
          <Radar
            name="Habilidades"
            dataKey="value"
            stroke="#667eea"
            fill="#667eea"
            fillOpacity={0.6}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default SkillRadar;


