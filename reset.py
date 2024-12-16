import requests
from termcolor import colored

def reset_instagram_password(email_or_username):
    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"

    headers = {
        "Host": "www.instagram.com",
        "Cookie": "ig_did=04E26005-61BF-40E8-9DD2-C9FEAFBA2AE4; csrftoken=EP51Ep0IE2HWptZnj6kkto; datr=ObBfZ1hpYWN1_zDsxZDEpV_A; mid=Z1-wOQALAAFK7Wydjeowm8VfOU-v; ps_l=1; ps_n=1; wd=1396x663; dpr=1.375",
        "Sec-Ch-Ua-Full-Version-List": "",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Ch-Ua": "\"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-Ch-Ua-Model": "",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-Ig-App-Id": "936619743392459",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Instagram-Ajax": "1018894167",
        "X-Csrftoken": "EP51Ep0IE2HWptZnj6kkto",
        "X-Web-Session-Id": "1d7duz:57q4i4:hcf9ra",
        "Accept-Language": "en-US,en;q=0.9",
        "X-Asbd-Id": "129477",
        "Sec-Ch-Prefers-Color-Scheme": "dark",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
        "X-Ig-Www-Claim": "0",
        "Sec-Ch-Ua-Platform-Version": "",
        "Origin": "https://www.instagram.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.instagram.com/accounts/password/reset/",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i",
    }

    data = {
        "email_or_username": email_or_username
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        if response.status_code == 200:
            message = f"{response.status_code} | {email_or_username} | successfully sent reset mail"
            print(colored(message, "green"))
        else:
            message = f"{response.status_code} | Request failed | Unexpected error"
            print(colored(message, "red"))
    except requests.exceptions.Timeout:
        message = f"408 | Request timeout | The server did not respond in time"
        print(colored(message, "red"))
    except requests.exceptions.RequestException as e:
        message = f"{response.status_code if 'response' in locals() else 'N/A'} | Request failed | {str(e)}"
        print(colored(message, "red"))

# Example usage
if __name__ == "__main__":
    email_or_username = input("Enter your email or username: ")
    reset_instagram_password(email_or_username)
