from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, SelectField, SubmitField
import pymysql
import config

db = cursor = None

class Activity:
    def __init__(self, no=None, jenis_kegiatan=None, keterangan=None, tanggal=None, waktu=None):
        self.no = no
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
        cursor.execute("select * from activity order by tanggal desc, waktu")
        container = []
        for no, jenis_kegiatan, keterangan, tanggal, waktu in cursor.fetchall():
            container.append((no, jenis_kegiatan, keterangan, tanggal, waktu))
        self.closeDB()
        return container
    
    def insertDB(self, data):
        self.openDB()
        cursor.execute("insert into activity(jenis_kegiatan, keterangan, tanggal, waktu) values('%s', '%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()

    def insertTugas(self, data):
        self.openDB()
        # cursor.execute("insert into tugas(aktivitas, tanggal, waktu) values('%s', '%s', '%s')" % data)
        cursor.execute("insert into tugas(aktivitas, tanggal, waktu, status) values('%s', '%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()

    def insertRencana(self, data):
        self.openDB()
        cursor.execute("insert into rencana(aktivitas, tanggal, waktu, prioritas) values('%s', '%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()

    def getDBbyNo(self, no):
        self.openDB()
        cursor.execute("select * from activity where no='%s'" % no)
        data = cursor.fetchone()
        return data
    
    def updateDB(self, data):
        self.openDB()
        cursor.execute("update activity set jenis_kegiatan='%s', keterangan='%s', tanggal='%s', waktu='%s' where no=%s" % data)
        db.commit()
        self.closeDB()

    def deleteDB(self, no):
        self.openDB()
        cursor.execute("delete from activity where no=%s" % no)
        db.commit()
        self.closeDB()

    def deleteRutin(self, no):
        self.openDB()
        cursor.execute("delete from rutin where no=%s" % no)
        db.commit()
        self.closeDB()

    def deleteRencana(self, no):
        self.openDB()
        cursor.execute("delete from rencana where no=%s" % no)
        db.commit()
        self.closeDB()

    def deleteTugas(self, no):
        self.openDB()
        cursor.execute("delete from tugas where no=%s" % no)
        db.commit()
        self.closeDB()

    def selectRutin(self):
        self.openDB()
        cursor.execute("select no, keterangan, tanggal, waktu from activity where jenis_kegiatan='Rutin' order by tanggal desc, waktu")
        container = []
        for no, keterangan, tanggal, waktu in cursor.fetchall():
            container.append((no, keterangan, tanggal, waktu))
        self.closeDB()
        return container
    
    def selectRencana(self):
        self.openDB()
        cursor.execute("select no, aktivitas, tanggal, waktu, prioritas from rencana order by tanggal desc, waktu")
        container = []
        for no, aktivitas, tanggal, waktu, prioritas in cursor.fetchall():
            container.append((no, aktivitas, tanggal, waktu, prioritas))
        self.closeDB()
        return container
    
    def selectTugas(self):
        self.openDB()
        # cursor.execute("select no, aktivitas, tanggal, waktu from tugas order by tanggal desc, waktu")
        cursor.execute("select no, aktivitas, tanggal, waktu, status from tugas order by tanggal desc, waktu")
        container = []
        for no, aktivitas, tanggal, waktu, status in cursor.fetchall():
            container.append((no, aktivitas, tanggal, waktu, status))
        self.closeDB()
        return container
    
    

class ActivityForm(FlaskForm):
    jenis_kegiatan = SelectField(choices=[
        ('Rutin'),
        ('Rencana'),
        ('Tugas')
        ])
    aktivitas = StringField()
    keterangan = TextAreaField()
    tanggal = DateField()
    waktu = TimeField()
    submit = SubmitField('Kirim')