import requests
import os
import time

def run(target):
    try:
        api_key = os.getenv('VIRUSTOTAL_API_KEY')
        headers = {'x-apikey': api_key}
        
        # Get URL/Domain report
        response = requests.get(
            f'https://www.virustotal.com/api/v3/domains/{target}',
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            return {
                'harmless': data['data']['attributes']['last_analysis_stats']['harmless'],
                'malicious': data['data']['attributes']['last_analysis_stats']['malicious'],
                'suspicious': data['data']['attributes']['last_analysis_stats']['suspicious']
            }
        elif response.status_code == 404:
            return {'error': 'Not found in VirusTotal database'}
        else:
            return {'error': f"API error: {response.status_code}"}
            
    except Exception as e:
        return {'error': str(e)}