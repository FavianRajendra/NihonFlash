# Extensive Grammar datasets with meaning and example sentences
# Covering N5 to N2 levels
GRAMMAR_DATA = {
    "grammar_n5": [
        {
            "front": "～です / ～だ",
            "reading": "Desu / Da",
            "type": "N5 Grammar",
            "connection": "Noun / Na-adj + です/だ",
            "usage": "Standard copula to equate two things (A is B). 'Desu' is polite, 'Da' is casual.",
            "back": "To be (is, am, are)",
            "example": "私は学生です。\n(Watashi wa gakusei desu.)",
            "meaning": "I am a student."
        },
        {
            "front": "～も",
            "reading": "Mo",
            "type": "N5 Grammar",
            "connection": "Noun + も",
            "usage": "Particle replacing 'wa', 'ga', or 'o' to indicate 'also' or 'too'.",
            "back": "Too / Also",
            "example": "私も学生です。\n(Watashi mo gakusei desu.)",
            "meaning": "I am a student too."
        },
        {
            "front": "～で",
            "reading": "De (Particle)",
            "type": "N5 Grammar",
            "connection": "Noun (Place/Tool) + で",
            "usage": "Indicates the location of an action or the means/tool used to do something.",
            "back": "At / In / By means of",
            "example": "バスで学校へ行きます。\n(Basu de gakkou e ikimasu.)",
            "meaning": "I go to school by bus."
        },
        {
            "front": "～に / ～へ",
            "reading": "Ni / E (Particle)",
            "type": "N5 Grammar",
            "connection": "Noun (Place) + に/へ",
            "usage": "'Ni' highlights the destination/arrival point. 'E' highlights the direction. Often interchangeable for 'going to'.",
            "back": "To (Direction/Destination)",
            "example": "日本へ行きたいです。\n(Nihon e ikitai desu.)",
            "meaning": "I want to go to Japan."
        },
        {
            "front": "～を",
            "reading": "O (Particle)",
            "type": "N5 Grammar",
            "connection": "Noun + を + Transitive Verb",
            "usage": "Object marker. Indicates the direct object of an action.",
            "back": "Object marker",
            "example": "水を飲みます。\n(Mizu o nomimasu.)",
            "meaning": "I drink water."
        },
        {
            "front": "～ませんか",
            "reading": "Masen ka",
            "type": "N5 Grammar",
            "connection": "Verb (Masu-stem) + ませんか",
            "usage": "A polite negative question used to invite someone to do something.",
            "back": "Won't you? (Invitation)",
            "example": "一緒に映画を見ませんか。\n(Issho ni eiga o mimasen ka?)",
            "meaning": "Won't you watch a movie with me?"
        },
        {
            "front": "～ましょう",
            "reading": "Mashou",
            "type": "N5 Grammar",
            "connection": "Verb (Masu-stem) + ましょう",
            "usage": "Volitional form. Used to suggest doing something together or offering to do something.",
            "back": "Let's...",
            "example": "帰りましょう。\n(Kaerimashou.)",
            "meaning": "Let's go home."
        },
        {
            "front": "～があります / ～がいます",
            "reading": "Ga arimasu / Ga imasu",
            "type": "N5 Grammar",
            "connection": "Noun + が + あります/います",
            "usage": "Use 'arimasu' for inanimate objects (plants, things). Use 'imasu' for living things (people, animals).",
            "back": "There is / There are",
            "example": "部屋に机があります。\n(Heya ni tsukue ga arimasu.)",
            "meaning": "There is a desk in the room."
        },
        {
            "front": "～たいです",
            "reading": "Tai desu",
            "type": "N5 Grammar",
            "connection": "Verb (Masu-stem) + たいです",
            "usage": "Expresses the speaker's desire to do an action.",
            "back": "Want to do...",
            "example": "寿司が食べたいです。\n(Sushi ga tabetai desu.)",
            "meaning": "I want to eat sushi."
        },
        {
            "front": "～たくないです",
            "reading": "Takunai desu",
            "type": "N5 Grammar",
            "connection": "Verb (Masu-stem) + たくない",
            "usage": "Negative desire. 'Tai' conjugates like an i-adjective.",
            "back": "Do not want to do...",
            "example": "何もしたくないです。\n(Nani mo shitakunai desu.)",
            "meaning": "I don't want to do anything."
        },
        {
            "front": "～好きです",
            "reading": "Suki desu",
            "type": "N5 Grammar",
            "connection": "Noun + が + 好きです",
            "usage": "Used to express fondness. Note the particle is 'ga', not 'o'.",
            "back": "Like",
            "example": "私は猫が好きです。\n(Watashi wa neko ga suki desu.)",
            "meaning": "I like cats."
        },
        {
            "front": "～嫌いです",
            "reading": "Kirai desu",
            "type": "N5 Grammar",
            "connection": "Noun + が + 嫌いです",
            "usage": "Used to express dislike. A fairly strong word in Japanese.",
            "back": "Dislike / Hate",
            "example": "納豆が嫌いです。\n(Nattou ga kirai desu.)",
            "meaning": "I dislike natto."
        },
        {
            "front": "～上手です",
            "reading": "Jouzu desu",
            "type": "N5 Grammar",
            "connection": "Noun + が + 上手です",
            "usage": "Used to praise ability. Usually not used for oneself.",
            "back": "Good at",
            "example": "彼は歌が上手です。\n(Kare wa uta ga jouzu desu.)",
            "meaning": "He is good at singing."
        },
        {
            "front": "～下手です",
            "reading": "Heta desu",
            "type": "N5 Grammar",
            "connection": "Noun + が + 下手です",
            "usage": "Used to describe lack of skill. Often used humbly for oneself.",
            "back": "Bad at",
            "example": "私は絵が下手です。\n(Watashi wa e ga heta desu.)",
            "meaning": "I am bad at drawing."
        },
        {
            "front": "まだ～ていません",
            "reading": "Mada ~te imasen",
            "type": "N5 Grammar",
            "connection": "まだ + Verb (Te-form) + いません",
            "usage": "Indicates an action that has not happened yet but is expected to.",
            "back": "Have not yet...",
            "example": "まだ昼ご飯を食べていません。\n(Mada hirugohan o tabete imasen.)",
            "meaning": "I haven't eaten lunch yet."
        },
        {
            "front": "～より～のほうが",
            "reading": "Yori ~ no hou ga",
            "type": "N5 Grammar",
            "connection": "Noun A + より + Noun B + のほうが",
            "usage": "Comparison. B is more [property] than A.",
            "back": "A is more ... than B",
            "example": "電車より車のほうが速いです。\n(Densha yori kuruma no hou ga hayai desu.)",
            "meaning": "Cars are faster than trains."
        },
        {
            "front": "～の中で～が一番",
            "reading": "No naka de ~ ga ichiban",
            "type": "N5 Grammar",
            "connection": "Noun (Group) + の中で",
            "usage": "Superlative. Establishing the best item within a category/group.",
            "back": "Among ..., ... is the best/most",
            "example": "スポーツの中でサッカーが一番好きです。\n(Supootsu no naka de sakkaa ga ichiban suki desu.)",
            "meaning": "Among sports, I like soccer the best."
        },
        {
            "front": "～つもりです",
            "reading": "Tsumori desu",
            "type": "N5 Grammar",
            "connection": "Verb (Dict-form/Nai-form) + つもりです",
            "usage": "Expresses a definite intention or plan.",
            "back": "Plan to / Intend to",
            "example": "来年、日本へ行くつもりです。\n(Rainen, Nihon e iku tsumori desu.)",
            "meaning": "I plan to go to Japan next year."
        },
        {
            "front": "～くする / ～にする",
            "reading": "Ku suru / Ni suru",
            "type": "N5 Grammar",
            "connection": "i-adj (remove i) + くする / na-adj + にする",
            "usage": "To alter the state of something (make it hot, make it clean).",
            "back": "To make something (adjective)",
            "example": "音を大きくします。\n(Oto o ookiku shimasu.)",
            "meaning": "I will make the sound louder."
        },
        {
            "front": "～たいと思います",
            "reading": "Tai to omoimasu",
            "type": "N5 Grammar",
            "connection": "Verb (Masu-stem) + たい + と思います",
            "usage": "Softens a statement of desire/intent. More polite than just 'tai desu'.",
            "back": "I think I want to...",
            "example": "医者になりたいと思います。\n(Isha ni naritai to omoimasu.)",
            "meaning": "I think I want to become a doctor."
        },
        {
            "front": "～たり～たり",
            "reading": "Tari ~ tari",
            "type": "N5 Grammar",
            "connection": "Verb (Ta-form) + り + Verb (Ta-form) + り + します",
            "usage": "Lists representative actions (doing this, doing that, etc.). Implies other actions.",
            "back": "Do things like A and B",
            "example": "休みの日は本を読んだり、寝たりします。\n(Yasumi no hi wa hon o yondari, netari shimasu.)",
            "meaning": "On holidays, I do things like reading books and sleeping."
        },
        {
            "front": "～たあとで",
            "reading": "Ta ato de",
            "type": "N5 Grammar",
            "connection": "Verb (Ta-form) + あとで",
            "usage": "Sequence of events. Action A happens, then Action B.",
            "back": "After doing...",
            "example": "ご飯を食べたあとで、歯を磨きます。\n(Gohan o tabeta ato de, ha o migakimasu.)",
            "meaning": "I brush my teeth after eating."
        },
        {
            "front": "～前に",
            "reading": "Mae ni",
            "type": "N5 Grammar",
            "connection": "Verb (Dict-form) + 前に",
            "usage": "Sequence of events. Before A happens, do B.",
            "back": "Before doing...",
            "example": "寝る前に本を読みます。\n(Neru mae ni hon o yomimasu.)",
            "meaning": "I read a book before sleeping."
        },
        {
            "front": "～ながら",
            "reading": "Nagara",
            "type": "N5 Grammar",
            "connection": "Verb (Masu-stem) + ながら",
            "usage": "Simultaneous actions. The main action is the second verb.",
            "back": "While doing...",
            "example": "音楽を聞きながら勉強します。\n(Ongaku o kikinagara benkyou shimasu.)",
            "meaning": "I study while listening to music."
        },
        {
            "front": "もう～ました",
            "reading": "Mou ~mashita",
            "type": "N5 Grammar",
            "connection": "もう + Verb (Past tense)",
            "usage": "Indicates completion of an action.",
            "back": "Already done",
            "example": "もう宿題をしました。\n(Mou shukudai o shimashita.)",
            "meaning": "I already did my homework."
        },
    ],
    "grammar_n4": [
        {
            "front": "～ことができます",
            "reading": "Koto ga dekimasu",
            "type": "N4 Grammar",
            "back": "Can do (Potential)",
            "example": "漢字を書くことができます。\n(Kanji o kaku koto ga dekimasu.)",
            "meaning": "I can write Kanji."
        },
        {
            "front": "～かもしれません",
            "reading": "Kamoshiremasen",
            "type": "N4 Grammar",
            "back": "Might / Maybe",
            "example": "明日は雨が降るかもしれません。\n(Ashita wa ame ga furu kamoshiremasen.)",
            "meaning": "It might rain tomorrow."
        },
        {
            "front": "～でしょう",
            "reading": "Deshou",
            "type": "N4 Grammar",
            "back": "Probably / Right?",
            "example": "彼は来るでしょう。\n(Kare wa kuru deshou.)",
            "meaning": "He will probably come."
        },
        {
            "front": "～と言っていました",
            "reading": "To itte imashita",
            "type": "N4 Grammar",
            "back": "Someone said that...",
            "example": "田中さんは明日休むと言っていました。\n(Tanaka-san wa ashita yasumu to itte imashita.)",
            "meaning": "Mr. Tanaka said he will be absent tomorrow."
        },
        {
            "front": "～てみる",
            "reading": "Te miru",
            "type": "N4 Grammar",
            "back": "Try doing...",
            "example": "この帽子をかぶってみてもいいですか。\n(Kono boushi o kabutte mite mo ii desu ka?)",
            "meaning": "May I try putting on this hat?"
        },
        {
            "front": "～なら",
            "reading": "Nara",
            "type": "N4 Grammar",
            "back": "If / In the case of",
            "example": "東京へ行くなら、新幹線が便利です。\n(Tokyo e iku nara, shinkansen ga benri desu.)",
            "meaning": "If you are going to Tokyo, the Shinkansen is convenient."
        },
        {
            "front": "～ば",
            "reading": "Ba (Conditional)",
            "type": "N4 Grammar",
            "back": "If...",
            "example": "安ければ買います。\n(Yasukereba kaimasu.)",
            "meaning": "I will buy it if it is cheap."
        },
        {
            "front": "～たら",
            "reading": "Tara (Conditional)",
            "type": "N4 Grammar",
            "back": "If / When...",
            "example": "雨が降ったら、行きません。\n(Ame ga futtara, ikimasen.)",
            "meaning": "If it rains, I won't go."
        },
        {
            "front": "～と",
            "reading": "To (Conditional)",
            "type": "N4 Grammar",
            "back": "Whenever / If (Natural consequence)",
            "example": "春になると、花が咲きます。\n(Haru ni naru to, hana ga sakimasu.)",
            "meaning": "When spring comes, flowers bloom."
        },
        {
            "front": "～ほしい",
            "reading": "Hoshii",
            "type": "N4 Grammar",
            "back": "Want something",
            "example": "新しい車がほしいです。\n(Atarashii kuruma ga hoshii desu.)",
            "meaning": "I want a new car."
        },
        {
            "front": "～てほしい",
            "reading": "Te hoshii",
            "type": "N4 Grammar",
            "back": "Want someone to do...",
            "example": "あなたに来てほしいです。\n(Anata ni kite hoshii desu.)",
            "meaning": "I want you to come."
        },
        {
            "front": "～あげる",
            "reading": "Ageru",
            "type": "N4 Grammar",
            "back": "To give",
            "example": "私は母に花をあげました。\n(Watashi wa haha ni hana o agemashita.)",
            "meaning": "I gave flowers to my mother."
        },
        {
            "front": "～もらう",
            "reading": "Morau",
            "type": "N4 Grammar",
            "back": "To receive",
            "example": "私は父に時計をもらいました。\n(Watashi wa chichi ni tokei o moraimashita.)",
            "meaning": "I received a watch from my father."
        },
        {
            "front": "～くれる",
            "reading": "Kureru",
            "type": "N4 Grammar",
            "back": "To give (to me)",
            "example": "友達がプレゼントをくれました。\n(Tomodachi ga purezento o kuremashita.)",
            "meaning": "My friend gave me a present."
        },
        {
            "front": "～そう（様態）",
            "reading": "Sou (Youtai)",
            "type": "N4 Grammar",
            "back": "Looks like / Seem",
            "example": "このケーキはおいしそうです。\n(Kono keeki wa oishisou desu.)",
            "meaning": "This cake looks delicious."
        },
        {
            "front": "～そう（伝聞）",
            "reading": "Sou (Denbun)",
            "type": "N4 Grammar",
            "back": "I heard that...",
            "example": "明日は雨だそうです。\n(Ashita wa ame da sou desu.)",
            "meaning": "I heard it will rain tomorrow."
        },
        {
            "front": "～ために",
            "reading": "Tame ni",
            "type": "N4 Grammar",
            "back": "For the sake of / In order to",
            "example": "健康のために運動します。\n(Kenkou no tame ni undou shimasu.)",
            "meaning": "I exercise for my health."
        },
        {
            "front": "～ように",
            "reading": "You ni",
            "type": "N4 Grammar",
            "back": "So that / In order to",
            "example": "忘れないようにメモします。\n(Wasurenai you ni memo shimasu.)",
            "meaning": "I take notes so that I don't forget."
        },
        {
            "front": "～すぎる",
            "reading": "Sugiru",
            "type": "N4 Grammar",
            "back": "Too much...",
            "example": "この靴は大きすぎます。\n(Kono kutsu wa ookisugimasu.)",
            "meaning": "These shoes are too big."
        },
        {
            "front": "～やすい",
            "reading": "Yasui",
            "type": "N4 Grammar",
            "back": "Easy to...",
            "example": "このペンは書きやすいです。\n(Kono pen wa kakiyasui desu.)",
            "meaning": "This pen is easy to write with."
        },
        {
            "front": "～にくい",
            "reading": "Nikui",
            "type": "N4 Grammar",
            "back": "Hard to...",
            "example": "この漢字は覚えにくいです。\n(Kono kanji wa oboenikui desu.)",
            "meaning": "This Kanji is hard to memorize."
        },
        {
            "front": "～てある",
            "reading": "Te aru",
            "type": "N4 Grammar",
            "back": "Is done (Result of action)",
            "example": "窓が開けてあります。\n(Mado ga akete arimasu.)",
            "meaning": "The window has been opened (and is open)."
        },
        {
            "front": "～ておく",
            "reading": "Te oku",
            "type": "N4 Grammar",
            "back": "Do in advance",
            "example": "ホテルを予約しておきます。\n(Hoteru o yoyaku shite okimasu.)",
            "meaning": "I will book the hotel in advance."
        },
        {
            "front": "～てしまう",
            "reading": "Te shimau",
            "type": "N4 Grammar",
            "back": "Completely / Regretfully",
            "example": "宿題を忘れてしまいました。\n(Shukudai o wasurete shimaimashita.)",
            "meaning": "I regrettably forgot my homework."
        },
        {
            "front": "～ところ",
            "reading": "Tokoro",
            "type": "N4 Grammar",
            "back": "Just about to / Just did",
            "example": "今、出かけるところです。\n(Ima, dekakeru tokoro desu.)",
            "meaning": "I am just about to leave."
        },
        {
            "front": "～ばかり",
            "reading": "Bakari",
            "type": "N4 Grammar",
            "back": "Just did / Nothing but",
            "example": "食べたばかりです。\n(Tabeta bakari desu.)",
            "meaning": "I just ate."
        },
        {
            "front": "～はず",
            "reading": "Hazu",
            "type": "N4 Grammar",
            "back": "Supposed to / Expectation",
            "example": "彼はもうすぐ来るはずです。\n(Kare wa mousugu kuru hazu desu.)",
            "meaning": "He is supposed to come soon."
        },
        {
            "front": "～よう",
            "reading": "You (Volitional)",
            "type": "N4 Grammar",
            "back": "Let's... (Casual)",
            "example": "一緒に行こう。\n(Issho ni ikou.)",
            "meaning": "Let's go together."
        },
        {
            "front": "命令形",
            "reading": "Meireikei (Imperative)",
            "type": "N4 Grammar",
            "back": "Command form",
            "example": "早く行け！\n(Hayaku ike!)",
            "meaning": "Go quickly!"
        },
        {
            "front": "禁止形",
            "reading": "Kinshikei (Prohibitive)",
            "type": "N4 Grammar",
            "back": "Don't do...",
            "example": "ここに入るな。\n(Koko ni hairu na.)",
            "meaning": "Don't enter here."
        },
        {
            "front": "受身形",
            "reading": "Ukemi (Passive)",
            "type": "N4 Grammar",
            "back": "Passive voice",
            "example": "私は犬に噛まれました。\n(Watashi wa inu ni kamaremashita.)",
            "meaning": "I was bitten by a dog."
        },
        {
            "front": "使役形",
            "reading": "Shieki (Causative)",
            "type": "N4 Grammar",
            "back": "Make/Let someone do",
            "example": "母は子供に野菜を食べさせました。\n(Haha wa kodomo ni yasai o tabesasemashita.)",
            "meaning": "The mother made her child eat vegetables."
        },
        {
            "front": "使役受身形",
            "reading": "Shieki Ukemi",
            "type": "N4 Grammar",
            "back": "Forced to do",
            "example": "私は母に買い物に行かされました。\n(Watashi wa haha ni kaimono ni ikasaremashita.)",
            "meaning": "I was forced by my mother to go shopping."
        },
        {
            "front": "尊敬語",
            "reading": "Sonkeigo",
            "type": "N4 Grammar",
            "back": "Honorific Language",
            "example": "先生はもう帰られました。\n(Sensei wa mou kaeraremashita.)",
            "meaning": "The teacher has already gone home (Honorific)."
        },
        {
            "front": "謙譲語",
            "reading": "Kenjougo",
            "type": "N4 Grammar",
            "back": "Humble Language",
            "example": "私が荷物をお持ちします。\n(Watashi ga nimotsu o omochi shimasu.)",
            "meaning": "I will carry your luggage (Humble)."
        },
        {
            "front": "～のに",
            "reading": "Noni",
            "type": "N4 Grammar",
            "back": "Even though / Despite",
            "example": "雨なのに、ゴルフに行きました。\n(Ame na noni, gorufu ni ikimashita.)",
            "meaning": "Even though it was raining, I went golfing."
        },
    ],
    "grammar_n3": [
        {
            "front": "～うちに",
            "reading": "Uchi ni",
            "type": "N3 Grammar",
            "back": "While / Before",
            "example": "若いうちにいろいろな経験をしたい。\n(Wakai uchi ni iroiro na keiken o shitai.)",
            "meaning": "I want to experience many things while I am young."
        },
        {
            "front": "～間 / ～間に",
            "reading": "Aida / Aida ni",
            "type": "N3 Grammar",
            "back": "While / During",
            "example": "留守の間に友達が来ました。\n(Rusu no aida ni tomodachi ga kimashita.)",
            "meaning": "A friend came while I was out."
        },
        {
            "front": "～てからでないと",
            "reading": "Te kara denai to",
            "type": "N3 Grammar",
            "back": "Unless / Until",
            "example": "宿題をやってからでないと、遊びに行けません。\n(Shukudai o yatte kara denai to, asobi ni ikemasen.)",
            "meaning": "You can't go play until you finish your homework."
        },
        {
            "front": "～ところだ",
            "reading": "Tokoro da",
            "type": "N3 Grammar",
            "back": "Just about to / Just did",
            "example": "これから食べるところです。\n(Korekara taberu tokoro desu.)",
            "meaning": "I am just about to eat."
        },
        {
            "front": "～とおり",
            "reading": "Toori",
            "type": "N3 Grammar",
            "back": "Just as / As",
            "example": "私が言ったとおりにしてください。\n(Watashi ga itta toori ni shite kudasai.)",
            "meaning": "Please do exactly as I said."
        },
        {
            "front": "～によって",
            "reading": "Ni yotte",
            "type": "N3 Grammar",
            "back": "By / Depending on",
            "example": "文化は国によって違います。\n(Bunka wa kuni ni yotte chigaimasu.)",
            "meaning": "Culture differs depending on the country."
        },
        {
            "front": "～たびに",
            "reading": "Tabi ni",
            "type": "N3 Grammar",
            "back": "Every time",
            "example": "この写真を見るたびに、昔を思い出します。\n(Kono shashin o miru tabi ni, mukashi o omoidashimasu.)",
            "meaning": "Every time I see this photo, I remember the old days."
        },
        {
            "front": "～ば～ほど",
            "reading": "Ba ~ hodo",
            "type": "N3 Grammar",
            "back": "The more... the more",
            "example": "日本語は話せば話すほど上手になります。\n(Nihongo wa hanaseba hanasu hodo jouzu ni narimasu.)",
            "meaning": "The more you speak Japanese, the better you become."
        },
        {
            "front": "～ついでに",
            "reading": "Tsuide ni",
            "type": "N3 Grammar",
            "back": "While / Incidentally",
            "example": "買い物のついでに郵便局へ行きました。\n(Kaimono no tsuide ni yuubinkyoku e ikimashita.)",
            "meaning": "I went to the post office while I was out shopping."
        },
        {
            "front": "～くらい / ～ほど",
            "reading": "Kurai / Hodo",
            "type": "N3 Grammar",
            "back": "About / To the extent",
            "example": "死ぬほど疲れました。\n(Shinu hodo tsukaremashita.)",
            "meaning": "I'm so tired I could die."
        },
        {
            "front": "～くらいなら",
            "reading": "Kurai nara",
            "type": "N3 Grammar",
            "back": "Rather than...",
            "example": "諦めるくらいなら、死んだほうがましだ。\n(Akirameru kurai nara, shinda hou ga mashi da.)",
            "meaning": "I would rather die than give up."
        },
        {
            "front": "～に限る",
            "reading": "Ni kagiru",
            "type": "N3 Grammar",
            "back": "Is the best / Is limited to",
            "example": "夏はビールに限ります。\n(Natsu wa biiru ni kagirimasu.)",
            "meaning": "Beer is the best in summer."
        },
        {
            "front": "～に対して",
            "reading": "Ni taishite",
            "type": "N3 Grammar",
            "back": "In contrast to / Regarding",
            "example": "兄は活発なのに対して、弟はおとなしい。\n(Ani wa kappatsu na no ni taishite, otouto wa otonashii.)",
            "meaning": "In contrast to my active older brother, my younger brother is quiet."
        },
        {
            "front": "～反面",
            "reading": "Hanmen",
            "type": "N3 Grammar",
            "back": "On the other hand",
            "example": "都会の生活は便利な反面、ストレスも多い。\n(Tokai no seikatsu wa benri na hanmen, sutoresu mo ooi.)",
            "meaning": "City life is convenient, but on the other hand, it's stressful."
        },
        {
            "front": "～一方",
            "reading": "Ippou",
            "type": "N3 Grammar",
            "back": "On the other hand / Meanwhile",
            "example": "会議では意見が対立する一方、合意点も見つかった。\n(Kaigi de wa iken ga tairitsu suru ippou, gouiten mo mitsukatta.)",
            "meaning": "While opinions clashed in the meeting, points of agreement were also found."
        },
        {
            "front": "～というより",
            "reading": "To iu yori",
            "type": "N3 Grammar",
            "back": "Rather than",
            "example": "彼は先生というより、友達のようです。\n(Kare wa sensei to iu yori, tomodachi no you desu.)",
            "meaning": "He is more like a friend than a teacher."
        },
        {
            "front": "～かわりに",
            "reading": "Kawari ni",
            "type": "N3 Grammar",
            "back": "Instead of",
            "example": "日曜日ですが、休むかわりに働きます。\n(Nichiyoubi desu ga, yasumu kawari ni hatarakimasu.)",
            "meaning": "It's Sunday, but I'm working instead of resting."
        },
        {
            "front": "～ために",
            "reading": "Tame ni",
            "type": "N3 Grammar",
            "back": "Because / In order to",
            "example": "事故のために電車が遅れました。\n(Jiko no tame ni densha ga okuremashita.)",
            "meaning": "The train was late because of an accident."
        },
        {
            "front": "～によって",
            "reading": "Ni yotte (Cause)",
            "type": "N3 Grammar",
            "back": "Due to / Because of",
            "example": "台風によって木が倒れました。\n(Taifuu ni yotte ki ga taoremashita.)",
            "meaning": "The tree fell due to the typhoon."
        },
        {
            "front": "～から / ～ことから",
            "reading": "Kara / Koto kara",
            "type": "N3 Grammar",
            "back": "From the fact that...",
            "example": "道が濡れていることから、雨が降ったとわかった。\n(Michi ga Nurete iru koto kara, ame ga futta to wakatta.)",
            "meaning": "I knew it rained from the fact that the road was wet."
        },
        {
            "front": "～おかげで / ～せい",
            "reading": "Okage de / Sei",
            "type": "N3 Grammar",
            "back": "Thanks to / Fault of",
            "example": "先生のおかげで合格しました。\n(Sensei no okage de goukaku shimashita.)",
            "meaning": "Thanks to the teacher, I passed."
        },
        {
            "front": "～のだから",
            "reading": "No dakara",
            "type": "N3 Grammar",
            "back": "Since / Because",
            "example": "もう子供じゃないのだから、自分でしなさい。\n(Mou kodomo janai no dakara, jibun de shinasai.)",
            "meaning": "Since you are not a child anymore, do it yourself."
        },
        {
            "front": "～（の）なら",
            "reading": "(No) Nara",
            "type": "N3 Grammar",
            "back": "If it is the case that...",
            "example": "嫌いなら、食べなくてもいいです。\n(Kirai nara, tabenakute mo ii desu.)",
            "meaning": "If you dislike it, you don't have to eat it."
        },
        {
            "front": "～ては / ～では",
            "reading": "Te wa / De wa",
            "type": "N3 Grammar",
            "back": "If / Since (Negative result)",
            "example": "そんなに遊んでいては、試験に合格できませんよ。\n(Sonna ni asonde ite wa, shiken ni goukaku dekimasen yo.)",
            "meaning": "If you play around that much, you won't pass the exam."
        },
        {
            "front": "～さえ～ば",
            "reading": "Sae ~ ba",
            "type": "N3 Grammar",
            "back": "If only...",
            "example": "お金さえあれば、幸せです。\n(Okane sae areba, shiawase desu.)",
            "meaning": "If only I have money, I am happy."
        },
        {
            "front": "～たとえ～ても",
            "reading": "Tatoe ~ temo",
            "type": "N3 Grammar",
            "back": "Even if...",
            "example": "たとえ反対されても、結婚します。\n(Tatoe hantai saretemo, kekkon shimasu.)",
            "meaning": "Even if I am opposed, I will get married."
        },
        {
            "front": "～ということだ",
            "reading": "To iu koto da",
            "type": "N3 Grammar",
            "back": "It means that / I heard that",
            "example": "彼は来ないということは、欠席ということだ。\n(Kare wa konai to iu koto wa, kesseki to iu koto da.)",
            "meaning": "The fact that he isn't coming means he is absent."
        },
        {
            "front": "～と言われている",
            "reading": "To iwarete iru",
            "type": "N3 Grammar",
            "back": "It is said that...",
            "example": "納豆は体にいいと言われています。\n(Nattou wa karada ni ii to iwarete imasu.)",
            "meaning": "It is said that natto is good for the body."
        },
        {
            "front": "～とか",
            "reading": "Toka",
            "type": "N3 Grammar",
            "back": "I heard that... (Rumor)",
            "example": "来月、新しい店ができるとか。\n(Raigetsu, atarashii mise ga dekiru toka.)",
            "meaning": "I heard that a new shop will open next month."
        },
        {
            "front": "～って",
            "reading": "Tte",
            "type": "N3 Grammar",
            "back": "They say / Speaking of (Casual)",
            "example": "田中さん、結婚するって。\n(Tanaka-san, kekkon suru tte.)",
            "meaning": "I heard Tanaka-san is getting married."
        },
        {
            "front": "～はずがない",
            "reading": "Hazu ga nai",
            "type": "N3 Grammar",
            "back": "Cannot be / Impossible",
            "example": "彼が嘘をつくはずがない。\n(Kare ga uso o tsuku hazu ga nai.)",
            "meaning": "There is no way he would lie."
        },
        {
            "front": "～わけがない",
            "reading": "Wake ga nai",
            "type": "N3 Grammar",
            "back": "Definitely not / Impossible",
            "example": "そんな高いもの、買えるわけがない。\n(Sonna takai mono, kaeru wake ga nai.)",
            "meaning": "There is no way I can buy such an expensive thing."
        },
        {
            "front": "～とは限らない",
            "reading": "To wa kagiranai",
            "type": "N3 Grammar",
            "back": "Not necessarily",
            "example": "高いものがいいとは限らない。\n(Takai mono ga ii to wa kagiranai.)",
            "meaning": "Expensive things are not necessarily good."
        },
        {
            "front": "～わけではない",
            "reading": "Wake dewa nai",
            "type": "N3 Grammar",
            "back": "It doesn't mean that...",
            "example": "嫌いなわけではないが、食べたくない。\n(Kirai na wake dewa nai ga, tabetakunai.)",
            "meaning": "It's not that I dislike it, but I don't want to eat it."
        },
        {
            "front": "～ないことはない",
            "reading": "Nai koto wa nai",
            "type": "N3 Grammar",
            "back": "It is not that... not...",
            "example": "走れば間に合わないことはない。\n(Hashireba maniawanai koto wa nai.)",
            "meaning": "It's not impossible to make it in time if I run."
        },
        {
            "front": "～ことは～が",
            "reading": "Koto wa ~ ga",
            "type": "N3 Grammar",
            "back": "It is true that... but",
            "example": "ピアノは弾けることは弾けるが、上手ではない。\n(Piano wa hikeru koto wa hikeru ga, jouzu dewa nai.)",
            "meaning": "It is true that I can play piano, but I am not good."
        },
        {
            "front": "～てもらいたい",
            "reading": "Te moraitai",
            "type": "N3 Grammar",
            "back": "Want someone to do",
            "example": "あなたにこの本を読んでもらいたい。\n(Anata ni kono hon o yonde moraitai.)",
            "meaning": "I want you to read this book."
        },
        {
            "front": "～させてもらいたい",
            "reading": "Sasete moraitai",
            "type": "N3 Grammar",
            "back": "Let me do / Allow me to",
            "example": "今日は早く帰らせてもらいたいのですが。\n(Kyou wa hayaku kaerasete moraitai no desu ga.)",
            "meaning": "I would like to be allowed to go home early today."
        },
        {
            "front": "～なさい",
            "reading": "Nasai",
            "type": "N3 Grammar",
            "back": "Command (Parent to child)",
            "example": "早く寝なさい。\n(Hayaku nenasai.)",
            "meaning": "Go to sleep early."
        },
        {
            "front": "～ば / ～たら / ～と... よかった",
            "reading": "Ba / Tara / To... yokatta",
            "type": "N3 Grammar",
            "back": "Should have / I wish",
            "example": "もっと勉強しておけばよかった。\n(Motto benkyou shite okeba yokatta.)",
            "meaning": "I wish I had studied more."
        },
        {
            "front": "～こと",
            "reading": "Koto",
            "type": "N3 Grammar",
            "back": "Command (Written)",
            "example": "教室で走らないこと。\n(Kyoushitsu de hashiranai koto.)",
            "meaning": "Do not run in the classroom."
        },
        {
            "front": "～べき",
            "reading": "Beki",
            "type": "N3 Grammar",
            "back": "Should / Must",
            "example": "約束は守るべきだ。\n(Yakusoku wa mamoru beki da.)",
            "meaning": "Promises should be kept."
        },
        {
            "front": "～わけにはいかない",
            "reading": "Wake ni wa ikanai",
            "type": "N3 Grammar",
            "back": "Cannot (Socially/Morally)",
            "example": "明日試験があるので、寝るわけにはいかない。\n(Ashita shiken ga aru node, neru wake ni wa ikanai.)",
            "meaning": "I have an exam tomorrow, so I cannot sleep."
        },
        {
            "front": "～ことにする",
            "reading": "Koto ni suru",
            "type": "N3 Grammar",
            "back": "Decide to",
            "example": "毎朝ジョギングすることにしました。\n(Maiasa jogingu suru koto ni shimashita.)",
            "meaning": "I decided to go jogging every morning."
        },
        {
            "front": "～ようにする",
            "reading": "You ni suru",
            "type": "N3 Grammar",
            "back": "Try to",
            "example": "野菜を食べるようにしています。\n(Yasai o taberu you ni shite imasu.)",
            "meaning": "I try to eat vegetables."
        },
        {
            "front": "～ようとする",
            "reading": "You to suru",
            "type": "N3 Grammar",
            "back": "Try to / About to",
            "example": "電車に乗ろうとしたとき、ドアが閉まりました。\n(Densha ni norou to shita toki, doa ga shimarimashita.)",
            "meaning": "When I was about to get on the train, the doors closed."
        },
        {
            "front": "～つもりだ",
            "reading": "Tsumori da",
            "type": "N3 Grammar",
            "back": "Believe that... (Assumption)",
            "example": "若いつもりで無理をしてはいけません。\n(Wakai tsumori de muri o shite wa ikemasen.)",
            "meaning": "Don't overdo it believing you are young."
        },
        {
            "front": "～について",
            "reading": "Ni tsuite",
            "type": "N3 Grammar",
            "back": "About / Concerning",
            "example": "日本の歴史について調べました。\n(Nihon no rekishi ni tsuite shirabemashita.)",
            "meaning": "I researched about Japanese history."
        },
        {
            "front": "～に対して",
            "reading": "Ni taishite (Target)",
            "type": "N3 Grammar",
            "back": "Towards / To",
            "example": "客に対して失礼なことを言ってはいけない。\n(Kyaku ni taishite shitsurei na koto o itte wa ikenai.)",
            "meaning": "You must not say rude things to customers."
        },
        {
            "front": "～にとって",
            "reading": "Ni totte",
            "type": "N3 Grammar",
            "back": "For / To (Perspective)",
            "example": "私にとって家族は一番大切です。\n(Watashi ni totte kazoku wa ichiban taisetsu desu.)",
            "meaning": "To me, family is the most important."
        },
        {
            "front": "～として",
            "reading": "To shite",
            "type": "N3 Grammar",
            "back": "As / In the capacity of",
            "example": "彼は医者として働いています。\n(Kare wa isha to shite hataraite imasu.)",
            "meaning": "He is working as a doctor."
        },
    ],
    "grammar_n2": [
        {
            "front": "～に際して",
            "reading": "Ni saishite",
            "type": "N2 Grammar",
            "back": "On the occasion of / At the time of",
            "example": "留学に際して、多くの準備が必要です。\n(Ryuugaku ni saishite, ooku no junbi ga hitsuyou desu.)",
            "meaning": "Many preparations are necessary when studying abroad."
        },
        {
            "front": "～恐れがある",
            "reading": "Osore ga aru",
            "type": "N2 Grammar",
            "back": "There is a fear/risk that...",
            "example": "台風が来る恐れがあります。\n(Taifuu ga kuru osore ga arimasu.)",
            "meaning": "There is a risk that a typhoon will come."
        },
        {
            "front": "～ものなら",
            "reading": "Mono nara",
            "type": "N2 Grammar",
            "back": "If one could...",
            "example": "帰れるものなら、今すぐ国へ帰りたい。\n(Kaereru mono nara, ima sugu kuni e kaeritai.)",
            "meaning": "If I could return, I would want to go back to my country right now."
        },
        {
            "front": "～ざるを得ない",
            "reading": "Zaru o enai",
            "type": "N2 Grammar",
            "back": "Cannot help but / Have no choice but",
            "example": "社長の命令だから、やらざるを得ない。\n(Shachou no meirei dakara, yarazaru o enai.)",
            "meaning": "Since it's the president's order, I have no choice but to do it."
        },
        {
            "front": "～最中に",
            "reading": "Saichuu ni",
            "type": "N2 Grammar",
            "back": "Right in the middle of",
            "example": "会議の最中に携帯が鳴った。\n(Kaigi no saichuu ni keitai ga natta.)",
            "meaning": "My phone rang right in the middle of the meeting."
        },
        {
            "front": "～うちに",
            "reading": "Uchi ni (Change)",
            "type": "N2 Grammar",
            "back": "While (unintentional change)",
            "example": "知らないうちに雨が降っていた。\n(Shiranai uchi ni ame ga futte ita.)",
            "meaning": "It started raining before I knew it."
        },
        {
            "front": "～ばかりだ",
            "reading": "Bakari da",
            "type": "N2 Grammar",
            "back": "Continue to (Negative trend)",
            "example": "成績は下がるばかりだ。\n(Seiseki wa sagaru bakari da.)",
            "meaning": "My grades just keep going down."
        },
        {
            "front": "～ようとしている",
            "reading": "You to shite iru",
            "type": "N2 Grammar",
            "back": "About to",
            "example": "コンサートが始まろうとしている。\n(Konsaato ga hajimarou to shite iru.)",
            "meaning": "The concert is about to start."
        },
        {
            "front": "～つつある",
            "reading": "Tsutsu aru",
            "type": "N2 Grammar",
            "back": "In the process of",
            "example": "景気は回復しつつある。\n(Keiki wa kaifuku shi tsutsu aru.)",
            "meaning": "The economy is in the process of recovering."
        },
        {
            "front": "～つつ",
            "reading": "Tsutsu",
            "type": "N2 Grammar",
            "back": "While / Although",
            "example": "体に悪いと知りつつ、タバコを吸ってしまう。\n(Karada ni warui to shiri tsutsu, tabako o sutte shimau.)",
            "meaning": "While knowing it's bad for my body, I end up smoking."
        },
        {
            "front": "～てはじめて",
            "reading": "Te hajimete",
            "type": "N2 Grammar",
            "back": "Only after...",
            "example": "病気になってはじめて健康のありがたさがわかった。\n(Byouki ni natte hajimete kenkou no arigatasa ga wakatta.)",
            "meaning": "Only after becoming sick did I understand the value of health."
        },
        {
            "front": "～上（で）",
            "reading": "Ue (de)",
            "type": "N2 Grammar",
            "back": "Upon / After",
            "example": "両親と相談した上で、決めます。\n(Ryoushin to soudan shita ue de, kimemasu.)",
            "meaning": "I will decide upon consulting with my parents."
        },
        {
            "front": "～次第",
            "reading": "Shidai",
            "type": "N2 Grammar",
            "back": "As soon as",
            "example": "決まり次第、連絡します。\n(Kimari shidai, renraku shimasu.)",
            "meaning": "I will contact you as soon as it is decided."
        },
        {
            "front": "～て以来",
            "reading": "Te irai",
            "type": "N2 Grammar",
            "back": "Ever since",
            "example": "日本に来て以来、彼に会っていない。\n(Nihon ni kite irai, kare ni atte inai.)",
            "meaning": "I haven't met him ever since I came to Japan."
        },
        {
            "front": "～てからでないと",
            "reading": "Te kara denai to",
            "type": "N2 Grammar",
            "back": "Unless / Until",
            "example": "準備ができてからでないと、始められません。\n(Junbi ga dekite kara denai to, hajimeraremasen.)",
            "meaning": "We can't start until preparations are done."
        },
        {
            "front": "～をはじめ（として）",
            "reading": "O hajime (to shite)",
            "type": "N2 Grammar",
            "back": "Starting with / Including",
            "example": "この動物園にはパンダをはじめ、珍しい動物がたくさんいる。\n(Kono doubutsuen ni wa panda o hajime, mezurashii doubutsu ga takusan iru.)",
            "meaning": "There are many rare animals in this zoo, starting with pandas."
        },
        {
            "front": "～からして",
            "reading": "Kara shite",
            "type": "N2 Grammar",
            "back": "Judging from / Even",
            "example": "あの人は服装からして金持ちそうだ。\n(Ano hito wa fukusou kara shite kanemochi sou da.)",
            "meaning": "Judging from his clothes, he looks rich."
        },
        {
            "front": "～にわたって",
            "reading": "Ni watatte",
            "type": "N2 Grammar",
            "back": "Over a period of / Throughout",
            "example": "会議は３日間にわたって行われた。\n(Kaigi wa mikka kan ni watatte okonawareta.)",
            "meaning": "The conference was held over a period of 3 days."
        },
        {
            "front": "～を通じて / ～を通して",
            "reading": "O tsuujite / O tooshite",
            "type": "N2 Grammar",
            "back": "Through / Via",
            "example": "インターネットを通じてニュースを知った。\n(Intaanetto o tsuujite nyuusu o shitta.)",
            "meaning": "I learned the news through the internet."
        },
        {
            "front": "～限り",
            "reading": "Kagiri",
            "type": "N2 Grammar",
            "back": "As long as / As far as",
            "example": "私が知っている限り、彼はいい人です。\n(Watashi ga shitte iru kagiri, kare wa ii hito desu.)",
            "meaning": "As far as I know, he is a good person."
        },
        {
            "front": "～だけ",
            "reading": "Dake",
            "type": "N2 Grammar",
            "back": "As much as",
            "example": "食べたいだけ食べてください。\n(Tabetai dake tabete kudasai.)",
            "meaning": "Please eat as much as you want."
        },
        {
            "front": "～に限り",
            "reading": "Ni kagiri",
            "type": "N2 Grammar",
            "back": "Only for / Limited to",
            "example": "女性に限り、ランチ半額。\n(Josei ni kagiri, ranchi hangaku.)",
            "meaning": "Lunch is half price only for women."
        },
        {
            "front": "～限りでは",
            "reading": "Kagiri dewa",
            "type": "N2 Grammar",
            "back": "As far as (based on info)",
            "example": "天気予報の限りでは、明日は晴れだ。\n(Tenki yohou no kagiri dewa, ashita wa hare da.)",
            "meaning": "As far as the weather forecast goes, tomorrow will be sunny."
        },
        {
            "front": "～に限って",
            "reading": "Ni kagitte",
            "type": "N2 Grammar",
            "back": "Only when / Unlucky coincidence",
            "example": "忙しい時に限って、電話がかかってくる。\n(Isogashii toki ni kagitte, denwa ga kakatte kuru.)",
            "meaning": "Phone calls come only when I am busy."
        },
        {
            "front": "～に限らず",
            "reading": "Ni kagirazu",
            "type": "N2 Grammar",
            "back": "Not limited to",
            "example": "この漫画は子供に限らず、大人にも人気がある。\n(Kono manga wa kodomo ni kagirazu, otona ni mo ninki ga aru.)",
            "meaning": "This manga is popular not limited to children, but adults too."
        },
        {
            "front": "～のみならず",
            "reading": "Nomi narazu",
            "type": "N2 Grammar",
            "back": "Not only... but also",
            "example": "彼は英語のみならず、中国語も話せる。\n(Kare wa Eigo nomi narazu, Chuugokugo mo hanaseru.)",
            "meaning": "He can speak not only English but also Chinese."
        },
        {
            "front": "～ばかりか",
            "reading": "Bakari ka",
            "type": "N2 Grammar",
            "back": "Not only... but also",
            "example": "薬を飲んだのに、治るばかりか悪化した。\n(Kusuri o nonda noni, naoru bakari ka akka shita.)",
            "meaning": "Even though I took medicine, not only did I not get better, I got worse."
        },
        {
            "front": "～はもとより",
            "reading": "Wa motoyori",
            "type": "N2 Grammar",
            "back": "Also / Let alone",
            "example": "平日はもとより、週末も忙しい。\n(Heijitsu wa motoyori, shuumatsu mo isogashii.)",
            "meaning": "I am busy on weekends, let alone weekdays."
        },
        {
            "front": "～上（に）",
            "reading": "Ue (ni)",
            "type": "N2 Grammar",
            "back": "On top of / Besides",
            "example": "彼は頭がいいうえに、性格もいい。\n(Kare wa atama ga ii ue ni, seikaku mo ii.)",
            "meaning": "On top of being smart, he has a good personality."
        },
        {
            "front": "～に関して",
            "reading": "Ni kanshite",
            "type": "N2 Grammar",
            "back": "Regarding / About",
            "example": "この問題に関して、ご意見をお願いします。\n(Kono mondai ni kanshite, goiken o onegai shimasu.)",
            "meaning": "Please give your opinion regarding this problem."
        },
        {
            "front": "～をめぐって",
            "reading": "O megutte",
            "type": "N2 Grammar",
            "back": "Concerning / Around (dispute)",
            "example": "遺産をめぐって兄弟が争っている。\n(Isan o megutte kyoudai ga arasotte iru.)",
            "meaning": "The siblings are fighting over the inheritance."
        },
        {
            "front": "～にかけては",
            "reading": "Ni kakete wa",
            "type": "N2 Grammar",
            "back": "When it comes to",
            "example": "料理にかけては、誰にも負けない。\n(Ryouri ni kakete wa, dare ni mo makenai.)",
            "meaning": "When it comes to cooking, I won't lose to anyone."
        },
        {
            "front": "～に対して",
            "reading": "Ni taishite",
            "type": "N2 Grammar",
            "back": "Against / Towards",
            "example": "政府に対してデモが行われた。\n(Seifu ni taishite demo ga okonawareta.)",
            "meaning": "A demonstration was held against the government."
        },
        {
            "front": "～にこたえて",
            "reading": "Ni kotaete",
            "type": "N2 Grammar",
            "back": "In response to",
            "example": "アンコールにこたえて、もう一曲歌った。\n(Ankooru ni kotaete, mou ikkyoku utatta.)",
            "meaning": "In response to the encore, I sang one more song."
        },
        {
            "front": "～をもとに（して）",
            "reading": "O moto ni (shite)",
            "type": "N2 Grammar",
            "back": "Based on",
            "example": "実話をもとにして作られた映画。\n(Jitsuwa o moto ni shite tsukurareta eiga.)",
            "meaning": "A movie made based on a true story."
        },
        {
            "front": "～に基づいて",
            "reading": "Ni motozuite",
            "type": "N2 Grammar",
            "back": "Based on (Data/Law)",
            "example": "データに基づいて計画を立てる。\n(Deeta ni motozuite keikaku o tateru.)",
            "meaning": "Make a plan based on data."
        },
        {
            "front": "～に沿って",
            "reading": "Ni sotte",
            "type": "N2 Grammar",
            "back": "Along with / In accordance with",
            "example": "川に沿って歩く。\n(Kawa ni sotte aruku.)",
            "meaning": "Walk along the river."
        },
        {
            "front": "～のもとで",
            "reading": "No moto de",
            "type": "N2 Grammar",
            "back": "Under (supervision/influence)",
            "example": "厳しい監督のもとで練習した。\n(Kibishii kantoku no moto de renshuu shita.)",
            "meaning": "I practiced under a strict coach."
        },
        {
            "front": "～向けだ",
            "reading": "Muke da",
            "type": "N2 Grammar",
            "back": "Intended for",
            "example": "これは子供向けの本です。\n(Kore wa kodomo muke no hon desu.)",
            "meaning": "This book is intended for children."
        },
        {
            "front": "～につれて",
            "reading": "Ni tsurete",
            "type": "N2 Grammar",
            "back": "As ... then ... (Change)",
            "example": "台風が近づくにつれて、風が強くなった。\n(Taifuu ga chikazuku ni tsurete, kaze ga tsuyoku natta.)",
            "meaning": "As the typhoon approached, the wind became stronger."
        },
        {
            "front": "～にしたがって",
            "reading": "Ni shitagatte",
            "type": "N2 Grammar",
            "back": "In accordance with / As",
            "example": "北へ行くにしたがって、紅葉が早くなる。\n(Kita e iku ni shitagatte, kouyou ga hayaku naru.)",
            "meaning": "As you go north, the autumn leaves change earlier."
        },
        {
            "front": "～に伴って",
            "reading": "Ni tomonatte",
            "type": "N2 Grammar",
            "back": "Along with / Accompanying",
            "example": "人口が増えるに伴って、ゴミも増えた。\n(Jinkou ga fueru ni tomonatte, gomi mo fueta.)",
            "meaning": "Along with the population increase, trash also increased."
        },
        {
            "front": "～とともに",
            "reading": "To tomo ni",
            "type": "N2 Grammar",
            "back": "Together with / As",
            "example": "年をとるとともに、体力が落ちる。\n(Toshi o toru to tomo ni, tairyoku ga ochiru.)",
            "meaning": "As I age, my physical strength drops."
        },
        {
            "front": "～次第だ",
            "reading": "Shidai da",
            "type": "N2 Grammar",
            "back": "Depending on",
            "example": "成功するかどうかは努力次第だ。\n(Seikou suru ka douka wa doryoku shidai da.)",
            "meaning": "Whether you succeed depends on your effort."
        },
        {
            "front": "～に応じて",
            "reading": "Ni oujite",
            "type": "N2 Grammar",
            "back": "According to / In response to",
            "example": "予算に応じてメニューを決めます。\n(Yosan ni oujite menyuu o kimemasu.)",
            "meaning": "We will decide the menu according to the budget."
        },
        {
            "front": "～につけて",
            "reading": "Ni tsukete",
            "type": "N2 Grammar",
            "back": "Whenever",
            "example": "この曲を聞くにつけて、故郷を思い出す。\n(Kono kyoku o kiku ni tsukete, furusato o omoidasu.)",
            "meaning": "Whenever I hear this song, I remember my hometown."
        },
        {
            "front": "～やら～やら",
            "reading": "Yara ~ yara",
            "type": "N2 Grammar",
            "back": "Things like A and B (Chaos)",
            "example": "悲しいやら嬉しいやら、複雑な気持ちだ。\n(Kanashii yara ureshii yara, fukuzatsu na kimochi da.)",
            "meaning": "Sad, happy... it's a complex feeling."
        },
        {
            "front": "～というか～というか",
            "reading": "To iu ka ~ to iu ka",
            "type": "N2 Grammar",
            "back": "Whether A or B (Hard to define)",
            "example": "あの人は子供っぽいというか、無邪気というか。\n(Ano hito wa kodomoppoi to iu ka, mujaki to iu ka.)",
            "meaning": "He is childish, or perhaps innocent..."
        },
        {
            "front": "～にしても～にしても",
            "reading": "Ni shitemo ~ ni shitemo",
            "type": "N2 Grammar",
            "back": "Whether A or B",
            "example": "行くにしても行かないにしても、連絡してください。\n(Iku ni shitemo ikanai ni shitemo, renraku shite kudasai.)",
            "meaning": "Whether you go or not, please contact me."
        },
        {
            "front": "～といった",
            "reading": "To itta",
            "type": "N2 Grammar",
            "back": "Such as",
            "example": "京都や奈良といった古い町が好きです。\n(Kyouto ya Nara to itta furui machi ga suki desu.)",
            "meaning": "I like old towns such as Kyoto and Nara."
        },
        {
            "front": "～を問わず",
            "reading": "O towazu",
            "type": "N2 Grammar",
            "back": "Regardless of",
            "example": "年齢を問わず、誰でも参加できます。\n(Nenrei o towazu, dare demo sanka dekimasu.)",
            "meaning": "Anyone can participate regardless of age."
        },
        {
            "front": "～にかかわりなく",
            "reading": "Ni kakawarinaku",
            "type": "N2 Grammar",
            "back": "Regardless of",
            "example": "理由にかかわりなく、遅刻は認めない。\n(Riyuu ni kakawarinaku, chikoku wa mitomenai.)",
            "meaning": "Regardless of the reason, lateness is not accepted."
        },
        {
            "front": "～もかまわず",
            "reading": "Mo kamawazu",
            "type": "N2 Grammar",
            "back": "Without caring about",
            "example": "人目もかまわず泣いた。\n(Hitome mo kamawazu naita.)",
            "meaning": "I cried without caring about public gaze."
        },
        {
            "front": "～はともかく",
            "reading": "Wa tomokaku",
            "type": "N2 Grammar",
            "back": "Setting aside / Anyway",
            "example": "味はともかく、値段は安い。\n(Aji wa tomokaku, nedan wa yasui.)",
            "meaning": "Setting aside the taste, the price is cheap."
        },
        {
            "front": "～はさておき",
            "reading": "Wa sateoki",
            "type": "N2 Grammar",
            "back": "Setting aside",
            "example": "冗談はさておき、本題に入りましょう。\n(Joudan wa sateoki, hondai ni hairimashou.)",
            "meaning": "Jokes aside, let's get to the main topic."
        },
        {
            "front": "～わけがない",
            "reading": "Wake ga nai",
            "type": "N2 Grammar",
            "back": "Impossible that...",
            "example": "彼が犯人のわけがない。\n(Kare ga hannin no wake ga nai.)",
            "meaning": "It's impossible that he is the culprit."
        },
        {
            "front": "～どころではない",
            "reading": "Dokoro dewa nai",
            "type": "N2 Grammar",
            "back": "No time/room for...",
            "example": "忙しくて、旅行どころではない。\n(Isogashikute, ryokou dokoro dewa nai.)",
            "meaning": "I'm so busy, this is no time for a trip."
        },
        {
            "front": "～どころか",
            "reading": "Dokoro ka",
            "type": "N2 Grammar",
            "back": "Far from...",
            "example": "彼は漢字どころか、ひらがなも書けない。\n(Kare wa kanji dokoro ka, hiragana mo kakenai.)",
            "meaning": "Far from Kanji, he can't even write Hiragana."
        },
        {
            "front": "～ものか",
            "reading": "Mono ka",
            "type": "N2 Grammar",
            "back": "Definitely not (Strong denial)",
            "example": "二度と行くものか。\n(Nido to iku mono ka.)",
            "meaning": "I will definitely never go again."
        },
        {
            "front": "～とか",
            "reading": "Toka",
            "type": "N2 Grammar",
            "back": "I heard that...",
            "example": "彼は来月結婚するとか。\n(Kare wa raigetsu kekkon suru toka.)",
            "meaning": "I heard he is getting married next month."
        },
        {
            "front": "～ということだ",
            "reading": "To iu koto da",
            "type": "N2 Grammar",
            "back": "It means / I heard",
            "example": "試験は来週だということです。\n(Shiken wa raishuu da to iu koto desu.)",
            "meaning": "I heard the exam is next week."
        },
        {
            "front": "～からには",
            "reading": "Kara ni wa",
            "type": "N2 Grammar",
            "back": "Since / Now that",
            "example": "約束したからには、守らなければならない。\n(Yakusoku shita kara ni wa, mamoranakereba naranai.)",
            "meaning": "Since I promised, I must keep it."
        },
        {
            "front": "～以上（は）",
            "reading": "Ijou (wa)",
            "type": "N2 Grammar",
            "back": "Since / Now that",
            "example": "学生である以上、勉強すべきだ。\n(Gakusei de aru ijou, benkyou subeki da.)",
            "meaning": "Since you are a student, you should study."
        },
        {
            "front": "～上は",
            "reading": "Ue wa",
            "type": "N2 Grammar",
            "back": "Since / Now that (Formal)",
            "example": "こうなった上は、やるしかない。\n(Kou natta ue wa, yaru shika nai.)",
            "meaning": "Now that it's come to this, I have no choice but to do it."
        },
        {
            "front": "～ものだから",
            "reading": "Mono dakara",
            "type": "N2 Grammar",
            "back": "Because (Reason/Excuse)",
            "example": "電車が遅れたものだから、遅刻しました。\n(Densha ga okureta mono dakara, chikoku shimashita.)",
            "meaning": "Because the train was late, I was late."
        },
        {
            "front": "～あまり",
            "reading": "Amari",
            "type": "N2 Grammar",
            "back": "So much that...",
            "example": "驚きのあまり、声が出なかった。\n(Odoroki no amari, koe ga denakatta.)",
            "meaning": "I was so surprised that I couldn't make a sound."
        },
        {
            "front": "～につき",
            "reading": "Ni tsuki",
            "type": "N2 Grammar",
            "back": "Due to (Formal)",
            "example": "工事中につき、立ち入り禁止。\n(Koujichuu ni tsuki, tachiiri kinshi.)",
            "meaning": "Due to construction, entry is forbidden."
        },
        {
            "front": "～ことだし",
            "reading": "Koto da shi",
            "type": "N2 Grammar",
            "back": "Since (among other reasons)",
            "example": "天気もいいことだし、散歩に行こう。\n(Tenki mo ii koto da shi, sanpo ni ikou.)",
            "meaning": "Since the weather is nice (among other things), let's go for a walk."
        },
        {
            "front": "～だけに",
            "reading": "Dake ni",
            "type": "N2 Grammar",
            "back": "Precisely because",
            "example": "期待していただけに、がっかりした。\n(Kitai shite ita dake ni, gakkari shita.)",
            "meaning": "Precisely because I expected a lot, I was disappointed."
        },
        {
            "front": "～ばかりに",
            "reading": "Bakari ni",
            "type": "N2 Grammar",
            "back": "Simply because (Negative result)",
            "example": "お金がないばかりに、進学できなかった。\n(Okane ga nai bakari ni, shingaku dekinakatta.)",
            "meaning": "Simply because I had no money, I couldn't go to college."
        },
        {
            "front": "～からといって",
            "reading": "Kara to itte",
            "type": "N2 Grammar",
            "back": "Just because...",
            "example": "寒いからといって、家の中にばかりいてはいけない。\n(Samui kara to itte, ie no naka ni bakari ite wa ikenai.)",
            "meaning": "Just because it's cold, you shouldn't stay inside all the time."
        },
        {
            "front": "～としても",
            "reading": "To shitemo",
            "type": "N2 Grammar",
            "back": "Even if assuming...",
            "example": "仮にそれが事実だとしても、許せない。\n(Kari ni sore ga jijitsu da to shitemo, yurusenai.)",
            "meaning": "Even assuming that is the truth, I can't forgive it."
        },
        {
            "front": "～ないことには",
            "reading": "Nai koto ni wa",
            "type": "N2 Grammar",
            "back": "Unless...",
            "example": "やってみないことには、できるかどうかわからない。\n(Yatte minai koto ni wa, dekiru ka douka wakaranai.)",
            "meaning": "Unless I try, I don't know if I can do it."
        },
        {
            "front": "～ものなら",
            "reading": "Mono nara",
            "type": "N2 Grammar",
            "back": "If I could...",
            "example": "戻れるものなら、過去に戻りたい。\n(Modoreru mono nara, kako ni modoritai.)",
            "meaning": "If I could return, I'd want to return to the past."
        },
        {
            "front": "～ようものなら",
            "reading": "You mono nara",
            "type": "N2 Grammar",
            "back": "If one were to... (Bad result)",
            "example": "遅刻しようものなら、先生に怒られる。\n(Chikoku shiyou mono nara, sensei ni okorareru.)",
            "meaning": "If I were to be late, the teacher would get angry."
        },
        {
            "front": "～ないことはない",
            "reading": "Nai koto wa nai",
            "type": "N2 Grammar",
            "back": "It's not impossible to...",
            "example": "走れば間に合わないことはない。\n(Hashireba maniawanai koto wa nai.)",
            "meaning": "It's not impossible to make it if I run."
        },
        {
            "front": "～まい",
            "reading": "Mai",
            "type": "N2 Grammar",
            "back": "Will not / Intend not to",
            "example": "二度とあんな店には行くまい。\n(Nido to anna mise ni wa iku mai.)",
            "meaning": "I will never go to that kind of shop again."
        },
        {
            "front": "～ものがある",
            "reading": "Mono ga aru",
            "type": "N2 Grammar",
            "back": "There is something... (Feeling)",
            "example": "彼の実力には見るものがある。\n(Kare no jitsuryoku ni wa miru mono ga aru.)",
            "meaning": "There is something impressive about his ability."
        },
        {
            "front": "～ことだ",
            "reading": "Koto da",
            "type": "N2 Grammar",
            "back": "Should (Advice)",
            "example": "健康になりたければ、運動することだ。\n(Kenkou ni naritakereba, undou suru koto da.)",
            "meaning": "If you want to be healthy, you should exercise."
        },
    ]
}