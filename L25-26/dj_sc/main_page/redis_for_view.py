

import redis

redis_db = redis.Redis('localhost', 6379)


def run_task():
    print("def run_task")
    print("==========================================================================")



    try:
        redis_db.lpush(
            'porter_scrap:start_urls',
            'https://www.net-a-porter.com/us/en/d/Shop/Shoes/All'
        )
    except Exception:
            return "Error DB"
