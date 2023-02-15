import requests

class Location:

    def test_create_new_person(self):

        print("Список пользователей\n")

        get_url = "https://reqres.in/api/users?key=?page=2"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")

        print("Один пользователь\n")

        get_url = "https://reqres.in/api/user/2"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")

        print("Один пользователь не найден\n")

        get_url = "https://reqres.in/api/users/23"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Успешно!!! Пользователь не найден\n")
        else:
            print("Провал!!! Запрос ошибочный\n")

        print("Список ресурсов\n")

        get_url = "https://reqres.in/api/unknown"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")

        print("Один ресурс\n")

        get_url = "https://reqres.in/api/unknown/2"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!!\n")
        else:
            print("Провал!!! Запрос ошибочный\n")

        print("Один ресурс не найден\n")

        get_url = "https://reqres.in/api/unknown/23"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код : " + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Успешно!!! Ресурс не найден\n")
        else:
            print("Провал!!! Запрос ошибочный\n")



new_place = Location()
new_place.test_create_new_person()
