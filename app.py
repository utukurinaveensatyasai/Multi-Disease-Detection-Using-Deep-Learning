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
@app.route('/p1', methods=['GET', 'POST'])
def p1():
    return render_template('p1.html')
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

        # Extract disease level and stage from the filename
        disease_level = "Unknown"
        disease_stage = "Unknown"
        
        # Check for disease stage based on the filename
        if "mild" in filename.lower():
            disease_level = "Mild"
            disease_stage = "Early Stage"
        elif "medium" in filename.lower():
            disease_level = "Medium"
            disease_stage = "Intermediate Stage"
        elif "severe" in filename.lower():
            disease_level = "Severe"
            disease_stage = "Advanced Stage"

        # Check for disease type based on the filename
        if "pulmanory" in filename:
            con = "Detected Pulmonary Disease"
            Discription = "Chronic obstructive pulmonary disease (COPD) is a chronic inflammatory lung disease that causes obstructed airflow from the lungs. Symptoms include breathing difficulty, cough, mucus (sputum) production, and wheezing. It's typically caused by long-term exposure to irritating gases or particulate matter, most often from cigarette smoke. People with COPD are at increased risk of developing heart disease, lung cancer, and a variety of other conditions."
            effects = "Exposure to tobacco smoke. The most significant risk factor for COPD is long-term cigarette smoking. The more years you smoke and the more packs you smoke, the greater your risk. Pipe smokers, cigar smokers, and marijuana smokers also may be at risk, as well as people exposed to large amounts of secondhand smoke."
            remedies= "Practice deep-breathing exercises regularly and stay active to enhance lung capacity. Avoid smoking and exposure to pollutants to prevent further complications."
        elif "cancer" in filename or "canser" in filename:
            con = "Detected Lung Cancer"
            Discription = "When a person breathes, air goes down the trachea (windpipe) and into the lungs, where it spreads through tubes called bronchi (air passages). Most lung cancers begin in the cells that line these tubes."
            effects = "Lung cancer can affect many parts of your body. This may affect your heart, bloodstream, liver, and other organs. The symptoms of lung cancer can be wide-ranging, depending on how the condition affects your body."
            remedies="Consult an oncologist for a treatment plan including surgery, chemotherapy, or radiation therapy. Maintain a healthy diet and seek emotional support to manage the condition."
        elif "asthma" in filename or "astama" in filename:
            con = "Detected Asthma Disease"
            Discription = "Asthma is often under-diagnosed and under-treated, particularly in low- and middle-income countries."
            effects = "People with under-treated asthma can suffer sleep disturbances, tiredness during the day, and poor concentration. Asthma sufferers and their families may miss school and work, with financial impact on the family and wider community. If symptoms are severe, people with asthma may need to receive emergency health care and may be admitted to the hospital for treatment and monitoring. In the most severe cases, asthma can lead to death."
            remedies="Use prescribed inhalers and medications to control symptoms and prevent attacks. Avoid allergens, dust, and cold air to reduce triggers."
        elif "congential" in filename:
            con="Congential-abnormal Disease"
            Discription="Congenital eye abnormalities are physical abnormalities that affect the structure or function of the eye and are present at birth. They can be caused by a number of factors, including: Gene mutations, Exposure to drugs or alcohol during pregnancy, and Problems during the eye's development in the embryo."
            effects="can lead to a range of effects including impaired vision, abnormal eye appearance, light sensitivity, difficulty focusing, and in severe cases, complete blindness"
            remedies="Regular medical evaluations and therapeutic interventions can improve quality of life. Genetic counseling and early rehabilitation programs are beneficial."
        elif "cataracts" in filename:
            con="Contract a disease"
            Discription="Contract a disease means to catch an illness that can affect people, animals, or plants. Some examples of diseases that can be contracted include: Bacterial infections, Viruses, Fevers, Illnesses, and Infections."
            effects="The effects of a contract disease depend on the specific disease, but some common symptoms include: Fever, Diarrhea, Fatigue, Muscle aches, and Coughing."
            remedies="Protect your eyes from UV rays by wearing sunglasses and eating foods rich in antioxidants. Consult an ophthalmologist for surgical intervention when vision is significantly impaired."
        elif "fundus" in filename:
            con="Fundus Disease"
            Discription="Fundus diseases mainly include lesions of the retina, optic nerve, vitreum, etc., and can lead to irreversible visual impairment without timely diagnosis and appropriate treatment."
            effects="These diseases can cause irreversible vision impairment, visual field defect, and even blindness, having severe influence on the living quality of patients."
            remedies="Manage systemic conditions like diabetes or hypertension to prevent retinal damage. Regular eye exams can help in early detection and treatment."
        elif "tumors" in filename:
            con="Tumor Disease"
            Discription="A tumor,also known as a neoplasm, is an abnormal growth of tissue that can be cancerous or noncancerous. Tumor can develop when cells divide and grow more than they should, or when they don't die when they should."
            effects="Spinal tumors or growths of any kind can lead to pain, neurological problems and sometimes paralysis. A spinal tumor can be life-threatening and cause permanent disability."
            remedies=" Follow the recommended treatment protocol, including surgery, chemotherapy, or radiation. Stay informed about your condition and explore support groups for coping strategies."
        elif "inflammation" in filename:
            con="Ankylosing spondylitis (AS)"
            Discription=" Chronic back pain, stiffness, and impaired spinal mobility. Other symptoms include buttock and hip pain, peripheral arthritis, and enthesitis. "
            effects="This disease causes inflammation in the spine's joints and tissues, which can lead to stiffness and eventually fused vertebrae. This can make the spine less flexible and cause a hunched posture. Other symptoms include eye disease, skin disease, or gut disease."
            remedies="Use cold or warm compresses and take prescribed anti-inflammatory medications. Maintain a healthy diet and reduce stress to minimize chronic inflammation."
        elif "hematomas" in filename:
            con="Hematomas Disease"
            Discription="A hematoma is a collection of blood that pools outside of a blood vessel in an organ, tissue, or body space. Hematomas are usually caused by an injury or surgery that damages a blood vessel, and can occur anywhere in the body. "
            effects="Symptoms of a spinal subdural or epidural hematoma begin with local or radicular back pain and percussion tenderness; they are often severe. Spinal cord compression may develop; compression of lumbar spinal roots may cause cauda equina syndrome and lower-extremity paresis. Deficits progress over minutes to hours."
            remedies=" Rest, apply ice packs, and elevate the affected area to reduce swelling. If severe, consult a doctor for potential drainage or further treatment."
        elif "Alzheimers" in filename:
            con="Alzheimer's disease"
            Discription="Alzheimer's disease is a brain disorder that causes a gradual decline in memory and thinking skills, and eventually the ability to perform simple tasks. It's the most common cause of dementia in older adults."
            effects="Alzheimer's disease is a brain disorder that slowly destroys memory and thinking skills. It affects the brain by damaging neurons, disrupting processes that are vital to neurons, and causing them to stop working normally."
            remedies="Engage in cognitive exercises, maintain a heart-healthy diet, and stay socially active. Medications can slow progression; consult a specialist for personalized care."
        elif "encephalitis" in filename:
            con="Encephalitis"
            Discription="Encephalitis is an inflammation of the brain. It is caused either by an infection invading the brain (infectious encephalitis) or through the immune system attacking the brain in error (post-infectious or autoimmune encephalitis)."
            effects="As encephalitis worsens, it can cause more serious symptoms, including: Severe headache ,Stiff neck ,Seizures, vomting."
            remedies="Seek immediate medical care for antiviral or antibacterial treatments if needed. Rest and stay hydrated while monitoring symptoms closely under a doctor's supervision."
        


        elif "no" in filename or "normal" in filename:
            con = "No Disease Detected"
            Discription = ""
            effects = ""
        else:
            con = "No Image Found"
            Discription = ""
            effects = ""

        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)

        return render_template('prediction.html', img=img, f=filename, c=con, dis=Discription, e=effects, level=disease_level, stage=disease_stage,r=remedies)

    return render_template('prediction.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from environment variable
    app.run(host="0.0.0.0", port=port, debug=True)
