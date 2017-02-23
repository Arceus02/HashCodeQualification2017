from src import extract
import math


def solver_endpoints(path):
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = extract.extract(path)
    videos_sorted = sort_videos_by_request(requests)  # pour chaque endpoint, liste des videos par ordre de requests maximal
    server_sorted_by_latency = sort_endpoints_by_latency(endpoints)  # pour chaque endpoint, liste des servers classes par ordre de latence min
    add_list = [1 for i in range(endpoints)]  # pour chaque endpoint, 1 si on a ajoute une video ce tour ci, 0 sinon
    # condition d'arret : tout vaut 0, on n'a rien ajoute

    output_list=[ [] for i in range(n_servers)]


    while sum (add_list)!=0:
        for i in range(len(endpoints)):
            add_done = False
            while not add_done and server_sorted_by_latence[i] != []:
                serv_min = server_sorted_by_latence[i][0]  # serveur de latence minimale par rapport au endpoint i
                j = 0  # tentatives d'ajout
                while j < 4 and not add_done:  # 4 tentatives max avant de passer au serveur suivant
                    if videos_sorted[i][j] not in output_list[serv_min]:  # video avec le plus de requetes pour l'endpoint i, si elle n'y est pas
                        add_video(output_list,serv_min,videos_sorted[i][j])  # n'ajoute pas si ca depasse la taille du serveur ou si elle y est deja
                        add_done = True
                        delete_video(videos_sorted,i,j)  # on supprime la video de la liste des plus populaires vu qu'elle est accessible
                    else:
                        j += 1  # on tente d'inserer la video du rang d'apres
                if not add_done:
                    delete_server(server_sorted_by_latence, i)  # on supprime le serveur des accessibles
            if not add_done:
                add_list[i]=0
            else:
                add_list[i]=1

    return output_list


def add_video(output, server_id, video_id):
    if video_id not in output[server_id]:
        output[server_id].append(video_id)
    else:
        print("Erreur : doublon video")

def delete_video(sorted_videos,i,j):
    del sorted_videos[i][j]



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


def delete_server(server_sorted_by_latency, i):
    del server_sorted_by_latency[i][0]


if __name__ == "__main__":
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = extract.extract(extract.names[0])
    result = sort_videos_by_request(requests)
    print(result)