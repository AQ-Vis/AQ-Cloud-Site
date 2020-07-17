import random
from locust import HttpUser, task, between

class QuickStartUser(HttpUser):
    wait_time = between(5, 9)
    @task
    def load_page(self):
        self.client.get("/")
