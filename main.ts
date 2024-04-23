// press a to start music
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.play(music.stringPlayable("C C D C F E - - ", 140), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C C D C G F - - ", 140), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C C C5 A F E D - ", 140), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("F F E C D C C C ", 140), music.PlaybackMode.UntilDone)
})
// press b to skip to next part 
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.stopAllSounds()
})
