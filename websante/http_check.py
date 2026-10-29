import requests, time

def check(domain):
    results = {"https_redirect": False, "headers": {}, "cookies": [], "tech": None, "error": None}
    urls = [f"http://{domain}", f"https://{domain}"]
    try:
        for url in urls:
            r = requests.get(url, allow_redirects=True, timeout=10, headers={"User-Agent":"WebSanteAudit/1.0"})
            if r.url.startswith("https://") and url.startswith("http://"):
                results["https_redirect"] = True
            results["headers"] = dict(r.headers)
            for c in r.cookies:
                results["cookies"].append({"name":c.name,"secure":c.secure,"httponly":c.has_nonstandard_attr("HttpOnly"),"samesite":c.get_nonstandard_attr("SameSite")})
            srv = r.headers.get("Server","")
            if "WordPress" in srv or "wp-content" in r.text[:5000]:
                results["tech"] = "WordPress"
            if results["https_redirect"]:
                break
    except Exception as e:
        results["error"] = str(e)
    return results
