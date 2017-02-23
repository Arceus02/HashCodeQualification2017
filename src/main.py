from src import extract
from src import solver_endpoints
from src import export

result = solver_endpoints.solver_endpoints(extract.names[0])
export.export(result)