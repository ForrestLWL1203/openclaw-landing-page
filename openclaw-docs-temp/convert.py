import markdown

with open(r'D:\openClaw\workspace\openclaw-docs-temp\openclaw学习笔记.md', 'r', encoding='utf-8') as f:
    content = f.read()

html = markdown.markdown(content, extensions=['extra', 'codehilite'])

full_html = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; line-height: 1.6; font-size: 12px; }
h1 { color: #333; border-bottom: 2px solid #333; padding-bottom: 10px; }
h2 { color: #555; margin-top: 30px; }
h3 { color: #666; }
code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }
pre { background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }
blockquote { border-left: 4px solid #ddd; margin: 0; padding-left: 20px; color: #666; }
table { border-collapse: collapse; width: 100%; margin: 20px 0; font-size: 10px; }
th, td { border: 1px solid #ddd; padding: 6px; text-align: left; }
th { background: #f4f4f4; }
img { max-width: 100%; }
</style>
</head>
<body>
''' + html + '''
</body>
</html>'''

with open(r'D:\openClaw\workspace\openclaw-docs-temp\openclaw学习笔记.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('HTML created successfully')
