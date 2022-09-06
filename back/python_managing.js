module.exports = {
    activate: function activate_script(spawn, path) {
        var dataToSend;
        // spawn new child process to call the python script
        const python = spawn('python', [path]);
        // collect data from script
        python.stdout.on('data', function (data) {
            console.log('running python ' + path);
            dataToSend = data.toString();
            console.log(dataToSend)
        });
        // in close event we are sure that stream from child process is closed
        python.on('close', (code) => {
            console.log(`exited python ` + path + ` with ${code}`);
        });
    }
}