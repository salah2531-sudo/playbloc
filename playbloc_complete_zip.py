import zipfile, os

# Base directory for PLAYBLOC complete platform
base_dir = "/mnt/data/playbloc_complete"
os.makedirs(base_dir, exist_ok=True)

# Files content
files = {
    "index.html": """<!DOCTYPE html>
<html lang=\"fr\">
<head>
<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>PLAYBLOC - Hub</title>
<style>
body{margin:0;font-family:Arial;background:#111;color:white;text-align:center}
a{display:block;margin:20px auto;padding:20px;background:#ff4d4d;color:white;text-decoration:none;width:260px;border-radius:16px;font-size:18px}
</style>
</head>
<body>
<h1>🎮 PLAYBLOC</h1>
<p>Bienvenue sur la plateforme</p>
<a href=\"oneblock.html\">▶ ONE BLOCK</a>
<a href=\"avatar.html\">🧍 Éditeur d’avatar</a>
</body>
</html>""",

    "avatar.html": "<!-- Avatar editor -->\nVoir version complète déjà fournie",
    "oneblock.html": "<!-- ONE BLOCK placeholder -->\nVoir version complète déjà fournie"
}

# Create the files
for filename, content in files.items():
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Create ZIP file
zip_path = "/mnt/data/PLAYBLOC_COMPLETE.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files_in_dir in os.walk(base_dir):
        for f in files_in_dir:
            full_path = os.path.join(root, f)
            z.write(full_path, arcname=f)

zip_path