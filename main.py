from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton,MDIconButton,MDFlatButton,MDFillRoundFlatIconButton,MDRoundFlatIconButton
from kivymd.toast import toast
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.datatables import MDDataTable
import mysql.connector as sql
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDTimePicker
from kivy.metrics import dp#importing display pixles
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
import datetime
import csv

screen_helper="""
ScreenManager:
    Screen1Screen:
        name:'scr1'
    ViewAllScreen:
        name:'view'
    FilterScreen:
        name:'filter'
    Filter1Screen:
        name:'filter_data'
    UpdateScreen:
        name:'upd'
    DelrowScreen:
        name:'drow'
        
<Screen1Screen>:
    name:'scr1'

    ScrollView:
        do_scroll_x: False
        do_scroll_y: True

        GridLayout:
            cols:2
            padding:10,10
            spacing:10,10
            size_hint_y:None
            height:self.minimum_height
            row_default_height:30

            MDLabel:
            MDLabel:
            MDLabel:
            MDLabel:

            MDTextField:
                id:airline
                hint_text: "Airline Name:"
                helper_text: ""
                required:True
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDTextField:
                id:flight_no
                hint_text: "Flight Number:"
                helper_text: ""
                required:True
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDTextField:
                id:arr_time
                hint_text: "Arrival Time:"
                helper_text: ""
                required:True
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDIconButton:
                id:arr
                icon:"airplane-clock"
                on_press:app.arrival_time()

            MDTextField:
                id:dep_time
                hint_text: "Departure Time:"
                helper_text: ""
                required:True
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDIconButton:
                id:dep
                icon:"airplane-clock"
                on_press:app.depart_time()

            MDLabel:

            MDTextField:
                id:to
                hint_text: "Destination:"
                helper_text: ""
                required:True
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDTextField:
                id:arr_runway
                hint_text: "Arrival Runway:"
                input_filter:'int'
                required:True
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDTextField:
                id:dep_runway
                hint_text: "Departure Runway:"
                input_filter:'int'
                required:True
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDTextField:
                id:passengers
                hint_text: "No of passengers:"
                input_filter:'int'
                required:True
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
            MDLabel:
            MDLabel:

            MDFillRoundFlatIconButton:
                id:submit
                icon:"database-arrow-up"
                text:"UPLOAD DATA"
                on_press:app.get_all()

            MDFillRoundFlatIconButton:
                icon:"database-eye"
                text:"View All"
                on_press:app.chscr('view')

            MDLabel:

            MDFillRoundFlatIconButton:
                icon:"database-search"
                text:"Filter"
                on_press:app.chscr('filter')

            MDLabel:

            MDFillRoundFlatIconButton:
                icon:"database-edit"
                text:"Update Status"
                on_press:app.chscr('upd')

            MDLabel:

            MDFillRoundFlatIconButton:
                icon:"database-remove"
                text:"Remove row(s)"
                on_press:app.chscr('drow')

            MDLabel:

            MDFillRoundFlatIconButton:
                icon:"database-off"
                text:"Delete All"
                on_press:app.delete_all()

    BoxLayout:

        orientation:'vertical'

        MDTopAppBar:
            title:'Flight Management System'

        MDLabel:

<ViewAllScreen>:

    name:'view'

    BoxLayout:

        orientation:'vertical'

        MDTopAppBar:
            title:'View All the stored Data'
            left_action_items:[["chevron-left",lambda x:app.chscr('scr1')]]

        MDLabel:

<FilterScreen>:
    name:'filter'

    ScrollView:
        do_scroll_x: False
        do_scroll_y: True

        GridLayout:
            cols:1
            padding:10,10
            spacing:10,10
            size_hint_y:None
            height:self.minimum_height
            row_default_height:30

            MDLabel:
            MDLabel:

            MDTextField:
                id:line_fil
                hint_text: "Airline Name:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:flight_fil
                hint_text: "Flight number:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:arr_fil
                hint_text: "Arrival Time:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:arrun_fil
                hint_text: "Arrival Runway:"
                helper_text: ""
                input_filter:'int'
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:dep_fil
                hint_text: "Departure Time:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:deprun_fil
                hint_text: "Departure Runway:"
                helper_text: ""
                input_filter:'int'
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:passenger_fil
                hint_text: "No of Passengers:"
                helper_text: ""
                input_filter:'int'
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:dest_fil
                hint_text: "Destination:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:status_fil
                hint_text: "Status:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDFillRoundFlatButton:
                id:search
                text:"SEARCH"
                on_release:app.chscr('filter_data')
                on_release:root.initiate()

    BoxLayout:

        orientation:'vertical'

        MDTopAppBar:
            title:'Filter data according to:'
            left_action_items:[["chevron-left",lambda x:app.chscr('scr1')]]

        MDLabel:

<Filter1Screen>:

    name:'filter_data'

    BoxLayout:

        orientation:'vertical'

        MDTopAppBar:
            title:'Result:'
            left_action_items:[["chevron-left",lambda x:app.reset()]]

        MDLabel:

<UpdateScreen>:
    name:'upd'

    ScrollView:
        do_scroll_x: False
        do_scroll_y: True

        GridLayout:
            cols:1
            padding:10,10
            spacing:10,10
            size_hint_y:None
            height:self.minimum_height
            row_default_height:30

            MDLabel:
            MDLabel:
            MDLabel:
                text:"NEW VALUE"
                bold:True
                font_style:"H5"

            MDTextField:
                id:line_new
                hint_text: "Airline Name:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:arr_new
                hint_text: "Arrival Time:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:arrun_new
                hint_text: "Arrival Runway:"
                helper_text: ""
                input_filter:'int'
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:dep_new
                hint_text: "Departure Time:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:deprun_new
                hint_text: "Departure Runway:"
                helper_text: ""
                input_filter:'int'
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:passenger_new
                hint_text: "No of Passengers:"
                helper_text: ""
                input_filter:'int'
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:dest_new
                hint_text: "Destination:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"OR"

            MDTextField:
                id:status_new
                hint_text: "Status:"
                helper_text: "Approaching/Delayed/Cancelled/Arrived/Departed/Maintenance"
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDLabel:
                text:"WHERE?"
                bold:True
                font_style:"H5"

            MDTextField:
                id:flight_ref
                hint_text: "Flight Number:"
                helper_text: ""
                helper_text_mode: "on_focus"
                size_hint_x: None
                width: 400

            MDFillRoundFlatButton:
                id:update
                text:"UPDATE"
                on_release:root.updt()

    BoxLayout:

        orientation:'vertical'

        MDTopAppBar:
            title:'Filter data according to:'
            left_action_items:[["chevron-left",lambda x:app.chscr('scr1')]]

        MDLabel:

<DelrowScreen>:
    name:'drow'

    MDLabel:
    MDLabel:

    MDTextField:
        id:flightno_del
        hint_text: "Flight Number to be deleted"
        helper_text: ""
        helper_text_mode: "on_focus"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint_x: None
        width: 400

    MDFillRoundFlatButton:
        id:delrow
        text:"DELETE"
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_release:root.dialogbox()

    BoxLayout:

        orientation:'vertical'

        MDTopAppBar:
            title:'Delete a Row:'
            left_action_items:[["chevron-left",lambda x:app.chscr('scr1')]]

        MDLabel:
    
"""

class Screen1Screen(Screen):
    pass
class ViewAllScreen(Screen):
    
    def load_table(self):
        cursor.execute("SELECT * FROM fms")
        data=cursor.fetchall()
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
        pos_hint={'center_y': 0.5, 'center_x': 0.5},
        size_hint=(0.9, 0.6),
        use_pagination=True,
        column_data=[
            ("Airline", dp(30)),
            ("Flight Number", dp(30)),
            ("Arrival Time", dp(30)),
            ("Arrival Runway", dp(30)),
            ("Departure Time", dp(30)),
            ("Departure Runway", dp(30)),
            ("Passengers", dp(30)),
            ("Destination", dp(30)),
            ("Status", dp(30))],
        row_data=data)
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()

class FilterScreen(Screen):
    def initiate(self):
        airline=self.ids.line_fil.text
        flight_no=self.ids.flight_fil.text
        arr_tm=self.ids.arr_fil.text
        arr_run=self.ids.arrun_fil.text
        dep_tm=self.ids.dep_fil.text
        dep_run=self.ids.deprun_fil.text
        passenger=self.ids.passenger_fil.text
        dest=self.ids.dest_fil.text
        status=self.ids.status_fil.text
        if airline==flight_no==arr_tm==arr_run==dep_tm==dep_run==passenger==dest==status=="":
            toast("Query is empty")
        else:
            if airline!="":
                q="SELECT * FROM fms WHERE Airline=%s"
                val=(airline,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            elif flight_no!="":
                q="SELECT * FROM fms WHERE Flight_no=%s"
                val=(flight_no,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            elif arr_tm!="":
                q="SELECT * FROM fms WHERE Arrival_time=%s"
                val=(arr_tm,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            elif arr_run!="":
                q="SELECT * FROM fms WHERE Arrival_runway=%s"
                val=(arr_run,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            elif dep_tm!="":
                q="SELECT * FROM fms WHERE Departure_time=%s"
                val=(dep_tm,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            elif dep_run!="":
                q="SELECT * FROM fms WHERE Departure_runway=%s"
                val=(dep_run,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            elif passenger!="":
                q="SELECT * FROM fms WHERE Passengers=%s"
                val=(passenger,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            elif dest!="":
                q="SELECT * FROM fms WHERE Destination=%s"
                val=(dest,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            elif status!="":
                q="SELECT * FROM fms WHERE Status=%s"
                val=(status,)
                cursor.execute(q,val)
                result=cursor.fetchall()
            f=open("query.csv",'w',newline='',encoding='utf-8')
            writer = csv.writer(f)
            writer.writerows(result)
            f.close()

class Filter1Screen(Screen):
    def load_table(self):
        f=open("query.csv",mode='r',encoding="utf-8")
        reader = csv.reader(f, delimiter=',')
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
        pos_hint={'center_y': 0.5, 'center_x': 0.5},
        size_hint=(0.9, 0.6),
        use_pagination=True,
        column_data=[
            ("Airline", dp(30)),
            ("Flight Number", dp(30)),
            ("Arrival Time", dp(30)),
            ("Arrival Runway", dp(30)),
            ("Departure Time", dp(30)),
            ("Departure Runway", dp(30)),
            ("Passengers", dp(30)),
            ("Destination", dp(30)),
            ("Status", dp(30))],
        row_data=reader)
        self.add_widget(self.data_tables)
        f.close()
        return layout
    def on_enter(self):
        self.load_table()

class UpdateScreen(Screen):
    def updt(self):
        airline=self.ids.line_new.text
        a_time=self.ids.arr_new.text
        a_run=self.ids.arrun_new.text
        d_time=self.ids.dep_new.text
        d_run=self.ids.deprun_new.text
        pas=self.ids.passenger_new.text
        dest=self.ids.dest_new.text
        stat=self.ids.status_new.text
        ref=self.ids.flight_ref.text
        if airline!="" and ref!="":
            try:
                q="UPDATE fms SET Airline=%s WHERE Flight_no=%s"
                val=(airline,ref)
                cursor.execute(q,val)
                db.commit()
                toast("Updated successfully")
            except:
                toast("Error encountered while updating")

        elif a_time!="" and ref!="":
            try:
                q="UPDATE fms SET Arrival_time=%s WHERE Flight_no=%s"
                val=(a_time,ref)
                cursor.execute(q,val)
                db.commit()
                toast("Updated successfully")
            except:
                toast("Error encountered while updating")

        elif a_run!="" and ref!="":
            try:
                q="UPDATE fms SET Arrival_runway=%s WHERE Flight_no=%s"
                val=(a_run,ref)
                cursor.execute(q,val)
                db.commit()
                toast("Updated successfully")
            except:
                toast("Error encountered while updating")

        elif d_time!="" and ref!="":
            try:
                q="UPDATE fms SET Departure_time=%s WHERE Flight_no=%s"
                val=(d_time,ref)
                cursor.execute(q,val)
                db.commit()
                toast("Updated successfully")
            except:
                toast("Error encountered while updating")

        elif d_run!="" and ref!="":
            try:
                q="UPDATE fms SET Departure_runway=%s WHERE Flight_no=%s"
                val=(d_run,ref)
                cursor.execute(q,val)
                db.commit()
                toast("Updated successfully")
            except:
                toast("Error encountered while updating")

        elif pas!="" and ref!="":
            try:
                q="UPDATE fms SET Passengers=%s WHERE Flight_no=%s"
                val=(pas,ref)
                cursor.execute(q,val)
                db.commit()
                toast("Updated successfully")
            except:
                toast("Error encountered while updating")

        elif dest!="" and ref!="":
            try:
                q="UPDATE fms SET Destination=%s WHERE Flight_no=%s"
                val=(dest,ref)
                cursor.execute(q,val)
                db.commit()
                toast("Updated successfully")
            except:
                toast("Error encountered while updating")

        elif stat in ["Approaching","Delayed","Cancelled","Arrived","Departed","Maintenance"] and ref!="":
            try:
                q="UPDATE fms SET Status=%s WHERE Flight_no=%s"
                val=(stat,ref)
                cursor.execute(q,val)
                db.commit()
                toast("Updated successfully")
            except:
                toast("Error encountered while updating")

class DelrowScreen(Screen):
    def dialogbox(self):
        fno=self.ids.flightno_del.text
        dclose_button=MDFlatButton(text="No",on_release=self.closedialog)#Dialogbox closing button
        conf=MDFlatButton(text="Yes",on_release=self.delte)
        self.dialog=MDDialog(title="Confirmation",text="Please confirm whether you want to delete data for flight number {}".format(fno),
                        size_hint=(0.7,1),
                        buttons=[dclose_button,conf])# creates a dialogbox
        self.dialog.open()#pops up the dialogbox on screen

    def closedialog(self,*args):
        self.dialog.dismiss()
        
    def delte(self,*args):
        fno=self.ids.flightno_del.text
        q="DELETE FROM fms WHERE Flight_no=%s"
        val=(fno,)
        cursor.execute(q,val)
        db.commit()
        self.closedialog()
        toast("Data for flight number {} deleted successfully".format(fno))

class FlightManagementApp(MDApp):

    def chscr(self,screen):
        self.screen.current=screen

    def arrival_time(self):
        cur=datetime.datetime.now()
        picker=MDTimePicker()
        picker.set_time(cur)
        picker.bind(on_cancel=self.arr_cancel,time=self.arr_get)
        picker.open()

    def arr_get(self,instance,time):
        scr=self.screen.get_screen('scr1')
        scr.ids.arr_time.text=str(time)

    def arr_cancel(self,instance,time):
        scr=self.screen.get_screen('scr1')
        scr.ids.arr_time.text="NULL"

    def depart_time(self):
        cur=datetime.datetime.now()
        picker=MDTimePicker()
        picker.set_time(cur)
        picker.bind(on_cancel=self.dep_cancel,time=self.dep_get)
        picker.open()

    def dep_get(self,instance,time):
        scr=self.screen.get_screen('scr1')
        scr.ids.dep_time.text=str(time)

    def dep_cancel(self,instance,time):
        scr=self.screen.get_screen('scr1')
        scr.ids.dep_time.text="NULL"

    def get_all(self):
        scr=self.screen.get_screen('scr1')
        airline=scr.ids.airline.text
        flight_no=scr.ids.flight_no.text
        arrival=scr.ids.arr_time.text
        departure=scr.ids.dep_time.text
        destination=scr.ids.to.text
        arr_runway=scr.ids.arr_runway.text
        dep_runway=scr.ids.dep_runway.text
        passenger_no=scr.ids.passengers.text
        if airline=="" or flight_no=="" or arrival=="" or departure=="" or destination=="" or arr_runway=="" or dep_runway=="" or passenger_no=="":
            toast("Blank inputs are not allowed")
        else:
            cursor.execute("SELECT * FROM fms")
            data=cursor.fetchall()
            cv=0
            if data!=[]:
                for i in data:
                    if i[2]==arrival and i[3]==int(arr_runway):
                        dia="Arrival time and arrival runway of new entry collides with the arrival time and arrival runway of an existing entry"
                        self.dialogbox(dia)
                        cv=0
                        break
                    elif i[2]==departure and i[3]==int(dep_runway):
                        dia="Departure time and departure runway of new entry collides with the arrival time and arrival runway of an existing entry"
                        self.dialogbox(dia)
                        cv=0
                        break
                    elif i[4]==arrival and i[5]==int(arr_runway):
                        dia="Arrival time and arrival runway of new entry collides with the departure time and departure runway of an existing entry"
                        self.dialogbox(dia)
                        cv=0
                        break
                    elif i[4]==departure and i[5]==int(dep_runway):
                        dia="Departure time and departure runway of new entry collides with the departure time and departure runway of an existing entry"
                        self.dialogbox(dia)
                        cv=0
                        break
                    elif i[1]==flight_no:
                        dia="Data already exists for the entered Flight number"
                        self.dialogbox(dia)
                        cv=0
                        break
                    else:
                        cv+=1
                        continue
                if cv==len(data):
                    cv=0
                    if arrival!=departure:
                        query="INSERT INTO fms VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        values=(airline,flight_no,arrival,int(arr_runway),departure,int(dep_runway),int(passenger_no),destination,"Approaching")
                        cursor.execute(query,values)
                        db.commit()
                        toast("Data stored to database successfully")
                    else:
                        toast("Arrival time and departure time of new entry are same")
            else:
                query="INSERT INTO fms VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values=(airline,flight_no,arrival,int(arr_runway),departure,int(dep_runway),int(passenger_no),destination,"Approaching")
                cursor.execute(query,values)
                db.commit()
                toast("Data stored to database successfully")

    def dialogbox(self,dialogtext):
        dclose_button=MDFlatButton(text="OK",on_release=self.closedialog)#Dialogbox closing button
        self.dialog=MDDialog(title="Warning",text=dialogtext,
                        size_hint=(0.7,1),
                        buttons=[dclose_button,])# creates a dialogbox
        self.dialog.open()#pops up the dialogbox on screen

    def closedialog(self,*args):
        self.dialog.dismiss()

    def on_start(self):
        try:
            global db,cursor
            db=sql.connect(host="localhost",user="root",password="s_1234",database='flight')
            cursor=db.cursor()
            toast("Connected to database successfully")
        except:
            toast("Failed to connect to database")

    def on_stop(self):
        db.close()

    def build(self):
        self.theme_cls.primary_palette="Amber"#box and button color
        self.screen=Builder.load_string(screen_helper)
        return self.screen

    def delete_all(self):
        dlog="Please confirm whether you want to delete EVERYTHING from the table"
        conf=MDFlatButton(text="Yes",on_release=self.deletedata)
        cancel=MDFlatButton(text="No",on_release=self.closedialog)
        self.dialog=MDDialog(title="Confirmation",text=dlog,size_hint=(0.7,1),buttons=[cancel,conf])
        self.dialog.open()

    def deletedata(self,*args):
        cursor.execute("DELETE FROM fms")
        db.commit()
        self.dialog.dismiss()
        toast("All data deleted successfully")

    def reset(self):
        f=open("query.csv",'w',newline='',encoding='utf-8')
        f.close()
        self.chscr('filter')

FlightManagementApp().run()
        
