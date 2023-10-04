from discord.ext.commands import Bot
import os
# from keep_alive import keep_alive
from time import sleep
from flask import Flask, render_template
from threading import Thread
import os

app = Flask(__name__)


@app.route('/')
def index():
  return "Alive"


def run():
  app.run(host='0.0.0.0', port=8080)


bot = Bot(command_prefix="..", self_bot=False, chunk_guilds_at_startup=False)


async def all9(msg: int):
  for i in range(0, 3):
    await msg.components[0].children[i].click()
    sleep(0.4)
  for i in range(0, 3):
    await msg.components[1].children[i].click()
    sleep(0.4)
  for i in range(0, 3):
    await msg.components[2].children[i].click()
    sleep(0.4)


channell = 1153540723082272798
harvest = 1153848401302126685
hoe = 1153848467442122842
water = 1153848548807409716
plant = 1153849222827868222


@bot.event
async def on_ready():
  print('I am ready')
  channel = bot.get_channel(channell)
  harvestM = await channel.fetch_message(harvest)
  hoeM = await channel.fetch_message(hoe)
  waterM = await channel.fetch_message(water)
  plantM = await channel.fetch_message(plant)
  sleep(3)
  await harvestM.components[3].children[0].click()
  sleep(3)
  await all9(hoeM)
  sleep(3)
  await all9(waterM)
  sleep(3)
  await all9(plantM)
  os._exit(0)


# keep_alive()
sleep(5)


def r():
  bot.run("MTE0NzQ4ODA4NjcwMDM0MzM5Nw.G5MTv8.FXmbeP0Kgkx3wt9S4o9clM5KvqzM5_L0KbJLbs")


t = Thread(target=run)
t.start()
y = Thread(target=r)
y.start()

print('on run')
sleep(200)
os._exit(0)
