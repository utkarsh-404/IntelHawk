import nmap
import logging
from datetime import datetime

def run(target):
    try:
        logging.info(f"Starting Nmap scan for {target}")
        
        scanner = nmap.PortScanner()
        scanner.scan(
            hosts=target,
            arguments='-sV -T4 -O -F --script=banner',  # Fast scan with service detection
            timeout=300  # 5 minutes timeout
        )
        
        scan_results = []
        for host in scanner.all_hosts():
            host_info = {
                'host': host,
                'status': scanner[host].state(),
                'protocols': {}
            }
            
            for proto in scanner[host].all_protocols():
                host_info['protocols'][proto] = []
                ports = scanner[host][proto].keys()
                
                for port in ports:
                    service = scanner[host][proto][port]
                    host_info['protocols'][proto].append({
                        'port': port,
                        'state': service['state'],
                        'service': service['name'],
                        'version': service['version'],
                        'product': service['product'],
                        'extra': service['extrainfo']
                    })
            
            scan_results.append(host_info)
        
        return {
            'target': target,
            'scan_start': datetime.now().isoformat(),
            'results': scan_results
        }
        
    except nmap.PortScannerError as e:
        logging.error(f"Nmap error: {str(e)}")
        return {'error': f"Nmap scan failed: {str(e)}"}
    except Exception as e:
        logging.error(f"Nmap scan error: {str(e)}")
        return {'error': str(e)}