
// SETUP
const port = 3030;
const express = require('express');
const srvapp = express();

const cors = require("cors");
srvapp.use(cors());

const {spawn} = require('child_process');

const api = require('./api')
const python_managing = require('./python_managing');

const database_path = "./algorithms/output"
// TODO: static public. return web displayer

// START
api(srvapp, port, database_path);
python_managing.activate(spawn, './algorithms/train_tanks.py');