import os
import tmuxer

SESSIONS_FILENAME = "potato_sessions.txt"

sessions_file = os.path.join(os.path.dirname(__file__), "tasks", SESSIONS_FILENAME)
tmuxer.import_and_run(sessions_file)