import json,platform,sys
from pathlib import Path
from .integrity import sha256_file

def reproduction_manifest(*,case_id,source_files,code_commit,parameters,outputs,perturbation=None):
    return {
      "case_id":case_id,
      "source_files":[{"path":str(p),"sha256":sha256_file(p)} for p in source_files],
      "code_commit":code_commit,
      "parameters":parameters,
      "perturbation":perturbation,
      "outputs":[{"path":str(p),"sha256":sha256_file(p)} for p in outputs],
      "environment":{"python":sys.version.split()[0],"platform":platform.platform()},
      "reproduction_status":"RECORDED"
    }

def write_manifest(payload,path):
    Path(path).write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
