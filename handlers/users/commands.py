import logging
from io import BytesIO

from PIL import Image
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ContentType, InputFile
from torchvision.transforms import ToTensor, ToPILImage

from config import IMAGE_FORMATS
from keyboards.inline.callback_datas import help_callback
from keyboards.inline.choice_buttons import help_markup
from keyboards.normal.choise_buttons import cat_markup, remove_keyboard
from loader import dp, bot, model
from model import norm, denorm
from states.cat import Cat
from torch import save, set_grad_enabled
from utils.strings import cat_enter_msg, image_processing_msg, start_msg, help_msg, unknown_msg, cancel_msg, \
    helper_call, cat_wrong_format, cat_too_large_image, cat_after_processing


# starting dialog with bot
@dp.message_handler(Command("start"))
async def start(message: Message):  # starting dialog with user
    logging.info("Started")  # logging that we started
    await message.answer(text=start_msg)  # greetings to user
    await message_help(message, state=None, from_start=True)  # give user a list of commands


# starting "cat" sequence from command
@dp.message_handler(Command("cat"))
async def cat(message: Message):
    await message.answer(text=cat_enter_msg,
                         reply_markup=cat_markup)  # answer with a actions description and "cancel" keyboard
    try:
        await message.edit_reply_markup(reply_markup=None)  # erase inline keyboard if necessary
    except Exception:
        pass
    finally:
        await Cat.working.set()  # set state to Cat.working


# starting "cat" sequence from callback
@dp.callback_query_handler(help_callback.filter(command="cat"))
async def call_cat(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)  # cache callback
    logging.info(f"call = {callback_data}")  # logging callback data
    await cat(call.message)  # handle to message handler


# image document handler
@dp.message_handler(content_types=ContentType.DOCUMENT, state=Cat.working)
async def getting_image(message: Message, state: FSMContext):
    async def process_image(image: Image.Image):  # function to process an image
        with set_grad_enabled(False):
            image_tensor = await norm(  # turn to tensor and make B x C x W x H shape
                ToTensor()(image)
            )
            image_tensor = image_tensor.unsqueeze(0)
            super_res_image = await model(image_tensor[:, :3, :])

        # make image so bot can send it
        image_denorm = await denorm(super_res_image)
        image_to_return = ToPILImage(mode='RGB')(image_denorm[0])
        image_bytesio = BytesIO()
        image_to_return.save(image_bytesio, format='png')
        image_bytesio.seek(0)
        await message.answer_document(InputFile(image_bytesio,  # answer with refined image
                                                filename=f"better_{fname.split('.')[0]}.png"))
        await message.answer(cat_after_processing)  # answer with thanks

    image_doc = message.document  # get file as document
    logging.info(await state.get_state())  # logging state just in case
    logging.info(f"image_doc = {image_doc}")  # logging what type of image bot got
    fname = image_doc["file_name"]  # get filename
    if fname.split('.')[-1] in IMAGE_FORMATS:  # check if file is image
        img_id = image_doc["file_id"]  # get image id
        img_bytesio = BytesIO()  # set bytesIO instance for downloading image
        await bot.download_file_by_id(img_id, destination=img_bytesio)  # downloading image to img_bytesio
        img = Image.open(img_bytesio)  # open img_bytesio as PIL object

        img_width, img_height = img.size
        if img_width > 200 or img_height > 200:  # image is too large
            await message.answer(cat_too_large_image)
            if img_width > img_height:
                scale = img_width / img_height
                new_width = 200
                new_height = round(200 / scale)
                img = img.resize((new_width, new_height))
            else:
                scale = img_height / img_width
                new_height = 200
                new_width = round(200 / scale)
                img = img.resize((new_width, new_height))

        await message.answer(image_processing_msg)  # answer to user that something happening
        await process_image(img)  # refine image

    else:
        await message.answer(cat_wrong_format)  # if file is not an image answer to user


# message help handler
@dp.message_handler(Command("help"), state="*")
async def message_help(message: Message, state: FSMContext, from_start=False):
    if not from_start:  # remove keyboard if not from start
        await message.answer(helper_call, reply_markup=remove_keyboard)  # answer that helper is called
    await message.answer(help_msg,  # show list of commands
                         reply_markup=help_markup)
    try:
        await message.edit_reply_markup(reply_markup=None)  # remove inline keyboard if possible
    except Exception:
        pass
    finally:
        if state is None:
            return
        # get current state and if None exit
        current_state = await state.get_state()
        if current_state is None:
            return

        logging.info(f"Cancelling state {current_state}")  # logging which state was cancelled
        await state.finish()


# callback help handler
@dp.callback_query_handler(help_callback.filter(command="help"), state="*")
async def call_help(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)  # cache callback
    logging.info(f"call = {callback_data}")  # logging callback data
    await message_help(call.message, state=state)  # handle to message help handler


# cancel handler
@dp.message_handler(text="Отмена", state="*")
async def cancel(message: Message, state: FSMContext):
    await message.answer(cancel_msg, reply_markup=remove_keyboard)  # cancelling message

    # get current state and if None exit
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info(f"Cancelling state {current_state}")  # logging which state was cancelled
    await state.finish()


# unknown messages handler
@dp.message_handler()
async def unknown(message: Message):
    logging.info(f"unknown command = {message.text}")  # logging unknown command
    await message.answer(unknown_msg)  # tell user that bot does not know such command
