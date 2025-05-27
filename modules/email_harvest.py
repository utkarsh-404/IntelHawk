import subprocess
import tempfile
import json
import re

def run(target):
    try:
        # Clean input to domain only
        domain = re.sub(r'^https?://(www\.)?', '', target).split('/')[0]
        
        with tempfile.NamedTemporaryFile() as tmp:
            cmd = [
                'theHarvester',
                '-d', domain,
                '-b', 'google,bing,linkedin',
                '-f', tmp.name,
                '--json'
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if "0 hosts found" in result.stdout:
                return {'domain': domain, 'emails': [], 'message': 'No emails found'}
            
            try:
                with open(f"{tmp.name}.json") as f:
                    data = json.load(f)
                    return {
                        'domain': domain,
                        'emails': data.get('emails', []),
                        'hosts': data.get('hosts', [])
                    }
            except:
                return {'error': 'Failed to parse results'}

    except Exception as e:
        return {'error': str(e)}