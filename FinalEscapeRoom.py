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

def seteaza_fundal():
    global fundal_horror_tk
    imagine_fundal = Image.open("fundalhorror.jpg")
    imagine_fundal = imagine_fundal.resize((1600, 1200), Image.Resampling.LANCZOS)
    imagine_fundal_tk = ImageTk.PhotoImage(imagine_fundal)
    label_fundal = Label(radacina, image=imagine_fundal_tk)
    label_fundal.place(x=0, y=0, relwidth=1, relheight=1)
    radacina.fundal_ref = imagine_fundal_tk

# Funcție pentru a începe jocul
def incepe_joc():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()
    reda_sunet_fundal()  # Pornește sunetul de fundal
    introducere()
    afiseaza_imagine_tkinter("cabana.png")
    adauga_butoane_dupa_imagine()

# Funcție pentru a închide jocul
def inchide_joc():
    opreste_sunet_fundal()  # Oprește sunetul de fundal
    radacina.destroy()


def meniu_principal():
    frame_meniu = Frame(radacina, bg="black", pady=20)
    frame_meniu.pack(expand=True)

    label_bine_venit = Label(
        frame_meniu,
        text="Bine ai venit în Escape Room",
        font=("Arial", 27),
        pady=10
    )
    label_bine_venit.pack()

    label_instruc = Label(
        frame_meniu,
        text=("Scopul jocului este să rezolvi puzzle-urile și să reușești să părăsești casa.\n"
              "Ești pregătit să începi?"),
        font=("Arial", 19),
        pady=10
    )
    label_instruc.pack()

    frame_butoane = Frame(frame_meniu, bg="black")
    frame_butoane.pack(pady=10)

    buton_start = Button(
        frame_butoane,
        text="Start",
        font=("Arial", 14),
        width=12,
        command=incepe_joc,
        bg="green",
        fg="white"
    )
    buton_start.grid(row=0, column=0, padx=5)

    buton_exit = Button(
        frame_butoane,
        text="Exit",
        font=("Arial", 14),
        width=12,
        command=inchide_joc,
        bg="red",
        fg="white"
    )
    buton_exit.grid(row=0, column=1, padx=5)

def introducere():
    label_intro = Label(
        radacina,
        text=("Te trezești brusc, cu inima bătând nebunește în piept. Capul îți zvâcnește de durere, \n"
              "iar în jur totul e învăluit de o ceață densă și nefirească.\n"
              " Aerul rece îți pătrunde în plămâni, iar mirosul de pământ ud și mucegai îți invadează nările. \n"
              "Te ridici încet, amețit și nesigur, încercând să-ți recapeți echilibrul. \n"
              "Nu-ți amintești cum ai ajuns aici, dar sentimentul apăsător de a fi urmărit îți dă fiori pe șira spinării..\n"
              "Ești amețit și confuz, iar în fața ta observi o casă mare și impunătoare.\n"
              "Pare singura opțiune... Ce vei face?"),
        font=("Lucida Handwriting", 15),
        pady=10
    )
    label_intro.pack(pady=10)

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

def adauga_butoane_dupa_imagine():
    frame_butoane = Frame(radacina, bg="black")
    frame_butoane.pack(pady=10)

    buton_intra_casa = Button(
        frame_butoane,
        text="Intră în casă",
        font=("Arial", 14),
        bg="blue",
        fg="white",
        command=scena_usa_incuiata
    )
    buton_intra_casa.pack(side="left", padx=5)

    buton_fugi = Button(
        frame_butoane,
        text="Fugi cât te țin picioarele",
        font=("Arial", 14),
        bg="orange",
        fg="black",
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
        font=("Lucida Handwriting", 37),
        pady=20,
        fg="green"
    ).pack(pady=20)
    afiseaza_imagine_tkinter("working.png")


def scena_usa_incuiata():
    pygame.mixer.init()
    sunet_forta_usa = pygame.mixer.Sound("door_forced.mp3")
    sunet_forta_usa.play()

    continua_joc()
    seteaza_fundal()

    Label(
        radacina,
        text=(
            "Odată ce ai pășit în casă, un zgomot asurzitor răsună din spatele tău, ca un tunet ce zguduie pereții \n"
            "vechi și scârțâitori. Inima îți îngheață, iar un val de panică te împinge să alergi spre ușă.\n"
            " Încerci să o deschizi disperat, dar e blocată, de parcă ceva invizibil te-ar ține captiv aici.\n"
            "Respiri greu, iar umbra nesigură a unei lumânări pâlpâie pe peretele din fața ta. Un fior rece\n"
            " îți traversează șira spinării când realizezi... singura cale este să continui să explorezi casa. \n"
            "Însă cu fiecare pas, ai senzația că cineva – sau ceva – te privește din întuneric."
        ),
        font=("Lucida Handwriting", 17),
        pady=20,
        fg="white"
    ).pack(pady=10)

    buton_continua = Button(
        radacina,
        text="Continuă să inspectezi casa",
        font=("Arial", 37),
        bg="grey",
        fg="white",
        command=scena_reguli
    )
    buton_continua.pack(pady=20)

def scena_reguli():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    Label(
        radacina,
        text=(
            "Pentru a evada din casă, trebuie să îți folosești inteligența și să rezolvi puzzle-urile pregătite pentru tine,\n"
            " cât mai rapid. Ai la dispoziție 30 de minute pentru a scăpa, iar timpul începe să se scurgă din momentul în care \n"
            "începi prima probă. Fii atent! Fiecare greșeală te va costa un minut din timpul prețios. Tensiunea crește cu fiecare\n"
            " secundă, iar evadarea depinde doar de tine.\n"
            "Ești pregătit să înfrunți provocarea și să începi jocul?"
        ),
        font=("Lucida Handwriting", 21),
        wraplength=1100,
        pady=20,
        fg="red"
    ).pack()

    Button(
        radacina,
        text="Începe jocul",
        font=("Arial", 14),
        bg="green",
        fg="white",
        command=scena_prima_proba  # Legătură corectă către prima probă
    ).pack(pady=20)

def scena_prima_proba():
    # Curățăm fereastra pentru prima probă
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    # Textul introductiv
    Label(
        radacina,
        text=(
            "Te trezești într-o casă întunecată și înfricoșătoare. Pereții par să șoptească povești de groază, iar lumina\n"
            " abia pătrunde prin ferestrele prăfuite. Totul în jur te face să simți un fior rece pe șira spinării."
            "Privirea îți cade asupra unei foi de hârtie aruncate lângă ușă. Este îngălbenită și pătată, ca și cum ar fi\n"
            " fost acolo de ani de zile. Simți o curiozitate inexplicabilă, dar și o teamă care îți strânge inima.\n"
            "Ce faci? Decizi să ridici hârtia și să o citești? Sau rămâi pe loc, întrebându-te ce se va întâmpla în continuare?"
        ),
        font=("Lucida Handwriting", 16),
        wraplength=1100,
        pady=20,
        fg="white"
    ).pack()

    # Frame pentru butoane
    frame_butoane = Frame(radacina, bg="black")
    frame_butoane.pack(pady=10)

    # Buton pentru "Inspectează foaia"
    Button(
        frame_butoane,
        text="Inspectează foaia",
        font=("Arial", 14),
        bg="blue",
        fg="white",
        command=scena_inspecteaza_foaia
    ).pack(side="left", padx=10)

    # Buton pentru "Ignoră foaia"
    Button(
        frame_butoane,
        text="Ignoră foaia",
        font=("Arial", 14),
        bg="red",
        fg="white",
        command=scena_ignora_foaia
    ).pack(side="left", padx=10)


# Scena pentru "Inspectează foaia"
def scena_inspecteaza_foaia():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    afiseaza_imagine_tkinter("planul_casei.jpg")  # Asigură-te că imaginea există

    Label(
        radacina,
        text=(
            "Observi cum casa este formată din parter, etaj și subsol. "
            "Nu ai curajul necesar pentru a urca la următorul etaj, nici de a coborî la subsol, "
            "așa că te decizi să rămâi la parter. Observi un hol lung și întunecat. "
            "Noroc că pe o măsuță în hol ai zărit o candelă în fața unui tablou și o vei folosi pentru a-ți lumina calea."
        ),
        font=("Lucida Handwriting", 16),
        wraplength=800,
        pady=20,
        fg="white"
    ).pack()

    Button(
        radacina,
        text="Continuă povestea",
        font=("Arial", 14),
        bg="green",
        fg="white",
        command=scena_hol  # Legătura corectă cu scena holului
    ).pack(pady=20)


# Scena pentru "Ignoră foaia"
def scena_ignora_foaia():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    Label(
        radacina,
        text=(
            "După ce citești scrisoarea, frica ta devine realitate. Simți o prezență nevăzută care te urmărește din umbre,\n"
            " iar timpul pare să se scurgă tot mai repede. Respiri greu, dar știi că trebuie să mergi mai departe."
            "Iei cu tine lumânarea pe care ai vazut-o, singura ta sursă de lumină. Cu flacăra tremurândă în mână,\n"
            " faci un pas înainte. Nu te poți opri acum. Cineva – sau ceva – te urmărește."
        ),
        font=("Lucida Handwriting", 16),
        wraplength=1100,
        pady=20,
        fg="white"
    ).pack()

    Button(
        radacina,
        text="Continuă povestea",
        font=("Arial", 14),
        bg="green",
        fg="white",
        command=scena_hol  # Legătura corectă cu scena holului
    ).pack(pady=20)


# Scena holului (continuare comună după alegerea foii)
def scena_hol():
    for widget in radacina.winfo_children():
        widget.destroy()
    seteaza_fundal()

    Label(
        radacina,
        text=(
            "Te uiți în capătul holului și realizezi că acolo se află bucătăria. "
            "Însă până acolo mai sunt două camere: una cu ușa închisă, iar cealaltă are ușa întredeschisă. "
            "Unde dorești să intri prima dată?"
        ),
        font=("Lucida Handwriting", 16),
        wraplength=800,
        pady=20,
        fg="white"
    ).pack()

    frame_butoane = Frame(radacina, bg="black")
    frame_butoane.pack(pady=10)

    Button(
        frame_butoane,
        text="Bucătărie",
        font=("Arial", 14),
        bg="orange",
        fg="white",
        command=scena_bucatarie
    ).pack(side="left", padx=10)

    Button(
        frame_butoane,
        text="Camera cu ușa închisă",
        font=("Arial", 14),
        bg="purple",
        fg="white",
        command=scena_usa_inchisa
    ).pack(side="left", padx=10)

    Button(
        frame_butoane,
        text="Camera cu ușa întredeschisă",
        font=("Arial", 14),
        bg="yellow",
        fg="black",
        command=scena_usa_intredeschisa
    ).pack(side="left", padx=10)


# Placeholder pentru cele trei alegeri din scena holului
def scena_bucatarie():
    print("Se trece la scena bucătărie (de implementat)")

def scena_usa_inchisa():
    print("Se trece la scena cu ușa închisă (de implementat)")

def scena_usa_intredeschisa():
    print("Se trece la scena cu ușa întredeschisă (de implementat)")


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
