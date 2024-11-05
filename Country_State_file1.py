import json


class CountryState:
    def __init__(self):
        # Инициализируем пустой словарь
        self.data = {}

    def add_country(self, country, capital):
        """Добавляет пару 'страна - столица'."""
        self.data[country] = capital

    def remove_country(self, country):
        """Удаляет пару 'страна - столица' по ключу 'страна'."""
        if country in self.data:
            del self.data[country]
        else:
            print(f"{country} не найдена в данных.")

    def find_capital_by_country(self, country):
        """Ищет столицу по названию страны."""
        return self.data.get(country, "Страна не найдена.")

    def find_country_by_capital(self, capital):
        """Ищет страну по названию столицы."""
        for country, cap in self.data.items():
            if cap == capital:
                return country
        return "Столица не найдена."

    def edit_capital(self, country, new_capital):
        """Редактирует столицу по названию страны."""
        if country in self.data:
            self.data[country] = new_capital
        else:
            print(f"{country} не найдена в данных.")

    def save_to_file(self, filename):
        """Сохраняет данные в файл в формате JSON."""
        with open(filename, 'w') as file:
            json.dump(self.data, file)

    def load_from_file(self, filename):
        """Читает данные из файла формата JSON."""
        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка при декодировании файла {filename}.")


# Пример использования
if __name__ == "__main__":
    country_state = CountryState()

    # Добавить страны и столицы
    country_state.add_country("Казахстан", "Нур-Султан")
    country_state.add_country("Россия", "Москва")
    country_state.add_country("США", "Вашингтон")

    # Поиск столицы
    print(country_state.find_capital_by_country("Казахстан"))  # Нур-Султан

    # Поиск страны по столице
    print(country_state.find_country_by_capital("Москва"))  # Россия

    # Редактирование столицы
    country_state.edit_capital("Казахстан", "Астана")
    print(country_state.find_capital_by_country("Казахстан"))  # Астана

    # Удаление страны
    country_state.remove_country("Россия")

    # Сохранение данных в файл
    country_state.save_to_file("countries.json")

    # Загрузка данных из файла
    new_country_state = CountryState()
    new_country_state.load_from_file("countries.json")
    print(new_country_state.data)  # {'Казахстан': 'Астана', 'США': 'Вашингтон'}