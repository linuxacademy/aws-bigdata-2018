'use strict';
var AWS = require("aws-sdk");
var mysql = require('mysql');
var endpoint = "moviesdb.cluster-cvqpiwbyxdjk.us-east-1.rds.amazonaws.com"
var username = "cloud_user"
var password = "linuxacademy"
var dbname = "moviesdb"
var tablename = "Movies"

exports.handler = (event, context, callback) => {

    event.Records.forEach((record) => {
        console.log('Stream record: ', JSON.stringify(record, null, 2));
        
        if (record.eventName == 'INSERT') {
            var year = JSON.stringify(record.dynamodb.NewImage.year.N);
            var title = JSON.stringify(record.dynamodb.NewImage.title.S);
            var actor = JSON.stringify(record.dynamodb.NewImage.actor.S);
            var rating = JSON.stringify(record.dynamodb.NewImage.rating.N);
            var running_time = JSON.stringify(record.dynamodb.NewImage.running_time.N);
            var uploaded = JSON.stringify(record.dynamodb.NewImage.uploaded.S);
            
            console.log(year, title, actor, rating, running_time, uploaded);
            var con = mysql.createConnection({
              host: endpoint,
              user: username,
              password: password,
              database: dbname
            });
            console.log(con);
            
            con.connect(function(err) {
              if (err) throw err;
              console.log("Connected!");
              var sql = `INSERT INTO ${tablename} (Year, Title, Actor, Rating, Runtime, Uploaded) VALUES (${year},${title},${actor},${rating},${running_time},${uploaded})`;
              con.query(sql, function (err, result) {
                if (err) throw err;
                console.log("1 record inserted");
              con.destroy();
              });
            });
        }
    });
    callback(null, `Successfully processed ${event.Records.length} records.`);
}; 