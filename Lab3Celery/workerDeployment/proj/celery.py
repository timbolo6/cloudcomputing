from celery import Celery
import re
app = Celery('proj', broker='amqp://test:test@192.168.2.143:5672/',backend='rpc://', include=['proj.tasks'])

#app.conf.update(result_expires=3600,)
if __name__ == '__main__':
    app.start()
