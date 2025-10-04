studenten = [('Isa', 8.4),
             ('Tess', 5.7),
             ('Pieter', 6.3),
             ('Bob', 9.1),
             ('Quinn', 7.8),
             ('Olivia', 4.2),
             ('Liam', 6.9),
             ('Alice', 8.6),
             ('Sam', 7.0),
             ('Eva', 5.1)]

lijst_met_cijfers = []
lijst_met_studenten = []
herstarten = True

lijn = "==============================================================================================================="
## om een tijdelijke lijst met alleen toets-cijfers aan te maken
for naam, cijfer in studenten:
    lijst_met_cijfers.append(cijfer)

## om een tijdelijke lijst met alleen studenten aan te maken
for naam, cijfer in studenten:
    lijst_met_studenten.append(naam)

while herstarten:
    keuze_menu = int(input("Welkom bij de applicatie studenten en hun cijfers! "
                           "\nWat wil je doen? "
                           "\n1: Ik wil graag alle studenten met hun bijbehorende cijfer zien "
                           "\n2: Ik wil weten welke student het hoogste cijfer heeft behaald "
                           "\n3: Ik wil zoeken naar een specifieke student "
                           "\n4: Ik wil een nieuwe student + cijfer toevoegen "
                           "\n5: Ik wil het gemiddelde cijfer weten "
                           "\n6: Ik wil mijn lijst met cijfers sorteren" 
                           "\n7: Ik wil de applicatie afsluiten"))

    while keuze_menu == 1:
        ## Alle studenten met hun cijfers displayen
        print(lijn)
        for naam, cijfer in studenten:
            print(f'Student {naam} heeft een {cijfer} behaald op de toets')
            print(lijn)
        nogmaals = int(input("Wil je terugkeren naar het hoofdmenu? "
                                 "\n1: Ja "
                                 "\n2: Nee"))
        if nogmaals == 1:
            break
        elif nogmaals == 2:
            keuze_menu = 7
            break

    while keuze_menu == 2:
        ## vind het hoogste cijfer in de lijst
        hoogste_cijfer = max(lijst_met_cijfers)

        ## zoek de beste student die bij dat cijfer hoort
        hoogste_cijfer_positie = (lijst_met_cijfers.index(hoogste_cijfer))
        beste_student = lijst_met_studenten[hoogste_cijfer_positie]
        print(lijn)
        print(f'De top student is {beste_student} met het cijfer {hoogste_cijfer}')
        print(lijn)
        nogmaals = int(input("Wil je terugkeren naar het hoofdmenu? "
                             "\n1: Ja "
                             "\n2: Nee"))
        if nogmaals == 1:
            break
        elif nogmaals == 2:
            keuze_menu = 7
            break

    while keuze_menu == 3:
        ##student zoeken
        zoek_student = str(input("Wat is de naam van de student die je zoekt?: "))
        zoek = zoek_student in lijst_met_studenten
        if zoek_student not in lijst_met_studenten:
            print(lijn)
            print(f"{zoek_student} staat niet in de lijst met studenten")
            print(lijn)
            nogmaals = int(input("Wil je terugkeren naar het hoofdmenu? "
                                 "\n1: Ja "
                                 "\n2: Nee"))
            if nogmaals == 1:
                break
            elif nogmaals == 2:
                keuze_menu = 7
                break

        ##positie van die student zoeken en dan cijfer uitrekenen
        zoek_student_positie = (lijst_met_studenten.index(zoek_student))

        cijfer_gezochte_student = lijst_met_cijfers[zoek_student_positie]
        print(lijn)
        print(f"{zoek_student} heeft een {cijfer_gezochte_student} behaald op de toets")
        print(lijn)
        nogmaals = int(input("Wil je terugkeren naar het hoofdmenu? "
                             "\n1: Ja "
                             "\n2: Nee"))
        if nogmaals == 1:
            break
        elif nogmaals == 2:
            keuze_menu =7
            break

    while keuze_menu == 4:
        ##Extra student toevoegen
        extra_student = input("Wat is de naam van je student?: ")
        lijst_met_studenten.append(extra_student.capitalize())

        ##Extra cijfer toevoegen
        extra_cijfer = float(input(f"Welke cijfer heeft {extra_student.capitalize()} behaald?: "))
        lijst_met_cijfers.append(extra_cijfer)

        ##Bovenstaande opnemen in de lijst met alle studenten
        studenten.append((extra_student.capitalize(), extra_cijfer))
        print(lijn)
        print(f'Je hebt {extra_student.capitalize()} met cijfer {extra_cijfer} opgenomen in de lijst met studenten!')
        print(lijn)
        nogmaals = int(input("Wil je terugkeren naar het hoofdmenu? "
                             "\n1: Ja "
                             "\n2: Nee"))
        if nogmaals == 1:
            break
        elif nogmaals == 2:
            keuze_menu =7
            break
    while keuze_menu == 5:
        ## gemiddelde cijfer resetten
        gemiddelde_cijfer = 0
        ## Gemiddelde cijfer berekenen
        aantal_studenten = len(studenten)
        for naam, cijfer in studenten:
            gemiddelde_cijfer += cijfer
        print(lijn)
        print(f'Het gemiddelde cijfer = {(gemiddelde_cijfer / aantal_studenten).__round__(1)}')
        print(lijn)
        nogmaals = int(input("Wil je terugkeren naar het hoofdmenu? "
                             "\n1: Ja "
                             "\n2: Nee"))
        if nogmaals == 1:
            break
        elif nogmaals == 2:
            keuze_menu =7
            break

    while keuze_menu == 6:
        ## Sorteren op cijfers, klein naar groot
        sorteren = sorted(lijst_met_cijfers)
        ## Sorteren omdraaien, hoog naar laag
        cijfer_hoog_naar_laag = (sorteren[::-1])
        # for cijfers in cijfer_hoog_naar_laag:
        print(lijn)
        print(f'cijfers van hoog naar laag zijn {cijfer_hoog_naar_laag}')
        print(lijn)
        nogmaals = int(input("Wil je terugkeren naar het hoofdmenu? "
                             "\n1: Ja "
                             "\n2: Nee"))
        if nogmaals == 1:
            break
        elif nogmaals == 2:
            keuze_menu =7
            break

    while keuze_menu == 7:
        print(lijn)
        print(f'Je hebt gekozen om de applicatie te sluiten')
        print(lijn)
        herstarten = False
        break

