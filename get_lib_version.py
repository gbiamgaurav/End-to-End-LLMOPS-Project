import importlib.metadata

def read_requirements(file_path="requirements.txt"):
    packages = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                pkg = line.split("==")[0].split(">=")[0].split("<=")[0].strip()
                if pkg:
                    packages.append(pkg)
    return packages

packages = read_requirements()

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")
        