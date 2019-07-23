from locust import HttpLocust, TaskSet, task


class UserTask(TaskSet):

    @task
    def job(self):
        params = {"user_id": 871081, "pending_total": 1, "filter_zero": 1}
        a=self.client.get('/v1/walletserv/wallets', params=params)
        # with self.client.get('/v1/walletserv/wallets', catch_response=True) as response:
        #     if response.status_code == 200:
        #         response.success()
        #     else:
        #         response.failure('Failed!')
        #print(a.status_code)

class User(HttpLocust):
    task_set = UserTask
    min_wait = 1000
    max_wait = 3000
    host = "http://l-test-elb1-1859238974.ap-southeast-1.elb.amazonaws.com"
