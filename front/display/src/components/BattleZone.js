import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { useRef } from 'react';

import 'bootstrap/dist/css/bootstrap.min.css'

import Tank from './Tank';
import './BattleZone.css';

const base_url = "http://localhost:3030";

function BattleZone() {
    const FPS_SEC = 800, FFPS_SEC = FPS_SEC / 2;
    let childRef = useRef(null);
    childRef.current = {}
    const [tanks, setTanks] = useState([]);
    const [frames, setFrames] = useState([]);
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
        
        i += 1
        let _frames = []
        while (typeof info_split[i] === 'string') {
            let frame = {};
            info_split[i].trim().split(';').forEach(turn => {
                turn = turn.trim();
                if (turn !== "") {
                    turn = JSON.parse(turn);
                    frame[turn._id] = turn;
                }
            });
            _frames.push(frame);
            i += 1;
        }
        setFrames(_frames);

        setGameStatus("Game ID: " + info_split[0]);
    }

    function start_game (e) {
        e.preventDefault();
        let _frames = frames;
        
        let interval = setInterval(() => {
            if (_frames.length == 0) {
                clearInterval(interval);
                return;
            }
            // console.log(_frames[_frames.length - 1])
            let _tanks = tanks;
            let frame = _frames.pop();
            // console.log(frame)
            for (let index = 0; index < _tanks.length; index++) {
                let tank = _tanks[index];
                let tid = get_tank_val("_id", tank);
                if (tid in frame) {
                    let details = tank.props.details;
                    let key = tank.key;
                    let new_details = frame[tid];
                    //console.log(new_details);
                    Object.keys(new_details).forEach((key) => details[key] = new_details[key]);
                    _tanks[index] = <Tank details={new_details} key={key}/>
                    // console.log(_tanks[index]);
                }
            }
            console.log(_frames.length)
            console.log(_tanks)
            console.log(tanks)
            setTanks(_tanks)
            console.log(tanks)
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
                {tanks}
            </div>
            <div id='map-footer'></div>
        </div>
    </div>
}

function get_tank_val(key, tank) {
    return tank.props.details[key]
}

export default BattleZone;