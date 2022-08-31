import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import bodypic from "../images/Body.png";
import './Tank.css';
function Tank(props) {
    const maxBody = 50, maxTor = 50;
    const height = props.size * maxBody;
    const width = height / 1.3;
    const [angle, setAngle] = useState(props.rot)

    const bodyStyle = {
        height: height,
        
    }
    const tankStyle = {
        marginLeft: props.xpos - width/2,
        marginBottom: props.ypos - height/2,
        transform: 'rotate('+ angle + 'deg)',
        backgroundImage: 'url(' + bodypic + ')',
        backgroundSize: 'cover',
        height: height,
        width: width
    };
    function Turrent() {
        return <div>
            <img src='../../public/Turret.png' />
        </div>
    }
    return <div className='tank' style={tankStyle}>
        <Turrent/>
    </div>;
}

export default Tank;