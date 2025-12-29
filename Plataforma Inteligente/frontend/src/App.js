import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import AthleteList from './components/AthleteList';
import AthleteForm from './components/AthleteForm';
import AthleteDetail from './components/AthleteDetail';
import Dashboard from './components/Dashboard';
import MatchAnalysis from './components/MatchAnalysis';
import Reports from './components/Reports';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <div className="container">
            <h1 className="logo">⚽ Plataforma Inteligente de Atletas</h1>
            <ul className="nav-links">
              <li><Link to="/">Atletas</Link></li>
              <li><Link to="/cadastro">Cadastrar</Link></li>
              <li><Link to="/dashboard">Dashboard</Link></li>
              <li><Link to="/match">Match</Link></li>
              <li><Link to="/reports">Relatórios</Link></li>
            </ul>
          </div>
        </nav>
        
        <div className="container">
          <Routes>
            <Route path="/" element={<AthleteList />} />
            <Route path="/cadastro" element={<AthleteForm />} />
            <Route path="/atleta/:id" element={<AthleteDetail />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/match" element={<MatchAnalysis />} />
            <Route path="/reports" element={<Reports />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;


