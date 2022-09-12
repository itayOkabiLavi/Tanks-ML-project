import React from 'react';
import ReactDOM, { render } from 'react-dom';
import bullet_pic from '../images/Bullet.png'

class Bullet {
    constructor(props) {
        super(props)
        this.id = props.id
        this.size = props.size
        this.xpos = props.xpos
        this.ypos = props.ypos
        this.color_rot = props.color_rot
        this.style = this.getStyle(this.xpos, this.ypos)
    }

    getStyle = (xpos, ypos) => {return {
        position: 'absolute',
        height: this.size,
        filter: 'hue-rotate(' + this.color_rot + 'deg)',
        marginLeft: xpos - this.size / 2.0,
        marginBottom: ypos - this.size / 2.0,
    }}

    setPosition = (xpos, ypos) => {
        this.style = this.getStyle(xpos, ypos)
    }

    render() {
        return <img src={bullet_pic} style={this.style}/>
    }
}