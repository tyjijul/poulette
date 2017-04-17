'use strict';
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
var path = require('path')

let mainWindow;
let subpy;
let apiUrl = 'http://localhost:8000';

app.on('window-all-closed', function() {
  app.quit();
});

app.on('quit', function() {
  subpy.kill('SIGINT');
});

app.on('ready', function() {
  subpy = require('child_process').spawn('python', [__dirname + '/api.py']);
  
  var openWindow = function () {
    mainWindow = new BrowserWindow({width: 800, height: 600, icon: path.join(__dirname, '/static/img/icon_microbs.png')});
    mainWindow.setTitle(require('../package.json').name);
    mainWindow.loadURL('file://' + __dirname + '/templates/route.html', {"extraHeaders" : "pragma: no-cache\n"});
    mainWindow.on('closed', function() {
    mainWindow = null;
    });
  };
  
  var startUp = function () {
    require('request-promise')(apiUrl).then(function(){
      openWindow();
    }).catch(function(err) {
      startUp();
    });
  }
  
  //startUp();
  openWindow();

});

