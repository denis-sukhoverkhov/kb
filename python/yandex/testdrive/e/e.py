from collections import defaultdict


class RateLimiter:

    def __init__(self, user_limit, service_limit, duration):
        self.user_limit = user_limit
        self.service_limit = service_limit
        self.duration = duration

        self.time_after_refresh = duration
        self.count_requests = 0

        self.count_requests_per_user = {}

    def handle_request(self, t, user_id):
        self.count_requests += 1

        if self.time_after_refresh < t:
            self.time_after_refresh += duration
            self.count_requests = 0

        if self.count_requests > self.service_limit:
            self.count_requests -= 1
            return 503

        if user_id not in self.count_requests_per_user:
            self.count_requests_per_user[user_id] = {
                'time': self.duration,
                'ct': 1
            }
        else:
            self.count_requests_per_user[user_id]['ct'] += 1

        if self.count_requests_per_user[user_id]['time'] < t:
            self.count_requests_per_user[user_id]['time'] += duration

        if self.count_requests_per_user[user_id]['ct'] > self.user_limit:
            self.count_requests_per_user[user_id]['ct'] -= 1
            self.count_requests -= 1
            return 429

        return 200


if __name__ == "__main__":
    with open("input.txt", "r") as fi:
        user_limit, service_limit, duration = map(int, fi.readline().strip().split(' '))

        rate_limiter = RateLimiter(user_limit, service_limit, duration)

        buff = fi.readline().strip()
        while buff != '-1':
            t, user_id = map(int, buff.split(' '))
            print(rate_limiter.handle_request(t, user_id))
            buff = fi.readline().strip()
