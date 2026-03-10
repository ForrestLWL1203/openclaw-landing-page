import express from 'express'
import cors from 'cors'
import path from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

const app = express()
const PORT = process.env.PORT || 4000

// Middleware
app.use(cors())
app.use(express.json())

// API Routes
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() })
})

app.get('/api/stats', (req, res) => {
  // Placeholder for future stats (downloads, stars, etc.)
  res.json({
    downloads: '10K+',
    stars: '1.2K',
    version: '1.0.0'
  })
})

// Serve static files in production
app.use(express.static(path.join(__dirname, '../../client/dist')))

// Handle Vue SPA routes
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../../client/dist/index.html'))
})

app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`)
})
