while True:
    try:
        user_input = input("Introduceți o listă de elemente: ").strip()
        filtered_input = ''.join(filter(lambda x: x.isalnum() or x.isspace(), user_input))
        unique_elements = list(set(filtered_input.split()))
        result = ' #'.join(unique_elements)

        print(f"Lista fără duplicate: #{result}")

    except Exception as e:
        print("Eroare:", e)

