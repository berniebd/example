var page = require('webpage').create();
var fs = require('fs');
page.open("http://oa.dangdang.com", function(){
	page.evaluate(function(){

	});
	page.render("1.jpeg");
	fs.write("1.html", page.content, 'w');
	phantom.exit();
});