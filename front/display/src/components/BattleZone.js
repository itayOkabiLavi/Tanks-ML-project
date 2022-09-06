import React, { useState } from 'react';
import ReactDOM from 'react-dom';

import 'bootstrap/dist/css/bootstrap.min.css'

import Tank from './Tank';
import './BattleZone.css';

const base_url = "http://localhost:3030";



function BattleZone() {
    const [tanks, setTanks] = useState([]);
    const [gameStatus, setGameStatus] = useState("No Game Loaded");
    
    function req_game (e) {
        e.preventDefault();
    
        const response = fetch(base_url + '/battle', {method: 'get'}).then(res => {
            if (res.status == 200) {
                res.text().then(data => {
                    setGameStatus("Loading Game...");
                    parseTextFile(data);
                });
            } else {
                setGameStatus("Game Loading Error");
            }
        });
    }

    function parseTextFile(game_text) {
        const info_split = game_text.split('\n');
        let i = 1;
        const _tanks = [];
        while (info_split[i].trim() !== 'g') {
            let tank_det = info_split[i].trim();
            tank_det = JSON.parse(tank_det);
            _tanks.push(
                <Tank details={tank_det} key={i}/>
            );
            i += 1;
        }
        setTanks(_tanks);

        setGameStatus("Game ID: " + info_split[0]);
    }

    return <div id='grid'>
        <div id='zone_details'>
            <button className='btn btn-dark w' onClick={req_game}>Request game</button>
            <p>{gameStatus}</p>
        </div>
        <div id='zonedisplay'>
            <div id='map-header'></div>
            <div id='map'>
                {tanks}
            </div>
            <div id='map-footer'></div>
        </div>
    </div>
}

export default BattleZone;