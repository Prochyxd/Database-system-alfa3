# Database-system-alfa3
This project will allow user to work with database


pip install mysql-connector-python

**CHECKLIST ZADÁNÍ**

- [x] Vložení, smazání a úpravu nějaké informace, záznamu, který se ukládá do více než jedné tabulky.
- [x] Provést transakci nad více než jednou tabulkou.
- [x] Vygenerovat souhrný report, který bude obsahovat smysluplná agregovaná data z alespoň tří tabulek Vaší databáze. Report musí mít hlavičku a patičku.
- [ ] Import dat do min. dvou tabulek z formátu CSV, XML nebo JSON.
- [ ] Nastavit celý program v konfiguračním souboru.

**CHECKLIST PRO ODEVZDÁNÍ PROJEKTU**
- [x] Dokumentace obsahuje název projektu, jméno autora, jeho kontaktní údaje, datum vypracování, název školy a informaci, že se jedná o školní projekt.
- [ ] Dokumentace obsahuje nebo odkazuje na specifikaci požadavků uživatele na práci s aplikací nebo UML Use Case diagramy, které to popisují.
- [ ] Dokumentace databáze obsahuje popis architektury aplikace pomocí návrhových vzorů nebo UML strukturálních diagramů, například Class diagramy, Deployment diagramy apod.
- [ ] Dokumentace databáze obsahuje popis používání a chodu aplikace pomocí UML behaviorálních diagramů, například State diagramy, Activity diagramy apod.
- [x] Dokumentace obsahuje E-R model databáze, ze kterého jsou patrné názvy tabulek, atributů a jejich datové typy a další konfigurační volby, pokud aplikace databázi používá.
- [ ] Dokumentace obsahuje schéma importovaných a exportovaných souborů, pokud aplikace databázi export a import používá, včetně povinných a nepovinných položek.
- [ ] Dokumentace obsahuje informace o tom, jak se program konfiguruje, jaké konfigurační volby jsou přípustné a co dělají.
- [ ] Dokumentace obsahuje popis instalace a spuštění aplikace, případně odkazuje na soubor README.txt, kde je to popsáno.
- [ ] Dokumentace obsahuje popis všech chybových stavů, které mohou v aplikaci nastat, a případně i kódy chyb a popis postupu jejich řešení.
- [ ] Dokumentace obsahuje výčet knihoven třetích stran, které program využívá.
- [ ] Dokumentace obsahuje závěrečné resumé projektu.
- [ ] Dokumentace je zpracována v jednom souboru s příponou .pdf nebo .md, případně jako HTML stránka se vstupním souborem index.html.

**Export programu a zdrojových kódů**

Pro kontrolu při odevzdání a exportu zdrojových kódů, včetně dalších souborů potřebných pro běh programu, použijte níže uvedený seznam. Především dbájte na dobře pojmenovaní složek a souborů.

- [ ] Export zdrojových kódů obsahuje rozumnou strukturu složek a modulů (src pro kód, test pro unit testy, doc pro dokumentaci, bin pro spustitelné soubory a skripty, apod.)
- [ ] Export zdrojových kódů obsahuje řádné komentáře a/nebo dobře čitelný zdrojový kód s vhodně pojmenovanými třídami, proměnnými apod.
- [ ] Export zdrojových kódů obsahuje soubor README.txt, ve kterém je uvedeno jméno projektu, autor a je popsáno, jak program instalovat a spustit.
- [ ] Export zdrojových kódů obsahuje konfigurační a další soubory potřebné ke spuštění.
- [ ] Export zdrojových kódů aplikace je uložen do jednoho archivu s příponou: .zip

**Export databáze**

V případě, že váš projekt potřebuje ke spuštění vlastní relační databázi, je třeba ji exportovat tak, aby splňovala pravidla níže. Postup instalace/importu databáze doporučujeme popsat v souboru README.txt

- [x] Export databáze obsahuje DDL příkazy pro vytvoření databázového schématu/modelu.
- [x] Export databáze obsahuje DML příkazy pro vložení testovacích záznamů/dat.
- [x] Export databáze je uzavřen v transakci.
- [x] Export databáze obsahuje komentář se jménem projektu, autorem a jeho kontaktními údaji.
- [x] Export databáze je ve formátu SQL v jednom textovém souboru s příponou: .sql