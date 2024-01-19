# *Pydle* - terminal based wordle clone written in Python

![Pydle logo](/pydle_logo1.jpg)

*Pydle* is a little Wordle clone, written in Python.

The game was written as a Project for my Introduction to Programming class at University of Gdansk.



### Requirements

1. podział projektu na pliki (2pkt)
2.  własne funkcje + testy 5 pkt (po 1 pkt za funkcję i test do niej)
3. użycie list, krotek, słowników (1,5 pkt)
4. lista  najwyżej punktowanych odbytych gier (wraz z imieniem/nazwą gracza).(1pkt)
5. odczyt i zapis do pliku (1 pkt)
6. algorytm  (np sortowanie) (2 pkt)
7. kompletność rozwiązania (2,5 pkt)
8. akademicki poziom (5 pkt)

### Goals:

- Scoreboard stored in a .txt or .csv file
- unit tests
- corect `wordle` functionality

### Accomplished:

- [ ] Podział na pliki
- [x] ~~Własne funkcje~~
- [ ] testy
- [x] ~~listy~~
- [ ] krotki
- [ ] slowniki
- [ ] scoreboard
- [x] ~~odczyt i **zapis** do pliku~~
- [ ] algorytm
- [ ] kompletnosc

### Code Examples:

Terminal color changing functions (ANSI escape codes):
```py
def green():
    print("\033[32m", end="")

def yellow():
    print("\033[93m", end="")

def clear_screen():
    print("\033[H\033[J", end="")

def reset():
    print("\033[0m", end="")
```

example of usage: ``print(green(), 'Pydle')``

