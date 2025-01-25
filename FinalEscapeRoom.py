from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
import pygame

# Funcție pentru a reda sunetul de fundal
def reda_sunet_fundal():
    pygame.mixer.init()  # Inițializează mixerul
    pygame.mixer.music.load("fundal_horror.mp3.mp3")  # Înlocuiește cu calea fișierului tău audio
    pygame.mixer.music.play(-1)  # Redă în buclă (-1 pentru repetare infinită)

# Funcție pentru a opri sunetul de fundal
def opreste_sunet_fundal():
    pygame.mixer.music.stop()

def afisare_treptata(label, text, index=0, interval=50, callback=None):
    if index < len(text):
        label.config(text=label.cget("text") + text[index])
        radacina.after(interval, afisare_treptata, label, text, index + 1, interval, callback)
    else:
        if callback:
            callback()

def afiseaza_imagine_tkinter(cale_imagine):
    try:
        imagine = Image.open(cale_imagine)
        imagine = imagine.resize((500, 400), Image.Resampling.LANCZOS)
        imagine_tk = ImageTk.PhotoImage(imagine)
        radacina.imagine_ref = imagine_tk
        label_imagine = Label(radacina, image=imagine_tk, bg="black")
        label_imagine.pack(pady=10)
    except FileNotFoundError:
        Label(radacina, text="Imaginea nu a fost găsită!", font=("Arial", 12), fg="red").pack()


def seteaza_fundal():
    global fundal_horror_tk
    imagine_fundal = Image.open("fundalhorror.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 1200), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def seteaza_fundal2():
    global fundal_horror_tk
    imagine_fundal = Image.open("cabana.png")
    imagine_fundal = imagine_fundal.resize((1600, 1200), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def seteaza_fundal_scrisoare1():
    global fundal_horror_tk
    imagine_fundal = Image.open("scrisoare1.jpg")
    imagine_fundal = imagine_fundal.resize((1170, 946), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def seteaza_fundal_scrisoare2():
    global fundal_horror_tk
    imagine_fundal = Image.open("scrisoare2.jpg")
    imagine_fundal = imagine_fundal.resize((1170, 946), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def meniu_principal():
    frame_meniu = Frame(radacina, bg="black", pady=20)
    frame_meniu.pack(expand=True)

    label_bine_venit = Label(
        frame_meniu,
        text="Bine ai venit în Escape Room",
        font=("Chiller", 37),
        pady=10
    )
    label_bine_venit.pack()

    label_instruc = Label(
        frame_meniu,
        text=("Pregătește-te să înfrunți ce e mai întunecat, pentru că aici nimic nu este ceea ce pare.\n"
                "Ești pregătit să descoperi ce se ascunde în umbrele acestei lumi?"),
        font=("Chiller", 37),
        pady=10
    )
    label_instruc.pack()

    frame_butoane = Frame(frame_meniu, bg="black")
    frame_butoane.pack(pady=10)

    buton_start = Button(
        frame_butoane,
        text="Start",
        font=("Chiller", 29, "bold"),
        width=12,
        command=incepe_joc,
        bg="#330000",
        fg="#FF0000",
        activebackground="#660000",
        activeforeground="#FFFFFF",
        relief="groove",
        bd=3
    )
    buton_start.grid(row=0, column=0, padx=5)

    buton_exit = Button(
        frame_butoane,
        text="Exit",
        font=("Chiller", 29, "bold"),
        width=12,
        command=inchide_joc,
        bg="#111111",
        fg="#990000",
        activebackground="#220000",
        activeforeground="#FFAAAA",
        relief="ridge",
        bd=3
    )
    buton_exit.grid(row=0, column=1, padx=5)

# Funcție pentru a începe jocul
def incepe_joc():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal2()
    reda_sunet_fundal()  # Pornește sunetul de fundal
    introducere()

# Funcție pentru a închide jocul
def inchide_joc():
    opreste_sunet_fundal()  # Oprește sunetul de fundal
    radacina.destroy()

def introducere():
    label_intro = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_intro.pack(pady=10)
    text_intro=("Te trezești brusc, cu inima bătând nebunește în piept. Capul îți zvâcnește de durere, \n"
              "iar în jur totul e învăluit de o ceață densă și nefirească.\n"
              " Aerul rece îți pătrunde în plămâni, iar mirosul de pământ ud și mucegai îți invadează nările. \n"
              "Te ridici încet, amețit și nesigur, încercând să-ți recapeți echilibrul. \n"
              "Nu-ți amintești cum ai ajuns aici, dar sentimentul apăsător de a fi urmărit îți dă fiori pe \n"
              "șira spinării..Ești amețit și confuz, iar în fața ta observi o casă impunătoare.\n"
              "Pare singura opțiune... Ce vei face?")
    afisare_treptata(label_intro, text_intro, interval=50, callback=adauga_butoane_dupa_imagine)


def adauga_butoane_dupa_imagine():
    frame_butoane = Frame(radacina, bg="black")
    frame_butoane.pack(pady=20)

    buton_intra_casa = Button(
        frame_butoane,
        text="Intră în casă",
        font=("Chiller", 27),
        bg="#2e2e2e",  # gri inchis
        fg="white",
        command=scena_usa_incuiata
    )
    buton_intra_casa.pack(side="left", padx=5)

    buton_fugi = Button(
        frame_butoane,
        text="Fugi cât te țin picioarele",
        font=("Chiller", 27),  # Font mai puternic pentru un impact mai mare
        bg="#8b0000",  # Roșu închis
        fg="white",  # Text alb pentru contrast
        command=castiga_joc
    )
    buton_fugi.pack(side="left", padx=5)

def continua_joc():
    for widget in radacina.winfo_children():
        widget.destroy()

def castiga_joc():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    Label(
        radacina,
        text="Felicitări, ai câștigat!",
        font=("Chiller", 37),
        pady=20,
        fg="green"
    ).pack(pady=20)
    afiseaza_imagine_tkinter("working.png")


def scena_usa_incuiata():
    continua_joc()
    seteaza_fundal()

    text_scrisoare = (
        "Cu inima bătând nebunește, pășești în casă. Aerul e greu, înțesat de un miros rânced, iar scândurile podelei \n"
        "scârțâie sub greutatea ta. Deodată, un zgomot asurzitor sparge liniștea – o bubuitură puternică răsună în spatele tău. \n"
        "Te întorci brusc, dar tot ce vezi este ușa... acum încuiată. Încerci cu disperare să o deschizi, trăgând de mâner,\n"
        " lovind cu pumnii, dar totul e în zadar. Te simți prins ca într-o capcană. Ești singur, înconjurat de pereți tăcuți \n"
        "și întunecați. Singura ta opțiune este să explorezi casa. Vei încerca să găsești o cale de scăpare?"
    )

    label_scrisoare = Label(
        radacina,
        text="",  # Inițial, textul este gol
        font=("Chiller", 33),
        wraplength=1300,
        pady=20,
        fg="white"
    )
    label_scrisoare.pack()
    afisare_treptata(label_scrisoare, text_scrisoare, interval=50, callback=continua_inspectia)

def continua_inspectia():
    buton_continua = Button(
        radacina,
        text="Continuă să inspectezi casa",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=scena_reguli
    )
    buton_continua.pack(pady=20)

def scena_reguli():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    frame_reguli = Frame(radacina, bg="black", pady=20)
    frame_reguli.pack(expand=True)

    label_bine_venit = Label(
        frame_reguli,
        text="Pentru a evada din casă, trebuie să îți folosești inteligența și să rezolvi\n"
             " puzzle-urile pregătite pentru tine cât mai rapid. \n"
             "Ai la dispoziție 30 de minute pentru a scăpa, iar timpul începe să se scurgă \n"
             "din momentul în care începi prima probă. \n"
             "Fii atent! Fiecare greșeală te va costa un minut din timpul prețios. \n"
             "Tensiunea crește cu fiecare secundă, iar evadarea depinde doar de tine.\n"
            "Ești pregătit să înfrunți provocarea și să începi jocul?",
        font=("Arial", 27),
        fg="#FF0000",
        pady=10
    )
    label_bine_venit.pack()

    frame_buton = Frame(frame_reguli, bg="black")
    frame_buton.pack(pady=10)

    buton_start = Button(
        frame_buton,
        text="Începe jocul",
        font=("Lucida Handwriting", 29, "bold"),
        width=12,
        command=scena_prima_proba,
        bg="#330000",
        fg="#FF0000",
        activebackground="#660000",
        activeforeground="#FFFFFF",
        relief="groove",
        bd=3
    )
    buton_start.grid(row=0, column=0, padx=5)


def scena_prima_proba():
    # Curățăm fereastra pentru prima probă
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    # Textul introductiv
    text_introductiv = (
        "Te trezești într-o casă întunecată și înfricoșătoare. Pereții par să șoptească povești de groază, iar lumina\n"
        " abia pătrunde prin ferestrele prăfuite. Totul în jur te face să simți un fior rece pe șira spinării.\n"
        "Privirea îți cade asupra unei foi de hârtie aruncate lângă ușă. Este îngălbenită și pătată, ca și cum ar fi\n"
        " fost acolo de ani de zile. Simți o curiozitate inexplicabilă, dar și o teamă care îți strânge inima.\n"
        "Ce faci? Decizi să ridici hârtia și să o citești? Sau rămâi pe loc, întrebându-te ce se va întâmpla în continuare?"
    )

    label_introductiv = Label(
        radacina,
        text="",  # Textul este inițial gol
        font=("Chiller", 33),
        wraplength=1100,
        pady=20,
        fg="white"
    )
    label_introductiv.pack()
    afisare_treptata(label_introductiv, text_introductiv, interval=50, callback=butoane_scrisoare)

def butoane_scrisoare():
    frame_butoane = Frame(radacina, bg="black")
    frame_butoane.pack(pady=10)

    # Buton pentru "Inspectează foaia"
    Button(
        frame_butoane,
        text="Inspectează foaia",
        font=("Lucida Handwriting", 17),
        bg="#003366",  # Albastru închis, pentru a crea o atmosferă misterioasă și rece
        fg="white",  # Text alb pentru contrast
        activebackground="#000080",  # Culoare mai închisă când este apăsat
        activeforeground="#FFFF00",  # Text galben când este apăsat, pentru un efect de atenționare
        command=scena_inspecteaza_foaia1
    ).pack(side="left", padx=10)

    # Buton pentru "Ignoră foaia"
    Button(
        frame_butoane,
        text="Ignoră foaia",
        font=("Lucida Handwriting", 17),
        bg="#8B0000",  # Roșu închis, pentru a crea un sentiment de pericol
        fg="white",  # Text alb pentru contrast
        activebackground="#B22222",  # Roșu mai deschis când este apăsat
        activeforeground="#FFFF00",  # Text galben aprins când este apăsat
        command=scena_ignora_foaia
    ).pack(side="left", padx=10)


# Scena pentru "Inspectează foaia"
def scena_inspecteaza_foaia1():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal_scrisoare1()

    Button(
        radacina,
        text="Partea 2",
        font=("Lucida Handwriting", 19),
        bg="#4B0082",  # Violet închis pentru un efect misterios și sumbru
        fg="white",  # Text alb pentru contrast puternic
        activebackground="#800080",  # Violet mai intens când este apăsat, pentru a adânci senzația de tensiune
        activeforeground="#FFFF00",  # Text galben când este apăsat, pentru un efect de alertă
        command=scena_inspecteaza_foaia2  # Legătura corectă cu scena holului
    ).pack(pady=20)

def scena_inspecteaza_foaia2():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal_scrisoare2()

    frame_foaia2 = Frame(radacina, bg="black")
    frame_foaia2.pack(pady=10)

    Button(
        frame_foaia2,
        text="Partea 1",
        font=("Lucida Handwriting", 19),
        bg="#003366",  # Albastru închis, pentru a crea o atmosferă misterioasă și rece
        fg="white",  # Text alb pentru contrast
        activebackground="#000080",  # Culoare mai închisă când este apăsat
        activeforeground="#FFFF00",  # Text galben când este apăsat, pentru un efect de atenționare
        command=scena_inspecteaza_foaia1
    ).pack(side="left", padx=10)

    Button(
        frame_foaia2,
        text="Mai departe",
        font=("Lucida Handwriting", 19),
        bg="#8B0000",  # Roșu închis, pentru a crea un sentiment de pericol
        fg="white",  # Text alb pentru contrast
        activebackground="#B22222",  # Roșu mai deschis când este apăsat
        activeforeground="#FFFF00",  # Text galben aprins când este apăsat
        command=ai_citit_scrisoarea
    ).pack(side="left", padx=10)


def ai_citit_scrisoarea():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    text_scrisoare = (
        "După ce citești scrisoarea, frica ta devine realitate. Simți o prezență nevăzută care te urmărește din umbre,\n"
        " iar timpul pare să se scurgă tot mai repede. Respiri greu, dar știi că trebuie să mergi mai departe."
        "Iei cu tine lumânarea pe care ai vazut-o, singura ta sursă de lumină. Cu flacăra tremurândă în mână,\n"
        " faci un pas înainte. Nu te poți opri acum. Cineva – sau ceva – te urmărește."
    )

    label_scrisoare = Label(
        radacina,
        text="",  # Text inițial gol
        font=("Chiller", 33),
        wraplength=1100,
        pady=20,
        fg="white"
    )
    label_scrisoare.pack()

    # Afișare treptată a textului
    afisare_treptata(label_scrisoare, text_scrisoare, interval=50, callback=continua_povestea)

def continua_povestea():
    Button(
        radacina,
        text="Continuă povestea",
        font=("Lucida Handwriting", 19),
        bg="#2F4F4F",  # O nuanță de verde închis pentru un efect sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#A52A2A",
        # O nuanță de roșu închis pentru a adăuga un sentiment de pericol când butonul este apăsat
        activeforeground="yellow",  # Text galben pentru un contrast alertant când este apăsat
        command=scena_hol  # Legătura corectă cu scena holului
    ).pack(pady=20)


# Scena holului (continuare comună după alegerea foii)
def scena_hol():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    text_hol = ("Te uiți în capătul holului și realizezi că acolo se află bucătăria.\n "
                "Însă până acolo mai sunt două camere: una cu ușa închisă, iar cealaltă are ușa întredeschisă.\n"
                "Unde dorești să intri prima dată?"
                )
    label_hol = Label(
        radacina,
        text="",
        font=("Chiller", 33),
        wraplength=800,
        pady=20,
        fg="white",
        bg="black"
    )
    label_hol.pack()
    afisare_treptata(label_hol, text_hol, interval=50, callback=decizie_incapere)

def decizie_incapere():
    frame_butoane = Frame(radacina, bg="black")
    frame_butoane.pack(pady=10)

    Button(
        frame_butoane,
        text="Bucătărie",
        font=("Lucida Handwriting", 19),
        bg="#2F4F4F",  # Gri închis pentru un fundal mai sumbru
        fg="white",  # Text alb pentru contrast puternic
        activebackground="#8B0000",  # Roșu închis când este apăsat pentru a adăuga un efect de pericol
        activeforeground="black",  # Text negru când butonul este apăsat
        command=scena_bucatarie
    ).pack(side="left", padx=10)

    Button(
        frame_butoane,
        text="Camera cu ușa închisă",
        font=("Lucida Handwriting", 19),
        bg="#8B0000",  # Roșu închis, o culoare care sugerează pericol sau groază
        fg="white",  # Text alb pentru contrast
        activebackground="#A52A2A",  # Roșu-maro pentru un efect de alarmă când butonul este apăsat
        activeforeground="black",  # Text negru
        command=scena_usa_inchisa
    ).pack(side="left", padx=10)

    Button(
        frame_butoane,
        text="Camera cu ușa întredeschisă",
        font=("Lucida Handwriting", 19),
        bg="#A9A9A9",  # Gri deschis pentru un ton de întuneric, dar nu la fel de sumbru ca negrul total
        fg="black",  # Text negru pentru un contrast puternic
        activebackground="#8B0000",  # Roșu închis pentru o reacție de alertă
        activeforeground="white",  # Text alb pentru contrast când este apăsat
        command=scena_usa_intredeschisa
    ).pack(side="left", padx=10)


# Placeholder pentru cele trei alegeri din scena holului
def scena_bucatarie():
    print("Se trece la scena bucătărie (de implementat)")

def scena_usa_inchisa():
    print("Se trece la scena cu ușa închisă (de implementat)")

def scena_usa_intredeschisa():
    print("Se trece la scena cu ușa întredeschisă (de implementat)")

def scena_ignora_foaia():
    print("TREBUIE SA CONTINUI!")


# Crearea ferestrei principale
radacina = Tk()
radacina.title("Escape Room")
radacina.geometry("900x600")
radacina.option_add("*Label.background", "black")
radacina.option_add("*Label.foreground", "white")
seteaza_fundal()
meniu_principal()

# Redarea sunetului de fundal din momentul în care aplicația pornește
reda_sunet_fundal()

radacina.mainloop()