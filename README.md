
Reverse Shell Tool
📖 Opis
To repozytorium zawiera przykład implementacji narzędzia typu reverse shell, stworzonego w celach edukacyjnych oraz do przeprowadzania legalnych testów penetracyjnych. Reverse shell pozwala na zdalne zarządzanie komputerem poprzez połączenie inicjowane przez system docelowy.

🎯 Cel projektu
Edukacja w zakresie bezpieczeństwa IT.
Zrozumienie, jak działają narzędzia używane w testach penetracyjnych.
Praktyka w tworzeniu prostych narzędzi sieciowych.
🛡️ Ważne ostrzeżenie
To narzędzie powinno być używane wyłącznie:

W kontrolowanych środowiskach testowych.
Za zgodą właściciela systemu, na którym jest używane.
Użycie tego narzędzia do nielegalnych celów może być sprzeczne z prawem i skutkować odpowiedzialnością karną. Autor nie ponosi odpowiedzialności za niewłaściwe użycie tego oprogramowania.

⚙️ Funkcjonalność
Klient: Uruchamiany na systemie docelowym, łączy się z serwerem i wykonuje przesyłane komendy.
Serwer: Nasłuchuje połączeń od klienta, wysyła polecenia i odbiera odpowiedzi.
📋 Wymagania
Python 3.x
System operacyjny: Windows/Linux/MacOS
Uprawnienia sieciowe umożliwiające połączenie między klientem a serwerem.

🚀 Jak uruchomić

1. Uruchom serwer
Na komputerze testowym (Twoim):
Skopiuj kod
python3 server.py


2. Uruchom klienta
Na systemie docelowym:
Skopiuj kod
python3 client.py


📝 Przykład użycia
Serwer nasłuchuje na porcie 4444.
Klient łączy się z serwerem, otwierając powłokę umożliwiającą przesyłanie komend.
Wpisz komendę w serwerze (np. ls lub whoami), a odpowiedź zostanie przesłana z klienta.
🛠️ Zastosowanie
Testy penetracyjne: Sprawdzenie, czy system docelowy ma odpowiednie zabezpieczenia.
Edukacja: Nauka o technikach i metodach stosowanych w testach bezpieczeństwa.
📚 Materiały dodatkowe
OWASP Testing Guide
Hack The Box
TryHackMe
⚠️ Zastrzeżenia
Używaj tego narzędzia zgodnie z prawem.
Kod został stworzony wyłącznie w celach edukacyjnych.
Sprawdź przepisy obowiązujące w Twoim kraju dotyczące testów penetracyjnych.
