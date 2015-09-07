var casper = require('casper').create();

casper.start('https://www.baidu.com', function(){
	this.fillSelectors('form#form', {
		'input#kw': 'casper'
	}, true);
});
casper.run(function(){
	echo('hello world!');
});