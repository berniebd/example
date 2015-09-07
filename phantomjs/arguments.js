var system = require('system');
if(system.args.length == 1){
	console.log('try to pass some arguments');
} else{
	system.args.forEach(function(arg, i){
		console.log(i + ': ' + arg);
	});
}
phantom.exit();