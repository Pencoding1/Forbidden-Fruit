label route2:
    scene bedhop2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15)
    hide char_x1
    show char1scared at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15):
        xalign 0.0
    show char_x2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15):
        xalign 1.0
    "Cả hai người" "{size=50}{b}HẢ?!{/b}"
    "Cả hai người đều tỏ vẻ nghiêm trọng."
    scene bedhop2 with fade
    show char_x1
    x1 "Cậu hãy đi ra ngoài đi. Việc này hãy để tôi giải quyết."
    play sound hoot
    "Bác sĩ Toshihida quay sang chàng y tá đang tỏ vẻ lúng túng rồi nói. Dứt lời nam y tá trẻ tuổi lập tức bước ra ngoài."
    x1 "Cậu Kinjiru. Tôi khuyên cậu nên báo chính quyền đi. Bởi vì cậu biết mà phụ nữ và đàn ông là những mầm bệnh của nhau. Nếu họ biết cậu..."
    "Anh ta tỏ vẻ ngập ngừng như không muốn nói."
    scene wall with dissolve
    play music bg2 fadein 0.5 volume 0.5
    "{cps=20}Yêu đương là một căn bệnh. Một căn bệnh ngọt ngào nhưng chết chóc.{/cps}"
    "{cps=20}Bởi thế bức tường ngăn cách thế giới làm hai phần mới được dựng lên.{/cps}"
    "{cps=20}Hai phần của loài người được sống tách biệt nhau. Một bên cho nam giới, bên còn lại là địa phận của phụ nữ.{/cps}"
    "{cps=20}Điều cơ bản đến mức trẻ con cũng phải biết.{/cps}"
    scene bedhop2 with fade
    show char_x1
    "...Nếu như bọn họ mà biết cậu bao che cho cô ta thì hai người sẽ bị xử tử đấy."
    menu:
        "Tôi không nghĩ là tôi sẽ làm thế.":
            pass
        "Tôi cũng đã suy nghĩ tới rồi. Có lẽ tôi nên báo chính quyền.":
            x1 "Đúng vậy. Thôi để tôi liên hệ với bên cảnh sát đến, cậu cứ nằm nghỉ ở đây đi."
            show black with dissolve
            "Sau khi lấy lời khai từ tôi thì cảnh sát đã đi điều tra ngay. Ít lâu sau thì tôi nhận được tin người ta đã bắt được cô gái ấy trong nhà tôi."
            jump gameover
    x1 "Tại sao chứ? Cậu có thể chết cùng với cô gái ấy đấy. Thậm chí cậu còn chả biết đến cô ta mà phải chứ?"
    main "Phải nhưng có thứ gì đó trong tôi nói rằng tôi không nên làm thế."
    x1 "Thứ gì cơ chứ?"
    main "Tôi không biết. Nhưng có thể nó là sự tò mò."
    x1 "Tò mò? Này đừng nói là cậu..."
    main "Không phải. Đây không phải là yêu. Tôi dám khẳng định điều đó."
    x1 "..."
    "Bác sĩ Toshihida thở dài. Anh ta tỏ vẻ bỏ cuộc."
    x1 "Thôi đó là ý của cậu. Tôi cũng không hẳn là ủng hộ cậu nhưng dưới danh nghĩa là một bác sĩ thì tôi không thể để cho ai phải chết cả."
    x1 "Tuy vậy. Nếu nhỡ như cậu bị bắt thì cũng đừng nói tôi có liên quan được chứ?"
    main "Được thôi. Miễn là anh đừng nói việc này ra là được."
    x1 "Bây giờ chúng tôi cần giữ cậu một thời gian để theo dõi. Giờ tôi phải đi rồi."
    x1 "À nếu cậu thấy không khỏe thì nhớ uống một viên thuốc trên bàn nhé. Một viên thôi đấy."
    "Rồi bác sĩ Toshihida bước ra ngoài. Trước khi đi anh để lại trên bàn một hộp thuốc."
    play sound footstep
    hide char_x1 with dissolve
    pause (2)
    stop sound
    "???" "Bạn có uống viên thuốc đó không?"
    menu:
        "Có":
            main "Uống một viên thôi nhỉ?."
            pass
        "Không":
            main "Chắc vẫn chưa cần thiết. Ngủ tý thì khỏe thôi."
            $ h -= 1
        "Uống năm viên":
            main "Cơ thể đau quá nên uống nhiều chút chả sao đâu nhỉ?"
            scene black with fade
            "Bạn đã chết do tim ngừng đập vì uống quá nhiều thuốc."
            jump gameover
    stop music
    scene black with fade
    pause(3)
    scene bg_house with dissolve
    main "Cuối cùng cũng thoát khỏi cái nơi toàn mùi thuốc khử trùng ấy."
    "Sau khi giữ tôi lại vài ngày trong bệnh viện thì đám người đó cuối cùng cũng cho tôi về nhà."
    "Tôi tra chìa khóa vào ổ khóa và mở cánh cửa gỗ có phần hơi cũ kỹ ra. Bên trong vẫn bừa bộn như ngày nào."
    play sound opendoor
    "Lý trí tôi như bị bào mòn, tất cả cảm giác không còn hoạt động. Không còn có thể kiểm soát."
    "Nhưng bỗng có một thứ gì đó làm tôi có cảm giác không thoải mái."
    "Tôi đưa lưỡi ra phía răng cửa và cắn thật mạnh nhằm lấy lại chút tỉnh táo."
    "Tôi nuốt lấy nước bọt cùng máu trên đầu lưỡi vào bên trong cái cổ họng đau rát, từ từ bước vào bên trong phòng khách."
    "Ý thức tôi đã trở lại một chút. Đủ để tôi cảm nhận được thứ khiến tôi khó chịu"
    main "Mùi gì thế này?"
    stop music
    #scene gcut3 with dissovel
    pause (2)
    "!!!"
    "Mùi hương dịu nhẹ phảng phất khắp căn phòng bừa bộn."
    "Một dòng suối màu đen mượt mà chảy ra khỏi mũ áo và trải đều ra xung quanh."
    "Ngay giữa phòng bỗng nhiên tỏa sáng lạ kỳ, ánh sáng như chiếu thẳng từ trên xuống tỏa ra rực rỡ khắp căn phòng."
    "Từ dưới mặt đất tắm mình trong ánh sáng, những bông hoa màu hổ phách mọc lên cùng những nhúm cỏ xanh tươi."
    "Cô gái đó, cô gái mà tôi từng bắt gặp trên đường..."
    "Giờ đây đang nằm giữa nhà tôi và ngủ say sưa như một cô công chúa ngủ trong rừng."
    "Tôi uống thuốc quá liều nên sinh ảo giác à?"
    "Mong là vậ...{b}LÀM GÌ CÓ CHUYỆN ĐÓ CHỨ!!!"
    "Đây là {b}THẬT{/b}, không có chút ảo tưởng và cảm giác này là {b}THẬT{/b}, không chút ngụy biện."
    main "Cái gì thế này?"
    "Vì sao cô gái này lại ở đây, vì sao cô ta nằm ngay giữa phòng tôi, tôi không biết. Tôi chỉ biết rằng đây hẳn chẳng phải điều tốt lành gì."
    "Tôi có nên giữ cô ta lại?"
    menu:
        "Đuổi cô ta đi":
            "Tuy tôi đã giúp cô ta một lần nhưng tôi không muốn chuốc quá nhiều phiền phức vào người."
            "Tôi gọi cô ta dậy nhưng không thấy phản hồi. Vì vậy tôi đã mang cô ta ra đường."
            "Sáng hôm sau thì đã mất tăm. Cô ta có lẽ đã tự đi đâu đó."
            jump gameover
        "Giữ lại.":
            pass
    "Có lẽ tôi nên báo chính quyền như lời người bác sĩ đã nói. Tôi nên làm điều đó, nó tốt hơn cho tôi. Tuy vậy..."
    "Có thứ gì đó trong tôi đang ngăn cản tôi làm việc đó. Một thứ gì đó mờ ảo và khó đoán. Một loại cảm xúc không thể mô tả."
    "Nhưng tôi không muốn chấp nhận thứ cảm xúc mơ hồ và đầy đau đớn này."
    "Dù sao thì tôi cũng sẽ giữ lại cô gái này vì sự tò mò. Giờ tôi nên làm gì với cô ta đây."
    "Nhưng... ít nhất cũng phải nằm trong giường của tôi đi chứ?"
    menu:
        "Bế cô gái vào phòng ngủ":
            "Tôi bế người cô gái đó lên. Cẩn thận không để da thịt tôi chạm vào cô ấy."
            "Vì cô ta khá nhẹ nên việc tôi mang cô vào phòng ngủ có vẻ nhanh chóng hơn. Đặt cô xuống chiếc giường của mình rồi tôi nhìn cô ta một lát."
            pass
        "Cứ để cô ta nằm đó.":
            "Thôi tốt nhất cứ để cô ta nằm ở yên đó."
    "Mà khoan đã, làm sao mà cô ta qua được bên kia bức tường chứ? Hơn nữa, ngay từ đầu thì cô ta vào nhà tôi kiểu gì?? Tôi có nên hỏi cô ta?"
    menu:
        "Gọi cô gái dậy.":
            jump callgirl
        "Tôi nên tự tìm hiểu thì hơn":
            pass
    $ end += 1
    return