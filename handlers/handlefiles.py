import json



def loadconfig():
    with open("./config.json") as f:
        configs = json.load(f)
    return configs


def load_bad_words():
    with open("data/bad_words.json") as f:
        data = json.load(f)
    return data["BadWords"]


def get_server_prefix(client, message):
    with open("data/prefixes.json") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


def load(file):
    with open(f"data/{file}") as f:
        data = json.load(f)
    return data


def commit(data, file):
    with open(f"data/{file}", "w") as f:
        json.dump(data, f, indent=4)