import time

temps_systeme = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(temps_systeme)

def runChronometre():
    reponse_user = input("Voulez-vous démarrer le chrono ? répondez par oui ou non : ")
    if reponse_user == "oui":
        for counter in range(0, 101):
            print(counter + " seconde(s)")
            time.sleep(1.0)

runChronometre()