#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.



def l2n(letter):
    global number
    global wd
    if letter == "A":
       return float(4)
    if letter == "A-":
        return float(3.7)
    if letter == "B+":
        return float(3.3)
    if letter == "B":
        return float(3)
    if letter == "B-":
        return float(2.7)
    if letter == "C+":
        return float(2.3)
    if letter == "C":
        return float(2)
    if letter == "C-":
        return float(1.7)
    if letter == "D+":
        return float(1.3)
    if letter == "D":
        return float(1)
    if letter == "F" or "FX" or "FZ":
        return float(0)
    if letter == "W":
        print "Withdraw Detected!"
        return float(0)
        wd = True
    else:
        print "Error."

print "GPA Calculator v0.1.1"

ge100c = 1
turk101c = 2
math101c = 4
eng101c = 3
phys101c = 4
me101c = 2

ge100 = raw_input("GE 100: ")
turk101 = raw_input("TURK 101: ")
math101 = raw_input("MATH 101: ")
eng101 = raw_input("ENG 101: ")
phys101 = raw_input("PHYS 101: ")
me101 = raw_input("ME 101: ")

ge100=float(l2n(ge100))
turk101=float(l2n(turk101))
math101=float(l2n(math101))
eng101=float(l2n(eng101))
phys101=float(l2n(phys101))
me101=float(l2n(me101))

try:
    if wd == True:
        print (ge100*1+math101*4+eng101*3+phys101*4+me101*2)/14
except:
    print (ge100*1+turk101*2+math101*4+eng101*3+phys101*4+me101*2)/16
