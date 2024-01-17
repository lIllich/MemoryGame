from classes.HomeWindow import HomeWindow
from classes.ConfigManager import ConfigManager

#!// bug - kada se close-a GameWindow u sred igre, javi exception
#!// bug - extended display, ako se window prikaze izvan dozovljenih granica (displaya) -> vrati ga
#!// bug - kada se na kartici koja je pronađena (zelena) mouse pointer zadrži dulje od 1sek i potom makne, u buttonu text posetane ''
#!// bug - pomicanje grida kako se slike otvaraju

#todo//: dodati razine - easy, normal, hard, extra hard? (settings)
#todo//: dodati varijablnog intervala za označavanje card (settings)
#todo//: dodati spremanje scora po razinama, u json se spremaju 10 najbojih po razini
#todo: manager za dodavanje kategorija/kartica - text&text, text&slika, slika&slika
#todo: custom - kategorije i kartice se spremaju u json (text - id, value; slika - id, url), slika se sprema u neki subfolder
#todo: manager za konvertiranje slika u ogovarajuci format
#todo//: starter - poseban json sa gotovim(predinstaliranim) kategorijama, npr. slova, brojevi, neke slike...
# todo// : velika slova
#!// todo: dodati jos jednu kategoriju - svakodnevica
#! todo: full screen, grid na sredini
#!// todo: homewindow - biranje kategorije

#! bug: oznacavanje kartica

def main():
    config_file = "config.json"

    cm = ConfigManager(config_file)
    cm.load_configs()

    while True:
        hw = HomeWindow(cm)
        again = hw.show()
        if again == 0:
            break


if __name__ == "__main__":
    main()