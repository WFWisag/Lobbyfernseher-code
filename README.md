# Code für die Diashow für den Lobbyfernseher

Der Fernseher in der Lobby des HQ's der WISAG Berlin ist lange Zeit nicht in den Betrieb gegangen. Doch nun existiert der Code für den Raspberry Pi 3B+, der den
Fernseher zum Leben erwecken soll! Das hier ist die Dokumentation für den.

*Das Programm wird noch weiterentwickelt, siehe Issues und PR's.*

## Dokumentation

![image](https://user-images.githubusercontent.com/85707089/219309295-f1b80e21-d3e8-4013-8365-df57300f6a02.png)

(Grobe Übersicht, wie die einzelnen Skripte untereinander kommunizieren)

- Grün: Haupt-Skripte
- Blau: Module für Skripte
- Gelb: andere externe Dateien / Ordner

**Am Besten ist es, wenn man das Programm auf einem Raspberry Pi laufen lässt und autostart.py in den Autostart integriert.** Sonst muss man alles manuell starten usw.

## Hinweise zur Anwendung

|Datei|Hinweis|
|:---:|:-----:|
|autostart.py| Zeile 14 ersetzen durch: ``os.system("chromium-browser --kiosk index.html")`` , wenn auf Raspi verwendet|
