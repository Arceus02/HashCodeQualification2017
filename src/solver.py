import math


def solver(n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests):
    score=[]
    sortie=[]
    for icache in range(nombre_cache):
        sortie_i=[]
        score=[0 for k in range(n_videos)]
        cache=liste_cache[icache]
        liste_endpoint=fonction1(cache)
        place_restante=server_space

        sortie_i += [icache]



        for endpoint in liste_endpoint:
            iendpoint=liste_endpoint[0]
            ping_end=liste_endpoint[1]
            liste_video=fonction2(endpoint[0])
            for ivideo in range(len(liste_video)):
                j=liste_video[ivideo][0]
                score[j]+=(liste_video[ivideo][1])*(ping_main[iendpoint]-ping_end)/(video_sizes[j])



        for k in range(n_videos):
            score[k]=[k,score[k]]
        score=sorted(score, key=lambda score: score[1])

        for k in range(n_videos):
            if (place_restante >= video_sizes[score[k][0]]):
                sortie_i+=[score[k][0]]
                place_restante-=video_sizes[score[k][0]]
            if (score[k][1]==0):
                break
        sortie+=[sortie_i]
    return(sortie)
