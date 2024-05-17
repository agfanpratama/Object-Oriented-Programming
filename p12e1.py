
import datetime
import pytz

def my_decorator(inner):
    def inner_decorator():
        # Mendapatkan waktu UTC
        utc_now = datetime.datetime.now(pytz.utc)
        # Mengubah waktu UTC menjadi UTC+7
        jakarta_tz = pytz.timezone('Asia/Jakarta')
        jakarta_now = utc_now.astimezone(jakarta_tz)
        print("Timezone: Asia/Jakarta")
        print(f"Tanggal: {jakarta_now.strftime('%Y-%m-%d')}")
        print(f"Waktu: {jakarta_now.strftime('%H:%M:%S.%f')}")
        inner()
        utc_now = datetime.datetime.now(pytz.utc)
        jakarta_now = utc_now.astimezone(jakarta_tz)
        print(f"Tanggal: {jakarta_now.strftime('%Y-%m-%d')}")
        print(f"Waktu: {jakarta_now.strftime('%H:%M:%S.%f')}")

    return inner_decorator

@my_decorator
def decorated():
    print("\nBerubah Menjadi\n")

if __name__ == "__main__":
    print("===========================\nNama: Agfan Herru Pratama Hendarsin ||\nNim: 064002100043        ||\n===========================")
    decorated()
