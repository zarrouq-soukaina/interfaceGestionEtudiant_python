from  tkinter import *
from  tkinter import ttk

from tkinter.ttk import Treeview
import tkinter.messagebox as MessageBox
import sqlite3
##########################voir le guide d'utilisation !
class Etudiant:
    def __init__(self,root):
        #create object reference instance of database class as p
        p = Database()
        p.conn()
        self.root = root
        self.root.title("Etudiants et filiéres")
        self.root.geometry("1400x900")
        EID = StringVar
        Enom = StringVar()
        Eprenom = StringVar()
        Eage = StringVar()
        fID = StringVar()
        Fnom = StringVar()
        FIDF = StringVar()
        ###############################################fonctions etudiant#################################
        def clearFi():

            F_nom.delete(0, 'end')
            F_IDF.delete(0, 'end')
            tviewFl.delete(*tviewFl.get_children())

        def showAllFi():

            con = sqlite3.connect("EtudiantFilieres.db")
            c = con.cursor()
            c.execute("SELECT * FROM FILIERE ")
            rows = c.fetchall()
            if len(rows) == 0:
                MessageBox.showinfo("Information", "No Record exists")
            else:
                tviewFl.delete(*tviewFl.get_children())
                for row in rows:
                    tviewFl.insert('', 'end', values=row)

        def insertFi():
            ID = F_IDF.get()
            NOM = F_nom.get() ;

            if ( F_nom.get()== ""  or F_IDF.get() == "" ):
                MessageBox.showinfo("Insert status", "All filds are required")
            else:
                con = sqlite3.connect("EtudiantFilieres.db")
                c = con.cursor()
                queery = "insert into FILIERE values (?,?)"
                c.execute(queery, (   ID, NOM ))
                c.execute("commit");

                MessageBox.showinfo("Insert status", "Inserted Successfully");
                F_nom.delete(0, 'end')
                F_IDF.delete(0, 'end')

                con.close();

        def deleteFi():

            if (F_IDF.get() == "" ):
                MessageBox.showinfo("Delete status", "ID is compolsary for delete")
            else:

                con = sqlite3.connect("EtudiantFilieres.db")
                c = con.cursor()
                c.execute("SELECT * from FILIERE where IdFiliere ='" + F_IDF.get() + "'")
                rows = c.fetchall()
                if len(rows) == 0:
                    MessageBox.showinfo("Delete status", "id not found!");
                else:
                    c.execute("SELECT * FROM ETUDIANT where IDFiliereK ='" + F_IDF.get() + "'")
                    rows = c.fetchall()
                    if len(rows) == 0:
                        c.execute("delete from FILIERE where IdFiliere = ?", (F_IDF.get(),))

                        c.execute("commit");
                        MessageBox.showinfo("Delete status", "Deleted Successfully !");

                    else:
                        c.execute("delete from FILIERE where IdFiliere = ?", (F_IDF.get(),))

                        c.execute("delete from ETUDIANT where IDFiliereK = ?", (F_IDF.get(),))

                        c.execute("commit");
                        MessageBox.showinfo("Delete status", "Deleted Successfully");
                        con.close();






        def updateFi() :


            if (F_IDF.get() == ""):
                MessageBox.showinfo("Insert status", "ID is compolsary for delete")

            else:
                con = sqlite3.connect("EtudiantFilieres.db")
                c = con.cursor()
                c.execute("SELECT * FROM FILIERE where IdFiliere ='" + F_IDF.get() + "'")
                rows = c.fetchall()
                if len(rows) == 0:
                    MessageBox.showinfo("Update status", " id not found , try with another one  !");
                else :

                    c.execute("update FILIERE set IdFiliere='" + F_IDF.get() + "' , nomF='" + F_nom.get() + "' ")
                    c.execute("commit");
                    MessageBox.showinfo("Update statut ", "Updated Successfully");

                    F_nom.delete(0, 'end')
                    F_IDF.delete(0, 'end')

                    con.close();


        def getFi() :

            if (F_IDF.get() == ""):
                MessageBox.showinfo("Delete status", "ID is compolsary for delete")
            else:
                con = sqlite3.connect("EtudiantFilieres.db")
                c = con.cursor()
                c.execute("SELECT * FROM FILIERE where IdFiliere ='" + F_IDF.get() + "'")
                rows = c.fetchall()
                if len(rows) == 0:
                    MessageBox.showinfo("Get status", " id not found, try with another one!");
                else:
                    c.execute("select * from FILIERE where IdFiliere ='" + F_IDF.get() + "'")
                    rows = c.fetchall()

                    for row in rows:
                        F_nom.insert(0, row[1])


                    con.close()






        ############################################### fonctions Etudiant#############################################
        def clearEt():
            e_nom.delete(0, 'end')
            e_prenom.delete(0, 'end')
            e_age.delete(0, 'end')
            F_ID.delete(0, 'end')
            E_ID.delete(0, 'end')
            tviewEt.delete(*tviewEt.get_children())


        def insertEt():
            nom = e_nom.get()
            prenom = e_prenom.get();
            age = e_age.get();
            IDfiliere = F_ID.get();
            IDEtudiant = E_ID.get();


            if (nom == "" or prenom == "" or age == "" or IDfiliere == "" or IDEtudiant == ""):
                MessageBox.showinfo("Insert status", "All filds are required")
            else:
                con = sqlite3.connect("EtudiantFilieres.db")
                c = con.cursor()
                c.execute("SELECT * FROM FILIERE where IdFiliere ='"+ IDfiliere +"'")
                rows = c.fetchall()
                if len(rows) == 0:
                    MessageBox.showinfo("Insert status", "id filiére not found , try with another one ")
                else:

                    queery = "insert into Etudiant values (?,?,?,?,?)"
                    c.execute(queery, (IDEtudiant, nom, prenom, age, IDfiliere))
                    c.execute("commit");

                    MessageBox.showinfo("Insert status", "Inserted Successfully");
                    e_nom.delete(0, 'end')
                    e_prenom.delete(0, 'end')
                    e_age.delete(0, 'end')
                    F_ID.delete(0, 'end')
                    E_ID.delete(0, 'end')
                    con.close();

        def deleteEt():
            if(E_ID.get()== ""):
                MessageBox.showinfo("Delete status", "ID is compolsary for delete")
            else:

                con = sqlite3.connect("EtudiantFilieres.db")
                c = con.cursor()
                c.execute("SELECT * FROM ETUDIANT where IdEtudiant  ='" + E_ID.get() + "'")
                rows = c.fetchall()
                if len(rows) == 0:
                    MessageBox.showinfo("Delete status", " id not found , try with another one !");
                else :
                    c.execute("delete from Etudiant where IdEtudiant = ?", (E_ID.get(),))
                    c.execute("commit");

                    MessageBox.showinfo("Delete status", "Deleted Successfully");
                    con.close();



        def updateEt() :
            nom = e_nom.get()
            prenom = e_prenom.get();
            age = e_age.get();
            IDfiliere = F_ID.get();
            IDEtudiant = E_ID.get();

            if (nom == "" or prenom == "" or age == "" or IDfiliere == "" or IDEtudiant == ""):
                MessageBox.showinfo("Update status", "All filds are required")
            else:
                con = sqlite3.connect("EtudiantFilieres.db")
                c = con.cursor()
                c.execute("SELECT * FROM ETUDIANT where IdEtudiant  ='" + IDEtudiant + "'")
                rows = c.fetchall()
                if len(rows) == 0:
                    MessageBox.showinfo("Update status", " id not found !");
                else :
                    c.execute("SELECT * FROM FILIERE where IdFiliere ='" + F_IDF.get() + "'")
                    rows = c.fetchall()
                    if len(rows) == 0:
                        MessageBox.showinfo("Update status", " id Filiere not found , try with another id Filiere !");
                    else :
                        c.execute("update Etudiant set IdEtudiant='" + IDEtudiant + "' , nom='" + nom + "' , prenom= '" + prenom + "',age ='" + age + "' ,IDFiliereK = '" + IDfiliere + "' ")

                        c.execute("commit");
                        e_nom.delete(0, 'end')
                        e_prenom.delete(0, 'end')
                        e_age.delete(0, 'end')
                        F_ID.delete(0, 'end')
                        E_ID.delete(0, 'end')
                        MessageBox.showinfo("Update statut ", "Updated Successfully");
                        con.close();

        def getEt() :
            if (E_ID.get() == ""):
                MessageBox.showinfo("Delete status", "ID is compolsary for delete")
            else:
                con = sqlite3.connect("EtudiantFilieres.db")
                c = con.cursor()
                c.execute("SELECT * FROM ETUDIANT where IdEtudiant  ='" + E_ID.get()  + "'")
                rows = c.fetchall()
                if len(rows) == 0:
                    MessageBox.showinfo("Get status", " id not found !");
                else :
                    c.execute("select * from Etudiant where IdEtudiant='" + E_ID.get() + "'")
                    rows = c.fetchall()

                    for row in rows:
                        e_nom.insert(0, row[1])
                        e_prenom.insert(0, row[2])
                        e_age.insert(0, row[3])
                        F_ID.insert(0, row[1])
                    con.close()


        def showAllET():
            con = sqlite3.connect("EtudiantFilieres.db")
            c = con.cursor()
            c.execute("SELECT * FROM Etudiant")
            rows = c.fetchall()
            if len(rows) == 0:
                MessageBox.showinfo("Information", "No Record exists")
            else:
                tviewEt.delete(*tviewEt.get_children())
                for row in rows:
                    tviewEt.insert('', 'end', values=row)
        ############################################# frame header #############################

        MainFrame = Frame(self.root , bg= "white")
        MainFrame.grid()
        HeadFrame =Frame(MainFrame , bd=1 , padx=50 , pady=10, bg="sea green", relief=RIDGE)
        HeadFrame.pack(side=TOP)
        self.ITitle=Label(HeadFrame , text = "    Institut National de Statistique et d'Economie Appliquée",
                    bg = "sea green", fg = 'black', font = ("bold",25))
        self.ITitle.grid()


        #########################################frame etudiant ################################
        FrameEtudiant = LabelFrame(root, text='Étudiant', width=650, height=645, bd=2, bg='sea green',
                                   font=('bold', 20)).place(x=14, y=102)
        frameEt = LabelFrame(FrameEtudiant, width=632, height=556, bd=2, font=('bold', 20)).place(x=23, y=130)
        tviewEt = Treeview(frameEt, columns=(1, 2, 3, 4, 5), show='headings', height=12)
        tviewEt.place(x=56, y=430)

        tviewEt.heading(1, text='id étudinat')
        tviewEt.column(1, anchor='center', width=90)

        tviewEt.heading(2, text='nom')
        tviewEt.column(2, anchor='center', width=120)

        tviewEt.heading(3, text='prénom')
        tviewEt.column(3, anchor='center', width=120)

        tviewEt.heading(4, text='age')
        tviewEt.column(4, anchor='center', width=95)

        tviewEt.heading(5, text='id filière')
        tviewEt.column(5, anchor='center', width=125)

        scroll_et = Scrollbar(frameEt, orient=VERTICAL, command=tviewEt.yview)
        tviewEt.configure(yscroll=scroll_et.set)
        scroll_et.place(x=600, y=450)

        #################################### entresEtudiant ################################
        E_ID= Entry(root, width=32, borderwidth=4)
        E_ID.place(x=290, y=183)
        E_ID.focus()
        e_nom= Entry(root, width=32, borderwidth=4)
        e_nom.place(x=290, y=235)
        e_prenom = Entry(root, width=32, borderwidth=4)
        e_prenom.place(x=290, y=286)
        e_age= Entry(root, width=32, borderwidth=4)
        e_age.place(x=290, y=338)
        F_ID = Entry(root, width=32, borderwidth=4)
        F_ID.place(x=290, y=390)

        ################################ register etudiant ###################################
        EID = Label(root, text=" ID étudiant:", width=24, height=2, bg="PaleGreen3").place(x=50, y=180)
        Enom = Label(root, text=" Nom:", width=24, height=2, bg="PaleGreen3").place(x=50, y=232)
        Eprenom = Label(root, text="Prénom:", width=24, height=2, bg="PaleGreen3").place(x=50, y=282)
        Eage= Label(root, text=" Age :", width=24, height=2, bg="PaleGreen3").place(x=50, y=338)
        FID= Label(root, text=" ID de filiére  :", width=24, height=2, bg="PaleGreen3").place(x=50, y=390)



        #################################frame filiere###################################
        FrameFilere = LabelFrame(root, text='Filière', width=650, height=645, bg='sea green', bd=2,
                                 font=('bold', 20)).place(x=688, y=102)
        frameFl = LabelFrame(FrameFilere, width=632, height=556, bd=2, font=('bold', 20)).place(x=697, y=130)

        tviewFl = Treeview(frameFl, columns=(1, 2), show='headings', height=12)
        tviewFl.place(x=790, y=340)
        tviewFl.heading(1, text='id filière')
        tviewFl.column(1, anchor='center', width=130)
        tviewFl.heading(2, text='nom filière')
        tviewFl.column(2, anchor='center', width=330)
        scroll_fl = Scrollbar(frameFl, orient=VERTICAL, command=tviewFl.yview)
        tviewFl.configure(yscroll=scroll_fl.set)
        scroll_fl.place(x=1254, y=360)
        ################"###################ENTRIES FILIÈRE #######################

        F_IDF =  Entry(root, width=32, borderwidth=4)
        F_IDF.place(x=990, y=278)
        F_nom = Entry(root, width=32, borderwidth=4)
        F_nom.place(x=990, y=228)
        F_nom.focus()
        ######################################### register filiere##################

        FIDF = Label(root, text="ID filière ", width=24, height=2, bg="PaleGreen3").place(x=740, y=275)
        Fnom = Label(root, text="Nom filière :", width=24, height=2, bg="PaleGreen3").place(x=740, y=225)


        ####################################button Etudiant#####################"


        insertEt = Button(FrameEtudiant, text="save", width=9, height=2, fg="black", bg="honeydew2",font=("Calibri",15 ),command=insertEt).place(x=21, y=698)
        deletetEt = Button(FrameEtudiant, text="Delete", width=9, height=2, fg="black", bg="honeydew2",font=("Calibri", 15), command=deleteEt).place(x=129, y=698)
        updateEt = Button(FrameEtudiant, text="Update ", width=9, height=2, fg="black", bg="honeydew2", font=("Calibri", 15), command=updateEt).place(x=237, y=698)
        getEt = Button(FrameEtudiant, text="Get", width=9, height=2, fg="black", bg="honeydew2", font=("Calibri", 15),command=getEt).place(x=344, y=698)
        clearEt = Button(FrameEtudiant, text="Clear", width=9, height=2, fg="black", bg="honeydew2", font=("Calibri", 15),command=clearEt).place(x=453, y=698)
        showAllET=Button(FrameEtudiant, text="show all", width=9, height=2, fg="black", bg="honeydew2", font=("Calibri", 15),command=showAllET).place(x=561, y=698)


        ################################### button Filiere ######################
        insertFi = Button(FrameEtudiant, text="Save", width=9, height=2, fg="black", bg="honeydew2",font=("Calibri", 15), command=insertFi).place(x=696, y=698)
        deletetFi = Button(FrameEtudiant, text="Delete", width=9, height=2, fg="black", bg="honeydew2", font=("Calibri", 15), command=deleteFi).place(x=804, y=698)
        updateFi = Button(FrameEtudiant, text="Update", width=9, height=2, fg="black", bg="honeydew2",font=("Calibri", 15), command=updateFi).place(x=912, y=698)
        getFi = Button(FrameEtudiant, text="Get", width=9, height=2, fg="black", bg="honeydew2", font=("Calibri", 15),command=getFi).place(x=1020, y=698)
        clearFi = Button(FrameEtudiant, text="Clear", width=9, height=2, fg="black", bg="honeydew2",font=("Calibri", 15), command=clearFi).place(x=1127, y=698)
        showAllFi = Button(FrameEtudiant, text="show all", width=9, height=2, fg="black", bg="honeydew2",font=("Calibri", 15), command=showAllFi).place(x=1234, y=698)


# header



#Back end database:
class Database:
    def conn(self):
        con=sqlite3.connect("EtudiantFilieres.db")
        c = con.cursor()
        c.execute("""  CREATE TABLE IF NOT EXISTS FILIERE (
                IdFiliere INTEGER PRIMARY KEY NOT NULL ,
                nomF TEXT NOT NULL
                )
                """)
        c.execute("""CREATE TABLE IF NOT EXISTS Etudiant(
        IdEtudiant INTEGER NOT NULL PRIMARY KEY  ,
        nom TEXT NOT NULL ,
        prenom TEXT NOT NULL ,
        age INTEGER NOT NULL,
        IDFiliereK INTEGER NOT NULL ,
        FOREIGN KEY (IDFiliereK) REFERENCES FILIERE (IdFiliere)
        ON UPDATE SET NULL
        ON DELETE SET NULL

        )""")



        con.commit()
        con.close()
        ########### Lef fonction Etudiant :






if __name__ =='__main__' :
    root=Tk()
    application = Etudiant(root)
    root.mainloop()