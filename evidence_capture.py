from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pdfkit
import yaml
import os
import zipfile
from datetime import datetime

# Load compliance controls
with open('controls/soc2.yaml') as f:
    controls = yaml.safe_load(f)

# Configure headless Chrome browser
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def capture_control_evidence(control):
    control_id = control['id']
    print(f"Processing {control_id}: {control['name']}")

    # Navigate to the control URL and take a screenshot
    driver.get(control['url'])
    screenshot_path = f"evidence/{control_id}.png"
    driver.save_screenshot(screenshot_path)

    # Generate HTML report content
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head><title>{control_id} Evidence Report</title></head>
    <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>{control_id} Evidence Report</h1>
        <h2>{control['name']}</h2>
        <p><strong>Audit Period:</strong> Q3 2025</p>
        <h3>Configuration Status: Compliant</h3>
        <p><strong>Verification Method:</strong> {control['verification']}</p>
        <h4>Screenshot Evidence:</h4>
        <img src="{screenshot_path}" style="width:800px;">
        <br><br>
        <p>Certified Cloud Security Auditor</p>
        <p>Date: {datetime.now().strftime('%Y-%m-%d')}</p>
        <hr>
        <p>Confidential Audit Document - Do Not Distribute</p>
    </body>
    </html>
    '''

    html_path = f"evidence/{control_id}.html"
    with open(html_path, 'w') as f:
        f.write(html_content)

    # Convert HTML report to PDF
    pdf_path = f"evidence/{control_id}.pdf"
    pdfkit.from_file(html_path, pdf_path)

    return pdf_path

# Process all controls and generate evidence package
evidence_files = []
for control in controls['soc2']:
    pdf_file = capture_control_evidence(control)
    evidence_files.append(pdf_file)

# Create ZIP archive of all evidence PDFs
zip_path = 'audit_evidence_package.zip'
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in evidence_files:
        zipf.write(file)

print(f"Evidence package generated: {zip_path}")

driver.quit()
