import dpkt
import manuf
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_data")
async def get_ips():
    filename = "trabalho1.pcapng"
    dados = ler_arquivo_pcapng(filename)
    return {"dados": dados }
    # return {"message": "Hello World"}


def obter_fabricante(endereco_mac):
    try:
        
        return manuf.MacParser().get_manuf(endereco_mac)
    except:
        return "Fabricante não encontrado"


def ler_arquivo_pcapng(filename):
    # obj para armazenar os fabricantes e quantas vezes eles aparecem
    dataFabricante = {}
    dataFabricanteDest = {}
    dataTtlFabricante = [] 
    obj_rtrn = {
            "fabricante": "",
            "enderecos_mac": []
        }
    contadorMax = 0
    with open(filename, 'rb') as file:
        pcap = dpkt.pcapng.Reader(file)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            ipv4= eth.data
            #pega endereco mac de origem o fabricante e adiciona no objeto
            if hasattr(eth, 'src'):
                endereco_mac_origem = ':'.join('%02x' % byte for byte in eth.src)
                fabricante = obter_fabricante(endereco_mac_origem)
                if(fabricante in dataFabricante):
                    dataFabricante[fabricante] += 1
                else:
                    dataFabricante[fabricante] = 1
            ########################################
            #pega endereco mac de destino o fabricante e adiciona no objeto
            if(hasattr(ipv4, 'dst')): 
                endereco_mac_destino = ':'.join('%02x' % byte for byte in eth.dst)
                fabricanteDest = obter_fabricante(endereco_mac_destino)
                if(fabricanteDest in dataFabricanteDest):
                    dataFabricanteDest[fabricanteDest] += 1
                else:
                    dataFabricanteDest[fabricanteDest] = 1
            ########################################
            if(hasattr(ipv4, 'ttl')):
                dataTtlFabricante.append({
                    "fabricante": fabricante,
                    "ttl": ipv4.ttl
                })
            ########################################
            contadorMax += 1
            if(contadorMax == 100):
                break
        
    obj_rtrn["fabricante"] = dataFabricante
    # obj_rtrn["enderecos_mac"] = obj_endereco_mac
    obj_rtrn["ttl"] = dataTtlFabricante
    return obj_rtrn
