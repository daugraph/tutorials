import json
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant(3)
b = tf.constant(2)

with tf.device("/job:worker/task:0"):
    x = tf.multiply(a, b)

with tf.device("/job:worker/task:1"):
    y = tf.multiply(a, b)

# 给session显式指定target
with tf.Session("grpc://localhost:20001", config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(sess.run([x, y]))
