import numpy as np
import sklearn.preprocessing

# Gets an X-matrix given data as 2-element tuples with IDs and vectors.
from get_songs import vectors


def get_x(values):
    return np.vstack([x[1] for x in values])

# Given an object with a .transform(), apply it to the data vectors.
def apply_transform(transformer, data):
    return [(x[0], transformer.transform(x[1].reshape(1, -1))) for x in data]

def train_and_apply(transformer, data):
    X = get_x(data)
    transformer.fit(X)
    return apply_transform(transformer, data)

scaled = train_and_apply(sklearn.preprocessing.StandardScaler(), vectors)