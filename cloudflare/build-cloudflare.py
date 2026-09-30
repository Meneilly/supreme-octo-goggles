#!/usr/bin/env python3
"""Turn a portal draft into a standalone site folder for Cloudflare Pages.
Usage: python3 cloudflare/build-cloudflare.py portal/draft-10.html cloudflare/site"""
import os, re, sys

src = open(sys.argv[1], encoding='utf-8').read()
out = sys.argv[2]
os.makedirs(out, exist_ok=True)

head, sep, body = src.partition('</style>')
assert sep and head.lstrip().startswith('<title>'), 'draft layout changed'

# Outside Claude there are no Artifact capabilities: progress is already saved in the browser,
# so the only gap is the key facts file. Save it with a plain browser download instead.
fallback = """
if(!window.claude){downloads={save:function(o){var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([o.data],{type:'text/plain'}));a.download=o.filename;document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},1000);return Promise.resolve();}};showSaveBtn();}
"""
assert body.count('</script>') == 1 and 'var downloads=null;' in body
body = body.replace('</script>', fallback + '</script>')

page = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + head.strip() + '\n</style>\n</head>\n<body>\n' + body.strip() + '\n</body>\n</html>\n')
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page)
print('wrote', os.path.join(out, 'index.html'), len(page), 'bytes')
