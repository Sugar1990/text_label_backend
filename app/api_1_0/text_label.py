from flask import request, jsonify
import time

from . import api_text_label as blue_print
from ..models.pg_models import TreeSet, Task


@blue_print.route('/getftasktypelist', methods=['GET'])
def getftasktypelist():
    types = []
    for i in TreeSet.get_task_types():
        types.append({
            "ftask_type_id": i.id,
            "ftask_type_name": i.name
        })

        res = {
            'total_num': len(TreeSet.get_task_types()),
            "ftask_type_list": types
        }
    return jsonify(res)


@blue_print.route('/gettasktypelist', methods=['GET'])
def gettasktypelist():
    type_id = request.args.get('ftask_type_id', type=int)
    t = Task.query.filter_by(task_type_id=type_id).all()

    res = {
        "total_num": len(t),
        "task_type_list": [{
            "task_type_id": i.id,
            "task_type_name": i.task_name,
            "ftask_type_id": type_id,
            "ftask_type_name": i.get_task_type_name()
        } for i in t]
    }

    return jsonify(res)


@blue_print.route('/gettasklist', methods=['GET'])
def task_list():
    task_id = request.args.get('task_id', '')
    page_num = request.args.get('page_No', 0, type=int)
    page_size = request.args.get('page_Size', 0, type=int)
    limit = request.args.get('limit', '')
    label_user = request.args.get('label_user', '')
    review_user = request.args.get('review_user', '')
    start_time = request.args.get('start_time', '')
    end_time = request.args.get('end_time', '')
    ftask_type_id = request.args.get('ftask_type_id', '')
    task_type_id = request.args.get('task_type_id', [])
    task_status = request.args.get('task_status', '')

    res = []
    if task_id:
        t = Task.query.filter_by(id=task_id).first()
        if t:
            res = [{
                "txt_id": 0,
                "task_id": t.id,
                "task_type_name": t.task_name,
                "ftask_type_name": t.get_task_type_name(),
                "task_status": t.get_task_status_name(),
                "task_type_id": t.task_type_id,
                "task_status_id": t.task_status_id,
                "review_user": t.get_review_user_name(),
                "label_user": t.get_label_user_name(),
                "task_start_time": {
                    "date": t.create_time.isoformat(),
                    "day": t.create_time.day,
                    "hours": t.create_time.hour,
                    "minutes": t.create_time.minute,
                    "nanos": "**",
                    "seconds": t.create_time.second,
                    "time": time.mktime(t.create_time.timetuple()),
                    "timezoneOffset": '**',
                    "year": t.create_time.year,
                },
                "txt_content": 'some txt'
            }]

    return jsonify({
        "total_num": len(res),
        "task_list": res,
    })
