class Models:
    users = '''
                CREATE TABLE IF NOT EXISTS users(
                user_id         SERIAL          NOT NULL PRIMARY KEY,
                email           VARCHAR(64)     UNIQUE,
                login           VARCHAR (64)    NOT NULL UNIQUE,
                password        VARCHAR(1024),
                room            VARCHAR(1024)
                );'''

    docs = '''
            
            '''

    votes = '''
                CREATE TABLE IF NOT EXISTS votes(
                vote_id        SERIAL          NOT NULL PRIMARY KEY,
                chat_name      VARCHAR(64)     NOT NULL
                plus           INT,
                minus          INT
            );'''

    votes_users = '''
                CREATE TABLE IF NOT EXISTS votes_users(
                 vote_id     INT REFERENCES votes (vote_id) ON DELETE CASCADE,
                 user_id     INT REFERENCES users (user_id) ON DELETE CASCADE
                );'''


    chats = '''
                CREATE TABLE IF NOT EXISTS chats(
                chat_id        SERIAL          NOT NULL PRIMARY KEY,
                chat_name      VARCHAR(64)     NOT NULL
                );'''

    chat_users = '''
                CREATE TABLE IF NOT EXISTS chat_users(
                 chat_id     INT REFERENCES chats (chat_id) ON DELETE CASCADE,
                 user_id     INT REFERENCES users (user_id) ON DELETE CASCADE
                );'''

    chat_messages = '''
                CREATE TABLE IF NOT EXISTS chat_messages(
                 chat_id     INT REFERENCES chats (chat_id) ON DELETE CASCADE,
                 message_id  INT REFERENCES messages (message_id) ON DELETE CASCADE
                );'''
    messages = '''
                 CREATE TABLE IF NOT EXISTS messages(
                 message_id     SERIAL          NOT NULL PRIMARY KEY,
                 creation_date  VARCHAR(64)     NOT NULL,
                 text           TEXT            NOT NULL,
                 author         INT             NOT NULL REFERENCES users(user_id) ON DELETE CASCADE
                 );'''