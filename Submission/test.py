import requests, time

def main():
  try:
    r = requests.post('http://requestbin.net/r/1d7sfug1',
          json={
            "ts":time.time(),
            "taskId": "task1",
            "courseId": "course1",
            "studentId": 11107042,
            "universityId": 1,
            "submission": {
              "exc1": "pip install requirements",
            }
          },
        )
  except Exception as e:
    print(e)
  else:
    print(r.status_code)
    print (r.content)

def ping():
  try:
    r = requests.get('http://requestbin.net/r/1d7sfug1/ping')
  except Exception as e:
    print(e)
  else:
    print(r.status_code)
    print (r.content)

if __name__ == "__main__":
    main()
    ping()
