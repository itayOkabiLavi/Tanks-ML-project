import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import tankpic from "../images/Body.png";
import turretpic from "../images/Turret.png";

function rot(deg) {
    return 'rotate(' + deg + 'deg)';
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
    const [details, setDetails] = useState(props.details);
    const id = details._id;

    const SIZE_FACTOR = 5;

    const [tankStyle, setTankStyle] = useState(getTankStyle(details));

    function getTankStyle(details) {
        const tankHeight = details.size * SIZE_FACTOR;
        const tankWidth = tankHeight / 1.4;
        return {
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            position: 'absolute',
            backgroundImage: 'url(' + tankpic + ')',
            backgroundSize: 'cover',
            filter: 'hue-' + rot(details.color_rot),
            marginLeft: details.xpos - tankWidth / 2.0,
            marginBottom: details.ypos - tankHeight / 2.0,
            transform: rot(details.rot),
    
            height: tankHeight,
            width: tankWidth
        };
    }
    
    function change_detail(key, val) {
        details[key] = val;
        setDetails(details);
        setTankStyle(details);
    }

    // function set_turn_details(turn_details) {
    //     console.log(details)
    //     Object.keys(turn_details).forEach((key) => details[key] = turn_details[key])
    //     setDetails(details);
    //     setTankStyle(details);
    //     console.log(details)
    // }

    const turretStyle = getTurStyle(details);

    function getTurStyle(details) {
        const turHeight = details.tursize * SIZE_FACTOR;
        return {
            backgroundImage: 'url(' + turretpic + ')',
            backgroundSize: 'cover',
            height: turHeight,
    
            transform: rot(details.tur_rot),
            transformOrigin: '50% 75%',
            position: 'absolute',
            bottom: '15%',
    
        }
    }

    
    return <div className='tank' style={tankStyle}>
        <img src={turretpic}  style={turretStyle}/>
    </div>;
}

export default Tank;