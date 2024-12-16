# shellyplug-modem

Wir haben im [MHDS](hausderschueler.de) immer wieder Internetprobleme, die sich am einfachsten dadurch beheben lassen, das Modem neuzustarten.
Wir haben schon mehrfach mit dem Internetanbieter telefoniert, scheinbar ist das Fritzbox-Update nicht mit unserer Modem-Fritzbox-Kombination kompatibel, obwohl der MNET-techniker das selbst so installiert hat. 🤷‍♂️

Ich habe den Netzstecker vom Modem einfach in einen Shellyplug gesteckt, das Skript testet alle 2min (Verzögerung, damit nicht das Modem gerade noch neustartet während die Verbindung gestestet wird) die Internetverbindung zu Cloudflare (weil ich davon ausgehe, dass die online sind) - und startet bei fehlen der Verbindung einfach das Modem neu, indem die Stromversorgung für 5s unterbrochen wird.

Das Skript läuft auf einem RaspberryPi vor Ort, weil der sowieso schon da läuft.

## Installation
Das Projekt verwendet python `virtualenv`
Mit 
```
python -m virtualenv .venv
```
kann die neue Umgebung erstellt werden, mit 
```
source .venv/bin/activate
```
kann diese dann gesourced werden.

Die verwendeten Pakete können einfach per 
```
pip install -r requirements.txt
```
installiert werden.

Der service `shellyplug_modem.service` muss in `/etc/system/systemd/` kopiert (und er start-Pfad angepasst) werden und kann dann per 
```
sudo systemctl enable --now shellyplug_modem
```
aktiviert und gestartet werden.

Mit 
```
sudo systemctl start|stop|restart|status shellyplug_modem
``` 
kann derStatus eingesehen und der Dienst gestoppt/(neu)gestartet werden.