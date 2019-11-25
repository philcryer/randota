# randota

randota = randomize twitter avatar = randomize your Twitter avatar from the commandline

## Idea

I wanted a way to randomly change my Twitter avatar, as a bonus I wanted to have many variations on my original avatar, but have them all 'glitched'

## Steps

### Create a Twitter app

twitter api via curl
tips https://gist.github.com/apolloclark/2d4f6362f31666c1c81f

https://developer.twitter.com/en/docs/basics/authentication/overview/application-only

https://developer.twitter.com/en/apps/17031299`

keey and token create

https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image
The avatar image for the profile, base64-encoded. Must be a valid GIF, JPG, or PNG image of less than 700 kilobytes in size. Images with width larger than 400 pixels will be scaled down. Animated GIFs will be converted to a static GIF of the first frame, removing the animation.

POST https://api.twitter.com/1.1/account/update_profile_image.json?image=ABCDEFGH...

### Glitch your avatar

If you want to do the same with the glithed idea, play on here, otherwise jump to the next section

1) save your avatar locally
2) hit [jpg-glitch](https://snorpey.github.io/jpg-glitch/), upload your avatar, glitch it as much as you want, or just choose the 'random' option
3) save the file into a directory `img`
4) repeat as many times as you'd like to increase your randomness

### Install requirements

```
pip install -r requirements.txt
```

### Build your config file

```
cp config.json.dist config.json
```

Edit `config.json` and add your values from your Twitter app page

### Run it

```
python3 randota.py
```

View the hilarity on Twitter.com/<your_username>

## License

[Modified BSD License](LICENSE)

### thanks
