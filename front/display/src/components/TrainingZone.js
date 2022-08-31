import React from 'react';
import ReactDOM from 'react-dom';
import Tank from './Tank';
import './TrainingZone.css';

function TrainingZone() {
    return <div id='grid'>
        <div id='zone-details'>

        </div>
        <div id='zonedisplay'>
            <div id='map-header'></div>
            <div id='map'>
                <Tank id={1} xpos={0} ypos={100} rot={90} size={1} torsize={1}/>
            </div>
            <div id='map-footer'></div>
        </div>
    </div>
}

export default TrainingZone;