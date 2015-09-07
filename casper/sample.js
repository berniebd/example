var casper = require('casper').create({
	verbose: true,
	logLevel: "debug"
});

casper.start('http://casper.org', function(){
	this.echo(this.getTitle());
});

casper.thenOpen('http://phantomjs.org', function(){
	this.echo(this.getTitle());
});

casper.run();