# modules/subdomain_enum.py
import subprocess
import tempfile
import logging

def run(domain):
    try:
        logging.info(f"Starting subdomain scan for {domain}")
        
        with tempfile.NamedTemporaryFile() as tmp:
            cmd = [
                'sublist3r',
                '-d', domain,
                '-o', tmp.name,
                '-t', '20',
                '--no-color',
                '--verbose'  # Enable verbose mode
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )

            # Check if file exists
            try:
                with open(tmp.name) as f:
                    subs = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                return {'error': 'No subdomains found', 'debug': result.stderr}
                
            return {
                'domain': domain,
                'subdomains': subs,
                'count': len(subs)
            }

    except Exception as e:
        return {'error': str(e)}