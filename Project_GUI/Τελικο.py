#το προγραμμα για να λειτουργισει πρεπει να ειναι τουλαχιστον 3.4.0 η εκδοση python
#Κωδικος:1234

#εισαγουμε τις βιβλειοθηκες ()
from turtle import*
from random import*
from tkinter import*
from tkinter.messagebox import*
import time
import tkinter as tk

bg="orange""
fg="blue"       #χρωμα γραμματων αρχικης σελιδας
fg2="blue"      # χρωμα γραμματων menu
wi=50           # πλατος
hi=100          # υψος εικονας

pin=input("Δώσε κωδικό ")
while pin!="1234" :
    if pin=="":
        print("Δεν δώσατε κωδικό ")
        pin=input("Δώσε κωδικό ")
    else:
        print("Μην αποδεκτός κωδικός")
        pin=input("Δωσε κωδικο")
print("Αποδεκτός κωδικός")
print("To πρόγραμμα άνοιξε σε νέο παράθυρο")

root = Tk()          #δημιουργεια παραθυρου
root.title("Python") #τιτλος παραθηρου

#εισαγωγη εικονας
image= Frame(root) 
image.pack(side= TOP) 
image = tk.PhotoImage(file="python2.png")
label = tk.Label(width=7000,height=hi,image=image,background=bg)
label.pack(side=TOP)

textf= Frame(root)      #δημιουργεια πλαισιου
textf.pack(side=LEFT)   #στιχιση πλαισιου
text=Text(textf, height=40, width=40, font="Arial 20",
           selectforeground="darkorange", foreground=fg2, background=bg)
label.pack(side=TOP)    # οριζουμε τα στοιχεια του κειμενου
text.pack(side= LEFT)   # στιχιση κειμενου
text.insert(END,
"""
Η Python είναι μια υψηλού επιπέδου γλώσσα
προγραμματισμούη οποία δημιουργήθηκε
από τον Ολλανδό Γκβίντο βαν Ρόσσουμ (Guido van Rossum)
το 1990. Ο κύριος στόχος της
είναι η αναγνωσιμότητα του κώδικά της
και η ευκολία χρήσης της και το συντακτικό της
επιτρέπει στους προγραμματιστές να εκφράσουν έννοιες
σε λιγότερες γραμμές κώδικα απ'ότι θα
ήταν δυνατόν σε γλώσσες όπως η C++ ή η Java.
Διακρίνεται λόγω του ότι έχει πολλές βιβλιοθήκες που
διευκολύνουν ιδιαίτερα αρκετές
συνηθισμένες εργασίες και για την ταχύτητα εκμάθησης της.
""")

textf= Frame(root) 
textf.pack(side=RIGHT) 
text= Text(textf, height=60, font="Arial 20",
            selectforeground="darkorange", foreground=fg2, background=bg)
text.pack(side= RIGHT)
text.insert(END,
"""
                  Τύποι δεδομένων

int : χρησιμοποιείτε για
ακεραίους αριθμούς 

float:  χρησιμοποιείτε για
δεκαδικούς αριθμούς

str:  χρησιμοποιείτε για
χαρακτήρεςπ.χ α,β,4,8

               Προσοχή

Στην python γίνετε διάκριση
κεφαλαία και μικρά.
""")

# δημειουργεια συναρτισεων

def Tkinter():
    showinfo("Tkinter","""   
  Η βιβλιοθήκη Tkinter περιέχει εντολές που
     έχουν σχέσει με την δημιουργία παραθύρων""")

def Time():
    showinfo("Time","""   
     Η βιβλιοθήκη Time περιέχει εντολές που
     έχουν σχέσει με τον χρόνο""")

def Random():
    showinfo("Random","""   
      Η βιβλιοθήκη Random περιέχει εντολές που
     έχουν σχέσει με την τυχαία επιλογή""")

def turtl():
    showinfo("Turtle","""   
      Η βιβλιοθήκη Turtle περιέχει εντολές που
     έχουν σχέσει με την δημιουργία γραφικών σχεδίων """)

def kyklos():
    showinfo("ΚΩΔΙΚΑΣ","""   
 bgcolor("black")
    for x in range(50):
            speed(30)
            for i in range(1,5):
                col=["red", "green", "blue"]
                color(choice(col))
                forward(200)
                left(89)
""" )
        
#αστερια
def drawStar():
    speed(4000)
    bgcolor("black")
    for i in range(80):
        col1=["gold", "green", "orange", "red", "blue"]
        color(choice(col1))
        pendown()
        begin_fill()
        penup()
        h=randint(-600,600)
        v=randint(-600,600)
        setpos(v ,h)
        pendown()
        m=randint(5,30)
        for side in range(5):
            left(144)
            forward(m)
        end_fill()
        penup()

def draw():
    b=input("Δώσε χρώμα  για background")
    bgcolor(b)
    col1=["gold", "green", "orange", "red", "blue"]
    print("""
    Μένου για τoυς κωδικούς χρωμάτων :
    Για χρυσο πατα 0
    Για πρασινο πατα 1
    Για πορτοκαλι πατα 2
    Για κοκκινο πατα 3
    Γα μπλε πατα 4
    """)
    c=int(input("Δωσε χρώμα : "))
    p=int(input("Πόσες πλευρές θα έχει το σχήμα : "))
    g=int(input("Δώσε γωνιά : "))
    m=int(input("Δώσε μήκος πλευράς  : "))
    apo=int(input("Δώσε μήκος / απόσταση σχεδίων : "))
    while p!=0 and g!=0 and m!=0:
        color(col1[c])
        pendown()
        for side in range(p):
            left(g)
            forward(m)
        penup()
        forward(apo)
        h=randint(-600,600)
        v=randint(-600,600)
        setpos(v ,h)
    print("________________________")
            
#πολλα τετραγωνα σχηματιζουν ενα κυκλο
def tetragono():
    bgcolor("black")
    for x in range(80):
            speed(30)
            for i in range(1,5):
                col=["red", "green", "blue"]
                color(choice(col))
                forward(200)
                left(89)                
def helpstar():
    #showinfo ειναι ο τυπος ενος παραθυρου
    showinfo("ΚΩΔΙΚΑΣ","""  
from turtle import*
from random import*
bgcolor("black")
speed(40)
for i in range(80):
    col1=["red", "green", "blue", "yellow"] 
    color(choice(col1))
    pendown()
    begin_fill()
    penup()
    h=randint(-360,360)
    v=randint(-360,360)
    setpos(v ,h)
    pendown()
    for side in range(5):
         left(144)
         forward(20)
    end_fill()
    penup()
""")

def antionoma(): 
    showinfo("info","Πηγαίνετε στην γραμμή εντολών της  Python")
    print("Δώσε 5 ονόματα ")
    lista=[]
    for i in range(5):
        onoma=input(i)
        lista=lista+[onoma]
    lista.sort()
    print("Τα ονόματα που έδωσες  αλφαβητικά είναι:", lista)
    print("Τα ονόματα αντίστροφα είναι:")
    for i in range(5):
        print(lista[4-i])
    f=input("Δώσε ένα όνομα για να δεις αν υπάρχει στην λίστα ")
    while f!="":
        fo=False
        for i in lista:
            if i==f:
                fo=True
        if fo==True:
            print("Βρέθηκε")
        else:
            print("Δεν βρέθηκε")
        f=input("Δώσε ένα άλλο όνομα για να δεις αν υπαρχει στην λίστα ή πάτα enter για τέλος ") 
    print("________________________")
def helponoma():
    showinfo("ΚΩΔΙΚΑΣ","""
print("Δώσε 5 ονόματα ")
    lista=[]
    for i in range(5):
        onoma=input(i)
        lista=lista+[onoma]
    lista.sort()
    print("Τα ονόματα που έδωσες  αλφαβητικά είναι :", lista)
    print("Τα ονόματα αντίστροφα είναι:")
    for i in range(5):
        print(lista[4-i])
    f=input("Δώσε ένα όνομα για να δεις αν υπαρχει στην λίστα")
    while f!="":
        fo=False
        for i in lista:
            if i==f:
                fo=True 
        if fo==True:
            print("Βρέθηκε")
        else:
            print("Δεν βρέθικε")
        f=input("Δώσε ένα άλλο όνομα για να δεις αν υπάρχει στην λίστα ή πάτα enter για τέλος")
        """)
def WHILE():
     showinfo("WHILE","""
        Χρησιμοποιείτε για την επανάληψη όταν δεν ξέρουμε τον αριθμό των επαναλήψεων 
           (μπορεί να χρησιμοποιηθεί και όταν ξέρουμε των αριθμό των επαναλήψεων)
    
        while (Συνθήκη):
            .
            .    
            .  Εντολές
            .
            .
        """)

def PRINT():
    showinfo("PRINT","""
    Για να εμφανίσουμε ένα μήνυμα     

    print(15)                   Τυπώνει 15       
    print("Hi")                 Τυπώνει Hi
    print(5+5)                  τυπώνει 10
    print("Mήκος  =", 20)       τυπώνει Μήκος =20
    """)

def FOR():
    showinfo("FOR","""
    Χρησιμοποιείτε για την επανάληψη όταν  ξέρουμε τον αριθμό των επαναλήψεων
    
for (Μεταβλητή) in range(Αρχή,Τέλος,Βήμα):
        .
        .
        .   Εντολές
        .
        .   
""")

def IF():
    showinfo("IF","""
Για να ελέγξουμε   κάτι

if (Συνθήκη):
    .
    .
    .   Εντολές
    .
    .

""")

def ELSE():
    showinfo("ELSE","""
    if:Για να ελέγξουμε   κάτι

    else: Αν δεν ισχύει η if τότε εκτελούνται οι εντολές της else

    if (Συνθήκη):
        .
        .
        .   Εντολές
        .
        .
    else:
        .
        .
        . Εντολές
        .
        .

""")

def ELIF():
    showinfo("ELIF","""
Η elif  εκτελείται αν 
1. Η παραπάνω συνθήκη(if) δεν ισχύει
2. Η συνθήκη της elif  ισχύει

 if (Συνθήκη):
        .
        .
        .   Εντολές
        .
        .

elif (Συνθήκη):  #ΜΠΟΡΕΙ ΝΑ ΥΠΑΡΧΟΥΝ ΠΕΡΙΣΟΤΕΡΕΣ ΑΠΟ ΜΙΑ elif
        .
        .
        .  Εντολές
        .
        .
        .
        
else:
        .
        .
        . Εντολές
        .
        .

""")

def Import():
    showinfo("Import","""Με την εντολή import εισάγουμε βιβλιοθήκες """)

def helpgames():
    showinfo("ΠΡΟΣΟΧΗ",""" Δες στην αρχική σελίδα του προγράμματος""")
       
def games():
    score=0
    showinfo("ΠΡΟΣΟΧΗ","""
     Μεταβείτε στην γραμμή εντολών της python για να ξεκινήσετε το παιχνίδι 
     Μέχρι να ολοκληρωθεί το παιχνίδι δεν μπορείτε να κάνετε τίποτα άλλο στο πρόγραμμα """)
    print("""
    ΟΔΗΓΙΕΣ
    Πληκτρολογήστε :
    Για Nαι πατα 1  
    Για Oχι πατα 0     
    Για Βοήθεια πατα 2 
    """)
    #1
    a1=int(input("Υπάρχει εντολή print  "))
    if a1==2:
         PRINT()
         a1=int(input("Υπάρχει εντολή print "))
    if a1==1:
        score=score+1
    #2
    a2=int(input("Υπάρχει βιβλιοθήκη  Tkinter ?"))
    if a2==2:
        Tkinter()
        a2=int(input("Υπάρχει βιβλιοθήκη  Tkinter ?"))
    if a2==1:
        score=score+1
    #3
    a3=int(input(" Με την while εισάγουμε μια βιβλιοθήκη  "))
    if a3==2:
         WHILE()
         a2=int(input(" Με την while εισάγουμε μια βιβλιοθήκη"))
    if a3==0:
        score=score+1
    #4
    a4=int(input("Η for χρησιμοποιείτε για την επανάληψη  "))
    if a4==2:
         FOR()
         a2=int(input("Η for χρησιμοποιείτε για την επανάληψη "))
    if a4==1:
        score=score+1
    #5
    a5=int(input("Η int είναι για τους δεκαδικούς αριθμούς"))
    if a5==2:
         helpgames()
         a2=int(input("Η int είναι για τους δεκαδικούς αριθμούς"))
    if a5==0:
        score=score+1
    #6
    a6=int(input("Πληκτρολογήστε 2 για να δεις τον κωδικά του  Star και γράψε ποσά  χρώματα υπάρχουν  ?"))
    if a6==2:
        helpstar()
        a2=int(input("Πληκτρολογήστε τον αριθμό  χρώματα υπάρχουν στο Star?"))
    if a6==4:
        score=score+1
    #7
    a7=int(input("Η elif μόνο μια μπορεί να υπάρχει "))
    if a7==2:
         ELIF()
         a2=int(input("Η elif μόνο μια μπορεί να υπάρχει "))
    if a7==0:
        score=score+1
    #8
    a8=int(input("Η Time άφορα  την ώρα  "))
    if a8==2:
         Time()
         a2=int(input("Η Time άφορα  την ώρα"))
    if a8==1:
        score=score+1
    #9
    a9=int(input("Υπαρχή βιβλιοθήκη που σου δίνουν την δυνατότητα για τυχαίες επιλογές "))
    if a9==2:
         Random()
         a2=int(input("Υπαρχή βιβλιοθήκη που σου δίνουν την δυνατότητα για τυχαίες επιλογές "))
    if a9==1:
        score=score+1
    #10
    a10=int(input("Στην python γίνεται διάκριση Κεφαλαίων και μικρόν "))
    if a10==2:
         helpgames()
         a2=int(input("Στην python γίνεται διάκριση Κεφαλαίων και μικρόν "))
    if a10==1:
        score=score+1
    print("TEΛΟΣ ΠΑΙΧΝΙΔΙΟΥ")
    if  score>8:
        print("Τα πήγες τελεία ")
        print("Απάντησες σωστά στης ",score,"απο τις 10")
    elif score>5:
        print("Τα πήγες καλά ")
        print("Απάντησες σωστά στης ",score,"απο τις 10")
    else:
        print(" Ξαναδοκίμασε ")
        print("Απάντησες σωστά στης ",score,"απο τις 10")
    print("________________________")
    
def Exit():
    exit()
    
def dimturtle():
    showinfo("πετρά,μολύβι,ψαλίδι,χαρτί","""Μεταβείτε στην γραμμή εντολών της python για να ξεκινήσετε το παιχνίδι """)
    print("")
    print("""Ας παίξουμε πετρά,μολύβι,ψαλίδι,χαρτί  
ΠΛΗΚΡΩΛΟΓΙΣΕ 
Για Πετρά πατα p
Για Μολύβι πατα m
Για Χαρτί πατα  x
Για Ψαλίδι πατα c
""")
    g=4
    pai=input("=>")
    while g!=0:
        if pai=="p":
            print("Πετρά")
            pai=1
        elif pai=="m":
            print("Μολύβι")
            pai=2
        elif pai=="x":
            print("Χαρτί")
            pai=3
        else:
            print("Ψαλίδι")
            pai=4
        print("vs")
        c=randint(1,4)
        if c==1:
          print("Πετρά")
        elif c==2:
          print("Μολύβι")
        elif c==3:
          print("Χαρτί")
        else:
          print("Ψαλίδι")
            #εκδοχες
        if c==1 and pai==1:
          print("Ισοπαλία")
      
        if c==2 and pai==2:
            print("Ισοπαλία")
      
        if c==3 and pai==3:
            print("Ισοπαλία")
    
        if c==4 and pai==4:
            print("Ισοπαλία")
      
        if c==1 and pai==2:
            print("O H/Y κέρδισε ")

        if c==2 and pai==1:
            print("O παίχτης κέρδισε ")

        if c==3 and pai==4:
            print("Ο παίχτης κέρδισε ")

        if c==4 and pai==3:
            print("Ο Η/Υ κέρδισε ")

        if c==1 and pai==3:
            print("Ο παίχτης κέρδισε  ")

        if c==3 and pai==1:
            print("Ο Η/Υ κέρδισε ")

        if c==3 and pai==2:
            print("O παίχτης κέρδισε ")

        if c==2 and pai==3:
            print("O Η/Υ κέρδισε ")

        if c==1 and pai==4:
            print("Ο Η/Υ κέρδισε  ")

        if c==4 and pai==1:
            print("Ο παίχτης κέρδισε  ")

        if c==2 and pai==4:
            print("Ο παίχτης κέρδισε ")

        if c==4 and pai==2:
            print("Ο Η/Υ κέρδισε  ")
        pai=input("=>")
        g=g-1
    print("________________________")

def kremala():
    showinfo("ΚΡΕΜΑΛΑ","""Μεταβείτε στην γραμμή εντολών της python για να ξεκινήσετε το παιχνίδι """)
    lej=["σπιτι","πετρα","σχολειο","υπολογιστης","πετρος","τσαντα","τραπεζι","μουσικη","πληροφορικη"]
    l=choice(lej)
    q=3
    print("Προσοχή τα γράμματα να είναι στα ελληνικά και μικρά")
    print("Ζωές", q)
    ww=[]                
    sw1=[] 
    x=len(l)
    for i in range(x):
        k=" __"
        sw1.append(k)
    print(" __"*len(l))
    print("Η λέξη ξεκινά με", l[0])
    found=False
    g=input("Δώσε γραμμα")
    while q!=0 and x!=0 :
        t=0
        if g in l:
            for i in l:
                if i==g:
                    sw1.pop(t)
                    sw1.insert(t,g)
                    x=x-1
                t=t+1
            print(sw1)
        else:
            q=q-1
            ww.append(g)
            print("γραμματα που εχεις πει  :", ww)
            print("Ζωές", q)
        if x!=0:
            g=input("Δώσε γραμμα")
        else:
            found=True
    if found==True:
        print("Μπράβο την βρήκες την λέξη ")
    else:
        print("Λυπάμαι....")
        print("Η λέξη είναι :", l)  
    print("________________________")
def triliza():
    x=["","1","2","3",""]
    y=["","4","5","6",""]
    c=["","7","8","9",""]
    print("Παίξε τρίλιζα στην πιστά της python")
    print("""
    Οδηγίες
    2.Πληκτρολόγησε τον αριθμό που θέλεις να βάλεις το Χ ή το Ο 
    3. Όταν τελειώσεις και δεν έχει νικήσει κανένας πάτα enter
    """)
    print()
    print("",x[1],"",x[2],"",x[3])
    print()
    print("",y[1],"",y[2],"",y[3])
    print()
    print("",c[1],"",c[2],"",c[3])
    print()
    print("1ος παίχτης έχει το X")
    print("2ος παίχτης έχει το Ο")
    ls=[]
    g=1
    niki=False
    while g<=5:
        print("_ _ _ _ _ _ _ _")
        print("Γύρος:",g)
        print("- - - - - - - -")
        pp=input(" Χ : ")
        while (pp in ls) or (pp==""):
            pp=input(" Χ : ")
        ls.append(pp)
        if pp in x:
            t=0
            for i in x:
                if i==pp:
                    x.pop(t)
                    x.insert(t,"x")
                t=t+1

        if pp in y:
            t=0
            for i in y:
                if i==pp:
                    y.pop(t)
                    y.insert(t,"x")
                t=t+1

        if pp in c:
            t=0
            for i in c:
                if i==pp:
                    c.pop(t)
                    c.insert(t,"x")
                t=t+1        
        print("________________")
        print()
        print("",x[1],"",x[2],"",x[3])
        print()
        print("",y[1],"",y[2],"",y[3])
        print()
        print("",c[1],"",c[2],"",c[3])
        print()
        print("________________")
        dp=input("  O : ")
        while (dp in ls) or (dp==""):
            dp=input(" O : ")
        ls.append(dp)
        if dp in x:
            t=0
            for i in x:
                if i==dp:
                    x.pop(t)
                    x.insert(t,"o")
                t=t+1

        if dp in y:
            t=0
            for i in y:
                if i==dp:
                    y.pop(t)
                    y.insert(t,"o")
                t=t+1

        if dp in c:
            t=0
            for i in c:
                if i==dp:
                    c.pop(t)
                    c.insert(t,"o")
                t=t+1
        print("________________")
        print()
        print("",x[1],"",x[2],"",x[3])
        print()
        print("",y[1],"",y[2],"",y[3])
        print()
        print("",c[1],"",c[2],"",c[3])
        print()
        print("________________")
    
    
#ekdoxes x
        if x[1]=="x" and x[2]=="x" and x[3]=="x":
            g=10
            print("ΝΙΚΗΣΕ Ο ΠΡΩΤΟΣ")
            niki=True
        if c[1]=="x" and c[2]=="x" and c[3]=="x":
            g=10
            print("ΝΙΚΗΣΕ Ο ΠΡΩΤΟΣ")
            niki=True
        if y[1]=="x" and y[2]=="x" and y[3]=="x":
            g=10
            print("ΝΙΚΗΣΕ Ο ΠΡΩΤΟΣ")
            niki=True
        if x[1]=="x" and y[2]=="x" and c[3]=="x":
            g=10
            print("ΝΙΚΗΣΕ Ο ΠΡΩΤΟΣ")
            niki=True
        if x[3]=="x" and y[2]=="x" and c[1]=="x":
            g=10
            print("ΝΙΚΗΣΕ Ο ΠΡΩΤΟΣ")
            niki=True
        if x[1]=="x" and y[1]=="x" and c[1]=="x":
            g=10
            print("ΝΙΚΗΣΕ Ο ΠΡΩΤΟΣ")
            niki=True
        if x[2]=="x" and y[2]=="x" and c[2]=="x":
            g=10
            print("ΝΙΚΗΣΕ Ο ΠΡΩΤΟΣ")
            niki=True
        if x[3]=="x" and y[3]=="x" and c[3]=="x":
            g=10
            print("ΝΙΚΗΣΕ Ο ΠΡΩΤΟΣ")
            niki=True
# ekdoxes o
        if x[1]=="o" and x[2]=="o" and x[3]=="o":
            g=10
            print("ΝΙΚΗΣΕ Ο ΔΕΥΤΕΡΟΣ")
            niki=True
        if c[1]=="o" and c[2]=="o" and c[3]=="o":
            g=10
            print("ΝΙΚΗΣΕ Ο ΔΕΥΤΕΡΟΣ")
            niki=True
        if y[1]=="o" and y[2]=="o" and y[3]=="o":
            g=10
            print("ΝΙΚΗΣΕ Ο ΔΕΥΤΕΡΟΣ")
            niki=True
        if x[1]=="o" and y[2]=="o" and c[3]=="o":
            g=10
            print("ΝΙΚΗΣΕ Ο ΔΕΥΤΕΡΟΣ")
            niki=True
        if x[3]=="o" and y[2]=="o" and c[1]=="o":
            g=10
            print("ΝΙΚΗΣΕ Ο ΔΕΥΤΕΡΟΣ")
            niki=True
        if x[1]=="o" and y[1]=="o" and c[1]=="o":
            g=10
            print("ΝΙΚΗΣΕ Ο ΔΕΥΤΕΡΟΣ")
            niki=True
        if x[2]=="o" and y[2]=="o" and c[2]=="o":
            g=10
            print("ΝΙΚΗΣΕ Ο ΔΕΥΤΕΡΟΣ")
            niki=True
        if x[3]=="o" and y[3]=="o" and c[3]=="o":
            g=10
            print("ΝΙΚΗΣΕ Ο ΔΕΥΤΕΡΟΣ")
            niki=True
        g=g+1
    if niki==False:
        print("Δεν νίκησε κανένας")
    print("Τέλος Παιχνιδιού ")    
    print("________________________")
#δημιουργεια γραμμης μενου
menu= Menu(root)
root.config(menu=menu)

#οριζουμε στα menu τα ονοματα τους
python=Menu(menu)
ent=Menu(menu)
entoles=Menu(menu)
dra=Menu(menu)
vivl=Menu(menu)
gr=Menu(menu)
kgr=Menu(menu)
ep=Menu(menu)
sin=Menu(menu)
tetr=Menu(menu)
st=Menu(menu)
lis=Menu(menu)

#python
menu.add_cascade(label="Python", menu=entoles)
entoles.add_cascade(label="Βιβλιοθήκες", menu=vivl) 
entoles.add_cascade(label="Εντολές", menu=ent)
ent.add_cascade(label="Επανάληψη", menu=ep)

#επανάληψη
ent.add_cascade(label="Έλεγχος", menu=sin) 
ep.add_command(label="While", command=  WHILE, foreground=fg)
ep.add_command(label="For", command= FOR, foreground=fg)

#Έλεγχος 
sin.add_command(label="If", command= IF, foreground=fg)
sin.add_command(label="If/Else", command= ELSE, foreground=fg)
sin.add_command(label="If/Elif/Else", command= ELIF, foreground=fg)
ent.add_command(label="Import", command= Import, foreground=fg)
ent.add_command(label="Print", command= PRINT, foreground=fg)
entoles.add_command(label="Παιχνίδι Ερωτήσεων για την Python", command=games, foreground=fg)

#βιβλιοθηκες
vivl.add_command(label="Tiknter",  foreground=fg, command=Tkinter)
vivl.add_command(label="Random",  foreground=fg, command=Random)
vivl.add_command(label="Turtle",  foreground=fg, command=turtl)
vivl.add_command(label="Time",  foreground=fg, command=Time)

#παραδηγματα
menu.add_cascade(label="Παραδείγματα", menu= python)

python.add_cascade(label="Σχηματισμός κύκλου από τετράγωνα", menu= tetr)
tetr.add_command(label="Πρόγραμμα", command= tetragono, foreground=fg)
tetr.add_command(label="Κωδικας", command= kyklos, foreground=fg )

python.add_cascade(label="Star", menu= st)
st.add_command(label="Πρόγραμμα", command= drawStar, foreground=fg )
st.add_command(label="Kωδικας", command= helpstar, foreground=fg )

python.add_cascade(label="Λίστα με ονόματα", menu= lis)
lis.add_command(label="Πρόγραμμα ", command=antionoma, foreground=fg)
lis.add_command(label="Κωδικας ", command= helponoma, foreground=fg )

#Παιχνιδια
menu.add_cascade(label="Παιχνίδια", menu=dra) 
dra.add_command(label="Ζωγραφική", command=draw, foreground=fg)
dra.add_command(label="Πετρά/μολύβι/ψαλίδι/χαρτί    ", command=dimturtle, foreground=fg)
dra.add_command(label="Κρεμάλα", command=kremala, foreground=fg)
dra.add_command(label="Τριλιζα", command=triliza, foreground=fg)

#time and  day
menu.add_command(label=time.strftime(' %x '))
menu.add_command(label=time.strftime(' %A '))

#exit
menu.add_command(label="Έξοδος", command=Exit)




