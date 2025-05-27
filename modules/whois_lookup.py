import whois
import logging

def run(domain):
    try:
        w = whois.whois(domain)
        return {
            'domain_name': w.domain_name,
            'registrar': w.registrar,
            'creation_date': str(w.creation_date),
            'expiration_date': str(w.expiration_date),
            'name_servers': w.name_servers
        }
    except Exception as e:
        logging.error(f"WHOIS lookup failed: {str(e)}")
        return {'error': str(e)}