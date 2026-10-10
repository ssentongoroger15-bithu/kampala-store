from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>RICKRODS - Movie Plug Uganda</title>
<style>
body{background:#000;color:white;font-family:Arial;margin:0;padding:0}
header{background:#E50914;padding:15px;text-align:center;font-size:28px;font-weight:bold;letter-spacing:2px}
.sub{color:#aaa;text-align:center;padding:10px;font-size:14px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:15px}
.card{background:#111;border-radius:10px;overflow:hidden;border:1px solid #222}
.card img{width:100%;height:160px;background:#222;object-fit:cover}
.info{padding:10px}
.title{font-weight:bold;font-size:14px}
.price{color:#0f0;font-size:13px;margin:5px 0}
.btn{display:block;background:#25D366;color:white;text-align:center;padding:10px;border-radius:6px;text-decoration:none;font-weight:bold;margin-top:8px}
footer{text-align:center;padding:20px;color:#666;font-size:12px}
.whatsapp-float{position:fixed;bottom:20px;right:20px;background:#25D366;color:white;width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:30px;text-decoration:none;box-shadow:0 4px 10px rgba(0,0,0,0.5)}
</style>
</head>
<body>
<header>RICKRODS</header>
<div class="sub">🔥 UG's Baddest Movie Plug - Latest HD Movies 500/= 🔥<br>WhatsApp: 0708839598</div>

<div class="grid">
<div class="card"><div style="height:160px;background:linear-gradient(45deg,#E50914,#000);display:flex;align-items:center;justify-content:center;font-size:40px">🎬</div><div class="info"><div class="title">Deadpool & Wolverine (2026)</div><div class="price">500 UGX - HD</div><a class="btn" href="https://wa.me/256708839598?text=Hi%20RICKRODS%20I%20want%20Deadpool%20%26%20Wolverine">BUY NOW</a></div></div>

<div class="card"><div style="height:160px;background:linear-gradient(45deg,#007, #000);display:flex;align-items:center;justify-content:center;font-size:40px">🔥</div><div class="info"><div class="title">John Wick 4 - Latest</div><div class="price">500 UGX - HD</div><a class="btn" href="https://wa.me/256708839598?text=Hi%20RICKRODS%20I%20want%20John%20Wick%204">BUY NOW</a></div></div>

<div class="card"><div style="height:160px;background:linear-gradient(45deg,#550055,#000);display:flex;align-items:center;justify-content:center;font-size:40px">💀</div><div class="info"><div class="title">The Beekeeper (2026)</div><div class="price">500 UGX - HD</div><a class="btn" href="https://wa.me/256708839598?text=Hi%20RICKRODS%20I%20want%20The%20Beekeeper">BUY NOW</a></div></div>

<div class="card"><div style="height:160px;background:linear-gradient(45deg,#005500,#000);display:flex;align-items:center;justify-content:center;font-size:40px">⚡</div><div class="info"><div class="title">Fast X Part 2</div><div class="price">500 UGX - HD</div><a class="btn" href="https://wa.me/256708839598?text=Hi%20RICKRODS%20I%20want%20Fast%20X">BUY NOW</a></div></div>
</div>

<footer>
RICKRODS © 2026<br>
Kampala, Uganda - We Deliver via Telegram/WhatsApp<br>
Pay via MTN MoMo: 0708839598 - Ssentongo
</footer>

<a class="whatsapp-float" href="https://wa.me/256708839598">💬</a>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
