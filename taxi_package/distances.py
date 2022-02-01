import numpy as np

def manhattan(lon1, lat1, lon2, lat2):

    distance = np.abs(lon1 - lon2) + np.abs(lat1 - lat2)

    return distance


def euclidean(lon1, lat1, lon2, lat2):

    distance = ((lon1 - lon2)**2 + (lat1 - lat2)**2)**0.5

    return distance
