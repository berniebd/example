var casper = require('casper').create();

casper.start('http://localhost:8080/casper.html', function(){
	this.fill('#contact-form',{
		'subject': 'I am watching you',
		'civility': 'Mr',
		'cc': true,
		'attachment': 'try.js'
	});
});

casper.run();
