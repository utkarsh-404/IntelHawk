import requests
import os

def run(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719")
        data = response.json()
        return {
            'country': data.get('country'),
            'region': data.get('regionName'),
            'city': data.get('city'),
            'zip': data.get('zip'),
            'lat': data.get('lat'),
            'lon': data.get('lon'),
            'isp': data.get('isp')
        }
    except Exception as e:
        return {'error': str(e)}