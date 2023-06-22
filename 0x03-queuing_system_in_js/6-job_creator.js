import { createClient } from 'redis';

const kuee = require('kue');

const kue = kuee.createQueue();

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const job = {
  phoneNumber: '0702060203',
  message: 'Halo halo',
};

const aJob = kue.create('push_notification_code', job).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${aJob.id}`);
  }
});

aJob.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
