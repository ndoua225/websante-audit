import dns.resolver

def check(domain):
    res = {"spf":"","dmarc":"","dkim":[],"mx":"","error":None}
    try:
        for r in dns.resolver.resolve(domain, "TXT"):
            txt = r.to_text()
            if "v=spf1" in txt: res["spf"]=txt
            if "v=DMARC1" in txt: res["dmarc"]=txt
        for sel in ["default","google","selector1","selector2","k1"]:
            try:
                dns.resolver.resolve(f"{sel}._domainkey.{domain}", "TXT")
                res["dkim"].append(sel)
            except: pass
        for r in dns.resolver.resolve(domain, "MX"):
            res["mx"] += str(r.exchange)+" "
    except Exception as e:
        res["error"] = str(e)
    return res
