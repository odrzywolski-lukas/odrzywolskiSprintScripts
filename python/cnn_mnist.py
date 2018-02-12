#cnn file for tf tutorial 
#Lukas Odrzywolski

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function 

#imports
import numpy as np 
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

#application of logic added here
def cnn_model_fn(feature, labels, mode):
	"""Model function for CNN."""
	#input layer
	input_layer = tf.reshape(features["x"], [-1, 28, 28, 1])

	#convloutional laqyer #1
	conv1 = tf.layer.conv2d(
		inputs=input_layer,
		filters=32,
		kernel_size=[5, 5],
		padding="same",
		activation=tf.nn.relu)

	#pooling layer #1
	pool1 = tf.layer.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

	#convolutional layer #2 and pooling layer #2
	conv2 = tf.layer.conv2d(
		inputs=pool1,
		filters=64,
		kernel_size=[5, 5],
		padding="same",
		activation=tf.nn.relu)
	pool2 = tf.layers.ax_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

	#dense layer
	pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
	dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
	dropout = tf.layers.dropout(
		inputs=dense, rate=0.4, training=mode == tf.estimator. ModeKeys.TRAIN)

	#logits layer 
	logits = tf.layers.dense(inputs=dropout, units=10)

	predictions = {
		#generate prediction (for PREDICT and EVAL mode)
		"classes": tf.argmax(input=logits, axis=1),
		#add 'softmax_tensor' to the graph. it is used for PREDICT and by the 'logging_hook'.
		"probabilities": tf.nn.softmax(logits, name="softmax_tensor")
	}

	if mode == tf.estimator.ModeKeys.PREDICT:
		return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

	#calculate loss (for both TRAIN and EVAL modes)
	loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

	#configure the training Op (for TRAIN mode)
	if mode == tf.estimator.ModeKeys.TRAIN:
		optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
		train_op = optimizer.minimize(
			loss=loss,
			global_step=tf.train.get_global_step())
		return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

	#add evaluation metric (for EVAL mode)
	eval_metric_ops = {
		"accuracy": tf.metrics.accuracy(
			labels=labels, predictions=predictions["classes"])}
		return tf.estimator.EstimaorSpec(
			mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)

if __name__ == "__main__":
	tf.app.run()