#!/usr/bin/env python3

from hermes_python.hermes import Hermes, MqttOptions
from playsound import playsound
import datetime
import random
import toml

USERNAME_INTENTS = "RedStriped"
MQTT_BROKER_ADDRESS = "localhost:1883"
MQTT_USERNAME = None
MQTT_PASSWORD = None
NAMES = ["Hannah Ahlers", "Joshua Becker", "Theodor van Campen", "Tim Diefenthaler", "Pia Engel", "Mia Fuchs", "Tim Garlich", "Fridolin Hacker", "Lara Ihmken", "Eric zu Jeddeloh",
"Tim Krüger", "Joshua Lehmann", "Pia Müller", "Hannah Neemeyer", "Liam Ohsenbeck", "Laura Peters", "Jonas Quathammer", "Tom Raabe", "Bob Schneider", "Lara Thiesmeyer",
"Anna Ullrichs", "Ursula Voigt", "Tom Wolff", "Thomas Xylander", "Jonas Yost", "Thomas Zimmermann"]

def user_intent(intentname):
    return USERNAME_INTENTS + ":" + intentname


def subscribe_intent_callback(hermes, intent_message):
    intentname = intent_message.intent.intent_name

    if intentname == user_intent("takeYourMeds"):
        name = random.choice(NAMES)
        result_sentence = "Das kann ich nicht"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Adler"):
        playsound('hawk.wav')

    elif intentname == user_intent("Apfel"):
        result_sentence = NAMES[25]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Becken"):
        result_sentence = NAMES[1]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Explosion"):
        result_sentence = NAMES[24]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Zwerg"):
        result_sentence = NAMES[2]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Decepticon"):
        result_sentence = NAMES[23]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Elch"):
        result_sentence = NAMES[3]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Smiley"):
        result_sentence = NAMES[22]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Schwellkoerper"):
        result_sentence = NAMES[4]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Murmeltier"):
        result_sentence = NAMES[21]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Baum"):
        result_sentence = NAMES[5]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Frau"):
        result_sentence = NAMES[20]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("OffeneHaende"):
        result_sentence = NAMES[6]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Kolibri"):
        result_sentence = NAMES[19]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Vampir"):
        result_sentence = NAMES[7]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Hexe"):
        result_sentence = NAMES[18]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Nichts"):
        result_sentence = NAMES[8]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Teufel"):
        result_sentence = NAMES[17]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Schaedel"):
        result_sentence = NAMES[9]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Panda"):
        result_sentence = NAMES[16]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Reproduktionssystem"):
        result_sentence = NAMES[10]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Hase"):
        result_sentence = NAMES[15]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Pfau"):
        result_sentence = NAMES[11]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Hasenkampf"):
        result_sentence = NAMES[14]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Koch"):
        result_sentence = NAMES[12]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Raumschiff"):
        result_sentence = NAMES[13]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Lunge"):
        name = random.choice(NAMES)
        result_sentence = "{name} ist cool!".format(name=name)
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Kaleidoskop"):
        result_sentence = "Kannst du das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Kaleidoskop"):
        result_sentence = "Kannst du das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

if __name__ == "__main__":
    snips_config = toml.load('/etc/snips.toml')
    if 'mqtt' in snips_config['snips-common'].keys():
        MQTT_BROKER_ADDRESS = snips_config['snips-common']['mqtt']
    if 'mqtt_username' in snips_config['snips-common'].keys():
        MQTT_USERNAME = snips_config['snips-common']['mqtt_username']
    if 'mqtt_password' in snips_config['snips-common'].keys():
        MQTT_PASSWORD = snips_config['snips-common']['mqtt_password']

    mqtt_opts = MqttOptions(username=MQTT_USERNAME, password=MQTT_PASSWORD, broker_address=MQTT_BROKER_ADDRESS)
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intents(subscribe_intent_callback).start()
