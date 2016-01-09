## Latitude and Longitude data formats


### Signed degrees format (DDD.dddd)

A latitude or longitude with 8 decimal places pinpoints a location to within 1 millimeter,( 1/16 inch).

* Precede South latitudes and West longitudes with a minus sign.
* Latitudes range from -90 to 90.
* Longitudes range from -180 to 180.

```
41.25 and -120.9762
-31.96 and 115.84
90 and 0 (North Pole)
```

### DMS + compass direction formats

These formats use degrees, minutes, and seconds. For the following formats:
* Latitudes range from 0 to 90.
* Longitudes range from 0 to 180.
* Use N, S, E or W as either the first or last character, which represents a compass direction North, South, East or West.
* The last degree, minute, or second of a latitude or longitude may contain a decimal portion.
* Degrees minutes seconds formats (DDD MM SS + compass direction)

```
41 25 01N and 120 58 57W
41°25'01"N and 120°58'57"W
S17 33 08.352 and W69 01 29.74
```
### Degrees minutes formats (DDD MM + compass direction)

```
41 25N and 120 58W
41°25'N and 120°58'W
N41 25.117 and W120 58.292 (Common geocoding format)
```

### Degrees only formats (DDD + compass direction)

```
41 N and 120 W
41°N and 120°W
N41.092 and W120.8362
90S and 0E (South Pole)
```
