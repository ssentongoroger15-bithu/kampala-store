from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
<style>
body{margin:0;font-family:sans-serif;background:#f5f5f5}
header{background:#111;color:white;padding:15px;text-align:center}
.hero{background:linear-gradient(135deg,#ff6a00,#ee0979);color:white;padding:60px 20px;text-align:center}
.btn{background:white;color:#ee0979;padding:12px 25px;border-radius:25px;text-decoration:none;font-weight:bold;display:inline-block;margin-top:15px}
.card{background:white;margin:15px;padding:20px;border-radius:10px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
footer{background:#111;color:#aaa;padding:20px;text-align:center}
</style></head><body>
<header><h2>KAMPALA STORE 🇺🇬</h2></header>
<div class='hero'><h1>Welcome to My Website!</h1><p>Built on phone with Flask</p><a class='btn' href='#'>Shop Now</a></div>
<div class='card'><h3>🔥 Our Services</h3><p>We sell quality products in Kampala. Fast delivery!</p></div>
<div class='card'><h3>📞 Contact</h3><p>WhatsApp: 0708 839 598<br>Location: Kampala, Uganda</p></div>
<footer>© 2026 Kampala Store - Built on Tecno Camon 20</footer>
</body></html>
    """
