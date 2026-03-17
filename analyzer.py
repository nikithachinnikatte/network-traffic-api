import pyshark
import pandas as pd

def process_pcap(file_path):
    capture = pyshark.FileCapture(file_path)

    data = []

    for packet in capture:
        try:
            src = packet.ip.src
            dst = packet.ip.dst
            protocol = packet.transport_layer

            data.append({
                "src": src,
                "dst": dst,
                "protocol": protocol
            })

        except:
            continue

    capture.close()

    return pd.DataFrame(data)