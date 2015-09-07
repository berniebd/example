var casper = require('casper').create();

casper.start('http://www.baidu.com');

casper.echo('begin wait');
casper.waitFor(function(){
	this.wait(2000, function(){
		this.echo('end wait');
	});
	return true;
}, function(){
	this.echo('then');
});

casper.run();