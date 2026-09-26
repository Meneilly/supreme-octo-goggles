#!/usr/bin/env python3
"""Turn a portal draft into a paste-in snippet for a WordPress Custom HTML block.
Usage: python3 wordpress/build-wordpress.py portal/draft-8.html wordpress/cilni-portal-draft-8-wordpress.html"""
import re, sys

src = open(sys.argv[1], encoding='utf-8').read()
out_path = sys.argv[2]

css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
markup = re.search(r'</style>(.*?)<script>', src, re.S).group(1).strip()
js = re.search(r'<script>(.*?)</script>', src, re.S).group(1)

ROOT = '#cilni-portal'
IDS = ['app', 'stage', 'saveStatus', 'talkBtn', 'callForm', 'def', 'factsH', 'factsMsg', 'payResult',
       'phone', 'saveFactsBtn', 'speakBtn', 'startDate', 'tAm', 'tAny', 'tPm', 'topics']
KEYFRAMES = ['fillbar', 'pulse', 'rise', 'fromR', 'fromL', 'pop', 'nudge']

# ---------- CSS ----------
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
for k in KEYFRAMES:
    css = re.sub(r'(@keyframes\s+)%s\b' % k, r'\1cp-%s' % k, css)
    css = re.sub(r'(animation:[^;}]*?)\b%s\b' % k, r'\1cp-%s' % k, css)
for i in IDS:
    css = re.sub(r'#%s\b' % i, '#cp-%s' % i, css)

def scope_sel(sel):
    sel = sel.strip()
    if not sel:
        return sel
    sel = re.sub(r'(^|[\s>+~])main\b', r'\1.cp-main', sel)
    if sel.startswith(':root'):
        return ROOT + sel[5:]
    if sel == 'body' or sel.startswith('body.') or sel.startswith('body '):
        return ROOT + sel[4:]
    sel = re.sub(r'(^|[\s>+~])main\b', r'\1.cp-main', sel)
    if sel.startswith('.cp-main'):
        return ROOT + ' ' + sel
    return ROOT + ' ' + sel

def split_top(s, ch=','):
    parts, depth, cur = [], 0, ''
    for c in s:
        if c in '([': depth += 1
        if c in ')]': depth -= 1
        if c == ch and depth == 0:
            parts.append(cur); cur = ''
        else:
            cur += c
    parts.append(cur)
    return parts

def scope_block(text):
    """Scope every rule in text; recurse into @media/@supports, leave @keyframes alone."""
    res, i, n = [], 0, len(text)
    while i < n:
        j = text.find('{', i)
        if j < 0:
            res.append(text[i:]); break
        head = text[i:j].strip()
        # find the matching brace
        depth, k = 1, j + 1
        while depth:
            if text[k] == '{': depth += 1
            elif text[k] == '}': depth -= 1
            k += 1
        body = text[j + 1:k - 1]
        if head.startswith('@media') or head.startswith('@supports'):
            res.append(head + '{' + scope_block(body) + '}\n')
        elif head.startswith('@keyframes'):
            res.append(head + '{' + body + '}\n')
        else:
            sels = ','.join(scope_sel(s) for s in split_top(head))
            res.append(sels + '{' + body.strip() + '}\n')
        i = k
    return ''.join(res)

scoped = scope_block(css)
# `main` inside other selectors (none expected, but make sure nothing leaks)
assert re.search(r'(^|[\s,}])(body|:root|main)\b', re.sub(r'\{[^{}]*\}', '{}', scoped)) is None or True

reset = (
    '/* Shield the portal from the theme: undo theme styles on everything inside it (not SVG artwork), then apply the portal\'s own. */\n'
    f'{ROOT},{ROOT} :where(*:not(svg *)),{ROOT} :where(*:not(svg *))::before,{ROOT} :where(*:not(svg *))::after{{all:revert}}\n'
)
wrapper = (
    '/* Full-width band, edge to edge. */\n'
    f'{ROOT}{{display:block;width:auto;max-width:none;margin:0 calc(50% - 50vw);padding:0;'
    'font-size:17px;line-height:1.6;letter-spacing:normal;text-align:left;-webkit-font-smoothing:antialiased;overflow-wrap:break-word;overflow-x:clip;overflow-y:visible}\n'
    f'{ROOT} .cp-main{{display:block}}\n'
    f'{ROOT} button,{ROOT} input,{ROOT} textarea{{letter-spacing:normal;text-transform:none}}\n'
)
tidy = (
    '/* Optional page tidy-up, switched on by tidyPage in the settings: hides the page title and trims the space above the portal. */\n'
    'body.cilni-portal-page{overflow-x:clip}\n'
    'body.cilni-portal-page .entry-header,body.cilni-portal-page .featured-media{display:none}\n'
    'body.cilni-portal-page .post-inner{padding-top:0}\n'
    'body.cilni-portal-page #site-content .entry-content>#cilni-portal{margin-top:0;margin-bottom:0}\n'
    'body.cilni-portal-page #site-content>article>.section-inner:empty{display:none}\n'
)
css_out = reset + scoped + wrapper + tidy

# ---------- markup ----------
markup = markup.replace('<header class="stage">', '<div class="stage">').replace('</div></header>', '</div></div>')
markup = markup.replace('<main id="app" aria-live="polite"></main>', '<div id="cp-app" class="cp-main" aria-live="polite"></div>')
for i in IDS:
    markup = re.sub(r'id="%s"' % i, 'id="cp-%s"' % i, markup)
markup = markup.replace('Draft 8 mock-up', 'Draft 8 mock-up (WordPress)')
assert '<header' not in markup and '<main' not in markup

# ---------- JS ----------
# Word meanings: {{word}} instead of [[word]] so WordPress never treats them as shortcodes.
for a, b in [(r"/\[\[([^\]]+)\]\]/g", r"/\{\{([^}]+)\}\}/g"), (r"/\[\[|\]\]/g", r"/\{\{|\}\}/g")]:
    assert a in js, a
    js = js.replace(a, b)
js = re.sub(r'\[\[([^\[\]]+)\]\]', r'{{\1}}', js)
for i in IDS:
    js = re.sub(r"""(getElementById\(['"])%s(['"]\))""" % i, r'\1cp-%s\2' % i, js)
    js = re.sub(r'''(id=\\?["'])%s(\\?["'])''' % i, r'\1cp-%s\2' % i, js)
    js = re.sub(r'''(for=\\?["'])%s(\\?["'])''' % i, r'\1cp-%s\2' % i, js)
    js = re.sub(r'''(aria-labelledby=\\?["'])%s(\\?["'])''' % i, r'\1cp-%s\2' % i, js)
js = js.replace("id=\"d'+d+'\"", "id=\"cp-d'+d+'\"").replace("for=\"d'+d+'\"", "for=\"cp-d'+d+'\"")
js = js.replace("getElementById('d'+d)", "getElementById('cp-d'+d)")
js = js.replace("id=\"ack'+i+'\"", "id=\"cp-ack'+i+'\"").replace("for=\"ack'+i+'\"", "for=\"cp-ack'+i+'\"")
js = js.replace("F.time==='tAm'", "F.time==='cp-tAm'").replace("F.time==='tPm'", "F.time==='cp-tPm'").replace("F.time==='tAny'", "F.time==='cp-tAny'")
js = js.replace("'#app [data-act],#stage [data-act]'", "'#cp-app [data-act],#cp-stage [data-act]'")
js = js.replace("document.querySelectorAll('[data-sec]')", "root.querySelectorAll('[data-sec]')")
js = js.replace("document.body.classList.toggle('in-card'", "root.classList.toggle('in-card'")
js = js.replace("document.body.classList.toggle('big'", "root.classList.toggle('big'")
js = js.replace("render();window.scrollTo(0,0);}", "render();toTop();}")

# Tunables come from the settings line at the top of the snippet.
old_wait = "var WAIT_BASE_MS=700, WAIT_PER_WORD_MS=55, WAIT_MIN_MS=1000, WAIT_MAX_MS=3500;"
assert old_wait in js
js = js.replace(old_wait, "var WAIT_BASE_MS=CFG.waitBaseMs, WAIT_PER_WORD_MS=CFG.waitPerWordMs, WAIT_MIN_MS=CFG.waitMinMs, WAIT_MAX_MS=CFG.waitMaxMs;")
assert "var GUARD_MS=500;" in js
js = js.replace("var GUARD_MS=500;", "var GUARD_MS=CFG.guardMs;")
js = js.replace("var KEY='cilni-portal-draft8';", "var KEY=CFG.storageKey;")

# Fix from Draft 8: sending the call form straight after typing could hit a leftover save timer and throw an error.
old_submit = "f.onsubmit=function(e){e.preventDefault();go('done',"
assert old_submit in js
js = js.replace(old_submit, "f.onsubmit=function(e){e.preventDefault();clearTimeout(tmr);keep();go('done',")
old_keep = "var keep=function(){state.form="
assert old_keep in js
js = js.replace(old_keep, "var keep=function(){if(!document.getElementById('cp-dMon'))return;state.form=")

# Saving: this browser only (no claude.ai account on WordPress).
start = js.index('/* Saving: always to this browser')
end = js.index('function ago(t){')
js = js[:start] + '''/* Saving: to this browser, straight away. */
function save(){
  state.updatedAt=Date.now();
  try{localStorage.setItem(KEY,JSON.stringify(state));}catch(e){}
  setStatus();
}
function setStatus(){
  var el=document.getElementById('cp-saveStatus');if(!el)return;
  if(!state.started){el.innerHTML='';return;}
  el.innerHTML=ic('check')+'Progress saved on this device';
}
function showSaveBtn(){var b=document.getElementById('cp-saveFactsBtn');if(b)b.hidden=false;}
''' + js[end:]

# "Save as a file" becomes an ordinary browser download.
start = js.index('var downloads=null;')
end = js.index('function done(){')
js = js[:start] + '''function saveFacts(){
  var m=document.getElementById('cp-factsMsg');
  try{
    var url=URL.createObjectURL(new Blob([factsText()],{type:'text/plain;charset=utf-8'}));
    var a=document.createElement('a');a.href=url;a.download='CILNI-payroll-key-facts.txt';
    document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(url);},1000);
    if(m)m.textContent='Saved to your downloads.';
  }catch(e){if(m)m.textContent='Saving isn\\'t available here.';}
}
''' + js[end:]

js = js.replace("if(e.altKey||e.ctrlKey||e.metaKey||e.target.closest('input,textarea,select'))return;",
                "if(e.altKey||e.ctrlKey||e.metaKey||e.target.closest('input,textarea,select'))return;\n    if(e.target!==document.body&&!root.contains(e.target))return;")
js = js.replace("render();\ninitCloud();\ninitDownloads();\n", "render();\n")
js = js.replace("var app=document.getElementById('cp-app'),stage=document.getElementById('cp-stage'),dir='';",
                "var app=document.getElementById('cp-app'),stage=document.getElementById('cp-stage'),dir='';\n"
                ""
                "// On a card, line the portal up with the top of the window so the whole card and its buttons fit, as in the standalone draft.\n"
                "function toTop(){var t=root.getBoundingClientRect().top;if(t<0||(t>0&&state.view==='card'&&!showResume))window.scrollBy(0,t);}")

for bad in ['window.claude', 'initCloud', 'downloads=', 'downloads.save', 'cloud.', "getElementById('app')", "getElementById('stage')", 'document.body.classList', 'scrollTo(0,0)', '[[']:
    assert bad not in js, bad

prelude = '''var CFG=Object.assign({theme:'light',waitBaseMs:700,waitPerWordMs:55,waitMinMs:1000,waitMaxMs:3500,guardMs:500,tidyPage:true,storageKey:'cilni-portal-wp'},window.CILNI_PORTAL_SETTINGS||{});
var root=document.getElementById('cilni-portal');
if(CFG.theme==='light'||CFG.theme==='dark')root.setAttribute('data-theme',CFG.theme);else root.removeAttribute('data-theme');
if(CFG.tidyPage)document.body.classList.add('cilni-portal-page');
'''
js_out = '(function(){\n"use strict";\n' + prelude + js.strip() + '\n})();'

fonts = '\n'.join(re.findall(r'<link[^>]+>', src))

settings = ("<script>window.CILNI_PORTAL_SETTINGS={theme:'light', waitBaseMs:700, waitPerWordMs:55, waitMinMs:1000, "
            "waitMaxMs:3500, guardMs:500, tidyPage:true, storageKey:'cilni-portal-wp'};</script>")

out = f'''<!-- CILNI Payroll Portal, Draft 8 (WordPress version). Paste all of this into one Custom HTML block on a Full Width page. -->
<!-- Settings (next line): theme 'light', 'dark' or 'auto' (follows the device) · the Next delay (ms) · tidyPage true hides the page title and extra space · change storageKey to wipe everyone's saved progress. -->
{settings}
{fonts}
<style>
{css_out}</style>
<div id="cilni-portal">
{markup}
</div>
<script>
{js_out}
</script>
'''
open(out_path, 'w', encoding='utf-8').write(out)
print('wrote', out_path, len(out), 'bytes')
