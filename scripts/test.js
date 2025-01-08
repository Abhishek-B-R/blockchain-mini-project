import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 20 }, // Ramp up to 50 users
    { duration: '1m', target: 20 }, // Stay at 50 users
    { duration: '30s', target: 0 }, // Ramp down
  ],
};

export default function () {
  const res = http.get('https://blockchain-mini-project.vercel.app/');
  console.log(`Status: ${res.status}, Response time: ${res.timings.duration}ms`);
  if (res.status !== 200) {
    console.error(`Request failed with status ${res.status}`);
  }
  sleep(1);
}
