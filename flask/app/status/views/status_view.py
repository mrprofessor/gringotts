from flask_classful import FlaskView


class StatusView(FlaskView):
    def index(self):
        return "Status: OK"
