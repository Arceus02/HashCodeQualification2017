from src import extract
import math

def solver_endpoints(path):
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = extract.extract(path)
    condition_arret = False
    videos_sorted = sort_videos_by_request(requests)  # pour chaque endpoint, liste des videos par ordre de requests maximal
    server_sorted_by_latence=sort_endpoints_by_latency(endpoints)

    while not condition_arret:
        for i in range len(endpoints):
            add_done=False
            serv_min = serv_latence_min(i)  # serveur de latence minimale par rapport au endpoint i
            if serv_min != -1: #serv_min =-1 s'il n'y a pas de serveur connecte a ce endpoint
                j = 0  # tentatives d'ajout
                while j < 4 and not add_done: #4 tentatives max avant de passer au serveur suivant
                    if videos_sorted[i][j] not in serv_min_vids:  # video avec le plus de requetes pour l'endpoint i
                        ajouter_vid(serv_min)  # n'ajoute pas si ca depasse la taille du serveur
                        add_done = True
                        delete_vid[i][j]  # on supprime la video de la liste des plus populaires vu qu'elle est accessible
                    else:
                        j += 1  # on tente d'inserer la video du rang d'apres

def sort_videos_by_request(requests):
    result = []
    requests_t = list(map(list, zip(*requests)))
    for i_endpoint, requests_by_endpoint in enumerate(requests_t):
        requests_in_endpoint = [[i, amount] for i, amount in enumerate(requests_t[i_endpoint]) if amount > 0]
        result.append([data[0] for data in sorted(requests_in_endpoint, key=lambda data: -data[1])])
    return result

def sort_endpoints_by_latency(endpoints):
    result = []
    for i_endpoint, endpoints in enumerate(endpoints):
        servers_to_endpoint_latency = endpoints[1]
        servers = [[i, latency] for i, latency in enumerate(servers_to_endpoint_latency) if latency != math.inf]
        result.append([data[0] for data in sorted(servers, key=lambda data: data[1])])
    return result



if __name__ == "__main__":
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = extract.extract(extract.names[0])
    result = sort_videos_by_request(requests)
    print(result)