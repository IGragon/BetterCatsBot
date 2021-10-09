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
There are examples of upscaling 128px images to 512px


