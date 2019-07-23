from locust import HttpLocust, TaskSet, task


class stay(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print("start test")

    @task(1)
    def readBook(self):
        print('I am reading a book.')

    # @task(1)
    # def listenMusic(self):
    #     print('I am listening to music.')
    #
    # @task(1)
    # def logOut(self):
    #     self.interrupt()


class UserTask(TaskSet):
    tasks = {stay:1}
    @task(1)
    def leave(self):
        print('I don not like this page.')


class User(HttpLocust):
    task_set = UserTask
    host = "https://uat1.klook.io"