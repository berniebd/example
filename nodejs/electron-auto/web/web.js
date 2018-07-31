'use strict';
const { ipcRenderer, BrowserWindow } = require('electron');
const task = require('../shared/task');
const screenshot = require('electron-screenshot');
const fs = require('fs');

window.onload = function () {
	const backgroundButton = document.getElementById('background-task');
	backgroundButton.onclick = function createBackgroudWeb() {
		const backgroudWindow = new BrowserWindow({
			width: 600,
			height: 800
		});
		backgroudWindow.loadURL(url.format({
        	pathname: path.join('www.baidu.com'),
        	protocol: 'http:',
        	slashes: true
    	}));
    	screenshot({
    		width: 1024,
    		height: 768
    	}).then(function(img){
    		fs.writeFile('./out.png', img.data, function(err){
    			screenshot.close();
    		});
    	});
	}
}