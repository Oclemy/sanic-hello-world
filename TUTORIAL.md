# Building Your First Sanic Web App: A Step-by-Step Guide

Hey! So you've got a Sanic application running, and you want to understand what's actually happening under the hood. Great news—this is a perfect beginner-friendly example. Let's break it down piece by piece.

## What is Sanic, Anyway?

Think of Sanic like Flask's faster cousin. It's a Python web framework that's built specifically for speed and modern Python features. The key difference? It uses `async` and `await` to handle requests super efficiently, which means it can juggle tons of simultaneous users without breaking a sweat. Perfect for APIs, real-time apps, and microservices.

## Let's Dig Into the Code

### Step 1: Setting Up Your App

```python
import os
from sanic import Sanic
from sanic.response import html

app = Sanic("HelloApp")
```

Here's what's happening:

- **Line 1-3:** We're importing the tools we need. `os` lets us read environment variables (more on that later), `Sanic` is our web framework, and `html` is a response helper that tells the browser "hey, this is HTML content."

- **Line 5:** We're creating a Sanic application instance and giving it a name: `"HelloApp"`. Think of this like opening a blank canvas for your web application. This `app` object is where you'll register all your routes and set up your API endpoints.

### Step 2: Creating Your First Route - The Homepage

```python
@app.get("/")
async def hello(request):
    return html("""
    ...HTML content here...
    """)
```

Let's unpack this:

- **`@app.get("/")`** - This is a decorator that says "when someone visits the root URL of my website (just the `/` part), run the function below." The `get` means it's listening for HTTP GET requests specifically (that's what your browser does when you just type in a URL).

- **`async def hello(request)`** - This is an asynchronous function. The `async` keyword means this function can be paused and resumed, allowing Sanic to handle other requests while it's waiting. The `request` parameter contains info about what the user asked for (headers, body, query parameters, etc.).

- **`return html(...)`** - We're returning a response. The `html()` function wraps our HTML string and tells the browser "this is an HTML page, render it!"

### Step 3: The Styling Section - Making It Look Pretty

```html
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    ...
  }
  .card { ... }
  .badge { ... }
  h1 { ... }
  p { ... }
  .meta { ... }
</style>
```

Don't worry, this is just CSS making the page look fancy. Here's what it does:

- **The gradient background:** Creates a sleek dark blue gradient that goes from top-left to bottom-right
- **Flexbox centering:** Uses `display: flex` to center everything both horizontally and vertically
- **The card:** Has a frosted glass effect with `backdrop-filter: blur(10px)` - that semi-transparent, blurred background you see on modern apps
- **The badge:** That pink "🚀 Live on Railway" label
- **Overall vibe:** Modern, clean, and professional

### Step 4: The HTML Content - What Users See

```html
<div class="card">
  <div class="badge">🚀 Live on Railway</div>
  <h1>Hello, World!</h1>
  <p>Powered by <strong>Sanic</strong> &amp; deployed via <strong>Railway</strong></p>
  <div class="meta">GET / → 200 OK</div>
</div>
```

This is the actual content that shows up on the page. It's wrapped in a `<div class="card">` which applies all that fancy styling we just talked about. The page displays:
- A badge saying it's live on Railway (a deployment platform)
- The classic "Hello, World!" heading
- A subtitle explaining what's powering this app
- Some meta info showing the HTTP status

### Step 5: The Health Check Endpoint

```python
@app.get("/health")
async def health(request):
    return html("OK", status=200)
```

This is a separate route that's super useful in production. Here's why:

- Deployment platforms and monitoring tools periodically check if your app is still alive by hitting `/health`
- It returns just "OK" with an HTTP status code of 200 (which means everything is fine)
- It's simple and fast—perfect for quick health checks
- In a real app, you might check database connections here too, but for now it's just a simple "yep, I'm running"

### Step 6: Running the Server

```python
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, single_process=True)
```

This is the magic that actually starts your web server:

- **`if __name__ == "__main__"`** - This checks if the script is being run directly (not being imported by another script). It's a Python best practice.

- **`os.environ.get("PORT", 8080)`** - This looks for an environment variable called `PORT`. If it exists, use that number. If not, default to port 8080. This is why Railway can set a custom port, and your app will respect it automatically.

- **`app.run(...)`** - This starts the Sanic server:
  - **`host="0.0.0.0"`** - Listen on all available network interfaces (important for deployment platforms)
  - **`port=port`** - Use the port we just determined
  - **`single_process=True`** - Run in a single process (as opposed to multiple workers)

## Putting It All Together - The Request Flow

Here's what happens when someone visits your site:

1. **User visits `yourapp.com/`** → Browser sends an HTTP GET request to the root path
2. **Sanic receives it** → The `@app.get("/")` decorator catches it and routes it to the `hello()` function
3. **Function runs** → `hello(request)` is called asynchronously
4. **Response is built** → The HTML string (with all the styling) is wrapped with the `html()` function
5. **User sees it** → The browser receives the HTML and renders the beautiful styled page

If they visit `yourapp.com/health` instead, step 2 would route to the `health()` function, which returns just "OK".

## Key Takeaways

- **Sanic is an async-first framework** — it's built for speed and modern Python
- **Decorators like `@app.get()` are route handlers** — they connect URLs to functions
- **Environment variables keep your app flexible** — the PORT example shows how to make your code adapt to different deployment environments
- **Health checks are production best practice** — even simple apps benefit from having a `/health` endpoint
- **HTML responses are just strings** — you could replace the HTML with JSON or plain text if you wanted

## What's Next?

You could expand this by:
- Adding more routes with `@app.get()`, `@app.post()`, etc.
- Returning JSON instead of HTML for building APIs
- Adding database connections
- Implementing error handling
- Adding request logging

But for now, you've got a solid foundation. Your app is clean, fast, and deployment-ready! 🚀
