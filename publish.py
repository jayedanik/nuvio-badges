import os
import subprocess
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_cmd(cmd):
    print(f">> Running: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=BASE_DIR, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip())
    return res.returncode == 0

def main():
    if len(sys.argv) > 1:
        username = sys.argv[1].strip()
    else:
        username = input("Enter your GitHub username: ").strip()

    if not username:
        print("GitHub username is required!")
        return

    repo_name = "nuvio-badges-original"

    print(f"\n[1/4] Updating badges.json for GitHub user '{username}'...")
    import build_manifest
    build_manifest.build_manifest(username=username, repo=repo_name, branch="main")

    print("\n[2/4] Configuring Git...")
    run_cmd(f'git config user.name "{username}"')
    run_cmd(f'git config user.email "{username}@users.noreply.github.com"')

    print("\n[3/4] Staging and committing files...")
    run_cmd("git add .")
    run_cmd('git commit -m "feat: Add official Nuvio original logo badges and manifest"')

    remote_url = f"https://github.com/{username}/{repo_name}.git"
    print(f"\n[4/4] Setting remote origin to {remote_url}...")
    run_cmd("git remote remove origin")
    run_cmd(f"git remote add origin {remote_url}")

    print("\nPushing to GitHub (A browser window may open once to confirm your GitHub login via Git Credential Manager)...")
    success = run_cmd("git push -u origin main")

    if success:
        print("\n=======================================================")
        print("SUCCESS! Your Nuvio badge kit is live!")
        print("Your Nuvio Fusion Badge URL:")
        print(f"https://cdn.jsdelivr.net/gh/{username}/{repo_name}@main/badges.json")
        print("=======================================================")
    else:
        print("\nTip: Make sure you have created an empty public repository named:")
        print(f"     'nuvio-badges-original' on https://github.com/new")
        print("Then run this script again or run: git push -u origin main")

if __name__ == "__main__":
    main()
