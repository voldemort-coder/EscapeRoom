try:
    numar = int(input("Introduceti numărul pentru care vrei să găsești multiplii: "))

    if numar == 0:
        print("Eroare: Numărul nu poate fi 0!")
    elif numar < 0:
        print("Eroare: Numărul nu poate fi negativ!")
    else:
        inceput = int(input("Introduceti începutul intervalului: "))
        sfarsit = int(input("Introduceti sfârșitul intervalului: "))

        if inceput > sfarsit:
            print("Eroare: Intervalul nu este valid. Începutul trebuie să fie mai mic decât sfârșitul.")
        else:
            print(f"Multiplii lui {numar} în intervalul [{inceput}, {sfarsit}] sunt:")
            for i in range(inceput, sfarsit + 1):
                if i % numar == 0:
                    print(i)
except ValueError:
    print("Eroare: Te rog introduceti un numar valid!")


#sfarsit + 1 este folosit pentru a include și sfarsit în interval pt ca range() exclude întotdeauna valoarea finală
# De aceea, pentru a include sfarsitul în interval, folosesc sfarsit + 1