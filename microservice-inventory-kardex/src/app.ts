import { config } from './config/index.js';
import express from 'express';
import type { Request, Response } from 'express';
import cors from 'cors';

const app = express();
app.disable('x-powered-by');

app.use(express.json());
app.use(cors({
  origin: config.frontendUrl,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
}));

const PORT = config.port

app.get('/health', (_req: Request, res: Response) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`Microservicio Inventory Kardex corriendo en http://localhost:${PORT}`);
});
