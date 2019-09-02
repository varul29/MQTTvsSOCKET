import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("Log", +buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad COnnection= ",rc)

# Define Variables
broker = "192.168.0.1"
#MQTT_PORT = 1883

client = mqtt.Client("python1")
client.on_connect = on_connect
client.on_log = on_log
print("Connectingg to broker",broker)
client.connect(broker)
client.loop_start()

time.sleep(1)
client.loop_stop()
client.disconnectt()
