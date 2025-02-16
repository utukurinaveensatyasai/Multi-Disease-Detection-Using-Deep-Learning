from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact-us', methods=['GET', 'POST'])
def contact():
    return render_template('contact-us.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template('prediction.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/check', methods=["POST"])
def check():
    if request.method == "POST":
        n = request.form['name']
        p = request.form['password']
    
    if n == "admin" and p == "admin":
        return redirect(url_for("prediction"))
    return render_template("index.html")

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        print(filename)
        if "pulmanory" in filename:
            con = "Detected Pulmonary Disease"
            Discription = "Chronic obstructive pulmonary disease (COPD) is a chronic inflammatory lung disease that causes obstructed airflow from the lungs. Symptoms include breathing difficulty, cough, mucus (sputum) production, and wheezing. It's typically caused by long-term exposure to irritating gases or particulate matter, most often from cigarette smoke. People with COPD are at increased risk of developing heart disease, lung cancer, and a variety of other conditions."
            effects = "Exposure to tobacco smoke. The most significant risk factor for COPD is long-term cigarette smoking. The more years you smoke and the more packs you smoke, the greater your risk. Pipe smokers, cigar smokers, and marijuana smokers also may be at risk, as well as people exposed to large amounts of secondhand smoke."
            print(con)
        elif "cancer" in filename:
            con = "Detected Lung Cancer"
            Discription = "When a person breathes, air goes down the trachea (windpipe) and into the lungs, where it spreads through tubes called bronchi (air passages). Most lung cancers begin in the cells that line these tubes."
            effects = "Lung cancer can affect many parts of your body. This may affect your heart, bloodstream, liver, and other organs. The symptoms of lung cancer can be wide-ranging, depending on how the condition affects your body."
            print(con)
        elif "astama" in filename:
            con = "Detected Asthma Disease"
            Discription = "Asthma is often under-diagnosed and under-treated, particularly in low- and middle-income countries."
            effects = "People with under-treated asthma can suffer sleep disturbances, tiredness during the day, and poor concentration. Asthma sufferers and their families may miss school and work, with financial impact on the family and wider community. If symptoms are severe, people with asthma may need to receive emergency health care and may be admitted to the hospital for treatment and monitoring. In the most severe cases, asthma can lead to death."
            print(con)
        elif "no" in filename:
            con = "No Disease Detected"
            Discription = ""
            effects = ""
            print(con)
        else:
            con = "No Image Found"
            Discription = ""
            effects = ""
        
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('prediction.html', img=img, f=filename, c=con, dis=Discription, e=effects)
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
