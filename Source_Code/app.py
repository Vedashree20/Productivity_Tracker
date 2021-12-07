from flask import Flask,request,render_template,redirect
from matplotlib import axes
import psycopg2
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#---------Connection Page--------------------

conn = psycopg2.connect(database="main_database", user='postgres', password='8May1997$',host='127.0.0.1', port= '5432')
cursor=conn.cursor()

#---------Home Page--------------------

app = Flask(__name__)
@app.route("/")
def home():
     return render_template('Home.html')

#---------Day1 Page--------------------
@app.route("/Day1/",methods = ['GET', 'POST'])
def input1():
     if request.method == "POST":
           work = request.form.get("Work")
           exercise = request.form.get("Exercise") 
           screentime = request.form.get("Screentime")
           hobbies = request.form.get("Hobbies")
           social = request.form.get("Social")
           sleep = request.form.get("Sleep")
           #insert values into database 
           cursor.execute('UPDATE Time VALUES set Work_=%s,Exercise_=%s,Screentime_=%s,Hobbies_=%s,Social_=%s,Sleep_=%s WHERE Dayn=1',(work,exercise,screentime,hobbies,social,sleep))
           conn.commit()
           return render_template('Day2.html')
          
     return render_template('Day1.html')

#---------Day2 Page--------------------
@app.route("/Day2/",methods = ['GET', 'POST'])
def input2():
     if request.method == "POST":
           work = request.form.get("Work")
           exercise = request.form.get("Exercise") 
           screentime = request.form.get("Screentime")
           hobbies = request.form.get("Hobbies")
           social = request.form.get("Social")
           sleep = request.form.get("Sleep")
           cursor.execute('UPDATE Time VALUES set Work_=%s,Exercise_=%s,Screentime_=%s,Hobbies_=%s,Social_=%s,Sleep_=%s WHERE Dayn=2',(work,exercise,screentime,hobbies,social,sleep))
           conn.commit()
           return render_template('Day3.html')

     return render_template('Day2.html')

#---------Day3 Page--------------------
@app.route("/Day3/",methods = ['GET', 'POST'])
def input3():
     if request.method == "POST":
           work = request.form.get("Work")
           exercise = request.form.get("Exercise") 
           screentime = request.form.get("Screentime")
           hobbies = request.form.get("Hobbies")
           social = request.form.get("Social")
           sleep = request.form.get("Sleep")
           cursor.execute('UPDATE Time VALUES set Work_=%s,Exercise_=%s,Screentime_=%s,Hobbies_=%s,Social_=%s,Sleep_=%s WHERE Dayn=3',(work,exercise,screentime,hobbies,social,sleep))
           conn.commit()
           return render_template('Day4.html')
        
     return render_template('Day3.html')

#---------Day4 Page--------------------    
@app.route("/Day4/",methods = ['GET', 'POST'])
def input4():
     if request.method == "POST":
           work = request.form.get("Work")
           exercise = request.form.get("Exercise") 
           screentime = request.form.get("Screentime")
           hobbies = request.form.get("Hobbies")
           social = request.form.get("Social")
           sleep = request.form.get("Sleep")
           cursor.execute('UPDATE Time VALUES set Work_=%s,Exercise_=%s,Screentime_=%s,Hobbies_=%s,Social_=%s,Sleep_=%s WHERE Dayn=4',(work,exercise,screentime,hobbies,social,sleep))
           conn.commit()
           return render_template('Day5.html')
         
     return render_template('Day4.html')

     
#---------Day5 Page--------------------
@app.route("/Day5/",methods = ['GET', 'POST'])
def input5():
     if request.method == "POST":
           work = request.form.get("Work")
           exercise = request.form.get("Exercise") 
           screentime = request.form.get("Screentime")
           hobbies = request.form.get("Hobbies")
           social = request.form.get("Social")
           sleep = request.form.get("Sleep")
           cursor.execute('UPDATE Time VALUES set Work_=%s,Exercise_=%s,Screentime_=%s,Hobbies_=%s,Social_=%s,Sleep_=%s WHERE Dayn=5',(work,exercise,screentime,hobbies,social,sleep))
           conn.commit()
           return render_template('Day6.html')
        
     return render_template('Day5.html')

#---------Day6 Page--------------------
@app.route("/Day6/",methods = ['GET', 'POST'])
def input6():
     if request.method == "POST":
           work = request.form.get("Work")
           exercise = request.form.get("Exercise") 
           screentime = request.form.get("Screentime")
           hobbies = request.form.get("Hobbies")
           social = request.form.get("Social")
           sleep = request.form.get("Sleep")
           cursor.execute('UPDATE Time VALUES set Work_=%s,Exercise_=%s,Screentime_=%s,Hobbies_=%s,Social_=%s,Sleep_=%s WHERE Dayn=6',(work,exercise,screentime,hobbies,social,sleep))
           conn.commit()
           return render_template('Day7.html')
       
     return render_template('Day6.html')

#---------Progress Page--------------------
@app.route("/Progress/",methods = ['GET', 'POST'])
def prog():
     query='SELECT *FROM Time'
     cursor.execute(query)
     tuples=cursor.fetchall()
     df = pd.DataFrame(tuples, columns=['Dayn','Work_','Exercise_','Screentime_','Hobbies_','Social_','Sleep_'])
     df.fillna(df.mean())
     #df.describe()
     d1=df['Work_'].mean()
     d2=df['Exercise_'].mean()
     d3=df['Screentime_'].mean()
     d4=df['Hobbies_'].mean()
     d5=df['Social_'].mean()
     d6=df['Sleep_'].mean()
     my_data = [d1,d2,d3,d4,d5,d6]
     #my_colors = ['lightblue','lightsteelblue','silver']
     my_labels = 'work','exercise','screen time','hobbies','socialising','sleep'
     plt.pie(my_data,labels=my_labels,autopct='%1.1f%%',)
     plt.title('Weekly Average Chart')
     plt.axis('equal')
     plt.savefig('Flask/static/images/Chart1.png')
     df.plot(x='Dayn', kind='bar', stacked=True,title='Activity Graph over the Week')
     plt.xticks(rotation = 360)
     plt.savefig('Flask/static/images/Chart2.png')
     return render_template('Progress.html')

#---------Day7 Page--------------------
@app.route("/Day7/",methods = ['GET', 'POST'])
def input7():
     if request.method == "POST":
           work = request.form.get("Work")
           exercise = request.form.get("Exercise") 
           screentime = request.form.get("Screentime")
           hobbies = request.form.get("Hobbies")
           social = request.form.get("Social")
           sleep = request.form.get("Sleep")
           cursor.execute('UPDATE Time VALUES set Work_=%s,Exercise_=%s,Screentime_=%s,Hobbies_=%s,Social_=%s,Sleep_=%s WHERE Dayn=7',(work,exercise,screentime,hobbies,social,sleep))
           conn.commit()
           return redirect("/Progress/")
         
     return render_template('Day7.html')

#---------Running Page--------------------
if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5000) 