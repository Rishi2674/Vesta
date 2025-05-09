// src/App.js
import React from 'react';
import Header from './components/Header';
import ChatInterface from './components/ChatInterface';
import './styles/styles.css';

function App() {
  return (
    <div className="app-container">
      <Header />
      <ChatInterface />
    </div>
  );
}

export default App;