import React, { useState } from 'react';
import {Button} from 'react-bootstrap/Button'
import 'bootstrap/dist/css/bootstrap.min.css'

import logo from './logo.svg';
import './App.css';
import BattleZone from './components/BattleZone';
import base_url from './variables.js'


function App() {
  
  const [switcher, setSwitcher] = useState(true)
  
  const homepage_req = (e) => {
    e.preventDefault();
    console.log("Homepage clicked");
    fetch(base_url + '/homepage', {method: 'get', url: 'http://localhost:3030'}).then(res => 
      {
        console.log('answered');
      })
  }

  return (
    <div className="App">
      <div id='menu'>
      Menu
      </div>
      <div id='main'>
        {switcher ? <BattleZone/> : "false"}
      </div>
    </div>
  );
}

export default App;
