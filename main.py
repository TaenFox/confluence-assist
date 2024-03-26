from atlassian import Confluence
import os

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
print(confluence.get_all_spaces(start=0, limit=500, expand=None))