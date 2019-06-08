import tensorflow as tf


class CalculatorController:
    def __init__(self, num1, num2, opcode):
        self._num1 = num1
        self._num2 = num2
        self._opcode = opcode
        # self는 클래스 내부에서 사용하는 값, private의 의미
        # 내부에서 사용하는 값은 일반적으로 네이밍을 할때 _ underscore를 해준다.

    def calc(self):
        n1 = self._num1
        n2 = self._num2
        opcode = self._opcode
        print('컨트롤러에 넘어온 값 n1 = {}, n2 = {}, op = {}'.format(n1,n2,opcode ))
        tf.reset_default_graph()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver = tf.train.import_meta_graph('calculator/saved_add_model/model-1000.meta')
            saver.restore(sess, tf.train.latest_checkpoint('calculator/saved_add_model'))
            graph = tf.get_default_graph()
            w1 = graph.get_tensor_by_name('w1:0')
            w2 = graph.get_tensor_by_name('w2:0')
            print('num1 is {}\n'.format(float(n1)))
            print('num2 is {}'.format(float(n2)))
            feed_dict = {w1: float(n1), w2: float(n2)}
            op_to_restore = graph.get_tensor_by_name("op_add:0")
            result = sess.run(op_to_restore, feed_dict)
            print('최종결과 : {}'.format(result))
        return result
        """
        n1 = self._num1
        n2 = self._num2
        opcode = self._opcode

        print('controller value N1 ={}, N2 ={}, OP = {}'.format(n1, n2, opcode))

        tf.reset_default_graph()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver = tf.train.import_meta_graph('calculator/saved_add_model/model-1000.meta')
            saver.restore(sess, tf.train.latest_checkpoint('calculator/saved_add_model'))

            graph = tf.get_default_graph()
            w1 = graph.get_tensor_by_name('w1:0')
            w2 = graph.get_tensor_by_name('w2:0')
            print('num1 is {}\n'.format(float(n1)))
            print('num2 is {}\n'.format(float(n2)))
            feed_dict = {w1: float(n1), w2: float(n2)}

            op_to_restore = graph.get_tensor_by_name('op_add:0')
            result = sess.run(op_to_restore, feed_dict)
            print('FINAL RESULT : {}'.format(result))
            # with는 내부의 로컬영역을 만든다. 즉, 위의 session은 with 내부에서만 유효
            # saver.restore 으로 checkpoint에 새로운 데이터를 계속 쌓고 있다.
"""