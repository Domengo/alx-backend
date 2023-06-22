import { createClient } from "redis";
const kuee = require('kue');
const kue = kuee.createQueue();
// Create a client instance
const client = createClient();

client.on('connect', () => {
  console.log("Redis connected to the server");
});

client.on('error', () => {
  console.log(`Redis client not connected to the server: ${ err }`);
});

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

kue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});