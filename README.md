londonbikes
===========

Simple script which allows to search in the TFL BikePoint API.


Instalation
-----------

```shell
python setup.py install --user
```


Usage
-----

The script requires Application ID and Key from [TFL
API](https://api.tfl.gov.uk). Once you have them, export those as environment
variables:

```shell
export TFL_APP_ID='abcdefgh'
export TFL_APP_KEY='1234567890abcdefghijklmnopqrstuv'
```

The usage of the script is:

```
$ londonbikes
Usage:
  londonbikes search <search_string>
  londonbikes search <latitude> <longitude> <radius_in_metres>
  londonbikes id <bike_point_id>
```

You can search for BikePoints:

```
$ londonbikes search East
Id              Name                                           Latitude   Longitude
BikePoints_50   East Road, Hoxton                              51.528673  -0.087459
BikePoints_233  Pall Mall East, West End                       51.50777   -0.130699
BikePoints_330  Eastbourne Mews, Paddington                    51.516417  -0.179135
[...]
```

Or search for BikePoints in certain distance from a specific location:

```
$ londonbikes search 51.53 -0.09 250
Id             Name                  Latitude,Longitude   Distance
Id             Name                   Latitude,Longitude   Distance
BikePoints_63  Murray Grove , Hoxton  51.53089,-0.089782   100.1   
BikePoints_50  East Road, Hoxton      51.528673,-0.087459  229.5
```

Or display information about a specific BikePoint:

```
$ londonbikes id BikePoints_50
Name               Latitude   Longitude  Num Bikes  Empty Docks
East Road, Hoxton  51.528673  -0.087459  24         3
```

Debug messages will be shown if the following environment variable is exported:

```shell
export LONDONBIKES_DEBUG='1'
```


Author
------

Jiri Tyr


License
-------

MIT
