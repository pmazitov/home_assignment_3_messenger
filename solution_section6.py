import re

messenger = {chat_id1: {users_in_chat: {user_id1, user_id2},
                        messsages: [(timestamp1_1, text1_1, user_id1),
                                    (timestamp1_2, text1_2, user_id2),
                                    (timestamp1_3, text1_3, user_id1)
                                    ]
                        },
             chat_id2: {users_in_chat: {user_id1, user_id3},
                        messsages: [(timestamp2_1, text2_1, user_id1),
                                    (timestamp2_2, text2_2, user_id3),
                                    (timestamp2_3, text2_3, user_id1)
                                    ]
                        }
             }


def add_user(chat_id, *users_id):
    for user_id in users_id:
        if user_id in messenger[chat_id][users_in_chat]:
            print(f'User with id {user_id} is already in this chat!')
            continue
        messenger[chat_id][users_in_chat].add(user_id)
        print(f'User {user_id} is added to chat {chat_id}')

def find_regex(chat_id: int, regex: str) -> None:
    for m in messenger[chat_id][messages][::-1]:
        if re.search(regex, m[1]):
            print(f'User: {m[2]}, time: {m[0]}')
            print(m[1], '\n')

def show_shared_chats(*users_id):
    for chat_id, chat in messenger.items():
        if len(set(users_id) & chat[users_in_chat]) == len(users_id):
            print(f'Chat {chat_id} is common for given users')
