from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk

def incepe_joc():
    for widget in radacina.winfo_children():
        widget.destroy()
    introducere()
    afiseaza_imagine_tkinter("casa_mare.png")
    adauga_butoane_dupa_imagine()



def inchide_joc():
    radacina.destroy()
"functia care inchide aplicatie"



#eticheta de intampinare(TITLUL)
def meniu_principal():
    label_bine_venit=Label(
        radacina,
        text="Bine ai venit în Escape Room",
        font=("Arial", 27),         #font si dimensiune text
        pady=31                     #spatiu vertical intre text si alte elemente
    )
    label_bine_venit.pack()             #adaugam titlul in fereastra

    #eticheta cu intructiuni pentru utlizator
    label_instruc=Label(
        radacina,
        text=("Scopul jocului este să rezolvi puzzle-urile și să reușești să părăsești casa.\n"
            "Ești pregătit să începi?"
        ),
        font=("Arial", 19),
        pady=21
    )
    label_instruc.pack()

    #Buton Start pentru a incepe jocul
    buton_start=Button(
        radacina,
        text="Start",               #textul de pe buton
        font=("Arial", 14),
        width=10,
        height=2,
        command=incepe_joc,         #ce se intampla cand butonul este apasat
        bg="green",                 #culoarea de fundal a butonului
        fg="white"                  #culoarea textului
    )
    buton_start.pack(pady=21)       #adaugam butonul in fereastra

    #Buton Exit pentru a inchide aplicatia
    buton_exit=Button(
        radacina,
        text="Exit",
        font=("Arial", 14),
        width=10,
        height=2,
        command=inchide_joc,
        bg="red",
        fg="white"
    )
    buton_exit.pack(pady=21)



def introducere():
    #adaugam textul introductiv in fereastra
    label_intro= Label(
        radacina,
        text=("Te trezești brusc într-o curte necunoscută. Totul este învăluit de liniște.\n"
            "Ești amețit și confuz, iar în fața ta observi o casă mare și impunătoare.\n"
            "Pare singura opțiune... Ce vei face?"
        ),
        font=("Lucida Handwriting", 15),
        pady=20
    )
    label_intro.pack()


def afiseaza_imagine_tkinter(cale_imagine):
    try:
        imagine = Image.open(cale_imagine)
        imagine = imagine.resize((400, 300), Image.Resampling.LANCZOS)
        imagine_tk = ImageTk.PhotoImage(imagine)
        radacina.imagine_ref = imagine_tk
        label_imagine = Label(radacina, image=imagine_tk)
        label_imagine.pack()
    except FileNotFoundError:
        Label(radacina, text="Imaginea nu a fost găsită!", font=("Arial", 12), fg="red").pack()



def adauga_butoane_dupa_imagine():
    #cream un frame pentru a organiza butoanele pe acelasi rand
    frame_butoane=Frame(radacina)
    frame_butoane.pack(pady=10)

    #buton de intrat in casa
    buton_intra_casa=Button(
        frame_butoane,
        text="Intră în casă",
        font=("Arial", 14),
        bg="blue",
        fg="white"
    )
    buton_intra_casa.pack(side="left", padx=5)

    #buton de fuga
    buton_fugi=Button(
        frame_butoane,
        text="Fugi cât te țin picioarele",
        font=("Arial", 14),
        command=castiga_joc,
        bg="orange",
        fg="black"
    )
    buton_fugi.pack(side="left", padx=5)



def continua_joc():
    #curățăm ecranul și pregătim scena următoare (placeholder pentru jocul care continuă)
    for widget in radacina.winfo_children():
        widget.destroy()



def castiga_joc():
    #afișăm mesajul "Felicitări, ai câștigat" și imaginea
    for widget in radacina.winfo_children():
        widget.destroy()
    Label(
        radacina,
        text="Felicitări, ai câștigat!",
        font=("Lucida Handwriting", 37),
        pady=50,
        fg="green"
    ).pack()
    afiseaza_imagine_tkinter("working,png.jpg")

radacina=Tk()                               #creeaza fereastra principala a aplicatiei
radacina.title("Escape Room")               #seteaza titlul ferestrei
radacina.geometry("900x600")                #seteaza dimensiunea ferestrei in pixeli
meniu_principal()
radacina.mainloop()                         #mentine aplicatia deschisa si interactiva