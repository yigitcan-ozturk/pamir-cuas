#!/usr/bin/env python3
"""Fetch public Figshare metadata only; source payload download is a separate step."""
import argparse,json,urllib.request

def get_json(url):
    with urllib.request.urlopen(url,timeout=60) as r: return json.load(r)

def main():
    p=argparse.ArgumentParser(); p.add_argument("article_id",type=int); p.add_argument("--output",default="figshare_inventory.json"); a=p.parse_args()
    base=f"https://api.figshare.com/v2/articles/{a.article_id}"
    meta=get_json(base); files=get_json(base+"/files")
    out={"article_id":a.article_id,"title":meta.get("title"),"doi":meta.get("doi"),"license":meta.get("license"),"files":[{"id":f.get("id"),"name":f.get("name"),"size":f.get("size"),"download_url":f.get("download_url"),"computed_md5":f.get("computed_md5")} for f in files]}
    open(a.output,"w",encoding="utf-8").write(json.dumps(out,indent=2)+"\n")
    print(json.dumps({"files":len(out["files"]),"bytes":sum((f["size"] or 0) for f in out["files"])},indent=2))
if __name__=="__main__": main()
