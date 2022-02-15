import logging

logger_foo=logging.getLogger('foo')
logger_foo_bar=logging.getLogger('foo.bar')
#logger_foo.propagate=False
logger_foo_bar.propagate=False
logger_foo.setLevel(2)
logger_foo_bar.setLevel(2)

c_handler=logging.StreamHandler()
f_handler_foo=logging.FileHandler('foo.log')
f_handler_foo_bar=logging.FileHandler('foo.bar.log')

c_handler.setLevel(logging.NOTSET)
f_handler_foo.setLevel(logging.DEBUG)
f_handler_foo_bar.setLevel(logging.INFO)

c_format=logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler_foo.setFormatter(f_format)
f_handler_foo_bar.setFormatter(f_format)

logger_foo.addHandler(c_handler)
logger_foo_bar.addHandler(c_handler)
logger_foo.addHandler(f_handler_foo)
logger_foo_bar.addHandler(f_handler_foo_bar)

logger_foo.warning('WARNING')
logger_foo.warning('WARNING')
logger_foo.info('INFO')
logger_foo.error('ERROR')
logger_foo.debug('DEBUG')
logger_foo.info('INFO')
logger_foo.log(5,'A log message')

logger_foo_bar.warning('WARNING')
logger_foo_bar.log(7,'A log message')
logger_foo_bar.error('ERROR')
logger_foo_bar.info('INFO')
logger_foo_bar.debug('DEBUG')
logger_foo_bar.log(2,'A log message')
logger_foo_bar.warning('WARNING')
