"""from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
import pygame                                   #pentru sunet



def seteaza_fundal():
    global fundal_horror_tk
    imagine_fundal= Image.open("fundalhorror.jpg")                                              #deschiderea imaginii de fundal
    imagine_fundal= imagine_fundal.resize((900,600), Image.Resampling.LANCZOS)             #i.r.l utilizata pt a mentine calitatea imaginii in timpul redimensionarii
    imagine_fundal_tk=ImageTk.PhotoImage(imagine_fundal)                                        #convertirea imaginii intr un obiect tkinter compatinil necesar pt afisare in tkinter
    label_fundal=Label(radacina, image=imagine_fundal_tk)                                    #cream un widget label care contine imaginea ca fundal, poate afisa atat texte cat si imagini
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)                                       #x,y=0 seteaza pozitita din coltul stanga sus, iar rw,rh=1 asigura ca img ocupa intreaga fereastra
    radacina.fundal_ref=imagine_fundal_tk                                                       #saalvam referinta imaginii in obiectul radacine pt ca tkinter elimina automat imaginile fara referinta



def incepe_joc():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
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
        fg="white",
        command=usa_incuiata
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
    seteaza_fundal()
    Label(
        radacina,
        text="Felicitări, ai câștigat!",
        font=("Lucida Handwriting", 37),
        pady=50,
        fg="green"
    ).pack()
    afiseaza_imagine_tkinter("working.png")


def usa_incuiata():
    pygame.mixer.init()
    sunet_incuiere=pygame.mixer.Sound("door_locked.mp3")
    sunet_incuiere.play()

    continua_joc()
    seteaza_fundal()

    Label(
        radacina,
        text=("Te-ai speriat foarte tare auzind o bubuitură și \n ai realizat că ești încuiaț.\n"
               "\n\nÎncepi să te panichezi și vrei să deschizi ușa."),
        font=("Lucida Handwriting", 21),
        pady=20,
        fg="white"
    ).pack()

    buton_deschide_usa=Button(
        text="Încearcă să deschizi ușa",
        font=("Arial", 21),
        bg="purple",
        fg="white"
    )
    buton_deschide_usa.pack(pady=45)

radacina=Tk()                               #creeaza fereastra principala a aplicatiei
radacina.title("Escape Room")               #seteaza titlul ferestrei
radacina.geometry("900x600")                #seteaza dimensiunea ferestrei in pixeli
radacina.option_add("*Label.background", "black")  #fundal negru pentru toate Label-urile
radacina.option_add("*Label.foreground", "white")  #text alb pentru toate Label-urile
seteaza_fundal()
meniu_principal()
radacina.mainloop()                         #mentine aplicatia deschisa si interactiva



# * este un wildcard (caracter general) care înseamnă "pentru toate widget-urile" de un anumit tip.
#combinarea *Label.option înseamnă: aplica regula specificată la toate widget-urile de tip Label"""

from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
import pygame  # pentru sunet

def seteaza_fundal():
    global fundal_horror_tk
    imagine_fundal = Image.open("fundalhorror.jpg")
    imagine_fundal = imagine_fundal.resize((900, 600), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def incepe_joc():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    introducere()
    afiseaza_imagine_tkinter("casa_mare.png")
    adauga_butoane_dupa_imagine()

def inchide_joc():
    radacina.destroy()

# Eticheta de intampinare (TITLUL)
def meniu_principal():
    frame_meniu = Frame(radacina, bg="black")
    frame_meniu.pack(expand=True, fill="both")

    # Eticheta titlu
    label_bine_venit = Label(
        frame_meniu,
        text="Bine ai venit în Escape Room",
        font=("Arial", 27, "bold"),
        pady=20,
        bg="black",
        fg="red"
    )
    label_bine_venit.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

    # Eticheta cu instrucțiuni
    label_instruc = Label(
        frame_meniu,
        text=(
            "Scopul jocului este să rezolvi puzzle-urile și să reușești să părăsești casa.\n"
            "Ești pregătit să începi?"
        ),
        font=("Arial", 19),
        bg="black",
        fg="white"
    )
    label_instruc.grid(row=1, column=0, columnspan=2, pady=20)

    # Butoane
    buton_start = Button(
        frame_meniu,
        text="Start",
        font=("Arial", 14),
        width=12,
        height=2,
        command=incepe_joc,
        bg="green",
        fg="white"
    )
    buton_start.grid(row=2, column=0, padx=10, pady=20, sticky="e")

    buton_exit = Button(
        frame_meniu,
        text="Exit",
        font=("Arial", 14),
        width=12,
        height=2,
        command=inchide_joc,
        bg="red",
        fg="white"
    )
    buton_exit.grid(row=2, column=1, padx=10, pady=20, sticky="w")

def introducere():
    # Adaugam textul introductiv in fereastra
    label_intro = Label(
        radacina,
        text=(
            "Te trezești brusc într-o curte necunoscută. Totul este învăluit de liniște.\n"
            "Ești amețit și confuz, iar în fața ta observi o casă mare și impunătoare.\n"
            "Pare singura opțiune... Ce vei face?"
        ),
        font=("Lucida Handwriting", 15),
        bg="black",
        fg="white",
        pady=20
    )
    label_intro.pack()

def afiseaza_imagine_tkinter(cale_imagine):
    try:
        imagine = Image.open(cale_imagine)
        imagine = imagine.resize((400, 300), Image.Resampling.LANCZOS)
        imagine_tk = ImageTk.PhotoImage(imagine)
        radacina.imagine_ref = imagine_tk
        label_imagine = Label(radacina, image=imagine_tk, bg="black")
        label_imagine.pack(pady=10)
    except FileNotFoundError:
        Label(radacina, text="Imaginea nu a fost găsită!", font=("Arial", 12), fg="red", bg="black").pack()

def adauga_butoane_dupa_imagine():
    # Cream un frame pentru a organiza butoanele pe acelasi rand
    frame_butoane = Frame(radacina, bg="black")
    frame_butoane.pack(pady=10)

    # Buton de intrat in casa
    buton_intra_casa = Button(
        frame_butoane,
        text="Intră în casă",
        font=("Arial", 14),
        bg="blue",
        fg="white",
        command=usa_incuiata
    )
    buton_intra_casa.grid(row=0, column=0, padx=10)

    # Buton de fuga
    buton_fugi = Button(
        frame_butoane,
        text="Fugi cât te țin picioarele",
        font=("Arial", 14),
        bg="orange",
        fg="black",
        command=castiga_joc
    )
    buton_fugi.grid(row=0, column=1, padx=10)

def continua_joc():
    # Curățăm ecranul și pregătim scena următoare (placeholder pentru jocul care continuă)
    for widget in radacina.winfo_children():
        widget.destroy()

def castiga_joc():
    # Afișăm mesajul "Felicitări, ai câștigat" și imaginea
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    Label(
        radacina,
        text="Felicitări, ai câștigat!",
        font=("Lucida Handwriting", 37),
        pady=50,
        fg="green",
        bg="black"
    ).pack()
    afiseaza_imagine_tkinter("working.png")

def usa_incuiata():
    pygame.mixer.init()
    sunet_incuiere = pygame.mixer.Sound("door_locked.mp3")
    sunet_incuiere.play()

    continua_joc()
    seteaza_fundal()

    Label(
        radacina,
        text=("Te-ai speriat foarte tare auzind o bubuitură și \n ai realizat că ești încuiaț.\n"
              "\n\nÎncepi să te panichezi și vrei să deschizi ușa."),
        font=("Lucida Handwriting", 21),
        pady=20,
        fg="white",
        bg="black"
    ).pack()

    buton_deschide_usa = Button(
        text="Încearcă să deschizi ușa",
        font=("Arial", 21),
        bg="purple",
        fg="white"
    )
    buton_deschide_usa.pack(pady=45)

radacina = Tk()
radacina.title("Escape Room")
radacina.geometry("900x600")
radacina.option_add("*Label.background", "black")
radacina.option_add("*Label.foreground", "white")
seteaza_fundal()
meniu_principal()
radacina.mainloop()
