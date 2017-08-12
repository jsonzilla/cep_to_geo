# cep2geo
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7920e2ebdf1347fcb55b1e9e3a787b60)](https://www.codacy.com/app/0unit/cep2geo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=0unit/cep2geo&amp;utm_campaign=Badge_Grade)

 Query geolocation with base of a brazilian zip code (cep)

```
$ python cep2geo.py -i <inputfile> -o <outputfile>
$ cep2geo_zippopotam.py -i <inputfile> -o <outputfile>
```

*Only need a cep per line!*

Input a csv file (Cep without hifen!):
```
88010000,"Rua Felipe Schmidt, até 348/349",Centro,3454,24
```

Output a csv file:
```
88010000,"Rua Felipe Schmidt, até 348/349",Centro,3454,24,-27.5957101,-48.5532068,APPROXIMATE,-27.5924921,-48.5462376,-27.600032,-48.5574976
```

## Question
Why have more information what one latitude and longitude?
Google Maps API return more information.

          "geometry" : {
             "bounds" : {
                "northeast" : {
                   "lat" : -27.5848141,
                   "lng" : -48.9514556
                },
                "southwest" : {
                   "lat" : -27.7738787,
                   "lng" : -49.2029872
                }
             },
             "location" : {
                "lat" : -27.6728835,
                "lng" : -49.1019233
             },
             "location_type" : "APPROXIMATE",
             "viewport" : {
                "northeast" : {
                   "lat" : -27.5848141,
                   "lng" : -48.9514556
                },
                "southwest" : {
                   "lat" : -27.7738787,
                   "lng" : -49.2029872
                }
             }
          },