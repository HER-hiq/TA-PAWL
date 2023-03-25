from flask_wtf import FlaskForm
from wtforms import TextAreaField, DateField, TimeField, SelectField, SubmitField
import pymysql
import config

db = cursor = None

class Activity:
    def __init__(self, jenis_kegiatan=None, keterangan=None, tanggal=None, waktu=None):
        self.jenis_kegiatan = jenis_kegiatan
        self.keterangan = keterangan
        self.tanggal = tanggal
        self.waktu = waktu
        
    def openDB(self):
        global db, cursor
        db = pymysql.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASSWORD, database = config.DB_NAME)
        cursor = db.cursor()

    def closeDB(self):
        global db, cursor
        db.close()
    
    def selectDB(self):
        self.openDB()
        cursor.execute("select * from activity")
        container = []
        for jenis_kegiatan, keterangan, tanggal, waktu in cursor.fetchall():
            container.append((jenis_kegiatan, keterangan, tanggal, waktu))
        self.closeDB()
        return container
    
    def insertDB(self, data):
        self.openDB()
        cursor.execute("insert into activity(jenis_kegiatan, keterangan, tanggal, waktu) values('%s', '%s')" % data)
        db.commit()
        self.closeDB()


class ActivityForm(FlaskForm):
    jenis_kegiatan = SelectField('Jenis Kegiatan: ', choices=[
        ('Rutin'),
        ('Rencana'),
        ('Tugas'),
        ])
    keterangan = TextAreaField('Keterangan: ')
    tanggal = DateField('Tanggal: ')
    waktu = TimeField('Waktu: ')
    submit = SubmitField('Kirim')