import board
import neopixel

from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
import adafruit_led_animation.color as color
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence

pixel1_pin = board.D13
pixel1_num = 50
pixel2_pin = board.D12
pixel2_num = 50

pixels1 = neopixel.NeoPixel(pixel1_pin, pixel1_num, brightness=0.5, auto_write=False)
pixels2 = neopixel.NeoPixel(pixel2_pin, pixel2_num, brightness=0.5, auto_write=False)

solid1 = Solid(pixels1, color=color.WHITE)
solid2 = Solid(pixels2, color=color.GREEN)
rainbow1 = Rainbow(pixels1, speed=0.1, period=2)
rainbow1_chase = RainbowChase(pixels1, speed=0.1, size=5, spacing=3)
rainbow1_comet = RainbowComet(pixels1, speed=0.1, tail_length=7, bounce=True)
rainbow1_sparkle = RainbowSparkle(pixels1, speed=0.1, num_sparkles=15)
rainbow2 = Rainbow(pixels2, speed=0.1, period=2)
rainbow2_chase = RainbowChase(pixels2, speed=0.1, size=5, spacing=3)
rainbow2_comet = RainbowComet(pixels2, speed=0.1, tail_length=7, bounce=True)
rainbow2_sparkle = RainbowSparkle(pixels2, speed=0.1, num_sparkles=15)

rainbow = AnimationGroup(solid1, rainbow2)
rainbow_chase = AnimationGroup(rainbow1_chase, solid2)
rainbow_comet = AnimationGroup(rainbow1_comet, solid2)
rainbow_sparkle = AnimationGroup(solid1, rainbow2_sparkle)

animations = AnimationSequence(
    rainbow,
    rainbow_chase,
    rainbow_comet,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
