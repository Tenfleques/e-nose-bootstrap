var http = require('http');
let fs = require("fs");

let intxt =  "[" + fs.readFileSync("/home/node/models/models.config").toString();

var jsontemp  = intxt
                .replace(/\s/g,'')
                .replace(/config:/g,"")
                .replace('model_config_list:{','')
                .replace('}}','}]');

jsontemp  = jsontemp.replace((/([\w]+)(:)|"config":/g), "\"$1\"$2");

let modelsRaw = JSON.parse(jsontemp);

let modelDetails = JSON.parse(fs.readFileSync("/home/node/models/description.json"));

let models = modelsRaw.map(function(model){
    let details = modelDetails.find(function(details){
        return details.model == model.name;
    }) || modelDetails[0];

    model["details"] = details;
    return model;
})

http.createServer(function (req, res) {
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Charset', 'utf-8');
    res.end(JSON.stringify(models, null, 3));
}).listen(8080);


