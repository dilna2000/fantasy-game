from tkinter import *
from tkinter import messagebox
import mysql.connector
import wikipedia
top=Tk()
top.geometry("900x900")
top.title("FANTASY CRICKET LEAGUE")
imga=PhotoImage(file="stads.png")                      #Background Image
font=PhotoImage(file="font.png")                       #Background Image

def click1():
    top.destroy()                                      #Destroying the first window
    top1=Tk()
    top1.geometry("600x500")
    global lb,lb1
    img1=PhotoImage(file="sky.png")
    batimage=PhotoImage(file="bat.png")
    ballimage=PhotoImage(file="ball.png")
    arimage=PhotoImage(file="batball.png")
    wicketimage=PhotoImage(file="wicket.png")
    Label(top1,image=img1).pack(side=TOP)
   
    lb=Listbox(top1,height=20,width=35)                 #Listbox containing available players
    lb1=Listbox(top1,height=20,width=35)                 #Listbox containing selected players
    
    def on_click_listbox(event):                         #Selected batsman  will be transferred to other  listbox
     
        index = lb.curselection()
        seltext = lb.get(index)
        if lb1.size()!=4:
            lb.delete(ANCHOR)
            lb1.insert(0,seltext)
            
            
        else:
            messagebox.showinfo("Error","Select only 4 Batsman")
            
            
        
        bat1.delete(0,END)
        bat1.insert(0,lb1.size())
    def on_click_listbox1(event):                               #Selected bowlers  will be transferred to other  listbox
    
        index = lb.curselection()
    
        seltext = lb.get(index)
        
        
        if (lb1.size())!=8:
            
            lb.delete(ANCHOR)
            lb1.insert(0,seltext)
            
            
            
        else:
            messagebox.showinfo("Error","Select only  4 Bowlers")
            
            
        bowl1.delete(0,END)

        bowl1.insert(0,lb1.size()-4)
            
        
        
    def on_click_listbox2(event):                                       #Selected allrounders  will be transferred to other  listbox
    
        index = lb.curselection()
    
        seltext = lb.get(index)
        
        if (lb1.size())!=10:
            lb.delete(ANCHOR)

            lb1.insert(0,seltext)
            
            
        else:
            messagebox.showinfo("Error","Select only 2  All Rounders")
            
            
            
        ar1.delete(0,END)

        ar1.insert(0,lb1.size()-8)
            
    def on_click_listbox3(event):                                       #Selected wicketkeepers  will be transferred to other  listbox
    
        index = lb.curselection()
    
        seltext = lb.get(index)
        
        if (lb1.size())!=11:
            lb.delete(ANCHOR)
            lb1.insert(0,seltext)
            
            
            
        else:
            messagebox.showinfo("Error","Select only 1 Wicket Keeper")
            
            
        wk1.delete(0,END)

        wk1.insert(0,lb1.size()-10)
            
            

    
    def r1():                                             #Function to display available players when radiobox is selected
        lb.delete(0,END)
        messagebox.showinfo("Error"," Select 4 Batsman")

        lb.insert(1,"Rohit Sharma")
        lb.insert(2,"Virat Kohli")
        lb.insert(3,"Prithvi Shaw")
        lb.insert(4,"Mayank Agarwal")
        lb.insert(5,"Kedhar Jadhav")
        lb.insert(6,"A Rahane")
        lb.insert(7,"Shikar Dhawan")
        lb.insert(8,"S Iyer")
        lb.insert(9,"Manish Pandey")
        
       
        lb.bind('<ButtonRelease-1>', on_click_listbox)

    def r2():
        lb.delete(0,END)
        messagebox.showinfo("Error","Select 4 Bowlers")
        lb.insert(1,"Bhuvaneshwar Kumar")
        lb.insert(2,"Yuvendra Chahal")
        lb.insert(3,"Jasprit Bumrah")
        lb.insert(4,"Mohammed Shami")
        lb.insert(5,"Kuldeep Jadhav")
        
        lb.insert(6,"Umesh Yadav")
        lb.bind('<ButtonRelease-1>', on_click_listbox1)
    def r3():
        
        lb.delete(0,END)
        messagebox.showinfo("Error","Select 2 All Rounders")
        lb.insert(1,"Hardik Pandya")
        lb.insert(2,"Ravindra Jadeja")
        lb.insert(3,"R Ashwin")
        lb.insert(4,"Yuvraj Singh")
        
        
       
      
        lb.bind('<ButtonRelease-1>', on_click_listbox2)
    def r4():
        lb.delete(0,END)
        lb.insert(1,"Mahendra Singh Dhoni")
        lb.insert(2,"KL Rahul")
        lb.insert(2,"Dinesh Kartik")
        lb.bind('<ButtonRelease-1>', on_click_listbox3)
        
        
        
        
        
    def new():                                                    #when new  team is clicked all the widgets are abled
        messagebox.showinfo("Name","Enter a new name for team and select help to know how to play the game!")
        e.config(state=NORMAL)
        R1.config(state=NORMAL)
        R2.config(state=NORMAL)
        R3.config(state=NORMAL)
        R4.config(state=NORMAL)
        bat1.config(state=NORMAL)
        bowl1.config(state=NORMAL)
        ar1.config(state=NORMAL)
        wk1.config(state=NORMAL)
        
    def save():                                                 #when team is saved
        myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "", database = "fantasy")
        mycur=myconn.cursor()
                                                                                              
        if e.get()=="":
            messagebox.showinfo("Name","Enter Team Name")
        mycur.execute("SELECT teamname FROM team")
        repeat=mycur.fetchall()
        
        for i in repeat:
                
                if e.get()==i[0]:
                    messagebox.showinfo("Repeat","Team already exists\nselect new team again")
                    lb1.delete(0,END)
                    break
        if lb1.size()==11:
            messagebox.showinfo("Saved","Your team has been succesfully saved")
            global lb2
            lb2=Listbox(top1)
            n=lb1.get(0,lb1.size())
            lb2.insert(0,n)
            
            for i in range(0,lb1.size()):
                n1=lb1.get(i)
                mys="INSERT INTO team(teamname,playername) VALUE(%s,%s) "
                val=(e.get(),n1)
                mycur.execute(mys,val)
            myconn.commit()

            
        elif lb1.size()>11:
            messagebox.showinfo("Error","Insufficient players greater than 11")
        elif lb1.size()<11:
            messagebox.showinfo("Error","Insufficient players less than 11")
        
        
        

    def evaluate():                                      #Function for evaluation of team
        
        top2=Toplevel()
        top2.geometry("500x500")
        top2.title("Evaluate Team")
        back1=PhotoImage(file="back1.png")                #Background Image
        Label(top2,image=back1).pack(side=TOP)
        global comp
        global point
        l1=[ ]
        tot1=[ ]
        tot=[ ]
        l2=[ ]
        comp=[ ]
        point=[ ]
        ind=[ ]
        curs=mysql.connector.connect(host="localhost",user="root",passwd="",db="fantasy")              #Making connection to database
        mycursor=curs.cursor()
        mycursor.execute("SELECT teamname FROM team ")
        myresult = mycursor.fetchall()
        for x in myresult:
            l1.append(x)
            
        l2 = list(set(l1))                                                                             #non repetition of teamnames
        eval=Label(top2,text="Evaluation",width=10,font=('Helvetica',15,'bold'),bg="black")
        eval.pack(side=TOP)
        eval1=Label(top2,text="Team Name",width=10,font=('Helvetica',11),bg="white")
        eval1.place(x=20,y=40)
        optionVar = StringVar()
        optionVar.set(l2[0])
        option = OptionMenu(top2, optionVar, *l2 )                                                      #Drop down list                                                      
        option.config(width=10)
        option.config(bg="white")
        option.place(x=140,y=40)
        eval2=Label(top2,text="Players",width=10,font=('Helvetica',11),bg="white")
        eval2.place(x=5,y=90)
        listeval=Listbox(top2,height=20,width=35)
        listeval.place(x=5,y=130)
        eval3=Label(top2,text="Points",width=10,font=('Helvetica',11),bg="white")
        eval3.place(x=260,y=90)
        evaltxt=Text(top2,width=10,height=1)
        evaltxt.place(x=340,y=90)
        listeval1=Listbox(top2,height=20,width=35)
        listeval1.place(x=250,y=130)
        
        def select(*args):                                                       #When a team name is selected for evaluation
            listeval1.delete(0,END)
            listeval.delete(0,END)

            seloption=optionVar.get()
            sel=seloption.translate({ord(i): None for i in "('),'"})
            mys1="SELECT playername FROM team WHERE teamname='" + sel + "';"                          #Points Calculation by retrieving value from  database
            
            mycursor.execute(mys1)
            result = mycursor.fetchall()
            for i in result:
                i =  ''.join(i)
                listeval.insert(0,i)
            for i in range(0,listeval.size()):
                sel1=listeval.get(i)
                sel2 =  ''.join(sel1)
                batmys="SELECT scored FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(batmys)
                result2=mycursor.fetchone()
                result2=int(result2[0])
                batpoint=1*(result2/2)
                batmys1="SELECT 50s FROM stats1 WHERE player='" + sel2 + "';"
                mycursor.execute(batmys1)
                result3=mycursor.fetchone()
                result3=int(result3[0])
                batpoint1=5*(result3)
                
                batmys2="SELECT 100s FROM stats1 WHERE player='" + sel2 + "';"
                mycursor.execute(batmys2)
                result4=mycursor.fetchone()
                result4=int(result4[0])
                batpoint2=10*(result4)
                
                batmys3="SELECT fours FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(batmys3)
                result5=mycursor.fetchone()
                result5=int(result5[0])
                batpoint3=1*(result5)
                
                batmys4="SELECT sixes FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(batmys4)
                result6=mycursor.fetchone()
                result6=int(result6[0])
                batpoint4=2*(result6)
                
                batmys5="SELECT faced FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(batmys5)
                result7=mycursor.fetchone()
                result7=int(result7[0])
                batmys6="SELECT runs FROM stats1 WHERE player='" + sel2 + "';"
                mycursor.execute(batmys6)
                result8=mycursor.fetchone()
                result8=int(result8[0])
                if result7==0:
                    result8=0
                else:
                    result8=result8/result7
                    
                if result8>80 and result8<100:
                    result8=2

                    
                elif result8>100:
                    result8=4
                else:
                    result8=0
                bowlmys="SELECT wkts FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(bowlmys)
                res=mycursor.fetchone()
                res=int(res[0])
                res=10*(res)
                ecomys="SELECT given FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(ecomys)
                res1=mycursor.fetchone()
                res1=int(res1[0])
                res1=res1/20
                if res1>3.5 and res1<4.5:
                    res1=4
                elif res1>2 and res1<3.5:
                    res1=7
                elif res1<2 and res1>0:
                    res1=10
                else:
                    res1=0
                    
                catchmys="SELECT catches FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(catchmys)
                res2=mycursor.fetchone()
                res2=int(res2[0])
                res2=10*res2
                catchmys1="SELECT stumping FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(catchmys1)
                res3=mycursor.fetchone()
                res3=int(res3[0])
                res3=10*res3
                catchmys2="SELECT RO FROM match2 WHERE player='" + sel2 + "';"
                mycursor.execute(catchmys2)
                res4=mycursor.fetchone()
                res4=int(res4[0])
                res4=10*res4
                total=round(batpoint)+round(batpoint1)+round(batpoint2)+round(batpoint3)+round(batpoint4)+round(result8)+round(res)+round(res1)+round(res2)+round(res3)+round(res4)

                tot.append(total)
            
            tot1=tot[::-1]
            
            for i in range(0,len(tot1)):
                listeval1.insert(0,tot1[i])
            points=sum(tot1)   
            
            
            def eval():                                              #Function for when points button is clicked 
                evaltxt.delete("1.0","end")
                
                evaltxt.insert(INSERT,points)
                value=evaltxt.get("1.0","end")
                value=int(value)
                point.append(value)
                comp.append(sel)
                for i in range(0,listeval1.size()):
                    k=listeval1.get(i)
                    ind.append(k)
                
                
            def compare():                                            #For comparing points of two teams
    
                root=Toplevel()
                root.geometry("500x300")
                root.title("FINAL")
                back2=PhotoImage(file="back2.png")
                Label(root,image=back2).pack(side=TOP)
                finallab=Label(root,text="Team name",width=10,bg="white")
                finallab.place(x=10,y=10)
                finaltext=Text(root,width=15,height=1)
                finaltext.place(x=100,y=10)
                finallab1=Label(root,text="Team name",width=10,bg="white")
                finallab1.place(x=280,y=10)
                finaltext1=Text(root,width=15,height=1)
                finaltext1.place(x=370,y=10)
                finallab2=Label(root,text="Points",width=10,bg="white")
                finallab2.place(x=10,y=130)
                finaltext2=Text(root,width=15,height=1)
                finaltext2.place(x=100,y=130)
                finallab3=Label(root,text="Points",width=10,bg="white")
                finallab3.place(x=280,y=130)
                finaltext3=Text(root,width=15,height=1)
                finaltext3.place(x=370,y=130)
                
                if len(comp)==1 and len(point)==1 :                             #when only one team  is selected
                    root.destroy()
                    top2.destroy()
                    messagebox.showinfo("Error","Only one team selected\nEvaluate again")
                elif comp[0]==comp[1]:                                            #when team is already selected
                    root.destroy()
                    top2.destroy()
                    messagebox.showinfo("Repeat Action","Team is already selected\nEvaluate again")
                    
                else:
                    
                    mys11="SELECT playername FROM team WHERE teamname='" + comp[0] + "';"
            
                    mycursor.execute(mys11)
                    result = mycursor.fetchall()
                    
                    for i,j in zip(result,range(0,len(ind))):
                        i =  ''.join(i)
                        mys22="INSERT INTO teams2(name,players,value) VALUE(%s,%s,%s)"
                        val=(comp[0],i,ind[j])
                        mycursor.execute(mys22,val)
                        curs.commit()
                    mys12="SELECT playername FROM team WHERE teamname='" + comp[1] + "';"
            
                    mycursor.execute(mys12)
                    result = mycursor.fetchall()
                    for i,j in zip(result,range(11,len(ind))):
                        i =  ''.join(i)
                        mys21="INSERT INTO teams2(name,players,value) VALUE(%s,%s,%s)"
                        val=(comp[1],i,ind[j])
                        mycursor.execute(mys21,val)
                        curs.commit()
                    
                    finaltext.insert(INSERT,comp[0])
                    finaltext1.insert(INSERT,comp[1])
                    finaltext2.insert(INSERT,point[0])
                    finaltext3.insert(INSERT,point[1])
                
                    c="Team "+" "+comp[0]+" "+"Won"
                    c1="Team "+" "+comp[1]+" "+"Won"
                    if point[0]>point[1]:
                        messagebox.showinfo(" Congratulations! ",c)
                        finalmys="INSERT INTO final1(team,points,status) VALUE(%s,%s,%s)"                        #Inserting into database
                        val=(comp[0],point[0],"won")
                        mycursor.execute(finalmys,val)
                        curs.commit()
                        finalmys1="INSERT INTO final1(team,points,status) VALUE(%s,%s,%s)"
                        val=(comp[1],point[1],"lost")
                        mycursor.execute(finalmys1,val)
                        curs.commit()   
                        
                    else:
                        messagebox.showinfo("Congratulations! \nTeam ",c1)
                        finalmys="INSERT INTO final1(team,points,status) VALUE(%s,%s,%s)"
                        val=(comp[0],point[0],"lost")
                        mycursor.execute(finalmys,val)
                        curs.commit()
                        finalmys1="INSERT INTO final1(team,points,status) VALUE(%s,%s,%s)"
                        val=(comp[1],point[1],"won")
                        mycursor.execute(finalmys1,val)
                        curs.commit()   
                    def exit():                                                                           #When exit button is clicked
                        MsgBox =messagebox.askquestion ('Exit Application','Are you sure you want to exit the screen',icon = 'warning')
                        if MsgBox == 'yes':
                    
                            root.destroy()
                            top2.destroy()
                        else:
                    
                            messagebox.showinfo('Return','You will now return to the application screen')
                    exitbutton=Button(root,text="Exit",width=15,command=exit)
                    exitbutton.place(x=200,y=260)
                comp.clear()
                point.clear()
                ind.clear()
                root.mainloop()
        
                
                
                
            evalbut=Button(top2,text="Points",width=15,command=eval,bg="white")
            evalbut.place(x=30,y=470)
            evalbut2=Button(top2,text="Evaluate",width=15,command=compare,bg="white")
            evalbut2.place(x=300,y=470)
            
            tot1.clear()
            tot.clear()
            
            
                
        optionVar.trace('w',select)
        

        top2.mainloop()
    def help():                                     #Function when help option is selected
        
        top3=Toplevel()
        top3.geometry("1500x1500")
        top3.title("Help")
        back1=PhotoImage(file="back.png")
        Label(top3,image=back1).pack(side=TOP)
        string="Welcome to cricket fantasy game!\n\n\nThis Quarantine ,let us stop missing our criket matches and go back to the times where we predicted how well team would perform wuth the given players!\nLet's become the master-planners,so that after quarantine we can have the best teams!! "
        help1=Label(top3,text=string,bg="white",font="Broadway")
        help1.place(x=10,y=10)
        string1="->HOW TO PLAY\n"
        help2=Label(top3,text=string1,bg="white",font=("Forte",19,"bold"))
        help2.place(x=10,y=150)
        string2="***Click on Start game\n***Go to Team and select New Team until then all options are disabled and then enter a team name and create your own team\n***Save your team\n***Go to evaluate team and choose your team and any other team and click on evaluate,according to player's selection team will be evaluated\n***There is a section of profiles where you can see the players's profile and information about them.  "
        help3=Label(top3,text=string2,bg="white",font="Broadway")
        help3.place(x=10,y=200)
        top3.mainloop()
    def profile():                                #Function when profile option is selected
        top5=Toplevel()
        top5.geometry("1500x1000")
        top5.title("Profiles")
        back=PhotoImage(file="back.png")
        pro=PhotoImage(file="virat kohli.png")
        pro1=PhotoImage(file="rohit sharma.png")
        pro2=PhotoImage(file="ms dhoni.png")
        pro3=PhotoImage(file="kl rahul.png")
        pro4=PhotoImage(file="hardik pandya.png")
        pro5=PhotoImage(file="bhuwaneshwar.png")
        pro6=PhotoImage(file="Dinesh-Karthik.png")
        pro7=PhotoImage(file="Shikar Dhawan.png")
        pro8=PhotoImage(file="Jasprit-Bumrah.png")
        pro9=PhotoImage(file="Kedar-Jadhav.png")
        pro10=PhotoImage(file="Kuldeep-Yadav.png")
        pro11=PhotoImage(file="Mayank Agarwal.png")
        pro12=PhotoImage(file="Mohammed shami.png")
        pro13=PhotoImage(file="Yuvendra Chahal.png")
        pro14=PhotoImage(file="Prithvi Shaw.png")
        pro15=PhotoImage(file="Ravindra-Jadeja.png")
        pro16=PhotoImage(file="A Rahane.png")
        pro17=PhotoImage(file="S Iyer.png")
        pro18=PhotoImage(file="Manish Pandey.png")
        pro19=PhotoImage(file="Yuvraj Singh.png")
        pro20=PhotoImage(file="R Ashwin.png")
        def wiki(name):                               #Importing information from wikipedia
            window=Toplevel()
            window.geometry("1500x1500")
            window.title("Information")
            #back=PhotoImage(file="back.png")
            #frame = Frame(window, height=200, width=200)
            #frame.pack(side=LEFT, fill=BOTH)
            #Label(window,image=back).pack(side=TOP)
            z = Label(window,text=wikipedia.page(name).content)
            
            z.pack(side=TOP, fill=BOTH)
            
            
            top5.destroy()
            window.mainloop()
        Label(top5,image=back).pack(side=TOP)
        play1=Label(top5,width=90,image=pro,bg="snow")
        play1.place(x=5,y=5)
        play2=Label(top5,text="Virat Kohli\nBatsman",font=('Helvetica', 11, 'bold'),bg="snow")
        play2.place(x=100,y=5)
        infobut=Button(top5,width=7,text="More Info",command=lambda: wiki("Virat Kohli"),bg="snow" )
        infobut.place(x=100,y=110)
        play3=Label(top5,width=90,image=pro1,bg="snow")
        play3.place(x=5,y=150)
        play4=Label(top5,width=10,text="Rohit Sharma\nBatsman",font=('Helvetica', 11, 'bold'),bg="snow")
        play4.place(x=100,y=150)
        infobut1=Button(top5,width=7,text="More Info",command=lambda: wiki("Rohit Sharma"),bg="snow")
        infobut1.place(x=100,y=255)
        play5=Label(top5,width=90,image=pro2,bg="snow")
        play5.place(x=5,y=290)
        play6=Label(top5,width=21,text="Mahendra Singh Dhoni\nWicket Keeper",font=('Helvetica', 11, 'bold'),bg="snow")
        play6.place(x=100,y=290)
        infobut2=Button(top5,width=7,text="More Info",command=lambda: wiki("Mahendra Singh Dhoni"),bg="snow")
        infobut2.place(x=100,y=380)
        play7=Label(top5,width=90,image=pro3,bg="snow")
        play7.place(x=5,y=420)

        play8=Label(top5,width=11,text="KL Rahul\nWicket Keeper",font=('Helvetica', 11, 'bold'),bg="snow")
        play8.place(x=100,y=420)
        infobut3=Button(top5,width=7,text="More Info",command=lambda: wiki("KL  Rahul"),bg="snow")
        infobut3.place(x=100,y=500)
        play9=Label(top5,width=90,image=pro4,bg="snow")
        play9.place(x=5,y=550)
        play10=Label(top5,width=12,text="Hardik Pandya\nAll Rounder",font=('Helvetica', 11, 'bold'),bg="snow")
        play10.place(x=100,y=550)
        infobut4=Button(top5,width=7,text="More Info",command=lambda: wiki("Hardik Pandya"),bg="snow")
        infobut4.place(x=100,y=640)
        play11=Label(top5,width=90,image=pro5,bg="snow")
        play11.place(x=380,y=5)
        play12=Label(top5,width=17,text="Bhuvneshwar Kumar\nBowler",font=('Helvetica', 11, 'bold'),bg="snow")
        play12.place(x=500,y=5)
        infobut5=Button(top5,width=7,text="More Info",command=lambda: wiki("Bhuvneshwar Kumar"),bg="snow")
        infobut5.place(x=500,y=100)
        play13=Label(top5,width=90,image=pro6,bg="snow")
        play13.place(x=380,y=150)
        play14=Label(top5,width=15,text="Dinesh Karthik\nWicket Keeper",font=('Helvetica', 11, 'bold'),bg="snow")
        play14.place(x=500,y=150)
        infobut6=Button(top5,width=7,text="More Info",command=lambda: wiki("Dinesh Karthik"),bg="snow")
        infobut6.place(x=500,y=245)
        play15=Label(top5,width=90,image=pro7,bg="snow")
        play15.place(x=380,y=290)
        play16=Label(top5,width=15,text="Shikhar Dhawan\nBowler",font=('Helvetica', 11, 'bold'),bg="snow")
        play16.place(x=500,y=290)
        infobut7=Button(top5,width=7,text="More Info",command=lambda: wiki("Shikhar Dhawan"),bg="snow")
        infobut7.place(x=500,y=380)
        play17=Label(top5,width=90,image=pro8,bg="snow")
        play17.place(x=380,y=440)
        play18=Label(top5,width=15,text="Jasprit Bumrah\nBowler",font=('Helvetica', 11, 'bold'),bg="snow")
        play18.place(x=500,y=440)
        infobut8=Button(top5,width=7,text="More Info",command=lambda: wiki("Jasprit Bumrah"),bg="snow")
        infobut8.place(x=500,y=530)
        play19=Label(top5,width=90,image=pro9,bg="snow")
        play19.place(x=380,y=580)
        play20=Label(top5,width=15,text="Kedar Jadhav\nBatsman",font=('Helvetica', 11, 'bold'),bg="snow")
        play20.place(x=500,y=580)
        infobut9=Button(top5,width=7,text="More Info",command=lambda: wiki("Kedar Jadhav"),bg="snow")
        infobut9.place(x=500,y=660)
        play21=Label(top5,width=90,image=pro10,bg="snow")
        play21.place(x=750,y=5)
        play22=Label(top5,width=15,text="Kuldeep Yadav\nBowler",font=('Helvetica', 11, 'bold'),bg="snow")
        play22.place(x=850,y=5)
        infobut10=Button(top5,width=7,text="More Info",command=lambda: wiki("Kuldeep Yadav"),bg="snow")
        infobut10.place(x=850,y=80)
        play23=Label(top5,width=90,image=pro11,bg="snow")
        play23.place(x=750,y=150)
        play24=Label(top5,width=15,text="Mayank Agarwal\nBatsman",font=('Helvetica', 11, 'bold'),bg="snow")
        play24.place(x=850,y=150)
        infobut11=Button(top5,width=7,text="More Info",command=lambda: wiki("Mayank Agarwal"),bg="snow")
        infobut11.place(x=850,y=220)
        play25=Label(top5,width=90,image=pro12,bg="snow")
        play25.place(x=750,y=290)
        play26=Label(top5,width=15,text="Mohammed Shami\nBowler",font=('Helvetica', 11, 'bold'),bg="snow")
        play26.place(x=850,y=290)
        infobut12=Button(top5,width=7,text="More Info",command=lambda: wiki("Mohammed Shami"),bg="snow")
        infobut12.place(x=850,y=360)
        play27=Label(top5,width=90,image=pro13,bg="snow")
        play27.place(x=750,y=420)
        play28=Label(top5,width=15,text="Yuzvendra Chahal\nBowler",font=('Helvetica', 11, 'bold'),bg="snow")
        play28.place(x=850,y=420)
        infobut13=Button(top5,width=7,text="More Info",command=lambda: wiki("Yuzvendra Chahal"),bg="snow")
        infobut13.place(x=850,y=500)
        play29=Label(top5,width=90,image=pro14,bg="snow")
        play29.place(x=750,y=550)
        play30=Label(top5,width=15,text="Prithvi Shaw\nBowler",font=('Helvetica', 11, 'bold'),bg="snow")
        play30.place(x=850,y=550)
        infobut14=Button(top5,width=7,text="More Info",command=lambda: wiki("Prithvi Shaw"),bg="snow")
        infobut14.place(x=850,y=640)
        play31=Label(top5,width=90,image=pro15,bg="snow")
        play31.place(x=1000,y=5)
        play32=Label(top5,width=15,text="Ravindra Jadeja\nAll Rounder",font=('Helvetica', 11, 'bold'),bg="snow")
        play32.place(x=1090,y=5)
        infobut15=Button(top5,width=7,text="More Info",command=lambda: wiki("Ravindra Jadeja"),bg="snow")
        infobut15.place(x=1090,y=80)
        play33=Label(top5,width=90,image=pro16,bg="snow")
        play33.place(x=1000,y=150)
        play34=Label(top5,width=15,text="A Rahane\nBatsman",font=('Helvetica', 11, 'bold'),bg="snow")
        play34.place(x=1090,y=150)
        infobut16=Button(top5,width=7,text="More Info",command=lambda: wiki("A Rahane"),bg="snow")
        infobut16.place(x=1090,y=220)
        play35=Label(top5,width=90,image=pro17,bg="snow")
        play35.place(x=1000,y=290)
        play36=Label(top5,width=15,text="S Iyer\nBatsman",font=('Helvetica', 11, 'bold'),bg="snow")
        play36.place(x=1100,y=290)
        infobut17=Button(top5,width=7,text="More Info",command=lambda: wiki("S Iyer"),bg="snow")
        infobut17.place(x=1110,y=360)
        play37=Label(top5,width=90,image=pro19,bg="snow")
        play37.place(x=1000,y=420)
        play38=Label(top5,width=15,text="Yuvraj Singh\nAll Rounder",font=('Helvetica', 11, 'bold'),bg="snow")
        play38.place(x=1100,y=420)
        infobut18=Button(top5,width=7,text="More Info",command=lambda: wiki("Yuvraj Singh"),bg="snow")
        infobut18.place(x=1110,y=500)
        play39=Label(top5,width=90,image=pro20,bg="snow")
        play39.place(x=1000,y=550)
        play40=Label(top5,width=15,text="R Ashwin\nAll Rounder",font=('Helvetica', 11, 'bold'),bg="snow")
        play40.place(x=1090,y=550)
        infobut19=Button(top5,width=7,text="More Info",command=lambda: wiki("R Ashwin"),bg="snow")
        infobut19.place(x=1090,y=620)
        top5.mainloop()
    def score():                                        #showing the points and status
        score=Toplevel()
        score.title("SCORECARD")
        score.geometry("1500x1500")
        
        curs=mysql.connector.connect(host="localhost",user="root",passwd="",db="fantasy")
        mycursor=curs.cursor()
        
        scorelab1=Label(score,width=15,text="Team name")
        scorelab1.grid(row=0,column=0)
        scorelab2=Label(score,width=15,text="Point")
        scorelab2.grid(row=0,column=1)
        scorelab3=Label(score,width=15,text="Status")
        scorelab3.grid(row=0,column=2)
        
        #mycursor.execute("SELECT teamno FROM final ORDER BY teamno DESC LIMIT 1")
        #scoreresult1= mycursor.fetchone()
        #scoreresult1=scoreresult1[0]
        mycursor.execute("SELECT * FROM final1 ORDER BY teamno DESC LIMIT 2")
        scoreresult=mycursor.fetchall()
        for i,j in zip(scoreresult,range(0,3)):
            
            
            Label(score,text=i[1]).grid(row=j+1,column=0)
            Label(score,text=i[2]).grid(row=j+1,column=1)
            Label(score,text=i[3]).grid(row=j+1,column=2)
            
        
        score.mainloop()    
        
    def exit():
        
        MsgBox =messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
   
            top1.destroy()
        else:
                    
            messagebox.showinfo('Return','You will now return to the application screen')
        

    
    menubar = Menu(top1)                                                       #Placing widgets
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Team", command=new)
    filemenu.add_command(label="Evaluate Team", command=evaluate)
    filemenu.add_command(label="Save Team", command=save)
    filemenu.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="Team", menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    #helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=help)
    menubar.add_cascade(label="Help", menu=helpmenu)
    profilemenu = Menu(menubar, tearoff=0)
    profilemenu.add_command(label="Profiles", command=profile)
    
    menubar.add_cascade(label="Profile Info", menu=profilemenu)
    tablemenu = Menu(menubar, tearoff=0)
    tablemenu.add_command(label="Scores and Status", command=score)
    
    menubar.add_cascade(label="Scorecard", menu=tablemenu)

    top1.config(menu=menubar)
    l=Label(top1,width=10,text="Team name:",font=("bold"),bg="LightCyan3",fg="white")
    l.place(x=10,y=10)
    #top1.wm_attributes('-transparentcolor','LightCyan3')
    
    e=Entry(top1,width=20,state=DISABLED)
    e.place(x=120,y=10)
    curs=mysql.connector.connect(host="localhost",user="root",passwd="",db="fantasy")
    mycursor=curs.cursor()
    mycursor.execute("SELECT name FROM login ORDER BY no DESC LIMIT 1")
    user= mycursor.fetchone()
    user=user[0]
    curs.commit()
    username=Label(top1,text="Username: %s" %user,width=20,fg="white",bg="LightCyan3",font=("bold"))
    username.place(x=450,y=10)
    can=Canvas(top1,width=570,height=80,bg="lavender",relief="groove",highlightcolor="black")
    can.place(x=5,y=40)
    pointlab=Label(can,width=12,text="Your Selection:",bg="lavender",font=("bold"))
    pointlab.place(x=5,y=8)
    batimg=Label(can,image=batimage)
    batimg.place(x=5,y=35)
    bat=Label(can,width=9,text="Batsman",bg="lavender")
    bat.place(x=45,y=35)
    bat1=Entry(can,width=3,state=DISABLED)
    bat1.place(x=110,y=35)
    ballimg=Label(can,image=ballimage)
    ballimg.place(x=145,y=35)
    bowl=Label(can,width=7,text="Bowler",bg="lavender")
    bowl.place(x=190,y=35)
    bowl1=Entry(can,width=3,state=DISABLED)
    bowl1.place(x=240,y=35)
    arimg=Label(can,image=arimage)
    arimg.place(x=270,y=35)
    ar=Label(can,width=9,text="AllRounder",bg="lavender")
    ar.place(x=310,y=35)
    ar1=Entry(can,width=3,state=DISABLED)
    ar1.place(x=380,y=35)
    wicketimg=Label(can,image=wicketimage)
    wicketimg.place(x=415,y=35)
    wk=Label(can,width=10,text="WicketKeeper",bg="lavender")
    wk.place(x=460,y=35)
    wk1=Entry(can,width=3,state=DISABLED)
    wk1.place(x=540,y=35)
    
    var = IntVar()
    R1 = Radiobutton(top1, text="BAT",variable=var,value=1,command=r1,state=DISABLED,width=5,height=1,bg="lavender")
    
    R2 = Radiobutton(top1, text="BWL", variable=var, value=2,command=r2,state=DISABLED,width=5,height=1,bg="lavender")
    R3 = Radiobutton(top1, text="AR",variable=var,value=3,state=DISABLED,command=r3,width=5,height=1,bg="lavender")
    R4 = Radiobutton(top1, text="WK",variable=var,value=4,state=DISABLED,command=r4,width=5,height=1,bg="lavender")

    R1.place(x=10,y=130)
  
    R2.place(x=70,y=130)
    
    R3.place(x=130,y=130)
    R4.place(x=180,y=130)

    
    lb.place(x=10,y=160)
    
    lb1.place(x=250,y=160)
    messagebox.showinfo("Info","Select team and make new team")

    top1.mainloop()
def submit():                       #function for submitting name and number 
    if len(nametxt.get())==0 :
        messagebox.showinfo("Empty","Enter Your Name")
        nametxt.delete(0,END)
    elif len(numtxt.get())==0:
        messagebox.showinfo("Empty","Enter Your Number")
        numtxt.delete(0,END)
    elif len(numtxt.get())!=10:
        messagebox.showinfo("Length","Enter 10 digit numbers")
        numtxt.delete(0,END)
    elif (not numtxt.get().isnumeric()):
        messagebox.showinfo("Empty","Enter only numbers")
        numtxt.delete(0,END)
    else:
        
        curs=mysql.connector.connect(host="localhost",user="root",passwd="",db="fantasy")
        mycursor=curs.cursor()
        sub="INSERT INTO login(name,number) VALUE(%s,%s)"
        val=(nametxt.get(),numtxt.get())
        mycursor.execute(sub,val)
        curs.commit()
        messagebox.showinfo("Successful","Submitted Successfully\nNow you can start the game")
        b=Button(top,width=15,text="Start game",command=click1,bg="black",height=1,font=("Broadway",15,"bold"),fg="red")
        b.place(x=360,y=650)
    
        
    


Label(top,image=imga).pack(side=TOP)
Label(top,image=font).place(x=350,y=10)

#b=Button(top,width=15,text="Start game",command=click1,bg="black",height=1,font=("Broadway",15,"bold"),fg="red")
#b.place(x=360,y=650)
name=Label(top,width=10,text="NAME",bg="black",fg="red",font=("Broadway",12,"bold"))
name.place(x=20,y=300)
num=Label(top,width=10,text="NUMBER",bg="black",fg="red",font=("Broadway",12,"bold"))
num.place(x=20,y=370)
nametxt=Entry(top,width=20)
nametxt.place(x=160,y=300)
numtxt=Entry(top,width=20)
numtxt.place(x=160,y=370)
submit=Button(top,width=15,text="Submit",command=submit,bg="black",height=1,font=("Broadway",15,"bold"),fg="red")
submit.place(x=360,y=520)

top.mainloop()
