import tensorflow as tf


class CalculatorModel:
    # 클래스 이름 첫글자는 대문자
    def __init__(self):
        pass

    def create_add_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict = {'w1' : 8.0, 'w2': 2.0}
        r = tf.add(w1, w2, name='op_add')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1 : feed_dict['w1'], w2 : feed_dict['w2']})
        print('TF 덧셈결과 {}'.format(result))
        saver.save(sess, './saved_add_model/model', global_step=1000)

        """"
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        # placeholder는 외부에서 받는 변수
        feed_dict = {'w1': 8.0, 'w2': 2.0}

        r = tf.add(w1, w2, name='op_add')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        # tf.initialize_all_variables() 라는 op을 이용해서
        # 위에 정의된 모든 변수들을 초기화하며 이를 수행하지 않고 실행을 하면 에러가 발생
        # Variable 시리즈는 텐서플로가 연산을 위해 사용하는 변수

        sess.run(tf.global_variables_initializer())
        # 초기화된 변수들은 session에서 한번 실행을 해주어야 실제로 사용이 가능

        saver = tf.train.Saver()
        # 훈련된 결과를 저장한다.
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('Add Result of Tensorflow : {}'.format(result))

        saver.save(sess, './saved_add_model/model', global_step=1000)
        # 1000번 훈련시킨 모델을 저장함
        # 매번 훈련시켜서 쓰면 오래걸리기 때문"""
"""
    def create_sub_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        # placeholder는 외부에서 받는 변수
        feed_dict = {'w1': 8.0, 'w2': 2.0}

        r = tf.subtract(w1, w2, name='op_sub')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('Substract Result of Tensorflow : {}'.format(result))
        saver.save(sess, './saved_sub_model/model', global_step=1000)

    def create_mul_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        # placeholder는 외부에서 받는 변수
        feed_dict = {'w1': 8.0, 'w2': 2.0}

        r = tf.multiply(w1, w2, name='op_mul')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('Multifly Result of Tensorflow : {}'.format(result))
        saver.save(sess, './saved_mul_model/model', global_step=1000)

    def create_div_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        # placeholder는 외부에서 받는 변수
        feed_dict = {'w1': 8.0, 'w2': 2.0}

        r = tf.divide(w1, w2, name='op_div')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('Divide Result of Tensorflow : {}'.format(result))
        saver.save(sess, './saved_div_model/model', global_step=1000)
    """