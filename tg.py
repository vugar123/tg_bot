import telebot
from telebot import types
import random

bot = telebot.TeleBot('6734036487:AAHQYhlx_YUR8DlN7XD2_gJvkPy7QrfUiD8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет моя любимая, минара ❤️')
    photo = open('Love.png', 'rb')
    bot.send_photo(message.chat.id, photo) 
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("И я тебя люблю")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Я тебя очень сильно люблю, а ты меня?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'И я тебя люблю':
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Комплементы от Вугара')
        btn2 = types.KeyboardButton('Фотоальбом')
        btn3 = types.KeyboardButton('Заметки')
        btn4 = types.KeyboardButton('Играть в игру с Вугаром')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Ты самая лучшая. что будем делать?', reply_markup=markup)
        
    elif message.text == 'Комплементы от Вугара':
        compliments = [
            'Ты обладаешь невероятной внешностью',
            'Твоя улыбка заставляет меня таять',
            'Ты всегда выглядишь великолепно, даже без макияжа',
            'Твоя уверенность в себе вдохновляет меня',
            'У тебя очаровательный голос',
            'Ты умна и эрудирована',
            'Ты всегда можешь найти правильные слова, чтобы меня поддержать',
            'Ты очень щедрая и заботливая',
            'Твоя энергия заразительна',
            'У тебя прекрасное geвидение стиля',
            'Ты обладаешь неподдельной красотой',
            'Твое присутствие успокаивает меня',
            'Ты вдохновляешь меня на саморазвитие',
            'Ты всегда стараешься делать мир лучше',
            'Ты обладаешь хорошим чувством юмора',
            'Ты очень талантлива во всем, что делаешь',
            'Твоя интуиция всегда ведет тебя в нужном направлении',
            'У тебя прекрасный слух',
            'Ты способна улучшить настроение окружающих',
            'Ты очень креативная и идеи просто летают к тебе',
            'Ты всегда заботишься о других людях',
            'Ты драгоценное пламя, которое согревает мое сердце',
            'Твои глаза – искусство, которое оживляет мир вокруг меня',
            'Ты обладаешь фантастической силой духа',
            'Ты умеешь читать мои мысли',
            'Ты всегда находишь время для меня',
            'Ты очень дисциплинирована и организована',
            'Твоя улыбка – это солнце, освещающее мой день',
            'Ты всегда находишь способ сделать мир интереснее',
            'Ты умеешь находить добро во всех людях',
            'Ты преображаешься на сцене, и это просто завораживает',
            'Твой голос – это музыка, которую я хочу слушать вечно',
            'Твоя элегантность и изящество восхищают меня',
            'Ты всегда выкладываешься на полную, чтобы достичь своих целей',
            'У тебя причудливый и уникальный вкус',
            'Ты очень смелая и не останавливаешься перед преградами',
            'Ты умеешь решать проблемы с умом и логикой',
            'Ты всегда готова помочь другим',
            'Твоя любовь к жизни заразительна',
            'Ты обладаешь прекрасным чувством ритма',
            'Ты очень хорошо разбираешься в иску'+chr(1085)+'скустве',
            'Твоя креативность не имеет границ',
            'Ты всегда ищешь возможности для роста и самосовершенствования',
            'У тебя чудесное чутье на моду',
            'Ты способна придать изюминку любому наряду',
            'Ты отлично владеешь искусством коммуникации',
            'Твоя доброта и сострадание к другим – бесценные качества',
            'Ты всегда стремишься к самосовершенствованию',
            'Ты обладаешь особой изящностью в движениях',
            'Ты умеешь привлечь внимание комнаты только своим присутствием',
            'Ты всегда находишь способы вдохновить меня',
            'У тебя прекрасное понимание человеческих эмоций',
            'Ты очень сильная и устойчивая женщина',
            'Твоя любовь к животным впечатляет',
            'Ты всегда находишь новые способы проявить свою творческую натуру',
            'У тебя отличное чувство пропорций и баланса',
            'Ты способна уроки жизни учиться быстро и эффективно',
            'Ты обладаешь абсолютным алантом в...',
            'Ты всегда готова поддержать и похвалить своих близких',
            'Твоя интуиция и чувство настроения позволяют тебе легко адаптироваться к ситуациям',
            'Ты всегда находишь светлую сторону любой ситуации',
            'Ты умеешь выражать свои мысли и чувства ясно и доходчиво',
            'Ты обладаешь красивым и естественным обаянием',
            'Ты всегда стремишься помочь другим и делаешь это с легкостью',
            'У тебя потрясающая улыбка, которая может растопить сердца',
            'Ты умная, сильная и независимая женщина',
            'Ты всегда готова встретить новые вызовы и преодолеть преграды',
            'Ты полна энергии и оптимизма, что вдохновляет меня',
            'У тебя прекрасный голос, который может покорить сердца людей',
            'Твоя внутренняя красота отражается на тебе внешне',
            'Ты всегда стараешься быть лучшей версией себя',
            'Ты способна улучшить настроение любого человека своим присутствием',
            'Ты обладаешь изумительной интуицией и чувством предвидения',
            'Твоя улыбка – это настоящий солнечный луч',
            'Ты всегда олицетворяешь нежность и женственность',
            'Ты умеешь наслаждаться каждым моментом жизни',
            'У тебя прекрасное чувство юмора, которое улучшает любую атмосферу',
            'Ты всегда искренне заботишься о людях вокруг тебя',
            'Ты способна преодолеть любую трудность с легкостью',
            'Ты обладаешь великолепным вкусом в выборе одежды',
            'Твоя уверенность в себе – это просто притягательно',
            'Ты всегда готова вложить свое сердце и душу во все, что делаешь',
            'Ты способна находить красоту и в мелочах',
            'Ты умеешь видеть потенциал в любом человеке',
            'Твоя энергия и страсть просто захватывают',
            'Ты всегда следуешь за своим сердцем и стремишься к своим мечтам',
            'У тебя прекрасный голос, который можешь использовать, чтобы привлекать и вдохновлять людей',
            'Твое присутствие делает этот мир более ярким и прекрасным',
            'Ты всегда оказываешь теплую поддержку и понимание',
            'Ты обладаешь красивыми манерами и элегантностью',
            'Ты способна вдохновить кого угодно на действие',
            'Ты всегда находишь свет в самых темных моментах',
            'У тебя отличная интуиция и умение слушать себя',
            'Ты обладаешь невероятной искренностью и честностью',
            'Ты всегда стремишься к личностному росту и самосовершенствованию',
            'Ты способна заставить людей окружающих себя чувствовать себя особенными',
            'У тебя прекрасная способность видеть красоту в простых вещах',
            'Ты всегда ищешь возможности для развития и реализации своих талантов',
            'Ты способна сделать любое помещение уютным и привлекательным',
            'Твоя улыбка может стать лучшим лекарством от плохого настроения',
            'Ты всегда заботишься о здоровье и благополучии тех, кто тебе дорог',
            'Ты обладаешь добротой и открытостью сердца',
            'Ты способна находить красоту и гармонию во всем, что тебя окружает',
            'Твое внутреннее сияние делает этот мир лучше',
            'Ты всегда находишь новые и интересные способы реализовать свои идеи',
            'Ты способна создать атмосферу радости и веселья в любой компании',
            'У тебя отличный вкус в выборе подарков для других',
            'Ты всегда находишь способы сделать свои мечты реальностью',
            'Ты обладаешь уникальным стилем, который никто не может повторить',
            'Твоя улыбка — луч света в темноте',
            'Ты всегда готова поддержать других и помочь им',   
            'Ты способна вдохновить меня на новые высоты',
            'У тебя прекрасное понимание красоты и гармонии',
            'Ты всегда остаешься верной себе в любой ситуации',
            'Ты способна заглянуть в душу любого человека',
        ]
        random_index = random.randint(0, len(compliments)-1)
        bot.send_message(message.from_user.id, compliments[random_index])
        
    elif message.text == 'Играть в игру с Вугаром':   
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Камень')
        btn2 = types.KeyboardButton('Ножницы')
        btn3 = types.KeyboardButton('Бумага')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Спорим на миллион рублей, что не выиграешь у меня в игру камень, ножницы, бумага', reply_markup=markup)
        if message.text == 'Камень':
            bot.send_message(message.from_user.id, 'Бумага', reply_markup=markup)

            
    
            
bot.polling(none_stop=True)
