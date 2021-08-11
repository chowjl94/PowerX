from app import application, db
from app.models import User, Question, Challenge, TimeRecord

@application.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Question': Question,
			'Challenge': Challenge,
			'TimeRecord': TimeRecord}

if __name__ == "__main__":
	application.run(host="127.0.0.1", port=5000, debug=True)
