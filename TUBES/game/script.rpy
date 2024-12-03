# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define prot = Character("protagonis")
define deh = Character("Dehen") 
default remember = 0
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    #show
    
    
    "Anda tinggal di Samarinda dan bekerja untuk Dr. W.R. Wisnu Raksa, ilmuwan paling cerdas di negara ini. /n
    Impianmu adalah menjadi ilmuwan terkemuka dan mampu memenangkan nobel di tahun ini."

    prot "Aduh, proyek dari Pak Wisnu besar sekali, aku merasa sangat lelah. /n
    Sudah 5 hari aku tidur di laboratoriumnya yang sangat dingin itu"

    "Anda saat ini sedang menuju perjalanan ke rumah setelah 5 hari tidak pulang." 
    
    #scene bg house_room #pending asset
    

    "Sesampainya di rumah, anda segera mandi, memakai baju, lalu tidur karena kelelahan."
    "Anda dikejutkan dengan telepon yang masuk, ternyata dari rekan sejawat Anda, Dehen"
    
    prot "haaah, baru saja aku memejamkan mata." 
    prot "Halo Dehen, mengapa kau menelponku."

    deh "Aku ada di depan rumahmu dengan membawa makanan, cepat buka"    
    
    #show dehen #pending asset
    deh "Aku tahu kau pasti tidak sempat membeli makan karena lembur 5 hari, jadi aku membelikannya untukmu."
    deh "yok makan bersama"

    prot "Waw, terima kasih teman"

    #
    "Anda terkejut karena Dehen membeli banyak sekali makanan seperti sate payau, gence ruan, ayam cincane, nasi bekepor, pisang gapit, dan lainnya."

    prot "Hey, mengapa kau membeli banyak sekali makanan? Siapa yang akan menghabiskannya?"

    deh "Sudahlah, jika tak habis kau masukkan saja ke kulkas."
    deh "Komisi yang diberi Pak Wisnu atas penelitian ini besar sekali, sesekali kita juga harus self rewards."

    prot "Memang sepantasnya kita mendapat komisi sebesar itu, penelitian Pak Wisnu ini memiliki risiko yang tinggi, salah sedikit saja kita bisa mengalami mutasi akibat radiasi sinar-sinar itu."
    
    "Setelah Anda dan Dehan selesai makan, Anda mencuci peralatan makan, sedangkan Dehan membersihkan dan merapikan kembali meja makan Anda."

    prot "Dehan, apa rencanamu sore ini?"

    deh "Entahlah, mungkin aku akan menonton tv dan bersantai di rumah"
    
    menu Free_time:
        "Bersantai untuk menikmati me time":
            prot "Yah, sepertinya aku juga akan melakukan hal yang sama. Aku ingin menonton serial favoritku"
            deh "Baiklah, selamat me time, aku pamit pulang"
            prot "Terima kasih untuk makannya, Dehan"
            deh "Tak masalah teman"
            jump Me_Time
        "Membaca jurnal ilmiah":
            prot "Sepertinya menyenangkan. Aku ingin membaca jurnal saja, mengejar impianku menjadi pemenang nobel tahun ini. Penelitian Pak Wisnu membuatku terjeda melakukan penelitianku sendiri"
            Dehen "Semoga kau segera menjadi pemenang nobel. Jangan terlalu memaksakan dirimu juga kawan"
            prot "Tak apa, aku sudah terbiasa dengan ini semua"
            deh "Baiklah aku pulang dulu sekarang"
            prot "Terima kasih untuk makannya, Dehen"
            deh "Tak masalah teman"
            jump Membaca_Jurnal

label Me_Time:



label Membaca_Jurnal:
    menu choice1:
        " Anda membuka google dan membaca…"

        "pilihan 1":
            $ remember = 1

        "pilihan 2":

        "pilihan 3":
    
    
    "Saat hendak tidur Anda teringat.."

    if remember == 1:
        "pilihan 1"
    elif remember == 2:
        "pilihan 2"
    elif remember == 3:
        "pilihan 3"
        

    
        
