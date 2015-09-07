var links = [];
var casper = require('casper').create();

function getLinks(){
	var links = document.querySelectAll('h3>a');
	return Array.prototype.map.call(links, function(e){
		return e.getAttribute('href');
	});
};

casper.start('https://www.baidu.com', function(){
	this.fillSelectors('form#form', {'input#kw': 'casperjs'}, true);
});

//this.echo(links);

casper.then(function(){
	links = this.evaluate(getLinks);
	this.fillSelectors('form#form', {'input#kw': 'phantomjs'}, true);
});
this.echo(links);

casper.then(function(){
	links = links.concat(this.evaluate(getLinks));
});

casper.run(function(){
	this.echo(links.length, ' links found');
	this.echo(' - ' + links.join('\n - ')).exit();
});