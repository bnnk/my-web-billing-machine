import os,time,random,re
import webbrowser as wb
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')
Future_list=['Aston Martin Rapide E','Suzuki Nexa Future S','Tesla Model X','Hyundai Kona EV',''' 09 Corvette ZRI ''',
             'Porsche Boxter','Dacia Swift','Renault Twizy','Rolls Royce Vision Next 100',
               'Cupra Tavascan','Honda E','Infiniti QX Inspiration', 'Mini Cooper SE', 'Wolkswagen ID.3', 'Seat El-Born','Lotus Evija',
              'Suzuki Survior EV','Lexus LC500','Lexus LF-30 EV','Mercedes-Benz Future Bus','Olli Concept Bus',
              'Transit Elevated Bus','Hyperloop train','Neva Aerospace AirQuadOne','Icare Motorcycle Concept',
              'Seat Minimó','Organic Transit ELF','Kyocera’s EOS folding concept','Motorola Piccolo Concept 1 Cell Phone',
               'Eclipse Intuit phone','Kambala Ear-Phone','Nanokia','Motorola Sparrow','Nokia Morph Concept Cellphone',
                'Mooon concept phone','Phlips Fluid Flexible Concept Phone','Glass Phone']
Future_list.sort()
random.seed(100)
Future_list_dict={Future_list[i]: random.randint(1,100) for i in range(len(Future_list))}
print(Future_list_dict)
@app.route('/',methods=['GET','POST','PUT']) 
def homepage_base(): 
    return render_template('redirector.html')
@app.route('/buy',methods=['GET','POST','PUT']) 
def homepage(): 
    return render_template("List.html", len = len(Future_list), Vehicles_list = Future_list,lst=list(Future_list_dict.values()))
@app.route('/buy-post',methods=['POST']) 
def homepage_post():
    y=re.split("\[", request.form['choosen'])
    y="".join(y)
    y=re.split("\]", y)
    y=y[:len(y)-1]
    cost=0
    for i in range(0,len(y)):
        cost = cost + Future_list_dict[y[i]]
    print('Points = %d' % cost)
    Text = "Received Order ["+request.form['choosen']+"] Cost is ["+str(cost)+"]"
    return render_template('task.html', txt = Text)
@app.route('/rev-project',methods=['GET','POST','PUT'])
def project():
    time.sleep(0.19)
    os.system('''"C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe" --profile-directory=Default --app-id=icnbpeblemailjmcmfkccklodhagdbpg''')
    return 'Starting app...'
@app.errorhandler(404)
def not_found(e): 
    return '<a href = http://127.0.0.1:5000/buy>You will be redirected.Click Me</a>'
wb.open_new_tab('127.0.0.1:5000')
app.run(host= None)   
