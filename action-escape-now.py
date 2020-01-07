#!/usr/bin/env python3

from hermes_python.hermes import Hermes, MqttOptions
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
        result_sentence = "Das kann ich nicht"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)
    
    elif intentname == user_intent("Adler"):
        result_sentence = NAMES[11]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)
    
    elif intentname == user_intent("Apfel"):
        result_sentence = NAMES[9]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)
    
    elif intentname == user_intent("Becken"):
        result_sentence = NAMES[0]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)
    
    elif intentname == user_intent("Zwerg"):
        result_sentence = NAMES[5]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Decepticon"):
        result_sentence = "Autobots transformiert euch!"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Elch"):
        result_sentence = NAMES[13]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)    

    elif intentname == user_intent("Explosion"):
        result_sentence = "Tick! Tack! Tick! Tack!"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Koch"):
        result_sentence = NAMES[7]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Hase"):
        result_sentence = NAMES[16]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)
    
    elif intentname == user_intent("Hasenkampf"):
        result_sentence = NAMES[20]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Smiley"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Kolibri"):
        result_sentence = NAMES[21]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("OffeneHaende"):
        result_sentence = NAMES[25]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Nichts"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Pfau"):
        result_sentence = NAMES[15]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Hexe"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Frau"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Schaedel"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Reproduktionssystem"):
        result_sentence = NAMES[11]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Schwellkoerper"):
        result_sentence = "Wir haben keine Zeit für Witze"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Baum"):
        result_sentence = NAMES[8]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Teufel"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Vampir"):
        result_sentence = "Aber nicht die, die im Sonnenlicht glitzern."
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Panda"):
        result_sentence = NAMES[6]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Murmeltier"):
        result_sentence = NAMES[1]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Raumschiff"):
        result_sentence = NAMES[19]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Lunge"):
        result_sentence = NAMES[17]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("General"):
        result_sentence = NAMES[2]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Gewicht"):
        result_sentence = "Das ist mir zu schwer!"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Nikolaus"):
        result_sentence = NAMES[14]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence) 

    elif intentname == user_intent("Heuschrecke"):
        result_sentence = NAMES[10]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Kaleidoskop"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Hummer"):
        result_sentence = NAMES[24]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Cowboy"):
        result_sentence = "Yee! Haa!"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Mamma"):
        result_sentence = NAMES[18]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Tuersteher"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Rueckenschmerzen"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Krone"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("Watchmen"):
        result_sentence = "Könnt ihr das auch sehen?"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("HeptapodischEins"):
        result_sentence = NAMES[23]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("HeptapodischZwei"):
        result_sentence = NAMES[3]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("HeptapodischDrei"):
        result_sentence = NAMES[22]
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    elif intentname == user_intent("HeptapodischVier"):
        result_sentence = NAMES[4]
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
