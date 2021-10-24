#  _____   ___            
# /       /      \      / 
# |       \___    \    /  
# |           \    \  /   
# \_____   ___/     \/    writer 2021 REV.01
#                         ----------

# JErfurt 2021

# Пишет сообщения из диалога в csv файл

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time

# Импортируем функцию из другого файла моего репозитория
from csv_tools import delRptdMsgs

from vk_info import token

# Введите ваш vk токен в файле vk_info
# Получить вы его можете на сайте https://vkhost.github.io/
# Выбирайте kate mobile, с ним лучше работает

# Введите ваш id!!! (в следующей версии добавлю получение id по api)
my_id = '140109438'

vk_session = vk_api.VkApi(token = token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def getHistory(id, count, offset):
    return vk_session.method('messages.getHistory', {'user_id' : id, 'count' : count, 'offset' : offset, 'rev' : '1'})

def getConversations(count, offset=0):
    #messages.getConversations выводит последние 20
    return vk_session.method('messages.getConversations', {'fields' : '', 'count' : count, 'offset' : offset})

def getUserIdConversations():
    ids = []
    count = getConversations('0')['count']
    count = int(count)

    cycle = count // 199
    if count > 199:
        if count % 199 > 0:
            cycle = cycle + 1

    for i0 in range(cycle):
        Conversations = getConversations('200', i0*199)
        if count > 199:
            cycle = count // 199
            if count % 199 > 0:
                cycle = cycle + 1

        for i in range(count):
            if i > 199:
                i = count
                break

            if Conversations['items'][i]['conversation']['peer']['type'] == 'user':
                ids.append(Conversations['items'][i]['conversation']['peer']['id'])
        if count > 199:
            count = count - 199
    return delRptdMsgs(ids)

def writeOneUserConversation(id):
    f = open('Onedialog.csv', 'w')
    f.write('person, me\n')
    wirte_msgs(f,id)
    f.close()
    return 'WellDone'

def writeAllUserConversations():
    print('Запрашиваем id пользователей с котороми вы переписывались...')
    ids = getUserIdConversations()
    count_ids = len(ids)
    print('Открываем файл Alldialogs.csv')
    f = open('Alldialogs.csv', 'w')
    f.write('person, me\n')
    
    for i in range(count_ids):
        wirte_msgs(f, str(ids[i]), i, count_ids)
        time.sleep(1)
    f.close()
    return 'WellDone'

def wirte_msgs(f ,partner_id, user_nomer=0, count_ids=0):
    print('Начинаю получать сообщения с', partner_id)
    history = getHistory(partner_id, '1', '0')
    count = history['count']
    count = int(count)
    cycle = count // 199
    if count > 199:
        if count % 199 > 0:
            cycle = cycle + 1

    for i0 in range(cycle):

#        print('Цикл:', i0, 'из', cycle)

        history = getHistory(partner_id, '200', i0*199)
        if count > 199:
            cycle = count // 199
            if count % 199 > 0:
                cycle = cycle + 1

        last_from_id = ''
        my_msg = ''
        partner_msg = ''
        for i in range(count):
            if i > 199:
                i = count
                break

            from_id = history['items'][i]['from_id']
            text = history['items'][i]['text']

            if text == '':
                attachments = history['items'][i]['attachments']
                if attachments == 'audio_message':
                    attach_type = history['items'][i]['attachments'][0]['type']
                    if attach_type == 'transcript':
                        text = history['items'][i]['attachments'][0]['audio_message']['transcript']
            
            if text != '':
#                print('Сообщение №:', i)
                #print('Сообщение от:', from_id)
                #print('Тело сообщения:', text)

                if last_from_id == partner_id:
                    if str(from_id) == partner_id:
                        partner_msg = partner_msg + ' ' + text

                elif last_from_id == my_id:
                    if str(from_id) == my_id:
                        my_msg = my_msg + ' ' + text

                if last_from_id != str(from_id):
                    if str(from_id) == my_id:
                        my_msg = text
                    elif str(from_id) == partner_id:
                        partner_msg = text

                    if my_msg != '' and partner_msg != '':
                        print('Пользователь:', partner_id, '№', user_nomer, 'из', count_ids)
                        print('Цикл:', i0, 'Осталось', cycle)
                        print('Сообщение №:', i)
                        print(partner_msg + ',"' + my_msg + '"\n')
                        try:
                            f.write(partner_msg.replace('"', ' ').replace(',', ' ').replace('\n', ' ') + ',"' + my_msg.replace('"', ' ').replace(',', ' ').replace('\n', ' ') + '"\n')
                        except:
                            print('Пропущено из-за ошибки')
                            pass
                        my_msg = ''
                        partner_msg = ''
            last_from_id = from_id
        if count > 199:
            count = count - 199
        time.sleep(1)


if __name__ == "__main__":   
#    print(getUserIdConversations())
    print(writeOneUserConversation('435073237'))
#    print(writeAllUserConversations())
    pass
