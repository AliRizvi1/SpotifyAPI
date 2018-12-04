import sklearn.cluster

from get_songs import USERNAME, grouper, sp
from scale import scaled, get_x

RUN_ON = scaled

# Select the 'elbow' and classify the tracks
NUM_CLUSTERS = 8
PLAYLIST_NAME_FMT = 'Version {}: Cluster {}'
VERSION = 6

model = sklearn.cluster.KMeans(n_clusters=NUM_CLUSTERS,
                               n_jobs=-1)
model.fit(get_x(RUN_ON))
classified = [(x[0], model.predict(x[1])[0]) for x in RUN_ON]

# Now convert the classified songs into some playlists.
ids = []
for cluster in range(NUM_CLUSTERS):
    playlist_id = sp.user_playlist_create(USERNAME,
                                          PLAYLIST_NAME_FMT.format(VERSION, cluster))['id']
    ids.append(playlist_id)

def get_all_classified_as(classified, item_class):
    return [x[0] for x in classified if x[1] == item_class]

for cluster in range(NUM_CLUSTERS):
    tracks = get_all_classified_as(classified, cluster)
    playlist = ids[cluster]
    for group in grouper(100, tracks):
        sp.user_playlist_add_tracks(USERNAME, playlist, group)