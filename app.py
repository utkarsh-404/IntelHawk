import os
import logging
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from modules import (
    subdomain_enum, nmap_scan, whois_lookup,
    email_harvest, tech_detect, geo_ip,
    breach_check, virustotal_check
)

load_dotenv()
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = os.urandom(24)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('IntelHawk')

MODULE_MAP = {
    'nmap': nmap_scan,
    'breach': breach_check,
    'whois': whois_lookup,
    'subdomains': subdomain_enum,
    'email': email_harvest,
    'tech': tech_detect,
    'virustotal': virustotal_check,
    'geoip': geo_ip
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan/<module_name>', methods=['POST'])
def handle_scan(module_name):
    try:
        data = request.get_json()
        target = data.get('target', '').strip()
        
        if not target:
            return jsonify({'error': 'No target specified'}), 400
            
        if module_name not in MODULE_MAP:
            return jsonify({'error': 'Invalid module'}), 400
            
        logger.info(f"Starting {module_name} scan for {target}")
        result = MODULE_MAP[module_name].run(target)
        return jsonify(result)

    except Exception as e:
        logger.error(f"{module_name} scan failed: {str(e)}", exc_info=True)
        return jsonify({
            'error': str(e),
            'module': module_name,
            'target': target
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)