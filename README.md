# PyTile
A Python 3 wrapper enabling serial comms with Swarm's Tile satellite module.


## Example Console Output
```(venv) Arya:pytile jonathan$ python3 example.py
Auto Detecting Port...
Connecting to /dev/cu.usbserial-1410
Tile Firmware Version:
$FV 2021-07-21-23:19:41,v1.1.0*7e

Current GPS Time (UTC):
2021-10-11 18:41:54+00:00

Swarm Tile GPS Fix:
Latitude: -34.5296
Longitude: 18.6837
Altitude: 12 meters
Course: 287 degrees
Speed: 2 km/h
Horizontal Dilution of Precision: 129
Vertical Dilution of Precision: 184
GNSS Sats: 7
Fix: G3
Fix Type: Standalone 3D

0 unread messages.

10 second monitor running... (Look in tile.log)
```

## Example tile.log 
```2021-10-11T20:41:53.499017 ### Tile Serial Connected on/dev/cu.usbserial-1410
2021-10-11T20:41:53.499121 >>> $DT 0*00
2021-10-11T20:41:53.508643 <<< $DT OK*34
2021-10-11T20:41:53.508938 >>> $GN 0*19
2021-10-11T20:41:53.518026 <<< $GN OK*2d
2021-10-11T20:41:53.518156 >>> $FV*10
2021-10-11T20:41:53.524861 <<< $FV 2021-07-21-23:19:41,v1.1.0*7e
2021-10-11T20:41:53.524970 >>> $DT 1*01
2021-10-11T20:41:53.533949 <<< $DT OK*34
2021-10-11T20:41:53.534043 >>> $DT @*70
2021-10-11T20:41:53.540001 <<< $DT 20211011184154,V*47
2021-10-11T20:41:53.540095 >>> $DT 0*00
2021-10-11T20:41:53.549106 <<< $DT OK*34
2021-10-11T20:41:53.555159 >>> $GN 1*18
2021-10-11T20:41:53.564375 <<< $GN OK*2d
2021-10-11T20:41:53.564478 >>> $GN @*69
2021-10-11T20:41:53.571690 <<< $GN -34.5396,18.5337,12,287,2*05
2021-10-11T20:41:53.571781 >>> $GN 0*19
2021-10-11T20:41:53.580854 <<< $GN OK*2d
2021-10-11T20:41:53.580965 >>> $GS 1*05
2021-10-11T20:41:53.590065 <<< $GS OK*30
2021-10-11T20:41:53.590200 >>> $GS @*74
2021-10-11T20:41:53.596093 <<< $GS 129,184,7,0,G3*40
2021-10-11T20:41:53.596222 >>> $GS 0*04
2021-10-11T20:41:53.605239 <<< $GS OK*30
2021-10-11T20:41:53.605389 >>> $MM C=**74
2021-10-11T20:41:54.914604 <<< $MM 0*10
2021-10-11T20:41:57.244761 <<< $RT RSSI=-92*26
2021-10-11T20:42:02.243278 <<< $RT RSSI=-94*20
```
