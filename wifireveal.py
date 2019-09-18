import subprocess

all_profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [ssid.split(":")[1][1:-1] for ssid in all_profiles if "All User Profile" in ssid]
current_ssid = ""
current_pwd = ""
for ssid in profiles:
    try: 
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            current_ssid = ssid
            current_pwd = results[0]
            print (f"SSID: {ssid}\nPassword: {results[0]}\n")
        except IndexError:
            current_ssid = ssid
            current_pwd = "NULL"
            print (f"SSID: {ssid}\nPassword: NULL\n")
    except subprocess.CalledProcessError as exc:
        current_ssid = "Error"
        current_pwd = "NULL"
        print (f"SSID: Error\nPassword: NULL\n")
print ("**********************************"
    f"\nCurrent SSID: {current_ssid}\nCurrent Password: {current_pwd}\n"
    "**********************************\n")