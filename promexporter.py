from prometheus_client import start_http_server, Summary
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

import random
import time

counter=0
spin=0
hbar=6.63e-34
# gives a single float value
class CustomCollector(object):     ## Class for CustomCollector which helps us

	def __init__(self):
		pass
	def collect(self):
		server_status = 1     ## place the logic here to get the server status
		cpu_usage = 7  		  ## place the logic here to get the CPU Usage.
		value = CounterMetricFamily("SERVER_STATUS", 'yardımmmmmm', labels=['value'])
		value.add_metric(["server_status"], server_status)
		value.add_metric(["spin"], spin)

		yield value

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    REGISTRY.register(CustomCollector())

    # Generate some requests.
    while True:
        process_request(1)
        spin=np.random.choice([hbar/2,-hbar/2],p=[1/3, 2/3]) #spinörü z yönünde spinleri hbar/2 ölçme olasılığı 1/3, -hbar/2 ölçme olasılığı 2/3 olan, 
        													 #beklenen değer -hbar/6 çıkmalı
        counter+=1
