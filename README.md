/morse 

json vyzera ako : {
	"text":"dolezity text..."
}

dostanes string "morseovka"


/notes

json vyzera ako :
{
	"notes":"C41-C41/2-G41/2-A31-C41-C41/2-G4(1/2)-A31"
 }

 parsujem len vstup v spravnom formate [A-Za-z][1-9]{2} | [A-Za-z][1-9]\[1-9]\\[1-9]
 

dostanes string "{{note}{note}{note}}"
