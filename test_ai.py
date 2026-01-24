#!/usr/bin/env python3
import json
import paho.mqtt.client as mqtt
import time

def test_ai():
    def on_connect(client, userdata, flags, rc):
        print(f"Connected: {rc}")
        client.subscribe("term-chat/global/v3")
        
        # Send test message
        test_msg = {
            "type": "chat",
            "id": "TESTER",
            "msg": "ai hello test"
        }
        client.publish("term-chat/global/v3", json.dumps(test_msg))
        print("Sent test message: ai hello test")

    def on_message(client, userdata, message):
        try:
            payload = json.loads(message.payload.decode())
            if payload.get("id") == "TERMAI":
                print(f"✅ AI Response: {payload.get('msg')}")
                client.disconnect()
            else:
                print(f"Message from {payload.get('id')}: {payload.get('msg')}")
        except Exception as e:
            print(f"Error: {e}")

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("broker.emqx.io", 1883, 60)
        client.loop_start()
        time.sleep(10)  # Wait for response
        client.loop_stop()
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    test_ai()