style screentext:
    color "#f29c2cff"
    size 16
# The game starts here.

label start:
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    stop music fadeout 1.3
    jump prolog_pertama

label prolog_pertama:
    play music "BGM/All_Idle_Game_BGM.mp3" volume 0.7
    scene bg kamar_larasati
    narrator "[narator_text[0]]"
    show lolilaras_base at left
    with fade
    larasati "[text_prolog_larasati[0]]"
    larasati "[text_prolog_larasati[1]]"
    narrator "[narator_text[1]]"
    scene bg ruang_menjahit
    show sriyani_senyum at right
    show lolilaras_base at left
    with fade
    sriyani "[text_prolog_sriyani[0]]"
    larasati "[text_prolog_larasati[2]]"
    narrator "[narator_text[2]]"
    play sound "SFX/SFX_MesinJahit2.mp3" fadeout 1.3
    with dissolve
    larasati "[text_prolog_larasati[3]]"
    sriyani "[text_prolog_sriyani[1]]"
    sriyani "[text_prolog_sriyani[2]]"
    stop sound fadeout 0.5
    sriyani "[text_prolog_sriyani[3]]"
    larasati "[text_prolog_larasati[4]]"
    hide lolilaras_base
    with fade
    narrator "[narator_text[3]]"
    play sound "SFX/Kain2.mp3" fadeout 1.3
    with dissolve
    show lolilaras_base at left
    with fade
    larasati "[text_prolog_larasati[5]]"
    sriyani "[text_prolog_sriyani[4]]"
    sriyani "[text_prolog_sriyani[5]]"
    narrator "[narator_text[4]]"
    larasati "[text_prolog_larasati[6]]"
    sriyani "[text_prolog_sriyani[6]]"
    larasati "[text_prolog_larasati[7]]"
    sriyani "[text_prolog_sriyani[7]]"
    larasati "[text_prolog_larasati[8]]"
    narrator "[narator_text[5]]"
    larasati "[text_prolog_larasati[9]]"
    larasati "[text_prolog_larasati[10]]"
    narrator "[narator_text[6]]"
    sriyani "[text_prolog_sriyani[8]]"
    narrator "[narator_text[7]]"
    hide lolilaras_base 
    hide sriyani_senyum
    with dissolve
    scene bg kamar_larasati
    show lolilaras_base
    with fade
    play sound "SFX/kertas.mp3" fadeout 1.3
    narrator "[narator_text[8]]"
    narrator "[narator_text[9]]"
    hide lolilaras_base
    with dissolve
    narrator "[narator_text[10]]"
    scene bg ruang_menjahit
    show lolilaras_bahagia at left
    show sriyani_senang at right
    with fade
    larasati "[text_prolog_larasati[11]]"
    narrator "[narator_text[11]]"
    sriyani "[text_prolog_sriyani[9]]"
    show lolilaras_senang at left
    show sriyani_ketawa at right
    narrator "[narator_text[12]]"
    hide lolilaras_senang
    hide sriyani_ketawa
    with dissolve
    scene bg ruang_menjahit
    with fade
    narrator "[narator_text[13]]"
    show lolilaras_base at left
    show sriyani_senyum at right
    with fade
    larasati "[text_prolog_larasati[12]]"
    play sound "SFX/SFX_MesinJahit2.mp3" fadeout 1.3
    with dissolve
    sriyani "[text_prolog_sriyani[10]]"
    larasati "[text_prolog_larasati[13]]"
    stop sound fadeout 0.5
    larasati "[text_prolog_larasati[14]]"
    sriyani "[text_prolog_sriyani[11]]"
    larasati "[text_prolog_larasati[15]]"
    narrator "[narator_text[14]]"
    narrator "[narator_text[15]]"
    show sriyani_ketawa at right
    narrator "[narator_text[16]]"
    show sriyani_ketawav2 at right
    larasati "[text_prolog_larasati[16]]"
    sriyani "[text_prolog_sriyani[12]]"
    sriyani "[text_prolog_sriyani[13]]"
    show lolilaras_penasaran at left
    larasati "[text_prolog_larasati[17]]"
    sriyani "[text_prolog_sriyani[14]]"
    sriyani "[text_prolog_sriyani[15]]"
    sriyani "[text_prolog_sriyani[16]]"
    larasati "[text_prolog_larasati[18]]"
    sriyani "[text_prolog_sriyani[17]]"
    show lolilaras_bahagia at left
    larasati "[text_prolog_larasati[19]]"
    larasati "[text_prolog_larasati[20]]"
    sriyani "[text_prolog_sriyani[18]]"
    larasati "[text_prolog_larasati[21]]"
    larasati "[text_prolog_larasati[22]]"
    sriyani "[text_prolog_sriyani[19]]"
    sriyani "[text_prolog_sriyani[20]]"
    show lolilaras_senang at left
    larasati "[text_prolog_larasati[23]]"
    larasati "[text_prolog_larasati[24]]"
    larasati "[text_prolog_larasati[25]]"
    hide sriyani_ketawav2 
    show sriyani_ketawa at right
    narrator "[narator_text[17]]"
    sriyani "[text_prolog_sriyani[21]]"
    larasati "[text_prolog_larasati[26]]"
    sriyani "[text_prolog_sriyani[22]]"
    larasati "[text_prolog_larasati[27]]"
    play sound "SFX/Kain2.mp3" fadeout 1.3
    with dissolve
    narrator "[narator_text[18]]"
    play sound "SFX/Kain.mp3" fadeout 1.3
    with dissolve
    sriyani "[text_prolog_sriyani[23]]"
    sriyani "[text_prolog_sriyani[24]]"
    narrator "[narator_text[19]]"
    hide lolilaras_senang
    hide sriyani_ketawa
    with dissolve


    jump larasati_sudah_sma


label larasati_sudah_sma:
    scene bg kamar_larasati
    narrator "[text_narrator_sma[0]]"
    narrator "[text_narrator_sma[1]]"
    narrator "[text_narrator_sma[2]]"
    narrator "[text_narrator_sma[3]]"
    scene bg ruang_menjahit
    show larasatisma_senang at left
    with fade
    larasati "[text_larasati_sma[0]]"
    show sriyanitua_senyum at right
    with fade
    sriyani "[text_sriyani_sma[0]]"
    larasati "[text_larasati_sma[1]]"
    sriyani "[text_sriyani_sma[1]]"
    sriyani "[text_sriyani_sma[2]]"
    larasati "[text_larasati_sma[2]]"
    sriyani "[text_sriyani_sma[3]]"
    sriyani "[text_sriyani_sma[4]]"
    hide larasatisma_senang
    show larasatisma_bingungheran at left
    larasati "[text_larasati_sma[3]]"
    narrator "[text_narrator_sma[4]]"
    hide sriyanitua_senyum
    show sriyanitua_pasrah at right
    sriyani "[text_sriyani_sma[5]]"
    hide sriyanitua_pasrah
    show sriyanitua_bingung at right
    sriyani "[text_sriyani_sma[6]]"
    sriyani "[text_sriyani_sma[7]]"
    hide larasatisma_bingungheran
    show larasatisma_pasrah at left
    larasati "[text_larasati_sma[4]]"
    larasati "[text_larasati_sma[5]]"
    hide larasatisma_pasrah
    hide sriyanitua_bingung
    with dissolve
    show larasatisma_kalem
    with fade
    narrator "[text_narrator_sma[5]]"
    narrator "[text_narrator_sma[6]]"
    with dissolve
    scene bg kamar_larasati
    show larasatisma_senang 
    with fade
    larasati "[text_larasati_sma[6]]"
    larasati "[text_larasati_sma[7]]"
    hide larasatisma_senang
    show larasatisma_bingungcemas
    larasati "[text_larasati_sma[8]]"
    hide larasatisma_bingungcemas
    show larasatisma_murungsedih
    larasati "[text_larasati_sma[9]]"
    larasati "[text_larasati_sma[10]]"
    hide larasatisma_murungsedih
    show larasatisma_pasrah
    narrator "[text_narrator_sma[7]]"
    narrator "[text_narrator_sma[8]]"
    narrator "[text_narrator_sma[9]]"
    narrator "[text_narrator_sma[10]]"
    hide larasatisma_pasrah
    show larasatisma_kagetemoji
    larasati "[text_larasati_sma[11]]"
    larasati "[text_larasati_sma[12]]"
    hide larasatisma_kagetemoji
    show larasatisma_kagethoror
    larasati "[text_larasati_sma[13]]"
    hide larasatisma_kagethoror
    show larasatisma_kagetemoji2
    narrator "[text_narrator_sma[11]]"
    narrator "[text_narrator_sma[12]]"
    hide larasatisma_kagetemoji2
    show larasatisma_bingungcemas
    larasati "[text_larasati_sma[14]]"
    larasati "[text_larasati_sma[15]]"
    larasati "[text_larasati_sma[16]]"
    larasati "[text_larasati_sma[17]]"
    larasati "[text_larasati_sma[18]]"
    hide larasatisma_bingungcemas
    show larasatisma_pasrah
    larasati "[text_larasati_sma[19]]"
    narrator "[text_narrator_sma[13]]"
    hide larasatisma_pasrah
    show larasatisma_bingungcemas
    larasati "[text_larasati_sma[20]]"
    hide larasatisma_bingungcemas
    narrator "[text_narrator_sma[14]]"
    narrator "Larasati memejamkan matanya"
    narrator "Dan tiba-tiba muncul notifikasi dari handphone"
    jump dm_dari_rani

label dm_dari_rani:
    scene kamar_larasati
    show phone at center
    with dissolve
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    larasati "[text_larasati_dm[0]]"
    rani "[text_rani[0]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[1]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[1]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[2]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[2]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[3]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[3]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[4]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[4]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[5]]"
    play sound "audio/SFX/typing2.mp3" fadeout 0.6
    larasati "[text_larasati_dm[5]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[6]]"
    play sound "audio/SFX/typing3.mp3" fadeout 0.7
    larasati "[text_larasati_dm[6]]"

    hide phone
    stop music fadeout 2.0
    with dissolve
    jump kafe_sore


label kafe_sore:
    scene cafe
    play music "BGM/Cafe_BGM3.mp3" volume 0.7
    with dissolve
    narrator "Pukul 15:35"
    narrator "Rani sudah sampai di kafe tapi Larasati belum datang"
    show rani_base
    rani "...."
    rani "Ternyata belum sampai Dia"
    hide rani_base
    narrator "Pukul 15:55"
    show rani_base
    rani "Lama banget sih itu anak"
    play sound "audio/SFX/SFX_Bell.mp3" fadeout 0.5
    narrator "Larasati akhirnya datang"
    hide rani_base
    show rani_seyumciptadent
    narrator "Rani melambaikan tangan untuk memberitahu Larasati"
    hide rani_seyumciptadent

    show rani_senyum:
        xalign 0.85 yalign 1.3

    rani "Datang juga kamu" 
    show larasati_senyum:
        xalign 0.2 yalign 1.3
    larasati "Ah iya"
    rani "Aku sampai pesan kopi duluan"
    rani "Kenapa lama sekali sih ?"
    hide larasati_senyum
    show larasati_bingungheran:
        xalign 0.2 yalign 1.3
    larasati "Dih.... macet tahu"
    hide rani_senyum

    show rani_ngodain :
        xalign 0.85 yalign 1.3

    rani "Dih... alasan"

    hide larasati_bingungheran
    show larasati_pasrah:
        xalign 0.2 yalign 1.3
    larasati "Au ah... aku mau pesan kopi dulu"
    narrator "Setelah Larasati memesan kopi, mereka melanjutkan pembicaraan"
    with fade
    hide larasati_pasrah
    show larasati_senyum:
        xalign 0.2 yalign 1.3
    larasati "Tempatnya lumayan juga "
    hide rani_ngodain
    show rani_base:
        xalign 0.85 yalign 1.3
    rani "Iyalah"
    larasati "Tapi lumayan mahal-mahal menunya"
    rani "Yaa standard harga kafe sih"
    rani "Ngomong-ngomong kemarin kamu lagi bikin desain motif batik ya ?"
    larasati "Iya"
    rani "Udah selesai ?"
    larasati "Sudah, tapi sepertinya aku harus buat ulang "
    rani "Loh...."
    larasati "Desain yang aku buat ternyata nggak sesuai keinginan pelanggan"
    rani "Ooh.... jadi kamu buat ulang lagi tuh ?"
    larasati "Iyalah"
    rani "Sudah selesai ?"
    larasati "Belum, Aku bingung nggak ada ide lagi"
    larasati "Eh udah sih tapi aku nggak yakin hasilnya bagus di mata orang lain"
    rani "Emang kamu bikin yang kaya gimana"
    larasati "Aku bikin yang modelnya agak modern gitu, tapi sepertinya aneh kalau di aplikasikan ke kemeja "
    rani "Batik tapi modern..? Emang ada ya..?"
    larasati "Ada aku pernah lihat waktu liburan ke Solo"
    rani "Hmm aku nggak tahu banyak sih tentang batik"
    rani "Tapi kalau desain harusnya selera masing-masing orang"
    larasati "...."
    larasati "Iya sih aku harus membuat desain yang menarik menurut pandangan orang lain"
    rani "Kamu tidak menggunakan desain model dari Ayahmu ?"
    rani "Kamu pernah bilang dulu Ayahmu suka sekali membuat model batik kan?"
    larasati "Sudah, aku sudah melihat semua buku gambarnya"
    larasati "Tapi aku cukup bosan melihat model yang begitu-begitu saja"
    larasati "Aku mau buat desain model batikku sendiri"
    rani "Memang susah sih kalau membuat desain sendiri"
    rani "Coba saja kamu cari buku-buku Ayahmu lagi"
    rani "Siapa tahu ada desain model batik yang dapat membantu kamu"
    larasati "Yaa.... nanti saja lah"
    rani "Aku sedang tidak ingin mencari ide untuk desain"
    rani "Hmm.. ya tidak apa-apa, untuk mencari ide memang tidak harus terburu-buru"
    rani "Eh kamu tahu nggak ? kakak kelas kita yang ikut ekskul bahasa Inggris...."
    hide larasati_senyum
    show larasati_bingungheran:
        xalign 0.2 yalign 1.3
    larasati "Yang mana ? ada banyak tuh"
    hide rani_base
    show rani_ngodain:
        xalign 0.85 yalign 1.3
    rani "Itu loh yang namanya kak Satria"
    hide larasati_bingungheran
    show larasati_bingungcemas:
        xalign 0.2 yalign 1.3
    larasati "Ohhh dia..."
    hide larasati_bingungcemas
    show larasati_kagetbiasa:
        xalign 0.2 yalign 1.3
    larasati "Dia kenapa ?"
    hide rani_ngodain
    show rani_jahil:
        xalign 0.85 yalign 1.3
    rani "Sepertinya dia butuh bantuan mu untuk tugas prakarya nya"
    hide larasati_kagetbiasa
    show larasati_pasrah:
        xalign 0.2 yalign 1.3
    larasati "Emang apa hubungannya sama aku rani..."
    hide rani_jahil
    show rani_seyumciptadent:
        xalign 0.85 yalign 1.3
    rani "Aku dengar-dengar dia mau membuat kain batik"
    larasati "Hmm.... begitu ya, tapi sepertinya aku tidak bisa bantu"
    larasati "Ini desain batik ku saja belum selesai malah bantu orang lain"
    rani "Yodah iya deh larasati kan aku cuma mau bilang aja"
    narrator "Obrolan mereka berlanjut sampai pukul 19:45"
    hide larasati_pasrah 
    hide rani_seyumciptadent
    with fade
    narrator "Dan mereka pulang ke rumah masing-masing"
    stop music fadeout 2.0
    with dissolve


    jump pulang_rumah

label pulang_rumah:
    scene bg ruang_menjahit
    play music "BGM/All_Idle_Game_BGM.mp3" volume 0.7
    show larasati_kalem
    with fade
    larasati "[text_larasati_pulangkafe[0]]"
    narrator "[text_narrator_pulang[0]]"
    narrator "[text_narrator_pulang[1]]"
    narrator "[text_narrator_pulang[2]]"
    hide larasati_kalem 
    show sriyanitua_tulus at right
    show larasati_senyum:
        xalign 0.2 yalign 1.3
    with fade
    sriyani "[text_respon_ibularas[0]]"
    sriyani "[text_respon_ibularas[1]]"
    hide larasati_senyum 
    show larasati_senang:
        xalign 0.2 yalign 1.3
    larasati "[text_larasati_pulangkafe[1]]"
    hide sriyanitua_tulus 
    show sriyanitua_senang at right
    sriyani "[text_respon_ibularas[2]]"
    larasati "[text_larasati_pulangkafe[2]]"
    hide sriyanitua_senang 
    show sriyanitua_bahagia at right
    sriyani "[text_respon_ibularas[3]]"
    hide larasati_senang
    show larasati_bingungheran:
        xalign 0.2 yalign 1.3
    larasati "[text_larasati_pulangkafe[3]]"
    hide larasati_bingungheran
    show larasati_pasrah:
        xalign 0.2 yalign 1.3
    larasati "[text_larasati_pulangkafe[4]]"
    narrator "[text_narrator_pulang[3]]"
    hide sriyanitua_tulus
    hide larasati_senyum 
    with dissolve
    scene bg kamar_larasatimalam
    show larasati_pasrah
    larasati "[text_larasati_pulangkafe[5]]"
    larasati "[text_larasati_pulangkafe[6]]"
    larasati "[text_larasati_pulangkafe[7]]"
    narrator "[text_narrator_pulang[4]]"
    narrator "[text_narrator_pulang[5]]"
    narrator "[text_narrator_pulang[6]]"
    hide larasati_pasrah
    show larasati_bingungcemas
    larasati "[text_larasati_pulangkafe[8]]"
    larasati "[text_larasati_pulangkafe[9]]"
    hide larasati_bingungcemas
    show larasati_pasrah
    larasati "[text_larasati_pulangkafe[10]]"
    narrator "[text_narrator_pulang[7]]"
    narrator "[text_narrator_pulang[8]]"
    larasati "[text_larasati_pulangkafe[11]]"
    hide larasati_pasrah
    narrator "[text_narrator_pulang[9]]"
    narrator "[text_narrator_pulang[10]]"
    narrator "[text_narrator_pulang[11]]"
    show larasati_bingungcemas
    narrator "[text_narrator_pulang[12]]"
    larasati "[text_larasati_pulangkafe[12]]"
    larasati "[text_larasati_pulangkafe[13]]"
    larasati "[text_larasati_pulangkafe[14]]"
    larasati "[text_larasati_pulangkafe[15]]"
    narrator "[text_narrator_pulang[13]]"
    hide larasati_bingungcemas
    show larasati_kagetemoji2
    narrator "[text_narrator_pulang[14]]"
    hide larasati_bingungcemas
    show larasati_kagetemoji1
    larasati "[text_larasati_pulangkafe[16]]"
    narrator "[text_narrator_pulang[15]]"
    hide larasati_kagetemoji1
    show larasati_kagetemoji2
    play sound "audio/SFX/BukuJatuh2.mp3" fadeout 0.5
    larasati "[text_larasati_pulangkafe[17]]"
    show larasati_kagetemoji2
    with hpunch
    larasati "[text_larasati_pulangkafe[18]]"
    with hpunch
    play sound "audio/SFX/BukuJatuh3.mp3" fadeout 0.5
    narrator "[text_narrator_pulang[16]]"
    with hpunch
    narrator "[text_narrator_pulang[17]]"
    narrator "[text_narrator_pulang[18]]"
    show dimensi
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide dimensi
    hide larasati_kagetemoji2
    narrator "[text_narrator_pulang[19]]"
    play sound "audio/SFX/BukuJatuh4.mp3" fadeout 0.5
    narrator "[text_narrator_pulang[20]]"
    narrator "[text_narrator_pulang[21]]"
    stop music fadeout 0.5
    jump chapter_2_hutan

    # ----- Hutan Parang --------

label chapter_2_hutan:
    scene hutan_parang
    play music "audio/BGM/parang.mp3" volume 0.7
    narrator "Suatu tempat yang tidak diketahui"
    show screen black_screen
    with dissolve
    pause 0.5
    hide screen black_screen
    with dissolve

    show larasati_bingungcemas at center
    with moveinbottom
    with dissolve
    larasati "Ukh.."
    narrator "Larasati terbangun dan membuka mata"
    narrator "Mencoba mengingat apa yang terjadi"
    larasati "Apa yang terjadi ?"
    larasati "HAH!?!?"
    larasati "Ini dimana ?"
    larasati "Perasaan aku baru saja ada di kamar"
    larasati "Kenapa aku bisa ada disini ?"
    narrator "Larasati mencoba untuk tidak panik dan tetap tenang"
    narrator "Serta memperhatikan sekelilingnya"
    narrator "Banyak sekali batang-batang pohon dan rumput yang tinggi"
    hide larasati_bingungcemas
    show larasati_bingungheran at center
    larasati "..."
    larasati "......"
    larasati "Tempat ini seperti hutan"
    larasati "Tapi kenapa pohon-pohon disini memiliki pola yang aneh"
    larasati "Semuanya terlihat seperti..."
    larasati "Batik ?"
    narrator "Larasati melihat sekelilingnya dan memahami apa yang benar-benar terjadi"
    larasati "Tempat ini benar-benar seperti hutan"
    hide larasati_bingungheran
    show larasati_bingungcemas at center
    larasati "Agak sedikit menyeramkan tapi.."
    larasati "Eh tunggu dulu"
    larasati "Disini ada hewan buas tidak ya ?"
    larasati "Apa aku disini sendiri ?"
    larasati "Kalau benar bagaimana caranya aku keluar dari sini"
    larasati "Dan juga ini tempat apa dan dimana sih"
    hide larasati_bingungcemas
    narrator "Sudah 4 menit Larasati diam ditempat dan memperhatikan sekelilingnya"
    narrator "Melihat pohon-pohon tinggi dengan pola yang dianggap seperti batik"
    narrator "Begitu pun juga rumput dan tanaman lainnya"
    narrator "Suasana yang tenang dengan angin lembut yang berhembus"
    narrator "Tapi tidak menutup kemungkinan bahwa hutan ini memiliki aura yang menyeramkan bagi orang yang pertama kali datang"
    show larasati_bingungheran at center
    with dissolve
    larasati "Aku harus kemana dan bagaimana ini"
    larasati "Hutan ini terlalu luas"
    narrator "Larasati tidak berani untuk mengambil keputusan untuk mencari jalan keluar"
    narrator "Karena tempat ini sangat asing baginya"
    narrator "Dan dia tidak tahu ada apa saja di tempat ini"
    larasati "......"
    narrator "Tapi ia terus mencoba untuk menenangkan pikirannya dan membuat dirinya berani untuk mencari jalan keluar"
    larasati "Mungkin ke arah sana"
    hide larasati_bingungheran
    show larasati_pasrah at left
    pause 1.0
    hide larasati_pasrah
    show larasati_pasrah at center
    pause 1.0
    hide larasati_pasrah
    show larasati_pasrah at right
    pause 1.0
    hide larasati_pasrah with dissolve
    narrator "Larasati meninggalkan tempatnya"
    narrator "Dia berjalan ke arah yang ia tidak tahu menuju kemana"
    narrator "Baru beberapa langkah berjalan, Larasati melihat ada bunga besar berwarna emas"
    narrator "Di bagian atas bunga tersebut ada sesuatu bergerak"
    show makaras_base:
        xpos 0.8
        xzoom -1
    show larasati_bingungcemas at left
    with moveinleft
    larasati "Eh itu apa ?"
    larasati "Seperti ekor"
    larasati "Hah ada makhluk hidup di disini ?"
    narrator "Larasati memperhatikan dari jarak yang cukup jauh"
    narrator "Dia ingin tahu makhluk hidup tersebut dapat membahayakan dirinya atau sebaliknya"
    hide larasati_bingungcemas
    show larasati_bingungcemas at left:
        xzoom -1
    narrator "Larasati menoleh ke belakang dan sekelilingnya untuk melihat situasi"
    hide makaras_base
    hide larasati_bingungcemas
    show larasati_bingungcemas at left
    narrator "Ketika dia kembali menoleh ke depan, tiba-tiba makhluk hidup tadi hilang"
    larasati "Haah, itu dia pergi kemana"
    show makaras_base at right
    with moveinright
    with dissolve
    makhluk "Kamu mencari siapa ?"
    hide larasati_bingungcemas
    show larasati_kagetemoji1 at left
    larasati "Huahhh"
    narrator "Tiba-tiba makhluk hidup tadi berada di sampingnya"
    hide larasati_kagetemoji1
    narrator "Dan Larasati terjatuh karena kaget"
    show larasati_bingungcemas at left
    with moveinbottom
    larasati "Siapa kamu"
    narrator "Makhluk hidup tersebut terlihat seperti burung"
    larasati "Kenapa kamu bisa bicara ?"
    makhluk "Kamu bicara apa ?"
    narrator "Karena Larasati sudah mencoba untuk tenang sebelumnya"
    narrator "Dia tidak terlalu panik di situasi ini"
    makhluk "Kamu siapa ?"
    makhluk "Dilihat dari pakaianmu sepertinya kamu bukan berasal dari sini"
    makhluk "Kamu berasal dari dunia luar ?"
    larasati "..."
    larasati "Kamu kok kamu bisa bicara ?"
    makhluk "Aku memang bisa bicara"
    hide larasati_bingungcemas
    show larasati_senyum at left
    narrator "Pikiran Larasati di situasi ini sudah tenang dan tidak merasa panik"
    narrator "Larasati pun mencoba untuk berbicara dengan makhluk hidup yang ada di depannya"
    makhluk "Hei kenapa kamu tidak menjawab ?"
    larasati "Ah aku tadi"
    larasati "Aku bukan berasal dari sini"
    makhluk "Berarti kamu dari dunia luar ya ?"
    larasati "Dunia luar ?, yaa sepertinya begitu"
    makhluk "Oh kamu dari dunia manusia"
    hide larasati_senyum
    show larasati_bingungheran at left
    larasati "Kamu tahu dunia manusia ?"
    makhluk "Seseorang pernah memberitahuku tentang dunia manusia"
    makhluk "Siapa namamu ?"
    larasati "Eh aku Larasati"
    hide makaras_base
    show makaras_senang at right
    makara "Namaku Makara"
    makara "Bagaimana kamu bisa berada di sini ?"
    larasati "Itu aku tidak tahu"
    larasati "Sebelumnya aku membuka buku dan tiba-tiba saja aku masuk ke buku itu"
    narrator "Makara menyadari sesuatu"
    narrator "Buku yang dimaksud Larasati adalah buku {b}Rahara Batik"
    narrator "Dan Larasati adalah orang yang diberi izin untuk masuk ke dunia ini oleh pemilik buku tersebut"
    makara "Itu terdengar aneh"
    makara "Tapi masuk akal karena kamu berada disini"
    larasati "Sebenarnya Makara ini tempat apa ?"
    larasati "Semua yang aku lihat disini memiliki pola seperti batik"
    makara "Hmm ya benar yang kamu lihat di sekeliling kamu memiliki pola batik"
    makara "Dan hutan ini adalah hutan Parang"
    larasati "Hutan Parang ?"
    makara "Ya benar"
    makara "Hutan ini sangat luas dan banyak sekali tumbuh-tumbuhan yang besar"
    makara "Serta ada beberapa makhluk hidup yang tinggal di hutan ini"
    makara "Tapi tidak perlu takut terhadap makhluk hidup yang tinggal disini"
    narrator "Makara menjelaskan isi dari hutan ini dengan nada yang ramah"
    makara "Oh ya, apa yang kamu rasakan saat berada di hutan ini ?"
    larasati "Aku merasakan banyak hal"
    larasati "Yang pasti aku merasa takut dan bingung"
    makara "Mungkin bagimu hutan ini berbahaya"
    makara "Sebenarnya hutan ini tidak terlalu berbahaya seperti yang kamu bayangkan"
    makara "Hutan parang ini memiliki aura yang kuat sehingga orang seperti kamu merasakan sesuatu dari esensi hutan ini
    "
    larasati "Begitu rupanya"
    makara "Sekarang apa yang kamu mau lakukan ?"
    narrator "Larasati sampai lupa bahwa ia ingin mencari jalan keluar dari dunia ini"
    hide larasati_bingungheran
    show larasati_murungsedih at left
    larasati "Aku, aku tidak tahu"
    larasati "Aku ingin mencari jalan keluar dari dunia ini"
    makara "Hmm aku bisa membantumu"
    larasati "Benarkah"
    makara "Yaa"
    hide larasati_murungsedih
    show larasati_senyum at left
    narrator "Larasati merasa senang dan mempercayai Makara untuk mencari jalan keluar dari dunia ini"
    makara "Sebenarnya untuk keluar dari sini tidak begitu mudah"
    makara "Kamu harus siap untuk rintangan-rintangan yang akan kamu hadapi"
    hide larasati_senyum
    show larasati_bingungheran at left
    larasati "Rintangan ?"
    narrator "Larasati melihat sekelilingnya yang penuh dengan pohon-pohon tinggi dan tumbuh-tumbuhan yang asing baginya"
    narrator "Tapi dia harus yakin jika ingin keluar dari dunia ini"
    narrator "Larasati tetap memberanikan dirinya dan menghilangkan rasa takutnya"
    hide larasati_bingungheran
    show larasati_tertarik at left
    larasati "Baiklah aku akan menghadapi rintangan yang aku hadapi"
    narrator "Makara tersenyum karena keputusan Larasati"
    makara "Pertama kita harus keluar dari hutan ini terlebih dahulu"
    makara "Ikuti aku lewat sini"
    hide makaras_senang
    show makaras_senang with dissolve:
        xpos 0.9
    pause 1.0
    hide makaras_senang
    hide larasati_tertarik with dissolve
    narrator "Mereka pun berjalan untuk keluar dari hutan parang"
    narrator "Selama diperjalanan Makara memperhatikan wajah Larasati"
    narrator "Makara berpikir ada sesuatu yang mengganggu pikirannya"
    show makaras_base at right
    show larasati_pasrah at left
    makara "Kamu, apa kamu baik-baik saja ?"
    larasati "Ah iya aku baik-baik saja"
    makara "Sepertinya ada yang mengganggu di pikiranmu"
    larasati "Itu.."
    larasati "Aku punya masalah dengan ibuku"
    makara "Ibumu ?"
    larasati "Aku disuruh membuat kemeja batik dengan motif yang sudah diberikan"
    larasati "Aku menginginkan motif lain"
    larasati "Tapi aku tidak memiliki ide untuk motif yang akan aku gunakan"
    larasati "Motif yang aku buat selalu gagal dan membuatku tidak bersemangat"
    larasati "Itu salah satu yang membuatku takut untuk desain baru dan menunjukkannya ke orang lain"
    narrator "Larasati menjelaskan permasalahan lebih lanjut antara dirinya dengan ibunya"
    narrator "Makara memahaminya dengan perlahan"
    window hide
    pause 0.5
    window show
    makara "Begitu rupanya"
    makara "Aku tidak memiliki solusi yang pasti untuk permasalahan itu"
    makara "Tapi terimakasih karena sudah berbagi cerita"
    larasati "Ah iya tidak masalah"
    makara "Ohiya aku hampir lupa"
    makara "Kamu membutuhkan ini nanti"
    narrator "Makara mengepakkan sayapnya"
    narrator "Mengeluarkan kertas dan pena lalu diberikan ke Larasati"
    larasati "Kertas dan pena ?"
    larasati "Ini untuk apa ?"
    makara "Kamu simpan dulu saja, nanti pasti dibutuhkan"
    larasati "Baiklah"
    narrator "Mereka pun tetap melanjutkan perjalanan"
    hide larasati_pasrah
    with dissolve
    hide makaras_base
    with dissolve
    narrator "Sampai didepan mereka ada sungai yang cukup lebar untuk dilewati"
    show larasati_bingungheran at left
    larasati "Sungai"
    larasati "Bagaimana cara melewatinya?"
    show makaras_base at right
    makara "Hmm..."
    narrator "Makara melihat ada batu-batu yang dapat dipijak untuk melewati sungai"
    makara "Lewat sini"
    narrator "Makara melompati batu-batu tersebut"
    makara "Ikuti aku"
    narrator "Larasati berpikir sejenak, batu mana yang harus dipijak untuk sampai ke seberang sungai"
    narrator "Lalu Larasati mulai melompati batu secara perlahan"
    narrator "Satu persatu batu dilompati dan dilangkahi"
    hide larasati_bingungheran 
    show larasati_kagetemoji2 at left
    larasati "Huaaa..."
    makara "Hati-hati"
    makara "tidak perlu terburu-buru, tidak perlu mempercepat langkah"
    makara "yang penting kamu konsisten dan tetap berusaha untuk sampai ke seberang sana"
    narrator "Larasati menyadari satu hal"
    narrator "Ini adalah salah satu rintangan yang dimaksud Makara sebelumnya"
    hide larasati_kagetemoji2
    show larasati_senyum at left
    larasati "Baiklah"
    narrator "Larasati terus mengikuti kecepatan langkah yang ia buat sebelumnya"
    narrator "Dan tetap semangat berjuang walaupun hanya batu yang ia pijak"
    narrator "Ketekunan dan semangat juang adalah hal yang dipahami Larasati saat ini"
    narrator "Setelah beberapa menit melewati sungai"
    narrator "Mereka sampai di seberang sungai"
    larasati "Akhirnya sampai juga"
    larasati "Aku tidak bisa membayangkan apa yang terjadi kalau aku kecebur di sungai"
    makara "Humm.. bagaimana ?"
    makara "Kamu mau melanjutkan atau istirahat dulu ?"
    makara "Sebentar lagi kita keluar dari hutan ini"
    makara "Hanya melewati jalan ini dan kita keluar dari hutan Parang"
    narrator "Larasati melihat jalan yang ditunjukkan Makara"
    larasati "Kita lanjutkan saja"
    larasati "Tapi bagaimana denganmu ?"
    larasati "Apa kamu mau istirahat dulu?"
    makara "Aku tidak masalah"
    makara "Kalau begitu kita lanjutkan perjalanannya"
    hide larasati_senyum
    hide makaras_base
    narrator "Mereka pun melanjutkan perjalanan"
    narrator "Hutan Parang yang mereka lewati sekarang berbeda dari sebelumnya"
    narrator "Hutan ini banyak sekali batu-batu besar yang menghalanginya dan semak-semak yang lebat"
    narrator "Tapi Larasati tidak masalah dengan hal itu"
    narrator "Ia sudah memiliki keberanian sejak sebelum melewati sungai"
    narrator "Saat ini keberanian Larasati semakin meningkat"
    show makaras_senang at center
    makara "Sepertinya kamu sudah mulai terbiasa dengan hutan ini"
    hide makaras_senang
    jump soal_quiz_1
    # ----- Quiz 1 -----
    

label soal_quiz_1:
    scene hutan_parang
    show makaras_base at center
    makara "Selama kita berada di hutan Parang"
    makara "Apa yang sudah kamu dapat ?"
    makara "Seperti esensinya"
    hide makaras_base
    call screen quiz_1

label jawaban_soal_1_1:
    show makaras_base at center
    makara "Hmm ?"
    makara "Bukan itu yang sebenarnya dari esensi Hutan Parang ini"
    makara "Esensi dari hutan Parang ini adalah keberanian, ketekunan dan semangat untuk menghadapi tantangan hidup"
    jump chapter_2_hutan_2

label jawaban_soal_1_2:
    hide makaras_base
    show makaras_senang at center
    makara "Benar"
    makara "Hutan Parang ini memiliki Esensi dari hutan Parang ini adalah keberanian, ketekunan dan semangat untuk menghadapi tantangan hidup"
    jump chapter_2_hutan_2

label chapter_2_hutan_2:
    scene hutan_parang
    hide makaras_senang
    hide makaras_base
    narrator "Larasati mengerti maksud perkataan Makara"
    narrator "Ketiga hal yang dibicarakan..."
    narrator "Keberanian, ketekunan, dan semangat berjuang"
    narrator "Sudah ada di dalam diri Larasati"
    show larasati_senang at left
    with dissolve
    larasati "Ngomong-ngomong jalannya menanjak"
    larasati "Apa kita sebentar lagi keluar dari hutan ini ?"
    show makaras_base at right
    makara "Ya benar kita sebentar lagi keluar dari hutan ini"
    narrator "Setelah beberapa saat"
    makara "Akhirnya kita keluar dari hutan Parang"
    stop music fadeout 1.0
    hide makaras_base 
    hide larasati_senang
    with fade
    
    scene bukit
    hide makaras_base
    show makaras_senang at right
    play music "audio/BGM/megamendung.mp3" volume 0.7
    makara "Lelah juga ya"
    narrator "Makara langsung rebahan di atas rumput"
    show larasati_senang at left
    larasati "Iya cukup melelahkan"
    larasati "Tapi disini anginnya cukup sejuk dari sebelumnya"
    makara "Karena kita berada di dataran tinggi"
    makara "Kamu tahu ?"
    makara "Hutan Parang ini sebenarnya motif batik dari dunia manusia tahu"
    larasati "Tapi Aku belum pernah mendengarnya"
    makara "Motif Parang berasal dari Solo"
    makara "Lebih tepatnya dari Keraton Mataram Kartasura"
    larasati "Solo ?"
    hide larasati_senang
    show larasati_tertarik at left
    larasati "Kamu benar-benar tahu dunia ku ya ?"
    makara "Aku sudah bilang sebelumnya"
    makara "Aku tahu karena seseorang pernah memberitahuku"
    larasati "Eh seseorang ?"
    makara "Aku ingin istirahat dulu"
    hide larasati_tertarik
    hide makaras_senang
    show larasati_senyum at center
    narrator "Melihat Makara yang sedang rebahan, Larasati langsung duduk dan memandangi hutan Parang"
    narrator "Larasati menghela nafas panjang karena melihat hutan Parang dan mengingat apa yang sudah dilewati serta pelajaran yang didapat"
    narrator "Ia melihat hutan tersebut, banyak sekali pohon-pohon yang menyerupai suatu pola dan begitu juga sungainya"
    narrator "Lalu Ia teringat kertas dan pena yang diberikan Makara"
    narrator "Larasati pun menggambar hutan Parang di kertas dengan pena"
    larasati "Aku buat seperti apa ya ?"
    larasati "Oh aku tahu"
    larasati "Sepertinya kalau seperti ini jadi menarik"

    # ---- mini game drag and drop -----

    narrator "Sesaat setelah selesai menggambar, Larasati rebahan di atas rumput sembari memandangi langit"
    narrator "Suasana saat ini membuatnya begitu sangat tenang, walaupun tetap harus mencari jalan keluar dari dunia ini"
    hide larasati_senyum
    jump chapter_3_gunung
    # ----- end chapter 2 -------

label chapter_3_gunung:
    scene bukit 
    narrator "Larasati memandangi langit yang biru"
    narrator "Tiba-tiba Dia melihat bentuk awan yang berbeda dari yang sebelumnya"
    narrator "Bentuk awan yang berbeda ketika Dia dan Makara berada di hutan Parang"
    show larasati_bingungheran at left
    larasati "Loh itu awannya berbeda"
    narrator "Larasati pun berdiri untuk melihat sekelilingnya"
    narrator "Menoleh kiri lalu kanan dan sebaliknya"
    narrator "Melihat perbedaan bentuk awan"
    hide larasatisma_bingungheran
    show larasati_kalem at left
    larasati "Awannya berbeda tapi masih seperti pola batik"
    hide larasati_kalem
    show larasati_bingungheran at left
    larasati "Hmm..."
    show makaras_kaget at right
    makara "Hoamm"
    makara "Kamu sedang apa ?"
    larasati "Itu..."
    narrator "Makara menoleh ke atas"
    makara "Awan ?"
    larasati "Iya awannya berbeda dengan yang di hutan Parang"
    makara "Itu karena kita sudah berada di tempat yang berbeda"
    makara "Tempat ini bukan hutan Parang lagi"
    makara "Melainkan gunung Megamendung"
    hide larasati_bingungheran
    show larasati_kagetemoji1 at left
    larasati "Ah iya juga kita berada di sekitar area pegunungan"
    larasati "Tapi sepertinya aku pernah mendengar kata Megamendung"
    hide makaras_kaget
    show makaras_base at right
    makara "Kamu tahu batik motif megamendung ?"
    hide larasati_kagetemoji1
    show larasati_senang at left
    larasati "Aku tidak tahu tapi aku pernah mendengarnya sebelumnya"
    makara "Batik motif Megamendung ini berasal dari Cirebon di Jawa Barat"
    larasati "Oh ternyata dari Cirebon"
    makara "Iya"
    larasati "Makara apakah kamu pernah ke dunia luar ?"
    makara "Keluar dari dunia batik maksudmu ?"
    larasati "Iya"
    makara "Aku tidak pernah memikirkan untuk keluar dari sini"
    makara "Lagipula aku memiliki tugas disini"
    hide larasati_senang
    show larasati_bingungheran at left
    larasati "Tugas ?"
    makara "Iya"
    makara "Kamu mau melanjutkan perjalanan ?"
    larasati "Hmm.."
    larasati "Ayo"
    larasati "Sekarang kita lewat mana ?"
    makara "Kita akan melewati gunung ini"
    larasati "Hah gunung ini ?"
    makara "Benar"
    makara "Tapi tidak perlu khawatir"
    makara "Aku tahu arahnya"
    makara "Cukup melewati jalan ini saja"
    makara "Ayo ikuti aku"
    narrator "Mereka pun akhirnya melanjutkan perjalanan"
    narrator "ketika mereka berjalan, Larasati menoleh ke belakang untuk melihat hutan Parang sekali lagi"
    narrator "Dan melihat kertas yang berisi desain gambar yang baru saja dibuatnya"
    narrator "Makara melihat ke arah Larasati"
    makara "Ada apa ?"
    larasati "Tidak apa-apa"
    makara "Kamu menggambar sesuatu ?"
    hide larasati_bingungheran
    show larasati_kalem at left
    larasati "Benar, aku menggambar hutan Parang di kertas ini"
    makara "Coba aku lihat"
    narrator "Larasati mencoba menunjukkan hasil desainnya"
    narrator "Berharap Makara memiliki respon yang baik"
    makara "Waah.. bagus sekali"
    makara "Kamu membuat seperti ini berapa kali mencoba"
    hide larasati_kalem 
    show larasati_senang at left
    larasati "Eh itu terimakasih aku membuatnya hanya sekali mencoba"
    makara "Hmm.."
    makara "Ini bagus"
    larasati "..."
    larasati "Terimakasih"
    narrator "Makara mengembalikan kertasnya ke Larasati"
    larasati "Ayo kita jalan"
    makara "Yaa"
    narrator "Perjalanan ini memiliki jalur yang menanjak dan menurun"
    narrator "Melewati jalan yang berkelok kiri dan kanan"
    larasati "Jalur ini benar-benar seperti pegunungan"
    makara "Kita memang berada di area pegunungan"
    larasati "Apakah gunung ini memiliki nama ?"
    makara "Hmm"
    makara "Gunung ini memiliki nama"
    makara "Namanya gunung Megamendung"
    larasati "Megamendung"
    narrator "Larasati ingin bertanya apakah gunung ini memiliki esensi seperti hutan Parang"
    narrator "Tapi Larasati sudah tahu jawabannya"
    narrator "Setiap tempat disini pasti memiliki esensinya tersendiri"
    narrator "Hanya saja Dia tidak tahu esensi apa yang ada di gunung Megamendung ini"
    hide larasati_senang
    show larasati_pasrah at left
    larasati "Jalannya melelahkan juga"
    makara "Hmm… ya begitulah"
    narrator "Mereka tetap melewati jalan yang melelahkan"
    narrator "Terkadang harus melompat atau melewati jalan bebatuan yang banyak"
    makara "Kamu suka mendesain sesuatu ?"
    hide larasati_pasrah
    show larasati_kalem at left
    larasati "Tidak juga"
    larasati "Aku hanya mendesain motif batik saja"
    makara "Hmm begitu"
    makara "Kamu tahu tentang batik sejak kapan ?"
    larasati "Sebenarnya sejak aku masih anak-anak"
    larasati "Aku tahu karena Ibuku penjahit"
    larasati "Seperti menjahit baju batik atau selendang"
    makara "Kamu bisa menjahit juga ?"
    larasati "Bisa"
    larasati "Tapi aku lebih suka mendesain batik"
    makara "Sudah berapa banyak yang kamu buat"
    larasati "Tidak begitu banyak"
    larasati "Sekitar tujuh atau delapan motif"
    hide larasati_kalem
    show larasati_pasrah at left
    larasati "Tapi akhir-akhir ini aku malas membuat desain"
    narrator "Makara mengingat permasalahan antara Larasati dengan Ibunya"
    makara "Kenapa ?"
    makara "Bukannya tadi kamu baru membuat desain ?"
    larasati "Maksudku..."
    larasati "Desain yang aku buat tidak memiliki makna yang baik"
    larasati "Dan Ibuku selalu menyuruhku untuk membuat desain motif yang baru"
    larasati "Padahal yang aku buat sudah bagus"
    makara "Begitu"
    makara "Dalam menjalani suatu masalah terkadang emosi selalu jalan duluan"
    makara "Tapi ada saatnya ketika masalah datang, pikiran harus tenang"
    larasati "..."
    narrator "Tiba-tiba saja jalan yang dilewati menjadi curam menanjak ke atas"
    hide larasati_pasrah
    show larasati_kagetbiasa at left
    larasati "Loh jalannya curam sekali"
    makara "Apa yang kamu tunggu ?"
    makara "Ayo naik"
    makara "Ikuti aku"
    narrator "Jalan yang curam dan jalan yang penuh dengan bebatuan"
    hide larasati_kagetbiasa
    show larasati_bingungheran at left
    larasati "Apa aku bisa berjalan di jalanan seperti ini ?"
    narrator "Melihat Makara yang sudah jalan duluan membuat Larasati ingin segera mengikutinya"
    narrator "Larasati sudah memiliki esensi keberanian dari hutan Parang"
    narrator "Maka Dia tidak ragu lagi untuk melewati jalan yang ada di depannya"
    narrator "Larasati pun perlahan berjalan"
    narrator "Seiring berjalan, tiba-tiba saja jalannya mengecil"
    narrator "Hanya bisa dilewati satu orang saja"
    larasati "Hah kenapa jalannya begini"
    narrator "Larasati menoleh kebawah"
    narrator "Dia tidak tahu apa yang akan terjadi jika terjatuh ke bawah sana"
    narrator "Dan Dia juga tidak ingin tahu apa yang akan terjadi jika terjatuh ke bawah"
    narrator "Kali ini berbeda, keberanian saja tidak cukup untuk melewati ini"
    narrator "Larasati teringat perkataan Makara"
    narrator "Tenang"
    narrator "Mungkin itu adalah kuncinya ?"
    narrator "Ya benar Larasati harus tenang dalam situasi ini"
    larasati "Huuft"
    larasati "Oke tenang dulu"
    larasati "Jalannya hanya setapak dan sebelah kiri ada jurang"
    larasati "Dan aku harus.."
    narrator "Di depan Larasati harus melompat"
    narrator "Melompat lagi"
    hide larasati_bingungheran
    show larasati_senang at left
    larasati "Huaah untung saja"
    larasati "Tapi tidak terlalu sulit"
    narrator "Dan di depan masih ada banyak rintangan yang harus dihadapi"
    larasati "Apa-apaan ini"
    larasati "Masih jauhkah jalan yang seperti ini"
    narrator "Makara yang sudah jauh di depannya tidak mendengar Larasati"
    narrator "Mau tidak mau Larasati harus mengikuti jalan yang tidak Ia sukai"
    narrator "Tapi melihat ke depan"
    narrator "Jalan yang seperti ini terlihat masih jauh"
    larasati "Hmm"
    larasati "Oke tenang, pasti bisa dengan perlahan"
    narrator "Secara tidak langsung Larasati belajar untuk tenang ketika masalah ada di hadapannya"
    narrator "Dan juga menyadari satu hal yaitu.."
    narrator "Kesabaran"
    larasati "Ternyata hampir sama seperti melewati sungai di hutan Parang"
    larasati "Tapi yang ini..."
    larasati "Harus lebih sabar"
    narrator "Cukup lama untuk sampai ke atas"
    narrator "Tapi mereka berhasil berada di sana"
    makara "Ayo sebentar lagi"
    narrator "Makara melihat Larasati dengan wajah yang tenang dan tidak tergesa-gesa"
    makara "..."
    makara "Ternyata dia sudah mendapatkan esensi dari gunung ini"
    larasati "Akhirnya sampai juga"
    larasati "Apa masih jauh jalannya"
    makara "Sebentar lagi"
    makara "Di depan sana sudah mencapai dataran tinggi di gunung ini"
    makara "Jalannya juga sudah normal lagi"
    narrator "..."
    narrator "Mereka berada di puncak gunung Megamendung"
    larasati "Disini anginnya lebih sejuk dari sebelumnya"
    makara "Benar karena kita berada di atas"
    narrator "Hembusan angin yang membuat pikiran menjadi lebih tenang"
    narrator "Tidak ada emosi yang dapat mengalahkan ketenangan Larasati"
    narrator "Walaupun Dia ingat permasalahan dengan Ibunya"
    makara "Yeay sampai"
    makara "Dari sini kita bisa melihat pemandangan yang indah"
    makara "Bagaimana perasaanmu ?"
    larasati "Eh aku merasa disini cukup tenang"
    larasati "Apa karena..."
    larasati "Esensi dari tempat ini ?"
    hide larasati_senang
    # ------ quiz 2 --------
    jump soal_quiz_2

label soal_quiz_2:
    scene bukit
    show makaras_base at center
    makara "Kamu sudah melewati rintangan di tempat ini"
    makara "Jadi apa yang kamu dapat dari tempat ini ?"
    hide makaras_base
    call screen quiz_2

label jawaban_soal_2_1:
    show makaras_senang at center
    makara "Benar"
    makara "Gunung Megamendung memiliki esensi ketenangan"
    hide makaras_senang
    jump chapter_3_gunung_2

label jawaban_soal_2_2:
    show makaras_base at center
    makara "Hmm"
    makara "Belum benar"
    makara "Gunung Megamendung ini memiliki esensi ketenangan di setiap tempatnya"
    makara "Itulah kenapa kamu berhasil menghadapi rintangan yang ada di Gunung Megamendung ini"
    hide makaras_base
    jump chapter_3_gunung_2

label chapter_3_gunung_2:
    scene bukit
    "Karena Larasati sudah mengerti esensi dari gunung Megamendung"
    show larasati_senyum at center
    with dissolve
    "Larasati kembali memandangi sekitarnya"
    "Dan menoleh ke atas untuk melihat awan yang sekiranya dianggap menarik"
    "Larasati melihat awan tersebut dengan penuh ketenangan di dalam pikirannya"
    "Dan mencari batu yang bisa diduduki"
    larasati "..."
    "Larasati duduk di atas batu dan mengeluarkan kertas serta pena"
    "Lalu membuat desain batik dengan bentuk awan yang dilihatnya"
    "Sedangkan Makara membiarkan Larasati menyelesaikannya dan beristirahat"
    "Larasati mengerti mengerti"
    "Dalam menyelesaikan sebuah masalah, pikiran harus tetap tenang"
    "Jangan membiarkan emosi mengambil alih pikiran"
    "Jika emosi tetap tinggi maka kesabaran akan membuatnya menjadi seimbang"
    "Dengan hal itu maka akan menciptakan keharmonisan untuk menghadapi sebuah masalah"
    "Itulah pelajaran yang didapat oleh Larasati di gunung Megamendung ini"
    larasati "..."
    larasati "Kayaknya seperti ini bagus"
    larasati "Bagaimana kalau..."
    
    # ------- Minigame Matching Puzzle ------

    larasati "Begini"
    larasati "Hmm bagus juga"
    "Setelah itu Larasati menghampiri Makara yang sedang melihat pemandangan"
    "Larasati ingin melanjutkan perjalanannya"
    makara "Apa ?"
    makara "Kamu mau melanjutkan perjalanan ?"
    larasati "Iyaa, kamu bagaimana ?"
    makara "Aku sih tidak apa apa"
    "Makara kembali melihat pemandangan yang ada di depannya"
    "Larasati ikut melihatnya"
    larasati "Itu.."
    larasati "Itu seperti desa"
    makara "Hmm ?"
    makara "Ya itu desa"
    makara "Itu adalah tujuan kita berikutnya"
    makara "Setelah itu kamu bisa kembali ke dunia asalmu"
    larasati "Benarkah ?"
    "Makara menganggukkan kepala dan tersenyum"
    larasati "Ayo kita lanjutkan perjalanan"
    jump desa_kawung
    # ------ end ch 3 ---------


label desa_kawung:
    scene bg bukit
    with fade
    narrator "Makara dan Larasati turun dari gunung untuk melanjutkan perjalanannya"
    narrator "Perjalanan turun gunung hanya membutuhkan waktu yang tidak banyak"
    narrator "Makara sudah memberitahukan Larasati sebelumnya"
    narrator "Larasati melihat dua kertas yang sudah ada gambar desain batiknya sendiri"
    narrator "Lalu tersenyum dengan hasil desainnya sendiri"
    narrator "Larasati belajar banyak hal di dunia batik ini"
    narrator "Berikutnya Larasati tidak sabar untuk sampai Desa Kawung"
    show larasati_senang at left
    with easeinleft
    larasati "Masih jauh kah...?"
    show makaras_base at right
    with easeinright
    makhluk_1 "Tidak juga"
    makhluk_1 "Jarak dari atas gunung Megamendung ke Desa Kawung tidak begitu jauh"
    narrator "Dan benar saja"
    narrator "Desa Kawung sudah jelas terlihat di mata mereka"
    hide larasati_senang
    hide makaras_base
    stop music fadeout 1.0
    with fade

    scene bg desa_kawung
    play music "BGM/kawung.mp3" volume 0.7
    with dissolve
    show larasati_tertarik at left
    with easeinleft
    larasati "Itu desanya....?"
    show makaras_senang at right
    with easeinright
    makhluk_1 "Benar"
    larasati "WOW..."
    hide larasati_tertarik
    hide makaras_senang
    show larasati_senang at left
    show makaras_base at right
    larasati "Apa ada orang yang tinggal disana ?"
    makhluk_1 "Ada"
    makhluk_1 "Tapi kita tidak bisa berbicara dengan mereka"
    makhluk_1 "Dan juga mereka tidak bisa melihat kita"
    hide larasati_senang
    show larasati_bingungheran at left
    larasati "Heeh kenapa begitu... ?"
    makhluk_1 "Mereka adalah orang-orang asli Desa Kawung"
    makhluk_1 "Mereka juga tidak bisa meninggalkan desa mereka"
    narrator "Larasati tidak mengerti ucapan Makara"
    hide larasati_bingungheran
    show larasati_bingungcemas at left
    makhluk_1 "Nanti kamu juga tahu ketika sampai di sana"
    larasati "Kawung itu apakah motif batik dari dunia ku juga ?"
    makhluk_1 "Ya benar"
    makhluk_1 "Kawung ini berasal dari Yogyakarta"
    hide larasati_bingungcemas
    show larasati_kalem at left
    larasati "Hmm... begitu"
    larasati "Sebenarnya kamu tahu seberapa banyak tentang dunia luar ?"
    larasati "Maksudku dunia aku"
    makhluk_1 "Tidak banyak"
    makhluk_1 "Aku hanya tahu tentang yang ada di dunia ini saja"
    makhluk_1 "Sebenarnya apa yang kamu lihat disini aku mengetahuinya"
    makhluk_1 "Tapi selebihnya aku tidak tahu banyak tentang dunia kamu"
    larasati "Ohh begitu ya..."
    narrator "Larasati berpikir kira-kira rintangan apa yang ada di desa tersebut"
    narrator "Tapi Dia tidak begitu cemas"
    narrator "Karena sudah banyak pelajaran yang dipahami sejak kedatangannya disini"
    narrator "Tapi ada satu hal yang masih ia bingungkan"
    hide larasati_kalem
    show larasati_bingungcemas at left
    narrator "Bagaimana caranya keluar dari dunia ini ?"
    larasati "Kira-kira penduduk Desa Kawung biasanya melakukan apa ?"
    makhluk_1 "Hmm..."
    makhluk_1 "Mereka biasanya bertani, mencari persediaan makanan, berinteraksi dengan satu sama lain dan banyak lagi"
    hide larasati_bingungcemas
    show larasati_senyum at left
    larasati "Hampir sama seperti dunia ku juga ya"
    hide larasati_senyum
    show larasati_senang at left
    larasati "Eh kita boleh masuk ke desa ini ?"
    makhluk_1 "Boleh-boleh saja"
    makhluk_1 "Lagipula mereka tidak dapat melihat kita"
    larasati "tapi sebelum itu aku ingin bertanya ?"
    makhluk_1 "Hmm...."
    makhluk_1 "Apa itu?"
    hide larasati_senang
    show larasati_bingungcemas at left
    larasati "Sepertinya aku tidak melihat rintangan di desa ini ?"
    larasati "Penduduk desa ini juga tidak menyadari kehadiran kita ?"
    larasati "Lalu apa yang kita lakukan disini ?"
    makhluk_1 "Kalau kamu perhatikan desa ini"
    makhluk_1 "Ada beberapa hal yang dapat kamu ambil"
    larasati "....."
    hide larasati_bingungcemas
    show larasati_senang at left
    narrator "Larasati menyadari desa ini memiliki pola seperti batik"
    hide larasati_senang
    show larasati_tertarik at left
    larasati "Sepertinya aku punya ide lagi untuk desain batik"
    hide larasati_tertarik
    with wipeleft
    hide makaras_base
    with wiperight
    play sound "audio/SFX/footstep2.mp3" fadeout 0.5
    narrator "Larasati pun berjalan mengelilingi desa untuk mencari tempat yang cocok untuk menggambar desainnya"
    narrator "Larasati dan Makara berjalan mengelilingi Desa Kawung"
    narrator "Dan melihat kehidupan penduduk desa tersebut"
    play sound "audio/SFX/suasanadesa.mp3" fadeout 1.5
    narrator "Seperti kehidupan manusia pada umumnya"
    narrator "Tapi semua penduduk terlihat senang dan bahagia"
    narrator "Tidak ada satupun yang sedih atau konflik diantara mereka"
    stop sound fadeout 0.5
    show larasati_senang at left
    with easeinleft
    larasati "Penduduk desa ini terlihat bahagia semua"
    show makaras_senang at right
    with easeinright
    makhluk_1 "Sepertinya begitu"
    narrator "Larasati melihat ada salah satu penduduk yang beda dari yang lainnya"
    hide larasati_senang
    show larasati_bingungheran at left
    narrator "Dia menggunakan aksesoris seperti topi"
    larasati "Orang itu terlihat berbeda dari yang lainnya"
    larasati "Tapi apa yang bisa didapat ?"
    narrator "Larasati mencoba untuk mencari makna dan esensi dari Desa Kawung ini"
    hide larasati_bingungheran
    with moveoutleft
    hide makaras_senang
    with moveoutright
    show larasati_bingungcemas
    narrator "Larasati pun berdiri di atas batu yang cukup besar"
    narrator "Dan duduk di atas batu yang ia naiki"
    narrator "Tapi Larasati hanya mendapat ide untuk desain motif batik"
    hide larasati_bingungcemas
    show larasati_tertarik
    larasati "Sepertinya aku punya ide untuk desain yang berikutnya"
    hide larasati_tertarik 
    show larasati_senyum
    larasati "Hmm....."
    larasati "Sepertinya motifnya begini"
    narrator "PUZZLE DRAG N DROP"
    hide larasati_senyum 
    show larasati_kalem
    narrator "Larasati membuat desain batik dengan serius"
    narrator "Tapi Dia juga memperhatikan Desa Kawung"
    narrator "Larasati melihat pemimpin dari penduduk tersebut"
    narrator "Dan mencari kesimpulan bahwa pemimpin tersebutlah yang membuat Desa Kawung terlihat damai seperti ini"
    larasati "Seorang pemimpin"
    larasati "Pemimpin yang baik akan membuat semuanya menjadi baik"
    hide larasati_kalem 
    show larasati_bingungheran
    larasati "Tapi kata-kata itu terdengar aneh"
    larasati "Pemimpin yang memiliki tanggung jawab…"
    larasati "Terhadap orang lain dan…"
    larasati "Terhadap dirinya"
    larasati "Memiliki kerendahan hati dan juga bijaksana"
    hide larasati_bingungheran 
    show larasati_bingungcemas
    larasati "Dan juga memiliki sifat adil ?"
    narrator ""
    hide larasati_bingungcemas 
    show larasati_kalem
    larasati "Sepertinya Aku mengerti"
    larasati "Seseorang harus rendah hati, memiliki rasa tanggung jawab terhadap orang lain dan juga dirinya sendiri"
    hide larasati_kalem
    show larasati_bingungcemas 
    larasati "Tapi benar tidak yah ?"
    narrator "Makara menghampiri Larasati yang ada di atas batu"
    hide larasati_bingungcemas
    show makaras_base at right
    with fade
    makhluk_1 "Kamu sedang apa duduk di atas batu ?"
    show larasati_bingungheran at left
    with dissolve
    larasati "Eh Makara ?"
    hide larasati_bingungheran
    show larasati_senang at left
    larasati "Aku tadi dapat ide desain dari Desa Kawung"
    hide makaras_base 
    show makaras_senang at right
    makhluk_1 "Hmm Benarkah ?"
    larasati "Iya..."
    hide larasati_senang
    show larasati_tertarik at left
    larasati "Sepertinya aku tahu esensi dari tempat ini"
    hide makaras_senang 
    show makaras_base at right
    narrator "Makara terdiam sebentar dan bertanya sesuatu ke Larasati"
    makhluk_1 "Kalau begitu"

    jump pilihan


label pilihan:
    default learned = False
    hide larasati_tertarik
    show larasati_bingungcemas at left
    makhluk_1 "Kira-kira apa esensi dari desa Kawung ini ?"
    larasati "Yang aku tahu dari penduduk disini, seseorang harus rendah hati dan juga...."
    menu:
        "...harus punya tanggung jawab":
            jump pilihan1
        "...memahami perasaan orang lain ":
            jump pilihan2

label pilihan1:
    hide makaras_base  
    show makaras_senang at right
    makhluk_1 "Hmm.. Benar"
    hide larasati_bingungcemas
    show larasati_senang at left
    makhluk_1 "Penduduk desa Kawung terlihat sangat ramah dan juga tidak terlihat adanya perdebatan diantara mereka"
    makhluk_1 "Karena pemimpin mereka rendah hati terhadap orang lain, bijaksana dan juga harus memiliki tanggung jawab terhadap diri sendiri maupun orang lain"
    $ learned = True
    jump pilihanumum

label pilihan2:
    hide makaras_base  
    show makaras_kaget at right
    makhluk_1 "Hmm.. "
    hide larasati_bingungcemas
    show larasati_pasrah at left
    makhluk_1 "Benar tapi kurang tepat"
    makhluk_1 "Penduduk desa Kawung terlihat sangat ramah dan juga tidak terlihat adanya perdebatan diantara mereka"
    hide makaras_kaget  
    show makaras_base at right
    makhluk_1 "Karena pemimpin mereka rendah hati terhadap orang lain, bijaksana dan juga harus memiliki tanggung jawab terhadap diri sendiri maupun orang lain"
    $ learned = False
    jump pilihanumum

label pilihanumum:
    hide larasati_pasrah
    show larasati_bingungheran at left
    makhluk_1 "Kamu orang yang cepat belajar juga ya"
    makhluk_1 "Ngomong-ngomong, coba aku lihat desain kamu"
    hide larasati_bingungheran
    show larasati_senang at left
    larasati "Ini..."
    narrator "Larasati menunjukkan tiga kertas yang masing-masing terdapat desain motifnya"
    narrator "Makara menaruh ketiga kertas tersebut di atas batu tepat di depan Larasati"
    makhluk_1 "Coba kamu simpulkan dari ketiga tempat yang sudah kita kunjungi"
    makhluk_1 "Hutan Parang"
    makhluk_1 "Gunung Megamendung"
    makhluk_1 "dan Desa Kawung"
    narrator "Larasati mencari kata-kata untuk kesimpulan dari awal berada di dunia ini"
    hide larasati_senang
    show larasati_senyum at left
    larasati "Hutan Parang"
    larasati "Aku belajar keberanian dan juga semangat juang"
    larasati "Keberanian dan semangat juang adalah prinsip yang kuat dan tidak mudah menyerah"
    larasati "Maka itu kunci untuk menghadapi tantangan hidup adalah keberanian dan semangat"
    larasati "Gunung Megamendung"
    larasati "Awan yang berputar dengan anggun"
    larasati "Aku belajar untuk menjadi pribadi yang tenang dan pribadi yang sabar"
    larasati "Maka setiap masalah yang aku hadapi harus dikendalikan dengan tenang"
    larasati "Maka itu kunci untuk menghadapi konflik batin adalah tenang dan sabar"
    larasati "Desa Kawung"
    larasati "Desa dengan rumah dan sawah yang tersusun dengan rapi"
    larasati "Penduduk yang ceria dan tidak ada permasalahan dalam bersosial"
    larasati "Dalam sebuah desa ini pasti ada pemimpin yang memiliki sifat adil, bijaksana dan juga rendah hati"
    larasati "Maka pemimpin inilah yang memiliki tanggung jawab terhadap dirinya sendiri dan orang lain di desa ini"
    larasati "Maka itu kunci untuk menyempurnakan dari keberanian, semangat juang, pribadi yang tenang dan sabar adalah…"
    larasati "Memiliki sifat kepemimpinan"
    larasati "Bertanggung jawab terhadap orang lain dan tanggung jawab terhadap dirinya sendiri"
    narrator "Setelah selesai membuat kesimpulan"
    narrator "Tiba-tiba saja ketiga kertas tersebut mengeluarkan cahaya"
    show dimensi
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide dimensi
    hide larasati_senyum
    show larasati_kagetbiasa at left
    narrator "Suasana sekitar berubah menjadi dramatis"
    hide larasati_kagetbiasa
    show larasati_kagetemoji1 at left
    with hpunch
    narrator "Tanah bergetar layaknya gempa bumi"
    hide larasati_kagetemoji1
    show larasati_kagetemoji2 at left
    with hpunch
    narrator "Angin bertiup sangat kencang"
    larasati "Huahhh....."
    hide larasati_kagetemoji2
    show larasati_kagethoror at left
    larasati "Apa yang terjadi ....??"
    narrator "Makara terlihat tenang dan hanya melihat sekitarnya"
    makhluk_1 "...."
    show makaras_senang at right
    makhluk_1 "....."
    narrator "Makara tersenyum"
    hide larasati_kagethoror
    show larasati_bingungheran at left
    makhluk_1 "Ternyata kamu sudah memahaminya"
    narrator "Tapi Larasati tidak mendengar perkataan Makara"
    narrator "Larasati...."
    hide larasati_bingungheran
    show larasati_bingungcemas at left
    larasati "Eh apa ? Makara kenapa dunia ini menjadi begini ?"
    narrator "Melihat Larasati panik"
    narrator "(Makara mencoba untuk membuat Larasati menjadi tenang"
    makhluk_1 "Larasati dengar"
    narrator "Larasati yang seketika melihat Makara"
    hide larasati_bingungcemas
    show larasati_bingungheran at left
    makhluk_1 "Tenangkan dirimu"
    makhluk_1 "Kamu sudah memahami esensi dan filosofi tentang setiap batik yang ada di dunia ini"
    makhluk_1 "Semuanya ada di dalam diri kamu"
    narrator "Larasati sekali lagi mencoba untuk tenang"
    narrator "Dan teringat momen ketika ia membuka buku Rahara Batik"
    narrator "Kejadian yang sama persis"
    narrator "Hanya berbeda tempat"
    hide larasati_bingungheran
    show larasati_bingungcemas at left
    larasati "Apa yang akan terjadi pada dunia ini ...??"
    makhluk_1 "Dunia ini tidak akan terjadi apa-apa, ini hanya membuktikan kamu sudah memahami setiap batik yang ada di dunia ini"
    makhluk_1 "Maksudku dunia buku Rahara Batik"
    makhluk_1 "Setelah ini kamu akan kembali ke dunia kamu"
    larasati "Kembali ke duniaku ?"
    hide larasati_bingungcemas
    show larasati_kagetbiasa at left
    larasati "Tunggu.... Kamu tahu buku Rahara Ba...."
    narrator "Kilatan cahaya datang dari berbagai arah"
    show dimensi
    with dissolve
    $renpy.pause(4.0, hard=True)
    narrator "Membuat dunia yang baru saja dilihat menjadi hilang"
    scene bg kamar_larasatimalam
    hide dimensi
    stop music fadeout 2.0
    with dissolve

    jump tibatiba_dikamar

label tibatiba_dikamar:
    show larasati_kagetbiasa
    play music "BGM/All_Idle_Game_BGM.mp3" volume 0.7
    larasati "Ehh.... dimana aku ....??"
    narrator "Kamar Larasati, tempat dimana Larasati menemukan buku Rahara Batik"
    narrator "Dan membuka buku tersebut"
    hide larasati_kagetbiasa
    show larasati_pasrah
    larasati "Pusing sekali"
    narrator "Larasati menyadari Dia sedang berada di kamarnya"
    hide larasati_pasrah
    show larasati_bingungcemas
    larasati "Heh ini di kamar ?"
    larasati "Aku sudah kembali"
    narrator "Larasati melihat sekelilingnya dengan teliti"
    larasati "Terakhir aku ingat…"
    larasati "Terjadi sesuatu di kamarku"
    larasati "Tapi kamarku terlihat rapi dan tidak ada yang berantakan"
    narrator "Larasati menoleh ke arah laci samping tempat tidurnya"
    narrator "Dia tahu buku yang membuatnya masuk ke dunia batik adalah buku Rahara Batik milik ayahnya"
    larasati "...."
    narrator "Larasati ingin melihat buku itu lagi"
    narrator "Ketika Larasati membuka laci tersebut terdapat buku Rahara Batik"
    narrator "Larasati mengambil buku tersebut dan hanya memegangnya"
    larasati "Tidak akan terjadi sesuatu kan ?"
    narrator "Larasati membuka buku tersebut dan tidak ada hal yang terjadi"
    narrator "Buku Rahara Batik berisi tentang batik Parang, Megamendung, dan Kawung. Terdapat desain motif batik yang Ia kenali"
    narrator "Larasati mengambil buku tersebut dan hanya memegangnya"
    larasati "Ini gambar tangan ayah"
    larasati "Aku mengenalinya"
    narrator "Larasati membolak-balikkan buku karena ada rasa penasaran"
    narrator "Tetapi hanya terdapat desain motif ayahnya dan penjelasan tentang motif batik tersebut"
    larasati "....."
    narrator "Melihat desain motif ayahnya"
    narrator "Larasati teringat apa yang terjadi selama di dunia batik"
    narrator "Aspek-aspek serta filosofi tentang batik yang dilihatnya"
    narrator "Ternyata memiliki maknanya tersendiri"
    larasati "....."
    narrator "Di halaman terakhir buku ada gambar seperti burung" 
    narrator "Tapi gambar tersebut tidak terlihat dengan jelas"
    larasati "....."
    hide larasati_bingungcemas
    show larasati_senyum
    larasati "Makara"
    hide larasati_senyum
    show larasati_senang
    larasati "Terima kasih...."
    narrator "Teringat sudah lama berada di dunia batik, Larasati tidak tahu berapa lama Ia berada disana"
    larasati "Eh iya.."
    larasati "Sekarang sudah jam berapa ?"
    narrator "Larasati meletakkan kembali buku Rahara Batik di laci"
    narrator "Pukul 21:25"
    larasati "Lohh.. ?!?!"
    narrator "Larasati kaget karena jam menunjukkan pukul 21:25"
    larasati "Perasaan aku lama sekali berada di sana"
    larasati "Ternyata waktu berjalan lebih lambat"
    larasati "Atau aku sudah seharian berada di sana ?"
    narrator "Tiba-tiba ibunya datang ke kamarnya"
    show larasati_senang:
        xalign 0.2 yalign 1.3
    show sriyanitua_bingung at right
    with fade
    sriyani "...."
    sriyani "Laras....?"
    sriyani "Kamu jam segini belum mandi juga ?"
    sriyani "Kamu kan tadi habis main sama temen kamu"
    larasati "Eh ibu...?"
    larasati "iya ini aku.... baru saja mau mandi"
    sriyani "Kalau sudah selesai langsung tidur, ingat jangan begadang ya sayang"
    larasati "Iya bu"
    hide sriyanitua_bingung
    hide larasati_senang
    show larasati_bingungheran at center
    with dissolve
    narrator "Larasati heran"
    narrator "Ternyata waktu seperti berhenti ketika berada di sana"
    narrator "Larasati menoleh ke arah meja kerjanya"
    larasati "....."
    larasati "Ah iya aku ada tugas yang harus dikerjakan"
    narrator "Larasati teringat desain motif batik yang dibuatnya saat berada di dunia batik"
    narrator "Kertas yang diberikan oleh Makara hilang"
    hide larasati_bingungheran
    show larasati_senang
    narrator "Tapi semua desain yang sudah dibuat teringat di kepala Larasati"
    narrator "Begitupun dengan esensi dan filosofi yang dipelajarinya"
    narrator "Sudah tertanam di dalam dirinya"
    larasati "Sebaiknya dikerjakan besok saja"
    larasati "Aku mau mandi lalu istirahat"
    narrator "Sebuah kejadian yang tidak terlupakan"
    narrator "Kejadian yang tidak bisa dijelaskan secara logika atau ilmiah"
    narrator "Seperti dunia fantasi yang terjadi di film-film terkenal"
    with dissolve
    scene bg kamar_larasati
    with fade
    narrator "Satu minggu setelah kejadian"
    narrator "Pukul 09:14"
    narrator "Larasati menyelesaikan desain motif batik yang dipesan oleh pelanggan"
    narrator "Dan membuat selendang dengan baik seperti biasanya"
    narrator "Banyak sekali perubahan yang ada di Larasati"
    narrator "Bahkan Ibunya menyadari ada perubahan dari Larasati"
    narrator "Gaya bicara"
    narrator "Keputusan yang diambil"
    narrator "Semangat yang lebih"
    narrator "Tanggung jawab yang baik"
    narrator "Emosi yang terkendali"
    scene bg ruang_menjahit
    with fade
    show sriyanitua_senyum at right
    sriyani "Laras..."
    sriyani "Desain motif batik yang kemarin sudah kamu kirim ?"
    show larasati_senyum:
        xalign 0.2 yalign 1.3
    with fade
    larasati "Yang motif Parang ?"
    sriyani "Iya sayang"
    larasati "Sudah tapi belum ada balasan dari orangnya"
    sriyani "Oh begitu ya sayang...."

    jump pilihan_quiz4

label pilihan_quiz4:
    default tau = False
    sriyani "Kamu tahu motif parang itu darimana ?"
    menu:
        "Dari Keraton Mataram Kartasura Solo":
            jump pilihan_quiz4_1
        "Dari Keraton Tarumanegara Kartasura Solo":
            jump pilihan_quiz4_2

label pilihan_quiz4_1:
    sriyani "Hmm..."
    hide sriyanitua_senyum
    show sriyanitua_senang at right
    sriyani "Benar"
    $ tau = True
    jump pilihan_umum_quiz4

label pilihan_quiz4_2:
    sriyani "Hmm..." 
    sriyani "Bukan..."
    sriyani "Yang benar itu Keraton Mataram Kartasura Solo"    
    $ tau = False
    jump pilihan_umum_quiz4

label pilihan_umum_quiz4:
    narrator "Dengan kejadian Larasati di dunia batik"
    hide sriyanitua_senang
    show sriyanitua_bahagia at right
    hide larasati_senyum
    show larasati_senang:
        xalign 0.2 yalign 1.3
    narrator "Hubungan dengan Ibunya menjadi baik"
    narrator "Hubungan anak dengan Ibu yang harmonis"
    narrator "Itulah hal yang harus terjadi"
    stop music fadeout 1.5
    with dissolve
    jump epilog

label epilog:
    play music "BGM/All_Idle_Game_BGM.mp3" volume 0.7
    scene bg kamar_larasati
    with fade
    show larasati_kalem
    larasati "Hmmm...." 
    larasati "Selendangnya bagus juga kalau begini"
    narrator "Larasati membuat selendang untuk temannya"
    narrator "Tiba-tiba notif handphone masuk"
    narrator "Larasati langsung mengecek notif tersebut"
    hide larasati_kalem
    with dissolve
    show phone at center
    with dissolve
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    larasati "Ish… kirain pelanggan yang kemarin"
    rani "Oii..."
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "Ntar sore ke kafe lagi yuk..."
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "Sore ini ?"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "Ya iya dong  :)"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "Kamu lagi sibuk gak ?"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "Ngga juga sih, aku sih mah ayuk aja"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "Oke bestie"
    play sound "audio/SFX/typing4.mp3" fadeout 1.5
    larasati "Kafe yang mana ?"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "Tempat biasaaaa...."
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "Oh... oke"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "Oke aku kesana jam 15:40 udah gerak"
    play sound "audio/SFX/typing3.mp3" fadeout 0.7
    larasati "Oke bestie.... "
    stop sound fadeout 0.5
    hide phone
    with dissolve
    show larasati_kalem
    with dissolve
    larasati "Kebetulan sekali"
    larasati "Aku harus menyelesaikan selendangnya sekarang"
    narrator "Pukul 15:25"
    hide larasati_kalem
    scene bg ruang_menjahit
    show sriyanitua_tulus at right
    show larasati_senang:
        xalign 0.2 yalign 1.3
    with dissolve
    larasati "Bu aku jalan dulu"
    sriyani "Iya hati-hati ya sayang..."
    sriyani "Jangan terlalu malam, kalau sudah mau hujan langsung pulang"
    larasati "Iya bu"
    stop music fadeout 2.0
    with dissolve
    jump kafe_epilog


label kafe_epilog:
    play music "BGM/Cafe_BGM2.mp3" volume 0.7
    scene cafe
    with fade
    show larasati_kalem
    narrator "Larasati tiba di kafe terlebih dahulu"
    narrator "Dengan membawa sesuatu untuk diberikan ke Rani"
    narrator "Pukul 15:58"
    narrator "Rani datang"
    narrator "Larasati melihat Rani, tapi ada seseorang disebelahnya"
    hide larasati_kalem
    show larasati_bingungheran:
        xalign 0.2 yalign 1.3
    show rani_senyum at right
    with dissolve
    rani "Hai Laras kenalin ini kak Satria yang kubilang kemarin"
    rani "Tapi kamu kayaknya udah kenal sih"
    larasati "Halo kak..."
    show rani_senyum:
        xalign 0.65 yalign 1.3
    show satria_senyum:
        xalign 1.05 yalign 1.3
    with dissolve
    satria "Halo laras..."
    larasati "Eh iya kak.."
    hide larasati_bingungheran
    show larasati_senang:
        xalign 0.2 yalign 1.3
    larasati "Ohya Rani, nih aku ada sesuatu buat kamu"
    hide rani_senyum
    show rani_senang:
        xalign 0.65 yalign 1.3
    rani "Apa tuh?"
    narrator "Larasati mengeluarkan kotak berukuran persegi lalu membukanya"
    larasati "Tada...."
    narrator "Rani tidak bisa berkata-kata"
    hide rani_senang
    show rani_ngodain:
        xalign 0.65 yalign 1.3
    rani "Eh itukan.... sarung ??"
    hide larasati_senang
    show larasati_pasrah:
        xalign 0.2 yalign 1.3
    satria "Itu selendang"
    larasati "ini selendang loh Rani"
    hide rani_ngodain
    show rani_jahil:
        xalign 0.65 yalign 1.3
    rani "Eh hahaha...."
    narrator "Larasati memberikan selendang tersebut ke Rani"
    hide larasati_pasrah
    show larasati_senyum:
        xalign 0.2 yalign 1.3
    larasati "Coba deh kamu pakai ini..."
    hide rani_jahil
    show ranisweater_nyengir:
        xalign 0.65 yalign 1.3
    rani "Cocok gak laras ?"
    hide larasati_senyum
    show larasati_tertarik:
        xalign 0.2 yalign 1.3
    larasati "Cocok sih buat kamu..."
    hide ranisweater_nyengir
    show ranisweater_senang:
        xalign 0.65 yalign 1.3
    rani "Laras makasih yah....."
    hide larasati_tertarik
    show larasati_senang:
        xalign 0.2 yalign 1.3
    larasati "Iyaa Rani"
    larasati "ohya kak Satria maaf ya aku tidak tau kalau kamu juga datang"
    hide satria_senyum
    show satria_merem:
        xalign 1.05 yalign 1.3
    satria "Oh tidak apa-apa"
    larasati "Lagi pula Rani ga ngasih tahu kalau kakak datang juga"
    rani "Sebenarnya kak Satria ini pengen tahu cara membuat motif batik"
    rani "Berhubung kamu tahu banyak tentang batik"
    satria "Eh iya, aku ada tugas prakarya"
    satria "Tugasnya itu disuruh buat dua motif batik"
    satria "Kamu mau bantuin gak? Tentu saja tidak secara gratis"
    satria "Anggap saja aku seperti membeli kain batik yang kamu buat"
    hide larasati_senang
    show larasati_senyum:
        xalign 0.2 yalign 1.3
    larasati "Boleh kok kak..."
    narrator "Obrolan mereka berlanjut sampai pukul 17:02 , mereka harus pulang karena hujan mau turun"
    rani "Eh sudah mau hujan nih"
    larasati "Pulang sekarang aja ..?"
    rani "Iya deh laras seperti pulang saja kita"
    satria "Ohya ini nomor aku, kalau ada waktu lagi kita bisa ketemuan membahas hal ini"
    larasati "Ohya oke kak..."
    rani "Oke laras sampai jumpa di sekolah besok"
    larasati "iya Rani...."
    hide ranisweater_senang
    hide satria_merem
    hide larasati_senyum
    with dissolve
    narrator "Mereka pun pulang meninggalkan kafe"
    with fade
    jump story_ending


label story_ending:
    scene bg kamar_larasatimalam
    show larasati_kalem
    with dissolve
    larasati "Hmm...."
    larasati "Makara pernah bilang dia tahu dunia manusia karena seseorang pernah memberitahukannya"
    larasati "Kira-kira orang yang dimaksud siapa ya ?"
    
    return