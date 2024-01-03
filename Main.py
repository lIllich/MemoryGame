from classes.HomeWindow import HomeWindow
from classes.ConfigManager import ConfigManager

#! bug - kada se close-a GameWindow u sred igre, javi exception
#! bug - extended display, ako se window prikaze izvan dozovljenih granica (displaya) -> vrati ga

#todo//: dodati razine - easy, normal, hard, extra hard? (settings)
#todo//: dodati varijablnog intervala za označavanje card (settings)
#todo//: dodati spremanje scora po razinama, u json se spremaju 10 najbojih po razini
#todo: manager za dodavanje kategorija/kartica - text&text, text&slika, slika&slika
#todo: manager za konvertiranje slika u ogovarajuci format
#todo: custom - kategorije i kartice se spremaju u json (text - id, value; slika - id, url), slika se sprema u neki subfolder
#todo//: starter - poseban json sa gotovim(predinstaliranim) kategorijama, npr. slova, brojevi, neke slike...

def main():
    config_file = "config.json"

    cm = ConfigManager(config_file)
    cm.load_configs()

    HomeWindow(cm)


if __name__ == "__main__":
    main()