var fs = require('fs');
var tj = require('togeojson'),
    fs = require('fs'),
    // node doesn't have xml parsing or a dom. use jsdom
    jsdom = require('jsdom').jsdom;

var kml = jsdom(fs.readFileSync('gxps.kml', 'utf8'));

//var converted = tj.kml(kml);

var converted_with_styles = tj.kml(kml, { styles: true });

var outputFilename = 'Network.json';

fs.writeFile(outputFilename, JSON.stringify(converted_with_styles, null, 4), function(err) {
    if(err) {
      console.log(err);
    } else {
      console.log("JSON saved to ");
    }
}); 
