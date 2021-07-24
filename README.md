# Grafana Setup with Prometheus

This files are for configuring a solid Grafana Monitoring System.

prometheus/prometheus.yml contains another job of node exporter to get metrics remotely from a Raspberry Pi.
Its IP address must be specified beforehand in the jobs section.

run
``
docker run -d -p 9100:9100 prom/node-exporter:latest'
``
in the Raspberry Pi shell


https://nosqldata-43a40-default-rtdb.firebaseio.com/ADC/node1.json