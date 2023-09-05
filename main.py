
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.server_api import ServerApi

#connecting to fastapi to connect the webpage with MongoDB database
app=FastAPI()

@component
def Account_creation():
    ## Creating state
    alltodo = use_state([])
    User_name, set_user_name = use_state("")
    password, set_password = use_state("")
    First_name, set_firstname= use_state("")
    Last_name, set_lastname=use_state("")





    def submit(event):
        newtodo = {"User_name": User_name,"password": password}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  

    



    list = []
    def handle_event(event):
        print(event)
        
        
    #UI/UX design code of the webpage using html and css
    return html.div(
      {"style": 
         {  "padding": "60px",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "background_image":"url(https://i.pinimg.com/originals/f0/ce/74/f0ce7470cb89c23dfb216c6e77098526.jpg)", 
            "background-size":"cover",
            "margin": "0px",
            "min-height": "800px",
            "min-width":"800px",
           }
           },

        # creating form to get Log in credentials
        html.form(
        
               {"on submit": submit},
                html.b(html.h1(
                    {"style": {"font-family": "MissionScript", "font-size": "40px","color":"LightCyan"}}
                    ,"Create Your Account",)),
                html.br(),

                html.b(html.h2(
                    {"style": {"font-family": "MissionScript", "font-size": "30px","color":"LightCyan", "font-family": "Italic"}}
                    ,'Login into your future')),

                html.label(
                    {"style": {"font-family": "MissionScript", "font-size": "25px","color":"#e6fffa",}}
                    ,"Enter First name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "First name",
                        "on_change": lambda event: set_firstname(event["target"]["value"]),
                          "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                        
                    }
                    ),
                
                html.label(
                    {"style": {"font-family": "MissionScript", "font-size": "25px","color":"#e6fffa",}}
                    ,"Enter Last name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Last name",
                        "on_change": lambda event: set_lastname(event["target"]["value"]),
                          "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                        
                    }
                    ),

                html.label(
                    {"style": {"font-family": "MissionScript", "font-size": "25px","color":"#e6fffa",}}
                    ,"Enter User name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "User name",
                        "on_change": lambda event: set_user_name(event["target"]["value"]),
                          "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                        
                    }
                    ),
                html.br(),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "25px","color":"#e6fffa"}}
                    ,"Password"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Password",
                        "on_change": lambda event: set_password(event["target"]["value"]),
                          "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                        
                    }
                    ),
                html.br(),
                html.p(""),
                # creating submit button on form
                html.button(
                    {
                        "type": "Create an Account",
                        "on_click":event(lambda event:submit(event)),
                        "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#00008B",
                            "color": "#f4f5f0",
                            "outline": "none",
                            },
                    },
                    "Create Account",
                ),
                html.button(
                {
                    "type": "Clear",
                    "on_click":lambda event: set_user_name("")  and set_password(""),
                    "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#00008B",
                            "color": "#f4f5f0",
                            "outline": "none",
                            },
                },
                "Clear",
                ),
                ),
        html.ul(list),    
    )

#Connection code to open up a connection in MongoDB Atlas colud data base
uri = "mongodb+srv://Raas1:Raas0@raas.cb1ezfm.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi("1"))

##The database name and collection credentials will be stored in
db = client["Raas"]
collection = db["Assignment"]

##checking for the data base connectivity 
try:
    client.admin.command("ping")
    print("Sucessfully connected Mongodb")
except Exception as e:
    print(e)


#code to store entered user data from webapplication to MongoDB atlas cloud database
def login(
    login_data: dict,
):  
    User_name= login_data["User_name"]
    password = login_data["password"]

    
    Sen_info={"User_name": User_name,}
    
    document = {"User name":User_name,"password": password}
    # logger.info('sample log message')
    print(document)

    ## Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id  # insert document
    print(post_id)

    return {"message": "Login successful"}

configure(app, Account_creation)