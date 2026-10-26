import os
import subprocess

html_path = os.path.abspath("cr.html")
pdf_path = os.path.abspath("cr.pdf")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
file_url = "file:///" + html_path.replace("\\", "/")

cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    file_url
]

print(f"Compiling {html_path} -> {pdf_path}...")
res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(pdf_path):
    print(f"SUCCESS: Generated {pdf_path} (Size: {os.path.getsize(pdf_path)} bytes)")
else:
    print(f"FAILED. Return code: {res.returncode}")
    print(f"Stdout: {res.stdout}")
    print(f"Stderr: {res.stderr}")
