from pathlib import Path
import re, json, shutil
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.urls=[];self.headings=[];self.images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for k in ('href','src'):
   if k in a:self.urls.append(a[k])
  if tag=='img':self.images.append(a)
  if tag in ('h1','h2','h3'):self.headings.append(tag)
html=(ROOT/'index.html').read_text(encoding='utf-8');page=Page();page.feed(html)
assert len(page.ids)==len(set(page.ids)),'Duplicate IDs'
assert page.headings.count('h1')==1,'Exactly one H1 required'
for url in page.urls:
 if url.startswith('#'):assert url[1:] in page.ids,f'Missing anchor {url}'
 elif not re.match(r'^[a-z]+:',url):assert (ROOT/url.split('#')[0]).is_file(),f'Missing asset {url}'
assert all('alt' in a for a in page.images)
assert '<html lang="en">' in html
assert 'name="viewport"' in html and 'rel="canonical"' in html
json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',html,re.S).group(1))
# Static file copy mirrors root-based Pages assets; GitHub still performs its legacy Jekyll build.
dist=ROOT/'dist';dist.mkdir(exist_ok=True)
for name in ('index.html','robots.txt','sitemap.xml'):
 shutil.copy2(ROOT/name,dist/name)
shutil.copytree(ROOT/'assets',dist/'assets',dirs_exist_ok=True)
print(f'PASS: HTML structure, {len(page.ids)} unique IDs, all local links/assets, metadata and JSON-LD')
print('PASS: static build written to dist; deployment configuration untouched')
