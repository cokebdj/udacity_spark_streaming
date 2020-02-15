from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def generate_data(self):
        with open(self.input_file, encoding='utf-8') as f:
            json_data = f.read()
            data = json.loads(json_data)
            for line in data:
                message = json.dumps(line).encode('utf-8')
                self.send(self.topic, message)
                time.sleep(0.01)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode("utf-8")
        