import re, socket, ipaddress

def validate(domain):
    d = domain.strip().lower()
    if not d or "/" in d or d.startswith("http") or d.startswith("www."):
        return False, "URL ou chemin détecté"
    if d in ("localhost","127.0.0.1","::1") or d.startswith("192.168.") or d.startswith("10."):
        return False, "IP privée / réservée"
    if not re.match(r"^[a-z0-9.-]+\.[a-z]{2,}$", d):
        return False, "Format invalide"
    try:
        ip = socket.getaddrinfo(d, None)[0][4][0]
        if ipaddress.ip_address(ip).is_private:
            return False, "Résout vers IP privée"
    except Exception as e:
        return False, f"Résolution échouée: {e}"
    return True, d
