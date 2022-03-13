from flask import Flask
from celery import Celery
from flask import jsonify,request
from flask_pymongo import PyMongo
from linkedBot import linkedBot
from flask_cors import CORS




app = Flask(__name__)
CORS(app)
app.secret_key="hello"
app.config['MONGO_URI']="mongodb://127.0.0.1:27017/prestalink"
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
mongo = PyMongo(app)



@celery.task()
def linkedsearch(search):
    link = linkedBot(96471601, "Tunis5555", mongo)
    # link.browser.quit()
    # passaron.papasarouni@gmail.com/firas.1997/firasghost@gmail.com
    link.login_linkedin()
    nmbrJaime = link.google_search(search)
    return nmbrJaime


@app.route("/")
def lists():
    i=0
    return jsonify([i for i in mongo.db.profiles.find({},{'_id': False})])
@app.route("/get_profile/<int:id>")
def insert_one(id):
    profile = mongo.db.profiles.find_one({"id": id},{'_id': False})
    return profile



@app.route('/run',methods=['POST'])
def scrapping_run():
    if request.method=="POST":
        print(str(request.json))
        #search=request.form['search']
        search=request.json['search']
        print(search)
        numberJaime=str(linkedsearch(search))
        obj={'search':numberJaime}
        print(numberJaime)
        return obj





if __name__ == '__main__':
    app.run(debug=False )