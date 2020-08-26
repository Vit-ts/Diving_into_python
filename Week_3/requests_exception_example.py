import sys 
import requests

url = sys.argv[1]
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status() # 200 OK
# timepot 30 s.
except requests.Timeout:
    print("Timeout error, url: ", url)
# несуществующий адрес и ответ не 200 OK
except requests.HTTPError as err:
    code = err.response.status_code
    print("Error url: {0}, code: {1}".format(url, code))
# other exceptions
except requests.RequestException:
    print("loading error url: ", url)
# исключение не произошло
else:
    print(response.content)
