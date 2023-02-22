# Code für die Diashow für den Lobbyfernseher

Der Fernseher in der Lobby des HQ's der WISAG Berlin ist lange Zeit nicht in den Betrieb gegangen. Doch nun existiert der Code für den Raspberry Pi 3B+, der den
Fernseher zum Leben erwecken soll! Das hier ist die Dokumentation für den.

*Das Programm wird noch weiterentwickelt, siehe Issues und PR's.*

## Dokumentation

![grafik](https://user-images.githubusercontent.com/85707089/220630879-28f3f874-99d8-4945-89bb-5c22af2b9a1b.png)


(Grobe Übersicht, wie die einzelnen Skripte untereinander kommunizieren)

- Grün: Haupt-Skripte
- Blau: Module für Skripte
- Gelb: andere externe Dateien / Ordner

<hr>

writeInHTML.py:
![grafik](https://user-images.githubusercontent.com/85707089/220661198-d0c880a5-4bbf-454b-8bfc-e9ddf8167f35.png)


## Hinweise zur Anwendung

|Datei|Hinweis|
|:---:|:-----:|
|autostart.py|Zeile 8 ersetzen durch ``os.system("sudo python main.py")``, wenn auf Raspi verwendet|
|autostart.py|Zeile 14 ersetzen durch: ``os.system("chromium-browser --kiosk index.html")`` , wenn auf Raspi verwendet|
|autostart.py|Wenn auf Raspi verwendet, möglichst in den autostart packen für bestes Erlebnis|

