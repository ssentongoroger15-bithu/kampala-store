from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>RICKRODS - #1 Movie Plug UG</title>
<style>
body{margin:0;background:#000;color:#fff;font-family:sans-serif}
header{background:#E50914;padding:18px;text-align:center;font-size:30px;font-weight:900;letter-spacing:3px}
.sub{text-align:center;padding:12px;color:#aaa;font-size:13px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:15px}
.card{background:#111;border-radius:12px;overflow:hidden;border:1px solid #222}
.thumb{height:160px;display:flex;align-items:center;justify-content:center;font-size:50px}
.info{padding:10px}
.t{font-weight:bold;font-size:14px;min-height:32px}
.p{color:#2ecc71;font-weight:bold;margin:6px 0;font-size:13px}
.btn{display:block;background:#25D366;color:#fff;text-align:center;padding:10px;border-radius:8px;text-decoration:none;font-weight:bold}
.float{position:fixed;bottom:20px;right:20px;background:#25D366;color:#fff;width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px;text-decoration:none}
footer{text-align:center;padding:25px;color:#666;font-size:11px}
</style></head><body>
<header>RICKRODS</header>
<div class="sub">UG's Baddest Movie Plug 🔥<br>Latest 2026 HD Movies - 500 UGX Only<br>📱 0708839598</div>
<div class="grid">
<div class="card"><div class="thumb" style="background:linear-gradient(135deg,#E50914,#000)">🎬</div><div class="info"><div class="t">Deadpool & Wolverine (2026)</div><div class="p">500 UGX - HD</div><a class="btn" href="https://wa.me/256708839598?text=Hi%20RICKRODS%2C%20I%20want%20Deadpool%20%26%20Wolverine">BUY NOW</a></div></div>
<div class="card"><div class="thumb" style="background:linear-gradient(135deg,#0011ff,#000)">⚡</div><div class="info"><div class="t">John Wick 5</div><div class="p">500 UGX - HD</div><a class="btn" href="https://wa.me/256708839598?text=Hi%20RICKRODS%2C%20I%20want%20John%20Wick%205">BUY NOW</a></div></div>
<div class="card"><div class="thumb" style="background:linear-gradient(135deg,#550055,#000)">💀</div><div class="info"><div class="t">The Beekeeper</div><div class="p">500 UGX - HD</div><a class="btn" href="https://wa.me/256708839598?text=Hi%20RICKRODS%2C%20I%20want%20Beekeeper">BUY NOW</a></div></div>
<div class="card"><div class="thumb" style="background:linear-gradient(135deg,#0a5,#000)">🏎️</div><div class="info"><div class="t">Fast X Part 2</div><div class="p">500 UGX - HD</div><a class="btn" href="https://wa.me/256708839598?text=Hi%20RICKRODS%2C%20I%20want%20Fast%20X">BUY NOW</a></div></div>
</div>
<footer>RICKRODS © 2026<br>Kampala Uganda | Pay MTN MoMo: 0708839598<br>Delivered on WhatsApp & Telegram Instant</footer>
<a class="float" href="https://wa.me/256708839598">💬</a>
</body></html>
"""
@app.route('/')
def home():
    return HTML
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
