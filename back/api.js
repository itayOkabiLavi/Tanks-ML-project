module.exports = 
function api(srvapp, port, database_path) {
    srvapp.listen(port, () => console.log('listening on ' + port));

    srvapp.get('/homepage', (req, res) => {
        var today = new Date();
        var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        console.log("request for homepage on: " + time)
        res.status(200).send("Homepage");
    });
    
    srvapp.get('/battle', (req, res) => {
        const fs = require('fs');
        const filename = database_path + '/' + 'battle_1.txt';
        console.log("request for battle on");
        let content = "";
        fs.readFile(filename, 'utf8', (err, data) => {
            content = data;
            console.log(content);
            if (err) {
                res.status(404).send(err);
            } else {
                res.status(200).send(data);
            }
        });
    });
}