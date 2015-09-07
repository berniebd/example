var casper = require('casper').create({
	verbose: true,
	logLevel: "debug",
	pageSettings: {
		webSecurityEnabled: false
	}
});

casper.start('http://www.51testing.com', function(){
	this.download('http://download.51testing.com/ddimg/uploadsoft/20150810/Software_Test_Engineer_Recruitment_Interview_Questions.pdf', '12.pdf');
});

casper.run();