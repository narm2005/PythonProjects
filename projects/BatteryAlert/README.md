## BatertAlert :loudspeaker:

BatertAlert is for all the lazy people (like me :bowtie: ) who often miss desktop notifications. BatertAlert 
will say it clear and loud whenever your battery status goes below a default critical level or the level decided by you! 


### Installation

##### Build from tar files
```sh
	tar xzvf BateryAlert-1.1.8.tar.gz
	cd BatertAlert-1.1.8
	python setup.py install
```
```
##### Using pip
```sh
	pip install BateryAlert
```
After installation is done successfully, run any combinations of below command in your terminal once for initial setup and then we are done! If you want to use the default setup then just run  ``` BatertAlert ``` in terminal. 

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

BateryAlert -l hindi

```

##### Set rate of speaking
```sh
BateryAlert -r 100

```

##### Set your custom alert message
```sh

BateryAlert -m "Delta is the state of mind"

```

##### Set custom charge level. 
If the battery level is below this critical level then it will give voice alert

```sh
BateryAlert -c 30

```
##### View the set configuration
```sh
BateryAlert -s
```

##### Get help
```sh
BateryAlert -h
```
##### Example
```sh
BateryAlert -m "Hi Check ur battery" -c 25
```
When you run the above code, you've set "Hey,Lazy dog" as your custom message and 25 as your critical charge level.
