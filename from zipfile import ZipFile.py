from zipfile import ZipFile
from pathlib import Path

# HTML and CSS content
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rashed</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div class="container">
    <h1>Hi, I'm Rashed</h1>
    <p>Welcome to my personal website.</p>
  </div>
</body>
</html>
"""

style_css = """/* style.css */
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background: #f5f5f5;
  color: #333;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  text-align: center;
}

h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1.2rem;
  color: #666;
}
"""

# Create directory and files
Path("rashed_website").mkdir(exist_ok=True)
Path("rashed_website/index.html").write_text(index_html)
Path("rashed_website/style.css").write_text(style_css)

# Zip the folder
with ZipFile("rashed_website.zip", "w") as zipf:
    zipf.write("rashed_website/index.html", arcname="index.html")
    zipf.write("rashed_website/style.css", arcname="style.css")

print("rashed_website.zip created on your desktop (or script location)!")
 