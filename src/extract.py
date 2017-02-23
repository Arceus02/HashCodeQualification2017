import math

files_path = ["../input/kittens.in", "../input/me_at_the_zoo.in", "../input/trending_today.in", "../input/videos_worth_spreading.in"]

def extract(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        data0 = [int(item) for item in lines[0].split(" ")]
        n_videos = data0[0]
        n_endpoints = data0[1]
        n_requests = data0[2]
        n_servers = data0[3]
        server_space = data0[4]
        video_sizes = [int(item) for item in lines[1].split(" ")]
        line_cursor = 1
        endpoints = [[0, [math.inf for k in range(n_servers)]] for k in range(n_endpoints)]
        requests = [[0 for k in range(n_endpoints)] for l in range(n_videos)]
        for i_endpoint in range(n_endpoints):
            line_cursor += 1
            data_endpoint = [int(item) for item in lines[line_cursor].split(" ")]
            n_servers_to_endpoint = data_endpoint[1]
            endpoints[i_endpoint][0] = data_endpoint[0]
            for i_server_endpoint in range(n_servers_to_endpoint):
                line_cursor += 1
                data_server_to_endpoint = [int(item) for item in lines[line_cursor].split(" ")]
                endpoints[i_endpoint][1][data_server_to_endpoint[0]] = data_server_to_endpoint[1]
        for i_request in range(n_requests):
            line_cursor += 1
            data_request = [int(item) for item in lines[line_cursor].split(" ")]
            video_id = data_request[0]
            endpoint_id = data_request[1]
            amount = data_request[2]
            requests[video_id][endpoint_id] = amount

    return n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests

if __name__ == "__main__":
    data = list(extract("../input/test.in"))
    for k in data:
        print(k)