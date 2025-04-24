import { useEffect, useState } from 'react';
import './App.css';
import PetClicker from './PetClicker';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('http://localhost:5000/')
      .then(res => res.text())
      .then(setMessage)
      .catch(() => setMessage("Error connecting to backend."));
  }, []);

  return (
    <div className="App">
      <h1>{message}</h1>
      {/* Pet Clicker Game */}
      <PetClicker />
    </div>
  );
}

export default App;
