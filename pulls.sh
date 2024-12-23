#!/bin/bash
set -e

# Проверка на наличие аргумента
if [ -z "$1" ]; then
    echo "Usage: $0 <github-username>"
    exit 1
fi

USERNAME="$1"
TOKEN=$(cat /home/users/FeelUsM/github_token)
REPO="datamove/linux-git2"
all_pulls=()
page=1
max_pages=20  # Максимальное количество страниц для загрузки

if true; then
# Получение всех пулл-реквестов пользователя с постраничным запросом
#echo '' > all_pulls.json
while [ "$page" -le "$max_pages" ]; do
    #echo $page

    # Запрос с указанием страницы и лимита
    pulls=$(curl -s -H "Authorization: token $TOKEN" "https://api.github.com/repos/$REPO/pulls?state=all&per_page=100&page=$page" )
    #echo $pulls >> all_pulls.json


    # Проверка на окончание данных
    if [ -z "$(echo $pulls | jq '.[]')" ]; then
        break
    fi

    # Добавление результатов текущей страницы к общему массиву

    all_pulls+=$'\n'"$pulls"
    ((page++))
done
#echo $all_pulls > all_pulls2.json
else
    echo load from file
    all_pulls=$(cat all_pulls.json)
fi

all_pulls=$(echo $all_pulls | jq --arg username "$USERNAME" '.[] | select(.user.login == $username)')

#echo $all_pulls > all_pulls-"$USERNAME".json

# Объединяем все страницы пулл-реквестов в один JSON массив
all_pulls_json=$(printf "%s\n" "${all_pulls[@]}" | jq -s '.')

# Подсчёт всех пулл-реквестов пользователя
total_pulls=$(echo "$all_pulls_json" | jq 'length')
echo "PULLS $total_pulls"

# Проверка на наличие пулл-реквестов
if [ "$total_pulls" -gt 0 ]; then
    # Поиск самого раннего пулл-реквеста
    earliest_pull=$(echo "$all_pulls_json" | jq 'sort_by(.created_at) | .[0]')
    earliest_number=$(echo "$earliest_pull" | jq '.number')
    echo "EARLIEST $earliest_number"

    # Проверка, был ли этот пулл-реквест смержен
    merged=$(echo "$earliest_pull" | jq '.merged_at != null')
    if [ "$merged" == "true" ]; then
        echo "MERGED 1"
    else
        echo "MERGED 0"
    fi
else
    echo "EARLIEST 0"
    echo "MERGED 0"
fi

