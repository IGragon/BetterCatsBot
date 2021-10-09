# BetterCatsBot

## Description
Bot is built on asynchronous library aiogram and deployed on heroku

Webhook is used

## Bot commands
/start - greets user

/cat - transition to image processing mode

/help - exits any mode and shows the list of commands

## Image processing
Images are refined by SRRes-Net, that was trained on a dataset with cats for 1000 epochs.

Due to Heroku's restriction on 500 Mb of memory, input images larger than 200px in any dimension will be compressed to 200px in that dimension.

## Examples
There are examples of upscaling 128px (on the left) images to 512px (on the right)

![first example](https://github.com/IGragon/BetterCatsBot/blob/master/img/1.png)

![second example](https://github.com/IGragon/BetterCatsBot/blob/master/img/2.png)

![third example](https://github.com/IGragon/BetterCatsBot/blob/master/img/3.png)

![fourth example](https://github.com/IGragon/BetterCatsBot/blob/master/img/4.png)
