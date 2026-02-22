import os
from sanic import Sanic
from sanic.response import html

app = Sanic("HelloApp")

@app.get("/")
async def hello(request):
    return html("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello World – Sanic on Railway</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
      font-family: 'Segoe UI', sans-serif;
      color: #fff;
    }
    .card {
      text-align: center;
      padding: 3rem 4rem;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 1.5rem;
      backdrop-filter: blur(10px);
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    .badge {
      display: inline-block;
      background: #e94560;
      color: #fff;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      padding: 0.3rem 1rem;
      border-radius: 2rem;
      margin-bottom: 1.5rem;
    }
    h1 { font-size: 3rem; font-weight: 800; margin-bottom: 0.5rem; }
    p  { font-size: 1.1rem; color: rgba(255,255,255,0.6); margin-top: 0.5rem; }
    .meta { margin-top: 2rem; font-size: 0.85rem; color: rgba(255,255,255,0.3); }
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">🚀 Live on Railway</div>
    <h1>Hello, World!</h1>
    <p>Powered by <strong>Sanic</strong> &amp; deployed via <strong>Railway</strong></p>
    <div class="meta">GET / → 200 OK</div>
  </div>
</body>
</html>
""")

@app.get("/health")
async def health(request):
    return html("OK", status=200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, single_process=True)
