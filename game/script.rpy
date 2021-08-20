call splashscreen from _call_splashscreen
label start:
    call opening from _call_opening
    call chap1 from _call_chap1
    if end == 1:
        call end from _call_end
    if chap2 == 1:
        stop music
        call transformchap2
        call chap2 from _call_chap2
return
label gameover:
    "Game Over"
return
