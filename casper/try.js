phantom.outputEncoding='GBK';
var casper = require('casper').create();

var links = ['http://www.baidu.com', 'http://www.bing.com', 'http://www.oschina.net'];

casper.start().each(links, function(self, link){
	self.thenOpen(link, function(){
		this.echo(this.getTitle());
	});
});

casper.run();