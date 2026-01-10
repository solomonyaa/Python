"""
FocusFlow Scheduler API
Manages single-day meeting schedules.

Constraints:
- Meetings must not cross midnight (00:00)
- All times are in 24-hour HH:MM format
"""

from flask import Flask, request, jsonify
from Meeting_Module import Meeting
import heapq

app = Flask(__name__)

meetings = [
    Meeting("M1", "13:00", 90),
    Meeting("M2", "15:00", 120),
    Meeting("M3", "17:00", 60),
    Meeting("M4", "08:30", 150),
    Meeting("M5", "11:00", 60),
]

heapq.heapify(meetings)


@app.route('/schedule', methods=['POST'])
def schedule_meeting():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    title = data.get('title')
    start_time = data.get('start')
    duration = data.get('duration')

    try:
        new_meeting = Meeting(title, start_time, duration)
    except (TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

    # Check for conflicts
    for exist_m in meetings:
        if (new_meeting.start_time < exist_m.end_time) and (new_meeting.end_time > exist_m.start_time):
            return jsonify({"error": "Conflict exists - unable to schedule meeting"}), 400

    heapq.heappush(meetings, new_meeting)

    return jsonify({
        "title": new_meeting.title,
        "start": new_meeting.get_start_time(),
        "end": new_meeting.get_end_time()
    }), 201


@app.route('/next', methods=['GET'])
def next_meeting():
    if not meetings:
        return jsonify({"error": "No meetings found"}), 404

    next_m = meetings[0]
    return jsonify({
        "title": next_m.title,
        "start": next_m.get_start_time(),
        "end": next_m.get_end_time()
    }), 200


@app.route('/complete', methods=['POST'])
def remove_meeting():
    if not meetings:
        return jsonify({"error": "No meetings found"}), 404

    removed_meeting = heapq.heappop(meetings)
    return jsonify({
        "title": removed_meeting.title,
        "start": removed_meeting.get_start_time(),
        "end": removed_meeting.get_end_time()
    }), 200


@app.route('/all', methods=['GET'])
def get_all_meetings():
    if not meetings:
        return jsonify({"error": "No meetings found"}), 404

    all_meetings = []

    for m in sorted(meetings):
        all_meetings.append({"title": m.title, "start": m.get_start_time(), "end": m.get_end_time()})

    return jsonify(all_meetings), 200


if __name__ == '__main__':
    app.run()
