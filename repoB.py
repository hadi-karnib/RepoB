import yaml

def load_config():
    path = '../config.yaml'
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config()

if config['error_repoB']:
    print("Error_RepoB is true")
else:
    print("Running in RepoB,all is Good")
