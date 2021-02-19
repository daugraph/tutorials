import json
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

with open('clusterspec.json', 'r') as f:
    clusterspec = json.load(f)

cluster = tf.train.ClusterSpec(clusterspec)

a = tf.constant(3)
b = tf.constant(2)

with tf.device("/job:worker/task:0"):
    x = tf.multiply(a, b)

with tf.device("/job:worker/task:1"):
    y = tf.multiply(a, b)

# 给session显式指定target
with tf.Session("grpc://10.67.8.141:20001", config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(sess.run([x, y]))
