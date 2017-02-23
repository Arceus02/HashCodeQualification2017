def get_path(name):
    return "../output/" + name + ".txt"

def export(name, videos_by_servers):
    output = ""
    output += str(len(videos_by_servers)) + "\n"
    for i_cache, videos in enumerate(videos_by_servers):
        if len(videos) > 0:
            output += str(i_cache) + " "
            output += " ".join(map(str,videos))
            output += "\n"
    with open(get_path(name), 'w') as file:
        file.write(output)

if __name__ == "__main__":
    export("test", [[2], [1, 3], [0, 1]])