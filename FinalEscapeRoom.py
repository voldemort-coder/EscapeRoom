from tkinter import Tk, Label, Button, Frame, Entry
from PIL import Image, ImageTk
import pygame

# Funcție pentru a reda sunetul de fundal
def reda_sunet_fundal():
    pygame.mixer.init()  # Inițializează mixerul
    pygame.mixer.music.load("fundal_horror.mp3.mp3")
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
    imagine_fundal = imagine_fundal.resize((1600, 1100), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def seteaza_fundal_scrisoare1():
    global fundal_horror_tk
    imagine_fundal = Image.open("scrisoare1.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def seteaza_fundal_scrisoare2():
    global fundal_horror_tk
    imagine_fundal = Image.open("scrisoare2.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def seteaza_fundal_scrisp():
    global fundal_horror_tk
    imagine_fundal = Image.open("scrisp1.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def fundal_tablouri():
    global fundal_horror_tk
    imagine_fundal = Image.open("fundal_tablouri.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def fundal_camera_inchisa():
    global fundal_horror_tk
    imagine_fundal = Image.open("camera_inchisa.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def fundal_foaie():
    global fundal_horror_tk
    imagine_fundal = Image.open("indicii.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def fundal_puzzle_ceasuri():
    global fundal_horror_tk
    imagine_fundal = Image.open("puzzle_ceasuri.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def fundal_scirsp2():
    global fundal_horror_tk
    imagine_fundal = Image.open("scirsp2.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def fundal_davinci():
    global fundal_horror_tk
    imagine_fundal = Image.open("oglinda_scris.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

def seteaza_fundal_working():
    global fundal_horror_tk
    imagine_fundal = Image.open("working.png")
    imagine_fundal = imagine_fundal.resize((1600, 800), Image.Resampling.LANCZOS)
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
        bg="#8b0000",  # gri inchis
        fg="white",
        command=scena_usa_incuiata
    )
    buton_intra_casa.pack(side="left", padx=5)

    buton_fugi = Button(
        frame_butoane,
        text="Fugi cât te țin picioarele",
        font=("Chiller", 27),  # Font mai puternic pentru un impact mai mare
        bg="#2e2e2e",  # Roșu închis
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
    seteaza_fundal_working()




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
    # Buton pentru "Inspectează foaia"
    Button(
        text="Inspectează foaia",
        font=("Lucida Handwriting", 17),
        bg="#003366",  # Albastru închis, pentru a crea o atmosferă misterioasă și rece
        fg="white",  # Text alb pentru contrast
        activebackground="#000080",  # Culoare mai închisă când este apăsat
        activeforeground="#FFFF00",  # Text galben când este apăsat, pentru un efect de atenționare
        command=scena_inspecteaza_foaia1
    ).pack(padx=10)


# Scena pentru "Inspectează foaia"
def scena_inspecteaza_foaia1():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal_scrisoare1()

    Button(
        radacina,
        text="Partea 2",
        font=("Lucida Handwriting", 19),
        bg="#333333",
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
    frame_foaia2.pack(side="bottom", pady=10)

    Button(
        frame_foaia2,
        text="Partea 1",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Albastru închis, pentru a crea o atmosferă misterioasă și rece
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
        " Iei cu tine lumânarea pe care ai vazut-o, singura ta sursă de lumină. Cu flacăra tremurândă în mână,\n"
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

    text_hol = ("Pe hol observi două camere: una cu ușa întredeschisă, lăsând să se vadă o lumină slabă din interior,\n"
                "iar cealaltă cu ușa larg deschisă, dezvăluind întunericul dinăuntru. În capătul holului, o ușă mare încuiată\n"
                "În care dintre cele două camere alegi să intri?"
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
        text="Camera cu ușa întredeschisă",
        font=("Lucida Handwriting", 19),
        bg="#8B0000",  # Roșu închis, o culoare care sugerează pericol sau groază
        fg="white",  # Text alb pentru contrast
        activebackground="#A52A2A",  # Roșu-maro pentru un efect de alarmă când butonul este apăsat
        activeforeground="black",  # Text negru
        command=scena_usa_inchisa
    ).pack(side="left", padx=10)

    Button(
        frame_butoane,
        text="Camera cu ușa deschisă",
        font=("Lucida Handwriting", 19),
        bg="#A9A9A9",  # Gri deschis pentru un ton de întuneric, dar nu la fel de sumbru ca negrul total
        fg="black",  # Text negru pentru un contrast puternic
        activebackground="#8B0000",  # Roșu închis pentru o reacție de alertă
        activeforeground="white",  # Text alb pentru contrast când este apăsat
        command=scena_usa_deschisa
    ).pack(side="left", padx=10)


def scena_usa_inchisa():
    for widget in radacina.winfo_children():
        widget.destroy()
    fundal_camera_inchisa()
    label_intrare = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_intrare.pack(pady=10)
    text_intrare = ("Ușa scârțâie în timp ce o deschizi încet, sunetul făcându-ți inima să bată mai tare. \n"
                    "Înăuntru, ochii îți cad imediat pe o statuie care te face să tresari—pentru o clipă,\n"
                    " ai crezut că e un spirit. Pe pereți, ceasuri cu bufnițe stau înșirate, toate arătând\n"
                    " ore diferite. Nu înțelegi legătura, dar simți că e ceva important. Privirea ți se oprește\n"
                    " în spatele statuii, unde zărești o bucată de hârtie. O iei cu mâinile tremurânde,\n"
                    " întunericul din cameră părând să se apropie de tine...")
    afisare_treptata(label_intrare, text_intrare, interval=50, callback=buton_citeste)

def buton_citeste():
        buton_pleci = Button(
            radacina,
            text="Citește",
            font=("Lucida Handwriting", 19),
            bg="#333333",  # Gri închis pentru un fundal sumbru
            fg="white",  # Text alb pentru contrast
            activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
            activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
            command=foaie
        )
        buton_pleci.pack(pady=20)

def foaie():
        for widget in radacina.winfo_children():
            widget.destroy()
        fundal_foaie()

        frame_foaie = Frame(radacina, bg="black")
        frame_foaie.pack(pady=10)

        Button(
            frame_foaie,
            text="Rezolvă puzzle",
            font=("Lucida Handwriting", 19),
            bg="#8B0000",  # Roșu închis, o culoare care sugerează pericol sau groază
            fg="white",  # Text alb pentru contrast
            activebackground="#A52A2A",  # Roșu-maro pentru un efect de alarmă când butonul este apăsat
            activeforeground="black",  # Text negru
            command=puzzle_ceasuri
        ).pack(side="left", padx=10)

        Button(
            frame_foaie,
            text="Caută în continuare",
            font=("Lucida Handwriting", 19),
            bg="#A9A9A9",  # Gri deschis pentru un ton de întuneric, dar nu la fel de sumbru ca negrul total
            fg="black",  # Text negru pentru un contrast puternic
            activebackground="#8B0000",  # Roșu închis pentru o reacție de alertă
            activeforeground="white",  # Text alb pentru contrast când este apăsat
            command=cealalta_camera
        ).pack(side="left", padx=10)


def cealalta_camera():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    label_usa_intredeschisa = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_usa_intredeschisa.pack(pady=10)
    text_usa_intredeschisa = ("Te decizi să verifici și cealalta cameră și pășești în ea,\n"
                              " ghidat de lumina palidă a lumânării din mâna ta. \n"
                              "Flacăra tremură, aruncând umbre bizare pe pereții reci și goi. Aerul e greu,\n"
                              " încărcat de o tensiune nevăzută. Privirea îți este atrasă de un perete pe care\n"
                              " stau așezate mai multe tablouri, toate într-un mod ciudat, aproape nefiresc. \n"
                              "Simți un fior rece trecându-ți pe șira spinării, iar parcă din depărtare auzi un\n"
                              "murmur slab, dar nu poți înțelege ce spune.")
    afisare_treptata(label_usa_intredeschisa, text_usa_intredeschisa, interval=50, callback=vezi_tablouri)


def vezi_tablouri():
    buton_vezi_tablouri = Button(
        radacina,
        text="Vezi tablourile",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=imagine_tablouri
    )
    buton_vezi_tablouri.pack(pady=20)


def imagine_tablouri():
    for widget in radacina.winfo_children():
        widget.destroy()
    fundal_tablouri()

    Button(
        radacina,
        text="Continuă",
        font=("Lucida Handwriting", 19),
        bg="#4B0082",  # Violet închis pentru un efect misterios și sumbru
        fg="white",  # Text alb pentru contrast puternic
        activebackground="#800080",  # Violet mai intens când este apăsat, pentru a adânci senzația de tensiune
        activeforeground="#FFFF00",  # Text galben când este apăsat, pentru un efect de alertă
        command=observi_peretele
    ).pack(side="top", pady=20)

def observi_peretele():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    label_observi_peretele = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_observi_peretele.pack(pady=10)
    text_observi_peretele = ("Privești în jur și observi că toate tablourile sunt picturi celebre ale lui Da Vinci,\n"
                             " dar fiecare pare să indice spre o oglindă spartă. Curios, te apropii și descoperi că, \n"
                             "prin cioburile ei, se reflectă un mesaj scris pe peretele din spatele tău.\n"
                             " Rapid, îți amintești că Da Vinci avea obiceiul de a scrie invers, așa că iei\n"
                             " un ciob de oglindă și începi să descifrezi cuvintele misterioase de pe perete.")
    afisare_treptata(label_observi_peretele, text_observi_peretele, interval=50, callback=vezi_scrisul2)

def vezi_scrisul2():
    buton_vezi_scrisul2 = Button(
        radacina,
        text="Întoarce-te",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=mesaj_davinci2()
    )
    buton_vezi_scrisul2.pack(pady=20)

def mesaj_davinci2():
    for widget in radacina.winfo_children():
        widget.destroy()
    fundal_davinci()

    label_davinci2 = Label(
        radacina,
        text="",
        font=("Lucida Handwriting", 29),
        pady=10
    )
    label_davinci2.pack(pady=10)
    text_davinci2 = (
        "Umbrele noptii, martore tacute,\n"
        "Au invelit-o-ntr-un vals de intuneric,\n"
        "O stea cazuta-n vant si ploi pierdute, \n"
        "Un suflet frant, un cantec prea himeric.\n"

        "Pe lespedea tacuta, doar un nume \n"
        "Si-un ceas gravat - trei:douazeci si noua \n"
        "Dar amintirea ei arde prin lume, \n"
        "Ca un suspin pierdut in vai de roua")
    afisare_treptata(label_davinci2, text_davinci2, interval=50, callback=ultima_alegere2)

def ultima_alegere2():
    buton_final2 = Button(
        radacina,
        text="Sunt gata să răspund la puzzle",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=puzzle_ceasuri
    )
    buton_final2.pack(pady=20)






def scena_usa_deschisa():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    label_usa_intredeschisa = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_usa_intredeschisa.pack(pady=10)
    text_usa_intredeschisa = ("Pășești în camera întunecată, ghidat de lumina palidă a lumânării din mâna ta. \n"
                              "Flacăra tremură, aruncând umbre bizare pe pereții reci și goi. Aerul e greu,\n"
                              " încărcat de o tensiune nevăzută. Privirea îți este atrasă de un perete pe care\n"
                              " stau așezate mai multe tablouri, toate într-un mod ciudat, aproape nefiresc. \n"
                              "Simți un fior rece trecându-ți pe șira spinării, iar parcă din depărtare auzi un\n"
                              "murmur slab, dar nu poți înțelege ce spune.")
    afisare_treptata(label_usa_intredeschisa, text_usa_intredeschisa, interval=50, callback=vezi_tablouri)
def vezi_tablouri():
        buton_vezi_tablouri = Button(
            radacina,
            text="Vezi tablourile",
            font=("Lucida Handwriting", 19),
            bg="#333333",  # Gri închis pentru un fundal sumbru
            fg="white",  # Text alb pentru contrast
            activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
            activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
            command=imagine_tablouri
        )
        buton_vezi_tablouri.pack(pady=20)

def imagine_tablouri():
    for widget in radacina.winfo_children():
        widget.destroy()
    fundal_tablouri()

    Button(
        radacina,
        text="Continuă",
        font=("Lucida Handwriting", 19),
        bg="#333333",
        fg="white",  # Text alb pentru contrast puternic
        activebackground="#800080",  # Violet mai intens când este apăsat, pentru a adânci senzația de tensiune
        activeforeground="#FFFF00",  # Text galben când este apăsat, pentru un efect de alertă
        command=observi_peretele
    ).pack(side="top", pady=20)

def observi_peretele():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    label_observi_peretele = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_observi_peretele.pack(pady=10)
    text_observi_peretele = ("Privind atent la tablouri, începi să te întrebi dacă felul în care sunt aranjate\n"
                             " ascunde un mesaj. Într-un moment de luciditate, oglinda din fața ta îți atrage atenția.\n"
                             " În reflexia ei, pe peretele din spatele tău, se întrezărește un mesaj misterios.\n"
                             " Te întorci încet, dorind să descoperi ce scrie.")
    afisare_treptata(label_observi_peretele, text_observi_peretele, interval=50, callback=vezi_scrisul)

def vezi_scrisul():
    buton_vezi_scrisul = Button(
        radacina,
        text="Întoarce-te",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=scris_perete
    )
    buton_vezi_scrisul.pack(pady=20)

def scris_perete():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal_scrisp()
    Button(
        radacina,
        text="Continuă",
        font=("Lucida Handwriting", 19),
        bg="#333333",
        fg="white",  # Text alb pentru contrast puternic
        activebackground="#800080",  # Violet mai intens când este apăsat, pentru a adânci senzația de tensiune
        activeforeground="#FFFF00",  # Text galben când este apăsat, pentru un efect de alertă
        command=nerealizare
    ).pack(side="top", pady=20)

def nerealizare():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    label_nerealizare = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_nerealizare.pack(pady=10)
    text_nerealizare = ("Te apropii de perete, încercând să descifrezi mesajul. Literele îți provoacă,\n"
                             " amestecate într-un mod care îți scapă. Îți încordezi privirea, dar cu cât te \n"
                             "concentrezi mai mult, cu atât mesajul devine mai enigmatic. Timpul trece,\n"
                             " iar o senzație de nerăbdare începe să te cuprindă. În mintea ta se strecoară un gând:\n"
                             " nu-ți poți permite să rămâi blocat aici. Cu o ultimă privire spre perete,\n"
                             " decizi să mergi în cealaltă cameră. Ceva îți spune că răspunsurile s-ar putea\n"
                             " ascunde acolo – iar fiecare secundă contează.")
    afisare_treptata(label_nerealizare, text_nerealizare, interval=50, callback=pleci)

def pleci():
    buton_pleci = Button(
        radacina,
        text="Du-te în cealaltă cameră",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=intrare
    )
    buton_pleci.pack(pady=20)

def intrare():
    for widget in radacina.winfo_children():
        widget.destroy()
    fundal_camera_inchisa()
    label_intrare = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_intrare.pack(pady=10)
    text_intrare = ("Ușa scârțâie în timp ce o deschizi încet, sunetul făcându-ți inima să bată mai tare. \n"
                    "Înăuntru, ochii îți cad imediat pe o statuie care te face să tresari—pentru o clipă,\n"
                    " ai crezut că e un spirit. Pe pereți, ceasuri cu bufnițe stau înșirate, toate arătând\n"
                    " ore diferite. Nu înțelegi legătura, dar simți că e ceva important. Privirea ți se oprește\n"
                    " în spatele statuii, unde zărești o bucată de hârtie. O iei cu mâinile tremurânde,\n"
                    " întunericul din cameră părând să se apropie de tine...")
    afisare_treptata(label_intrare, text_intrare, interval=50, callback=buton_citeste)

def buton_citeste():
    buton_pleci = Button(
        radacina,
        text="Citește",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=foaie
    )
    buton_pleci.pack(pady=20)

def foaie():
    for widget in radacina.winfo_children():
        widget.destroy()
    fundal_foaie()

    frame_foaie = Frame(radacina, bg="black")
    frame_foaie.pack(pady=10)

    Button(
        frame_foaie,
        text="Rezolvă puzzle",
        font=("Lucida Handwriting", 19),
        bg="#8B0000",  # Roșu închis, o culoare care sugerează pericol sau groază
        fg="white",  # Text alb pentru contrast
        activebackground="#A52A2A",  # Roșu-maro pentru un efect de alarmă când butonul este apăsat
        activeforeground="black",  # Text negru
        command=puzzle_ceasuri
    ).pack(side="left", padx=10)

    Button(
        frame_foaie,
        text="Caută în continuare",
        font=("Lucida Handwriting", 19),
        bg="#A9A9A9",  # Gri deschis pentru un ton de întuneric, dar nu la fel de sumbru ca negrul total
        fg="black",  # Text negru pentru un contrast puternic
        activebackground="#8B0000",  # Roșu închis pentru o reacție de alertă
        activeforeground="white",  # Text alb pentru contrast când este apăsat
        command=sunet_spartura
    ).pack(side="left", padx=10)

def puzzle_ceasuri():
    # Elimină toate widget-urile existente
    for widget in radacina.winfo_children():
        widget.destroy()

    # Apelează funcția pentru fundalul specific
    fundal_puzzle_ceasuri()

    # Text explicativ al puzzle-ului
    label_puzzle = Label(
        radacina,
        text="Ceasurile de pe pereți îți șoptesc o enigmă. Găsește ora corectă pentru a avansa.\n"
             "Introdu ora în format exact (exemplu: 3:29).",
        font=("Chiller", 24),
        bg="black",
        fg="white",
        wraplength=600,
        justify="center",
        pady=20
    )
    label_puzzle.pack(pady=10)

    # Câmp de intrare pentru răspuns
    intrare_raspuns = Entry(
        radacina,
        font=("Lucida Handwriting", 20),
        bg="#333333",  # Gri închis pentru un ton misterios
        fg="white",  # Text alb pentru vizibilitate
        justify="center",
        width=10
    )
    intrare_raspuns.pack(pady=10)

    # Mesaj pentru erori
    mesaj_eroare = Label(
        radacina,
        text="",
        font=("Chiller", 20),
        bg="black",
        fg="red",
        pady=10
    )
    mesaj_eroare.pack()

    # Funcție pentru verificarea răspunsului
    def verifica_raspuns():
        if intrare_raspuns.get().strip() == "3:29":
            scena_urmatoare()  # Treci la următoarea scenă
        else:
            mesaj_eroare.config(text="Răspuns greșit! Pereții par să se apropie de tine...")

    # Buton pentru a verifica răspunsul
    buton_verifica = Button(
        radacina,
        text="Verifică",
        font=("Lucida Handwriting", 19),
        bg="#8B0000",  # Roșu închis pentru atmosferă sumbră
        fg="white",  # Text alb
        activebackground="#A52A2A",  # Roșu-maro la apăsare
        activeforeground="black",  # Text negru la apăsare
        command=verifica_raspuns
    )
    buton_verifica.pack(pady=20)

def scena_urmatoare():
    for widget in radacina.winfo_children():
         widget.destroy()
    seteaza_fundal()

    label_scena_urmatoare = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_scena_urmatoare.pack(pady=10)
    text_scena_urmatoare = ("Cu o mișcare lentă și înfricoșătoare, gura statuii se deschide treptat, dezvăluind o cheie\n"
                        " ruginită, ca o relicvă uitată. O iei cu tine, simțind cum aerul devine tot mai greu,\n"
                        " iar inima îți bate cu putere. Fără să te mai gândești, fugi cu pași repezi \n"
                        "spre ușa blocată de la capătul holului")
    afisare_treptata(label_scena_urmatoare, text_scena_urmatoare, interval=50, callback=buton_iacheia)


def buton_iacheia():
    buton_iacheia = Button(
        radacina,
        text="Ia cheia",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=ultima_scena1
    )
    buton_iacheia.pack(pady=20)

def ultima_scena1():
    for widget in radacina.winfo_children():
        widget.destroy()

    radacina.config(bg="black")  # Schimbă fundalul principal în negru

    # Creează un label care conține textul final
    label_final = Label(
        radacina,
        text="",
        font=("Chiller", 50),  # Text mare pentru efectul dorit
        bg="black",  # Fundalul rămâne negru
        fg="white",  # Text alb pentru contrast
        pady=200  # Plasează textul în mijlocul ecranului
    )
    label_final.pack(pady=10)
    text_final="VA CONTINUA..."
    afisare_treptata(label_final, text_final, interval=50)

def sunet_spartura():
    for widget in radacina.winfo_children():
        widget.destroy()
    fundal_scirsp2()

    label_sunet_spartura = Label(
        radacina,
        text="",
        font=("Chiller", 29),
        pady=10
    )
    label_sunet_spartura.pack(pady=10)
    text_sunet_spartura = ("Un zgomot puternic sparge liniștea, iar inima îți sare din piept. Te duci\n"
                           " în cealaltă cameră tremurând ca să verifici și vezi oglinda spartă. \n"
                           "Gândurile îți zboară la Da Vinci, care obișnuia să scrie mesaje care puteau \n"
                           "fi citite doar în oglindă. Iei o bucată de sticlă, iar mâinile îți tremură.\n"
                           " O așezi spre perete și, din reflecție, începe să apară un text criptic. \n"
                           "Adevărul te privește din adâncul umbrei.")
    afisare_treptata(label_sunet_spartura, text_sunet_spartura, interval=50, callback=buton_verifica)


def buton_verifica():
    buton_verifica = Button(
        radacina,
        text="Întoarce-te",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=mesaj_davinci
    )
    buton_verifica.pack(pady=20)

def mesaj_davinci():
    for widget in radacina.winfo_children():
        widget.destroy()
    fundal_davinci()

    label_davinci = Label(
        radacina,
        text="",
        font=("Lucida Handwriting", 29),
        pady=10
    )
    label_davinci.pack(pady=10)
    text_davinci = (
        "Umbrele noptii, martore tacute,\n"
        "Au invelit-o-ntr-un vals de intuneric,\n"
        "O stea cazuta-n vant si ploi pierdute, \n"
        "Un suflet frant, un cantec prea himeric.\n"

        "Pe lespedea tacuta, doar un nume \n"
        "Si-un ceas gravat - trei:douazeci si noua \n"
        "Dar amintirea ei arde prin lume, \n"
        "Ca un suspin pierdut in vai de roua")
    afisare_treptata(label_davinci, text_davinci, interval=50, callback=ultima_alegere)

def ultima_alegere():
    buton_final = Button(
        radacina,
        text="Sunt gata să răspund la puzzle",
        font=("Lucida Handwriting", 19),
        bg="#333333",  # Gri închis pentru un fundal sumbru
        fg="white",  # Text alb pentru contrast
        activebackground="#444444",  # Fundal mai deschis când butonul este apăsat
        activeforeground="#ff0000",  # Culoare roșie pentru text când este apăsat
        command=puzzle_ceasuri
    )
    buton_final.pack(pady=20)


# Crearea ferestrei principale
radacina = Tk()
radacina.title("Escape Room")
radacina.geometry("1700x1100")
radacina.option_add("*Label.background", "black")
radacina.option_add("*Label.foreground", "white")
seteaza_fundal()
meniu_principal()

# Redarea sunetului de fundal din momentul în care aplicația pornește
reda_sunet_fundal()

radacina.mainloop()