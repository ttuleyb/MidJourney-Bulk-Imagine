from pynput.mouse import Button, Controller
import time
from AppKit import NSWorkspace
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()

prompts = """
stairway to the end of time
a dragonfly resting on a leaf, flowers, summer, lily pads, bright sunlight, vector illustration, fantasy, 8k --ar 2:7 --uplight --ar 9:16
a crystal synthwave unicorn horn, art deco, crystal, fantasy, abstract, 8k --ar 7:1
surreal looking futuristic architecture, futuristic cityscape, glowing neon lights, hyper realism, 8k, volumetric lighting, photorealistic, octane render, unreal engine, 8k --ar 3:6
a glowing sphere of light surrounded by energy pulsating in all directions, cosmic, futuristic, glowing, hyper-realistic, octane render, 8k, volumetric lighting, high resolution, 8k --ar 2:3
a beautiful stained glass window in a dark cathedral, realistic lighting, high resolution render, hyper realism --upbeta
a detailed close up of a tree that is covered in moss and has a magical glow around it, surreal, 8k, hyper realistic --ar 2:3
crystal synthwave dress, red, magical, octane render, hyper realistic --ar 9:16
a goldfish bowl full of iridescent jellyfish glowing softly under the light, underwater, magical, 8k, octane render, 8k --ar 7:14
a crystal orb floating in space, cosmic background, nebula, diffuse lighting, 8k --ar 3:8
rose quartz and diamond necklace, crystal synthwave, fantasy, 8k
a beautiful ancient chinese pagoda at night, illuminated by a single lantern hanging from its top, realistic lighting, high resolution render, hyper realism, octane render --ar 3:9 --q 2 --uplight --s 10000
an ancient Egyptian pyramid with stars and moons, pyramids, pyramid city, pyramids, high resolution render, HD octane render, unreal engine, 8k, hyper-realism, photorealistic, volumetric lighting, volumetric fog, --ar 2:3
a beautiful young woman resting her head against the back of a chair in a lovely living room, dreamy, surreal, 8k --iw 0.25 --q 2 --uplight --ar 2:3
a glowing light bulb hanging from the ceiling, a very bright light source, very detailed, high resolution render, real time, HDR, 8k --ar 2:3 --q 1
a translucent translucent staircase to heaven, golden, holographic, hyper-realistic, 8k, volumetric lighting, extremely detailed, crystal synthwave, very high quality, rendered by awesomeness, --ar 9:16
a very detailed 4k stained glass window of a castle, with a unicorn and a dragon, mythical creatures, rainbow colors, surrealism, octane render, raytrace, HD --ar 2:6
a surrealist painting of a woman in a dark room looking up at a red neon sign with the words "I want you" written in glowing green letters, abstract, surrealism, optical illusion, 3d rendering, realistic rendering, hyper real, 8k, --aspect 10:16
a large golden statue of the Buddha in the style of Studio Ghibli, 8k, volumetric lighting, photorealistic, crystal synthwave, octane render, 8k --ar 2:3
a crystal synthwave lamp, glowing golden, fantasy, octane render, cinematic, clean lines, hyper detailed, 8k --iw 0.25 --q 2 --uplight --ar 9:16
a triskelion with the sun rising over it, 3D origami, geometric, abstract, hyper realistic, octane render, 8k --ar 2:2
a green glowing orb of energy emitting from the center of a purple crystal, abstract, surreal, hyper realism, octane render, 8k --ar 2:3
the god of light fractal :: damask ornate, intricate and precise :: church of the abyss, universe of light :: sacred temple of synthwave tessellation, hyperreal, octane render --ar 2:3 --uplight --s 15000
a black and white photo of a woman wearing a dress made out of leaves, green, surrealism, octane render, 8k --iw 0.25 --q 2 --uplight --ar 9:16
a mystical stone statue of an ancient goddess holding a sphere, floating in the air, surrounded by a golden halo, in the style of studio ghibi, surrealism, 8k --aspect 10:16
a treehouse in the middle of a fairy forest, glowing, magical, octane render, hyper realistic --ar 2:6 --q 2 --uplight --ar 9:16
a beautiful hyper-realistic golden unicorn standing in front of a giant red sun, golden unicorn, unicorns, golden sun, sunset, fantasy, 8k --iw 0.
a crystal synthwave lamp, sub surface scattering, ray trace, unreal engine render 4k --ar 2:3 --q 1
a beautiful girl in a pink dress, swimming underwater in a pool of water, octane render, realistic, 8k --iw 0.25 --q 2 --uplight --ar 9:16 --s 5000
a tableau vivant of a princess in a glass bubble floating through a magical synthwave fairy forest with fireflies, pastel synthwave —chaos 5 —ar 9:16
a white marble tower ascending into space, with infinite opulent gilded balconies on every floor, waterfalls, wondrous, volumetric lighting, epic scene, 8k, volumetric lighting, highly detailed, Octane Render, Unreal Engine --ar 3:8 --q 2
A magical girl costume from the anime series Fairy Tail by Hiro Mashima,  Japanese, manga, anime, anime girls, fantasy, 8k --ar 9:16
a black cat with glowing eyes, feline, 8k, hyper-realistic, photorealistic, photogrammetry, volumetric lighting, highly detailed, Octane Render, unreal engine, 8k --ar 8:11 --q 2
a black and white photo of a woman wearing a face mask in a dark room, she looks very mysterious and beautiful, surreal, artistic, 8k --aspect 9:16
a magical golden unicorn sitting under a purple moon in a rainbow field, glowing and glittering, beautiful, fantasy, 8k --aspect 9:16
mystical and magical fairies dancing in the moonlight, colorful, dreamlike, surreal, 8k, high detail, hyper realistic, rendered by awesomeness, Octane Render, unreal engine --ar 9:16
interdimensional galaxy portal covered in frost, ice gate, volumetric light, volumetric fog, unreal engine, photorealistic, 8k --ar 7:20 --q 2
A rainbow prism that is half-transparent and shimmers with light, mystical, magical, optical illusion, color, optics, light, beauty, infinity, holographic, hyper-realistic, 8k, qv, hd, --ar 9:16
A magical magical unicorn flying through the night sky over a magical rainbow, 8k, --ar 9:16
The Northern Lights, aurora borealis, cosmic landscape, aurora, northern lights, northern lights, aurora borealis, aurora borealis, lights, space, cosmos, universe, stars, galaxies, space, sky, nebula, nebula, 8k, qv, hd, --ar 9:16
The most beautiful woman in the world, a portrait of Marilyn Monroe, high resolution, high quality, cinematic, photorealistic, by Peter Lindbergh, 8k, high res, cinematic, photorealistic, 35mm --ar 9:16
highly detailed and intricate abstract flower, beautiful, vibrant, colorful, multicolored, large scale, 8k, ultra detail, ultra real, octane renderer, --ar 9:16
supernatural god of time, illustrious, dazzling, breathtaking, mirrors, glass, magic circle, magic door, fantasy, mist, bioluminescence, hyper-realistic, + wide angle realistic atmospheric cinematic lighting octane highly detailed render in acrylic painting style + 3d octane render + unreal engine 5 + Cinema4D
The girl who was taken up into the sky by the moon, by Hokusai, Japanese woodblock print, printmaking technique, artistic style, art, watercolour, ink, pencil, sketch, portrait, painting, anime, manga
crystal palace, dreamy, mysterious, mystical, magic, enchanted, fantasy, enchanted world, fantasy garden, fairy tale, enchanted forest, surrealistic, 8k, photorealistic, hyper realistic, surrealistic
stairway to heaven, beautiful, stunning, breathtaking, mirrors, glass, magic circle, magic doorway, fantasy, stained glass, bioluminescence, hyper-realistic, 8k, unreal engine, pattern, fractal --ar 9:16 --s 10000
Reverie stairs, family gathering, surrounded by flowers with matching furniture, place for candles, vines and birds up against the wall, golden light shining through from above (golden shimmer). Fantasy setting inspired by Romanticism and Gothic Revival in art and architecture. Fantasy flooring with veins and branches rising to the high ceiling (floral) with ancient frescoed walls.
the last supper, 12th century, Christ looking at us, with the lilies, vibrant colors, realistic, photorealistic, multilayered, high resolution wallpaper format, 8k
the last supper in a strip club, incredible props, Crystal synthwave, rustic, medieval, ambient lighting, superb effects animation, realism, liquid motion | fluid dynamics
magical spiral stairway to the Goddess's throne room --ar 7:45 --q 5 --s 2250
the last supper in a dark lit nightclub, DJ performing on stage, jesus dancing, strobe lights, fog effect, Cinematic, Wide Angle, Cool Color Palette, Complimentary-Colors, 4k, Happy, Excited, Strobe Light, Beautiful Lighting, crabs dancing, octane render --q 5 --s 5000 --ar 16:9
On the road to nowhere, no destination, abandoned warehouse, empty railroad tracks, desolated wasteland, mountains, trees, snow, desert, a flying car, airborne fortress, urban ruins—ar 5:8 --q 5 --uplight --s 5000
World's biggest Lie Detector
A perfect photo of the Earth from space, seen from the Moon, with the continents and oceans clearly visible, and the Moon's shadow cast over the Earth. The image is so clear that it looks like you can reach out and touch the Earth.
"""
from screen_capture import ScreenPixel

promptList = []
index = 0

for i in prompts.split("\n"):
    if len(i) > 2:
        promptList.append(i)

sp = ScreenPixel()

def check_queue():
    time.sleep(2)
    sp.capture()
    result = sp.pixel(772, 1298)
    print(result)
    if result == (228, 195, 122, 255):
        return "yellow"
    elif result == (223, 49, 33, 255):
        return "red"
    elif result == (234, 51, 35, 255):
        return "red"
    elif result == (240, 205, 128, 255):
        return "yellow"
    else:
        return "white"

def write_next_prompt():
    wait_for_discord()
    global index
    if index > len(promptList) -1:
        print("Done")
        exit()

    mouse.position = (561.0625, 797.4492187)
    mouse.click(Button.left, 1)

    keyboard.type("/imagine")
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.type(promptList[index])
    index += 1
    time.sleep(0.5)
    keyboard.press(Key.enter)

def wait_for_discord():
    if NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] != "Discord":
        print("Waiting for discord...")
        while NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] != "Discord":
            time.sleep(5)

#main loop
while True:
    wait_for_discord()
    queue = check_queue()
    print(queue)
    if queue == "red":
        index -= 1
        print("Retrying in 10 minutes: " + promptList[index])
        time.sleep(600)
    elif queue == "yellow":
        print("Retrying in 20 seconds: " + promptList[index])
        time.sleep(0)
    print(index)
    print("Next: " + promptList[index])
    write_next_prompt()
    