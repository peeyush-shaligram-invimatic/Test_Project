import React, { useState } from 'react';
import './PetClicker.css';

const PetClicker = () => {
  const [clicks, setClicks] = useState(0);

  const handleClick = () => setClicks(clicks + 1);

  const getPetMood = () => {
    if (clicks < 5) return '🐶';       // Puppy
    if (clicks < 15) return '😄';      // Happy face
    if (clicks < 25) return '😎';      // Cool dog
    if (clicks < 50) return '🐕‍🦺';    // Trained dog
    return '🦄';                        // Evolved form
  };

  const getMoodText = () => {
    if (clicks < 5) return "Pet me more!";
    if (clicks < 15) return "I'm feeling good 🐾";
    if (clicks < 25) return "You're my best friend 🦴";
    if (clicks < 50) return "I know tricks now!";
    return "I've ascended to Pet Godhood 👑";
  };

  return (
    <div className="pet-container">
      <h2>🐾 Virtual Pet Clicker</h2>
      <div className="pet-display" onClick={handleClick}>
        <span className="pet-emoji">{getPetMood()}</span>
      </div>
      <p>Clicks: {clicks}</p>
      <p>{getMoodText()}</p>
      <button onClick={() => setClicks(0)}>🔁 Reset</button>
    </div>
  );
};

export default PetClicker;
