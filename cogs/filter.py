import discord
from discord.ext import commands, tasks
from time import sleep




filtered_words = ['kamine', 'bitch', 'xxx', 'erotic', 'shit', 'bra', 'nipple', 'jhaat', 'mc', 'bhosdika', 'baap', 'aulad',
 'wtf', 'chood', 'chhod', 'bhadwe', 'bhadve', 'behnchod', 'gaand', 'baap', 'mf', 'fuck', 'mc', 'bc', 'lawde', 'chutiya'
  'mother', 'laude', 'chutiye', 'maderchod', 'maderchhod', 'maderchood', 'madarchod', 'madarchhod', 'chut', 'bhen',
   'bsdk', 'kaminey', 'gaand','gand', 'tatti', 'pennis', 'fucker', 'madarchod', 'machod', 'chood', 'machod', 'fuck', 'fck'
    'fkuc', 'fuk', 'sex', 'sexy', 'nigga','asshole', 'bc', 'ass', 'fuckoff', 'cock', 'hardcore', 'leabian', 'motherfuck',
     'lund', 'dick', 'dickhead', 'nigga', 'orgasm', 'porn', 'slut', 'viagra', 'whore', 'dildo', 'pussy', 'piss', 'hijde'
      'madar', 'madarchodd', 'chodd', 'randi', 'randiii', 'lund', 'lundd', 'lode', 'laude', 'chuss', 'land', 'choot',
       'chut', 'maa', 'randy', 'madarchodd', 'nanga', 'nangi', 'benchod', 'bancho', 'behnchod', 'gaand', 'lundd', 'shit',
        'ass', 'asshole', 'ass', 'asa', 'ass', 'asshole', 'ahole', 'anal', 'anal impaler', 'anal leakage', 'analprobe']
filtered_words2 = [
         'anus', 'arsehole', 'ass', 'ass fuck', 'ass fuck', 'ass hole', 'assbag', 'assbandit', 'assbang', 'assbanged',
          'assbanger', 'assbangs', 'assbite', 'assclown', 'asscock', 'asscracker', 'asses', 'assface', 'assfaces',
           'assfuck', 'assfucker', 'assfucker', 'assfukka', 'assgoblin', 'asshole', 'asshat', 'asshat', 'asshead',
            'asshoie', 'asshole', 'assholes', 'asshopper', 'assjabber', 'assjacker', 'asslick', 'asslicker', 'assmaster',
             'assshole', 'asssucker', 'asswad', 'asswhole', 'asswipe', 'asswipes', 'erotic', 'azz', 'bitch', 'boobs', 
             'bitch', 'bitch', 'licking', 'sack', ' sucking', 'ballbag', 'balls', 'ballsack', 'bangbros', 'bastard', 
             'bastardo', 'bastards', 'beotch', 'bitch', 'biatch', 'big black', 'breasts', 'big tits', 'bigtits',
              'bitch', 'bitch tit', 'bitch tit', 'bitchass', 'bitched', 'bitcher', 'bitchers', 'bitches', 'bitchin', 
              'bitching', 'bitchtits', 'bitchy', 'black cock', 'blonde action', 'blonde on blonde action', 'bloody hell', 
              'blow job', 'blow me', 'blow your load', 'blowjob', 'blowjobs', 'boner', 'boners', 'boob', 'boobies', 'boobs', 
              'booby', 'booger', 'bookie', 'boong', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'bootee', 'bootie', 'booty', 
              'booty call', 'breasts', 'Breeder', 'brotherfucker', 'bull shit', 'bullshit', 'bullshits', 'bullshitted', 
              'bullturds', 'bung', 'bung hole', 'bunghole', 'bunny fucker', 'bust a load', 'bust a load', 'busty', 'butt', 
              'butt fuck', 'butt fuck', 'butt plug', 'buttcheeks', 'buttfuck', 'buttfucka', 'buttfucker', 'butthole', 
              'buttmuch', 'buttmunch', 'buttpirate', 'buttplug', 'cock', 'cock', 'cunt', 'cock', 'cock', 'cocksucker', 
              'chichi man', 'chick with a dick', 'childfucker', 'chode', 'chodes', 'clit', 'clit licker', 'clit licker', 
              'clitface', 'clitfuck', 'clitoris', 'clitorus', 'clits', 'clitty', 'clitty litter', 'clitty litter']
filtered_words3 = [
              'clusterfuck', 'cnut', 'cocain', 'cocaine', 'coccydynia', 'cock', 'cock', 'cock pocket', 'cock pocket', 
              'cock snot', 'cock snot', 'cock sucker', 'cockass', 'cockbite', 'cockblock', 'cockburger', 'cockeye', 
              'cockface', 'cockfucker', 'cockhead', 'cockholster', 'cockjockey', 'cockknocker', 'cockknoker', 
              'Cocklump', 'cockmaster', 'cockmongler', 'cockmongruel', 'cockmonkey', 'cockmunch', 'cockmuncher', 
              'cocknose', 'cocknugget', 'cocks', 'cockshit', 'cocksmith', 'cocksmoke', 'cocksmoker', 'cocksniffer', 
              'cocksuck', 'cocksuck', 'cocksucked', 'cocksucked', 'cocksucker', 'cocksucker', 'cocksuckers', 
              'cocksucking', 'cocksucks', 'cocksucks', 'cocksuka', 'cocksukka', 'cockwaffle', 'condom', 'coochie', 
              'coochy', 'corksucker', 'cornhole', 'cornhole', 'corp whore', 'corp whore', 'crackhead', 'crackwhore', 
              'crap', 'crappy', 'creampie', 'crikey', 'cripple', 'crotte', 'cum', 'cum chugger', 'cum chugger', 
              'cum dumpster', 'cum dumpster', 'cum freak', 'cum freak', 'cum guzzler', 'cum guzzler', 'cumbubble', 
              'cumdump', 'cumdump', 'cumdumpster', 'cumguzzler', 'cumjockey', 'cummer', 'cummin', 'cumming', 'cums', 
              'cumshot', 'cumshots', 'cumslut', 'cumstain', 'cunillingus', 'cunnie', 'cunnilingus', 'cunny', 'cunt', 
              'cunt', 'cunt hair', 'cunt hair', 'cuntass', 'cuntbag', 'cuntbag', 'cuntface', 'cunthole', 'cunthunter', 
              'cuntlick', 'cuntlick', 'cuntlicker', 'cuntlicker', 'cuntlicking', 'cuntlicking', 'cuntrag', 'cunts', 
              'cuntsicle', 'cuntsicle', 'cuntslut', 'cuntstruck', 'cuntstruck', 'cyberfuc', 'cyberfuck', 'cyberfuck', 
              'cyberfucked', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'cyberfucking', 'douche', 
              'douche', 'dick', 'dildo', 'dildo', 'darkie', 'rape', 'daterape', 'dawgiestyle', 'deep throat', 
              'deepthroat', 'dick', 'dick head', 'dick hole', 'dick hole', 'dick shy', 'dick shy', 'dickbag', 
              'dickbeaters', 'dickdipper', 'dickface', 'dickflipper', 'dickfuck', 'dickfucker', 'dickhead', 
              'dickheads', 'dickhole', 'dickish', 'dickish', 'dickjuice', 'dickmilk', 'dicks', 'dicksucker', 
              'dicksucking', 'dicktickler', 'dickwad', 'dildo', 'dildos', 'dog style', 'dogfucker', 'doggie style', 
              'doggiestyle', 'doggiestyle', 'doggin', 'dogging', 'doggy style', 'doggystyle', 'doggystyle', 
              'double penetration', 'douche', 'douche', 'dumass', 'dumb ass', 'dumbass', 'dumbasses', 'Dumbcunt', 
              'dumbfuck', 'dumbshit', 'dummy', 'dumshit', 'eat a dick', 'eat a dick', 'eat hair pie', 'eat hair pie']
filtered_words4 = [
              'eat my ass', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculates', 'ejaculating', 'ejaculating', 
              'ejaculatings', 'ejaculation', 'ejakulate', 'erect', 'erection', 'erotic', 'erotism', 'f u c k', 
              'f u c k e r', 'fuck', 'fuck', 'fack', 'fag', 'fagbag', 'fagfucker', 'fagg', 'fagged', 'fagging', 
              'faggit', 'faggitt', 'faggot', 'faggotcock', 'faggots', 'faggs', 'fagot', 'fagots', 'fatass', 'fcuk', 
              'fcuker', 'fcuking', 'fecal', 'feck', 'fecker', 'fcuk', 'fingerbang', 'fingerfuck', 'fingerfuck', 
              'fingerfucked', 'fingerfucked', 'fingerfucker', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucking', 
              'fingerfucks', 'fingerfucks', 'fingering', 'fuc', 'fuck', 'fuck', 'fuck', 'fuck buttons', 'fuck hole', 'fuck hole', 
              'Fuck off', 'fuck puppet', 'fuck puppet', 'fuck trophy', 'fuck trophy', 'fuck yo mama', 'fuck yo mama', 'fuck you', 
              'fucka', 'fuckass', 'fuckass', 'fuckass', 'fuckbag', 'fuckbitch', 'fuckbitch', 'fuckboy', 'fuckbrain', 'fuckbutt', 
              'fuckbutter', 'fucked', 'fuckedup', 'fucker', 'fuckers', 'fuckersucker', 'fuckface', 'fuckhead', 'fuckheads', 
              'fuckhole', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fuckme', 'fuckmeat', 'fuckmeat', 
              'fucknugget', 'fucknut', 'fucknutt', 'fuckoff', 'fucks', 'fuckstick', 'fucktard', 'fucktard', 'fucktards', 
              'fucktart', 'fucktoy', 'fucktoy', 'fucktwat', 'fuckup', 'fuckwad', 'fuckwhit', 'fuckwit', 'fuckwitt',
               'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkers', 'fukkin', 'fuks', 'fukwhit', 
               'fukwit', 'fuq', 'fux', 'fuxor', 'fvck', 'fxck', 'gae', 'gang bang', 'gangbang', 'gangbang', 'gangbang', 
               'gangbanged', 'gangbangs', 'ganja', 'gash', 'gassy ass', 'gassy ass', 'gay', 'gay sex', 'gayass', 'gaybob', 
               'gaydo', 'gayfuck', 'gayfuckist', 'gaylord', 'gays', 'gaysex', 'gaytard', 'gaywad', 'gender bender', 'genitals', 
               'gey', 'god damn', 'godamn', 'godamnit', 'goddam', 'goddam', 'goddammit', 'goddamn', 'goddamned', 'goddamned', 
               'goddamnit', 'godsdamn', 'gtfo', 'homo', 'homo', 'hand job', 'handjob', 'hard core', 'hard on', 'hardcore', 
               'hardcoresex', 'hentai', 'herp', 'herpes', 'herpy', 'heshe', 'heshe', 'hircismus', 'hitler', 'hiv', 'hoar', 
               'hoare', 'hobag', 'hoe', 'hoer', 'holy shit', 'homo', 'homo', 'homodumbshit', 'homoerotic', 'homoey', 'hore', 
               'horniest', 'horny', 'hot carl', 'hot chick', 'hotsex', 'how wtf', 'inbred', 'incest', 'injun', 'intercourse', 
               'jack off', 'jackass', 'jackasses', 'jackhole', 'jackoff', 'jackoff', 'jaggi', 'jagoff', 'jail bait', 'jailbait', 
               'jap', 'japs', 'jelly donut', 'jerk', 'jerk off', 'jerkoff', 'jerkass', 'jerked', 'jerkoff', 'jerkoff', 'kock', 
               'kondum', 'kondums', 'kooch', 'kooches', 'kootch', 'kraut', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 
               'kunja', 'kunt', 'lesbian', 'lesbians', 'lesbo', 'lesbos', 'lez', 'lezza', 'lesbo', 'lovemaking', 'lube', 'lust']
filtered_words5 = [
               'lusting', 'lusty', 'mofo', 'mofo', 'masterbate', 'masterbe', 'masterbate', 'mafugly', 'mafugly', 'make me come', 
               'male squirting', 'mams', 'masterbe', 'masterbate', 'masterbate', 'masterbate', 'masterbate', 'masterbate', 
               'masterbating', 'masterbation', 'masterbations', 'masturbate', 'masturbating', 'masturbation', 'mcfagget', 
               'menstruate', 'menstruation', 'meth', 'mfucking', 'milf', 'moron', 'mothafuck', 'mothafucka', 'mothafuckas', 
               'mothafuckaz', 'mothafucked', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 
               'mothafucking', 'mothafuckings', 'mothafucks', 'mother fucker', 'mother fucker', 'motherfuck', 'motherfucka', 
               'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 
               'motherfucks', 'muthafecker', 'muthafuckker', 'mutherfucker', 'nigga', 'nigger', 'naked', 'nigger', 'niggah', 'nigga', 
               'nude', 'nudity', 'numbnuts', 'nut butter', 'nut butter', 'nut sack', 'nutsack', 'nutter', 'nympho', 'nymphomania', 
               'octopussy', 'orgasim', 'orgasims', 'orgasm', 'orgasmic', 'orgasms', 'orgies', 'orgy', 'ovary', 'ovum', 'ovums', 
               'pussy', 'porn', 'pantie', 'panties', 'panty', 'pawn', 'pee', 'peepee', 'penetrate', 'penetration', 'penial', 
               'penile', 'penis', 'penisbanger', 'penisfucker', 'penispuffer', 'perversion', 'phallicsex', 'phonesex', 'phuck', 
               'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'piece of shit', 'pigfucker', 'pissed', 
               'pissed off', 'pisser', 'pissers', 'pisses', 'pisses', 'pissflaps', 'pissin', 'pissin', 'pissing', 'pissoff', 
               'pissoff', 'pissoff', 'pisspig', 'poop', 'poop chute', 'poopchute', 'Poopuncher', 'porch monkey', 'porchmonkey', 
               'porn', 'porno', 'pornography', 'pornos', 'psycho', 'puss', 'pusse', 'pussi', 'pussies', 'pussy', 'pussy fart', 
               'pussy fart', 'pussy palace', 'pussy palace', 'pussylicking', 'pussypounder', 'pussys', 'raging boner', 'rape', 
               'raped', 'raper', 'raping', 'rapist', 'rectal', 'rectum', 'rectus', 'reefer', 'reetard', 'reich', 'renob', 'retard',
               'retarded', 's hit', 'shit', 'scum', 'seaman', 'seamen', 'seduce', 'seks', 'semen', 'sex', 'sexo', 'sexual', 'sexy', 
               'shit', 'shit', 'shit', 'shit', 'shaved pussy', 'shemale', 'shit', 'shit', 'shit', 'shit ass', 'shit fucker']
filtered_words6 = [
               'shit fucker', 'shitass', 'shitbag', 'shitbagger', 'shitblimp', 'shitbrains', 'shitbreath', 'shitcanned', 'shitcunt', 
               'shitdick', 'shit', 'shiteater', 'shited', 'shitey', 'shitface', 'shitfaced', 'shitfuck', 'shitfull', 'shithead', 
               'shitheads', 'shithole', 'shithouse', 'shiting', 'shitings', 'shits', 'shitspitter', 'shitstain', 'shitt', 'shitted', 
               'shitter', 'shitters', 'shitters', 'shittier', 'shittiest', 'shitting', 'shittings', 'shitty', 'slut', 'slut bucket', 
               'slut bucket', 'slutbag', 'slutdumper', 'slutkiss', 'sluts', 'son of a bitch', 'son of a motherless goat', 
               'son of a whore', 'sonofabitch', 'sperm', 'stfu', 'suck', 'suckass', 'sucked', 'sucking', 'sucks', 'tit', 'titties', 
               'titties', 'testical', 'testicle', 'testis', 'threesome', 'throating', 'tied up', 'tight white', 'tinkle', 'tit', 
               'tit wank', 'tit wank', 'titfuck', 'titi', 'tities', 'tits', 'titt', 'titties', 'tittiefucker', 'titties', 'titty', 
               'tittyfuck', 'tittyfucker', 'tittywank', 'tongue in a', 'transsexual', 'two fingers', 'two fingers with tongue', 
               'undressing', 'urinal', 'urine', 'urophilia', 'vagina', 'viagra', 'vibrator', 'whore', 'whoreface', 'whore', 
               'whorealicious', 'whorebag', 'whored', 'whoreface', 'whorehopper', 'whorehouse', 'whores', 'whoring', 
               'wigger', 'wtf', 'xrated', 'xrated', 'xxx', 'xxx', 'what the fuck', 'the fuck', 'tf']





class filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        


        
    @commands.Cog.listener()
    async def on_message(self, 	msg	):
        if msg.content.lower() in filtered_words or filtered_words2 or filtered_words3 or filtered_words4 or filtered_words5 or filtered_words6:
             await msg.delete()


def setup(bot):
    bot.add_cog(filter(bot))