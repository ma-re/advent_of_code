# Get data
def get_data(path: str) -> list:
    data = [x.strip() for x in open(path)]
    return data