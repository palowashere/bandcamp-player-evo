const bcfetch = require('bandcamp-fetch');

//dunno if this works
bcfetch.cache.setTTL('page', 500);
bcfetch.cache.setMaxPages(20);

//get random interval
function randomIntFromInterval(min, max) { // min and max included 
    return Math.floor(Math.random() * (max - min + 1) + min)
  }
  
const rndInt = randomIntFromInterval(1, 20)

//define what you want and which page 
const params = {
    evopath: process.argv[2],
    genre: process.argv[3],
    location: process.argv[4],
    page: rndInt
}

//get results and store in file
var fs = require('fs');

/*
bcfetch.searchTag({q: process.argv[3]}).then( results => {
    console.log(results);
});
*/


bcfetch.discover({genre: process.argv[3], location: process.argv[4], page:rndInt}).then( results => {
    //console.log(results);
    var json = JSON.stringify(results);
    //console.log(results);
    results.items.forEach(element => {
        //console.log(element.location);
    });
    fs.writeFile(params["evopath"]+"/bandcamp_parser/albums.json", json, function(err) {
        if (err) {
            console.log(err);
        }
    });
});


bcfetch.cache.clear('constant');

