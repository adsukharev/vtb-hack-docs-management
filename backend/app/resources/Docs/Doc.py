from flask import request
from app.resources.Common.Base import Base
import datetime


class Doc(Base):

    def get(self, doc_id):
        votes = self.get_votes(doc_id)
        chats = self.get_chats(doc_id)
        res = {'votes': votes, 'chats': chats}
        return res

    def get_chats(self, doc_id):
        sql = """
                        SELECT  *
                        FROM chats
                        WHERE doc_id = %s
                    ;"""
        record = (doc_id,)
        doc = self.base_get_limited_all(sql, record)
        return doc

    def get_votes(self, doc_id):
        sql = """
                        SELECT  *
                        FROM votes v
                        left join docs_votes dv
                        on v.vote_id=dv.vote_id
                        WHERE dv.doc_id = %s
                    ;"""
        record = (doc_id,)
        votes = self.base_get_limited_all(sql, record)
        return votes

    def __get_messages(self, chat_id):
        sql = """   SELECT m.creation_date, m.text, u.login as author
                            FROM messages as m
                            JOIN chat_messages cm USING (message_id)
                            JOIN users u ON u.user_id = m.author
                            WHERE cm.chat_id = %s
                            ;"""
        record = (chat_id,)
        messages = self.base_get_limited_all(sql, record)
        return messages

