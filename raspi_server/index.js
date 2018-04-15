var express = require('express');
var app = express();

app.listen(3000, function() {
  console.log('listening on port 3000');
});

// Use the following URL example to send params:
// http://{ip}:3000/params?_prec=100&_type=10&_height=100
app.get('/params', callParams);

var PythonShell = require('python-shell');

function callParams(req, res) {
  var options = {
  //  pythonPath: 'path/to/python',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: './python/test.py',
    args: [
      req.query._prec,    // precision
      req.query._type,    // circle, line, ... 
      req.query._height  // in mm
    ]
  };
  PythonShell.run('test.py', options, function (err, results) {
    if (err) throw (err);
    console.log('results: %j', results);
  });
}