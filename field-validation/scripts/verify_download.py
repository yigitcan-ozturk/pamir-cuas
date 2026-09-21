#!/usr/bin/env python3
import argparse,hashlib,json
from pathlib import Path

def digest(path,alg):
 h=hashlib.new(alg)
 with open(path,"rb") as f:
  for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
 return h.hexdigest()

def main():
 p=argparse.ArgumentParser(); p.add_argument("path"); p.add_argument("--expected-md5"); a=p.parse_args()
 x={"path":str(Path(a.path)),"bytes":Path(a.path).stat().st_size,"sha256":digest(a.path,"sha256"),"md5":digest(a.path,"md5")}
 x["figshare_md5_match"]=None if not a.expected_md5 else x["md5"].lower()==a.expected_md5.lower()
 print(json.dumps(x,indent=2))
if __name__=="__main__":main()
