import telebot
from telebot import types
API_TOKEN = '2098535146:AAHg5Jqi3xHCH14VfbE_CUvFmhkrP6sPkao'
BOT_URL='https://sosayu.herokuapp.com/'
bot = telebot.TeleBot(API_TOKEN)

knownUsers = []  # todo: save these in a file,
userStep = {}    # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'       : 'Ботты қолдану үшін',
    'help'        : 'Қол жетімді командалар туралы ақпарат береді'
}

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("Қолданбаған жаңа пайдаланушы анықталды ботты қолдану үшін \"/start\" командасын басыңыз")
        return 0


@bot.message_handler(commands=['start'])
def command_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    item1=types.KeyboardButton('⛑️Қауіпсіздік ережелері')
    item2=types.KeyboardButton('ℹ️ Пайдалану ережесі')
    item3=types.KeyboardButton('🛑 SOS',request_location=True)
    item4=types.KeyboardButton('📞Call center')

    markup.add(item1,item2,item3,item4)
    bot.send_message(message.chat.id,'Cәлеметcіз бе, {0.first_name}!\nБұл чат-бот Қожа Ахмет Ясауи атындағы Халықаралық қазақ-түрік  университетінің қызметкерлері мен оқытушылары және студенттерін төтенше жағдайды алдын ала хабарлау үшін құрылды. \n\n Мен сізге қандай көмек бере алатынымды мәзірден таңдайсыз'.format(message.from_user), reply_markup=markup)
          
@bot.message_handler(content_types=["location","text"])
def bot_message(message):
    if message.chat.type =='private':
        if message.text =='⛑️Қауіпсіздік ережелері':
            markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
            item1=types.KeyboardButton('♨️Өрт қауіпсіздік ережелері')
            item2=types.KeyboardButton('👩‍💻Терроризмнен сақтану жолдары/жаднама')
            item3=types.KeyboardButton('⬅️ Артқа')
            markup.add(item1,item2,item3) 

            bot.send_message(message.chat.id, '⛑️Қауіпсіздік ережелері', reply_markup=markup)
        elif message.text =='🛑 SOS':
            bot.send_message(message.chat.id, 'Help me!')
            if message.location is not None:
                print(message.location)
                print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        elif message.text =='📞Call center':
            bot.send_message(message.chat.id, '+77017659784\n +77015554689\n Өрт сөндірушілер — 101\n Полиция — 102\nЖедел жәрдем — 103\nГаз апатынан құтақру қызметі — 104\nҚұтқару қызметі — 109')
        elif message.text =='ℹ️ Пайдалану ережесі':
            bot.send_message(message.chat.id, '"SOS.Ayu.bot "(бұдан әрі-SOS.Ayu) сандық дабыл түймесін пайдалану ережеcі:\n\n1. SOS.Ayu Университет студенттері мен қызметкерлерін, сондай – ақ студенттер мен қызметкерлердің Университетті төтенше оқиға (жер сілкінісі, су тасқыны, өзге де дүлей зілзала, террористік акт(тер) – бұдан әрі-ТО) туралы шұғыл хабардар етуге арналған.\n\n2. ТО туралы хабарлама:\n\n(1) университет студенті / қызметкерінен алған жағдайда: университеттің жауапты қызметкерлері, тиісті шаралар қабылдайды;\n(2) университеттен алған жағдайда: студенттер мен қызметкерлер хабарламада көрсетілген шараларды қабылдауға міндетті.\n\n3. SOS.Ayu-ды келесі жағдайларда қолдану қажет: сізге немесе басқа студентке/қызметкерге Университет аумағында тікелей шабуыл жасаған кезде; Университетке материалдық зиян келтірген кезде; Университетте өрт туындаған кезде; Университетке іргелес аумақта күдікті заттар табылған кезде; Университетте материалдық құндылықтарды ұрлауға әрекет жасаған кезде; басқа ТО туындаған кезде.\n4. SOS.Ayu-ды қажетсіз пайдалануға тыйым салынады. Осы тыйымды бұзуға жол берген адамдар тәртіптік және өзге де жауаптылыққа тартылады.\n5. SOS.Ayu-ды кездейсоқ пайдаланған жағдайда "SOS" хабарламасын жіберген университет студенті немесе қызметкері бұл туралы Call-center-ге қоңырау шалу арқылы хабарлауы тиіс.')
        elif message.text =='⬅️ Артқа':
            markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
            item1=types.KeyboardButton('⛑️Қауіпсіздік ережелері')
            item2=types.KeyboardButton('ℹ️ Пайдалану ережесі')
            item3=types.KeyboardButton('🛑 SOS',request_location=True)
            item4=types.KeyboardButton('📞Call center')

            markup.add(item1,item2,item3,item4)
            bot.send_message(message.chat.id, '⬅️ Артқа', reply_markup=markup)
        elif message.text =='♨️Өрт қауіпсіздік ережелері':
            bot.send_message(message.chat.id, '♨️Өрт шыққан жағдайда  не істеу керек?\n👨‍🚒Зардап шеккендерге алғашқы көмек\n❓Не істеуге болмайды?\n🔥Өрттің алдын алу үшін')
        elif message.text =='👩‍💻Терроризмнен сақтану жолдары/жаднама':
            bot.send_message(message.chat.id, '👮‍♂️Террористік актілерді болдырмау жөніндегі жаднама\n👮‍♂️Күдікті тұлғаларды байқаған жағдайда жаднама\n👮‍♂️Күдікті зат тауып алған кездегі жаднама\n👮‍♂️Жарылыс аймағында немесе ғимараттың қираған үйінділерінің арасында қалған тұрғындарға жаднама\n👮‍♂️ Адамдарды кепілге алған жағдайдағы іс-қимылдар бойынш жаднама')
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True)        
