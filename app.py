from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'academic1'

mysql = MySQL(app);

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *FROM course")
    dataku = cur.fetchall()
    cur.close()
    return render_template('home.html', course = dataku)


@app.route('/simpan',methods=["POST"])
def simpan():
    kode = request.form['xkode']
    nama = request.form['xname']
    sks = request.form['xsks']
    semester = request.form['xsemester']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO course (kode_matkul, course_name, sks, semester) VALUES (%s,%s,%s,%s)",(kode, nama,sks,semester))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/update',methods=["POST"])
def update():
    kode = request.form['xkode']
    nama = request.form['xname']
    sks = request.form['xsks']
    semester = request.form['xsemester']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE course SET course_name = %s, sks=%s, semester=%s WHERE kode_matkul=%s",(nama,sks,semester, kode))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/hapus/<string:kode>',methods=["GET"])
def hapus(kode):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM course WHERE kode_matkul=%s", (kode,))
    mysql.connection.commit()
    return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)