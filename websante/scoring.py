def score(http, tls, dns, whois):
    pts=0; details={}
    # règles fixes : chaque zone compte, non vérifié = 0
    for zone, data in [("http",http),("tls",tls),("dns",dns),("whois",whois)]:
        ok = not data.get("error") and (zone!="http" or data.get("https_redirect"))
        pts += 25 if ok else 0
        details[zone] = {"status":"réussi" if ok else ("non vérifié" if data.get("error") else "échec"),"points":25 if ok else 0,"proof":str(data)}
    return {"score":pts,"details":details,"note":pts}
