import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import tankpic from "../images/Body.png";
import turretpic from "../images/Turret.png";

function rot(deg) {
    return 'rotate(' + deg + 'deg)';
}

function getTankStyle(props, tankHeight, tankWidth) {
    return {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',

        backgroundImage: 'url(' + tankpic + ')',
        backgroundSize: 'cover',
        filter: 'hue-' + rot(props.color_rot),
        marginLeft: props.xpos - tankWidth / 2.0,
        marginBottom: props.ypos - tankHeight / 2.0,
        transform: rot(props.rot),

        height: tankHeight,
        width: tankWidth
    };
}

function getTurStyle(props, turHeight) {
    return {
        backgroundImage: 'url(' + turretpic + ')',
        backgroundSize: 'cover',
        height: turHeight,

        transform: rot(props.tur_rot),
        transformOrigin: '50% 75%',
        position: 'absolute',
        bottom: '15%',

    }
}
/**
 * props = {
 *  id      - tank id.
 *  xpos    - x position.
 *  ypos    - x position.
 *  size    - tank size [0,1].
 *  rot     - rotation (positive is to the right).
 *  color_rot - rotation of the color (change color).
 *  tursize - turrent size.
 *  tur_rot - turrent rotation acoording to tank.
 * }
 * @param {*} props 
 * @returns 
 */
function Tank(props) {
    const MAX_BODY = 50, MAX_TUR = 50;

    const tankHeight = props.size * MAX_BODY;
    const tankWidth = tankHeight / 1.4;

    const turHeight = props.tursize * MAX_TUR;
    const turWidth = turHeight / 1.6;

    const size = turHeight * 1.5;

    const tankStyle = getTankStyle(props, tankHeight, tankWidth);
    const turretStyle = getTurStyle(props, turHeight);

    return <div className='tank' style={tankStyle}>
        <img src={turretpic}  style={turretStyle}/>
    </div>;
}

export default Tank;