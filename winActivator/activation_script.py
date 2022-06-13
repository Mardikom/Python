import subprocess

def win8activate():
    subprocess.call(["slmgr/ipk", "NG4HW-VH26C-733KW-K6F98-J8CK4"])
    subprocess.call(["slmgr", "/skms", "kms.digiboy.ir"])
    subprocess.call(["slmgr", "/ato"])

def win81activate():
    subprocess.call(["slmgr/ipk", "GCRJD-8NW9H-F2CDX-CCM8D-9D6T9"])
    subprocess.call(["slmgr", "/skms", "kms.digiboy.ir"])
    subprocess.call(["slmgr", "/ato"])
    
def win10ProActivate():
    subprocess.call(["slmgr/ipk", "W269N-WFGWX-YVC9B-4J6C9-T83GX"])
    subprocess.call(["slmgr", "/skms", "kms.digiboy.ir"])
    subprocess.call(["slmgr", "/ato"])

def win10ltscActivate():
    subprocess.call(["slmgr/ipk", "M7XTQ-FN8P6-TTKYV-9D4CC-J462D"])
    subprocess.call(["slmgr", "/skms", "kms.digiboy.ir"])
    subprocess.call(["slmgr", "/ato"])