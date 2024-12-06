import requests

def get_steam_id(profile_url):
    if 'profiles' in profile_url:
        return profile_url.split('/')[-1]
    elif 'id' in profile_url:
        username = profile_url.split('/')[-1]
        api_key = 'STEAM_API_KEY'  # Замените на ваш API ключ
        response = requests.get(f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={username}')
        
        # Проверка на наличие ключа 'response' в ответе
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and data['response']['success'] == 1:
                return data['response']['steamid']
            else:
                print(f"Ошибка: {data.get('response', {}).get('success', 'Неизвестная ошибка')} для {username}")
                return None
        else:
            print(f"Ошибка запроса: {response.status_code} для {username}")
            return None
    return None

def convert_to_steam_format(steam_id):
    # Преобразование 64-битного Steam ID в формат STEAM_X:Y:Z
    steam_id = int(steam_id)  # Убедитесь, что steam_id - это строка, представляющая число
    steam_id_32 = steam_id - 76561197960265728
    return f"STEAM_0:{steam_id_32 % 2}:{steam_id_32 // 2}"

# Чтение профилей из файла
with open('profiles.txt', 'r') as file:
    profile_urls = file.read().splitlines()

# Открытие файла для записи результатов
with open('output.txt', 'w') as output_file:
    # Получение Steam ID для каждого профиля
    for url in profile_urls:
        steam_id = get_steam_id(url)
        if steam_id and steam_id.isdigit():  # Проверка, что steam_id - это число
            steam_id_formatted = convert_to_steam_format(steam_id)
            output_file.write(f'{steam_id_formatted}\n')  # Записываем только Steam ID
            print(f'Steam ID: {steam_id_formatted}')
        else:
            output_file.write(f'Не удалось получить Steam ID для {url}\n')
            print(f'Не удалось получить Steam ID для {url}')

print("Результаты сохранены в output.txt")
