import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883, 60)

time.sleep(1)
client.loop()
while True:
    message = input('Enter Message: ')  
    client.publish("joshua/message", message)