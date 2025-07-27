import os
import uuid
import subprocess

SCANS_DIR = os.path.join(os.path.dirname(__file__), '..', 'scans')

def run_zap_scan(url: str) -> dict:
    # Generate a unique scan ID
    scan_id = str(uuid.uuid4())
    output_file = os.path.join(SCANS_DIR, f"{scan_id}.html")

    try:
        # Ensure scans folder exists
        os.makedirs(SCANS_DIR, exist_ok=True)

        # Run ZAP scan using Docker or installed CLI
        command = [
            "zap-cli", "quick-scan", "--self-contained",
            "--start-options", "-config api.disablekey=true",
            "--spider", "--scanners", "xss,sqli",
            "--report", output_file,
            url
        ]

        subprocess.run(command, check=True)

        return {
            "status": "completed",
            "scan_id": scan_id,
            "report_path": f"/scans/{scan_id}.html"
        }
    except subprocess.CalledProcessError:
        return {
            "status": "failed",
            "message": "Scan process failed. Make sure ZAP CLI is installed and functional."
        }
