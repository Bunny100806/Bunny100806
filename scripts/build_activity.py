#!/usr/bin/env python3
'''Build an animated GitHub contribution flight from the authenticated GitHub GraphQL API.
No invented contribution counts; requires GH_TOKEN and defaults to this profile's username.
'''
import os, sys, json, urllib.request, pathlib, html
USERNAME=os.environ.get('GH_USERNAME','Bunny100806')
TOKEN=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
DEST=pathlib.Path(os.environ.get('OUTPUT_PATH','assets/activity-flight.svg'))
if not TOKEN:
    raise SystemExit('GH_TOKEN or GITHUB_TOKEN is required (never commit tokens)')
query="query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{weeks{contributionDays{date contributionCount}}}}}}"
data=json.dumps({'query':query,'variables':{'login':USERNAME}}).encode()
req=urllib.request.Request('https://api.github.com/graphql',data=data,headers={'Authorization':f'Bearer {TOKEN}','Content-Type':'application/json','User-Agent':'sai-profile-contributions'},method='POST')
with urllib.request.urlopen(req,timeout=25) as resp: result=json.load(resp)
if result.get('errors') or not result.get('data',{}).get('user'):
    raise SystemExit('GitHub GraphQL error: '+json.dumps(result.get('errors',result))[:600])
weeks=result['data']['user']['contributionsCollection']['contributionCalendar']['weeks'][-34:]
# Only use GitHub-supplied counts, never synthesized contributions.
PAD=34-len(weeks)
cols=[[{'date':None,'contributionCount':0}]*7 for _ in range(PAD)]
for w in weeks:
    days=w.get('contributionDays',[])
    cols.append(days + [{'date':None,'contributionCount':0}]*max(0,7-len(days)))
cols=cols[:34]
counts=[int(d.get('contributionCount',0)) for col in cols for d in col]
max_count=max([1]+counts)
# The sum is for the rendered 34-week portion only, and not labeled an annual total.
colors=['#301322','#62213e','#923554','#c26389','#f2b5d0']
def esc(v):return html.escape(str(v),quote=True)
svg=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="345" viewBox="0 0 1200 345" role="img" aria-label="Animated flight over true GitHub contribution cells">
<defs><linearGradient id="realbg" x2="1" y2="1"><stop stop-color="#10070C"/><stop offset="1" stop-color="#330F21"/></linearGradient><filter id="shadow"><feGaussianBlur stdDeviation="3"/></filter></defs>
<rect width="1200" height="345" rx="20" fill="url(#realbg)"/><rect x="18" y="18" width="1164" height="309" rx="11" fill="none" stroke="#D59BB7" stroke-opacity=".26"/>
<text x="61" y="63" font-family="Arial,sans-serif" font-size="14" letter-spacing="3" fill="#E5B5C7">08  /  ACTIVITY IN THE OPEN</text>
<text x="61" y="123" font-family="Georgia,serif" font-size="49" fill="#F8F0F3">A trail of real contributions.</text>
<text x="62" y="161" font-family="Arial,sans-serif" font-size="17" fill="#B78D9F">GitHub public contribution calendar  ·  last 34 weeks  ·  refreshed automatically</text>''']
for c,col in enumerate(cols):
 for r,d in enumerate(col[:7]):
    ct=int(d.get('contributionCount',0)); idx=0 if ct==0 else min(4,1+int(ct/max_count*3))
    x=61+c*31;y=192+r*18; color=colors[idx]
    svg.append(f'<rect x="{x}" y="{y}" width="23" height="12" rx="2" fill="{color}"/>')
# Purposefully avoid claiming jet changes graph data; aircraft is only decorative overlay.
svg.append('''<path d="M50 184 H1150" stroke="#D0A0B4" stroke-width=".7" stroke-opacity=".26" stroke-dasharray="2 12"/>
<g><path d="M-16 0 L8 -6 26 0 8 6 Z M-5 -3 L-14 -19 0 -6 M-5 3 L-14 19 0 6" fill="#F8EFF3" stroke="#F4B6D1" stroke-width="1"/>
<path d="M-18 0 H-88" fill="none" stroke="#E5B5C7" stroke-width="3" stroke-opacity=".7" stroke-dasharray="2 7"/>
<animateTransform attributeName="transform" type="translate" values="74 180;1093 180;74 180" dur="16s" repeatCount="indefinite"/></g>
<text x="1133" y="329" text-anchor="end" font-family="monospace" font-size="11" letter-spacing="1.2" fill="#C49BAE">DATA: GITHUB GRAPHQL • VISUAL FLIGHT: DECORATIVE</text></svg>''')
DEST.parent.mkdir(parents=True,exist_ok=True); DEST.write_text(''.join(svg),encoding='utf8')
print('Updated',DEST,'with real public contribution days,',sum(counts),'contributions in displayed 34-week interval')
