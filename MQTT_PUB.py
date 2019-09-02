import paho.mqtt.client as mqtt
import time
# Define Variables
broker = "192.168.0.1"
#MQTT_PORT = 1883

client = mqtt.Client("python1")
print("Connectingg to broker",broker)
client.connect(broker)

time.sleep(1)
client.disconnectt()
