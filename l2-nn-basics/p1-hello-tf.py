import numpy as np
import tensorflow as tf

# First, let's create a "placeholder", which is
# the value we as the user supply to the graph.
# TODO: 

# Here we create two variables: a and b. We can
# give them default values. 
# TODO:

# Now we form the computational graph:
# TODO:

# N.B. We could just as easily write:
# y = a*x + b

# Now we ask TensorFlow for a new session to run
# things on and initialize variables
# TODO:
# sess = tf.InteractiveSession()
# tf.global_variables_initializer().run()

# Here is the input we will feed to the graph.
our_x = 1.0

# Now run the computational graph.
# TODO: y_out = sess.run(y, feed_dict={x: our_x})

# Print the result.
print('y_out = {}'.format(y_out))