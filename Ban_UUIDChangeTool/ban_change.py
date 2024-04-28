import requests

def get_uuid(mcid):
    url = f"https://api.mojang.com/users/profiles/minecraft/{mcid}"
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        uuid = json_response.get('id', 'none')
        return uuid
    else:
        print(f"{mcid} は読み取り不可でした。")
        return 'none'

def main():
    with open('mcid.txt', 'r') as mcid_file:
        mcids = mcid_file.read().splitlines()

    with open('uuid.txt', 'w') as uuid_file:
        for mcid in mcids:
            uuid_value = get_uuid(mcid)
            uuid_file.write(uuid_value + '\n')

if __name__ == "__main__":
    main()
