from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
	if request.args.get('name'):
		template = '''
		{}
		'''.format(request.args.get('name'))
		return render_template_string(template)	
	else:
		return "No dice use ?name="

if __name__ == '__main__':
	app.run(debug=True)