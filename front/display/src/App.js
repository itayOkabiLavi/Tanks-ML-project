import React from 'react';
import Button from 'react-bootstrap/Button'
import 'bootstrap/dist/css/bootstrap.min.css'

import logo from './logo.svg';
import './App.css';
import TrainingZone from './components/TrainingZone';


function App() {
  const homepage_req = (e) => {
    e.preventDefault();
    console.log("Homepage clicked");
    fetch('/homepage', {method: 'get', url: 'http://localhost:3000'}).then(res => 
      {
        console.log('answered');
      })
  }
  const training_req = (e) => {
    e.preventDefault();
    console.log("Training clicked");
    fetch('/training', {method: 'get', url: 'http://localhost:3000'}).then(res => 
      {
        console.log('answered');
      })
  }
  const battle_req = (e) => {
    e.preventDefault();
    console.log("Battle clicked");
    fetch('/battle', {method: 'get', url: 'http://localhost:3000'}).then(res => 
      {
        console.log('answered');
      })
  }
  return (
    <div className="App">
      <div id='menu'>
      <button className='btn btn-dark menu-btn' onClick={homepage_req}>Home</button>
      <button className='btn btn-dark menu-btn' onClick={training_req}>Training Zone</button>
      <button className='btn btn-dark menu-btn' onClick={battle_req}>Battle Zone</button>
      </div>
      <div id='main'>
        <TrainingZone/>
      </div>
    </div>
  );
}

export default App;
