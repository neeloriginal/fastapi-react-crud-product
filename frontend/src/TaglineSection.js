import React from 'react';
import './TaglineSection.css';

const TaglineSection = () => {
  return (
    <div className="tagline-card">
      <div className="tagline-content">
        <h3>📈 Track. Manage. Grow.</h3>
        <p>Streamline your inventory with smart product management that scales with your business.</p>
        <div className="company-badge">
          <span className="powered-by">Powered by</span>
          <a href='https://github.com/neeloriginal' target="_blank" rel="noopener noreferrer" className="company-link" >
          <span className="company-name">NeelOriginal</span> </a>
        </div>
      </div>
    </div>
  );
};

export default TaglineSection;
