const {app, BrowserWindow} = require('electron');
const url = require('url');
const path = require('path');


app.on('ready', function() {
    mainWindow = new BrowserWindow({
        height: 768,
        width: 1024,
    });
    // console.log(path.join(path.join(__dirname, 'app/index.html')))
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'web/web.html'),
        protocol: 'file:',
        slashes: true
      }));


    mainWindow.on('closed', function(){
    	mainWindow = null
    });
});