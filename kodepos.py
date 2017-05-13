from PyQt4 import QtGui, QtCore
from raw_ui import main_ui
import sys
import myDB
import sqlite3


class Main(QtGui.QMainWindow,main_ui.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        self.koneksiDatabase()
        self.setupUi(self)
        myDB.tampilan()
        self.setWindowTitle('Kode Pos Indonesia')
        self.aksi()
        self.formNormal()
        self.comboProvinsi()

    def aksi(self):
        QtGui.QShortcut(QtGui.QKeySequence("Enter"), self.comboBoxProv, self.onProvEnter, context=QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Return"), self.comboBoxProv, self.onProvEnter, context=QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Enter"), self.comboBoxKab, self.onKabEnter, context=QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Return"), self.comboBoxKab, self.onKabEnter, context=QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Enter"), self.comboBoxKec, self.onKecEnter, context=QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Return"), self.comboBoxKec, self.onKecEnter, context=QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Enter"), self.comboBoxKel, self.onKelEnter, context=QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Return"), self.comboBoxKel, self.onKelEnter, context=QtCore.Qt.WidgetShortcut)
        self.comboBoxProv.currentIndexChanged.connect(self.onProvEnter)
        self.comboBoxKab.currentIndexChanged.connect(self.onKabEnter)
        self.comboBoxKec.currentIndexChanged.connect(self.onKecEnter)
        self.comboBoxKel.currentIndexChanged.connect(self.onKelEnter)
        self.lineEditCari.returnPressed.connect(self.onCariEnter)

    def onCariEnter(self):
        cari = str(self.lineEditCari.text())
        sql = "SELECT kecamatan.nama,kelurahan.nama,kecamatan.kec_id FROM kelurahan LEFT JOIN kecamatan ON kecamatan.kec_id = kelurahan.kec_id WHERE kodepos = '%s' ORDER BY 1"%(cari)
        baris, jumData = self.eksekusi(sql)
        

        if jumData == 0:
            QtGui.QMessageBox.warning(self,"Perhatian!","Tidak ditemukan data")
        else:
            self.tableWidget.setRowCount(jumData)
            for data in range(jumData):                
                sqlKab = "SELECT kabupaten.nama,kabupaten.kab_id FROM kecamatan,kabupaten WHERE kecamatan.kec_id = '%s' AND kecamatan.kab_id = kabupaten.kab_id"%(baris[data][2])
                barKab,jum = self.eksekusi(sqlKab)
                id_kab = barKab[0][1]
                
                sqlProv = "SELECT provinsi.nama,provinsi.prov_id FROM kabupaten,provinsi WHERE kabupaten.prov_id = provinsi.prov_id AND kabupaten.kab_id = '%s'"%(id_kab)                
                barProv,jum = self.eksekusi(sqlProv)
                
                teks = (barProv[0][0],barKab[0][0],baris[data][0],baris[data][1])
                
                for i in range(len(teks)):
                    item = QtGui.QTableWidgetItem()
                    item.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    item.setToolTip(str(teks[i]))
                    item.setText(str(teks[i]))
                    self.tableWidget.setItem(data, i, item)
            self.tableWidget.resizeColumnsToContents()


    def onKelEnter(self):
        kel = str(self.comboBoxKel.currentText()).upper()
        if kel=="":
            self.comboBoxKel.setFocus()
        else:
            sql_id_kel = "SELECT kodepos from kelurahan WHERE nama = '%s' AND kec_id = '%s'"%(kel,self.id_kec)
            bar,jum = self.eksekusi(sql_id_kel)    
            try:
                self.lineEditCari.setFocus()
                self.lineEditKodepos.setText(bar[0][0])
            except:
                QtGui.QMessageBox.warning(self,"Perhatian!","Tidak ditemukan data")
                self.comboBoxKel.setFocus()    
    
    def onKecEnter(self):
        kec = str(self.comboBoxKec.currentText()).upper()
        if kec == "":
            self.comboBoxKec.setFocus()
        else:
            sql_id_kec = "SELECT kec_id from kecamatan WHERE nama = '%s' AND kab_id = '%s'"%(kec,self.id_kab)
            bar,jum = self.eksekusi(sql_id_kec)
            try:
                self.comboBoxKel.setEnabled(True)
                self.comboBoxKel.setFocus()        
                self.comboBoxKel.clear()        
                self.id_kec = bar[0][0]
                sql = "SELECT nama FROM kelurahan WHERE kec_id = '%s'"%(self.id_kec)
                bar,jum = self.eksekusi(sql)
                a = [bar[i][0] for i in range(jum)]
                self.comboBoxKel.addItem("")      
                self.comboBoxKel.addItems(a)
            except:
                QtGui.QMessageBox.warning(self,"Perhatian!","Tidak ditemukan data")
                self.comboBoxKec.setFocus()
    
    def onKabEnter(self):             
        kab = str(self.comboBoxKab.currentText()).upper()
        if kab == "":
            self.comboBoxKab.setFocus()
        else:
            sql_id_kab = "SELECT kab_id from kabupaten WHERE nama = '%s' AND prov_id = '%s'"%(kab,self.id_prov)
            bar,jum = self.eksekusi(sql_id_kab)
            try:
                self.comboBoxKec.setEnabled(True)
                self.comboBoxKec.setFocus()                        
                self.comboBoxKec.clear()           
                self.id_kab = bar[0][0]            
                sql = "SELECT nama FROM kecamatan WHERE kab_id = '%s'"%(self.id_kab)
                bar,jum = self.eksekusi(sql)
                a = [bar[i][0] for i in range(jum)] 
                self.comboBoxKec.addItem("")     
                self.comboBoxKec.addItems(a)
            except:
                QtGui.QMessageBox.warning(self,"Perhatian!","Tidak ditemukan data")
                self.comboBoxKab.setFocus()

    def onProvEnter(self):
        prov = str(self.comboBoxProv.currentText()).upper()
        if prov == "":
            self.comboBoxProv.setFocus()
        else:
            sql_id_prov = "SELECT prov_id from provinsi WHERE nama = '%s'"%(prov)
            bar,jum = self.eksekusi(sql_id_prov)
            try:
                self.comboBoxKab.setEnabled(True)
                self.comboBoxKab.setFocus()                        
                self.comboBoxKab.clear()        
                self.id_prov = bar[0][0]
                sql = "SELECT nama FROM kabupaten WHERE prov_id = '%s'"%(self.id_prov)
                bar,jum = self.eksekusi(sql)
                a = [bar[i][0] for i in range(jum)]
                self.comboBoxKab.addItem("")
                self.comboBoxKab.addItems(a)
            except:
                QtGui.QMessageBox.warning(self,"Perhatian!","Tidak ditemukan data")
                self.comboBoxProv.setFocus()

    def formNormal(self):
        self.comboBoxProv.clear()
        self.comboBoxKab.clear()
        self.comboBoxKec.clear()
        self.comboBoxKel.clear()
        self.comboBoxProv.setEnabled(True)
        self.comboBoxKab.setEnabled(False)
        self.comboBoxKec.setEnabled(False)
        self.comboBoxKel.setEnabled(False)
        self.lineEditKodepos.clear()
        self.lineEditKodepos.setEnabled(False)
        self.lineEditCari.setFocus()

    def koneksiDatabase(self):           
        self.db = sqlite3.connect("database.db")
        self.cur = self.db.cursor()       

    def comboProvinsi(self):
        sql = "SELECT nama FROM provinsi"
        bar,jum = self.eksekusi(sql)
        a = [bar[i][0] for i in range(jum)]
        self.comboBoxProv.addItem("")
        self.comboBoxProv.addItems(a)

    def eksekusi(self,sql):
        self.cur.execute(sql)
        lineData = self.cur.fetchall()
        totData = len(lineData)
        return lineData, totData

    def onClose(self):
        self.db.close()
        self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())