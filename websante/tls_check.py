import ssl, socket

def check(domain, port=443):
    ctx = ssl.create_default_context()
    try:
        with socket.create_connection((domain, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                ver = ssock.version()
                exp = cert.get("notAfter") if cert else None
                return {"issuer":cert.get("issuer"),"expire":exp,"tls_ver":ver,"cipher":cipher,"valid":True,"raw":cert,"error":None}
    except Exception as e:
        return {"valid":False,"error":str(e)}
