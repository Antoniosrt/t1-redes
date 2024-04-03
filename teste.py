import dpkt

def read_pcapng(filename):
    with open(filename, 'rb') as file:
        pcap = dpkt.pcapng.Reader(file)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            # Aqui você pode acessar os campos do pacote IP, como endereço de origem, destino, etc.
            print("Source IP:", ".".join(map(str, ip.src)))
            print("Destination IP:", ".".join(map(str, ip.dst)))

if __name__ == "__main__":
    filename = "trabalho1.pcapng"
    read_pcapng(filename)
