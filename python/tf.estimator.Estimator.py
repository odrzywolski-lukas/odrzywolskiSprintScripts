import numpy as np
import tensorflow as tf

def model_fn(features, labels, mode):
	W = tf.get_variable("W", [1], dtype=tf.float64)
	b = tf.get_variable("b", [1], dtype=tf.float64)
	y= W*features['x']+b
	loss = tf.reduce_sum(tf.square(y-labels))
	global_step = tf.train.get_global_step()