from atlassian import Confluence
import os, json

#   документация на библиотеку https://atlassian-python-api.readthedocs.io/confluence.html
# перед началом работы создать виртуальную среду командой `python3 -m venv venv`
# записать в конец файла venv/bin/activate строки bash-скрипта для экспорта
# указанных ниже переменных (пример строки): export CONFLUENCE_LOGIN="user@domen.com" 
#                                            и аналогичные
# команды для терминала:
# активировать виртуальную среду - source venv/bin/activate
# деактивировать                 - deactivate
LOGIN = os.environ.get("CONFLUENCE_LOGIN")
TOKEN = os.environ.get("ATLASSIAN_TOCKEN")
URL = os.environ.get("CONFLUENCE_URL")

confluence = Confluence(
    url=URL,            # адрес, указанный со схемой: "http://xxxxxxx.atlassian.com/wiki"
    username=LOGIN,     # user@domen.com
    password=TOKEN,     # токен, сгенерированный на странице https://id.atlassian.com/manage-profile/security/api-tokens
    cloud=True)

'''
# Фрагмент кода, который добавляет новую метку label_B ко всем страницам, которые содержат метку label_A

all_content = confluence.get_all_pages_by_label("label_A", start=0, limit=500)
i=0
# Выводим список страниц
for page in all_content:
    try:
        i+=1
        print(f"Страница ID: {page['id']} - {page['title']}")
        result = confluence.set_page_label(page['id'], "label_B")
        for piece in result['results']:
            print(piece)
    except Exception as e:
        print(f"Ошибка при установке метки на странице {page['id']}: {str(e)}")
print(f"Старниц обработано {i}")
'''
'''
# Фрагмент кода, который удаляет метку label_A на страницах, которые содержат метку label_B

all_content = confluence.get_all_pages_by_label("label_B", start=0, limit=500)
i=0
for page in all_content:
    try:
        i+=1
        print(f"Страница ID: {page['id']} - {page['title']}")
        confluence.remove_page_label(page['id'], "label_A")
    except Exception as e:
        print(f"Ошибка при удалении метки на странице {page['id']}: {str(e)}")
print(f"Старниц обработано {i}")
'''