# NEA PROJECT
-----------

for Computer Science A-Level

AI chatbot, tine-tuned to computer science curriculum. With possible knowledge based embedding from file uploads.


## Deployment
Once required packages installed:
Create new [API key](https://platform.openai.com/api-keys) and update env `OPENAI_KEY`.

**Locally** run `python app.py` and open webpage at `127.0.0.1:5000`. Vary port in top level code of [app.py](docs/app.py).
**Deployed** run WSGI to serve python and Nginx to serve static assests.

### TODO:
file handling: 
...
