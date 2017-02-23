from src import extract


def solver_endpoints(path):
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = extract.extract(path)
    condition_arret = False
    videos_sorted = sort_videos_by_request(requests)  # pour chaque endpoint, liste des videos par ordre de requests maximal

    while not condition_arret:
        for i in range len(endpoints):
            serv_min = serv_latence_min(i)  # serveur de latence minimale par rapport au endpoint i
            if serv_min != -1: #serv_min =-1 s'il n'y a pas de serveur connecte a ce endpoint
                add_done = false
                j = 0  # tentatives d'ajout
                while j < 10 and not add_done:
                    if videos_sorted[i][j] not in serv_min_vids:  # video avec le plus de requetes pour l'endpoint i
                        ajouter_vid(serv_min)  # n'ajoute pas si ca depasse la taille du serveur
                        add_done = True
                    delete_vid[i][j]  # on supprime la video de la liste des plus populaires vu qu'elle est accessible
                    else:
                        j += 1  # on tente d'inserer la video du rang d'apres
