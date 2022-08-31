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
                <Tank id={1} 
                xpos={0} ypos={100} rot={0} 
                size={1} color_rot={0}
                tursize={1} tur_rot={0}/>
            </div>
            <div id='map-footer'></div>
        </div>
    </div>
}

export default TrainingZone;