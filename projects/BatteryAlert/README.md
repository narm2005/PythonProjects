## BatteryAlert :loudspeaker:

BatteryAlert is for all the lazy people (like me :bowtie: ) who often miss desktop notifications. BatteryAlert 
will say it clear and loud whenever your battery status goes below a default critical level or the level decided by you! 


### Installation

##### Build from tar files
```sh
	tar xzvf BatteryAlert-1.1.8.tar.gz
	cd BatteryAlert-1.1.8
	python setup.py install
```
```
##### Using pip
```sh
	pip install BatteryAlert
```
After installation is done successfully, run any combinations of below command in your terminal once for initial setup and then we are done! If you want to use the default setup then just run  ``` BatteryAlert ``` in terminal. 

###Default config:
	language: English
	rate    : 150
	charge  : 20 (in percentage)
    msg     : ""
    vol     : 1.0

###Options
```sh
usage: main.py [-h] [-r RATE] [-v VOL] [-l LANG] [-m MSG] [-c CHARGE] [-s]

Listen the voice of your battery whenever she is low!

optional arguments:
  -h, --help            show this help message and exit
  -r RATE, --rate RATE  Rate of speaking.(100-200)
  -v VOL, --vol VOL     Volume of speaking.(1.0)
  -l LANG, --lang LANG  Language speaking
  -m MSG, --msg MSG     Alert message of your own
  -c CHARGE, --charge CHARGE
                        Decide the critical charge level
  -s, --show            Show the currently set config


```

### Usage

##### Set language
To set the language eg. hindi, english , tamil. Default one is english
```sh

BatteryAlert -l hindi

```

##### Set rate of speaking
```sh
BatteryAlert -r 100

```

##### Set your custom alert message
```sh

BatteryAlert -m "Delta is the state of mind"

```

##### Set custom charge level. 
If the battery level is below this critical level then it will give voice alert

```sh
BatteryAlert -c 30

```
##### View the set configuration
```sh
BatteryAlert -s
```

##### Get help
```sh
BatteryAlert -h
```
##### Example
```sh
BatteryAlert -m "Hi Check ur battery" -c 25
```
When you run the above code, you've set "Hey,Lazy dog" as your custom message and 25 as your critical charge level.
