import math


def sort_server(server_id_list, data):
    pass


def get_score_server(server_id, data):
    """
    :param server_id:
    :param data:
    :return:
    """
    pass


def get_endpoints_by_server(server_id, data):
    """
    Liste les endpoints connects au serveur [[id0,latence0],..]
    :param server_id:
    :param data:
    :return:
    """

    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = data

    # Parcourir les endpoints et ajouter leur id si ceux ci sont connects au serveur_id

    server_endpoints = []

    for endpoint_id in range(len(endpoints)):
        endpoint = endpoints[endpoint_id]
        servers_list = endpoint[1]
        for current_server_id in range(len(servers_list)):
            if (current_server_id == server_id and server_list[current_server_id] != inf):
                server_endpoints.append([endpoint_id, servers_list[current_server_id]])

    return server_endpoints


def get_requests_by_endpoint(endpoint_id, data):
    """

    :param endpoint_id:
    :param data:
    :return:
    """
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = data

    videos = [0 for k in range(n_videos)]

    for request_id in range(n_requests):
        for video_id in range(n_videos):
            videos[video_id] += requests[video_id][endpoint_id]

    videos_clean = []
    for video_id in range(n_videos):
        if videos[video_id] > 0:
            videos_clean.append([video_id, videos[video_id]])

    return videos_clean


def solver(data):
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = data
    score = []
    sortie = []
    for icache in range(n_servers):
        sortie_i = []
        score = [0 for k in range(n_videos)]
        # cache=liste_cache[icache]
        liste_endpoint = get_endpoints_by_server(icache, data)
        place_restante = server_space

        sortie_i += [icache]

        for endpoint in liste_endpoint:
            iendpoint = endpoint[0]
            ping_end = endpoint[1]
            liste_video = get_requests_by_endpoint(endpoint[0], data)
            for ivideo in range(len(liste_video)):
                j = liste_video[ivideo][0]
                score[j] += (liste_video[ivideo][1]) * (endpoints[iendpoint][0] - ping_end) / (video_sizes[j])

        for k in range(n_videos):
            score[k] = [k, score[k]]
        score = sorted(score, key=lambda score: score[1])

        for k in range(n_videos):
            if (place_restante >= video_sizes[score[k][0]]):
                sortie_i += [score[k][0]]
                place_restante -= video_sizes[score[k][0]]
            if (score[k][1] == 0):
                break
        sortie += [sortie_i]
    return (sortie)

if __name__ == "__main__":
    import extract
    import solver

    data = extract.extract("kittens")

    sortie = solver(data)
    print
    sortie