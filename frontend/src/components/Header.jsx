// src/components/Header.jsx
import React from 'react';
import { FaHome } from 'react-icons/fa';

const Header = () => {
  return (
    <header className="header">
      <div className="header-container">
        <div className="logo-container">
          <FaHome className="logo-icon" />
          <h1 className="logo-text">Vesta</h1>
        </div>
        <div className="subtitle">Your Real Estate Assistant</div>
      </div>
    </header>
  );
};

export default Header;