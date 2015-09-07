var casper = require('casper').create();

casper.start('http://www.baidu.com', function(){
	this.capture('baidu.png');
});

casper.thenOpen('http://www.oschina.net', function(){
	this.captureSelector('oschina.png', '#IndustryNews');
});


casper.run();