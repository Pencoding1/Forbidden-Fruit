label opening:
    stop music
    scene black with dissolve
    pause(2)
    play music "audio/ost1.ogg" volume 0.65 fadein (1)
    scene bg_begin with fade
    show txt1 with dissolve
    pause (2)
    hide txt1 with dissolve
    show txt2 with dissolve
    pause (2)
    hide txt2 with dissolve
    show txt3 with dissolve
    pause (2)
    hide txt3 with dissolve
    show txt4 with dissolve
    pause (2)
    hide txt4 with dissolve
    show txt5 with dissolve
    pause (2)
    hide txt5 with dissolve
    show txt6 with dissolve
    pause (2)
    hide txt6 with dissolve
    show txt7 with dissolve
    pause (2)
    hide txt7 with dissolve
    show txt8 with dissolve
    pause (2)
    hide txt8 with dissolve
    show txt9 with dissolve
    pause (2)
    hide txt9 with dissolve
    show txt10 with dissolve
    pause(2)
    hide txt10 with dissolve
    show txt11 with dissolve
    pause (2)
    hide txt11 with dissolve
    show txt12 with dissolve
    pause(2)
    hide txt12 with dissolve
    show txt13 with dissolve
    pause (2)
    hide txt13 with dissolve
    show txt14 with dissolve
    pause (2)
    hide txt14 with dissolve
    stop music fadeout 1
    show txt15 with dissolve
    pause (2)
    hide txt15 with dissolve
    stop music fadeout 1
    show txt16 with dissolve
    pause (2)
    hide txt16 with dissolve
    stop music fadeout 1
    scene black with dissolve
    pause (2)
    return
label callgirl:
    main "Này. Tỉnh lại đi. Làm sao mà cô vào nhà tôi được thế?"
    "Cô gái" "..."
    main "Này, tỉnh lại đi nào."
    "Mặc dù tôi liên tục to tiếng gọi cô dậy nhưng cô nàng vẫn nằm bất động như không có gì xảy ra."
    main "Mình không thể chạm vào con gái được. Nhưng có vẻ là không có cách nào để làm cô ta tỉnh dậy nhỉ?"
    menu:
        "Đi ra ngoài tìm hiểu.":
            jump end
return
label transformchap2:
    scene black with fade
    pause(3)
    show txta with dissolve
    pause(1)
    hide txta
    show txtb with dissolve
    pause(2)
return
label my_shake:
  init:
    python:
        import math
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                return (int(nx), int(ny), 0, 0)
        def _Shake(start, time, child=None, dist=100.0, **properties):
            move = Shaker(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)
        Shake = renpy.curry(_Shake)
init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
return