import os, json

def write(result_json, out_path="reports/report.html"):
    html = "<html><body><h1>WebSanté Audit</h1><pre>" + json.dumps(result_json, ensure_ascii=False) + "</pre></body></html>"
    with open(out_path,"w",encoding="utf-8") as f: f.write(html)
    return out_path
