import requests
from datetime import datetime

r = requests.get('https://www.pagina12.com.ar/contratapa', allow_redirects=True)
contratapa_url = r.url

titulo = contratapa_url.split("/")[-1].replace("-", " ").capitalize()
fecha = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Contratapa Página12</title>
<link>https://www.pagina12.com.ar/secciones/contratapa</link>
<description>Última contratapa publicada</description>
<item>
<title>{titulo}</title>
<link>{contratapa_url}</link>
<guid>{contratapa_url}</guid>
<pubDate>{fecha}</pubDate>
</item>
</channel>
</rss>
"""

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(rss)
