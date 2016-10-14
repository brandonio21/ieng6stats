import os
import json

DB_FILENAME = 'db.json'

class JSONDatabaseProxy(object):
    def __init__(self, db_dir):
        self.database = {}
        self.db_dir = db_dir
        self._load_db()

    def _ensure_db_dir_exists(self):
        if not os.path.isdir(self.db_dir):
            os.mkdir(self.db_dir)

    def _save_db(self):
        self._ensure_db_dir_exists()

        db_path = os.path.join(self.db_dir, DB_FILENAME)
        with open(db_path, 'w+') as dbfile:
            dbfile.write(json.dumps(self.database))

    def _load_db(self):
        self._ensure_db_dir_exists()
        
        db_path = os.path.join(self.db_dir, DB_FILENAME)
        if os.path.isfile(db_path):
            with open(db_path, 'r') as dbfile:
                self.database = json.loads(dbfile.read())

    def get_latest_stat(self, hostname):
        all_stats = self.database[hostname]
        return all_stats[-1]

    def add_stat(self, hostname, stat_dict):
        if hostname not in self.database:
            self.database[hostname] = []

        self.database[hostname].append(stat_dict)
        self._save_db()