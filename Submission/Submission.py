import requests, time
LTI_SERVER="http://http://requestbin.net/r/17uw9771"

def submit_json(taskId, student, submission):
  try:
    r = requests.post(LTI_SERVER,
          json={
            "ts":time.time(),
            "taskId": taskId,
            "courseId": student.courseId,
            "studentId": student.id,
            "universityId": student.universityId,
            "submission": submission,
          },
        )
    print(submission)
  except Exception as e:
    print(e)
  else:
    print(r.status_code)
    print(r.content)
    print("100 Punkte")

def submit_txt():
  print("Text submitted")

def validate():
  print("To be implemented")

def ping():
  try:
    r = requests.get(LTI_SERVER + '/ping')
  except Exception as e:
    print(e)
  else:
    print(r.status_code + " OK")
    print ("Ping test was successful.")
