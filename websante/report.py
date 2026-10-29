from websante.writer import write
from websante.scoring import score

def generate(domain, http, tls, dns, whois):
    res = score(http, tls, dns, whois)
    res["domain"]=domain; res["json_path"]=f"reports/{domain}_raw.json"
    import json
    with open(res["json_path"],"w") as f: json.dump(res, f, ensure_ascii=False)
    html = write(res, f"reports/{domain}_report.html")
    return res, html
