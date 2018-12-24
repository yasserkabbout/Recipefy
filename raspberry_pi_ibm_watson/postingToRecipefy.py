import json
import requests
from watson_developer_cloud import VisualRecognitionV3
import os

watson_Data=""

#Foods types available to the api
apple=""
rice=""
tomato=""
onion=""
orange=""
tea=""
chocolate=""
egg=""
lentil =""
potato=""
lemon =""
garlic=""
strawberry=""


#Getting the username for bash
username = input("Please enter your Recipefy username:    ")

print(username)

os.system('fswebcam -S 20 --no-banner image.jpg')

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='REPLACE_WITH_YOUR_API_KEY')

with open('./image.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        classifier_ids=["food"]).get_result()
    print(json.dumps(classes, indent=2))
    watson_Data= json.dumps(classes)
    #print(json.dumps(classes, indent=2))

 #print(jsonWatsonData)

food_type = json.loads(watson_Data)

food_type= food_type['images'][0]['classifiers'][0]['classes'][0]['class']

#r = requests.get(url='http://localhost:8000/api/Users/?search='+username)
#print(r.json())

#food_type="tomato"


if(food_type=="tomato"):
	tomato=food_type
if(food_type=="apple"):
	apple=food_type
if(food_type=="rice"):
	rice=food_type
if(food_type=="onion"):
	onion=food_type
if(food_type=="orange"):
	orange=food_type
if(food_type=="tea"):
	tea=food_type
if(food_type=="chocolate"):
	chocolate=food_type
if(food_type=="egg"):
	egg=food_type
if(food_type=="lentil"):
	lentil=food_type
if(food_type=="potato"):
	potato=food_type
if(food_type=="lemon"):
	lemon=food_type
if(food_type=="garlic"):
	garlic=food_type
if(food_type=="starwberry"):
	strawberry=food_type

postData={
    "username": username,
    "apple": apple,
    "rice": rice,
    "tomato": tomato,
    "onion": onion,
    "orange": orange,
    "tea": tea,
    "chocolate": chocolate,
    "egg": egg,
    "lentil": lentil,
    "potato": potato,
    "lemon": lemon,
    "garlic": garlic,
    "strawberry": strawberry
}

postRequest = requests.post("http://recipefy-swe599.herokuapp.com/api/User_Groceries/", postData)
