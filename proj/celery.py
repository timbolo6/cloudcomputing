from celery import Celery

app = Celery('proj', broker='pyamqp://guest@localhost//',backend='rpc://', include=['proj.tasks'])

#app.conf.update(result_expires=3600,)


if __name__ == '__main__':
    app.start()
