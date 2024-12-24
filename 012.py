# author: naestech
# day: 12
# link: https://adventofcode.com/2024/day/12

puzzleInput = """
XXXXXUUUNNNNNNNNNNNNNNNNQQQQQQQQQJJJJJJJJJJJJJJJJCCCAAAAAAAAAAAAOVVVVVVVVVVVVVVVVVVLLLLLLLLKKKKGGGGGGGGGGGGGGGGGGGKKKKKKKKKKKKKKKKKKKKKKKKKK
XXXUXXUUUUNNNNNNNNNDNNDGQQQQQQQQQJJJJJJJJJJJJJJJJJJCCCAAAAAAAAAYVVZVVVVVVVVVVVVVVVVVLLLLLLLLKKKGGGGGGGGGGGGGGGGGGGKKKKKKKKKKKKJKKKKKKKKKKKKK
XUUUUUUUUUENNNNNNNNNNNDCCCCCCCCQQJJEJJJJJJJJJJJJJJCCAAAAAAAAAAAZZZZVVZVVVVVVVVVVVVVVLLLLLLLLKGGGGGGGGGGGGGGGGGGGGKKKKKKKKKKKKAKKKKKKKKKKKKKK
UUUUUUUUUUUYNNNNNNNNNNNCCCCCCCCQJJJJJJJJJJJJJJJJJJCAAAAAAAAAAAAZZZVVVVVVVVVVVVVVVVVVLLLLLLLLLLZGGGGGGGGGGLLGGGGGGKKKKKKKKKKAAAAKKKKKKKKKKKKG
UUUUUUUUUKKNNNNNNNNNNZZCCCCCCCCJJJJJJJJJJJDDJJJJJJCAAAAAAAAAAAAHZZVVVVVVVVVVVVVFVVMVVLLLLLLLLLMAAAGGGGLLGLLGGGGGGGGGKKKKKKKAAAAKKKKKKKKKKKKG
UUUUUUUUUKUANNNNNNNNNZZCCCCCCCCQJJJJJJJJJDDDDJJJJJCJJAAAAAAAAAAHZZVVVVVVVVVVVVVVVVMMLLLLLLLGLLMAAAAGGGLLGLLLLLLLGGGGKKKKKKKAAAAKKKKKKKKKKKKG
UUUUUUUUUUUUUNNNNNNNNZZCCCCCCCCQQQQJJDDDDDDDDDJJJJJJAAAAAAAAAAAZZZVVVVVVVVVVVVVVVVMMLLLLLLGGGMMAALGGGLLLLLLLLLLLGGGKRKKKKKKAPPPPPKKKKKKKKKKG
UUUUUUUUUUUUNNNNNNNNNZZCCCCCCCCCCCCCCCCCDDDDDDJJJJJJAAAAAAAAZZZZZZZVVVVVVVVVVVVVVVMMMLLLLLGGGMAAALLLLLLLLLLLLLLLKKKKKKKKKKKPPPPPKKKKKKKKKGGG
UUUUUUUUUUUZNYNNSNNNNZZCCCCCCCCCCCCCCCCCDDDDDDEJJJJJAAAAAAAAAZZZZZZVVVVVVVVVVVVVVVMMMLLLLLGMMMMMALJLLLLLLLLLLLLLKKKKKKKOKPKPPPPKKKKKKGGKGGGG
UUUUUUUUUUUZNSNZZZZZZZZCCCCCCCCCCCCCCCCCDDDDDDJJJJJAAAAAAAQAAAZZZZZZZMFMMMMMMMMMMMMMMMLLLGGMMMMMMMLLLLLLLLLLLLLLKKKKKKKKPPPPPPPPKKPKKGGKGGGG
UUUUUUUUUUMSSSZZZZZZZZZCCCCCCCCCCCCCCCCCDDDDDJJJJJJAAAAAAAQZZZZZZZZZZFFMFMMMMMMMMFFMMLLLLGAMMMMMMMMMLLLLLLLLLLLLLKKKKKKPPPPPPPPPKKPKKGGGGGGG
UUUUUUUUUMMSSSZZZZZZZZZCCCCCCCCCCCCCCCCCDDDJJJJJJJJJAAJAAQQZZZZZZZZZZFFFFMMMMMMMMFIAMMAAAAAMMMMMMMMLLLLLLLLLLLLLLKFKKKKEPPPPPPPPPKPKGGGGGGGG
OOUUUUUUSSSSSSZZZZZZZZZCCCCCCCCCCCCCCCCCDDDJJJJJJJJJJJJAAQQNNNZZZZZZZFFFFFFFFFFFFFFAAAAAAAAMMMMMMMMXLLLLLLLLLLLLKKUUUUUPPPPPPPPPPPPPPPGGGGCC
OUUUUOUUUPSSSSZZZZZZZZZZZZZZZQQCCCCCCCCDDSDDCJJJJJJJJAAAAAQNZZZZZZZZZFFFFFFFHFFFFFFFAAAAAAAAMMMMMMCCCLCLLLLLLLLLLTUUUUUPPPPPPPPPPPPPPPPGGGCC
OOUGGGGUUSSSSZZZZZZZZZZXXXXJJJJJJCCCCCCDDSSCCJJJJJJJJAAAAANNNNZZZZZBPPFFFFFFFFFFFFFFAAAMAAAAAMMMMMMCCCCCLLLLLLLLLMMUUUPPPPPPPPPPPPPPPPPGGGCC
OGGGGGGLLLLSSZZZZZZZZZZXXXJJJJJJJCCCCCCSSSSSJJJJJJJJJJJAAANNNNNZZZNPPPPFFGPPFFFFFFFAAAAMAAMMAMMMMMMCCCCCCOOOLLLLLLMMUUUPPPPPPPPPPZPPPPCCCCCC
OGZZGGGLLLLLSZZZSSSXXXXXXXXXJJJJJCCCCCCSSSSWJJJJJJJJJJPJANNNNNZZZNNPPPPPFPPPPPFFFVHHAAMMMMMMMMMCMCICCCCCCCCOOLTOOLMMMUUPPPPPPPZPPZPCCICCCCCP
OGGGGGGGGLLSSZZZSSSXXXXXXXXXJJJJJCCCCCCSSSSSJJJJJJJJJJJJNNNNNZZZZZNNPPPPPPPPPPPVVVVVMMMMMMMMMMCCCCCCCCCCCOOOOOOOOOMMUUUUPPPPPZZZZZZCCCCCCCCP
SGGGGGGGGLSSSZZZSXXXXXXXXXXJJJJJJCCCCCCJSSSRJJJJJJJNJJJNNNNNNNZZZNNPPPPPPPPPPPPVVVVVMVMMMMMMMCCWCCCCCCCCCCCOOOOOOOOOUUUUPPPPPNNZZZCCCCCCCCCP
SGGGGGGGSSSSSZZZSUXXXXXXXJJJJIJJJCCCCCCJWWWWJJJJJJJJLJJNNNNNNNNNNNNNPPPPPPPPPPPVVVVVVVMMMMMCCCCCCCCCCCCCCCCCCOOOOOOOUUUPPPPPPNNNNCCCCCCCCCPP
SSSGGGGGGGVSSSSSUUXXXXXXXJJJIIJJJCCCCCCWWWWWJJJJJJJJJJNNFNNNNNNNNPPPPPPPPPPPPPVVVVVVVMMMMMMMRRRRCCCCCCCCCCCCCOOOOUOOUUUPUTNNNNNNNCCCCCCCPCPP
SSSSZGGGGGRYSSSRXXXXXXXXXXJJJJJJJJJJJJWWWWWWWJJAJJJJJNNFFNNNNNNNNPPPPPPPPPPPPPVVVVVVVMMMMMMMMRRRCCCCCCCCCCCCCOOOOUUUUUUUUTNNNNNNNNCCCCCCPPPP
SSSZZGHGGGRRJSRRGXXXXXXXXXXJJSSJJJJJJJWWWWWWWJJAJJJJJJFFNNNNNNNNNNPPPPPPPPPPPPPVVVVVVMMMMMMMRRRRRCCCCCCCCCCCCOOOUUUUUUUUUTTTTTNNNNNCCCCPPPPP
SSQQZZGGGGRRRRRRRXXXXXXXXRXRRJJJJJJJJWWWWWWWWWJJJJJJJJJFFFFFFNNANNNPPPPPPPPPVVVVVVVVVMMMMMRRRRRRRCLLCLLLLLCCCCOOOUUUUUUUTTTTTTNNPPNCCPPPPPPP
QQQQQZZGGGRRRRRRRXXXXXRRRRRRRRJJJJJJWWWWWWWWWWWWWJJJJFFFFFFFFAAAAAPPPPPPPPPVVVVVVVVVVVVDMMMRRRRRRRLLLLLLLLCLCLOOUUUUUUUUUUUUUUUPPPPPPPPPPPPP
QQQQZZQQZRRRRRRRRRRRRRRRRRRRRRRJJJJJSWWWWWWWWWWWWWJJJFFFFFFFFAAAAAPPPPPPPPVVVVVVVVVVVVDDMDRRRRRRRRXXXXLLLLLLLLUOUUUUUUUUUUUUUUUPXPPPPPPPPPPP
QQQQQQQQQRRRRRRRRRRRRRRRRRRRRRRRJVJSSWWWWWWWWWWWWWFFFFFFFSFAAAAAAAPAPPPPPPVVVVVVVVVVDVDDDDRRRRRRRRLXLLLLLLLLLLUUUUUUUUUUUUUUUUUUXXPPPPPPPPPP
QQQQQQQQQRRRRRRPRRRRRRRRRRRRRRRRVVWWWZWWWWWWWWWWWWJFFFFFFFAAAAAAAAAAVPPPPPVVVVVVVVVVDDDDDDHRRRRRRELLLLLLLLLLLSSUUUUUUKUUUUUUUUKUXPPPPPPPPPPP
QQQQQDQDGRSPRPPPPRRRRRRRRRRRRRRRRVVVWWWWWWWWFFJJJJJJJJJFFAAAAAAAAAAAAAPPVVVVVVVVVVVDDDDDDRRRRRRRRRRRLLLLLLLLLLSUUUUUKKKUUKKKUUKUUPPPPPPPPPPP
QDDQDDQDGGPPPPPPPRRRRRRRRRRRRRRRRVVWWWWWWWWWDFFJJFFFFJJFFAAAAAAAAAAAAAAPVVVDDVVVVVDDDDDDDRRRRRRRRRRRLLLLLLLLLSSSUUSUUKKKKKKKKKKUYYPPPPPPPPPP
QDDDDDDDGPPPPPPPPRRRRRRRRRRRRRRRRVVVVWWWWWQQFFFJFFFFFFFFFAAAAAAAAAAAAABBHDDDDVVDVDDDDDDDDRFRRRRRRRRLLLLLLLLLLLSSSSSSKKKKKKKXXDYYYYYPPPPPPPPP
DDDDDDDGGGPWPPPPPPPPRRRRRRRRRRRRRRVVVWWQQWQQQFFJFFFFFFFFAAAAAAAAAAAAAUBBHBBBDDDDDDDDDDDDDDRRRRRRRRRLLLLLLLLLLSSSSSSSKKKKKKKKXDYYYYYPYPPPPPPP
DDDDDDDDDGPWPPPPPPPPPRRRRRRRRRRRRRVRWWWWQQQQQFFFFFFFFFZFAAAAAAAAAAAAABBBBBBBBBBDDDDDDDDDDDDDYRRRRRRRLLLLLLLJLLSSSSSSKKKKKKKKXDDDYYYYYYYPPPKP
DDDDDDDDDDDDPPPPPPPPPRRRRRRRRRRRRRRRRSSQQQFFFFFFFFKKFFFHHHAAAAAAAAAAABBBBBBBBBBBDDDDDDDDDDDDRRRRRRLLLLLLLLSSSSSSSSSUKKKKKKKKDDDDYYYYYYYPPPPY
DDDDDDDDDDAAPPPPPPPPPRRRRRRRRRRRRRRRSSQQQEEGFFFFHHFFFFHHHHAAAAAAAAABBBBBBBBBBBBBDDDDDDDDDDDDRRRRRRRLLLHHLLLSSSSSSSSSKKKKKKGGDDDDDDYYYYYPPPYY
DDDDDDDDDDAAAPPPPPPPPPRRRNNRRRRRRRRSSQQQQEEEFFFHHHHHFHHHHHHHAAAABBBBBBBBBBBBBBBBBDDDDDDDDDRRRRRRRRRLLLHHHLSSSSSSSSSSKKKKKKDDDDDDDDYYYYYYYYYY
DDDDDDDDDDDAAPPPPPPPPRRRNNNRRRRRRRQQSQQQQEEEFFFHHHHHHHHHHAAAABBBBBBSSBBBBBBBBBBBBDDDDDJJJJDDRRRRRRRHLLHLLLLSSSSSSSSKKKKKKKUDDCDDDDYYYYYYYYYY
DDDDDDDDDDAAAPPPPPIIIRRRRNRRRRRRRRQQQQQQQEEEFFFHHHHHHHHHHHHAABBBBBBBBYBTBBBBBKBRBDDDDJJMMJJDRRSSRRRHLHHHHHLQQQSSSSSSKKKKKKDDDDDDDYYYYYYYYYYY
DDDDDDDDDDDAAPPPPPPQIIIRRRRRRRRRRQQQQQQNNQEHHFFFHHHHHHHHHHHHHBBBBBBBYYYBBBBBBBBRRRRDDJJJJJJRRRRRRRHHHHHHJJLQQQSQQSSSSSSKKKDDDDDDDYYYYYYYYYYY
DDDDDDDDNNDQAPPPPPQQQIIRQRRRRRRRRRQQQQQQNNSHHFHHHHHHHHHHHHHHHBDBBBYYYYYBBBBBBRRRRTDDJJJJJJJTRRRRRRHHHHHHHQQQQQQQQSSSSSSSDDDDDDDDDYYYYYYYYYYY
DDDDDDDDNNNQAPPNPPPQQIIQQHRRRRRRRRQQQQQQQNSHHHHHHHHHHHHHHHHEHBDDGBBGWWWBBBBBBBRRRTTTTJJJTTTTRHHHHHHHHHHHHHQQQQQQQSSSSSSSSSDDDDDDYYYYYMYYMYYY
DDDDDDDNNNNQQQPPQQQQQQQQQHHHHHXXXXXQQQQQQNNNHHXXHHHHHHHRRHRRRRDDGBBGWWWWBBBWWBRRRTTTTTTTTTTTTHHHHHHHHHHHHQQQQQQQQSJJSSSSSSSDDDDDYYMYMMMMMMYM
DDDIIDDDDNNQQQQPQQQQQQQQQQHHHXXXXXQQQQQQQNNEEEHHHHHHHHHRRRRRRRGGGGGGWEWWWBBWWBWWWWRTTTTTTTTTHHHHHHHHFHHLQQQQQQQQQQJJJSSSSDSDIIDDYYMMMMMMMMYM
DDDDDDDHNNNNQQQQQQQQQQQQHHHHXFXXXXXXXNNNNNNNNHHHHHHHHHHRRRRRRUUGGGGGGGGWWWWWWWWWWWRRTTTTTTTHHHHHHHHFFHGQQQQQQQQQJJJJJJSSSDDDIIYYYYMMMMMMMMMM
QDDDDNNNNNNNNQQQQQQQZZQQQHHXXXXXXXXXXNUNNNNNNNNPNYYHHHRRRRRRRRUGGGGGGGGWWWWWWWWWWWWWTTTTCTTTHHHHHHHHHGGGQQQQQQQJJJJJVJWSWKKKYIYYYYYMMMMMMMMM
QDDQNNNNNNNNNNNQQQQQZZLQHHXXXXXXXXXNNNNNNNNNNNNNNNYHHHRRRRRRRRRGGGGGGGWWWWWWWCWWWWCWTTTTCCTCHHHHHHGGHGGQQQQQQQJJJJJJVWWSWKKKYYYYYYYYMMMMMMMM
QQQQNNNNNNNNNQQQQQQQZZZZZXXXXXXXXXTNNNNNNNNNNNNNNNNNHHRRRRRRRGGGGGGGGGGWWWWCCCWWWCCQQCCCCCCCHVHHHHHGGGGQQQQQQQJJJJJJJWWWWWKKKQYYYYMMMMMMMMMM
QQQNNNNNNNNNNNQQQQQQQZZZZLXUWXXXXXNNNNNNNNNNNNNNNNNKKHRRRRRRRGGGGGGGGGGWWWCCCCCCCCCQQQCCCCCCVVVVVDDGGGQQQQQQQQJJJJJJJWWWWWLKLQQYQQNMMMMMMMMM
QQQQNNNNNNNNNNQQQZZZZZZZZZOWWXWXXWNNWNNNNNNNNNNNKKKKKKARRRRRRGGGGGGGGGGGWWWCCNCCCCCCQCCCCCCCCVVVVDGGGGKOQOKKQJJJJJJJWWWWWWLLLQQQQMMMMMMMMMMM
QQQNNNNNNNNNNNNQZZZZZZZZZZZZWWWWWWNWWWNNNNNNNNNNKKKKKKARRRRKKKKGGGGGGGGGGWWWCCCCCCCCCCCCCCCCCCVDDDDDGGKOOOKKQQJJJJJWWWWWWLLLLMQQQMMMMMMMMMMU
LQQQNNNNNNNNNNQQZZZZZZZZZTTTTWTWWWWWWWNNNNNNNNNNNKKKKKARRRRKKKKGGGGGGGGGWWWUCRCCCCCCCCCCCCCCJDDDDDDGGKKKKKKKKKJJJJJWWWWWWMLLLMQQTMMMMMMMMMMM
LNNNNNNNNNNNNQQQZZZZZZZZTTTTTWTWWWWWWWNNNNNNNNNNKKKKKKARRRRDKKKKKKGGGGGGWGUUCCCCCCCCCCCCCCCUCCDDDDDGDKKKKKKKKKJJJJTTTWWWMMMMMMMMMMMMMMMMMMMM
LLNNNNNNNNNNNNQQZZZZZZZZTTTTTTTTWWWWWWWNNNNNNNNNNKKKKKKGGRRDDKKKKKKKKGGGGGUUUUCCCCCCCCCCCCCCCCDDDDDDDNKKKKKKKKKKJYYTTTTMMTTMMMMMMMMMMMMMMMMM
LLLNTNNNNNTNQNQQCCZZZZZTTTTTTTTTWWWWWWWNNNNNNNNNNKNNKKKGGRRRDDKKKKKKKUGGGUUUUUCCCCCCCCCCCCCCCCDDDDDNNNNNKKKKKKKKBYYTTTTMTTTTTTMMMMMMMMMMMMMM
LLLLTTNNNNTTQQQQQQZZZZTTNTTTTTTWWWWWWNNNNNNNNNNNNGGGGKGGGGGCDKKKKKKKKUGGUUUUUCCCCCCCCCCCCCCCCCDDDDDDNNNNKKKKKKKKKYYTTTTTTTTTMMMMMMMMMMMMMMMM
LLLLLTNNNNTTQTQQTTTTTTTTTTTTTTTWWWWWWWNNNNNNNNNNNNGGGGGGGCCCCCKKKKKKUUUUUUUVUCCCCCCCCCCCLCCCCCDDDDDDDDDDKKKKKKKKYYYTTTTTTTTTNNNMMMMMMMKKMMMM
LLLLLTNNNNTTTTQTTTTTTTTTGTTTTTKKKWKKKWNNNNNNNNNNNNNGGGGGGGCCCCKKKKKKUUUUUUUVVCCCCCCCCCCLLCEECCDDDDDDDDDKKKKKKKYYYYYTTTTTTTTNNNNNKKKKKKKKKKKK
LLLLLTTTNNTTTHBTHTTTTTTTGTTTTKKKKKKKKWNNNNNNNNNNNNNGGGGGGGXCCCCKKKKKUUUUUUZVVCCCCCLCCLLLLLLEDDDDDDDDDDDKKKKKKKYYYYYTTTTTTTTTENNNKKKKKKKKKKKK
LLLLLLLTTTTHHHHHHHTTTTTGGTGKKKKKKKKKKWWNNNNNNNNNNNGGGGGGGGCCCCKKKBBKUVVVVZZVCCCCFFLLLLLALZBDDDDDDDDDDDDKKKKKKKYYYYYTTTTTTTNNNNNNNKKKKKKKKKKK
TTTTTTLTTTHHHHHHHHHTTTTTGGGKKKKKKKKKKWWGNNGNNNNNNNNNGGGGGGCCCCCKKKCCUVVVVVVVVVCFFFFLLLLAZZZZZDDDDDDDKKKKKKKKYYYYYYYYTTTTTTNNNNNNNKKPKKKKKKKK
TTTITTTTTTHHHHHHHHTTTTTTGGKKKKKKKKKKKGGGGGGNNNNNNNNNNGGGGCCCCCCCCCCCUUUVVVVVVVVVVFFLLLLAAZZZZZDVDDDKKKKKKYYYYYYMYYTTTYTTTTTNNNNNNNKKKKKCKKKN
TTIIIIIIIIIIIIIHHHTTTTTTTACKPKKKKKKPKGGGGGGGNNNNNNNNNGGGGCCCCCCCCCCCCUUVVVVVVVVVVVRHHLLLZZZZZZZZDKKKKKKKKYYYYYYMMYYYYYYTTTNNNNNNNNNKKKKKKKNN
TTTIIIIIIIIIIHHHHHHTTTTTAAKKKKKKKKPPPGGGGGGGGGNGGNNNNGGGXCCCCCCCCCCCCCCVVVVVVVVVVVRRRRRLLZZZZZZZDZZZKKMMKMMYMMMMMMYYYYYYYYNNNNNNNNNNNNKKNNNN
TTIIIIIIIIIIIIPHAATTTTTAAAUKKKKKTPPPGLLGGGGGGGGGNNNKKKGXXXKCCCCCCCCCCVVVVVVVVVVRRRRRREEZZZZZZZZZZZZZKKMMMMMMMMMMMMYYYYYYYYNNNNNNNNNNNNNNNNNN
TTIIIIIIIIIIIIIIAAATTTAAAUUUKKTTTTPPGGGGGGGGGGGSKKKKKKKXXXCCCCCCCCCCVVVVVVVVVVVVRRRRRRRZZZZZZZZZZZZZKKMMMMMMMMMMMYYYYYYYYYYNNNNNNNNNNNNNNNNN
IIIIIIIIEEEIIIIIAAAAAAAAUOUUKKJTTTPPGGGGGGGGGGGSKKKKKKXXXXCCUCCCCCCCVVVVVVVVVVVVRRRRRRRZZZZZZZZZZZZZKMMMMMMMMMMMMMYYYYYYYYYYNANNNNNNNNNNNNNN
EERIIEEEEEBEIIIAAAAAAAUUUUUUUUJJTTTJJJGGGGGGGGGGGKKKKKXXXXXXCCCCCCCCVVVVVVVVVVRRRRRRFRRZEZZZZZZZZZZZKKKMMMMMMMMMMMYYYYYYYZZZZZZZNNNNNNNNNNXX
EEEIIEEEEEEEEEEEEAAAAUUUUWWNUUJJTTTTJGGGGGGGGGGGGKKKKXXQXXXQCCCCCQCCVVVVVVVVVRJJRRRRRRRZEEEZZZZZZZZKKKMMMMMMMMMMMMYYYYYTTZZZZZZZNNNNANTNNXXX
EEECEEEEEYEEEEEAEAAAAUULLWWWWLTTTTTTTGGGGGGGGGGGGKKKKKKQXQQQCCQCQQCCVVVVVVVVRRRRRRRRRRRRERRZZZZUZKKKKKHMMMMMMMMMPMMTTTTTTZZZZZZZAANNATTXXXXR
EEECEEEEEEEEEEJAAAAAAAUOOOOWWLLTTTTVGGGGGGGGGGGKKKKKKKKQQQQQQQQQQQCCCVVVVVKKRRRRRRRRRRRRRRIPBZZUZKKKKHHMMMMMMMMMMTTTTTTTTZZZZZZZAANNAARRRRRR
EEEEEEEEEEEEEEAAAAAAAAUOOOOWWLLLQUTVGGGGGGGGGGKKKKKKKKKQQQQQQQQQQQQCVVVVVVKKKRRRRRRRRRRRRIIPPPPPPKKKKHHHHMMMMMMMMMTTTTTTTZZZZZZZAAANARRRRRRR
EEEEEEEEEEEEEEEVAAAAAAPOOOOLLLLQQQLQGGGKGKKKKGTTKKKKKKKQQQQQQQQQKQQCCVVVVVKKKRRRRRRRRRRRRRPPPPPLPKKHHHHHHMMMMMMMMMTTTTTTTTOAZZZZAAAAAARRRRRR
EEIEEEEEEEEEEEEEAAAAAAOOOLLLLQQQQQQQGGQKKKKKKEETTKKKKKQQQQQQQKKKKQQQVVVVVKKKKRRRRRRRRRRRRPPPPPPPPHHHHHHHHMMMMMMOMOTTTTTTTTHAZZZZAHAAARRRRRRR
CEIEEEEEEEEEEEEEAAAAAAALLLLLLQQQQQQQGGQKKKKKKEETEKKWWKQQQQQQKKKKKKQKKVVKKKKKKKKKKKKKRRRRRPPPPPPPPPHHHHHHHHMMMMMOOOOTTTTTTCCCCCCCCCAAARRRRRRR
BBBBEEEEEEEEEEAAAAAAAAAALLLQQQQQQQQQQQQQQQQKKEETEEWWWQQQQQQKKKKKKMKKKVVKKKKKKKKKKKKKRBRRHVHHPPPPPPHHHHHHHMMMMMMMMMTTTTTTTCCCCCCCCCAAAARRRRRR
BBBEEEWEEEEEEEEEAAAAAAAALLLQQQQQQQQQQQQQQKKKKEEEEEWWWWWQQQQKKKKKKKKKKKKKKKKKKKKKKKKKRBKRHHHHPPPPPPRHHHHHRQMIMMMMMQTTTTTTTCCCCCCCCCHRRRRRRRRR
BBBBEEEEEEEEAAAEAAAAAAAALLQQQQQQQQQQQQQQKKEEEEEEEEWWWWWWWKKKKKKKKKKKKKNKKKKKKKKKKKKKKKKRHHHHPPPPPPPHHHHHQQVMMMMPPTTTTTTTTCCCCCCCCCHRRRRRRRRR
BBBBEEHEEEEEAAAAAAAAAAALLLSZQQQQQQQQQQQQQQEEEEEENEEWWWWWKKKKKKKKKKKKKNNKNNCKKKKCKKKKKKKHHHHHPPPPPPPHHHHHQQQLMMMMPPTTTTTTTCCCCCCCCCOORRRRRRRR
BBHHHHHHEAAEAAAAAAAAAAAALLSZQQQQQQQQQQQQQQEEEEEEEEEEHWWWKKKKKKKKKKKKKKNKNNCCCCCCCCKKKKKKHHHHHHPPPPDHHSSHQQLLLLMPPPTTTTTTTCCCCCCCCCOORRRRRRRR
BBHHHHAHEAAAAAAAAAAAAAAAASSZQQQQQQQQQQQQQUEUEEEEEEEHHWWWWEKKKKKKKKKKKKNNNNCCCCCCCCKKKKKKHHHNNHPPPPPHHSSQQQLLMMMPPPTTTTTTTCCCCCCCCCOOOOORRRRF
BBHHHHAAAAAAASSAAAAAAAAAYSSSSQQQQQQQQQQQUUUUUEEEBEHHEEEEEEEKKKKKKKKKKKKKNNCCCCCCCCKKKKHHHHHNNNXPPPPHHSSQQLLMMMMPMPPTTTTTTOOOOHHOOOOOOOOORRRR
BBHHHHHHAAAASSSAAAAAAAYYYYSSSSSQQQQQQQQQQUUBBBBBBBHHHHEEEEEKKKKKKKKKKKKKNCCCCCCCCCCKKHHHHHNNNXXRRPXHSSSQQLMMMMMMMPPTTTTSZZOOOOOOOOOOOOOOORDD
BBHHHHHJJAAAASSSSSSSYAAYYYYSSSQQQQQQQRQQQUUUUUBBBBBHHHEEEEEEEEEKKKKOOZCZNCCCCCCCCCCKKKHHHHNNNXXXXXXXSSSMSSMMMMMMMPPTTTTTZZOOOOOOCOOOOOOOOOOD
HJHHHHJJJJAAASSSSSSSYYYYYYYYYYQQQRQQQRRRUUUUBBBBBBBBHHEEEEEEEXXXXXXXZZZZZCCCCCCCCCCCCHHHNNNNXXXXXXXSSSSSSMMMMMMMMWPTTTTZZZZOOOOOCOOOOOOOOOCO
HHHHHJJJJJSSSSSSSSSSYYYYYYYYYRRQRRRRRRRRUUUUBBBBBBBBBHHHEEEEEXXXXXXXZZZZZCCCCCCCCCCCCCHHHNNNRXXXXXSSSSSSSSMMMMMMWWPTTTTZMZZZOOCCCCOOOOOOOOOO
HHHHJJJJJJJSSSSSSSSSSYYYYYYYYRRRRRRRRRRRUUQUUBBBHHBBHHEEEEEEWXXXXXXXZZZZZCCCCCCCCCCCCCCCHPPNNXXXSSSSSSSSSSMMMMMMWWWTTTTTZZZZCCCCCCCCOOOOOUOU
HJJHJJJJJJJMSSSSSSSSSSYYYYYYYYRRRRRRRRRRRUQUUHHBHHBHHHHEEEWWWXXXXXXXZZZZZCCCCCCCCCCCCCYYCPPPPPSSSSSSSSSSSSMMMMMMWWMTTTTTZCCCCCCCCCCCOOUUUUUU
JJJJJJJJJJJJJSSSSSSSSSSYYYYYYYRRRRRRRRRRQQQQHHHHHHHHHHHEEEWWXXXXXXXXZZZZZCCCCCCCCCCCCCCCCPPPPPSSSSSSSSSSSMMMMMMMMMMMTTTTZCCCCCCCCCCCQCUUUUUU
JJJJJJJJJJJJJSSSSSSSIISYYYYYYYRRRRRRRRRRRPQQQHHHHHHHHHHEEHHWXXXXXXXXZZZZZKKNCCCCCCCCCCPPPPPPPPSSSSSSSSSSMMMMMMMMMMMMMTTTTCCCCCCCCCCCCCUUUUUU
JJJJJJJJJJJJJSSSSIIIIIIYYYYRRRRRRRRRRRRRRPPQPPHHHHHHHHHHEEHWXXXXXXXXZZZZKKKKKKCCCCCCCOPPPPPPPPPPSSSSSSSSMMMMMMMMMMMMMTTTTCCCCCCCCCCCCUUUUUUU
JJJJJJJJJJJPPPIIIIIIIIYYIIIRRRRRRRRRRRRCCPPPPHHHHHHHHHHHHHHHXXXXXXXXZZKKKKWKKKKCCCCCPPPPPPPPPPPASSSSSSSSSKMMMMMMMMMMMTTTTTCMCCCCCCCCCUUUUUUU
JJJJJJJJJJJQIIIAAAAAAAAIIEEEREBRRRRRRRRCCPCPCYHHHHHHHHHHHHHHXXXZQZZZZZKCCKKKKKKKKKCQQQQQQQQPPPPSSSSSSSSSMMMMMMMMUMMHHTTTTTTMMCHCCCFCUUUUUUUU
JJJJJJAAAAAAAAAAAAAAAAAAAAAARRBRRRRRRCCCCCCCCYHHHHHZHHHHHHHSXXXZZZZZZZKCCKKKKKKKKKWQQQQQQQQPPPPPSSSSSSSSSSMMMMMMMHHHHTTTTTTMMCHCCCUUUUUUUUUY
QJJJJJAAAAAAAAAAAAAAAAAAAAAABBBBBBBRRRRCCCCCBHHHZZHZZHHHHHMSXXXSZZZZZCCCKKKKKSKKWKWQQQQQQQQPCCPSSSSSSSSSSSMMHHHMHHHHHTTHTTTMHHHCFCUUUUUUUUUY
QJJJJJAAAAAAAAAAAAAAAAAAAAAABBBBBBBBRRRRCCCEBEHHZZZZHHHHHHMSXXXSSZZZCCCCCKKKKKKWWWWQQQQQQQQGCCCCSSSSSSSSSSHHHHHHHHHSSSTHTVVMHHUUFFFUUUUUYUUY
AAAAAAAAAAAAAAAAAAAAAAAACCBBBBBBBBBBRRRCCCCEEEEZZZZZHHHHHHMSXXXSSSZSSCCCCKKKKKKWWWWQQQQQQQQCCCCCCCESSSSSSSSHHHHHHHHSSSHHHHVVUUUUUFUUUUUYYUYY
AAAAAAAAAAAAAAAAAAAAAAAACCBBBBBBBBBBBRRRDCSBEBEEEZZZZZHHHHMSXXXSSSSSSSSCCKOKWKWWWWWQQQQQQQQQQQQCCEEEESVSSEHHHHHHHHHSSHHHHHVVUUUUUUUUUUUUYYYY
AAAAAAAAAAAAAAAAAAAAAAAACBBBBBBBBBBBBBRRDDBBBBBEEEXXZZHMMMMMSPPPSSSSWWWKKKKKWWWWWWQQQQQQQQQQQQQCEEEEEEEEEEHHHPHHHHHHHHHHHVVUUUUUUUUUUUUUYYYY
AAAAAAAAGGGGGGAAAAAAAAAABBBBBBBBBBTBTBDDDDBBBBBBBEHHHHHMPPPPPPPPSSSWWWWKWKKWWWWWWQQQQQQQQQQQQQQEEEEEEEEEEEHHHHHHHHHHHHHHHVVVVUUUUUUUUUUUYYYY
AAAAAAAAGGGGGGAAAAAAAAAABBBBBBBTTBTTTMDDDDBBBBBBBBHHHHMMPPPPPPPPPPPPPPWWWWWWWWWWWQQQQQQQQQQQQQQEEEEEEEEEEEEHHHHHHHHHHHHHVVVVVUUUUUUUUUHHYYYY
GGGGGGGGGGGGGGAAAAAAAAAAZBBBBBBTTBTTTTTDDDBRBBBBBBHHHMMMPPPPPPPPPPPPPPWWWWWWWWWCWQQQQQQQQQQQQQQPPPPEPPPEEEEXHHHHHHHUHVVHVVVVVVUUUUUUHHHHHHHY
GGGGGGGGGGGGGGAAAZZZZZZZZBBBTTTTTBTTTTTDDDDBBBBBBBHHHMMJPPPPPPPPPPPPPPKWWKKWWWCCCQQQQQQQQQQQQQQPPPPPPXXXXXEXXIXXXHUUVVVVVVVVVVUUUUUUUHHHHHHH
GGGGGGGGGGGGAAAAAZZZZZZZZBBBTTTTTTTTTTTTTDDBBBBBBBHHHHMJPPPPPPPPKKKKKKKWKKKKWWCCCQQQQQQQQQQQQQQPPPPPPXXXXXXXXXXXUUUUVVVVJJVVVVVVVUVUUHHHHHHH
GGGGGGGGGGGGAAAAAAAZZZZZZZRRRTTTTTTTTTTTLBBBBBBBBBBBMMMJPPPPPPPPKKKKKKKKKKCCCCCCCQQQQQQQQQQQQQQQQQQPPXXXXXXXXXXXXUUUUUVJJJJJJVJVVVVVVHHHHHHH
YYGGGGGGGGGGAAAAAAAZZZZZZZZRRTTTTTTTTTQTLBBBBBBBBBBMMMMJPPPPPPPPPKKKKKKKKKCCCCCCCQQQQQQQQBBQQQQQQQQPPXXXXXXXXXYXXUUUUJVJJJJJJJJVVVVVHHHHHHHH
YYGGHGGGGGGGAAAAAAZZZZZZZRRRTTTTTTTTTTQQBBBBBBBBBBBBBBMJPPPPPPPPPKKKKKKKKKCCCCCCCQQQQQQQQBBQQQQQQQQPPPXXXXXXXXXUUUUUUJPJJJJJJJVVVVVVVHHHHHHH
YYPGHGGGGGGHADDAAAWZZZZZZZZRRTTTTTTTTTQQBBBBBBBBBBBBEEMJPPPPPPPPPKKKKKKKKKCCCCCCCQQQQQQQQBBGGGPPPPPPPPXXXXXXXXXUUUUUUJJJJJJJJJVVVVVHHHHHHHHH
PPPPHHHHGGGHHHMAAAAZZZZZHHHTTTTTTTTTTTQQBBBBBBBBBBOBOEMJJJJJJJKKKKKKKKKKIICCCCCCCCCCCCCBBBBGGGGHPPPPPXXXXXXXXXXUUUUUJJJJJJJJJCJJVVVVHHHHHHHH
PPHHHHHHHGGHMMMMMMMZZZHHHHHTTTTTTTTTTTTTTTBBBBBBBOOOOOWJJJJJJJJJJJJJJKKKIICCCCCCCCCCCCCBBBBGGGGGWLLLLXXXXXXXXXXUUUJJJJJJJJJJTJJJJVUUUHHHHHHH
HHHHHHHHHHHHMMMMMMMMMZHHHHHHTTTTTTTTTTTTTEBBBBBBBBBOOOWJJJJJJJJJJJJCCCCCCCCCCCCCHCCCCCCBBBBGGGSLLLLLLXXXXXXXXXXXUUUUUJHHJJJJJJJJJJUUUUHHHHHH
HHHHHHHHHHHHSMMMMMMMMZHHHHHHHHTTTTTTTTEEEEEEBBBBBBBBOOWJJJJJJJJJJJJCCCCCCCCCCCCCCCCICCVBBBBLLLLKKKKKKKKKKKKKKKUUUUULLLHHJJJJJJJJUUUUUUHHHHHH
HHHHHHHHXHDHSMMMMMMMMMMHHHHUHTTTTTTTTTEEEEEEHHDBBBBDOOLWLLLLJJJJJJJCCCCCCCCCCCCCICCIMHHBBBBKLLLKKKKKKKKKKKKKKKXXULUULLJJJJJJJJJUUUUUUUUHHHHH
HXXXHHHHHHHHMZMMMMMMMMMHUUUUUWTTTTTTTTEEEHEEHDDBBDDDOLLLLLLLJJJJJJJCCCCCCCCCCCCIIIIIIKKBBBBKLLLKKKKKKKKKKKKKKKXILLLLLLLJJJJJJJUUUUUUUUUUUHHH
HHXQXXXXHHQQMMMMMMMMMMUHUUUUUWBTTTTTNBBEHHHHHDDDDDDDLLLLLLLLJJJJJJJCCCCCCCCCCCIIIIIIIKKKKLLLLLLKKKKKKKKKKKKKKKXIILIILLIJJJJJJUUUUUWWWUUUHHHH
HXXXXXNNHHQQQMMMMMMMMUUUUUUUUBBTTBBBBBBEEHHHHDDDDDSDLLLLLLLLJJJJJJJCCCCCCCCCCCIIIIIIIIKKLLLLLLLKKKKKKKKKKKKKKKXIIIIIIIIIJJJJJUUUUUWWWWWWWWWH
XXXXXXXNNNXQCCCCCMMMDUUBUUUUUUBBBBBBBBBEEHHHHHHHSDSDDDDLDLLCJJJJJJJCCCCCCCCCCCJIIIIIIIIKKKKLLLLKKKKKKKKKSUXIIIIIIIIIIIIIJJJJJJUUUWWWWWWWWWWH
XXXXXXXXXXXXCCCCCCCDDUUUUUUUUUBBBBBBBBBBEHHHHHHHSSSSDSSSDDNNJJJJJJJCCCCCCCCCCCJIIIIIIIIIKKKLLLLKKKKKKKKKRSIIIIIIIIIIIIIIIIJJJJUUUWWWWWWWWWHH
XXXXXXXXXXXXCCCCCCCIDUUUUUUUUUUBBBBBBBBBBDDHHHHSSSSSSSSSSDDDNNNNNNNCCCCCCCCCCCJIIIIIIIHIIKLLLLLLSSSSSSSSSSIIIIIIIIIIIIIIIDDJJDDUUUWWWWWWWWHH
XXXXXXXXXXXXOCCCCCCIDUUUUUUUUUUBBBBTTBBBBDDSSHSSSSSSSSSSSSSNNNNNNNNNCCCCCCCCCCJJJJIIIHHHHLLLLLLSSSSSSSSSSSIIIIIIIIIIIIIDIIDJJDDDUUWWWWWWWWWW
XXXXXXXXXXXXOOHHHHHIIIIUUUUUUUUUBBBNTBNBDDSSSSSSSSSSSSSSSPPPNNNNNNNNCCCCCCCCCCJJJHHHHHHHHLLLLLLSSSSSSSSSSSSIIIIIIIIIIIIDDIDDDDDDDDDWWWWWWWWW
XXXXXXXDXXXXXOHAHHHHIIUUUUUUUUUUBBBNNNNNSSSSSSSSSSSSSSSPPPPPNNNNNNNNCCCCCCCCCCJJJHHHHHHHHLLLLLLSKSSSSSSSSSSIIIIIIIIIIIIIDDDDDDDDDDWWWWWWWWWW
XXKXXXXDDXXOOOHHHHQHWIIUUUUUUUUUUGGGNNNNNNNSSSSSSSSSSQHQPPQQQNNNNNNNCCCCCCCCCCJJJJHHHHHHHHHLLLLLSSSSSSSSSIIIIININIIIIIIDDDDDDDDDDDDWWWWWWWWW
NXXTXXTTTXXOOOHHHHHHHIIUUUUUUUUUUGEGNNNNNNNSSSSSSSSSSQQQQPQQQQQQNNNNCCCCCCCJJJJJCJHHHHHHHLHLLLLLVVSSSSSSSIIIINNNNIIIIIIDDDDDDDDDDDDWWWWWWWWW
XXTTTTTTTTOOOOHHHHHHHIIIUUUWMUUUUJGGNNNNNNPPSSPSSSSSQQQQQQQQQQQQNNNNNNNJJJJJJJJJJJHHHHLLLLLLLLLLVVSSSSSYYYINNNNNNICIIIIDDDDDDDDDDDWWWWWWWWWW
TXTTTTTTTTTOFFFHHHHIIIIIUWWWWWWUWGGGNNNNNNPPSPPPSSSSQQQQQQQQQQQQQNNNNNNJJJJJJJJJJJHHHHLLLHLLLLLLSSSSSSSSSYNNNNNNNCCCCICDDQQQQPDDDDYWWWWWWWWW
TXTTTTTTTTTOIJFFHHHIIIIIWWWWWWWWWWWGWNNNPPPPPPPPSSSQQQQQQQQQQQQQNNNNNNNNJJJJJJJJJJJJHHHHLHHHLLHYYYSSSSSYYYNNNNNCCCCCCCCQQQQQQQDDDDDWWWWWWWWS
TTTTTTTTTTTTIFFFIHIIIIWWWWWWWWWWWWWWWNUPPPPPPPPPSSSQQQQQQQQQQQQNNNRNNNNNJJJJJJJJJJJHHHHHHHHHHLHYYYSSYSSYYYYYNNNCCCCCCCCCQQQQQQDDDIIWWWWWWWWS
TTTTTTTTTTTTIIIIIIIIIWWWWWWWWWWWWWWHHHUPPPPZPPPPPSSQQQQQQQQQQQQNNRRNRRRRFFFFJFFJJHHHHHHHHHHHHHHHYYYYYYYYYYYYYNNCCCCCCCQQQQQQQDDIIIIWJWWWXWWW
TTTTTTTTTTTTIIIIIIIIIWWWWWWWWWWWWWHHHHUPPPPPPPPPPPPPLLQQQQQQQQQQRRRRRRRRFFFFFFFFHHHHHHHHHHHHHHHHHYYYYYYYYYYYAANDCCCCCCCQQQQIIIIIIIIWJWWWXWWW
TTTTTTTTTTTTIIIIIIMMIUWWWWWWWWWWWWHHHHUPPPPPPPPPPPPPQQQQQQQQQQAARRRRRRRRRFFFFFHHHHHHHZZHHHHHHYYYYYYYYYYYYYYYAAAAACCCCCCCCHYYIYIITIIWWWIWWWRQ
TTTTTTTTTTTTTIIIIIMYWWWWWWWWWWWHHHHHHHHPPPPPPPPPPPPPQQQQQQQQQQAQRRRRRRRRRRFFHHHHHHHHZZZZHHHHHYEEYEYYYYYYYYAAAAAACCCCCCCCCCCYIYIITTIIIIIWIIRQ
TTTTTTTTTTTTBIIIIIMMMMWWWWWWWWWWHHHHHHHHZPPPPPPPPPOOQQQQQQQQQQQQTRRRRRRRRRRRHHHHHHRZZZZZZPHHHYEEEEEYYYYYYYYYAAAACCZOOCCCCCCYYYIITIIIIIIIIRRQ
TTTTTXXXBTVVJIIIIIMMMWWWWWWWWWWHHHHHHHHHPPPPPPPPPPPOQQQQQQQQQQQQTTRRRRRRRRHHHHHHHZZZZZZZPPEEEEEEEEYYYYYYYYYAAAAZZZZOOOOCCCCCTTTTTTTTTIIIIIRQ
TTTTXXXXXXJVJJIIIMMMWWWWWWWWWWHHHHHHHNHHPPPPPPPPPPPOOOOOQOQQQQQOOTORRRRRRRRRHHHHZZZZZZZZEEEEEEEEEYYYYYYYYYYYYAAZEZZZOOOOCCCCCTTTTTTTTTTTTTRR
TTTXXXXXJJJVJJIIIIMVVVWWWWWWWHHHHHHHHHHHOPPPPPPPPOPOOOOOOOOQQOOOOOORRRRRRRHHHHHHHZZZZZZZYEEEEEEEYYYYYYYYYYYYYKAEEZZZOOOOOOIITTTTTTTTTTTTTTRR
TXXXXXXYYJJJJIIIIIIVVVWWWWWWWHHHHHHHHHHHOPPOPPOPOOOOOOOOOOQQQOOOOOORRRRRHHHHHHHHHZZZZZZYYEEEEEEEEEIYYYYYYYYYYKKTEEEEOOOOOOITTTTTTTTTTTTRRRRR
TXXXXXXXYJJJJJIJIIIVVVVWWWWWWHHHHHHHHHHOOOOOPOOOOOOOOOOOOOOQOOOOOOORRRRRHRHHHHHHHHHZZZZYYYYEEEEEEEYYYYYYYYYOOKKKEEOOOOOOOOITTTTTTTTTTTTRRRRR
TXTXXXXXYYJJJJJJVVVVVVWWWWWWWWHHHHHHHHHHOOOOOOOOOOOOOOOOOOQQOOOOOOORRRRRRRHHHHHHHHHHHHZYYYEEEEEEEYYYYYYYYYYOOOOOOOOOOOOOOOIITTTTTTTTTTRRRRRR
TTTXXXXXXXJJJJJVVVVVVVVVWWWWWWHFFFFFFFHHHOOOOOOOOOOOOOOOOOOQOOOOOQORRRRRRRHHHHHHHHHHHHHHYYEEEMEEMMYYYYYYYYYYOOOOOOOOOOOOOOIIITTTTTTTTRRRRRRR
TTTXXXXXXZZZJJJVVVVVVVVVWWWWWWFFFFFFFHHLOOOOOOOOOOOOOOOOOOOOOOOOOOORRRRRRRHHHHHHHHHHHHHHYYEEMMMMMYYYYYYYYYYOOOOOOOOOOOQOIIIIITTFFTTRRRRRRRRR
"""

def get_neighbors(x, y, max_x, max_y):
    neighbors = []
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < max_x and 0 <= new_y < max_y:
            neighbors.append((new_x, new_y))
    return neighbors

def count_distinct_sides(region_coords, grid):
    sides = 0
    height = len(grid)
    width = len(grid[0])
    
    # Check each cell in the region
    for x, y in region_coords:
        # Check each direction (up, right, down, left)
        for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
            nx, ny = x + dx, y + dy
            
            # If the neighbor is outside the region (either different type or out of bounds)
            if ((nx, ny) not in region_coords and 
                (0 <= nx < width and 0 <= ny < height)):
                # Check if this is a new side by looking at the previous cell in this direction
                prev_x, prev_y = x - dx, y - dy
                if ((prev_x, prev_y) not in region_coords or 
                    not (0 <= prev_x < width and 0 <= prev_y < height)):
                    sides += 1
    
    return sides

def find_regions(grid):
    if not grid or not grid[0]:
        return []
        
    visited = set()
    regions = []
    height = len(grid)
    width = len(grid[0])
    
    for y in range(height):
        for x in range(width):
            if (x, y) not in visited:
                region_type = grid[y][x]
                region_coords = set()
                stack = [(x, y)]
                
                while stack:
                    curr_x, curr_y = stack.pop()
                    if (curr_x, curr_y) not in visited:
                        visited.add((curr_x, curr_y))
                        if (0 <= curr_x < width and 0 <= curr_y < height and 
                            grid[curr_y][curr_x] == region_type):
                            region_coords.add((curr_x, curr_y))
                            for nx, ny in get_neighbors(curr_x, curr_y, width, height):
                                if grid[ny][nx] == region_type:
                                    stack.append((nx, ny))
                
                if region_coords:
                    regions.append((region_type, region_coords))
    
    return regions

# Parse input and remove any empty lines
grid = [list(line.strip()) for line in puzzleInput.strip().splitlines() if line.strip()]

# Find all regions and calculate total price
total_price = 0
for region_type, region_coords in find_regions(grid):
    area = len(region_coords)
    sides = count_distinct_sides(region_coords, grid)
    price = area * sides
    total_price += price

print(f"Total price: {total_price}")
