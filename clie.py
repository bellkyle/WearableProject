
# -*- coding: utf-8 -*-
"""
Test MQTT for Arduino MKR1000
Created on Fri Feb 23 14:53:01 2018

@author: ahnelson
"""


import paho.mqtt.client as mqtt
import base64
import random, string
import math
import json
import time

#Constants used in the script
TOPIC = 'uark/csce5013/kylebell/'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def convertImageToBase64():
    with open("keyboard.jpg", "rb") as image_file:
       encoded = base64.b64encode(image_file.read())
    return encoded

def send():
    payload = convertImageToBase64()
    #publishEncodedImage(payload)
    client.publish('uark/csce5013/kylebell/test', payload)
    

#Get an instance of the MQTT Client object
client = mqtt.Client()
#Set the function to run when the client connects
client.on_connect = on_connect
#Set the function to run when a message is received
client.on_message = on_message
#Connect to the broker.mqtt-dashboard.com server on port 1883
client.connect("thor.csce.uark.edu", 1883, 60)
#Non-blocking loop. Starts a new thread that listens for messages and prints them
client.loop_start()
client.subscribe("uark/csce5013/kylebell/test")
userInput = ""
while userInput != "exit":
    userInput = input("Please enter message or enter exit to quit \n")
    if userInput != "exit":
        send()
        time.sleep(4)
client.loop_stop()
