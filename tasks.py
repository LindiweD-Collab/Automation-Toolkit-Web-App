from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def run_batch_rename():
    
    print("Batch rename completed.")
