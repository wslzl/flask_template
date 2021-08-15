from flask_apscheduler.scheduler import APScheduler


def init_app(app):
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()