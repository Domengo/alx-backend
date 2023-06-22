import { error } from 'console';

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    console.log('Jobs is not an array');
    throw error();
  }
  jobs.forEach((job) => {
    const jb = queue.create('push_notification_code_3', job).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${jb.id}`);
      }
    });

    jb.on('complete', () => {
      console.log(`Notification job ${jb.id} completed`);
    });

    jb.on('failed', (err) => {
      console.error(`Notification Job ${jb.id} failed: ${err}`);
    });

    jb.on('progress', (progress) => {
      // do something with progress...
      console.log(`Notification job ${jb.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
