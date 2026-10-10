from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
<title>Kampala Movie Center - Latest Movies 2026</title>
<style>
body{margin:0;font-family:sans-serif;background:#0f0f0f;color:#fff}
header{background:#000;padding:15px;text-align:center;position:sticky;top:0;z-index:10;border-bottom:2px solid #e50914}
.logo{color:#e50914;font-size:24px;font-weight:900}
.hero{background:linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.7)),linear-gradient(135deg,#e50914,#000);padding:60px 20px;text-align:center}
.btn{background:#e50914;color:#fff;padding:16px 32px;border-radius:6px;text-decoration:none;font-weight:bold;display:inline-block;margin-top:15px;font-size:18px}
.card{background:#1a1a1a;margin:12px;border-radius:12px;padding:18px;border:1px solid #333}
.cats{display:flex;gap:8px;overflow-x:auto;padding:10px 0}
.cat{background:#222;padding:8px 16px;border-radius:20px;white-space:nowrap;border:1px solid #444;cursor:pointer}
.cat.active{background:#e50914;border-color:#e50914}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}
.movie{background:#222;border-radius:10px;overflow:hidden;border:1px solid #333}
.movie-img{height:140px;background:#333;display:flex;align-items:center;justify-content:center;font-size:50px}
.movie-info{padding:12px}
.movie-info b{font-size:14px;display:block;min-height:32px}
.price{color:#46d369;font-weight:bold;margin:6px 0}
.order{background:#e50914;color:white;padding:8px 0;border-radius:5px;text-decoration:none;display:block;text-align:center;font-weight:bold;margin-top:6px}
.wa{background:#25D366;color:white;padding:14px;border-radius:30px;text-decoration:none;display:inline-block;font-weight:bold}
footer{background:#000;color:#777;padding:20px;text-align:center;border-top:1px solid #222}
</style></head><body>
<header><div class='logo'>🎬 KAMPALA MOVIES UG 🇺🇬</div><div style='font-size:12px;color:#aaa'>Latest Movies • Series • Affordable</div></header>

<div class='hero'>
<h1 style='margin:0'>Latest Movies 2026 in HD</h1>
<p>Hollywood • Nollywood • Ugandan • Series<br>500 UGX per Movie | Delivered on WhatsApp / Telegram</p>
<a class='btn' href='https://wa.me/256708839598?text=Hello%20Kampala%20Movies%2C%20I%20want%20to%20buy%20movies'>🔥 Order Movies Now</a>
</div>

<div class='card'>
<h3 style='margin-top:0'>📁 Categories</h3>
<div class='cats'>
<div class='cat active'>🔥 Trending</div>
<div class='cat'>🎬 Hollywood 2026</div>
<div class='cat'>🇳🇬 Nollywood</div>
<div class='cat'>🇺🇬 Ugandan</div>
<div class='cat'>📺 Series</div>
<div class='cat'>💥 Action</div>
</div>
</div>

<div class='card'>
<h3>🔥 Trending This Week - UGX 500 each</h3>
<div class='grid'>
<div class='movie'><div class='movie-img'>🎬</div><div class='movie-info'><b>Deadpool & Wolverine (2026)</b><small style='color:#aaa'>Action • HD</small><div class='price'>500 UGX</div><a class='order' href='https://wa.me/256708839598?text=I%20want%20Deadpool%20and%20Wolverine%20movie%20500'>BUY NOW</a></div></div>
<div class='movie'><div class='movie-img'>🦁</div><div class='movie-info'><b>Mufasa: Lion King</b><small style='color:#aaa'>Animation • HD</small><div class='price'>500 UGX</div><a class='order' href='https://wa.me/256708839598?text=I%20want%20Mufasa%20Lion%20King%20movie'>BUY NOW</a></div></div>
<div class='movie'><div class='movie-img'>💀</div><div class='movie-info'><b>John Wick 5</b><small style='color:#aaa'>Action • 2026</small><div class='price'>500 UGX</div><a class='order' href='https://wa.me/256708839598?text=I%20want%20John%20Wick%205'>BUY NOW</a></div></div>
<div class='movie'><div class='movie-img'>👑</div><div class='movie-info'><b>Coming to Uganda</b><small style='color:#aaa'>Comedy • Luganda</small><div class='price'>500 UGX</div><a class='order' href='https://wa.me/256708839598?text=I%20want%20Coming%20to%20Uganda%20movie'>BUY NOW</a></div></div>
<div class='movie'><div class='movie-img'>⚔️</div><div class='movie-info'><b>Gladiator II</b><small style='color:#aaa'>Action • HD</small><div class='price'>500 UGX</div><a class='order' href='https://wa.me/256708839598?text=I%20want%20Gladiator%202'>BUY NOW</a></div></div>
<div class='movie'><div class='movie-img'>📺</div><div class='movie-info'><b>Shaka iLembe S2</b><small style='color:#aaa'>Series • All Episodes</small><div class='price'>2000 UGX</div><a class='order' href='https://wa.me/256708839598?text=I%20want%20Shaka%20iLembe%20S2%20Series'>BUY NOW</a></div></div>
</div>
</div>

<div class='card'>
<h3>💰 Packages - Save Money!</h3>
<div style='display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #333'><span>10 Movies<br><small style='color:#aaa'>Any choice</small></span><b style='color:#46d369'>4,000 UGX</b><a href='https://wa.me/256708839598?text=I%20want%2010%20movies%20package%204000' style='background:#46d369;color:#000;padding:6px 12px;border-radius:15px;text-decoration:none;font-size:13px;font-weight:bold'>Buy</a></div>
<div style='display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #333'><span>20 Movies + 1 Series<br><small style='color:#aaa'>Best Seller!</small></span><b style='color:#46d369'>7,000 UGX</b><a href='https://wa.me/256708839598?text=I%20want%2020%20movies%20package%207000' style='background:#46d369;color:#000;padding:6px 12px;border-radius:15px;text-decoration:none;font-size:13px;font-weight:bold'>Buy</a></div>
<div style='display:flex;justify-content:space-between;padding:12px 0'><span>Monthly Unlimited<br><small style='color:#aaa'>All new movies daily</small></span><b style='color:#46d369'>15,000 UGX</b><a href='https://wa.me/256708839598?text=I%20want%20monthly%20unlimited%2015000' style='background:#46d369;color:#000;padding:6px 12px;border-radius:15px;text-decoration:none;font-size:13px;font-weight:bold'>Buy</a></div>
</div>

<div class='card' style='text-align:center;background:linear-gradient(135deg,#25D366,#128C7E);border:none'>
<h3 style='margin-top:0'>📲 How It Works?</h3>
<p>1. Click BUY on any movie<br>2. Pay via MTN Mobile Money or Airtel<br>3. We send movie instantly on WhatsApp / Telegram<br><br><b>0708839598 - Fast Delivery 24/7!</b></p>
<a class='wa' style='background:#fff;color:#128C7E' href='https://wa.me/256708839598?text=Hello%20Kampala%20Movies%2C%20how%20to%20order%3F'>💬 Chat on WhatsApp</a>
</div>

<footer>© 2026 Kampala Movie Center 🇺🇬<br>0708839598 • Kampala, Uganda • We Deliver Instant<br><small>All movies in HD • Luganda Translation Available</small></footer>
</body></html>
    """
if __name__ == '__main__':
    app.run()
