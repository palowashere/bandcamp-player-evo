# coding=utf-8
import logging
import sys
import numpy as np
import json

from bandcamp_parser.tag import Tag
from bandcamp_parser.track import Track

logging.basicConfig(level=logging.INFO)
tags_all = ["electronic", "experimental", "alternative", "rock", "hip-hop/rap", "ambient", "metal", "punk", "indie", "noise", "techno", "indie rock", "pop", "instrumental", "hip", "hop", "drone", "rap", "folk", "acoustic", "house", "electronica", "psychedelic", "singer-songwriter", "hardcore", "dark ambient", "lo-fi", "industrial", "jazz", "alternative rock", "hip-hop", "indie pop", "experimental electronic", "world", "electro", "beats", "lofi", "black metal", "soundtrack", "post-punk", "deep", "house", "post-rock", "punk", "rock", "soul", "downtempo", "shoegaze", "death metal", "funk", "dance", "minimal", "avant-garde", "idm", "synthwave", "improvisation", "vaporwave", "blues", "progressive", "drum & bass", "emo", "synthpop", "dub", "indie folk", "trap", "synth", "underground hip hop", "r&b", "underground", "ambient electronic", "folk rock", "piano", "instrumental hip-hop", "garage", "electronic music", "dubstep", "tech house", "harsh noise", "americana", "chillout", "pop rock", "guitar", "chill", "soundscape", "classical", "progressive rock", "psychedelic rock", "hardcore punk", "pop punk", "atmospheric", "grunge", "edm", "garage rock", "psytrance", "dream pop", "trance", "reggae", "hard", "rock", "country", "hiphop", "grindcore", "bass", "trip", "hop", "diy", "darkwave", "doom", "noise rock", "acid", "glitch", "new wave", "devotional", "experimental rock", "post-hardcore", "dark", "r&b/soul", "heavy metal", "experiemental", "new age", "spoken word", "thrash metal", "sound art", "field recordings", "disco", "breakbeat", "doom metal", "jungle", "electroacoustic", "world", "music", "free jazz", "cinematic", "meditation", "metalcore", "rock & roll", "breaks", "chiptune", "progressive metal", "bedroom pop", "chillwave", "orchestral", "boom bap", "acoustic guitar", "fusion", "drone ambient", "stoner rock", "music", "instrumentals", "musique concrete", "alternative pop", "black-bandcamp", "blues rock", "soundscapes", "power pop", "electropop", "comedy", "sludge", "bass music", "alt-country", "free improvisation", "abstract", "breakcore", "roots", "melodic", "deep", "goth", "art rock", "contemporary", "progressive house", "space", "harsh noise wall", "power electronics", "dungeon synth", "math rock", "stoner", "ebm", "rave", "latin", "experimental hip-hop", "drum and bass", "live", "psych", "retrowave", "folk punk", "poetry", "space rock", "techno.", "krautrock", "garage punk", "dub techno", "plunderphonics", "psychedelic trance", "alternative hip-hop", "minimalism", "remix", "improv", "improvised music", "minimal techno", "independent", "dnb", "gothic", "hip hop instrumentals", "surf", "80s", "samples", "ska", "beat tape", "deep techno", "synthesizer", "modern classical", "post-metal", "bedroom", "house music", "atmospheric black metal", "rock and roll", "weird", "nu disco", "avant garde", "screamo", "christian", "spiritual", "synth pop", "folk pop", "prog", "film", "music", "experimental pop", "crust", "groove", "horror", "acoustic rock", "songwriter", "contemporary classical", "underground rap", "thrash", "avantgarde", "hard techno", "boombap", "field recording", "neo-soul", "powerviolence", "video game music", "video game", "loops", "prog rock", "dreampop", "noise pop", "classic rock", "grime", "improvised", "neoclassical", "rnb", "minimalist", "female vocals", "tokyo,japan", "chillhop", "drums", "jam", "retro", "heavy", "deathcore", "instrumental rock", "post rock", "noisecore", "jazz fusion", "rap & hip-hop", "dance music", "lounge", "vocal", "cassette", "tape", "raw black metal", "jazzy", "sample-based", "sad", "indiepop", "jazz and improvised music", "hnw", "space music", "leftfield", "deep tech", "soulful", "cyberpunk", "sound collage", "analog", "industrial techno", "heavy rock", "stoner metal", "future bass", "melodic hardcore", "love", "christmas", "surf rock", "free", "dancehall", "post punk", "funky", "neo-classical", "meditative", "microhouse", "sludge metal", "club", "holland", "bluegrass", "djent", "art", "witch house", "swing", "grind", "progressive trance", "melodic death metal", "coldwave", "future funk", "gospel", "punkrock", "easy listening", "rock'n'roll", "relaxation", "chill out", "beat", "footwork", "tribal", "piano solo", "relaxing", "modular", "post-industrial", "triphop", "rock n roll", "dreamy", "ethereal", "punk hardcore", "traditional", "glitch hop", "ambient rock", "postrock", "depressive suicidal black metal", "suicidal black metal"]

def loop():
    """ Playing tracks in infinite loop """
    if (len(sys.argv) == 1):
        tag_data = true_chaos()
    if (len(sys.argv) == 2):
        print("random location selected")
        tag_data = chaotic_good(0) 
    else:
        # so far this works only for 1 genre and 1 location
        if (len(sys.argv) >= 3):
            tag_data = Tag(sys.argv[1], sys.argv[2]) 
            print_info(sys.argv[1], sys.argv[2])

    while True:
        album_url = tag_data.album_random()
        print(f"playing from album {album_url}")
        track = Track(album_url)
        track.play()


def true_chaos():
    print("true chaos reigns...")
    [genre] = np.random.choice(tags_all, size=1, replace=False)
    tag_data = Tag(genre, 0)
    print_info(genre, 0)  
    return tag_data


def mild_chaos():
    tag_data = Tag(sys.argv[1], 0)
    print_info(sys.argv[1], 0) 
    return tag_data


def chaotic_good(location):
    tag_data = Tag(sys.argv[1], location)
    print_info(sys.argv[1], location) 
    return tag_data


def print_info(genre, location):
    print("playing ---> " + genre)
    print("from ------> " + str(location))


def main():
    """ Playing the tracks until CTRL-C """
    try:
        loop()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
