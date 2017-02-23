from src import extract
import math


def solver_endpoints(path):
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = extract.extract(path)
    videos_sorted = sort_videos(requests, video_sizes)  # pour chaque endpoint, liste des videos par ordre de requests maximal
    server_sorted_by_latency = sort_endpoints_by_latency(endpoints)  # pour chaque endpoint, liste des servers classes par ordre de latence min
    add_list = [1 for i in range(n_endpoints)]  # pour chaque endpoint, 1 si on a ajoute une video ce tour ci, 0 sinon
    # condition d'arret : tout vaut 0, on n'a rien ajoute
    output_list=[ [] for i in range(n_servers)]

    while sum (add_list)!=0:
        for i in range(len(endpoints)):
            add_done = False
            while not add_done and server_sorted_by_latency[i] != []:
                serv_min = server_sorted_by_latency[i][0]  # serveur de latence minimale par rapport au endpoint i
                j = 0  # tentatives d'ajout
                while j < 1 and not add_done:  # 4 tentatives max avant de passer au serveur suivant
                    if j < len(videos_sorted[i]) and videos_sorted[i][j] not in output_list[serv_min]:  # video avec le plus de requetes pour l'endpoint i, si elle n'y est pas
                        add_video(output_list,serv_min,videos_sorted[i][j], video_sizes, server_space)  # n'ajoute pas si ca depasse la taille du serveur ou si elle y est deja
                        add_done = True
                        delete_video(videos_sorted,i,j)  # on supprime la video de la liste des plus populaires vu qu'elle est accessible
                    else:
                        j += 1  # on tente d'inserer la video du rang d'apres
                if not add_done:
                    delete_server(server_sorted_by_latency, i)  # on supprime le serveur des accessibles
            if not add_done:
                add_list[i]=0
            else:
                add_list[i]=1



    return output_list


def add_video(output, server_id, video_id, video_sizes, server_space):
    server_storage_usage = sum([video_sizes[i] for i in output[server_id]])
    if video_id not in output[server_id] and server_storage_usage+video_sizes[video_id] < server_space:
        output[server_id].append(video_id)

def delete_video(sorted_videos,i,j):
    del sorted_videos[i][j]



def sort_videos(requests, video_sizes):
    result = []
    requests_t = list(map(list, zip(*requests)))
    for i_endpoint, requests_by_endpoint in enumerate(requests_t):
        requests_in_endpoint = [[i_video, amount*1000/video_sizes[i_video]] for i_video, amount in enumerate(requests_t[i_endpoint]) if amount > 0]
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