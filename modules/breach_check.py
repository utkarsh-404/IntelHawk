import subprocess
import re
import os

def run(email):
    try:
        # Use absolute path to Breach-Checker
        breach_path = os.path.expanduser("~/Breach-Checker")
        cmd = f"cd {breach_path} && python -m bchecker -m 1 -e {email} -v y"
        
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Clean output
        clean_output = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', result.stdout)
        
        return {'result': clean_output}

    except Exception as e:
        return {'error': f"{str(e)}\nVerify Breach-Checker exists at ~/Breach-Checker"}