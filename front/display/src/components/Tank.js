import React from 'react';
import ReactDOM, { render } from 'react-dom';
import tankpic from "../images/Body.png";
import turretpic from "../images/Turret.png";

const SIZE_FACTOR = 5

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
class Tank extends React.Component{
    constructor(props) {
        super(props)
        this.details = this.props
        this.style = this.getTankStyle(this.details)
        this.turretStyle = this.getTurStyle(this.details)
        this.id = this.details._id
    }

    getTankStyle = (details) => {
        const tankHeight = details.size * SIZE_FACTOR
        const tankWidth = tankHeight / 1.2
        return {
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            position: 'absolute',
            height: tankHeight,
            width: tankWidth,
            backgroundImage: 'url(' + tankpic + ')',
            backgroundSize: 'cover',
            filter: 'hue-' + rot(details.color_rot),
            marginLeft: details.xpos - tankWidth / 2.0,
            marginBottom: details.ypos - tankHeight / 2.0,
            transform: rot(details.rot),   
        }
    }

    getTurStyle = (details) => {
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

    set_turn_details = (turn_details) => {
        Object.keys(turn_details).forEach((key) => this.details[key] = turn_details[key])
        // console.log(this.state.details)
        this.style = this.getTankStyle(this.details)
    }

    render() 
    { return <div className='tank' style={this.style} key={this.id}>
            <img src={turretpic}  style={this.turretStyle}/>
        </div>;
    }
}

export default Tank;