from lib.my_music import MyMusic

def test_add_to_dict():
    band_track_instance = MyMusic()
    band1 = "Metallica"
    tracks1 = "Enter Sandman"

    band_track_instance.add_band(band1, tracks1)

    print("Result of test_add_to_dict:", band_track_instance.my_dict)
    assert band_track_instance.my_dict == {band1: tracks1}

def test_add_to_dict_second_band():
    band_track_instance = MyMusic()
    band1 = "Metallica"
    tracks1 = "Enter Sandman"
    band2 = "ACDC"
    tracks2 = "Riff Raff"

    band_track_instance.add_band(band1, [tracks1])
    band_track_instance.add_band(band2, [tracks2])

    print("Result of test_add_to_dict_second_band:", band_track_instance.my_dict)
    assert band_track_instance.my_dict == {band1: [tracks1], band2: [tracks2]}

def test_add_to_dict_third_band():
    band_track_instance = MyMusic()
    band1 = "Metallica"
    tracks1 = "Enter Sandman"
    band2 = "ACDC"
    tracks2 = "Riff Raff"
    band3 = "Iron Maiden"
    tracks3 = "Prowler"

    band_track_instance.add_band(band1, [tracks1])
    band_track_instance.add_band(band2, [tracks2])
    band_track_instance.add_band(band3, [tracks3])

    print("Result of test_add_to_dict_third_band:", band_track_instance.my_dict)
    assert band_track_instance.my_dict == {band1: [tracks1], band2: [tracks2], band3: [tracks3]}