import tensorflow as tf
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a= tf.constant([2])
b=tf.constant([3])
c = tf.add(a,b)
#step 4
session =tf.Session()
#step 5
result = session.run(c)
print(result)
#step 6
session.close()

#step 5 can be write as below
#with tf.Session() as session:
#result = session.run(c)
#print (result)