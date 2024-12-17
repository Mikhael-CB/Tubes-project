# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default persistent.main_menu_bg = gui.main_menu_background

define prot = Character("Aku", color = "#d9e7f1")
define deh = Character("Dehen", color = "#2a506b") 
define wis = Character("Dr. Wisnu", color = "#666666")
define mau = Character("Maura", color = "#d45680")
default remember = 0

transform left:
    xalign 0.15
    yalign 0.54
    zoom 2

transform right:
    xalign 0.85
    yalign 0.54
    zoom 2

transform centerC:
    xalign 0.5
    yalign 0.54
    zoom 2

transform x_flip:
    xzoom -1.

transform no_flip:
    xzoom 1
    yzoom 1.

transform zoom05x:
    zoom 0.5

transform bounce(num, interval):
    pause .05
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat num

transform darken:
    linear 0.5 matrixcolor TintMatrix("#696969") * SaturationMatrix(1.0)
transform lighten:
    linear 0.5 matrixcolor TintMatrix ("#ffffff") * SaturationMatrix(1.0)
transform darken_cus(time):
    linear (time) matrixcolor TintMatrix("#696969") * SaturationMatrix(1.0)
transform lighten_cus(time):
    linear (time) matrixcolor TintMatrix ("#ffffff") * SaturationMatrix(1.0)
transform opaque(X):
    linear (time) matrixcolor TintMatrix("#000000") * OpacityMatrix(X)
$ jawaban = ""




define vpunch_cus = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
define hpunch_cus = Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=.275)

# The game starts here.

label start:
    
    scene filler
    play music "SCENE 1_ SAMARINDA/Chill and Happy.mp3" loop if_changed
    "Anda tinggal di Samarinda dan bekerja untuk Dr. W.R. Wisnu Raksa, ilmuwan paling cerdas di negara ini.
    Impianmu adalah menjadi ilmuwan terkemuka dan mampu memenangkan nobel di tahun ini."

    
    
    prot "Aduh, proyek dari Pak Wisnu besar sekali, aku merasa sangat lelah.
    Sudah 5 hari aku tidur di laboratoriumnya yang sangat dingin itu"
    
    
    "Anda saat ini sedang menuju perjalanan ke rumah setelah 5 hari tidak pulang." 
    stop music fadeout 1.0
    #scene bg house_room #pending asset
    
    show bg kamar
    with dissolve
    play music "SCENE 1_ SAMARINDA/Cozy Home Music.mp3" fadein 1.0 loop if_changed volume 0.4
    "Sesampainya di rumah, anda segera mandi, memakai baju, lalu tidur karena kelelahan."
    "Anda dikejutkan dengan telepon yang masuk, ternyata dari rekan sejawat Anda, Dehen"
    
    prot "Haaah, baru saja aku memejamkan mata." 
    prot "Halo Dehen, mengapa kau menelponku."

    deh "Aku ada di depan rumahmu dengan membawa makanan, cepat buka"    
    "Anda bergegas menuju pintu dan membukanya."
    
    show dehen neutral at centerC
    with dissolve
    show bg kamar
    #show dehen #pending asset
    deh "Aku tahu kau pasti tidak sempat membeli makan karena lembur 5 hari, jadi aku membelikannya untukmu."
    show dehen senang at bounce(1, 0.175)
    with Dissolve (0.1)

    deh "Mari makan bersama!"

    prot "Wah, terima kasih teman"

    show dehen at darken
    "Anda terkejut karena Dehen membeli banyak sekali makanan seperti sate payau, gence ruan, ayam cincane, nasi bekepor, pisang gapit, dan lainnya."
    show dehen at lighten
    prot "Hey, mengapa kau membeli banyak sekali makanan? Siapa yang akan menghabiskannya?"

    deh "Sudahlah, jika tak habis kau masukkan saja ke kulkas."
    deh "Komisi yang diberi Pak Wisnu atas penelitian ini besar sekali, sesekali kita juga harus self rewards."

    prot "Memang sepantasnya kita mendapat komisi sebesar itu, penelitian Pak Wisnu ini memiliki risiko yang tinggi, salah sedikit saja kita bisa mengalami mutasi akibat radiasi sinar-sinar itu."
    show dehen at darken
    
    "Setelah Anda dan Dehan selesai makan, Anda mencuci peralatan makan, sedangkan Dehan membersihkan dan merapikan kembali meja makan Anda."
    
    show dehen at lighten
    prot "Dehen, apa rencanamu sore ini?"

    deh "Entahlah, mungkin aku akan menonton tv dan bersantai di rumah"
   
    menu Free_time:
        "Apa yang ingin kamu lakukan sore ini?"
        "Bersantai untuk menikmati me time":
            prot "Yah, sepertinya aku juga akan melakukan hal yang sama. Aku ingin menonton serial favoritku"
            deh "Baiklah, selamat me time, aku pamit pulang"
            prot "Terima kasih untuk makannya, Dehan"
            deh "Tak masalah teman"
            hide kamar with dissolve
            hide dehen with dissolve
            "Anda pun mengantar Dehen hingga ke teras dan membukakan pagar untuknya."
            
            show bg kamar
            "Setelah Dehen pulang Anda masuk kamar dan mulai menyalakan TV. Setelah menunggu beberapa jam, akhirnya serial favorit Anda mulai tayang. "
            "Anda sangat senang karena sudah 5 hari melewatkannya"
            
            prot "Akhirnya aku bisa menontonnya kembali"
            show bg kamar at darken
            "Baru 15 menit menonton, terjadi pemadaman listrik di kecamatan Anda, hal itu membuat anda kesal"
            prot "Kenapa sih harus terjadi pemadaman sekarang? Padahal serial ini tidak di upload di Youtube, aku melewatkannya lagi"
            "Anda pun hanya diam menatap lampu emergensi yang menyala. Di tengah kesunyian akibat pemadaman listrik Anda pun berpikir seandainya jumlah listrik di Indonesia sangat besar, pasti tidak akan terjadi pemadaman"
            prot "Kenapa Indonesia tidak memiliki listrik yang cukup dari Sabang hingga Merauke ya? Padahal kan semua orang membayar listrik, jika padam begini aktivitas masyarakat akan terganggu. Apalagi zaman modern ini, siapa coba yang ga pake listrik?"
            "Sempat terbesit di pikiran Anda seandainya ada daya listrik yang besar namun murah di seluruh penjuru di Indonesia."
            "Semakin lama, mata Anda semakin berat dan Anda pun tertidur"
            stop music fadeout 0.5
            jump scene2
        "Membaca jurnal ilmiah":
            prot "Sepertinya menyenangkan. Aku ingin membaca jurnal saja, mengejar impianku menjadi pemenang nobel tahun ini. Penelitian Pak Wisnu membuatku terjeda melakukan penelitianku sendiri"
            deh "Semoga kau segera menjadi pemenang nobel. Jangan terlalu memaksakan dirimu juga kawan"
            prot "Tak apa, aku sudah terbiasa dengan ini semua"
            deh "Baiklah aku pulang dulu sekarang"
            prot "Terima kasih untuk makannya, Dehen"
            deh "Tak masalah teman"
            hide dehen with dissolve
            "Anda mulai menyalakan komputer yang berada di kamar Anda."
            "Sambil menunggu komputer loading, Anda akan…"
            menu menunggu_komputer_loading:
                "Sambil menunggu komputer loading, Anda akan…"
                "Menyeduh kopi dan mengambil snack di kulkas":
                    "Anda pun menyeduh kopi dan mengambil snack di kulkas"
                "Membuat Teh dan mengambil biskuit di toples":
                    "Anda membuat Teh dan mengambil biskuit di toples"
                "Memasak mie instan lengkap dengan telur mata sapi":
                    "Anda memasak mie instan lengkap dengan telur mata sapi"
            "Kemudian Anda kembali ke kamar dan duduk di kursi yang berada di depan komputer Anda."
            "Anda membuka google dan membaca…"
            menu membuka_google:
                "Anda membuka google dan membaca…"
                "Jurnal para pemenang nobel tahun-tahun sebelumnya":
                    "Anda membaca jurnal para pemenang nobel tahun-tahun sebelumnya"
                    $ jawaban = "Enrico Fermi, seorang pemenang nobel fisika tahun 1938, karyanya mampu menjadi pionir dalam mengembangkan reaktor nuklir."
                "Berita kondisi Indonesia saat ini":
                    "Anda membaca Berita kondisi Indonesia saat ini"
                    $ jawaaban = "kondisi rakyat indonesia yang masih saja beberapa kali mengalami pemadaman listrik akibat jumlah listrik di Indonesia yang tidak terlalu besar."
                "Berita kondisi negara-negara di dunia":
                    "Anda membaca Berita kondisi negara-negara di dunia"
                    $ jawaban = "negara yang sudah menerapkan PLTN sehingga listrik tidak pernah mengalami pemadaman dan harganya sangat murah."
                "Gosip artis yang sedang hangat":
                    "Anda membaca Gosip artis yang sedang hangat"
                    $ jawaban = "Artis yang sedang berlibur di luar negeri bercerita masyarakat di sana tidak pernah mengalami pemadaman listrik."
            "Setelah kurang lebih 30 menit, Anda mulai membuka file penelitian Anda. Tampak informasi yang lengkap dan akurat mengenai nuklir. "
            "Anda mulai berkutat dengan berbagai jurnal dan video yang ada di youtube untuk mendukung kesuksesan penelitian nuklir Anda."
            "Tak terasa waktu sudah menunjukan pukul 2 pagi. Anda pun mematikan komputer dan berjalan menuju tempat tidur untuk beristirahat." 
            "Saat hendak tidur Anda teringat"
            "[jawaban]"
            stop music fadeout 0.5
            hide bg kamar with dissolve
            jump scene2





label scene2:
    centered "{size=*2}Besok pagi{/size}"
    show text "{size=*2}Besok pagi{/size}" at truecenter
    hide text with dissolve
    pause 0.5
    play sound "SCENE 2_ Menuju Pulau Gelasa/Cell Phone Ringing - Sound Effect.mp3" volume 0.9
    pause 0.2

    
    with hpunch_cus
    "{i}RINGGGG.... RINGGGG..... RINGGGG...{/i}" 
    

    stop sound fadeout 0.2
    show bg kamar with Dissolve(1.0)
    queue music "SCENE 2_ Menuju Pulau Gelasa/Chill.mp3" loop fadein 0.5

    "Lagi-lagi Anda terbangun akibat dering di ponsel Anda."
    "Ternyata pesan dari Dr. Wisnu yang mengabarkan akan mengadakan pertemuan penting bersama semua asistennya."
    "Pertemuan akan dilakukan pukul 7.00 di laboratorium Dr. Wisnu"
    prot "huh, ada hal apa yang yang ingin dibicarakan?"
    "Anda pun bergegas mandi dan menghangatkan makanan yang diberikan Dehen kemarin."
    stop music fadeout 0.5
    hide bg kamar with dissolve
    "Setelah sarapan Anda berangkat ke laboratorium Dr. Wisnu."
    
    pause 0.5
    centered "{size=*2}Laboratorium{/size}"
    show text "{size=*2}Laboratorium{/size}" at truecenter
    hide text with dissolve
    pause 1
    
    play music "SCENE 2_ Menuju Pulau Gelasa/Lab Music.mp3" loop fadein 0.5 volume 0.7
    
    show bg laboratorium with Dissolve(1.0)
    "Sesampainya di sana, Anda menyapa semua asisten Dr. Wisnu, termasuk Dehen."
    show dr_wisnu neutral at centerC with dissolve
    "Beberapa menit kemudian Dr. Wisnu masuk kedalam ruangan dan memberi informasi mengenai suatu proyek rahasia milik negara."
    "Proyek ini disponsori langsung oleh BUMN dengan modal minimal 100 triliun rupiah. Dr. Wisnu berpesan untuk menjaga kerahasiaan proyek ini."
    
    "Dr. Wisnu berpesan untuk menjaga kerahasiaan proyek ini. Setelah mendengar informasi lengkap tentang proyek dan peran Anda pada proyek ini, Dr. Wisnu meminta semua asistennya untuk menandatangani MOU. "
    
    "Anda tidak menyangka PLTN yang semalam Anda pikirkan sekilas sebelum tidur kini benar-benar menjadi kenyataan di Indonesia."
    "Anda pun merasa.."

    menu merasa:
        "Anda pun merasa.."
        "sangat jenius karena pernah memikirkannya":
            "khayalan yang dipirkirkan menjadi kenyataan"
        "biasa saja karena proyek itu sudah terlaksana di negara lain":
            "sudah waktunya memang indonesia maju untuk setara dengan negara lain"
        "akan menjadi kaya karena itu merupakan proyek besar":
            "pemikiran tentang uang yang dapat didapat dari proyek ini memenuhi pikiran Anda"
        "sangat bersyukur dan berusaha melakukan hal yang terbaik":
            "dengan ini kita dapat membantu semua orang di Indonesia"
    "Tidak berlansung dua detik pun, Dr. Wisnu Berkata"

    wis "Segera siapkan diri kalian dan mulai packing! Minggu depan kita akan berangkat ke pulau Gelasa."

    hide dr_wisnu neutra with dissolve

    "Seketika Dr. Wisnu membubarkan pertemuannya." 
    
    show dehen neutral at centerC
    show dehen at darken
    "Dehen perlahan mendekati Anda."
    show dehen at lighten
    with dissolve

    deh "Kita akan sampai di Gelasa besok sore. Aku dengar dari Dr. Wisnu kita baru memulai proyek ini setelah dua hari di sana."
    prot "Iya, yang tadi dipaparkan bukan? Pemasangan internet 6G juga selesai di saat itu. Oh, tadi katanya akan ada tambahan seorang lagi untuk melancarkan proyek ini?"
    deh "Ya, benar. Orang itu merupakan anggota Penelitian Radioaktivitas dan Kekuatan Atom yang diketuai langsung oleh Dr. Wisnu, namanya Maura."
    prot "Darimana kau tahu tentang hal sejauh ini?"

    show dehen senang with dissolve
    "Dehen tidak menjawab, ia hanya tersenyum tipis kepada Anda kemudian memalingkan mukanya."
    hide dehen with dissolve
    "Anda tahu, pasti lagi-lagi Dehen menguping percakapan Dr. Wisnu, karena cuma dia yang bisa berbahasa Ambon."
    "Dr. Wisnu sering menggunakan bahasa Ambon jika memberi informasi penting di teleponnya, tujuannya untuk menghindari penyadapan informasi."
    "Sebab saat ini hanya sedikit orang yang bisa berbahasa daerah, itupun didominasi oleh bahasa jawa dan sunda saja."
    "Mayoritas orang lebih tertarik mempelajari bahasa Inggris, mandarin, jerman, dan prancis."
    "haahh, waktunya bersiap untuk minggu depan"
    hide bg laboratorium with Dissolve(1)
    stop music fadeout 2
    pause 1
    scene filler
    jump scene3

label scene3:

    centered "{size=*2}Pulau Gelasa{/size}\n1 minggu kemudian"
    show text "{size=*2}Pulau Gelasa{/size}\n1 minggu kemudian" at truecenter
    hide text with dissolve
    pause 2
    play music "SCENE 3_ Pulau Gelasa/Beach Music Day.mp3" fadein 1.0 volume 0.3 loop
    hide text with dissolve
    pause 0.3
    
    show bg pantai siang
    "Setelah perjalanan yang panjang, akhirnya Anda dan tim Dr.Wisnu sampai di Pulau Gelasa."

    show dehen neutral at centerC
    prot "Dehen, apa yang akan kau lakukan setelah sampai di pulau itu?"
    deh "Membangun PLTN"
    prot "Bukan itu maksudku..."
    
    show dehen senang at bounce(2, 0.1)
    "Dehen tertawa melihat ekspresiku yang kesal"
    show dehen neutral
    deh "Malam ini aku akan membongkar barang-barangku dari dalam koper dan menatanya di mess, kemudian aku akan segera tidur. Duluan ya!"
    prot "Oke, jangan begadang main lagi ya Dehen"
    show dehen senang at bounce(2, 0.05)
    "Dehen tertawa"
    hide dehen with dissolve
    "Dengan itu, Dehen pergi ke kamarnya di mess"
    "Ada beberapa hal yang dapat anda lakukan untuk hari ini"
    "Anda akan.."
    menu anda_akan:
        "Anda akan.."
        "mengikuti apa yang Dehen lakukan":
            "Anda memilih untuk mengikuti apa yang Dehen lakukan"
            $ remember = 1
        "menikmati pemandangan malam di tepi laut":
            "Anda memilih untuk menikmati pemandangan malam di tepi laut"
            $ remember = 2
        "berjalan-jalan di sekitar mess":
            "Anda memilih berjalan-jalan di sekitar mess"
            $ remember = 3
    "Ternyata Pulau Gelasa memiliki penampakan alam yang sangat indah, bahkan meski dilihat di malam hari."
    "Berbeda dari Samarinda, Jakarta, ataupun Bangka Belitung, penduduk di pulau ini bisa dihitung pakai jari."
    "Penginapan yang dibangun juga dikhususkan untuk para pekerja saja."
            
    "Anda takjub dengan semua pemandangan ini ketika menginjakkan kaki di pasir pantai yang berwarna putih seperti kapas."
    "Para pihak militer membantu menurunkan semua barang kalian dari helikopter dan dibawakan menuju kamar mess masing-masing."
    "Anda pun mengikuti salah seorang anggota militer yang membantu membawakan tas anda. Tak lupa anda mengucap terima kasih kepadanya."
    stop music fadeout 0.5
    hide bg pantai siang with dissolve
    pause 0.5
    play music "SCENE 3_ Pulau Gelasa/Cozy Home Music.mp3" fadein 0.5 volume 0.7 loop
    show bg kamar with dissolve
    "Anda membongkar semua barang-barang yang ada di koper dan menatanya di lemari dengan rapi."
    "Saat masuk di kamar mandi untuk membersihkan badan, Anda terkejut ternyata terdapat water heater di dalamnya"
    prot "Tak ku sangka ternyata fasilitas di mess ini sangat lengkap, water heater, tv, komputer, AC, dan lainnya. Aku pasti sangat betah tinggal di pulau ini meskipun terpencil"
    "Setelah mandi dan memakai pakaian, Anda menyantap makanan yang sudah disiapkan di meja makan dan"

    if remember == 1:
        extend " bergegas tidur."
        stop music fadeout 0.5
    elif remember == 2:
        extend " memutuskan untuk berjalan-jalan di pantai menikmati keindahan alam di malam hari."
        stop music fadeout 0.5
        pause 0.5
        play music "SCENE 3_ Pulau Gelasa/Beach Music Night.mp3" fadein 0.5 volume 0.7 loop
        show bg pantai malam with dissolve
        "Suara ombak dan desir pasir membuat otak Anda benar-benar relax."
        "Anda melihat batu besar dan memutuskan untuk duduk di sana. Terlihat beberapa bayangan orang di dalam mercusuar"
        prot "Ketat sekali penjagaan di pulau ini, pasti mereka adalah orang yang mendapat tugas berjaga di shift malam"
        stop music fadeout 0.5
        hide bg pantai malam with dissolve
        "Setelah puas menikmati pemandangan alam, Anda kembali ke mess untuk tidur"        
    elif remember == 3:
        extend " memutuskan berjalan-jalan di sekitar mess."
        show bg ruang tamu with dissolve
        "Terdapat 3 mess dengan masing masing mess berisi 10 kamar."
        "Banyak kamar kosong di mess itu, kamar anda berada di lantai 2 dan saling berhadapan dengan kamar Dehen."
        prot "Senyap sekali kamar Dehen, pasti dia sudah tidur"
        show bg kamar with dissolve
        
        "Setelah Anda puas berkeliling di sekitar mess, Anda memutuskan kembali ke kamar Anda untuk tidur"
        stop music fadeout 0.5
        scene filler with dissolve
    jump scene4



label scene4:
    centered "{size=*2}Besok pagi{/size}"
    show text "{size=*2}Besok pagi{/size}" at truecenter
    hide text with dissolve
    pause 0.5
    play music "SCENE 4_ Bertemu Maura/Good Morning.mp3" fadein 1.0 volume 0.5 loop
    show bg kamar with dissolve
    
    "Anda terbangun sebelum matahari terbit, kali ini bukan karena suara ponsel yang mengganggu tidur Anda. Namun, Anda memang terbangun karena tubuh Anda sudah merasa tidur yang cukup sehingga badan Anda terasa bugar."
    prot "Selagi masih pagi pasti menyenangkan jogging di tepi pantai sambil menyaksikan sunrise"
    hide bg kamar with dissolve
    stop music fadeout 0.5
    play music "SCENE 4_ Bertemu Maura/Beach Mood Santai.mp3" fadein 0.5 volume 0.5 loop
    show bg pantai siang with dissolve
    
    "Sebelum joging Anda menyempatkan untuk mengecek ponsel, ternyata sinyal 6G telah selesai terpasang. Anda menyalakan strava sambil joging di tepi pantai"
    
    show maura neutral at centerC
    show maura at darken
    with dissolve
    "Sudah 1 jam anda joging, terlihat sebuah Helikopter Bell-412 menurunkan penumpang, seorang wanita dengan rambut panjang yang terurai"
    prot "Apakah itu Maura?"
    "Anda memutuskan untuk"
    
    menu bertemu_maura:
        "Anda memutuskan untuk"
        "menyambut kedatangannya sekaligus berkenalan":

            show maura at right, zoom05x, x_flip, lighten
            show dr_wisnu neutral at left

            "Ketika Anda menuju tempat berdirinya maura, Dr. wisnu sudah duluan tiba di sana. Mereka saling bercengkrama, ketika melihat kehadiran Anda, Dr. Wisnu memperkenalkan Anda pada Maura."
            
            prot "Hai Maura, salam kenal"
            mau "Hallo, salam kenal juga"
            
            hide dr_wisnu with dissolve
            hide maura with dissolve
            "Maura pamit menuju ke messnya untuk membongkar barang bawaannya di koper dan membersihkan diri. Karena kalian satu mess, Anda memutuskan berjalan bersama Maura menuju mess." 
            hide bg pantai siang with dissolve
            stop music fadeout 0.5
            
            play music "SCENE 4_ Bertemu Maura/Cozy Home Music.mp3" fadein 0.5 volume 0.5 loop
            show bg ruang tamu with dissolve
            "Berbeda dengan Anda dan Dehen, kamar Maura berada di lantai 1, kalian pun berpisah di dekat tangga menuju lantai 2." 
            "Sesampainya di depan kamar, Anda sempat melirik sebentar ke kamar Dehen"

            prot "Kenapa hening sekali? Sepertinya Deren belum bangun"
            hide bg ruang tamu with dissolve
            "Anda memutuskan untuk mandi dan sarapan. ketika sarapan Anda bertemu dengan Deren dan Maura yang sudah berada di meja makan. Ada asisten Dr. Wisnu lainnya juga di sana"
            
            show bg ruang tamu with dissolve
            "Saat sarapan Anda bertemu dengan Dehen dan Maura yang sudah berada di meja makan. Ada asisten Dr. Wisnu lainnya juga di sana"
            hide bg ruang tamu with dissolve

        "kembali ke mess tanpa mempedulikan kedatangan Maura":
            "Anda segera kembali ke mess untuk membersihkan badan setelah jogging."
            hide bg pantai siang with dissolve
            stop music fadeout 0.5
            play music "SCENE 4_ Bertemu Maura/Cozy Home Music,mp3" fadein 0.5 volume 0.5 loop
            show bg ruang tamu with dissolve
            

            "Ketika sampai di depan kamar, Anda sempat melirik sebentar ke kamar Dehen"
            prot "Kenapa hening sekali? Sepertinya Deren belum bangun"

            hide bg ruang tamu with dissolve
            "Anda memutuskan untuk mandi dan sarapan."
            
            show bg ruang tamu with dissolve
            "Setelah mandi, Anda pergi ke ruang tamu dan bertemu dengan Dehen dan Maura yang hendak makan. Juga ada banyak asisten Dr. Wisnu lainnya di sana." 
            
            show dehen neutral at centerC
            show dehen at darken
            with dissolve
            "Anda duduk di sebelah Dehen." 

            show dehen at lighten      
            deh "Bagaimana tidurmu? Nyenyak?"

            "Anda hanya mengangguk sambil menyendok nasi di meja makan"

            deh "kenalin nih, namanya Maura"
            show dehen at left, zoom05x
            with dissolve
            show maura neutral at right, x_flip
            with dissolve

            mau "Hallo salam kenal ya"
            prot "Hai, salam kenal juga"
            hide maura with dissolve
            hide dehen with dissolve

    
    jump scene5

label scene5:
    
    "Tak lama kemudian Dr. Wisnu meminta semua asistennya, termasuk Maura, untuk berkumpul."

    show dr_wisnu neutral at centerC
    with dissolve
    wis "Jarak 10 km ke utara dari mess ini, kalian akan menemukan lokasi proyek PLTN yang akan kita kerjakan."
    wis "Beberapa mesin baru datang besok." 
    wis "Jika kalian penasaran dan ingin menuju ke sana hari ini, temui saja anggota militer yang sedang berjaga di sekitar sini. kalian akan diantar menggunakan jeep." 

    "Setelah penjelasan dari Dr. Wisnu dan pembagian jobdesk masing-masing orang dalam tim ini selesai, Dr. Wisnu membubarkan semua orang di Aula." 
    hide dr_wisnu with dissolve

    show dehen neutral at left
    show maura neutral at right, x_flip
    with dissolve
    prot "Dehen, apa kau aka ikut melihat pabrik PLTN itu sekarang?"
    deh "tentu saja. bagaimana denganmu Maura?"
    mau "Aku akan ikut bersama kalian semua"
    hide dehen
    hide maura 
    hide bg
    with dissolve

    play music "SCENE 5_ Maura Kok Gitu_/Begin Your Journey.mp3" fadein 0.5 volume 0.5 loop
    show bg pantai siang with dissolve
    "Luas Area PLTN ini sekitar 2,5 juta meter persegi (2,5 km persegi), terdapat 5 reaktor yang akan berfungsi sebagai sumber energi panas yang dihasilkan dari reaksi fisi nuklir."
    "Reaksi panas ini akan menghasilkan uap dan akan menggerakan turbin sehingga mampu menghasilkan listrik." 
    "Reaktor juga dilengkapi dengan sistem pendingin utama untuk menyalurkan panas dari inti reaktor ke penukar panas untuk mencegah overheating." 

    prot "Semoga dengan adanya proyek ini seluruh kebutuhan listrik di Indonesia terpenuhi. Semoga tidak ada lagi pemadaman listrik untuk penghematan dan biaya listrik setelah ini akan menjadi murah"

    show maura neutral at centerC
    with dissolve
    mau "Sudah jelas itu. Kebutuhan listrik di Indonesia sekitar 775 GWh / hari. Adanya PLTS, PLTB, PLTA, dan PLTP yang dibangun mampu memenuhi 23 persen jumlah kebutuhan total listrik harian."
    mau "1 Generator yang kita miliki mampu menghasilkan 3500 MWh / jam, sehingga 1 generator mampu menghasilkan listrik sebesar 84 GWh / hari."
    mau "Kita memiliki 5 generator, jika ditotal listrik yang berhasil kita produksi sekitar 420 GWh / hari, jumlah ini akan jauh lebih banyak dibanding listrik yang kita butuhkan."

    prot "Wow pemikiranmu hebat sekali Maura"
    mau "Kau mau tau apa yang lebih hebat dari perhitunganku?"

    "Anda dan Dehen saling menatap, asisten laboratorium yang lain juga terlihat kebingungan dengan apa yang dikatakan Maura"
    show maura senang with Dissolve(1.5)
    mau "Dengan reaktor sebanyak ini, bukankah sayang jika Indonesia tidak memproduksi bom nuklir?"
    prot "Apa maksudmu?"

    "Maura hanya tersenyum dan kembali ke jeep tanpa menjawab pertanyaan terakhir Anda."
    hide maura with dissolve

    "Anggota militer yang menjadi supir jeep memanggil kalian semua untuk kembali ke jeep dan melakukan perjalanan pulang kembali ke mess."
    
    show dehen bingung at centerC
    with dissolve
    prot "Dehen, entah mengapa aku merasa ada hal yang mengganjal dari perkataan Maura tadi"
    deh "Sudahlah jangan ambil pusing, anggap saja dia hanya bercanda. Ayo kita kembali ke jeep"
    
    stop music fadeout 0.5
    hide dehen
    hide bg
    with dissolve
    centered "{size=*2}Pantai{/size}\nmalam"
    show text "{size=*2}Pantai{/size}\nmalam" at truecenter
    hide text with dissolve
    pause 0.5
    play music "SCENE 5_ Maura Kok Gitu_/Beach Music Night.mp3" fadein 1.0 volume 0.5 loop
    show bg pantai malam with dissolve

    "Anda pun kembali ke mess dengan menggunakan jeep yang sama seperti saat berangkat."

    "Semua orang turun dari jeep ketika jeep berhenti tepat di halaman mess." 

    "Anda turun dari jeep setelah Maura, dilanjut Dehen dan asisten laboratorium lainnya."
    "Maura segera masuk ke mess tanpa memperdulikan yang lainnya."
    "Anda melamun memperhatikan jejak ban dari mobil jeep dan suara Dr. Wisnu menyadarkan lamunan Anda"
    
    show dr_wisnu neutral at centerC
    with dissolve
    wis "Bagimana? Sudah melihat lokasi PLTN kita? Sangat menawan bukan?"
    "Anda hanya mengangguk"
    wis "Ada yang sedang kamu pikirkan?"


label scene6:
    #scene 6
    menu kamu_pikirkan:
        "Tidak ada, aku hanya merasa tidak enak badan":
            stop music fadeout 0.3
            jump scene6a_alam_mimpi

        "Saat sedang berada di lokasi, Maura sempat menyinggung kegunaan radiator untuk membuat bom nuklir. Apa maksudnya itu?": #scene 6 maksud maura
            stop music fadeout 0.3
            jump scene6_maksud_maura
            

label scene6a_alam_mimpi:

    play music "SCENE 6_ Alam Mimpi/Normal agak sedih.mp3" fadein 0.5 volume 0.6 loop
    wis "Baiklah, beristirahatlah, besok mesin-mesin itu akan disetting untuk penelitian kita dalam mendirikan PLTN"
    prot "Baik pak, aku izin masuk dulu"

    hide dr_wisnu with dissolve
    hide bg with dissolve
    scene filler
    show bg ruang tamu with dissolve

    "Anda pun masuk ke mess dan menuju ke kamar. Lagi-lagi Anda melirik sebentar ke kamar Dehen, kali ini pintunya tidak tertutup. terdengar suara (You destroyed a turret)."

    prot "(Umur berapa sih dia, masih saja suka mengisi waktu kosong dengan bermain games)"

    hide bg with dissolve
    show bg kamar with dissolve

    "Anda pun masuk kamar mess dan mandi."
    "Setelah mandi Anda dan memakai pakaian Anda rebahan di ranjang."
    "Anda membuka instagram, nampak berbagai instastory teman-teman Anda yang beragam." 
    "Ada yang bermain bersama hewan peliharaan, jalan-jalan bersama pasangan, liburan dengan keluarga, olahraga, dan lainnya."

    "Anda membuka galeri, nampak foto ketika matahari sunrise yang Anda ambil saat jogging tadi pagi, ada juga berbagai foto keindahan pulau Gelasa."
    "Ketika Anda ingin membuat story di instagram, muncul foto-foto lokasi PLTN dan daerah yang sudah diploting untuk mesin-mesin tertentu."
    "Anda pun mengurungkan niat untuk mengupload foto yang Anda ambil hari ini."
    
    prot "Seandainya pulau cantik ini tidak terisolasi……"
    prot "Seandainya proyek ini bukanlah rahasia negara, pasti aku akan mengunggah semuanya……"

    show bg kamar at darken:
        blur 10
    with Dissolve (2)
    hide bg kamar 
    with dissolve

    stop music fadeout 0.5
    hide dehen
    hide bg
    with dissolve
    centered "{size=*2}Pantai{/size}\n???"
    show text "{size=*2}Pantai{/size}\n???" at truecenter
    hide text with dissolve
    pause 0.5
    play music "SCENE 6_ Alam Mimpi/Normal.mp3" fadein 1.0 volume 0.5 loop
    show bg pantai siang with dissolve
    "Andapun keluar dari mess untuk melihat kondisi sekitar. nampak para anggota militer sedang berolahraga di sore hari. Anda yang ramah tersenyum kepada mereka ketika beberapa dari. mereka sedang lari melewati Anda sambil menyanyikan yel-yel."
    "Mereka memang tidak membalas senyum Anda, tetapi Anda tahu sorot mata mereka memancarkan senyuman."

    prot "Tak heran memang jika mereka terkesan kaku, memang apa yang terjadi jika mereka berhenti menyanyikan yel-yel sebentar. Dan membalas senyumku?"

    "Anda berjalan menuju pantai, arah mata anda tertuju pada penyu sisik (Eretmochelys imbricata) yang sedang menggali pasir. Setelah terbentuk lubang penyu itu bertelur." 
    "Mungkin ada sekitar 150 butir telur yang penyu itu hasilkan. Anda terus mengamati dari jauh."
    "Selesai bertelur, penyu itu kembali berenang ke laut lagi. Anda menyadari cahaya matahari mulai redup," 
    "Anda menyaksikan sunset yang amat indah di pulau gelasa, ditemani hembusan angin dan deburan ombak. Begitu matahari tenggelam Anda kembali ke mess."

    show bg ruang tamu with Dissolve(1.0)
    "Orang-orang bagian dapur sudah menyiapkan makanan untuk kalian makan malam. Anda pun duduk di kursi meja makan untuk bersiap makan." 
    "terdengar langkah beberapa orang turun dari tangga lantai 2, tentu saja itu pasti Dehen dan asisten lainnya. Selang beberapa saat, pintu kamar Maura terbuka, kalian semua berkumpul di meja makan untuk makan malam."

    "Tidak ada percakapan yang berarti malam itu, hanya candaan ringan yang menemani kalian semua ketika makan malam berlangsung." 
    "walaupun Anda masih ragu dengan pikiran anda tentang Maura, Anda berusaha menepisnya, Anda akan bekerja bersama Maura beberapa bulan kedepan, tidak nyaman tentunya jika ada perselisihan sekecil apapun itu."

    show bg kamar with Dissolve(1.0)
    "Selesai makan malam Anda kembali ke kamar Anda, segera Anda menyalakan komputer. Anda sempat membawa flashdisk yang berisi file penelitian Anda agar bisa menjadi pemenang nobel." 
    "Meskipun Anda bisa menyimpan semua file itu di drive dan dihubungkan dengan akun Anda agar lebih praktis, tapi Anda takut ada orang yang  meretas komputer disini, walaupun dengan semua kamaan yang ketat ini, kecil kemungkinan hal itu terjadi."

    prot "Sepertinya bukan di tahun ini, tak mungkin aku menyelesaikan penelitianku bersamaan dengan pengerjaan proyek ini."
    prot "Aku akan tetap mengumpulkan lebih banyak data agar saat proyek PLTN ini selesai aku bisa melanjutkan penelitianku sendiri."
    
    stop music fadeout 0.5
    play sound "SCENE 6_ Alam Mimpi/Big Explosion Sound Effect.mp3" volume 0.8
    hide bg with Dissolve(0.2)
    show bg awan jamur
    with hpunch
    "{i} DUARRRR {/i}"
    play music "SCENE 6_ Alam Mimpi/Lab Music.mp3" fadein 0.1 loop volume 0.6



    "terlihat kilatan merah yang disusul dengan suara yang amat keras dari posisi Anda berdiri. "
    "Tubuh Anda bergetar, Anda melihat ke sekeliling, terlihat Maura dan Dr. Wisnu tersenyum puas." 
    show bg laboratorium with dissolve
    "Anda seketika berada di dalam mercusuar."
    "Sekilas mercusuar ini terlihat biasa saja, ternyata di dalamnya terdapat ruangan dengan berbagai alat canggih." 
    "Suara, kilatan dan kilatan tadi berasal dari simulator yang Maura ciptakan. Dr. Wisnu menepuk bahu Anda"

    show dr_wisnu senang at left
    show maura senang at right
    show maura at x_flip
    with dissolve
    wis "Jika bukan karena penelitian tentang nuklir kita tak mungkin bisa melakukan ini"
    mau "Simulator ini aku design semirip mungkin dengan kemungkinan kondisi yang kan terjadi nanti." 
    mau "Walaupun kita hanya menyerang satu titik di kota itu, namun efek radiasinya akan menyebar di seluruh negara, bahkan ke negara sebelah. Mustahil jika negara lain masih berani dengan Indonesia. Negara ini akan menjadi negara adidaya."
    show dr_wisnu at darken
    show maura at darken
    "Maura dan Dr. Wisnu tertawa membayangkan semua rencana mereka berjalan dengan mulus. sedangkan Anda hanya diam, mencerna semua keadaan yang sedang terjadi."

    prot "Dimana Dehen?"
    show maura marah at lighten
    mau "Beraninya kau menyebut nama pengkhianat itu?"

    "Anda semakin bingung"
    prot "pengkhianat? Apa maksudnya? Apa yang dia maksud pengkhianat itu Dehen? Mana mungkin Dehen berkhianat? "
    show dr_wisnu neutral at lighten
    wis "Sudahlah Maura, butuh waktu untuk dia menerima keputusan Dehen"
    
    scene filler with dissolve

    "Anda pun keluar dari ruangan itu, ada terlalu banyak anak tangga yang harus Anda turuni. Setelah 25 menit Anda menuruni anak tangga, terdapat pintu besi besar."

    "Dari semua pintu yang Anda lihat sebelumnya di mercusuar ini, pintu ini memiliki ID Card Reader dan seorang anggota militer di depannya." 
    "Anggota militer ini segera menggesek kartu yang ia bawa dan memberikannya kepada Anda sebelum ia mendorong Anda masuk ke ruangan dibaliknya."
    "Pintu seketika tertutup rapat dan Anda melihat Dehen di dalam ruangan itu."
    
    "..."
    show bg ruang cahaya minim with Dissolve(0.1)
    show dehen neutral at centerC, darken
    "..!"
    show dehen bingung at centerC, lighten
    prot "Dehen? apa yang terjadi"
    deh "Ini semua salahmu"
    prot "Apa? Apa semua ini Dehen, aku tak mengerti apapun?"
    deh "Jika saja kau tak mudah terbujuk dengan tawaran Maura dan Dr. Wisnu, bom itu tidak akan meluncur besok"
    prot "Bom apa Dehen?"
    deh "Aku tahu kau sangat terobsesi dengan nuklir, tapi apa kau tidak memikirkan nyawa orang-orang yang tak berdosa? Anak-anak bahkan lansia?" 
    show dehen marah
    deh "{b}KAU ADALAH PENJAHAT YANG SEBENARNYA{/b}"
    scene filler with Dissolve (0.2)
    with vpunch
    show bg laboratorium with Dissolve(0.2)

    "Anda terbagun dengan keringat bercucuran, terlihat Dehen duduk disamping tubuh Anda." 
    show dehen senang at centerC
    with dissolve
    deh "Sudah 9x kau selalu terbangun dengan kondisi seperti ini. Bahkan reaktor belum menyala tetapi sepertinya otakmu sudah terpapar radiasi nuklir"

    show dehen at darken
    "Selama 9 hari terakhir Anda selalu bermimpi hal yang sama, tapi entah mengapa Anda enggan menceritakannya pada siapapun."
    "Proyek PLTN ini sudah berjalan selama 8 bulan. Kalian masih berkutat untuk menyelaraskan semua fungsi di sistem yang kalian rancang."
    show dehen neutral at lighten 
    deh "Makan dulu sana, aku lanjut kerja dulu"
    hide dehen with dissolve
    "Setelah makan, Anda melihat Dr. Wisnu duduk di kursinya dan bersiap menginterupsi kegiatan hari ini."
    "Sepertinya beliau tidak tidur lagi hari ini, terlihat jelas dari kantung matanya yang semakin membengkak dan menghitam."

    "Hari ini Anda bekerja di bagian wet lab, sedangkan Maura, Dr. Wisnu, dan Dehen bekerja di dry lab."
    "Setelah bekerja beberapa jam, Anda beristirahat untuk makan siang, Maura, Dr. Wisnu, dan Dehen belum memunculkan batang hidungnya"

    prot  "Sepertinya mereka sangat sibuk hari ini"

    "Anda akhirnya memutuskan untuk kembali ke mess."

    scene filler with Dissolve(2)
    pause 1.0
    show bg laboratorium with dissolve

    "Pagi harinya saat Anda memasuki lab, terlihat Maura, Dr. Wisnu, dan Dehen sudah duduk di kursinya."
    "Anda yakin mereka bekerja sangat keras semalam, sehingga Anda terdorong untuk meningkatkan efisiensi bahan bakar nuklir hari ini."
    "Saking fokusnya Anda dalam bekerja, Anda melewatkan makan siang bersama asisten wet lab lainnya, sehingga Anda merasa lemas di sore hari."
    "Saat malam tiba.."
    show bg ruang tamu with dissolve
    stop music fadeout 0.5
    pause 0.2
    play music "SCENE 6_ Alam Mimpi/Misteri.mp3" fadein 0.3 loop volume 0.6
    show dehen neutral at centerC
    with dissolve 
    
    deh "Bagaimana pekerjaanmu hari ini?"
    prot "Aku belum menemukan perbandingan yang pas antara plutonium dengan thorium dari pagi tadi"
    deh "Pantas, aku tidak melihatmu bersama asisten lain ketika makan siang tadi"
    prot "Harus aku akui, meskipun proyek ini sulit tetapi aku sangat menikmatinya"
    deh "Sebab kau sangat terobsesi dengan nuklir"
    prot "Bagaimana dengan dry lab kalian?"
    deh "Kau lihat saja Maura, ia tak kuat menahan kantuk walaupun kondisi jalan yang dilewati jeep ini membuat tubuhnya terguncang dan hampir jatuh"

    "kalian berdua tertawa melihat Maura"

    deh "Aku tidur di kamarmu yaa, sekalian jagain kalo kamu mimpi buruk lagi"

    "Anda mengerti dengan ucapan Dehen, pasti ada hal penting yang ingin ia katakan tetapi hanya berdua dengan Anda. Anda mengangguk sambil tersenyum."
    hide dehen with dissolve
    "Selesai makan malam, Dehen dan Anda menuju kamar Anda."
    show bg kamar with dissolve
    extend "Anda mengunci pintu kamar, sedangkan Dehen menutup jendela, memastikan obrolan mereka tidak terdengar hingga keluar kamar."
    show dehen neutral at centerC
    prot "Apa yang mau kau katakan sobat?" 
    deh "Dry lab kami dari kemarin tidak menemukan solusi. Bahkan Maura yang menguasai berbagai teorema matematika dan fisika tak kunjung berhasil menemukan perhitungan yang sesuai."
    prot "...."
    deh "tapi aku ingat, kau juga sedang mengembangkan penelitian mengenai nuklir kan? Penelitianmu sudah berjalan dari beberapa tahun yang lalu"
    prot "...."
    deh "Apa kau tidak pernah melakukan perhitungan? kau pasti sudah melakukan perhitungan bukan?"
    prot "...."
    deh "Yaa aku tahu kau memang ingin menjadi peraih nobel, tapi bukankah penelitianmu banyak? Apakah akan berdampak besar jika kau memberi tahu sedikit hasil perhitunganmu demi kelancaran proyek ini"
    prot "...."
    deh "Kau juga berkeinginan proyek ini sukses bukan? Kau ingin kebutuhan listrik semua rakyat Indonesia terpenuhi kan?"
    prot "....."
    deh "Maaf aku terlalu berlebihan, kau berhak mematenkan semua penelitianmu itu"
    show dehen at darken
    "Dehen berbaring di tempat tidur anda dan menarik selimut."
    prot "Akan aku pertimbangkan apa yang kau ucapkan malam ini Dehen"
    show dehen at lighten
    "Anda berbaring di sebelah Dehen. Sambil memunggungi Anda,"
    deh "Dengar, aku akan mendukungmu, aku sengaja tidak memberithu Dr. Wisnu tentang apa yang kau kerjakan dan tidak membahas ini di jeep karena aku sangat menghormatimu sebagai teman." 
    deh "Berjanjilah keputusan apapun yang kau ambil akan bermanfaat untuk Indonesia"
    prot "Ya, aku berjanji"
    # ini ujung dari scene 6 yang mimpi lanjut ke label pilihan
    jump yang_anda_lakukan_sekarang



label scene6_maksud_maura:
    play music "SCENE 6_ Maksud Maura/Curious.mp3" loop volume 0.6 fadein 0.3
    wis "Ah itu hanya lelucon biasa Maura. Tidak usah dihiraukan, biarkan saja."
    prot "Namun terlihat dari desain radiator, sepertinya Maura mengatakan sejujurnya. Bagaimana itu pak?"
    
    wis "Sudahlah, Mungkin kamu salah dengar perkataan Maura. Sudahkah kamu beristirahat? Mungkin kamu bisa beristirahat terlebih dahulu."
    prot "Tidak perlu pak."

    wis "Baiklah, selalu jaga kesehatan, di pulau ini tidak ada rumah sakit jika ada apa apa."
    hide dr_wisnu with dissolve

    "Dr. Wisnu tersenyum lalu tertawa, lalu berjalan membelakangi Anda secara perlahan. Percakapan tersebut meninggalkan rasa tidak enak didalam pikiran Anda." 
    "Sepertinya, kedua belah pihak; Dr. Wisnu, maupun Maura sedang menyembunyikan sesuatu yang besar dan penting."
    show dr_wisnu neutral at centerC
    "Dr Wisnu seketika berputar arah sebelum menjauh terlalu jauh, dan mencoba untuk mengatakan sesuatu."

    wis "Oh, ngomong-ngomong. Besok kamu akan ditempatkan di wet lab, sedangkan Dehen, aku dan Maura akan bekerja di dry lab." 
    wis "Dehen sempat menitipkan pesan kepadaku dia dapat bekerja di wet lab maupun dry lab sehingga kamu bebas memilih bisa kerja dimana. Gimana menurutmu?"

    menu Anda_memilih_bekerja_di:
        "Wet Lab":
            show dr_wisnu senang with dissolve 
            wis "Baiklah akan aku koordinasikan kepada Dehen, kamu lebih memilih bekerja di wet lab."
            jump scene_transisi_wet_lab
        "Dry Lab":
            show dr_wisnu senang with dissolve
            wis "Baiklah akan aku koordinasikan kepada Dehen, kamu lebih memilih bekerja di Dry lab."
            jump scene7_maura_drwisnu
            
label scene_transisisi_wet_lab:
    scene filler with dissolve
    stop music fadeout 0.5
    show bg ruang tamu with dissolve
    play music "SCENE TRANSISI/Cozy Home Music.mp3" loop volume 0.6 fadein 0.5
    "Setelah mengkonfirmasi ke Dr. Wisnu Anda kembali ke kamar Anda untuk beristirahat."
    "Anda masuk ke mess dan menuju ke kamar. Lagi-lagi Anda melirik sebentar ke kamar Dehen. Kali ini pintunya tidak tertutup dan terdengar suara, “You destroyed a turret”."

    prot "Umur berapa sih dia, masih saja suka mengisi waktu kosong dengan bermain game"
    show kamar with dissolve
    "Anda pun masuk kamar dan mandi. Setelah mandi, Anda memakai pakaian dan merebahkan diri. Anda membuka Instagram dan melihat berbagai Instastory teman-teman Anda." 
    "Ada yang bermain dengan hewan peliharaannya, jalan-jalan bersama pasangan, liburan dengan keluarga, dan lainnya."

    "Anda membuka galeri, tampak foto matahari pagi saat jogging tadi pagi dan foto keindahan Pulau Gelasa." 
    "Ketika Anda ingin membuat story di Instagram, muncul foto-foto lokasi PLTN dan denah pemetaan mesin-mesin. Anda pun mengurungkan niat untuk mengunggah story itu."

    prot "Seandainya pulau cantik ini tidak terisolasi… "
    prot "Seandainya proyek ini bukanlah rahasia negara, pasti aku akan mengunggah semuanya…"

    "Di tengah keheningan itu, Anda teringat akan penelitian Nobel Anda. Anda mengambil flashdisk yang berisi file penelitian Nobel Anda." 
    "Meskipun bisa menyimpan semua file itu di drive, Anda takut ada yang meretas komputer disini. Walaupun dengan semua keamanan yang ketat ini, kecil kemungkinan hal itu terjadi."

    prot "Sepertinya bukan di tahun ini, tak mungkin aku menyelesaikan penelitianku bersamaan dengan pengerjaan proyek ini." 
    prot "Aku akan tetap mengumpulkan lebih banyak data agar saat proyek PLTN ini selesai aku bisa melanjutkan penelitianku sendiri."

    scene filler with Dissolve(2)
    stop music fadeout 1

    show bg laboratiorium
    play music "SCENE TRANSISI/Lab Music.mp3" volume 0.6 loop fadein 0.5
    "Pagi harinya, ketika Anda memasuki lab pulau Gelasa, terlihat Dr. Wisnu, Dehen, dan Maura sudah duduk di kursinya." 
    "Anda yakin mereka bekerja sangat keras semalam. Hari ini Anda berfokus untuk meningkatkan efisiensi bahan bakar nuklir."

    "Saking fokusnya Anda dalam bekerja, Anda melewatkan makan siang bersama asisten wet lab lainnya, sehingga Anda merasa lemas di sore hari."
    scene filler with dissolve
    "Saat malam tiba.."
    stop music fadeout 0.5
    show bg ruang tamu
    play music "SCENE TRANSISI/Cosy Home Music.mp3" volume 0.6 loop fadein 0.5
    show dehen at centerC
    with dissolve
    deh "Bagaimana pekerjaanmu hari ini?"
    prot "Aku belum menemukan perbandingan yang pas antara Plutonium dan Thorium sejak pagi tadi."
    deh "Pantas, aku tidak melihatmu bersama asisten lain ketika makan siang tadi."
    prot "Harus aku akui. Meskipun proyek ini sulit, sampai saat ini aku sangat menikmatinya."
    show dehen bingung with dissolve
    deh "Haih, itu hanya karena kau sangat terobsesi dengan nuklir."
    prot "Haha. Bagaimana dengan dry lab kalian?"
    show dehen senang
    deh "Kau lihat saja Maura. Dia sampai bisa tertidur di sofa."

    show dehen at bounce(2, 0.05)
    "Kalian berdua tertawa melihat Maura. Namun, Anda jadi teringat tentang percakapan Anda dengan Dr. Wisnu kemarin. Anda memberitahu Dehen jika ada sesuatu yang harus dibicarakan tentang percakapan kemarin."


    prot "Dehen."
    show dehen senang
    deh "Ada apa?"
    prot "Ada sesuatu yang ingin kuucapkan, tapi disini terlalu ramai. Apakah kamu bisa ke kamarku nanti?"
    show dehen neutral
    deh "Baiklah."

    hide dehen with dissolve

    "Selesai makan malam, Dehen dan Anda menuju kamar Anda."
    "Anda mengunci pintu kamar sembari Dehen menutup jendela, memastikan obrolan kalian tidak terdengar siapapun."

    show dehen neutral at centerC
    with dissolve
    deh "Baiklah ada apa yang harus dibicarakan?"

    "Anda menceritakan omongan Maura dan tingkah laku Dr. Wisnu."

    deh "Hm, mengerti. Namun, aku tidak terima jika nantinya arah riset akan berujung ke pembuatan bom nuklir."
    prot "Aku sependapat denganmu."
    deh "Baiklah. Mari lupakan hal tersebut sejenak, ngomong-ngomong aku juga harus memberitahumu sesuatu juga. Di dry lab, kami dari kemarin tidak menemukan solusi." 
    deh "Bahkan Maura yang menguasai berbagai teorema matematika dan fisika tak kunjung berhasil menemukan perhitungan yang sesuai."
    prot "…"
    deh "Tapi aku teringat. Kau juga sedang mengembangkan penelitian mengenai nuklir kan?"
    deh "Penelitianmu sudah berjalan dari beberapa tahun yang lalu… Kau pasti sudah melakukan perhitungan bukan?"
    prot "…"
    deh "Aku tahu kau memang ingin menjadi peraih Nobel, tapi apakah akan berdampak besar jika kau memberi tahu sedikit hasil perhitunganmu demi kelancaran proyek ini?" 
    deh "Kau juga berkeinginan proyek ini sukses bukan? Kau ingin kebutuhan listrik semua rakyat Indonesia terpenuhi kan?"
    prot "…"
    deh "Maaf… Aku terlalu berlebihan. Kau berhak mematenkan semua penelitianmu itu."

    "Dehen menunggu jawaban Anda dengan sabar. Setelah menghela nafas panjang, Anda menjawab."

    prot "Akan aku pertimbangkan apa yang kau ucapkan malam ini Dehen."

    "Dehen mengangguk tersenyum dan keluar dari kamar."
    "Saat di pintu kamar Anda, Dehen mengatakan…"

    deh "Dengar, aku akan mendukungmu, aku sengaja tidak memberitahu Dr. Wisnu tentang apa yang kau kerjakan dan tidak membahas ini di Jeep karena aku sangat menghormatimu sebagai teman." 
    deh "Berjanjilah keputusan apapun yang kau ambil akan bermanfaat untuk Indonesia."
    prot "Ya, aku berjanji."
    jump yang_anda_lakukan_sekarang
            


label yang_anda_lakukan_sekarang:
    scene filler with Dissolve(2)
    centered "{size=*2}Pabrik PLTN{/size}"
    show text "{size=*2}Pabrik PLTN{/size}" at truecenter
    hide text with dissolve
    pause 0.5
    show bg pabrik pltn with dissolve

    "Esok paginya, setelah sampai di lokasi proyek PLTN Anda"
    menu ending:
        "Mempertahankan apa yang menjadi hak Anda":
            stop music fadeout 2
            scene filler with Dissolve(2)
            centered "{size=*2}Pabrik PLTN{/size}"
            show text "{size=*2}Pabrik PLTN{/size}" at truecenter
            hide text with dissolve
            pause 0.5
            play music "[END] SCENE 7_ PLTN Berhasil!/Achievement.mp3" fadein 0.3 loop volume 0.6
            show bg pabrik pltn with dissolve 
            "Setelah 2 minggu bekerja Anda berhasil menemukan kombinasi yang tepat dari Plutonium (Pu) dan Thorium (Th). Sekarang Anda berfokus pada MOX (Mixed Oxide Fuel). Kali ini Anda bekerja langsung bersama Dr. Wisnu."
            "Perlu waktu sekitar satu bulan untuk mendapat komposisi yang tepat. Dehen, Maura, dan asisten lain berkutat mati matian untuk mencari perhitungan yang tepat."

            "Di dalam hati nurani, Anda merasa apa yang Anda lakukan sangat egois. Sikap Anda seperti bertentangan dengan sila ke-2 dari Pancasila, yakni “Kemanusiaan yang Adil dan Beradab”."
            "Anda mengetahui secara pasti perhitungan yang sedang mereka cari, dan membiarkan mereka dalam kebingungan dan kelelahan."
            
            "Namun, disisi lain Anda teringat UUD 1945 Pasal 28C Ayat 2, yakni “Setiap orang berhak untuk memajukan dirinya dalam memperjuangkan haknya secara kolektif untuk membangun masyarakat, bangsa, dan negara”."
            "Anda berpikir jika Anda telah menjadi peraih Nobel, ilmu yang Anda miliki juga akan bermanfaat bagi kemajuan teknologi Indonesia."

            "Kali ini Anda bekerja sama dengan Maura di bagian wet lab. Sedangkan Dr. Wisnu bekerjasama dengan Dehen di dry lab."
            "Anda mencari komposisi serta metode yang tepat untuk memperlambat neutron, memungkinkan reaksi berantai yang stabil dalam reaktor nuklir menggunakan grafit."

            "Tak terasa sudah 5 bulan Anda bekerja satu lab bersama Maura. Anda semakin dekat dengannya, kalian saling bertukar cerita tentang latar belakang masing-masing."
            #lanjut ke ending
            jump good_ending

        "Menemui Dr. Wisnu untuk membicarakan penelitian Anda":
            prot "Dr. Wisnu, bolehkah hari ini aku bekerja secara dry lab?"
            wis "Apa kau sedang mengalami masalah?"
            prot "Tidak, aku ingin rehat sejenak mencium bau bahan-bahan kimia itu"
            wis "Baiklah, hari ini kamu, Maura, dan aku akan bekerja secara dry lab, dehen dan asisten lain akan bekerja secara wet lab"
            jump scene7_dr_wisnu




label good_ending: #Ini ending pltn scene 7

    show maura senang at centerC
    with dissolve
    mau "Kau adalah orang yang sangat jenius dan baik, apa mimpimu?"
    menu ending12:
        "Aku ingin membangun Indonesia melalui kemampuan yang aku punya, Ilmu Pengetahuan dan Teknologi":
            mau "Kupikir kau ingin menjadi peraih nobel"
            prot "(Kok dia ingat?)"
            mau "Setelah 5 bulan bekerja di lab yang sama, firasatku mengatakan kau bisa menjadi peraih nobel"
            "Anda merasa senang mendengar kata-kata itu dan menjadi lebih bersemangat dalam menyelesaikan proyek ini."
            scene filler with Dissolve(2)
            show bg good ending
            
            "Setelah hampir 2 tahun bekerja, akhirnya PLTN pertama yang dimiliki Bangsa Indonesia beroperasi, selama percobaan 3 minggu belum ada keluhan apapun tentang PLTN ini. Semua kebutuhan listrik rakyat Indonesia dari  Sabang hingga Merauke terpenuhi."
            "Harga listrik di Indonesia menjadi sangat murah. Indonesia dijadikan contoh negara di Asia tenggara yang menggunakan PLTN sebagai sumber utama dalam memenuhi listrik negara."
            "Rencananya akan ada proyek PLTN tambahan agar semua tenaga listrik hanya bersumber dari nuklir saja, tidak perlu mengAndalkan batubara yang kurang ramah lingkungan."

        "Aku ingin menjadi peraih nobel":
            mau "Yah, firasatku juga mengatakan hal yang sama, 5 bulan kita berada di lab yang sama, bertemu setiap hari, berdiskusi banyak hal untuk memecahkan masalah. Menurutku kau sangat pantas menjadi peraih nobel"
            prot "terimakasih Maura"
            prot "Apa mimpimu?"
            mau "Inang menyuruh aku untuk segera menikah, jadi setelah proyek ini selesai aku akan pulang ke Simalungun untuk menikah"
            prot "pfft"
            mau "Apa barusan kau tertawa?"
            prot "Maaf, tak pernah terbesit di otakku, orang ambisius sepertimu bermimpi untuk menikah?"
            mau "Semua orang waras ingin menikah, memangnya kau ga mau? Lagian aku mencari calon suami yang sepemikiran denganku, sehingga aku bisa melanjutkan berbagai riset yang ingin aku lakukan kedepannya"
            prot "Maaf aku hanya bercanda, sepertinya aku juga harus memikirkan waktu yang tepat untuk menikah."

            scene filler with Dissolve(2)
            show bg good ending

            "Setelah hampir 2 tahun bekerja, akhirnya PLTN pertama yang dimiliki Bangsa Indonesia beroperasi."
            "selama percobaan 3 minggu belum ada keluhan apapun tentang PLTN ini."
            "Semua kebutuhan listrik rakyat Indonesia dari sabang hingga merauke terpenuhi."
            "Harga listrik di Indonesia menjadi sangat murah."
            "Indonesia dijadikan contoh negara di Asia tenggara yang menggunakan PLTN sebagai sumber utama dalam memenuhi listrik negara."

            "Rencananya akan ada proyek PLTN tambahan agar semua tenaga listrik hanya bersumber dari nuklir saja, tidak perlu mengandalkan batubara yang kurang ramah lingkungan."
    
    scene filler with Dissolve(2)
    centered "{size=*2}Pabrik PLTN{/size}\n\"Kekuatan atom berada di tangan garuda, Majulah terus Indonesia\""
    show text "{size=*2}Good End{/size}\n" at truecenter
    hide text with dissolve
    pause 0.5
    stop music fadeout 5
    pause 6
    $ persistent.main_menu_bg = "images/bg/bg good ending.png"
    return

label scene7_dr_wisnu: 
    "Anda bergegas mencari Dr. Wisnu untuk memberitahukannya soal penelitian yang Anda sedang lakukan."


    "Dengan matanya yang tajam tertuju pada laptopnya, Dr. Wisnu seolah hilang dalam pekerjaannya. Kedatangan Anda membuatnya tersentak dan seketika berfokus pada Anda."
    wis "Sangat bersemangat ya. Ada apa dengan kamu hari ini?"
    prot "Dr. Wisnu, apakah saya dapat bekerja di dry lab hari ini?"
    wis "Hm? Apa kau sedang mengalami masalah?"
    prot "Tidak pak. Saya hanya ingin rehat sejenak dari bau bahan-bahan kimia itu."
    wis "Oh baiklah. Hari ini kamu, Maura, dan aku akan bekerja di dry lab. Dehen dan asisten lain akan bekerja secara wet lab."

    "Anda pun memasuki ruang wet lab. Dr. Wisnu kembali duduk di depan laptop sambil mencari data, dan Maura mendekati Anda. Ia mulai menjelaskan hasil perhitungannya dengan Dehen."

    mau "Ini perhitunganku kemarin, bagian ini aku hitung menggunakan teori fisi nuklir, yang ini difusi neutron, sedangkan ini untuk keamanan reaktor nuklir."
    prot "(diam mendengarkan)"
    mau "Aku merasa perhitungan bersama Dehen sudah tepat, namun entah mengapa galat yang dihasilkan masih sangat tinggi. ini lah yang menyebabkan proses selanjutnya tidak bisa dikerjakan"

    "Anda mengecek perhitungan Maura dengan seksama"

    prot "Kau melupakan reaksi berantai, 235U + 92Kr + 141Ba + 3n + Energi, dengan energi dalam bentuk panas dan radiasi." 

    "Maura mengoreksi kembali perhitungannya"

    mau "kau benar, aku akan menghitungnya kembali"

    "Beberapa saat kemudian"

    mau "Masih ada hal yang kurang, aku tidak tahu apalagi yang salah"

    "Maura memberikan data hasil hitungnya, Anda mengamati semua perhitungan Maura. Dr. Wisnu menghampiri kalian dan melihat hasil perhitungan Maura"

    prot "Kau belum memasukkan persamaan energi tahap akhir. Masukkan E = m.c2 dengan m merupakan selisih perbedaan selisih massa sebelum direaksikan dan setelah direaksikan."

    "Maura kembali menghitung. setelah 15 menit Maura berteriak kegirangan. Ia memegang tangan anda"

    mau "Kau sangat jenius, kau benar-benar jenius"
    prot "(tersenyum seneng krn dipuji)"

    wis "Tunggu"
    wis "Coba lihat bagian ini. Reaksi nuklir harus dijaga pada kondisi kritis (k = 1), sehingga neutron selalu stabil dan reaksi berantai berlangsung perlahan."

    "Anda dan Maura mengangguk"

    wis "Apa yang terjadi jika kita mempercepat reaksi nuklir ini dalam kondisi superkritis (k > 1) ?"

    "Perasaan Anda mulai tidak enak, sedangkan Maura hanya diam, tertegun mendengar ucapan Dr. Wisnu"

    prot "Dr. Wisnu, Anda tidak mencoba menciptakan.."
    wis "BOM NUKLIR, tepat sekali, kau memang sangat jenius"

    "Anda tidak percaya kata-kata yang dilontarkan Dr. Wisnu. Anda tidak pernah menyangka perhitungan Anda akan membuat ini semua terjadi."
    
    wis "Kondisi yang superkritis akan menghasilkan reaksi berantai tak terkendali yang sangat cepat, kita tidak perlu merancang sistem pengendalian sehingga reaksi bisa terjadi secara eksponensial"
    mau "Dengan begitu Indonesia akan menjadi negara adidaya"
    wis "tepat sekali Maura, Mari kita berkumpul dan membahas ini bersama asisten lainnya."

    "Setelah kejadian itu, Anda dengan cepat lari keluar laboratorium dan menenangkan diri."

    prot "Semuanya terjadi sangat cepat, apa yang dikatakan Dr. Wisnu sangat mengejutkan"

    "Anda akhirnya berpikir bahwa…"


    #masuk ke menu ini ending di scene 8 
    menu ending23:

        #ini ending yang bad
        "Bom nuklir akan membuat semua negara, terutama di wilayah asia tenggara akan tunduk":
            show Laboratorium
            "Saat Anda kembali masuk, sudah waktu untuk istirahat siang. Anda lihat Dehen mendatangi Anda."

            deh "Hai sobat, apakah kau menyesal masuk ke dry lab hari ini?" 

            "Anda hanya diam mendengar ejekan Dehen"

            mau "Tak ku sangka kau sangat jenius, kedepannya kita harus banyak berdiskusi."

            "Dehen berbisik kepada Anda"
            deh "Kau?"
            prot "Iya aku melakukannya"

            "Dehen tersenyum"

            "Setelah semua orang selesai makan, Dr. Wisnu meminta semua orang untuk masuk ke ruang dry lab. Setibanya di ruang dry lab, dr. Wisnu menjelaskan hal yang kalian alami, termasuk membahas ide pembuatan bom nuklir."

            deh "Apa kau gila Dr. Wisnu? Rasa sakitmu dipermalukan saat Manhattan Project Meetings beberapa tahun yang lalu harus kau lupakan"
            wis "Tidak, aku tidak akan pernah melupakan kejadian itu, kejadian saat Mr. Karan mempermalukanku di depan semua orang."
            deh "Tapi dia sudah minta maaf kepadamu"
            wis "Diam Dehen!! Kau ga tahu saat itu ideku dipakai untuk mengatasi masalah penelitian yang ia pimpin, namun ia memojokkanku dan membentakku. Apakah aku tidak pantas untuk sakit hati Dehen?"

            "Dehen menggelengkan kepala melihat reaksi Dr.Wisnu. Kemudian Dehen mencoba untuk keluar ruangan"

            deh "Aku tidak mau ikut proyek kotormu itu Dr. Wisnu!"

            "Ternyata Dr. Wisnu telah menyiapkan semuanya, beberapa anggota militer memegang lengan Dehen dengan kasar"

            wis "Tak masalah jika kau tak ingin ikut, namun kau tak akan bisa keluar dari pulau ini dan menghubungi siapapun sampai bom nuklir buatan kami siap diluncurkan."

            "Dr. Wisnu memerintahkan anggota militernya untuk menahan Dehen di suatu tempat di mercusuar. Dehen memberontak dan sempat berbicara dengan Anda"

            deh "Tolong, jangan lakukan itu, kau sudah berjanji keputusan apapun yang kau ambil akan bermanfaat untuk Indonesia"
            prot "(Diam)"
            wis "Ini juga akan bermanfaat untuk Indonesia"
            deh "kau ingin mengorbankan anak-anak yang tidak berdosa serta lansia yang tidak berdaya demi membalas rasa sakit hatimu?"
            wis "Diam! Cepat bawa Dehen ke ruang itu."

            "Jauh didalam lubuk hati Anda, Anda merasa bersalah pada Dehen, namun Anda juga sakit hati ketika mendengar kisah DR. Wisnu saat Manhattan Project Meetings."

            wis "Ada lagi yang mau jadi pembelot? Kondisi dunia saat ini sedang sangat genting. Teknologi sangat canggih, pilihannya hanya dua, menindas atau ditindas. Sudah cukup Indonesia merasakan berbagai penindasan, sekarang saatnya Indonesia menyerang"

            "Kata-kata dari Dr. Wisnu mengobarkan semangat semua orang termasuk Anda."


            "6 Bulan kemudian PLTN pertama Indonesia mulai beroperasi, ingin sekali Anda menemui Dehen untuk memberitahukan kabar ini. Namun Anda tahu Dr. Wisnu Akan menolak permintaan Anda. Ketika sedang memikirkan Dehen, Maura datang"

            mau "Aku sangat puas dengan kerja tim kita, PLTN pertama Indonesia akhirnya berdiri"
            prot "(tersenyum)"
            mau "Apa kau sedang memikirkan Dehen?"
            prot "..."
          
            mau "Tenang saja. Setelah peluncuran bom nuklir berhasil, Dehen akan dilepaskan. Walaupun dikurung Dehen mendapatkan perlakuan baik dari Dr. Wisnu, semua kebutuhannya terpenuhi,"
            mau "bahkan kamarnya sekarang sama dengan kamar kita, walaupun tak ada alat komunikasi ataupun jaringan di sekitarnya."

            "Anda tidak memperdulikan perkataan Maura, Anda pergi meninggalkan Maura"


            "Percobaan PLTN selama satu bulan telah terlewati, tidak ditemukan hal ganjil di mesin yang digunakan ataupun komplain dari masyarakat. Dr. Wisnu mulai mempersiapkan laboratorium tambahan di mercusuar untuk proyek tambahannya."
            "Laboratorium ini memang tidak sebagus laboratorium yang ada di lokasi proyek PLTN, namun Anda merasa peralatan yang digunakan lebih canggih." 
            "Selama 3 tahun Anda terlibat proyek Dr. Wisnu dalam perakitan bom nuklir, selama itu pula Anda terus menerus memikirkan Dehen."
            "Setiap malam Anda membuka foto-foto bersama Dehen sebelum berangkat ke pulau ini, tanpa sadar Anda meneteskan air mata. Anda benar-benar merasa bersalah karena Dehen ditahan di suatu tempat yang bahkan Anda tidak tahu."

            mau "Ayo ke lab utama, aku sudah menyempurnakan simulator sebelum bom ini diluncurkan"

            "Rencananya bom ini akan diluncurkan di kota sekitar satu bulan lagi. Sesampainya di lab Anda melihat simulator sedang dinyalakan oleh asisten Dr. Wisnu lainnya."

            "Duar… Terlihat kilatan merah yang disusul dengan suara yang amat keras dari posisi Anda berdiri. Tubuh Anda bergetar, Anda melihat ke sekeliling, terlihat Maura dan Dr. Wisnu tersenyum puas."

            mau "Simulator ini mampu memprediksi kemungkinan keadaan yang terjadi di tempat itu ketika bom nuklir di luncurkan dengan cukup akurat"

            "Dr. Wisnu mengirim gambar hasil simulator ke presiden RI dan jendral TNI RI. Beberapa menit kemudian ada balasan dari mereka." 
            "Mereka sudah mempersiapkan semua dengan baik, bahan jenderal TNI sudah menunjuk 1 tim yang akan melakukan eksekusi pelepasan bom nuklir ini"


            "hari yang mendebarkan itu tiba, hari dimana bom nuklir pertama Indonesia akan dilepaskan sekaligus Dehen akan keluar dari kurungan Dr. Wisnu." 
            "Anda, Dr. Wisnu, dan semua asistennya menyaksikan proses itu dari kamera yang disediakan oleh pemerintah pusat."

            "Duarrrrr!"
            "Bom nuklir itu meledak tepat sesuai perhitungan. Semua makhluk hidup yang ada di kota itu menjadi jasad seketika. Bahkan efek radiasinya menyebar hingga negara tetangganya." 
            "Negara luasnya tidak sampai setengah dari luas Indonesia itu seketika porak-poranda."
            "Semua stasiun TV mengabarkan berita ini. Indonesia diancam akan dikeluarkan dari PBB atas tindakannya. Namun siapa yang berani menggertak negara Indonesia sekarang?"
            "Tidak ada satu negara pun yang berani menentang bahkan melawan Indonesia, hanya sumpah serapah yang bisa orang-orang lakukan melihat keputusan Indonesia dari TV masing-masing."

            "Di tempat yang lain, akhirnya Anda bertemu dengan Dehen setelah beberapa tahun berpisah. Dehen menunjukkan wajah kecewanya ketik bertemu Anda."

            "Apa kau puas? Ribuan orang mati, entah berapa juta orang yang terkena radiasi nuklir ini, bagaimana dengan bayi yang ada di kandungan seorang ibu?" 
            "Bahkan sebelum lahir ia pasti sudah divonis terkena mutasi. KAU ITU MONSTER, KAU DAN KALIAN SEMUA ADALAH PENJAHAT SEBENARNYA"

            "Tubuh Anda bergetar hebat, anda teringat mimpi yang terus berulang sebanyak 9x beberapa tahun itu. Kaki Anda yang bergetar sudah tak dapat menahan massa tubuh Anda sendiri." 
            "Anda pun jatuh ke tanah dan mulaimenyesali semua hal yang dirii Anda sendiri lakukan. berbeda dengan Maura, ia justru menampar pipi kiri Dehen dengan sangat keras."

            mau "Kau, kau tidak tahu apapun tentang ini, kau tak pantas mengatakan itu semua ke sahabatmu sendiri. setiap malam ia selalu memandang fotomu sebelum tidur, tak jarang ia terbangun dngan mata bengkak karena merindukanmu"
            deh "sahabat? Aku tak mau bersahabat dengan pembunuh masal"
            return
            

        #ini ending yang netral
        "Bom nuklir akan memperkuat gerakan nonblok yang dilakukan oleh Indonesia, serta mengamankan negara Indonesia dari tekanan negara lain":
            jump scene8_demi_pertahanan



label scene7_maura_drwisnu:
    "Setelah mengkonfirmasi ke Dr.Wisnu Anda kembali ke kamar Anda untuk beristirahat."

    "Anda masuk ke mess dan menuju ke kamar. Lagi-lagi Anda melirik sebentar ke kamar Dehen. Kali ini pintunya tidak tertutup dan terdengar suara, “You destroyed a turret”."

    prot "Umur berapa sih dia, masih saja suka mengisi waktu kosong dengan bermain game"

    "Anda pun masuk kamar dan mandi. Setelah mandi, Anda memakai pakaian dan merebahkan diri. Anda membuka Instagram dan melihat berbagai Instastory teman-teman Anda." 
    "Ada yang bermain dengan hewan peliharaannya, jalan-jalan bersama pasangan, liburan dengan keluarga, dan lainnya."

    "Anda membuka galeri, tampak foto matahari pagi saat jogging tadi pagi dan foto keindahan Pulau Gelasa." 
    "Ketika Anda ingin membuat story di Instagram, muncul foto-foto lokasi PLTN dan denah pemetaan mesin-mesin. Anda pun mengurungkan niat untuk mengunggah story itu."

    prot "Seandainya pulau cantik ini tidak terisolasi… Seandainya proyek ini bukanlah rahasia negara, pasti aku akan mengunggah semuanya…"

    "Andapun keluar dari mess untuk melihat kondisi sekitar. nampak para anggota militer sedang berolahraga di sore hari." 
    "Anda yang ramah tersenyum kepada mereka ketika beberapa dari. mereka sedang lari melewati Anda sambil menyanyikan yel-yel."
    "Mereka memang tidak membalas senyum Anda, tetapi Anda tahu sorot mata mereka memancarkan senyuman."

    prot "Tak heran memang jika mereka terkesan kaku, memang apa yang terjadi jika mereka berhenti menyanyikan yel-yel sebentar. Dan membalas senyumku?"

    "Anda berjalan menuju pantai, arah mata anda tertuju pada penyu sisik (Eretmochelys imbricata) yang sedang menggali pasir. Setelah terbentuk lubang penyu itu bertelur." 
    "Mungkin ada sekitar 150 butir telur yang penyu itu hasilkan. Anda terus mengamati dari jauh."
    "Selesai bertelur, penyu itu kembali berenang ke laut lagi. Anda menyadari cahaya matahari mulai redup, Anda menyaksikan sunset yang amat indah di pulau gelasa, ditemani hembusan angin dan deburan ombak." 
    "Begitu matahari tenggelam Anda kembali ke mess."

    "Orang-orang bagian dapur sudah menyiapkan makanan untuk kalian makan malam. Anda pun duduk di kursi meja makan untuk bersiap makan." 
    "terdengar langkah beberapa orang turun dari tangga lantai 2, tentu saja itu pasti Dehen dan asisten lainnya. Selang beberapa saat, pintu kamar Maura terbuka, kalian semua berkumpul di meja makan untuk makan malam."

    "Tidak ada percakapan yang berarti malam itu, hanya cAndaan ringan yang menemani kalian semua ketika makan malam berlangsung." 
    "Walaupun Anda masih ragu dengan Maura, Anda berusaha menepisnya karena akan bekerja bersamanya beberapa bulan kedepan. Tidak nyaman tentunya jika ada perselisihan sekecil apapun itu."

    "Selesai makan malam, Anda kembali ke kamar dan segera menyalakan komputer. Anda mengambil flashdisk yang berisi file penelitian Nobel Anda. Meskipun bisa menyimpan semua file itu di drive,"
    "Anda takut ada yang meretas komputer disini. Walaupun dengan semua keamanan yang ketat ini, kecil kemungkinan hal itu terjadi."

    prot "Sepertinya bukan di tahun ini, tak mungkin aku menyelesaikan penelitianku bersamaan dengan pengerjaan proyek ini." 
    prot "Atau… mungkin dengan bergabung di dry lab dengan Maura dan Dr. Wisnu aku dapat menyelesaikan penelitianku bersamaan dengan PLTN ini!"

    "Keesokan paginya Anda pun memasuki ruang wet lab. Dr. Wisnu duduk di depan komputer sambil mencari data, sedangkan Maura mempersiapkan semua perhitungannya."

    mau "Pagi semua, mari kita tinjau perhitungan yang akan kita lakukan hari ini"

    "Anda, Maura dan Dr. Wisnu bekerja keras hingga sore hari, hingga pada suatu saat pada tahap perhitungan ditemukan galat yang sangat besar dari hasil perhitungan." 
    "Tentu saja, Anda mengetahui penyebab galat yang ada pada perhitungan tersebut."
    "Namun, Anda selalu memikirkan untuk mematenkan perhitungan tersebut. Sehingga Anda enggan untuk membantu menyelesaikan perhitungan tersebut."

    mau "Ini gimana sih? Galatnya Besar sekali!"

    "Dr. Wisnu lalu melihat Maura stres dengan perhitungannya. Waktu jam makan siang pun berdering."

    wis "Sudahlah Maura, kita lanjutkan di nanti hari saja. Waktu sudah menunjukkan waktu makan siang."

    mau "Kalian duluan saja, aku akan menghitung kembali perhitungannya dari awal"

    wis "Baiklah Maura, tolong jangan lupa untuk beristirahat."

    "Dr. Wisnu keluar dari ruangan, Anda berniat untuk mengikuti Dr.Wisnu keluar ruangan menuju makan siang; Namun, Anda kasihan melihat kondisi Maura yang stres." 
    "Pada akhirnya Anda berniat untuk membantu Maura menyelesaikan perhitungannya. Demi kebaikan Indonesia."

    mau "Kau masih disini? Jika kamu tidak makan siang juga tolong bantu aku menyelesaikan perhitungan dengan otakmu itu"

    prot "Baiklah, sepertinya aku baru terpikirkan tentang sesuatu dan hal apa yang bisa dilakukan untuk memperbaiki perhitungannya."

    mau "Syukurlah, mari kita lihat hal yang kamu pikirkan itu."

    "Anda dan Maura meninjau ulang perhitungan yang dilakukan"

    prot "Kau melupakan reaksi berantai, 235U + 92Kr + 141Ba + 3n + Energi, dengan energi dalam bentuk panas dan radiasi."

    "Maura mengoreksi kembali perhitungannya"

    mau "kau benar, aku akan menghitungnya kembali"

    "Beberapa saat kemudian."

    mau "Masih ada hal yang kurang… Aku tidak tahu apalagi yang salah."

    "Maura dengan lemas memberikan data hasil perhitungannya. Anda membaca dan mempelajari data dari Maura." 
    "Semua permasalahannya membutuhkan perhitungan yang Anda kembangkan untuk penelitian Nobel Anda. Anda mempertimbangkan hal ini untuk beberapa saat dan memutuskan untuk memberitahukannya."

    prot "Kau belum memasukkan persamaan energi tahap akhir. Masukkan E = m.c2, dengan m merupakan selisih perbedaan selisih massa sebelum direaksikan dan setelah direaksikan."

    "Maura mengangguk dan kembali menghitung. Setelah 15 menit, Maura berteriak kegirangan sembari memegang tangan Anda."

    mau "Kau sangat jenius! Kau benar-benar jenius!"

    "Anda merasa senang karena pujian itu, tetapi sekarang perhitungan itu tidak dapat Anda patenkan sendiri untuk penelitian Nobel Anda." 
    "Namun, seketika Anda teringat oleh perkataan Maura saat pertama melihat lokasi PLTN."

    prot "Ah, iya. Ngomong-ngomong aku ingin bertanya tentang perkataanmu saat melihat reaktor."

    mau "Hm, tentang bom nuklir? Gini saja, coba bayangkan apa yang dapat Indonesia capai jika berhasil membuat bom berkekuatan dahsyat itu."

    "Anda semakin bingung dengan prinsip Maura dan dengan tegas mengingatkannya."

    prot "Bagaimana dengan kehancuran yang disebabkan oleh bom tersebut? Kematian ratusan ribu orang yang tidak bersalah, ibu dan anak anak. Apakah kamu sama sekali tidak memikirkan hal tersebut?"

    mau "Lalu? Pikirkan masa lalu kita. Kamu pikir saat Indonesia dijajah oleh bangsa asing mereka mempedulikan kematian orang tidak bersalah? TIDAK SAMA SEKALI!"
    mau "Kita hanya melakukan hal yang sama kepada mereka sama seperti mereka melakukan itu kepada kita saat masa lalu. Tidak ada bedanya."

    "Anda dan Maura terdiam sejenak."

    mau "Tunggu, pada bagian ini terlihat bahwa reaksi nuklir harus dijaga pada kondisi kritis, bagaimana jika reaksi tidak terjaga dan dilepas begitu saja… AH."

    "Maura seperti mendapatkan ide. Anda semakin merasa tidak nyaman dan takut akan apa yang Maura akan lakukan."

    mau "Aku harus memberi tahu ini ke Dr. Wisnu."

    "Maura langsung berlari keluar ruangan dry lab, meninggalkan Anda."

    prot "Maura TUNGGU-!!!"

    "Maura tidak mendengar teriakan Anda. Anda berpikir kembali perkataan Maura, sepertinya Maura telah memecahkan perhitungan untuk… menciptakan sebuah bom nuklir." 
    "Ide gila yang akan keluar dari ruangan tersebut terlalu berbahaya jika terealisasi."
    "Namun, kenapa Maura harus memberitahu Dr. Wisnu? Dibalik semua pikiran ini, Anda masih merasa bahwa rasionalisasi untuk mengangkat status Indonesia menjadi negara adidaya merupakan alasan yang aneh."

    #ini masuk scene 8 yang percabangan
    menu disaat_genting:
        "Memutuskan untuk memberitahu Dehen tentang ini, berharap Ia setuju dengan Anda.":
            "Anda bergegas ke wet lab dan Anda melihat Dehen baru saja kembali setelah makan siang."
            jump scene8_mengambil_alih
        "Mulai menerima  pemikiran bahwa bom nuklir akan memperkuat gerakan nonblok yang dilakukan oleh Indonesia, serta mengamankan negara Indonesia dari tekanan negara lain.":
            jump scene8_demi_pertahanan

label scene8_demi_pertahanan:
    
    "Anda menghela nafas panjang dan berusaha menenangkan diri. Anda pun pergi mencari Dehen di ruangan wet lab."

    show bg laboratorium
    show dehen neutral at right
    
    deh "Hai sobat, apakah kau menyesal masuk ke dry lab hari ini?" 

    "Anda hanya diam mendengar ejekan Dehen"
    show maura neutral at left
    mau "Tak ku sangka kau sangat jenius, kedepannya kita harus banyak berdiskusi."
    hide maura neutral with dissolve
    hide dehen neutral with dissolve
    show dehen neutral at centerC
    "Dehen berbisik kepada Anda"
    deh "Kau?"
    prot "Iya aku melakukannya"

    "Dehen tersenyum"
    hide maura nutral with dissolve
    "Di tengah percakapan itu, Dr. Wisnu meminta semua orang untuk masuk ke ruang dry lab."

    "Setibanya di ruang dry lab, Dr. Wisnu menjelaskan hal yang kalian alami, termasuk membahas ide pembuatan bom nuklir."
    show dehen neutral at left
    show dr_wisnu neutral at right, x_flip
    deh "Apa kau gila Dr. Wisnu? Rasa sakitmu dipermalukan saat Manhattan Project Meetings beberapa tahun yang lalu harus kau lupakan."
    wis "Tidak Dehen, bukan itu maksudku. Saat itu aku memang sakit hati saat Mr. karan mempermalukanku di depan semua orang, bahkan ia menggunakan ideku yang sempat ia tolak mentah-mentah sebagai penyelesaian proyeknya saat itu." 
    wis "Aku berusaha keras untuk memaafkannya, namun tidak untuk melupakannya"

    wis "Aku sadar egoku begitu tinggi saat itu. Tenang saja Dehen, proek nuklir ini aku buat bukan berdasarkan rasa saki hati, namun untuk pertaanan nasional"
    prot "Bisa kau jelaskan lebih rinci lagi Dr?"
    wis "Negara kita itu sangat stategis, memang dari segi perdagangan dan hubungan internasional aka sangat baik. Namun pernahkah kalian berpikir jika terjadi perang di negara tetangga?" 
    wis "memang kita negara non block, tapi apakah menjamin tidak akan ikut terkena imbas dari perang yang tidak kita ikuti?"

    "kalian hanya terdiam menyimak penjelasan dr. wisnu"

    wis "kita akan membuat bom nuklir agar negara tetangga segan dengan kita. bom ini kita rakit dengan sempurna, namun tidak akan pernah kita ledakkan kecuali Indonesia diserang. Bagaimana? kalian semua setuju?"

    "Semua orang di dry lab menyatakan persetujuan mereka."

    wis "Baik terima kasih atas kepercayaan kalian padaku." 
    wis "Aku sudah meminta izin pada bapak presiden RI dan beliau memerintahkan proyek ini akan diawasi langsung oleh Jenderal TNI karena berhubungan dengan stabilitas nasional. jangan sampai informasi ini bocor kepada siapapun."

    wis "Silahkan tanda tangani MOU ini, jika kalian terbukti membocorkan proyek ini, kalian akan dianggap pengkhianat negara dan akan dipenggal."
    
    hide dehen neutral with dissolve
    hide dr_wisnu neutral with dissolve

    hide bg laboratorium with dissolve
    "Setelah 6 bulan proyek PLTN selesai, Dr. Wisnu mulai mempersiapkan laboratorium tambahan di bawah tanah untuk proyek tambahannya."


    "Laboratorium ini memang tidak sebagus laboratorium yang ada di lokasi proyek PLTN, tetapi Anda merasa peralatan yang digunakan lebih canggih."
    
    show bg pantai siang
    
    "Tidak terasa 4 tahun Anda dan tim bekerja sangat keras untuk merakit bom nuklir. Maura menemui Anda dan Dehen yang sedang mengamati telur penyu yang menetas"
    
    show dehen neutral at left 
    show maura neutral at right
    mau "Sim.."
    prot "Ssssttt, jangan berisik, kehidupan baru sedang dimulai"

    "Anda menutup mulut Maura dengan tangan. Ada sekitar 60 butir telur yang hampir semuanya mesetas secara bersamaan, hanya berselang beberapa menit saja perbedaan umur mereka." 
    "Setelah banyak telur penyu menetas, Anda dan Dehen berlomba meletakkan anak penyu ke laut"

    prot "Hehe maaf, tadi kamu bilang sesuatu?"

    mau "Hadeh!"

    mau "Simulator yang aku kembangkan untuk memprediksi bom nuklir telah selesai." 
    mau "Simulator ini mampu memprediksi kemungkinan keadaan yang terjadi di tempat itu ketika bom nuklir diluncurkan dengan cukup akurat. Dr. Wisnu memanggil kalian untuk melihat hasilnya bersama."

    deh "Pergilah dulu, kami akan menyusul."

    prot "Terima kasih infonya, Maura"
    hide dehen neutral with dissolve
    hide maura neutral with dissolve

    show bg laboratorium

    "Sesampainya di lab, asisten Dr. Wisnu yang lain menghidupkan simulator."

    "Duarrr" #screen shake

    "Suara bom yang begitu keras serta kilatan besar dari radiasi bom yang ditampilkan di simulator itu tampak sangat nyata." 
    "Semua orang di ruangan merinding tidak bisa membayangkan jika bom ini suatu saat diluncurkan, entah berapa ribu korban jiwa meninggal, belum lagi yang terkena radiasinya."

    "Dr. Wisnu mengirim gambar hasil simulator tersebut ke presiden RI dan jendral TNI RI."

    "Beberapa menit kemudian ada balasan dari mereka. Pasukan khusus yang telah dikirimkan untuk menjaga proses perakitan bom kini bertugas menjadi penjaga bom nuklir."

    "Dr. Wisnu menerangkan kepada pasukan itu apa saja yang perlu diperhatikan, dijaga dan dihindari demi keamanan bom ini."

    show bg netral
    "Berita Indonesia memiliki PLTN dan bom nuklir mulai disiarkan. Sesuai dengan prediksi, respon negara adidaya tidak begitu baik, tetapi hal ini menunjukkan bahwa Indonesia sedang di puncak kejayaan." 
    "Tidak ada negara yang berani bermasalah dengan negara Indonesia."

    "Karena misi Anda, Dr. Wisnu, dan asisten lain sudah selesai, Anda dan yang lain dipulangkan." 
    "Perjalanan pulang dari Pulau Gelasa menuju Pulau Bangka Belitung membuat Anda merasa puas dengan hasil kerja keras bertahun-tahun Anda, tetapi masih ada rasa cemas yang tersimpan di pikiran Anda bahwa apakah ini jalan yang benar."

    "Namun, rasa cemas tersebut sempat hilang karena sesampainya di Bangka Belitung, Anda kaget melihat kemajuan teknologi Indonesia saat ini. Tenaga listrik yang berlimpah mendorong pertumbuhan teknologi yang sangat cepat."

    #Tulisan di layar:
    "Indonesia berhasil membuktikan kepada dunia akan kekuatannya, tetapi pada setiap kekuatan ada bayaran tanggung jawab yang besar"
    return


label scene8_mengambil_alih:

    deh "Eh, mengapa kamu tidak makan sia-"

    prot "Tidak ada waktu lagi, kita harus ke dry lab sekarang."

    deh "Tunggu, tunggu, tunggu. Tolong jelaskan ada apa terlebih dahulu."

    "(Anda menjelaskan apa yang terjadi di dry lab)"

    deh "APA!?!? Mereka berencana untuk membuat BOM NUKLIR???"

    prot "(mengangguk)"

    "Setelah kejadian tersebut terdapat panggilan dari Dr.Wisnu kepada seluruh asisten untuk berkumpul di ruang dry lab pada malam hari."

    prot "Sudah ada panggilan dari Dr. Wisnu, sepertinya Maura sudah memberi tahu tentang perhitungannya."

    deh "Baiklah, kita akan kesana bersama. Untuk sekarang kita harus segera bicarakan dengan asisten-asisten lainnya."

    "Anda dan Dehen secara diam-diam mengajak setiap asisten untuk berkumpul di area pantai yang jauh dari lab. Setiap dari mereka terlihat skeptis dan tidak ingin ikut." 
    "Tapi, melihat kecemasan dan ketakutan di wajah kalian mereka tahu bahwa informasi yang kalian ingin beritahu, penting."

    "Tak lama, sore tiba dan kalian berhasil mengumpulkan semua asisten. Dehen seketika mengeluarkan suara."

    deh "Dr. Wisnu  dan Maura akan membuat bom nuklir bersamaan dengan PLTN yang kita sedang kerjakan."

    "Semua tersentak dan sesaat langsung ramai penuh gelisah dan ketakutan."

    prot "Kita harus menolak apa yang akan diberitahukan Dr. Wisnu malam nanti. Kalau tidak, kita akan ikut berkontribusi dalam pembuatan senjata dunia."

    "Para asisten bersama-sama menyerukan persetujuan mereka. Anda, Dehen, dan para asisten bergegas menuju lab Dr. Wisnu."

    jump scene9_titik_darah_penghabisan



label scene9_titik_darah_penghabisan:

    wis "Maura, terima kasih banyak, ya, atas perhitungannya."

    mau "Tentu saja, pak!"

    wis "Hahaha! Dengan perhitungan ini saja, dan semua sumber daya yang kita miliki sekarang, sudah lebih dari cukup untuk membuat bom nuklir! Kita bahkan bisa mulai membuatnya sekarang dengan cepat!!"

    "Anda, Dehen, dan para asisten akhirnya tiba di lab. Mereka menyaksikan Dr. Wisnu dan Maura yang baru saja selesai membangun bom nuklir bersama-sama."

    deh "Akhirnya sampai juga. Lihat! Mereka sudah selesai membangun bomnya!!"

    wis "Lihatlah apa yang telah kita capai. Semua ini adalah hasil dari dedikasi dan pengorbanan kita. Namun, ada satu langkah lagi untuk memastikan Indonesia berdiri sebagai kekuatan yang tak tergoyahkan."

    mau "Dengan bom nuklir ini, tidak ada negara yang berani menginjakkan kakinya di atas kehormatan bangsa kita!"

    "Anda tampak gelisah, terdiam beberapa saat, lalu menatap Dehen."

    prot "Apakah ini benar-benar jalan yang harus kita tempuh? Apa harga dari kekuatan ini tidak terlalu besar?"

    deh "Sudah kubilang, kekuatan seperti ini hanya akan membawa kehancuran... bukan kebangkitan."

    operator_pengeras_suara "Perhatian! Pengaktifan sistem utama dalam 10 detik."

    "Anda berdiri, terbelah antara idealisme dan tekanan tim. Pandangannya beralih dari Dr. Wisnu, ke Maura, lalu ke Dehen."

    prot "Tidak... Aku tidak akan membiarkan ini terjadi!(dengan suara tegas)"

    operator_pengeras_suara "Pengaktifan sistem utama dalam 10 detik. Semua personel dimohon untuk bersiap."

    "Anda berlari ke panel kontrol, melirik ke layar yang menunjukkan hitungan mundur."

    prot "Ini bukan jalan yang benar. Aku tidak akan membiarkan kehancuran ini terjadi!"

    "Dr. Wisnu dan Maura bergegas menghampiri Anda."

    wis "Apa yang kau lakukan?! Kau tidak punya hak untuk menghentikan ini! Ini adalah masa depan bangsa!"

    prot "Tidak, ini bukan masa depan. Ini adalah akhir. Indonesia tidak butuh kehancuran untuk menjadi besar!"

    "Maura mencoba menarik tangan Anda dari panel kontrol."

    mau "Kau tidak mengerti! Ini bukan hanya tentang kita—ini tentang bangsa, tentang kedaulatan yang tidak bisa ditawar lagi!"

    deh "Lepaskan dia, Maura!"

    "Dehen menarik Maura, memberi ruang bagi Anda untuk mematikan sistem. Anda dengan cepat menekan serangkaian tombol."

    prot "Tidak ada waktu lagi. Kita harus mengakhiri ini sekarang!"

    "Layar utama berkedip, muncul tulisan: (PEMBATALAN AKTIVASI BERHASIL.)"

    wis "Kau akan menyesali ini! Apa yang kau pikirkan?!(berteriak marah)"

    prot "Bahwa kita adalah manusia. Bahwa kita harus berjuang tanpa mengorbankan nyawa tak bersalah. Indonesia bisa besar dengan kedamaian, bukan ketakutan."

    "Dr. Wisnu tampak terpukul, lalu berjalan pergi dengan wajah penuh kekecewaan. Maura hanya menunduk tanpa berkata apa-apa."

    "Dehen yang mendekati Anda, menepuk pundaknya."

    deh "Kau menyelamatkan kita semua… dan juga dirimu sendiri."

    "Anda dan Dehen berdiri di bawah langit Pulau Gelasa."

    prot "Kita mungkin belum menyelesaikan semuanya, tapi setidaknya kita masih memiliki kesempatan untuk memperbaikinya."

    deh "Dan kesempatan itu cukup. Mari kita buat masa depan yang lebih baik."

    #tulisan di layar:
    "Dengan keberanian untuk melawan ketidakadilan, masa depan selalu dapat diubah. Untuk Indonesia yang lebih damai."
    return









 
    

        









        
