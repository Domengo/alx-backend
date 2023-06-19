#!/usr/bin/env node
"use strict";

var _redis = require("redis");
var client = (0, _redis.createClient)();
client.on('connect', function () {
  console.log('Redis client connected to the server');
});
client.on('error', function (err) {
  console.log("Redis client not connected to the server: ".concat(err));
});
