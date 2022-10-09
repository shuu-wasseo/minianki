![](https://progress-bar.dev/90/?title=alpha%20release)

# minianki

emulates an anki session in the terminal.

## installation instructions
firstly, clone this repository.

```
$ git clone https://github.com/shuu-wasseo/minianki
```
secondly, add the minianki directory into your PATH. 
```
export PATH=/home/uname/minianki:$PATH
```
thirdly, make the mnak file executable. for example, if you added minianki into your home directory:
```
$ chmod +x /home/uname/minianki/mnak
```
now, you are able to use minianki! enter "mnak" in your terminal to begin!

## commands
importing/exporting:
- import: import cards in import.txt to the main database.
- init: synchronise the program with the database to intialise the in-program deck.
- save: save your progress/scheduling and cards to the database.

review/learning sessions:
- learn: an anki-esque learning session.

settings and help:
- settings: customise learning variables.
- guide: see guides.
- help: view this message again.
- exit: end the program.

## directory
### main directory
- [README.md](https://github.com/shuu-wasseo/minianki/blob/main/READNE.md) - the file you are reading now :>
- [import.txt](https://github.com/shuu-wasseo/minianki/blob/main/import.txt) - file for importing new cards.
- [main.py](https://github.com/shuu-wasseo/minianki/blob/main/main.py) - main user interface.
- [minianki.py](https://github.com/shuu-wasseo/minianki/blob/main/minianki.py) - package file, contains all functions for main.py

### subdirectories
- [.userdata](https://github.com/shuu-wasseo/minianki/tree/main/.userdata) - exportable data.
  - [csv.mnak](https://github.com/shuu-wasseo/minianki/blob/main/.userdata/csv.mnak) - all cards with scheduling.
  - [learnvars.csv](https://github.com/shuu-wasseo/minianki/blob/main/.userdata/learnvars.csv) - all customised learning variables.
  - [txt.mnak](https://github.com/shuu-wasseo/minianki/blob/main/.userdata/txt.mnak) - all cards without scheduling.

- [.guides](https://github.com/shuu-wasseo/minianki/tree/main/export) - guides.
  - [faq.txt](https://github.com/shuu-wasseo/minianki/blob/main/guides/faq.txt)
  - [imexportguide.txt](https://github.com/shuu-wasseo/minianki/blob/main/guides/imexportguide.txt) - exporting instructions.

## guides
the following can also be found in [`./guides/`](https://github.com/shuu-wasseo/minianki/tree/main/export).

### import/export 
*(also found in [.guides/imexportguide.txt](https://github.com/shuu-wasseo/minianki/blob/main/.guides/imexportguide.txt))*

**IMPORTING NEW CARDS:**

either:
- paste text into import.txt in a terms-definitions format
- or replace import.txt with a .txt file in that format.

minianki will:
- import your files into the database with the "import" command and prompt you for a delimiter (4-space tab by default)
- refresh the deck with the "init" command. 
do remember to do both "import" and "init" everytime new cards are added into import.txt.

**IMPORTING/EXPORTING USER DATA:**

simply paste another .userdata subdirectory from your old minianki setup into the main minianki directory of your new minianki setup. 
the .userdata subdirectory contains data such as cards (with or without scheduling) and learning variables (preferences).

### faq
*(also found in [.guides/faq.txt](https://github.com/shuu-wasseo/minianki/blob/main/.guides/faq.txt))*

**how does the algorithm work in minianki?**

the minianki algorithm is similar to anki's algorithm without the use of leeches, timers and certain other features. for more information, see https://docs.ankiweb.net/deck-options.html.

**can i have subdecks in minianki?**

minianki currently does not support subdecks, but we are currently working to implement these in upcoming versions.

**can i have media in my minianki flashcards?**

while this is a prominent feature of anki, minianki does not currently support media and we are not planning to implement media support anytime soon.
