try:
    import whois
except ImportError:
    whois = None

def check(domain):
    if whois is None: return {"expire":None,"raw":"","error":"module whois indisponible"}
    try:
        w = whois.whois(domain)
        return {"expire":str(w.expiration_date),"raw":"","error":None}
    except Exception as e:
        return {"expire":None,"raw":"","error":str(e)}
