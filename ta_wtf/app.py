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
        jenis_kegiatan = form.jenis_kegiatan.data
        keterangan = form.keterangan.data
        tanggal = form.tanggal.data
        waktu = form.waktu.data
        data = (jenis_kegiatan, keterangan, tanggal, waktu)
        model = Activity()
        model.insertDB(data)
        return redirect(url_for('index'))
    else:
        return render_template('insert_form.html', form=form)
    
@app.route('/insert_tugas', methods = ['GET', 'POST'])
def insert_tugas():
    form = ActivityForm()
    if request.method == 'POST':
        aktivitas = request.form['aktivitas']
        tanggal = request.form['tanggal']
        waktu = request.form['waktu']
        status = request.form['status']
        data = (aktivitas, tanggal, waktu, status)
        model = Activity()
        model.insertTugas(data)
        return redirect(url_for('tugas'))
    else:
        return render_template('tugas.html', form=form)
    
@app.route('/insert_rencana', methods = ['GET', 'POST'])
def insert_rencana():
    form = ActivityForm()
    if request.method == 'POST':
        aktivitas = request.form['aktivitas']
        tanggal = request.form['tanggal']
        waktu = request.form['waktu']
        prioritas = request.form['prioritas']
        data = (aktivitas, tanggal, waktu, prioritas)
        model = Activity()
        model.insertRencana(data)
        return redirect(url_for('rencana'))
    else:
        return render_template('rencana.html', form=form)
    
@app.route('/update/<no>')
def update(no):
    model = Activity()
    form = ActivityForm()
    data = model.getDBbyNo(no)
    form.jenis_kegiatan.data = data[1]
    form.keterangan.data = data[2]
    form.tanggal.data = data[3]
    # form.waktu.data = data[4]
    return render_template('update_form.html', data=data, form=form)

@app.route('/update_process', methods = ['GET', 'POST'])
def update_process():
    form = ActivityForm()
    no = request.form['no']
    jenis_kegiatan = form.jenis_kegiatan.data
    keterangan = form.keterangan.data
    tanggal = form.tanggal.data
    waktu = form.waktu.data
    data = (jenis_kegiatan, keterangan, tanggal, waktu, no)
    model = Activity()
    model.updateDB(data)
    return redirect(url_for('index'))

@app.route('/delete/<no>')
def delete(no):
    model = Activity()
    model.deleteDB(no)
    return redirect(url_for('index'))

@app.route('/delete_rutin/<no>')
def delete_rutin(no):
    model = Activity()
    model.deleteRutin(no)
    return redirect(url_for('rutin'))

@app.route('/delete_rencana/<no>')
def delete_rencana(no):
    model = Activity()
    model.deleteRencana(no)
    return redirect(url_for('rencana'))

@app.route('/delete_tugas/<no>')
def delete_tugas(no):
    model = Activity()
    model.deleteTugas(no)
    return redirect(url_for('tugas'))

@app.route('/rutin')
def rutin():
    model = Activity()
    container = []
    container = model.selectRutin()
    return render_template('rutin.html', container=container)

@app.route('/rencana')
def rencana():
    model = Activity()
    container = []
    container = model.selectRencana()
    return render_template('rencana.html', container=container)

@app.route('/tugas')
def tugas():
    model = Activity()
    container = []
    container = model.selectTugas()
    return render_template('tugas.html', container=container)

if __name__ == '__main__' :
    app.run(debug=True)