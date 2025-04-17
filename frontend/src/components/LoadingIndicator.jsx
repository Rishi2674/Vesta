// src/components/LoadingIndicator.jsx
import React from 'react';

const LoadingIndicator = () => {
  return (
    <div className="loading-indicator">
      <div className="loading-spinner">
        <div className="dot"></div>
        <div className="dot"></div>
        <div className="dot"></div>
      </div>
      <div className="loading-text">Searching the web...</div>
    </div>
  );
};

export default LoadingIndicator;