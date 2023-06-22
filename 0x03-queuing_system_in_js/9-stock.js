const express = require('express');
import { createClient } from 'redis';

client = createClient();

client.on('connect', () => {
  console.log(`Connected to Redis`);
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

let listProducts = [
  {
    id: '1',
    name: 'Suitcase 250',
    price: '50',
    stock: '4'
  },
  {
    id: '2',
    name: 'Suitcase 450',
    price: '100',
    stock: '10'
  },
  {
    id: '3',
    name: 'Suitcase 650',
    price: '350',
    stock: '2'
  },
  {
    id: '4',
    name: 'Suitcase 1050',
    price: '550',
    stock: '5'
  },
];

function getElementById(id) {
  if (listProducts.id === id) {
    return listProducts[i] || null;
  }
};

function reserveStockById(itemId, stock) {

}

// Create an express server listening on the port 1245. (You will start it via: npm run dev 9-stock.js

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});