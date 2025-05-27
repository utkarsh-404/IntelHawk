import subprocess
import re

def clean_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def run(url):
    try:
        result = subprocess.run(
            ['whatweb', '--color=never', url],  # Disable colors
            capture_output=True,
            text=True,
            timeout=120
        )
        
        cleaned = clean_ansi_codes(result.stdout)
        technologies = [line.strip() for line in cleaned.split('\n') if line.strip()]
        
        return {'technologies': technologies}
    except Exception as e:
        return {'error': str(e)}