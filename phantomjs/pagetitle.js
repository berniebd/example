var page = require('webpage').create();
page.open(url, function(status){
	var title  page.evaluate(function({
		return document.title;
	}));
})