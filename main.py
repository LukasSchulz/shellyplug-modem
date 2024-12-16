import socket
import ShellyPy
import time
REMOTE_SERVER = "one.one.one.one"
def is_connected(hostname):
  try:
    # See if we can resolve the host name - tells us if there is
    # A DNS listening
    host = socket.gethostbyname(hostname)
    # Connect to the host - tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except Exception:
     pass # We ignore any errors, returning False
  return False

shelly_modem = ShellyPy.Shelly("192.168.178.96")

if __name__ == "__main__":
  while True:
    if not is_connected(REMOTE_SERVER):
       shelly_modem.relay(0, turn=False)
       time.sleep(5)
       shelly_modem.relay(0, turn=True)
       print("Internetverbindung verloren, Modem neugestartet")
    print("Warte 120s vor nächstem Internet-Check")
    time.sleep(120)
