# Python_OpenAI_API
## Plik zawiera
* opis repozytorium
* wymagania
* narzędzia
* instrukcja uruchomienia
## Opis repozytorium
- Aplikacja napisana w języku Python, komunikująca się z OpenAI API, w celu obróbki podanej treści przez AI. </br>
- Sztuczna inteligencja redaguje tekst tak, aby był gotowy na wklejenie do gotowych (np. ostylowanych) szablonów stron internetowych. </br>
- W aplikacji przekazywany jest odpowiedni prompt opisujący wytyczne obróbki. Odpowiednio wygenerowany plik jest tworzony jako HTML-owy i zapisywany w 
folderze z aplikacją. </br>
- Przykładowy, wygenerowany plik można podejrzeć po otwarciu pliku "artykul.html" w dowolnym edytorze tekstu. </br>
- Po otwarciu pliku "podglad.html" w dowolnej przeglądarce, możemy sprawdzić, jak wygląda strona internetowa po wrzuceniu wygenerowanego tekstu do szablonu strony inernetowej. </br>
- Plik "szablon_podglad.html" to prosta strona, która ukazuje jak będzie wyglądać strona, po wrzuceniu wygenerowanego tekstu HTML.
## Wymagania
* #### klucz do OpenAI API
* Python
* biblioteka "openai"
* biblioteka "requests"
* edytor tekstu np. Visual Studio Code
* przeglądarka internetowa

## Narzędzia 
* OpenAI API
* Python
* HTML
* CSS
* JavaScript
* GIT, GitHub
* Visual Studio Code

## Instrukcja uruchomienia
1. Sklonuj repozytorium do wybranego folderu. Otwórz konsolę i przenieś się do pobranego folderu:
```
cd nazwa folderu
```
2. Dodaj bibliotekę openai:
```
pip install openai==0.27.0
```
3. Dodaj bibliotekę requests:
```
pip install requests
```
4. Otwórz jeden z pobranych plików - main.py za pomocą edytora tekstu i w linii 5 wklej między apostrofami swój klucz dostępu do API.
5. Będąc w tym momencie w konsoli, w pobranym repozytorium uruchom aplikację za pomocą komendy i gratulacje, wygenerowałeś nowy plik "artykul.html", gotowy do implementacji w szablonie HTML!
```
python main.py
```
6. Sprawdzaj pozostałe pliki za pomocą przeglądarki i edytora tekstu :)

