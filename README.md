Datenbankstrukturen unterliegen in modernen Softwareprojekten einem kontinuierlichen Wandel. 
Ohne adäquate Migrationswerkzeuge kommt es bei Schemaevolutionen rapide zu inkonsistenten Datenbankzuständen und zunehmendem Fehlerrisiko.
Diese Arbeit untersucht den Einsatz von Alembic als Migrationswerkzeug für SQLAlchemy-basierte Projekte. 
Mithilfe einer praktischen Mini-Migration wurde eine neue Spalte in ein bestehendes Datenmodell integriert, ohne vorhandene Datensätze zu verlieren.
Die Durchführung erfolgte in einer realistischen Entwicklungsumgebung bestehend aus einer dev- und prod-VM, mittels des Oracle VirtualBox Managers. 
Die Ergebnisse zeigen, dass mit Alembic eine reproduzierbare und nachvollziehbare Schemaevolution möglich ist. 
Abschließend werden in dieser Arbeit Limitationen der gewählten Migrationsstrategie sowie weiterführende Ansätze diskutiert.
