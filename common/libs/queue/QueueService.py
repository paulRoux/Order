# -*- coding: utf-8 -*-
import json
from common.models.queue.QueueList import QueueList
from common.libs.Helper import get_current_date
from application import app, db


class QueueService(object):

    @staticmethod
    def add_queue(queue_name, data=None):
        model_queue = QueueList()
        model_queue.queue_name = queue_name
        if data:
            model_queue.data = json.dumps(data)

        model_queue.created_time = model_queue.updated_time = get_current_date()
        db.session.add(model_queue)
        db.session.commit()
        return True
