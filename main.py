#press a to start music
def on_button_pressed_a():
    music.play(music.string_playable("C C D C F E - - ", 140),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C C D C G F - - ", 140),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C C C5 A F E D - ", 140),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("F F E C D C C C ", 140),
        music.PlaybackMode.UNTIL_DONE)

input.on_button_pressed(Button.A, on_button_pressed_a)

#press b to skip to next part 
def on_button_pressed_b():
    music.stop_all_sounds()

input.on_button_pressed(Button.B, on_button_pressed_b)