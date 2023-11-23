class MyMusic:

def __init__(self):
#Empty dictionary to store our bands and tracks
    self.my_dict = {}

def add_band(self, band, tracks):
    self.my_dict[band] = tracks
    print(f"Added band: {band} with tracks: {tracks}")

def listened_to(self):
    print("I have listened to this so far")
    return self.my_dict