import paho.mqtt.client as mqtt  #import the client1
import time
import random


# broker list
brokers=["iot.eclipse.org","broker.hivemq.com",\
         "test.mosquitto.org"]

broker=brokers[1]


def on_log(client, userdata, level, buf):
        print("log: "+buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
def on_disconnect(client, userdata, flags, rc=0):
        print("DisConnected result code "+str(rc))
def on_message(client,userdata,msg):
        topic=msg.topic
        m_decode=str(msg.payload.decode("utf-8","ignore"))
        print("message received: ",m_decode)

client = mqtt.Client("IOT_pudfdzfb_ugfefweu_jdksf", clean_session=True) # create new client instance

client.on_connect=on_connect  #bind call back function
client.on_disconnect=on_disconnect
client.on_log=on_log
client.on_message=on_message
print("Connecting to broker ",broker)
port=1883
client.connect(broker,port)     #connect to broker
pub_topic= 'Safe_house'


for x in range(21):
    mylist1 = ['open', 'cloes']
    b = random.choice(mylist1)
    if (b =="open"):
        client.publish(pub_topic," There are open windows on floor " + str(x)+" "+"The system will close the windows :)")
    else:
        client.publish(pub_topic, "There are no open windows on the floor " + str(x))

    time.sleep(5)
client.publish(pub_topic, "The scan is finished :)")


client.disconnect() # disconnect
print("End publish_client run script")