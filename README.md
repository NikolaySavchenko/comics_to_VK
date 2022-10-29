# comics_to_VK

It's connects to [XKCD](https://xkcd.com/), fetch comics and public it in your public [VKontakte](https://vk.com/).

## How to install


Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
For using you need your TOKEN [VKontakte](https://vk.com/). 
You can get it according to the [instructions](https://dev.vk.com/api/access-token/implicit-flow-user).

You should use environment variables. Create file name `.env` and variables `VK_TOKEN` in the root directory.
In file `.env` only one line:

```
VK_TOKEN='here is your own TOKEN'
```

Example for command line:
```
$ python '\comics_to_VK\main.py'
```

And, **magic!**, one of the comics with the author's commentary will appear on your public page.



## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).