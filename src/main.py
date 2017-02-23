from src import extract
from src import solver_endpoints
from src import export

for name in extract.names:
    n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests = extract.extract(name)
    full_servers = [False for k in range(n_servers)]
    result = None
    for k in range(10):
        result, full_servers = solver_endpoints.solver_endpoints(n_videos, n_endpoints, n_requests, n_servers, server_space, video_sizes, endpoints, requests, full_servers)
    export.export(name, result)
    print("Done", name)