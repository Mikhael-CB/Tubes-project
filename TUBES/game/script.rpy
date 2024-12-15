# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define prot = Character("Aku")
define deh = Character("Dehen") 
define wis = Character("Dr. Wisnu")
define mau = Character("Maura")
default remember = 0
transform left:
    xalign 0.15
    yalign 0.54
transform right:
    xalign 0.85
    yalign 0.54

transform center:
    xalign 0.5
    yalign 0.54
    zoom 2.

transform x_flip:
    xzoom -1.

transform no_flip:
    xzoom 1
    yzoom 1.

transform zoom2x:
    zoom 2.

transform bounce(num):
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat num

transform darken:
    linear 0.5 matrixcolor TintMatrix(u"696969") * SaturationMatrix(1.0)
transform lighten:
    linear 0.5 matrixcolor TintMatrix (u"ffffff") * SaturationMatrix(1.0)
transform darken_cus(time):
    linear (time) matrixcolor TintMatrix(u"696969") * SaturationMatrix(1.0)
transform lighten_cus(time):
    linear (time) matrixcolor TintMatrix (u"ffffff") * SaturationMatrix(1.0)

$ jawaban = ""
# The game starts here.

label start:

    # Show a background. This use a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #showcase

    
    
    with dissolve
    "Anda tinggal di Samarinda dan bekerja untuk Dr. W.R. Wisnu Raksa, ilmuwan paling cerdas di negara ini.
    Impianmu adalah menjadi ilmuwan terkemuka dan mampu memenangkan nobel di tahun ini."

    
    with dissolve
    prot "Aduh, proyek dari Pak Wisnu besar sekali, aku merasa sangat lelah.
    Sudah 5 hari aku tidur di laboratoriumnya yang sangat dingin itu"
    
    with dissolve
    "Anda saat ini sedang menuju perjalanan ke rumah setelah 5 hari tidak pulang." 
    
    #scene bg house_room #pending asset
    
    show bg kamar
    with dissolve
    "Sesampainya di rumah, anda segera mandi, memakai baju, lalu tidur karena kelelahan."
    "Anda dikejutkan dengan telepon yang masuk, ternyata dari rekan sejawat Anda, Dehen"
    
    prot "Haaah, baru saja aku memejamkan mata." 
    prot "Halo Dehen, mengapa kau menelponku."

    deh "Aku ada di depan rumahmu dengan membawa makanan, cepat buka"    
    "Anda bergegas menuju pintu dan membukanya."
    
    show dehen neutral at center
    with dissolve
    #show dehen #pending asset
    deh "Aku tahu kau pasti tidak sempat membeli makan karena lembur 5 hari, jadi aku membelikannya untukmu."
    show dehen senang at bounce(1)
    with Dissolve (0.1)

    deh "Mari makan bersama!"

    prot "Wah, terima kasih teman"

    show dehen senang at darken
    "Anda terkejut karena Dehen membeli banyak sekali makanan seperti sate payau, gence ruan, ayam cincane, nasi bekepor, pisang gapit, dan lainnya."

    prot "Hey, mengapa kau membeli banyak sekali makanan? Siapa yang akan menghabiskannya?"

    deh "Sudahlah, jika tak habis kau masukkan saja ke kulkas."
    deh "Komisi yang diberi Pak Wisnu atas penelitian ini besar sekali, sesekali kita juga harus self rewards."

    prot "Memang sepantasnya kita mendapat komisi sebesar itu, penelitian Pak Wisnu ini memiliki risiko yang tinggi, salah sedikit saja kita bisa mengalami mutasi akibat radiasi sinar-sinar itu."
    
    "Setelah Anda dan Dehan selesai makan, Anda mencuci peralatan makan, sedangkan Dehan membersihkan dan merapikan kembali meja makan Anda."

    prot "Dehan, apa rencanamu sore ini?"

    deh "Entahlah, mungkin aku akan menonton tv dan bersantai di rumah"
   
    menu Free_time:
        "Apa yang ingin kamu lakukan sore ini?"
        "Bersantai untuk menikmati me time":
            prot "Yah, sepertinya aku juga akan melakukan hal yang sama. Aku ingin menonton serial favoritku"
            deh "Baiklah, selamat me time, aku pamit pulang"
            prot "Terima kasih untuk makannya, Dehan"
            deh "Tak masalah teman"
            "Anda pun mengantar Dehen hingga ke teras dan membukakan pagar untuknya."
            "Setelah Dehen pulang Anda masuk kamar dan mulai menyalakan TV. Setelah menunggu beberapa jam, akhirnya serial favorit Anda mulai tayang. "
            "Anda sangat senang karena sudah 5 hari melewatkannya"
            prot "Akhirnya aku bisa menontonnya kembali"
            "Baru 15 menit menonton, terjadi pemadaman listrik di kecamatan Anda, hal itu membuat anda kesal"
            prot "Kenapa sih harus terjadi pemadaman sekarang? Padahal serial ini tidak di upload di Youtube, aku melewatkannya lagi"
            "Anda pun hanya diam menatap lampu emergensi yang menyala. Di tengah kesunyian akibat pemadaman listrik Anda pun berpikir seandainya jumlah listrik di Indonesia sangat besar, pasti tidak akan terjadi pemadaman"
            prot "Kenapa Indonesia tidak memiliki listrik yang cukup dari Sabang hingga Merauke ya? Padahal kan semua orang membayar listrik, jika padam begini aktivitas masyarakat akan terganggu. Apalagi zaman modern ini, siapa coba yang ga pake listrik?"
            "Sempat terbesit di pikiran Anda seandainya ada daya listrik yang besar namun murah di seluruh penjuru di Indonesia."
            "Semakin lama, mata Anda semakin berat dan Anda pun tertidur"
        "Membaca jurnal ilmiah":
            prot "Sepertinya menyenangkan. Aku ingin membaca jurnal saja, mengejar impianku menjadi pemenang nobel tahun ini. Penelitian Pak Wisnu membuatku terjeda melakukan penelitianku sendiri"
            deh "Semoga kau segera menjadi pemenang nobel. Jangan terlalu memaksakan dirimu juga kawan"
            prot "Tak apa, aku sudah terbiasa dengan ini semua"
            deh "Baiklah aku pulang dulu sekarang"
            prot "Terima kasih untuk makannya, Dehen"
            deh "Tak masalah teman"
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
    "Lagi-lagi Anda terbangun akibat dering di ponsel Anda. "
    "Ternyata pesan dari Dr.Wisnu yang mengabarkan akan mengadakan pertemuan penting bersama semua asistennya."
    "Pertemuan akan dilakukan pukul 7.00 di laboratorium Dr. Wisnu"
    prot "huh, ada hal apa yang yang ingin dibicarakan?"
    "Anda pun bergegas mandi dan menghangatkan makanan yang diberikan Dehen kemarin dengan microwave."
    "Setelah sarapan Anda berangkat ke laboratorium Dr. Wisnu."
    "Sesampainya di sana, yang Anda lakukan…"
    menu berangkat_ke_lab:
        "Sesampainya di sana, yang Anda lakukan…"
        "menyapa dehen saja":
            "Hallo dehen"
        "menyapa semua asisten Dr. Wisnu":
            "Selamat pagi pak..."
        "Tidak menyapa siapapun, hanya menunggu Dr. Wisnu memasuki laboratorium":
            "..."
    "Beberapa menit kemudian Dr. Wisnu masuk dan memberi informasi mengenai suatu proyek rahasia milik negara."
    "Proyek ini disponsori langsung oleh BUMN dengan modal minimal 100 triliun rupiah. Dr. Wisnu berpesan untuk menjaga kerahasiaan proyek ini."
    "Setelah mendengar informasi lengkap tentang proyek ini dan apa saja peran kalian pada proyek ini, Dr. Wisnu meminta semua asistennya untuk menandatangani MOU."
    "Anda tidak menyangka PLTN yang semalam Anda pikirkan sekilas sebelum tidur kini benar-benar menjadi kenyataan di Indonesia."
    "Anda pun merasa.."

    menu merasa:
        "Anda pun merasa.."
        "sangat jenius karena pernah memikirkannya":
            "gambar protagonis bangga"
        "biasa saja karena proyek itu sudah terlaksana di negara lain":
            "gambar protagonis biasa saja"
        "akan menjadi kaya karena itu merupakan proyek besar":
            "gambar protagonis"
        "sangat bersyukur dan berusaha melakukan hal yang terbaik":
            "gambar protagonis"
    
    wis "Segera siapkan diri kalian dan mulai packing! Minggu depan kita akan berangkat ke pulau Gelasa."

    wis "Untuk keberangkatan kita akan bertemu di Bandara Aji Pangeran Tumenggung Pranoto jam 1 siang, sebab pesawat akan lepas landas pukul 14.00 WITA. Perkiraan sampai di jakarta untuk transit pukul 14.15 WIB dan sampai di Bandara Hanandjoeddin pukul 16.25 WIB."

    wis "Sesampainya di Bangka Belitung akan ada Helikopter Bell-412 yang menjemput kita semua untuk menuju pulau Gelasa dengan kawalan 4 orang dari pihak militer. Estimasi perjalanan sekitar 15 menit jika cuaca baik."


    "Setelah rapat berakhir, Anda mampir ke supermarket untuk membeli kebutuhan logistik selama di perjalanan dari Samarinda ke Pulau Gelasa. Sampai di rumah Anda mulai mengemas barang-barang yang akan Anda bawa."

    "Tak terasa waktu satu minggu telah berlalu. Anda sudah sampai di APT airport pukul 12.45 WITA dan melakukan boarding pass. Anda duduk di pesawat bersebelahan dengan Dehen"

    deh "Kita akan sampai di Gelasa sore hari, ku dengar dari Dr. Wisnu kita baru akan memulai proyek ini setelah 2 hari di sana."
    prot "Aku juga sudah mendengarnya, besok pagi proses pemasangan internet 6G akan selesai dan katanya akan ada tambahan seorang lagi untuk melancarkan proyek ini"
    deh "Ya, benar. Orang itu adalah anggota Panitia Penyelidikan Radioaktivitas dan Tenaga Atom yang diketuai langsung oleh Dr. Wisnu, namanya Maura."
    prot "Darimana kau tahu tentang hal sejauh ini?"

    "Dehen tidak menjawab, ia hanya tersenyum tipis kepada Anda kemudian memalingkan mukanya."
    "Anda tahu, pasti lagi-lagi Dehen menguping percakapan Dr. Wisnu, karena cuma dia yang bisa berbahasa Ambon."
    "Dr. Wisnu sering menggunakan bahasa Ambon jika memberi informasi penting di teleponnya, tujuannya untuk menghindari penyadapan informasi."
    "Sebab saat ini hanya sedikit orang yang bisa berbahasa daerah, itupun didominasi oleh bahasa jawa dan sunda saja."
    "Mayoritas orang lebih tertarik mempelajari bahasa Inggris, mandarin, jerman, dan prancis."

    "Setelah berbincang dengan Dehen, Anda pun…"
    menu setelah_berbincang:
        "Setelah berbincang dengan Dehen, Anda pun…"
        "menikmati pemandangan dari dalam pesawat":
            "..."
        "tidur untuk menghemat tenaga":
            "..."
    "Setelah transit di Jakarta dan menjalani penerbangan beberapa jam, akhirnya kalian tiba di Bandara Hanandjoeddin."
    "Tak perlu menunggu lama, ada seseorang yang menggunakan pakaian dengan corak loreng menghampiri Dr. Wisnu dan memberi hormat."
    "Dr. Wisnu pun memberi hormat balik kepadanya dan keduanya berbincang untuk beberapa waktu."
    "Setelah percakapan diantara keduanya selesai, Dr. Wisnu memerintahkan semua asisten laboratoriumnya untuk segera naik helikopter, semua barang-barang yang ada di bagasi pesawat akan diurus oleh pihak militer yang bertugas."

    prot "Dehen, apa yang akan kau lakukan setelah sampai di pulau itu?"
    deh "Membangun PLTN"
    prot "Bukan itu, maksudku"
    #show prot kesal
    
    "Dehen tertawa melihat ekspresiku yang kesal"
    deh "Malam ini aku akan membongkar barang-barangku dari dalam koper dan menatanya di mess, kemudian aku akan segera tidur. Kalau kau bagaimana?"
    "Anda akan.."
    menu anda_akan:
        "Anda akan.."
        "mengikuti apa yang Deren lakukan":
            "aku akan mengikuti apa yang kamu lakukan"
            "Ternyata Pulau Gelasa memiliki penampakan alam yang sangat indah, bahkan meski dilihat di malam hari."
            "Berbeda dari Samarinda, Jakarta, ataupun Bangka Belitung, penduduk di pulau ini bisa dihitung pakai jari."
            "Penginapan yang dibangun juga dikhususkan untuk para pekerja saja."
            "Dari kejauhan terlihat kapal KRI Diponegoro (365)."
            "Anda takjub dengan semua pemandangan ini ketika menginjakkan kaki di pasir pantai yang berwarna putih seperti kapas."
            "Para pihak militer membantu menurunkan semua barang kalian dari helikopter dan dibawakan menuju kamar mess masing-masing."
            "Anda pun mengikuti salah seorang anggota militer yang membantu membawakan tas anda. Tak lupa anda mengucap terima kasih kepadanya."
            "Anda membongkar semua barang-barang yang ada di koper dan menatanya di lemari dengan rapi."
            "Saat masuk di kamar mandi untuk membersihkan badan, Anda terkejut ternyata terdapat water heater di dalamnya"
            prot "Tak ku sangka ternyata fasilitas di mess ini sangat lengkap, water heater, tv, komputer, AC, dan lainnya. Aku pasti sangat betah tinggal di pulau ini meskipun terpencil"
            "Setelah mandi dan memakai pakaian, Anda menyantap makanan yang sudah disiapkan di meja makan. Selesai makan Anda kembali ke kamar untuk tidur."
        
        "menikmati pemandangan malam di tepi laut":
            "aku akan menikmati pemandangan malam di tepi laut"
            "Ternyata Pulau Gelasa memiliki penampakan alam yang sangat indah, bahkan meski dilihat di malam hari."
            "Berbeda dari Samarinda, Jakarta, ataupun Bangka Belitung, penduduk di pulau ini bisa dihitung pakai jari."
            "Penginapan yang dibangun juga dikhususkan untuk para pekerja saja."
            "Dari kejauhan terlihat kapal KRI Diponegoro (365)."
            "Anda takjub dengan semua pemandangan ini ketika menginjakkan kaki di pasir pantai yang berwarna putih seperti kapas."
            "Para pihak militer membantu menurunkan semua barang kalian dari helikopter dan dibawakan menuju kamar mess masing-masing."
            "Anda pun mengikuti salah seorang anggota militer yang membantu membawakan tas anda. Tak lupa anda mengucap terima kasih kepadanya."
            "Anda membongkar semua barang-barang yang ada di koper dan menatanya di lemari dengan rapi."
            "Saat masuk di kamar mandi untuk membersihkan badan, Anda terkejut ternyata terdapat water heater di dalamnya"
            prot "Tak ku sangka ternyata fasilitas di mess ini sangat lengkap, water heater, tv, komputer, AC, dan lainnya. Aku pasti sangat betah tinggal di pulau ini meskipun terpencil"
            "Setelah mandi dan memakai pakaian, Anda menyantap makanan yang sudah disiapkan di meja makan."
            "Selesai makan Anda memutuskan berjalan-jalan di pantai menikmati keindahan alam di malam hari."
            "Suara ombak dan desir psir membuat otak Anda benar-benar relax."
            "Anda melihat batu besar dan memutuskan untuk duduk di sana. Terlihat beberapa bayangan orang di dalam mercusuar"
            prot "Ketat sekal penjagaan di pulau ini, pasti mereka adalah orang yang mendapat tugas berjaga di shift malam"
            "Setelah puas menikmati pemandangan alam, Anda kembali ke mess untuk tidur"        

        "berjalan-jalan di sekitar mess":
            "aku akan berjalan-jalan di sekitar mess"
            "Ternyata Pulau Gelasa memiliki penampakan alam yang sangat indah, bahkan meski dilihat di malam hari."
            "Berbeda dari Samarinda, Jakarta, ataupun Bangka Belitung, penduduk di pulau ini bisa dihitung pakai jari."
            "Penginapan yang dibangun juga dikhususkan untuk para pekerja saja."
            "Dari kejauhan terlihat kapal KRI Diponegoro (365)."
            "Anda takjub dengan semua pemandangan ini ketika menginjakkan kaki di pasir pantai yang berwarna putih seperti kapas."
            "Para pihak militer membantu menurunkan semua barang kalian dari helikopter dan dibawakan menuju kamar mess masing-masing."
            "Anda pun mengikuti salah seorang anggota militer yang membantu membawakan tas anda. Tak lupa anda mengucap terima kasih kepadanya."
            "Anda membongkar semua barang-barang yang ada di koper dan menatanya di lemari dengan rapi."
            "Saat masuk di kamar mandi untuk membersihkan badan, Anda terkejut ternyata terdapat water heater di dalamnya"
            prot "Tak ku sangka ternyata fasilitas di mess ini sangat lengkap, water heater, tv, komputer, AC, dan lainnya. Aku pasti sangat betah tinggal di pulau ini meskipun terpencil"
            "Setelah mandi dan memakai pakaian, Anda menyantap makanan yang sudah disiapkan di meja makan."
            "Selesai makan Anda memutuskan berjalan-jalan di sekitar mess."
            "Terdapat 3 mess dengan masing masing mess berisi 10 kamar."
            "Banyak kamar kosong di mess itu, kamar anda berada di lantai 2 dan saling berhadapan dengan kamar Dehen."
            prot "Senyap sekali kamar Dehen, pasti dia sudah tidur"
            "Setelah Anda puas berkeliling di sekitar mess, Anda memutuskan kembali ke kamar Anda untuk tidur"
    "Anda terbangun sebelum matahari terbit, kali ini bukan karena suara ponsel yang mengganggu tidur Anda. Namun, Anda memang terbangun karena tubuh Anda sudah merasa tidur yang cukup sehingga badan Anda terasa bugar."
    prot "Selagi masih pagi pasti menyenangkan jogging di tepi pantai sambil menyaksikan sunrise"
    "Sebelum joging Anda menyempatkan untuk mengecek ponsel, ternyata sinyal 6G telah selesai terpasang. Anda menyalakan strava sambil joging di tepi pantai"
    "Sudah 1 jam anda joging, terlihat sebuah Helikopter Bell-412 menurunkan penumpang, seorang wanita dengan rambut panjang yang terurai"
    prot "Apakah itu Maura?"
    "Anda memutuskan untuk"
    menu bertemu_maura:
        "menyambut kedatangannya sekaligus berkenalan":
            "Ketika Anda menuju tempat berdirinya maura, Dr. wisnu sudah duluan tiba di sana. Mereka saling bercengkrama, ketika melihat kehadiran Anda, Dr. Wisnu memperkenalkan Anda pada Maura."
            prot "Hai Maura, salam kenal"
            mau "Hallo, salam kenal juga"

            "Maura pamit menuju ke messnya untuk membongkar barang bawaannya di koper dan membersihkan diri. Karena kalian satu mess, Anda memutuskan berjalan bersama Maura menuju mess. Berbeda dengan Anda dan Dehen, kamar Maura berada di lantai 1, kalian pun berpisah di dekat tangga menuju lantai 2." 

            "Sesampainya di depan kamar, Anda sempat melirik sebentar ke kamar Dehen"

            prot "Kenapa hening sekali? Sepertinya Deren belum bangun"

            "Anda memutuskan untuk mandi dan sarapan. ketika sarapan Anda bertemu dengan Deren dan Maura yang sudah berada di meja makan. Ada asisten Dr. Wisnu lainnya juga di sana"

        "kembali ke mess tanpa mempedulikan kedatangan Maura":
            "Anda segera kembali ke mess untuk membersihkan badan setelah jogging. Ketika sampai di depan kamar, Anda sempat melirik sebentar ke kamar Dehen"

            prot "Kenapa hening sekali? Sepertinya Deren belum bangun"

            "Anda memutuskan untuk mandi dan sarapan. ketika sarapan Anda bertemu dengan Deren dan Maura yang sudah berada di meja makan. Ada asisten Dr. Wisnu lainnya juga di sana. Anda duduk di sebelah Dehen"

            deh "Bagaimana tidurmu? Nyenyak?"

            "Anda hanya mengangguk sambil menyendok nasi di meja makan"

            deh "kenalin nih, namanya Maura"

            mau "Hallo salam kenal ya"
            prot "Hai, salam kenal juga"
    
    "....."
    "Dr. Wisnu mengumpulkan semua asistennya termasuk Maura di suatu ruangan yang mirip Aula"

    wis "Jarak 10 km ke utara dari mess ini, kalian akan menemukan lokasi proyek PLTN yang akan kita kerjakan."
    wis "Beberapa mesin baru datang besok. Jika kalian penasaran dan ingin menuju ke sana hari ini, temui saja anggota militer yang sedang berjaga di sekitar sini. kalian akan diantar menggunakan jeep." 

    "Setelah penjelasan dari Dr. Wisnu dan pembagian jobdesk masing-masing orang dalam tim ini selesai, Dr. Wisnu membubarkan semua orang di Aula." 

    prot "Dehen, apa kau aka ikut melihat pabrik PLTN itu sekarang?"
    deh "tentu saja. bagaimana denganmu Maura?"
    mau "Aku akan ikut bersama kalian semua"


    "Luas Area PLTN ini sekitar 2,5 juta meter persegi (2,5 km persegi), terdapat 5 reaktor yang akan berfungsi sebagai sumber energi panas yang dihasilkan dari reaksi fisi nuklir."
    "Reaksi panas ini akan menghasilkan uap dan akan menggerakan turbin sehingga mampu menghasilkan listrik. Reaktor juga dilengkapi dengan sistem pendingin utama untuk menyalurkan panas dari inti reaktor ke penukar panas untuk mencegah overheating." 

    prot "Semoga dengan adanya proyek ini seluruh kebutuhan listrik di Indonesia terpenuhi. Semoga tidak ada lagi pemadaman listrik untuk penghematan dan biaya listrik setelah ini akan menjadi murah"

    mau "Sudah jelas itu. Kebutuhan listrik di Indonesia sekitar 775 GWh / hari. Adanya PLTS, PLTB, PLTA, dan PLTP yang dibangun mampu memenuhi 23 persen jumlah kebutuhan total listrik harian."
    mau "1 Generator yang kita miliki mampu menghasilkan 3500 MWh / jam, sehingga 1 generator mampu menghasilkan listrik sebesar 84 GWh / hari."
    mau "Kita memiliki 5 generator, jika ditotal listrik yang berhasil kita produksi sekitar 420 GWh / hari, jumlah ini akan jauh lebih banyak dibanding listrik yang kita butuhkan."

    prot "Wow pemikiranmu hebat sekali Maura"
    mau "Kau mau tau apa yang lebih hebat dari perhitunganku?"

    "Anda dan Dehen saling menatap, asisten laboratorium yang lain juga terlihat kebingungan dengan apa yang dikatakan Maura"

    mau "Dengan reaktor sebanyak ini, bukankah sayang jika Indonesia tidak memproduksi bom nuklir?"
    prot "Apa maksudmu?"

    "Maura hanya tersenyum dan kembali ke jeep tanpa menjawab pertanyaan terakhir Anda."
    "Anggota militer yang menjadi supir jeep memanggil kalian semua untuk kembali ke jeep dan melakukan perjalanan pulang kembali ke mess."

    prot "Dehen, entah mengapa aku merasa ada hal yang mengganjal dari perkataan Maura tadi"
    deh "Sudahlah jangan ambil pusing, anggap saja dia hanya bercanda. Ayo kita kembali ke jeep"

    "Anda pun kembali ke mess dengan menggunakan jeep yang sama seperti saat berangkat."

    "Semua orang turun dari jeep ketika jeep berhenti tepat di halaman mess." 

    "Anda turun dari jeep setelah Maura, dilanjut Dehen dan asisten laboratorium lainnya."
    "Maura segera masuk ke mess tanpa memperdulikan yang lainnya."
    "Anda melamun memperhatikan jejak ban dari mobil jeep dan suara Dr. Wisnu menyadarkan lamunan Anda"

    wis "Bagimana? Sudah melihat lokasi PLTN kita? Sangat menawan bukan?"
    prot "Anda hanya mengangguk"
    wis "Ada yang sedang kamu pikirkan?"

    menu kamu_pikirkan:
        "Tidak ada, aku hanya merasa tidak enak badan":
            wis "Baiklah, beristirahatlah, besok mesin-mesin itu akan disetting untuk penelitian kita dalam mendirikan PLTN"
            prot "Baik pak, aku izin masuk dulu"

            "Anda pun masuk ke mess dan menuju ke kamar. Lagi-lagi Anda melirik sebentar ke kamar Dehen, kali ini pintunya tidak tertutup. terdengar suara (You destroyed a turret)."

            prot "(Umur berapa sih dia, masih saja suka mengisi waktu kosong dengan bermain games)"

            "Anda pun masuk kamar mess dan mandi."
            "Setelah mandi Anda dan memakai pakaian Anda rebahan di ranjang."
            "Anda membuka instagram, nampak berbagai instastory teman-teman Anda yang beragam." 
            "Ada yang bermain bersama hewan peliharaan, jalan-jalan bersama pasangan, liburan dengan keluarga, olahraga, dan lainnya."

            "Anda membuka galeri, nampak foto ketika matahari sunrise yang Anda ambil saat jogging tadi pagi, ada juga berbagai foto keindahan pulau Gelasa."
            "Ketika Anda ingin membuat story di instagram, muncul foto-foto lokasi PLTN dan daerah yang sudah diploting untuk mesin-mesin tertentu."
            "Anda pun mengurungkan niat untuk mengupload foto yang Anda ambil hari ini."
            
            prot "Seandainya pulau cantik ini tidak terisolasi."
            prot "Seandainya proyek ini bukanlah rahasia negara, pasti aku akan menguploadnya."

            "Andapun keluar dari mess untuk melihat kondisi sekitar. nampak para anggota militer sedang berolahraga di sore hari. Anda yang ramah tersenyum kepada mereka ketika beberapa dari mereka sedang lari melewati Anda sambil menyanyikan yel-yel. Mereka memang tidak membalas senyum Anda, tetapi Anda tahu sorot mata mereka memancarkan senyumaqn."

            prot " dalam hati :Tak heran memang jika mereka terkesan kaku, memang apa yang terjadi jika mereka berhenti menyanyikan yel-yel sebentar. Dan membalas senyumku?"

            "Anda berjalan menuju pantai, arah mata anda tertuju pada penyu sisik (Eretmochelys imbricata) yang sedang menggali pasir. Setelah terbentuk lubang penyu itu bertelur. Mungkin ada sekitar 150 butir telur yang penyu itu hasilkan. Anda terus mengamati dari jauh. Selesai bertelur, penyu itu kembali berenang ke laut lagi. Anda menyadari cahaya matahari mulai redup, Anda menyaksikan sunset yang amat indah di pulau gelasa, ditemani hembusan angin dan deburan ombak. Begitu matahari tenggelam Anda kembali ke mess."

            "Orang-orang bagian dapur sudah menyiapkan makanan untuk kalian makan malam. Anda pun duduk di kursi meja makan untuk bersiap makan. terdengar langkah beberapa orang turun dari tangga lantai 2, tentu saja itu pasti Dehen dan asisten lainnya. Selang beberapa saat, pintu kamar Maura terbuka, kalian semua berkumpul di meja makan untuk makan malam."

            "Tidak ada percakapan yang berarti malam itu, hanya candaan ringan yang menemani kalian semua ketika makan malam berlangsung. walaupun Anda masih ragu dengan pikiran anda tentang Maura, Anda berusaha menepisnya, Anda akan bekerja bersama Maura beberapa bulan kedepan, tidak nyaman tentunya jika ada perselisihan sekecil apapun itu."

            "Selesai makan malam Anda kembali ke kamar Anda, segera Anda menyalakan komputer. Anda sempat membawa flashdisk yang berisi file penelitian Anda agar bisa menjadi pemenang nobel. Meskipun Anda bisa menyimpan semua file itu di drive dan dihubungkan dengan akun Anda agar lebih praktis, tapi Anda takut ada orang yang  meretas komputer disini, walaupun dengan semua kamaan yang ketat ini, kecil kemungkinan hal itu terjadi."

            prot "Sepertinya bukan di tahun ini, tak mungkin aku menyelesaikan penelitianku bebarengan dengan mengerjakan proyek PLTN ini. Tpi aku akan tetap mengumpulkan lebih banyak data agar ketika proyek PLTN ini selesai aku bisa melanjutkan wet lab ku"


            "Duar… terlihat kilatan merah yang disusul dengan suara yang amat keras dari posisi Anda berdiri. Tubuh Anda bergetar, Anda melihat ke sekeliling, terlihat Maura dan Dr. Wisnu tersenyum puas. Anda baru sadar, ternyata Anda berada di dalam mercusuar. Sekilas mercusuar ini terlihat biasa saja, ternyata di dalamnya terdapat ruangan dengan berbagai alat canggih. Suara, kilatan dan kilatan tadi berasal dari simulator yang Maura ciptakan. Dr. Wisnu menepuk bahu Anda"

            wis "Jika bukan karena penelitian tentang nuklir kita tak mungkin bisa melakukan ini"
            mau "Simulator ini aku design semirip mungkin dengan kemungkinan kondisi yang kan terjadi nanti. Walaupun kita hanya menyerang satu titik di kota itu, namun efek radiasinya akan menyebar di seluruh negara, bahkan ke negara sebelah. Mustahil jika negara lain masih berani dengan Indonesia. Negara ini akan menjadi negara adidaya."

            "Maura dan Dr. Wisnu tertawa membayangkan semua rencana mereka berjalan dengan mulus. sedangkan Anda hanya diam, mencerna semua keadaan yang sedang terjadi."

            prot "Dimana Dehen?"
            mau "Beraninya kau menyebut nama pengkhianat itu?"

            "Anda semakin bingung"
            prot "dalam hati : pengkhianat? Apa maksudnya? Apa yang dia maksud pengkhianat itu Dehen? Mana mungkin Dehen berkhianat?"
            wis "Sudahlah Maura, butuh waktu untuk dia menerima keputusan Dehen"

            "Anda pun keluar dari ruangan itu, ada terlalu banyak anak tangga yang harus Anda turuni untuk mencapai dasar mercusuar. Walau begitu banyak anggota militer yang berjaga di sekitar 10-15 anak tangga. Kepala Anda dipenuhi berbagai macam pertanyaan. Langkah Anda terhenti ketika melihat wajah yang tak asing."

            prot "Bukankah kau anggota militer yang mengantar kami untuk melihat lokasi PLTN saat pertama kali?"

            "Ia hanya mengangguk, ketika Anda hendak bertanya tentang keberadaan Dehen, anggota militer itu segera menutup mulut Anda dan menarik tangan Anda mempercepat menuruni tangga mercusuar. Anda semakin bingung, namun feeling Anda tidak memunculkan perasaan tidak aman. Anda melihat pintu keluar mercusuar, namun Anda justru melewati pintu yang lain, nampak masih banyak anak tangga harus harus Anda lewati. Setelah 25 menit Anda menuruni Anak tangga, lagi-lagi Anda melihat pintu. Pintu ini berbeda dari semua pintu yang Anda lihat sebelumnya di mercusuar ini, pintu ini terbuat dari besi dan ada card id sebagai pengaman untuk masuk. Anggota militer ini menggesek card yang ia bawa, kemudian memberikannya pada Anda sesaat sebelum ia mendorong Anda masuk ke ruangan dibaliknya dan menutup kembali pintu itu. Dorongan mendadak itu membuat tubuh Anda membentur tembok. Anda yang kebingungan menyusuri ruangan itu, Anda menyadari beberapa tembok terbuat dari bahan yang berbeda. Saat Anda menyentuh salah sat bagian dinding di ruang itu, terbuka suatu ruang rahasia. Anda melihat Dehen di dalamnya"

            prot "Dehen? apa yang terjadi"
            deh "Ini semua salahmu"
            prot "Apa? Apa semua ini Dehen, aku tak mengerti apapun?"
            deh "Jika saja kau tak mudah terbujuk dengan tawaran Maura dan Dr. Wisnu, bom itu tidak akan meluncur besok"
            prot "Bom apa Dehen?"
            deh "Aku tahu kau sangat terobsesi dengan nuklir, tapi apa kau tidak memikirkan nyawa orang-orang yang tak berdosa? Anak-anak bahkan lansia?" 
            "KAU ADALAH PENJAHAT YANG SEBENARNYA"

            "Anda terbagun dengan keringat bercucuran, terlihat Dehen duduk disamping tubuh Anda." 
            deh "Sudah 9x kau selalu terbangun dengan kondisi seperti ini. Bahkan reaktor belum menyala tetapi sepertinya otakmu sudah terpapar radiasi nuklir"

            "Selama 9 hari terakhir Anda selalu bermimpi hal yang sama, tapi entah mengapa Anda enggan menceritakannya pada siapapun. Proyek PLTN ini sudah berjalan selama 8 bulan. Kalian masih berkutat untuk menyelaraskan semua fungsi di sistem yang kalian rancang."

            deh "Cepatlah mandi, aku tunggu di ruang makan"

            "Setelah semua orang sarapan, seperti biasanya kalian pergi ke lokasi PLTN menggunakan jeep. Berbeda dengan 8 bulan yang lalu, lokasi ini sudah dipenuhi oleh mesin-mesin besar, bahkan ada bangunan tambahan yang dibangun untuk mesin yang memerlukan sirkulasi tinggi namun tetap melindungi saat terjadi hujan. Anda masuk di laboratorium di pulau Gelasa, Dr. Wisnu sudah duduk di kursinya bersiap menginterupsi kegiatan hari ini. Sepertinya beliau tidak tidur lagi hari ini, terlihat jelas dari kantung matanya yang semakin membengkak dan menghitam"

            "Hari ini Anda bekerja di bagian wet lab, sedangkan Maura, Dr. Wisnu, dan Dehen bekerja di dry lab. Setelah bekerja beberapa jam, Anda beristirahat untuk makan siang, Maura, Dr. Wisnu, dan Dehen belum memunculkan batang hidungnya"

            prot  "dalam hati : Sepertinya mereka sangat sibuk hari ini"

            "Ketika pukul 20.00 WIB Anda bersama asisten lain yang bekerja secara wet lab bersiap untuk kembali, namun orang-orang bekerja secara dry lab belum juga terlihat sejak Dr. Wisnu menginterupsi tadi pagi."

            "Pagi harinya, ketika Anda memasuki lab pulau Gelasa, terlihat Dr. Wisnu, Dehen, dan Maura sudah duduk di kursinya. Anda yakin mereka bekerja sangat keras semalam. Hari ini anda berfokus pada plutonium dan thorium, kombinasi yang sesuai dari bahan ini akan meningkatkan efisiensi bahan bakar nuklir. Saking fokusnya Anda dalam bekerja, Anda sampai melewatkan makan siang bersama asisten wet lab lainnya, sehingga Anda merasa lemas di sore hari. Saat malam tiba.."

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

            "Sesampainya di mess Anda langsung masuk ke kamar dan mandi, begitu juga dengan Dehen yang masuk ke kamarnya dan membersihkan badan. Selesai makan malam Dehen dan Anda menuju kamar Anda. Anda mengunci pintu kamar, sedangkan dehen menutup jendela, memastikan obrolan mereka tidak terdengar hingga keluar kamar."

            prot "Apa yang mau kau katakan sobat?"
            deh "Dry lab kami dari kemarin tidak menemukan solusi. Bahkan Maura yang menguasai berbagai teorema matematika dan fisika tak kunjung berhasil menemukan perhitungan yang sesuai."
            prot "diam dan mendengarkan...."
            deh "tapi aku ingat, kau juga sedang mengembangkan penelitian mengenai nuklir kan? Penelitianmu sudah berjalan dari beberapa tahun yang lalu"
            prot "(diem ga berekspresi)"
            deh "Apa kau tidak pernah melakukan perhitungan? kau pasti sudah melakukan perhitungan bukan?"
            prot "masih diam"
            deh "Yaa aku tahu kau memang ingin menjadi peraih nobel, tapi bukankah penelitianmu banyak? Apakah akan berdampak besar jika kau memberi tahu sedikit hasil perhitunganmu demi kelancaran proyek ini"
            prot "(masih diam)"
            deh "Kau juga berkeinginan proyek ini sukses bukan? Kau ingin kebutuhan listrik semua rakyat Indonesia terpenuhi kan?"
            prot "....."
            deh "Maaf aku terlalu berlebihan, kau berhak mematenkan semua penelitianmu itu"

            "Dehen berbaring di tempat tidur anda dan menarik selimut."
            prot "Akan aku pertimbangkan apa yang kau ucapkan malam ini Dehen"

            "Anda berbaring di sebelah Dehen. Sambil memunggungi Anda,"
            deh "Dengar, aku akan mendukungmu, aku sengaja tidak memberithu Dr. Wisnu tentang apa yang kau kerjakan dan tidak membahas ini di jeep karena aku sangat menghormatimu sebagai teman. Berjanjilah keputusan apapun yang kau ambil akan bermanfaat untuk Indonesia"
            prot "Ya, aku berjanji"


        
        "Saat sedang berada di lokasi, Maura sempat menyinggung kegunaan radiator untuk membuat bom nuklir. Apa maksudnya itu?":
            "..."
    "Esok paginya, setelah sampai di lokasi proyek PLTN Anda"
    menu ending:
        "Mempertahankan apa yang menjadi hak Anda":
            "Setelah 2 minggu bekerja Anda berhasil menemukan kombinasi yang tepat dari plutonium (Pu) dan Thorium (Th). Sekarang Anda berfokus pada MOX (Mixed Oxide Fuel). Kali ini Anda bekerja langsung bersama Dr. Wisnu. Perlu waktu sekitar 1 bulan untuk mendapat komposisi yang pas. Dehen, Maura, dan asisten lain berkutat mati matian untuk mencari perhitungan yang tepat. Di dalam hati nurani, Anda merasa apa yang Anda lakukan sangat egois. Sikap Anda seperti bertentangan dengan sila ke-2 dari Pancasila, yakni “Kemanusiaan yang adil dan beradab”. Anda mengetahui secara pasti perhitungan yang sedang mereka cari, dan membiarkan mereka dalam kebingungan dan kelelahan. Namun disisi lain Anda teringat UUD 1945 pasal 28C ayat 2, yakni setiap orang berhak untuk memajukan dirinya dalam memperjuangkan haknya secara kolektif untuk membangun masyarakat, bangsa, dan negara. Anda berpikir jika Anda telah menjadi peraih nobel, ilmu yang Anda miliki juga akan bermanfaat bagi kemajuan teknologi Indonesia."
            "Kali ini Anda bekerja sama dengan Maura di bagian wet lab, sedangkan Dr. Wisnu bekerjasama dengan Dehen di dry lab. Anda mencari komposisi serta metode yang tepat untuk memperlambat neutron. Memungkinkan reaksi berantai yang stabil dalam reaktor nuklir menggunakan grafit (air berat)."
            "Tak terasa sudah 5 bulan Anda bekerja satu lab bersama Maura. Anda semakin dekat dengannya, kalian saling bertukar cerita tentang latar belakang masing-masing."
            jump good_ending

        "Menemui Dr. Wisnu untuk membicarakan penelitian Anda":
            prot "Dr. Wisnu, bolehkah hari ini aku bekerja secara dry lab?"
            wis "Apa kau sedang mengalami masalah?"
            prot "Tidak, aku ingin rehat sejenak mencium bau bahan-bahan kimia itu"
            wis "Baiklah, hari ini kamu, Maura, dan aku akan bekerja secara dry lab, dehen dan asisten lain akan bekerja secara wet lab"
            jump neutral_bad_ending




label good_ending:
    mau "Kau adalah orang yang sangat jenius dan baik, apa mimpimu?"
    menu ending12:
        "Aku ingin membangun Indonesia melalui kemampuan yang aku punya, Ilmu Pengetahuan dan Teknologi":
            mau "Kupikir kau ingin menjadi peraih nobel"
            prot "mengangguk"
            mau "Setelah 5 bulan bekerja di lab yang sama, firasatku mengatakan kau bisa menjadi peraih nobel"
            prot "(tersenyum)"

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

            "Dehen dan Dr, Wisnu berhasil menyelesaikan perhitungannya. Anda dan Maura ditempatkan di dry lab untuk menyempurnakan perhitungan mereka."

            "Setelah hampir 2 tahun bekerja, akhirnya PLTN pertama yang dimiliki Bangsa Indonesia beroperasi."
            "selama percobaan 3 minggu belum ada keluhan apapun tentang PLTN ini."
            "Semua kebutuhan listrik rakyat Indonesia dari sabang hingga merauke terpenuhi."
            "Harga listrik di Indonesia menjadi sangat murah."
            "Indonesia dijadikan contoh negara di Asia tenggara yang menggunakan PLTN sebagai sumber utama dalam memenuhi listrik negara."

            "Rencananya akan ada proyek PLTN tambahan agar semua tenaga listrik hanya bersumber dari nuklir saja, tidak perlu mengandalkan batubara yang kurang ramah lingkungan."
    return

label neutral_bad_ending:
    "Anda pun memasuki ruang wet lab. Dr. Wisnu duduk di depan komputer sambil mencari data, sedangkan Maura menjelaskan semua perhitungannya ketika bersama Dehen."

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
    prot "(anda terkaget)"
    wis "Kondisi yang superkritis akan menghasilkan reaksi berantai tak terkendali yang sangat cepat, kita tidak perlu merancang sistem pengendalian sehingga reaksi bisa terjadi secara eksponensial"
    mau "Dengan begitu Indonesia akan menjadi negara adidaya"
    wis "tepat sekali Maura"

    wis "Saat makan siang mari. Berkumpul untuk membahas ini bersama asisten lainnya"

    "Anda ke kamar mandi untuk mencuci muka dan menenangkan diri, di depan cermin anda bergumam"

    prot "Semuanya terjadi sangat cepat, apa yang dikatakan Dr. Wisnu sangat mengejutkan"

    "Anda berpikir bahwa…"
    menu ending13:
        "Bom nuklir akan membuat semua negara, terutama di wilayah asia tenggara akan tunduk":
            "Semua orang berkumpul untuk makan siang"
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

            wis "Ada lagi yang mau jadi pembelot? Kondisi dunia saat ini sedang sangat genting. Teknologi sangat canggih, pilihannya hanya 2, menindas atau ditindas. Sudah cukup Indonesia merasakan berbagai penindasan, sekarang saatnya Indonesia kembali mengaum"

            "Kata-kata dari Dr. Wisnu mengobarkan semangat semua orang termasuk Anda."


            "6 Bulan kemudian PLTN pertama Indonesia mulai beroperasi, ingin sekali Anda menemui Dehen untuk memberitahukan kabar ini. Namun Anda tahu Dr. Wisnu Akan menolak permintaan Anda. Ketika sedang memikirkan Dehen, Maura datang"

            mau "Aku sangat puas dengan kerja tim kita, PLTN pertama Indonesia akhirnya berdiri"
            prot "(tersenyum)"
            mau "Apa kau sedang memikirkan Dehen?"
            prot "..."
            mau "Tenang saja, setelah peluncuran bom nuklir berhasil, Dehen akan dilepaskan. Walaupun dikurung Dehen mendapatkan perlakuan baik dari Dr. Wisnu, semua kebutuhannya terpenuhi, bahkan kamarnya sekarang sama dengan kamar kita, walaupun tak ada alat komunikasi ataupun jaringan di sekitarnya"

            "Anda tidak memperdulikan perkataan Maura, Anda pergi meninggalkan Maura"


            "Percobaan PLTN selama 1 bulan telah terlewati, tidak ditemukan hal ganjil di mesin yang digunakan ataupun komplain dari masyarakat. Dr. wisnu mulai mempersiapkan laboratorium tambahan di mercusuar untuk proyek tambahannya. Laboratorium ini memang tidak sebagus laboratorium yang ada di lokasi proyek PLTN, namun Anda merasa peralatan yang digunakan lebih canggih. Selama 3 tahun Anda terlibat proyek Dr. Wisnu dalam perakitan bom nuklir, selama itu pula Anda terus menerus memikirkan Dehen. Setiap malam Anda membuka foto-foto bersama Dehen sebelum berangkat ke pulau ini, tanpa sadar Anda meneteskan air mata. Anda benar-benar merasa bersalah karena Dehen ditahan di suatu tempat yang bahkan Anda tidak tahu."

            mau "Ayo ke lab utama, aku sudah menyempurnakan simulator sebelum bom ini diluncurkan"

            "Rencananya bom ini akan diluncurkan di kota xxxxxx ga kepikiran kota negara apa, tolong bantu ngarang sekitar 1 bulan lagi. Sesampainya di lab utama anda melihat simulator sedang dinyalakan oleh asisten Dr. Wisnu lainnya. Duar… maaf aku ga tau ini suara harusnya gmn wkwkw terlihat kilatan merah yang disusul dengan suara yang amat keras dari posisi Anda berdiri. Tubuh Anda bergetar, Anda melihat ke sekeliling, terlihat Maura dan Dr. Wisnu tersenyum puas." 

            mau "Simulator ini mampu memprediksi kemungkinan keadaan yang terjadi di tempat itu ketika bom nuklir di luncurkan dengan cukup akurat"

            "Dr. Wisnu mengirim gambar hasil simulator ke presiden RI dan jendral TNI RI. Beberapa menit kemudian ada balasan dari mereka. Mereka sudah mempersiapkan semua dengan baik, bahan jenderal TNI sudah menunjuk 1 tim yang akan melakukan eksekusi pelepasan bom nuklir ini"


            "hari yang mendebarkan itu tiba, hari dimana bom nuklir pertama Indonesia akan dilepaskan sekaligus Dehen akan keluar dari kurungan Dr. Wisnu. Anda, Dr. Wisnu, dan semua asistennya menyaksikan proses itu dari kamera yang disediakan oleh pemerintah pusat."

            "Duarrrrr bom nuklir itu meledak tepat sesuai perhitungan. Semua makhluk hidup yang ada di kota itu menjadi jasad seketika. Bahkan efek radiasinya menyebar hingga negara tetangganya. Negara luasnya tidak sampai setengah dari luas Indonesia itu seketika porak-poranda. Semua stasiun tv mengabarkan berita ini. Indonesia diancam akan dikeluarkan dari PBB atas tindakannya. Namun siapa yang berani menggertak negara Indonesia sekarang? tidak ada satu negara pun yang berani menentang bahkan melawan Indonesia, hanya sumpah serapah yang bisa orang-orang lakukan melihat keputusan Indonesia dari tv masing-masing." 

            "Di tempat yang lain, akhirnya Anda bertemu dengan Dehen setelah beberapa tahun berpisah. Dehen menunjukkan wajah kecewanya ketik bertemu Anda."

            "Apa kau puas? Ribuan orang mati, entah berapa juta orang yang terkena radiasi nuklir ini, bagaimana dengan bayi yang ada di kandungan seorang ibu? Bahkan sebelum lahir ia pasti sudah divonis terkena mutasi. KAU ITU MONSTER, KAU DAN KALIAN SEMUA ADALAH PENJAHAT SEBENARNYA"

            "Tubuh Anda bergetar hebat, anda teringat mimpi yang terus berulang sebanyak 9x beberapa tahun itu. Kaki Anda yang bergetar sudah tak dapat menahan massa tubuh Anda sendiri. Anda pun jatuh ke tanah dan mulaimenyesali semua hal yang dirii Anda sendiri lakukan. berbeda dengan Maura, ia justru menampar pipi kiri Dehen dengan sangat keras."

            mau "Kau, kau tidak tahu apapun tentang ini, kau tak pantas mengatakan itu semua ke sahabatmu sendiri. setiap malam ia selalu memandang fotomu sebelum tidur, tak jarang ia terbangun dngan mata bengkak karena merindukanmu"
            deh "sahabat? Aku tak mau bersahabat dengan pembunuh masal"

        "Bom nuklir akan memperkuat gerakan nonblok yang dilakukan oleh Indonesia, serta mengamankan negara Indonesia dari tekanan negara lain":
            "Semua orang berkumpul untuk makan siang"
            deh "Hai sobat, apakah kau menyesal masuk ke dry lab hari ini?" 

            "Anda hanya diam mendengar ejekan Dehen"

            mau "Tak ku sangka kau sangat jenius, kedepannya kita harus banyak berdiskusi."

            "Dehen berbisik kepada Anda"
            deh "Kau?"
            prot "Iya aku melakukannya"

            "Dehen tersenyum"

            "Setelah semua orang selesai makan, Dr. Wisnu meminta semua orang untuk masuk ke ruang dry lab. Setibanya di ruang dry lab, dr. Wisnu menjelaskan hal yang kalian alami, termasuk membahas ide pembuatan bom nuklir."

            deh "Apa kau gila Dr. Wisnu? Rasa sakitmu dipermalukan saat Manhattan Project Meetings beberapa tahun yang lalu harus kau lupakan."
            wis "Tidak Dehen, bukan itu maksudku. Saat itu aku memang sakit hati saat Mr. karan mempermalukanku di depan semua orang, bahkan ia menggunakan ideku yang sempat ia tolak mentah-mentah sebagai penyelesaian proyeknya saat itu. Aku berusaha keras untuk memaafkannya, namun tidak untuk melupakannya"

            wis "Aku sadar egoku begitu tinggi saat itu. Tenang saja Dehen, proek nuklir ini aku buat bukan berdasarkan rasa saki hati, namun untuk pertaanan nasional"
            prot "Bisa kau jelaskan lebih rinci lagi Dr?"
            wis "Negara kita itu sangat stategis, memang dari seg perdagangan dan hubungan internasional aka sangat baik. Namun pernahkah kalian berpikir jika terjadi perang di negara tetangga? memang kita negara non block, tapi apakah menjamin tidak akan ikut terkena imbas dari perang yang tidak kita ikuti?"

            "kalian hanya terdiam menyimak penjelasan dr. wisnu"

            wis "kita akan membuat bom nuklir agar negara tetangga segan dengan kita. bom ini kita rakit dengan sempurna, namun tidak akan pernah kita ledakkan kecuali Indonesia diserang. Bagaimana? kalian semua setuju?"


            wis "Baik terima kasih atas kepercayaan kalian padaku. Aku sudah meminta izin pada bapak presiden RI dan beliau memerintahkan proyek ini akan diawasi langsung oleh Jenderal TNI karena berhubungan dengan stabilitas nasional. jangan sampai informasi ini bocor kepada siapapun."

            wis "Silahkan tanda tangani MOU ini, jika kalian terbukti membocorkan proyek ini, kalian akan dianggap pengkhianat negara dan akan dipenggal."

            "6 Bulan kemudian PLTN pertama Indonesia mulai beroperasi, Anda dan semua orang di pulau Gelasa sangat bahagia. Namun perlu dilakukan percobaan selama 1 bulan untuk melihat hasil PLTN ini."


            "Percobaan PLTN selama 1 bulan telah terlewati, tidak ditemukan hal ganjil di mesin yang digunakan ataupun komplain dari masyarakat. Dr. wisnu mulai mempersiapkan laboratorium tambahan di bawah tanah untuk proyek tambahannya. Laboratorium ini memang tidak sebagus laboratorium yang ada di lokasi proyek PLTN, namun Anda merasa peralatan yang digunakan lebih canggih."

            "Tidak terasa 4 tahun Anda dan tim bekerja sangat keras untuk merakit bom nuklir. Maura menemui Anda dan Dehen yang sedang mengamati telur penyu yang menetas"
            mau "Sim.."
            prot "Ssssttt, jangan berisik, kehidupan baru sedang dimulai"

            "Anda menutup mulut Maura dengan tangan. Ada sekitar 60 butir telur yang hampir semuanya mesetas secara bersamaan, hanya berselang beberapa menit saja perbedaan umur mereka. Setelah banyak telur penyu menetas, Anda dan Dehen berlomba meletakkan anak penyu ke laut"


            prot "Ayo Dehen, kita lihat kali ini siapa yang berhasil meletakkan baby penyu ini ke laut paling banyak!"

            "Anda dan dehen saling berlari secepat mungkin sambil tertawa. Maura yang melihat pemandangan ini mengernyitkan dahi."

            prot "Maura! Apa kau tidak ingin mencobanya?"

            "Maura yang belum pernah memegang penyu , ragu-ragu untuk melakukannya. Namun melihat keseruan kami akhirnya ia ikut berlari meletakkan baby penyu di .pantai."

            mau "Bagaimana dengan yang belum menetas?"
            prot "Kemungkinan mereka tidak akan menetas, mereka akan membusuk"
            mau "Mengapa begitu?"
            deh "Tidak semua makhluk beruntung untuk hidup"
            prot "Ada kemungkinan beberapa dari mereka infertil, kekurangan oksigen, ataupun gagal berkembang karena genetik"
            mau "Bagaimana kau tahu?"
            prot "Aku pernah ikut relawan ekosistem saat berkuliah dulu"
            deh "Mengapa kamu mencari kami?"

            mau "Simulator yang aku kembangkan untuk memprediksi bom nuklir telah selesai. Simulator ini mampu memprediksi kemungkinan keadaan yang terjadi di tempat itu ketika bom nuklir di luncurkan dengan cukup akurat. Dr. Wisnu memanggil kalian untuk melihat hasilnya bersama"
            deh "pergilah dulu, kami akan menyusul"
            prot "terima kasih infonya maura :D"

            "sesampainya di lab utama asisten Dr. Wisnu yang lain menghidupkan simulator."
            "Duarrr, suara bom yang begitu keras serta kilatan besar dari radiasi bom yang ditampilkan di simulator itu tampak sangat nyata. Semua orang di ruangan merinding tidak bisa membayangkan jika bom ini suatu saat diluncurkan, entah berapa ribu korban jiwa meninggal, belum lagi yang terkena radiasinya. Kemudian Dr. Wisnu mengirim gambar hasil simulator ke presiden RI dan jendral TNI RI. Beberapa menit kemudian ada balasan dari mereka. Pasukan khusus yang telah dikirimkan untuk menjaga proses perakitan bom kini bertugas menjadi penjaga bom nuklir. Dr. Wisnu menerangkan kepada pasukan itu apa saja yang perlu diperhatikan, dijaga dan dihindari demi keamanan bom ini."

            "Tidak seperti beberapa tahun yang lalu, kini pulau Gelasa terasa cukup amai semenjak kedatangan 30 orang dari pasukan khusus untuk menjaga bom itu."
            "berita Indonesia memiliki PLTN dan bom nuklir mulai disiarkan, sesuai dengan prediksi respon negara adidaya tidak begitu baik, namun hal ini menunjukkan bahwa Indonesia sedang di puncak kejayaan. Tidak ada negara yang berani bermasalah dengan negara Indonesia."

            "karena misi Anda, Dr. Wisnu, dan asisten lain sudah selesai, Anda dan yang lain dipulangkan. Pemberangkatan dari pulau Gelasa menuju Pulau Bangka Belitung menggunakan Helikopter yang sama, yakni Helikopter Bell-412. Sesampainya di Bangka Belitung anda kaget melihat kemajuan teknologi Indonesia saat ini. Tenaga listrik yang berlimpah mendorong pertumbuhan teknologi yang sangat cepat."





 
    

        









        
