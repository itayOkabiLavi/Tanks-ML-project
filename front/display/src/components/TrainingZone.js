import React from 'react';
import ReactDOM from 'react-dom';
import Tank from './Tank';
import './TrainingZone.css';

function parseTextFile(gameplan_file) {
    let frames_stack = [];
    const Fs = new FileReader();


}

function TrainingZone() {
    const tanks = [];
    const gameplan_file = "";
    const frames_stack = parseTextFile(gameplan_file);  // contains stacks : one for frame
    // bullets also have "commands"
    /* in loop ??? :
        cmd_stack = parseCommand(frameplan)

    */
    return <div id='grid'>
        <div id='zone-details'>

        </div>
        <div id='zonedisplay'>
            <div id='map-header'></div>
            <div id='map'>
                <Tank
            </div>
            <div id='map-footer'></div>
        </div>
    </div>
}

export default TrainingZone;