from cal_ui import *

"""
Övning 801 Ladda in almanackan och testa de användarfunktioner som finns beskrivna i listan nedan. Prova att skapa ett par almanackor, boka möten i dem och visa vilka möten som finns bokade en viss dag. Spara gärna undan koden som skapar kalendern i en Pythonfil och kör den därifrån, istället för att köra direkt från terminalen. Då kan du använda detta till framtida tester när du börjar ändra i almanackans kod! (Om du bara sparar resultatet, med save(), kan detta inte användas till att testa funktionerna för att skapa almanackan... så spara kod med själva anropen till create, book med mera.)
"""


create('Armen Asratian')

book('Armen Asratian', 23, 'nov', '01:00', '02:00', "Lick Noahs asshole")
book('Armen Asratian', 23, 'nov', '02:00', '03:00', "Fuck Kevin in the ass")
book('Armen Asratian', 23, 'nov', '03:00', '06:00', "Dildo in my ass in student huset")
book('Armen Asratian', 23, 'nov', '06:00', '23:59', "Piss in Noahs ear")

remove('Armen Asratian',23,'nov','06:00')

show('Armen Asratian',23, 'nov')
