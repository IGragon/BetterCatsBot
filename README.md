# BetterCatsBot

## Description
BetterCatsBot is the telegram bot (@BetterCatsBot), that is built on asynchronous library Aiogram and deployed on Heroku

Webhook is used

Some training info can be found in this .ipynb notebook https://colab.research.google.com/drive/1jrAvjN7hLNRRmqXT0vvswbFGq5putyKt?usp=sharing

## Bot commands
/start - greets user

/cat - transition to image processing mode

/help - exits any mode and shows the list of commands

## Image processing
Images are refined by SRGAN, that was trained on a dataset with cats for 1000 epochs.

SRGAN is initialized with SRRes-Net-MSE weights, that was pretrained for 100 epochs on the same dataset.

Due to Heroku's restriction on 500 Mb of memory, input images larger than 200px in any dimension will be compressed to 200px in that dimension.

## Examples
There are examples of upscaling 128px (on the left) images to 512px (on the right)

![first example](https://github.com/IGragon/BetterCatsBot/blob/master/img/1.png)
![second example](https://github.com/IGragon/BetterCatsBot/blob/master/img/2.png)
![third example](https://github.com/IGragon/BetterCatsBot/blob/master/img/3.png)
![fourth example](https://github.com/IGragon/BetterCatsBot/blob/master/img/4.png)
