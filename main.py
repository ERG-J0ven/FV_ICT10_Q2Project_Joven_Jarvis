from pyscript import display, document

def areyouin(e):
    document.getElementById("in").innerHTML = "" #resets the output when we enter a new one
    fname = document.getElementById("name").value #gets value of first name
    lname = document.getElementById("lname").value #gets value of last name
    mathpeoplename = ["Cheree Mendoza", "Anya Basuil", "Edrian Correa", "Emmanuel Correa", "Francesca Daquigan", "Francis Fernandez", "Gabrielle De Jesus", "Georgina Gamponia", "Hannah Galapon", "Jarvis Joven", "Jibril Abdul", "Julienne Musni", "Khadija Lucman", "Kian Ang", "Krishna Pascua", "Lorissa Paragas", "Lucas Ladion", "Maria Bamba ", "Orange Mendoza", "Rafael Castro", "Rayne Maniago", "Rohan Tabasan", "Tyler Sales", "Yanis Concepcion", "Zander Mirza"] #list of math club members

    fullnamenow = str(fname + " " + lname) #add the value of the two input boxes together and turn them to string
    checkplspls = fullnamenow in mathpeoplename #checks if the name the user entered is inside the list
    lolnotin = "Sorry" + " " + fullnamenow + "," + " " + "you have failed and you will not be joining Math Club for SY 26-27."
    hoorayin = "Congratulations" + " " + fullnamenow + "!" + " " + "you have passed and you will be joining Math Club for SY 26-27." #creates the result message

    display({
        False: lolnotin,
        True: hoorayin} #because it returns a boolean if i only do checkplspls,, we make both of the possible results of a boolean equal to the result messages we created earlier
          [checkplspls], target="in")


somemath7 = {"Jibril Abdul", "Lucas Ladion", "Emmanuel Correa", "Lorissa Paragas", "Maria Bamba", "Zander Mirza"}
somemath8 = {"Rayne Maniago", "Yanis Concepcion", "Rafael De Castro", "Orange Mendoza", "Krishna Pascua","Kian Ang", "Khadija Lucman", "Hannah Galapon", "Georgina Gamponia", "Francesca Daquigan", "Anya Basuil"}
somemath9 = {"Cheree Mendoza", "Jarvis Joven", "Edrian Correa", "Francis Fernandez", "Gabrielle De Jesus", "Rohan Tabasan", "Tyler Sales"}
somemath10= {"Cheree Mendoza", "Jericho Magsalin", "Edrian Correa", "Francis Fernandez", "Phillip Ponce", "Jarvis Joven"} #the 4 sets 
mathclubavengers = somemath7 | somemath8 | somemath9 | somemath10 #union them so that duplicate elements are excluded
mathclubber = sorted(mathclubavengers) #sorts them alphabetically
totalmembercounts = len(mathclubavengers) #gets the total number of people
if document.getElementById("listofmathdudes"):
    display(f"Total Members: {totalmembercounts}\n{'\n'.join(mathclubber)}" ,           target="listofmathdudes") #displays the initial amount and members before we add a new dude, \n is used to seperate the elements and it also removes the brackets, commas and quotation marks to make it more aesthetically pleasing


def goinnow(e):
    document.getElementById("listofmathdudes").innerHTML = "" #clears the previous result
    ffname = document.getElementById("fname").value
    llname = document.getElementById("lname").value #grabs the value of what the user typed in the textbox
    adddude = {f"{ffname} {llname}"} #f string combines these 2 variables into 1
    ultimatemathclub = somemath7 | somemath8 | somemath9 | somemath10 | adddude #same as line 7 but union the new dude along with it
    coolultimatemathclub = sorted(ultimatemathclub) 
    totalmembercount = len(ultimatemathclub) #gets the new amount
    waitthisalmostwork = '\n'.join(coolultimatemathclub) #\n is just <br> but for strings (https://www.geeksforgeeks.org/python/python-line-break-in-string/) and because doing <br> didnt work i had to do \n.join(coolultimatemathclub) so that it can add new lines
    display(f"Total Members: {totalmembercount}\n{waitthisalmostwork}" , target="listofmathdudes") #displays the output, again using \n as a br.


nometal = {"Hydrogen": ('H', 1, 1.0080), "Carbon": ('C', 6, 12.011), "Nitrogen": ('N', 7, 14.007), "Oxygen": ('O', 8, 16.00), "Phosphorus": ('P', 15, 30.9737), "Sulfur": ('S', 16, 32.07), "Selenium": ('Se', 34, 78.97)} #the 7 nonmetals

def yooo(e):
    nokmetal = document.getElementById("nometa").value #gets value of input
    resulting = nometal.get(nokmetal, ("Not a Non-metal", "N/A", "N/A")) #makes sure that if the elemenet entered wasnt a non metal, it would display not a non-metal
    document.getElementById("codes").innerText = nokmetal #puts result for element codde
    document.getElementById("namess").innerText = resulting[0] #puts result for element symbol
    document.getElementById("whereha").innerText = resulting[1] #puts result for atomicnumber
    document.getElementById("heavy").innerText = resulting[2] #puts in the result for mass