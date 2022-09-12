import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { useRef } from 'react';

import 'bootstrap/dist/css/bootstrap.min.css'

import Tank from './Tank';
import Parser from './Parser'
import './BattleZone.css';

const base_url = "http://localhost:3030";

function BattleZone() {
    const FPS_SEC = 100, FFPS_SEC = FPS_SEC / 2;
    let childRef = useRef(null);
    childRef.current = {}
    const parser = new Parser
    const [objects, setObjects] = useState({});
    const [frames, setFrames] = useState([]);
    const [gameStatus, setGameStatus] = useState("No Game Loaded");
    const [sprites, setSprites] = useState([])
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
        const [_gameID, _objects, _sprites, _frames] = parser.parseGameFile()
        setObjects(_objects)
        setSprites(_sprites)
        setFrames(_frames)

        setGameStatus("Game ID: " + _gameID);
    }

    function start_game (e) {
        e.preventDefault();

        let interval = setInterval(() => {
            if (frames.length <= 0) {
                clearInterval(interval)
                return
            }
            let frame = frames.shift()
            let tempTanks = []
            .forEach(tank => {
                if (tank.id in frame) {
                    tank.setTurnDetails(frame[tank.id])
                }
                tempTanks.push(tank.render())
            });
            // console.log(tempTanks);
            setSprites(tempTanks)
        }, FPS_SEC);
    }

    function stop_game (e) {
        e.preventDefault();
    }

    return <div id='grid'>
        <div id='zone_details'>
            <button className='btn btn-dark w' onClick={req_game}>Request game</button>
            <p>{gameStatus}</p>
            <button className='btn btn-dark w' onClick={start_game}>Play</button>
            <button className='btn btn-dark w' onClick={stop_game}>Stop</button>
        </div>
        <div id='zonedisplay'>
            <div id='map-header'></div>
            <div id='map'>
                {sprites}
            </div>
            <div id='map-footer'></div>
        </div>
    </div>
}

function get_tank_val(key, tank) {
    return tank.props.details[key]
}

export default BattleZone;