#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from websante.validation import validate
from websante.http_check import check as http_check
from websante.tls_check import check as tls_check
from websante.dns_check import check as dns_check
from websante.whois_check import check as whois_check
from websante.report import generate
def main():
    d = sys.argv[1] if len(sys.argv)>1 else ""
    ok, msg = validate(d)
    if not ok: print("REFUS:", msg); sys.exit(1)
    r = {"domain": msg, "http": http_check(msg), "tls": tls_check(msg), "dns": dns_check(msg), "whois": whois_check(msg)}
    res, html = generate(msg, r["http"], r["tls"], r["dns"], r["whois"])
    print("Audit", msg, "- Note:", res["note"], "- HTML:", html)
if __name__=="__main__": main()
