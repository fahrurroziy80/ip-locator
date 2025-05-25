
import requests
import argparse
import webbrowser

def locate_ip(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()

        if data["status"] == "success":
            print("\n[+] IP Location Info:")
            print(f"  - IP       : {ip_address}")
            print(f"  - Country  : {data['country']}")
            print(f"  - Region   : {data['regionName']}")
            print(f"  - City     : {data['city']}")
            print(f"  - ISP      : {data['isp']}")
            print(f"  - Lat, Lon : {data['lat']}, {data['lon']}")

            maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
            print(f"\n[+] Google Maps: {maps_url}")

            open_map = input("\n[?] Open in browser? (y/n): ").lower()
            if open_map == "y":
                webbrowser.open(maps_url)
        else:
            print("[-] Failed to retrieve IP info. Maybe private or invalid IP.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP Geolocation Tool")
    parser.add_argument("ip", help="IP address to locate")
    args = parser.parse_args()

    locate_ip(args.ip)
