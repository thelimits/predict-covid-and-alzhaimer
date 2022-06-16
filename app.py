import joblib
import cv2
from flask import Flask, render_template, request

app = Flask(__name__)

# home index ---> covid
@app.route('/', methods=["GET"])
def Home_index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def predicted_covid():
    if request.method == "POST":
        name = request.form["nameawal"]
        if name == "Covid":
            judul = "Covid-19"
            user = request.form["FirstName"]
            user1 = request.form["LN"]
            email = request.form["email"]
            Gender = request.form["gender"]
            
            if request.files:
                images = request.files["imagefile"]
                path = "static/Upload/Covid" + "/" + images.filename
                images.save(path)
                
                images_read = cv2.imread(path, 0)
                images1 = cv2.resize(images_read, (200,200))
                images1 = images1.reshape(1, -1)
                
                with open('Model_Learning_Covid', 'rb') as file:
                    mdl = joblib.load(file)
                
                predicteds = mdl.predict(images1)
                if predicteds == 1:
                    predicteds = "Covid"
                else:
                    predicteds = "Normal"
                
                images.close()
            return render_template('Predict.html', 
                                temp = user + " " +user1,
                                email = email, 
                                predicteds = predicteds,
                                path = path,
                                Gender = Gender,
                                judul = judul
                                )
        else:
            judul = "Alzhaimer"
            user = request.form["FirstName"]
            user1 = request.form["LN"]
            email = request.form["email"]
            Gender = request.form["gender"]

            if request.files:
                images = request.files["imagefile"]
                path = "static/Upload/Alzhaimer" + "/" + images.filename
                images.save(path)

                images_read = cv2.imread(path, 0)
                images1 = cv2.resize(images_read, (128, 128))
                images1 = images1.reshape(1, -1)

                with open('Model_Learning_Alzhaimer', 'rb') as file:
                    mdl = joblib.load(file)
                
                predicteds = mdl.predict(images1)
                if predicteds == 0:
                    predicteds = "MildDemented"
                elif predicteds == 1:
                    predicteds = "ModerateDemented"
                elif predicteds == 2:
                    predicteds = "NonDemented"
                else:
                    predicteds = "VeryMildDemented"
                
                images.close()
                return render_template('Predict.html', 
                                temp = user + " " +user1,
                                email = email, 
                                predicteds = predicteds,
                                path = path,
                                Gender = Gender,
                                judul = judul
                                )
    else:    
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)