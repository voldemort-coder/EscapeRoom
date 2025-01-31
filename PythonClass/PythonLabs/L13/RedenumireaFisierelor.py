import os


def rename_file():
    # Obține directorul unde rulează scriptul
    current_directory = os.getcwd()

    # Afișează lista fișierelor din folder
    files = [f for f in os.listdir(current_directory) if os.path.isfile(f)]

    if not files:
        print("❌ Nu există fișiere în acest folder.")
        return

    print("\n📂 Fișiere disponibile:")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")

    # Utilizatorul alege un fișier după număr
    try:
        choice = int(input("\n🔢 Introdu numărul fișierului pe care vrei să-l redenumești: "))
        if choice < 1 or choice > len(files):
            print("❌ Selecție invalidă. Încearcă din nou.")
            return
    except ValueError:
        print("❌ Te rog să introduci un număr valid.")
        return

    old_name = files[choice - 1]

    # Utilizatorul introduce un nou nume pentru fișier
    new_name = input("✍️ Introdu noul nume al fișierului (fără extensie): ").strip()

    if not new_name:
        print("❌ Numele fișierului nu poate fi gol.")
        return

    # Obține extensia fișierului original
    file_extension = os.path.splitext(old_name)[1]

    # Creează noul nume cu prefixul 'renamed_'
    final_name = f"renamed_{new_name}{file_extension}"

    # Redenumire fișier
    os.rename(old_name, final_name)
    print(f"✅ Fișierul a fost redenumit: {old_name} ➝ {final_name}")


# Rulează funcția
rename_file()
