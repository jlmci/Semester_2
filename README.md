# Sakai-Aufgabe-2-Beschreibung-im-Use-Case-Template
## UC 1.03 
### Eklärung
Allarm bei zu hoher bzw. zu nierdiger Herzfrequenz wobei auch bei arrythimin allarm geschlagen wird

### Beteiligte Akteure
- Diganostiker
- Sportler
- Trainier

### Status
- Aufzeichnungen noch nciht gestartet

### Vorbedingung
- Test muss zuvor gestartet angelegt und gestartet haben (UC 1.01; UC 1.02)
- Angschlossene HF Messung und angegebene Schwellwerte (Standartmäßig auf max. 200; min. 40)

### Auslöser
- Zum Funktionstest auslösung über Button
- Während dem Leitungstest bei Überschreitung/Unterschreitung der HF grenzen

### Standartablauf
Wenn Puls die Grenzen Überschreitet wird ein Alarm ausgelöst

### Alternative Ablaufschritte
- HF werte werden verletzt, Neustart und abbrauch werden angeboten
- Funktionstest

### Hinweise
- Es ist noch nicht geklrt, welcher Pulsmesser verwendet wird

### Änderungsgeschichte
- 0.01 14.03.25 Jakob W, Jakob L und Janick
```mermaid
classDiagram
direction TB
    class Address {
	    -String street
	    -String city
	    -String postal_code
	    -String country
	    -Boolean confirmed
	    +confirm_address()
	    +print_label() String
    }

    class Person {
	    -String name
	    -String phone_number
	    -String email
    }

    class Student {
	    -String student_id
	    -float average_grade
	    +enroll_module(module_name) String
    }

    class Professor {
	    -float salary
	    +teach() String
    }

    Person <|-- Student
    Person <|-- Professor
    Person "0..1" --> "0..*" Address : lives at

