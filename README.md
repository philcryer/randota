# randota

randota = randomize twitter avatar = randomize your Twitter avatar from the commandline, and automate it using cron.

## Idea1 - Glitched avatar

I wanted a way to randomly change my Twitter avatar, to a randomly 'glitched' out version, on a set time (currently hourly), so I created `glitchedavatar.py`. This method requires that you manually glitch the images you want, drop them in a directory, create a new Twitter App to get permissions to change your avatar, then install and use [Tweepy](https://www.tweepy.org/) to do the heavy lifting, all called by `cron`.

## Idea2 - thispersondoesntexist avatar

I wanted a way to update an avatar with a random one, but I took it a step further buy having it update it with a random one, of a person that doesn't exist. The new script `getthisperson.py` follows much of the same logic of `glitchedavatar.py`, but this time it pulls a user from [This Person Doesn't Exist](https://thispersondoesntexist.com). This is a machine learning project that generates fake people, that look real. See the site for more information, it's really facinating. To use this script, follow the same steps below, skipping the "Glitch you avatar" section.

## Steps

### Get the code

Clone the git repo and start to configure your environment

```
git clone https://github.com/philcryer/randota.git
cd randota
rm -rf img/*
cp config.json.dist config.json
```

### Install requirements

For Debian GNU/Linux, or any Ubuntu derivatives:

```
sudo apt install python3-pip
python3 -m pip install -r requirements.txt
```

For Arch Linux, or derivatives:

```
sudo pacman -S python-pip
python3 -m pip install -r requirements.txt
```

### Create a Twitter app

The first step you should take is to create a new Twitter App so you can get permissions to update your user's avatar. While there are many howtos out there, this one is complete and should get you going; [How to create a Twitter application](https://docs.inboundnow.com/guide/create-twitter-application/)

Once you get to "8. Make a note of your OAuth Settings", be sure and save the Consumer Key, Consumer secret, Access token and Access token secret, defining each of the values in your newly created `config.json` file

### Glitch your avatar

To glitch your avatar, play on here, otherwise if you just want to use standard avatars and rotate between them, jump to the next section

1) save your avatar locally
2) hit [jpg-glitch](https://snorpey.github.io/jpg-glitch/), upload your avatar, glitch it as much as you want, or just choose the 'random' option
3) save the file into a directory `img`
4) repeat as many times as you'd like to increase your randomness


### Run it

To run `glitchedavatar.py`:

```
python3 glitchedavatar.py
```

or, to run `getthisperson.py`:

```
python3 getthisperson.py
```

View the hilarity or disappointment at twitter.com/<your_username>

### Automate it

Add a new line to your user's crontab, fill out the path to where your code is

To automate `glitchedavatar.py`:

```
0 * * * *    cd ${HOME}/code/randota; python3 glitchedavatar.py >/dev/null 2>&1
```

or, to automate `getthisperson.py`:

```
0 * * * *    cd ${HOME}/code/randota; python3 getthisperson..py >/dev/null 2>&1
```

## License

[Modified BSD License](LICENSE.md)

### thanks
