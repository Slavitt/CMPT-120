#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random
class student:
    def __init__(self, name, id, year, major, gpa):
        self.name = name
        self.id = id
        self.year = year
        self.major = major
        self.gpa = gpa

    def honorsEligible(self):
       # if self.gpa.isdigit():
        #newGPA = self.gpa
        if self.gpa > 3.5:
            print("True")
            return True
        else:
            print("False")
            return False

    def wackFunction(self):
        randID = random.randint(100, 999)
        if self.id == randID:
            print("Winner! " + self.name + " gets free lunch!")
        else:
            print("You get nothing! You LOSE! Good DAY, sir!")

def main():
    #create three students and check if they get free lunch and if they qualify for honors
    sam = student("Samuel", 420, "freshman", "cs", 4.0)
    other1 = student("Melissa", 690, "grad i think", "data science or something idk", 4.0)
    other2 = student("placeholder", 123, "sophomore", "gender studies", 2.9)

    sam.honorsEligible()
    sam.wackFunction()

    other1.honorsEligible()
    other1.wackFunction()

    other2.honorsEligible()
    other2.wackFunction()
main()
