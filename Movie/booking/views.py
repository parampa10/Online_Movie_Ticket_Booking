from django.shortcuts import render
from movieupdate.models import Movie
from booking.models import Seat
import datetime
# Create your views here.
def booknow_view(request):
    if request.method == 'POST':
        movies=Movie.objects.all()
        for m in movies:
            if request.POST.get(m.moviename):
                selection=m.moviename  
                x = datetime.datetime.now()            
                date=x.day
                y = x + datetime.timedelta(days = 1)
                z = x + datetime.timedelta(days = 2)
                w = x + datetime.timedelta(days = 3) 
                date1=y.day
                date2=z.day
                date3=w.day
                month=x.month
                year=x.year
                slot=[9,10,11,12,13,14,15,16,17,18,19,20,21,22]
                return render(request,'booking.html',{'selection' : selection,'slot':slot,'date':date,'date1':date1,'date2':date2,'date3':date3,'month':month,'year':year })

def timecheck_view(request):
    if request.method == 'POST':
        movie= str(request.POST["movie"])
        radiotime = int(str(request.POST["time"])) 
        radioday = int(str(request.POST["date"]))
        x= datetime.datetime.now()
        if x.day==radioday :
            if x.hour < radiotime:
                return render(request,'seat.html',{'date': radioday,'movie':movie,'time':radiotime })
            else:
                invalidmsg="select proper date and time"
                return render(request,'wrong.html',{'invalidmsg' : invalidmsg})
        else:
            return render(request,'seat.html',{'date': radioday,'movie':movie,'time':radiotime })
        
def seat_view(request):
    if request.method == "POST":
        movie=str(request.POST["movie"])
        date=int(request.POST["date"])
        time=int(str(request.POST["time"])) 
        row=int(request.POST["row"])
        column=int(request.POST["column"])    
        flag=0
        username=request.user.username
        seats=Seat.objects.all()
        if seats is None :
            m=Seat(moviename=movie,date=date,time=time,username=username,row=row,column=column)
            m.save()
            done="booked 1 ticket!!"
            return render(request,'seat.html',{'done':done,'movie':movie,'date':date,'time':time})

        else:
            for s in seats:
               
                if(s.moviename==movie  and int(s.date)==date and int(s.time)==time and int(s.row)==row and int(s.column)==column):
                   
                    msg="SEAT ALREADY BOOKED "
                    flag=1
                    return render(request,'seat.html',{'msg':msg,'movie':movie,'date':date,'time':time})
                    
            if flag != 1:
                done="1 ticket booked!!"
                m=Seat(moviename=movie,date=date,time=time,username=username,row=row,column=column)
                m.save()
                return render(request,'seat.html',{'done':done,'movie':movie,'date':date,'time':time})

def show_ticket_view(request):
    if request.method == 'POST':
        movie=str(request.POST["moviename"])
        date=int(request.POST["date"])
        time=int(request.POST["time"])
        username=request.user.username
        count=0
        row=[]
        column=[]
        seats=Seat.objects.all()
        for s in seats:
            if(s.username==username and s.date==date and s.time==time and s.moviename==movie):
                row.append(s.row)
                column.append(s.column)
                count=count+1
        
        if(row == None):
            notdone="TICKETS ARE NOT BOOKED"
         
            return render(request,'done.html',{'row':row,'column':column,'notdone':notdone})
        else:
            price=0
            x= datetime.datetime.now()
            month=x.month
            year=x.year
            for r in row:
                if(int(r)<7):
                    price=price + 200
                else:
                    price=price + 150
                
            done="TICKETS ARE BOOKED!"
            return render(request,'done.html',{'row':row,'column':column,'done':done,'price':price,'movie':movie,'date':date,'time':time,'month':month,'year':year })
                

        

