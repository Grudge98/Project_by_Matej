def save_to_file():

    filename = input("Zadej nazev souboru (i s priponou .txt: ")

    text = input("Zadejte text, ktery chcete ulozit: ")

    try:
        with open(filename, "w", encoding = "utf-8") as file:
            file.write(text)
        print(f"Text byl uložen do souboru {filename}")

    except Exception as e:
        print("Nastala chyba")


save_to_file()