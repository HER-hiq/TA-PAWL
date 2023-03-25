from flask import Flask, render_template, request, redirect, url_for
from models import Activity, ActivityForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '@123456&*()'

@app.route('/')
def index():
    model = Activity()
    container = []
    container = model.selectDB()
    return render_template('index.html', container=container)

@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    form = ActivityForm()
    if request.method == 'POST':
        jenis_kegiatan = request.form[jenis_kegiatan]
        keterangan = request.form[keterangan]
        tanggal = request.form[tanggal]
        waktu = request.form[waktu]
        data = (jenis_kegiatan, keterangan, tanggal, waktu)
        model = Activity()
        model.insertDB(data)
        return redirect(url_for('index'))
    else:
        return render_template('form.html', form=form)

if __name__ == '__main__' :
    app.run(debug=True)