label chap1:
    scene black with fade
    pause (3)
    show num1 with dissolve
    pause (2)
    show num2 with dissolve
    pause (2)
    scene gcut1 with fade
    play sound hearbeat
    "...."
    scene black with fade
    play sound passing
    "Bộp..."
    scene black with fade
    pause (2.5)
    scene bedhop2 with dissolve
    pause (2)
    scene bedhop2 with fade
    scene bedhop2 with fade
    "???" "Cuối cùng cậu cũng dậy rồi à?"
    main "!!!"
    play music bg3 volume 0.75
    show char_x1 with dissolve
    main "..."
    "???" "Ahaha. Chắc cậu bất ngờ lắm nhỉ?"
    menu:
        "Đây là đâu thế? Và anh là ai?":
            pass
    x1 "Tôi là Toshihida Hime. Gọi tôi là bác sĩ Toshihida cũng được. Cậu đang ở bệnh viện đấy, vừa nãy có người đi đường thấy cậu bất tỉnh nên mang tới đây."
    main "Vậy à..."
    stop music fadeout 1.0
    hide char_x1
    play sound hardopen
    "Đột ngột cánh của phòng bật mở."
    play sound hoot
    show char_x2 with fade:
        xalign 0.5
    "Từ phía ngoài, một y tá trẻ tuổi hối hả chạy vào với xấp giấy trên tay."
    "Người của anh nhễ nhại mồ hôi. Có lẽ anh ta đã phải chạy rất nhanh."
    x2 "Bác sĩ Toshihida! Đã có kết quả xét nghiệm của bệnh nhân. A...anh ta tỉnh rồi à."
    show char_x1:
        xalign 0.0
    x1 "Vậy à? Đưa tôi xem nào."
    "Anh chàng y tá nhanh chóng đưa xấp giấy cho bác sĩ Toshihida. Mặt tỏ vẻ đầy lo lắng."
    play sound paper
    "Soạt..."
    hide char_x2
    hide char_x1 with dissolve
    show char1worry:
        xalign 0.5
    play sound paper
    play sound paper
    "Soạt...soạt..."
    x1 "..."
    play music bg0 fadein 1.0
    "Bác sĩ nhìn vào xấp giấy một hồi lâu, và rồi, trong khi ánh mắt của ông lướt trên những dòng chữ, khuôn mặt của ông cũng dần biến sắc."
    "Đoạn ông quay sang tôi."
    x1 "Kinjiru nhỉ? Tôi hỏi cậu một số thứ được chứ?"
    main "Vâng..."
    x1 "Dạo này cậu có cảm thấy kỳ lạ không? Đại loại như là hay nhìn vào gương. Hoặc có cảm giác kỳ lạ khi nói chuyện với bạn cùng lớp chẳng hạn."
    x1 "Nếu không liệu cậu..."
    "Bác sĩ Toshihida đột ngột làm vẻ mặt nghiêm trọng. Ông ngập ngừng nói."
    x1 "Có từng gặp cô gái nào không?"
    scene gc2 with fade
    play sound hearbeat
    main "Ư..."
    scene bedhop2
    show char_x1
    "{i}Ký ức của tôi thật sự không rõ ràng cho lắm nhưng hình như tôi đã gặp một người trông như một cô gái."
    menu:
        "Ký ức của tôi khá mờ nhạt. Tôi cũng không chắc nhưng có lẽ tôi đã gặp một cô gái":
            jump route2
        "Không tôi chẳng thấy cô gái nào cả. Với lại tôi cũng không thấy kỳ lạ gì hết.":
            pass
    stop music fadeout 1.0
    main "Vậy à. Đúng là vậy nhỉ, may thật."
    play music bg4 fadein 1.0
    #show char_x1_happy
    "Người bác sĩ thở phào nhẹ nhõm. Anh ta quay sang chàng y tá trẻ cũng đang tỏ vẻ như vừa trút đi gánh nặng."
    x1 "Chắc có sai sót gì rồi. Cậu nên đi kiểm tra lại đi"
    "Anh chàng y tá gật đầu rồi bước đi ra khỏi phòng."
    play sound hoot
    hide char_x2 with dissolve
    show char_x1:
        xalign 0.5
    "Rồi bác sĩ Toshihida quay sang tôi."
    x1 "Cậu cũng biết rằng phụ nữ và đàn ông đều là những mầm bệnh của nhau mà nhỉ? Vì vậy mà mới có bức tường kia."
    scene black with dissolve
    scene wall with fade
    play music bg2 fadein 0.5 volume 0.5
    "{cps=20}Yêu đương là một căn bệnh. Một căn bệnh ngọt ngào nhưng chết chóc.{/cps}"
    "{cps=20}Bởi thế bức tường ngăn cách thế giới làm hai phần mới được dựng lên.{/cps}"
    "{cps=20}Hai phần của loài người được sống tách biệt nhau. Một bên cho nam giới, bên còn lại là địa phận của phụ nữ.{/cps}"
    "{cps=20}Điều cơ bản đến mức trẻ con cũng phải biết.{/cps}"
    scene bedhop2 with fade
    show char_x1
    main "Vâng..."
    x1 "Thôi sao cũng được, miễn không gặp phụ nữ là tốt rồi. Bây giờ chúng tôi cần giữ cậu một thời gian để theo dõi. Giờ tôi phải đi rồi."
    x1 "À nếu cậu thấy không khỏe thì nhớ uống một viên thuốc trên bàn nhé. Một viên thôi đấy."
    "Rồi bác sĩ Toshihida bước ra ngoài. Trước khi đi ông để lại trên bàn một hộp thuốc."
    hide char_x1 with dissolve
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
    play sound opendoor
    "Tôi tra chìa khóa vào ổ khóa và mở cánh cửa gỗ có phần hơi cũ kỹ ra. Bên trong vẫn bừa bộn như ngày nào."
    "Lý trí tôi như bị bào mòn, tất cả cảm giác không còn hoạt động. Không còn có thể kiểm soát."
    "Nhưng bỗng có một thứ gì đó làm tôi có cảm giác không thoải mái."
    "Tôi đưa lưỡi ra phía răng cửa và cắn thật mạnh nhằm lấy lại chút tỉnh táo."
    "Tôi nuốt lấy nước bọt cùng máu trên đầu lưỡi vào bên trong cái cổ họng đau rát, từ từ bước vào bên trong phòng khách."
    "Ý thức tôi đã trở lại một chút. Đủ để tôi cảm nhận được thứ khiến tôi khó chịu"
    main "Mùi gì thế này?"
    #scene gcut3 with dissovel
    pause (2)
    "!!!"
    play music bg7 fadein 0.5
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
            "Tôi gọi cô ta dậy nhưng không thấy phản hồi. Vì vậy tôi đã quăng cô ta ra đường."
            "Sáng hôm sau thì cô ta có lẽ đã tự đi đâu đó."
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