from flask import Flask, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route("/update/deneme")
def update_repo(repo_name):
    repo_url = f"https://github.com/muhammete1/{repo_name}.git"

    if not os.path.exists(repo_name):
        subprocess.run(["git", "clone", repo_url], check=True)
    else:
        os.chdir(repo_name)
        subprocess.run(["git", "pull"], check=True)
        os.chdir("..")

    return jsonify({"message": f"{repo_name} repository successfully updated"})

if __name__ == "__main__":
    app.run()
