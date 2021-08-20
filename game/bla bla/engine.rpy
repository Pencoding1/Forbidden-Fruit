label opening:
    label opening:
    stop music
    scene black with dissolve
    pause(2)
    play music "audio/ost1.ogg" volume 0.65 fadein (1)
    "{cps=20}Một căn bệnh không thể miêu tả bằng lời.{w} Tất cả chỉ như một khái niệm không thể xác định{/cps}"
    "{cps=20}Không nguyên nhân.{/cps}"
    "{cps=20}Không triệu chứng.{/cps}"
    "{cps=20}Chỉ thầm lặng đến...{w} rồi mang theo sinh mệnh của nạn nhân{/cps}"
    "{cps=20}Căn bệnh mang tên tình yêu{/cps}"
    "{cps=20}Nghe thật ngọt ngào. {w} Nhưng cũng thật tàn nhẫn.{/cps}"
    "{cps=20}Không có thuốc chữa.{/cps}"
    "{cps=20}Không thể kiểm soát.{/cps}"
    "{cps=20}Tuy vậy vẫn có duy nhất một cách để phòng tránh hoàn toàn{/cps}"
    "{cps=20}Thế giới này sẽ không tồn tại tình yêu.{/cps}"
    "{cps=20}Đại khủng hoảng đã được dập tắt sau hàng ngàn năm.{/cps}"
    "{cps=20}Khi thế giới đang dần hồi phục.{/cps}"
    "{cps=20}Mọi thứ giờ chỉ còn là lịch sử{/cps}"
    "{cps=20}Vậy nhưng một thế giới như vậy có đáng để tồn tại?{/cps}"
    "{cps=20}Thế giới không có tình yêu?{/cps}"
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
