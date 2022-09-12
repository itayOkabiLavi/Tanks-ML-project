import React from 'react';
import ReactDOM, { render } from 'react-dom';
import tankpic from "../images/Body.png";
import turretpic from "../images/Turret.png";

const SIZE_FACTOR = 5

function rotation_format(deg) {
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
        this.id = this.details._id

        this.color_rot = this.details.color_rot
        this.tankHeight = this.details.size * SIZE_FACTOR
        this.tankWidth = this.tankHeight / 1.2
        
        this.turHeight = this.details.tursize * SIZE_FACTOR;
        
        this.style = this.getTankStyle(this.details.xpos, this.details.ypos, this.details.rot)
        this.turretStyle = this.getTurStyle(this.details.tur_rot)
    }

    getTankStyle = (xpos, ypos, angle) => {
        return {
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            position: 'absolute',
            height: this.tankHeight,
            width: this.tankWidth,
            backgroundImage: 'url(' + tankpic + ')',
            backgroundSize: 'cover',
            filter: 'hue-' + rotation_format(this.color_rot),
            marginLeft: xpos - this.tankWidth / 2.0,
            marginBottom: ypos - this.tankHeight / 2.0,
            transform: rotation_format(angle),   
        }
    }

    getTurStyle = (angle) => {
        return {
            backgroundImage: 'url(' + turretpic + ')',
            backgroundSize: 'cover',
            height: this.turHeight,
            
            transform: rotation_format(angle),
            transformOrigin: '50% 75%',
            position: 'absolute',
            bottom: '15%',
        }
    }

    setTurnDetails = (turn_details) => {
        Object.keys(turn_details).forEach((key) => this.details[key] = turn_details[key])
        // console.log(this.state.details)
        this.style = this.getTankStyle(this.details.xpos, this.details.ypos, this.details.rot)
        this.turretStyle = this.getTurStyle(this.details.tur_rot)
    }

    render() 
    { return <div className='tank' style={this.style} key={this.id}>
            <img src={turretpic} style={this.turretStyle}/>
        </div>;
    }
}

export default Tank;