import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { useRef } from 'react';

import 'bootstrap/dist/css/bootstrap.min.css'

import Tank from './Tank';
import './BattleZone.css';

const base_url = "http://localhost:3030";

function BattleZone() {
    const FPS_SEC = 100, FFPS_SEC = FPS_SEC / 2;
    let childRef = useRef(null);
    childRef.current = {}
    const [tanks, setTanks] = useState([]);
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
        const info_split = game_text.split('\n');
        let i = 1;
        let tempTanks = []
        let tempTankSprites = []
        while (info_split[i].trim() !== 'g') {
            let tank_det = info_split[i].trim()
            tank_det = JSON.parse(tank_det)
            let tank = new Tank(tank_det)
            tempTanks.push(tank)
            tempTankSprites.push(tank.render())
            i += 1
        }
        setTanks(tempTanks);
        setSprites(tempTankSprites)
        
        i += 1
        let _frames = []
        while (typeof info_split[i] === 'string') {
            let frame = {};
            info_split[i].trim().split(';').forEach(turn => {
                turn = turn.trim().slice(1,-1); // remove spaces before & after string + chars '[',']'
                if (turn !== "") {
                    let turn_list = turn.split(',');
                    turn = {
                        _id: turn_list[0].trim(),
                        xpos: turn_list[1].trim(),
                        ypos: turn_list[2].trim(),
                        rot: turn_list[3].trim(),
                        tur_rot: turn_list[4].trim()
                    }
                    // console.log(turn)
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

        let interval = setInterval(() => {
            if (frames.length <= 0) {
                clearInterval(interval)
                return
            }
            let frame = frames.shift()
            let tempTanks = []
            tanks.forEach(tank => {
                if (tank.id in frame) {
                    tank.set_turn_details(frame[tank.id])
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