def describe_vrp_plan():
    """Return the planned Vehicle Routing Problem formulation."""
    return {
        "objective": "Minimize total route distance/time/cost",
        "constraints": [
            "Vehicle capacity",
            "Depot start and return",
            "Delivery time windows",
            "Maximum route duration"
        ],
        "future_tool": "Google OR-Tools"
    }

# A full VRP implementation requires a distance/time matrix and
# operational constraints that are not contained in the Week 1 CSV.
# The function below documents the intended optimization stage.

def build_route_requirements(num_vehicles, vehicle_capacity, depot):
    return {
        "num_vehicles": num_vehicles,
        "vehicle_capacity": vehicle_capacity,
        "depot": depot
    }
