import json
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

with open('clusterspec.json', 'r') as f:
    clusterspec = json.load(f)

cluster = tf.train.ClusterSpec(clusterspec)
server = tf.train.Server(cluster, job_name="master", task_index=0)
server.join()
