const port = 3000;
const express = require('express');
const srvapp = express();
// TODO: static public. return web displayer

srvapp.listen(port, () => console.log('listening on ' + port));

srvapp.get('/homepage', (req, res) => {
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    console.log("request for homepage on: " + time)
    res.status(200).send("Homepage");
});

srvapp.get('/training', (req, res) => {
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    console.log("request for training on: " + time)
    res.status(200).send("Training");
});

srvapp.get('/battle', (req, res) => {
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    console.log("request for battle on: " + time)
    res.status(200).send("Battle");
});