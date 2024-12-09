screen quiz_1():
    hbox:
        xalign 0.5
        yalign 0.2
        spacing 100
        imagebutton:
            auto "images/quiz/quiz_1_1_%s.png"
            action Jump("jawaban_soal_1_1")
        imagebutton:
            auto "images/quiz/quiz_1_2_%s.png"
            action Jump("jawaban_soal_1_2")

screen quiz_2():
    imagebutton:
        auto "back_btn_ref_%s.png"
        action Jump("soal_quiz_2")
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        imagebutton:
            auto "images/quiz/quiz_2_1_%s.png"
            action Jump("jawaban_soal_2_1")
        imagebutton:
            auto "images/quiz/quiz_2_2_%s.png"
            action Jump("jawaban_soal_2_2")