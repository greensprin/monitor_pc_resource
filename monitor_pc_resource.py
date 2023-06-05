import subprocess
import psutil
import time

def get_disk_active_time():
    # コマンドプロンプトのtypeperfコマンドでディスクの状況を取得する
    disk_usage = subprocess.run('typeperf "\PhysicalDisk(_Total)\% Disk Time" -sc 1', shell=True, capture_output=True, text=True).stdout

    # 以下のsplit, replaceが正しく動いてなさそうな場合は、上記のコマンドを直接コマンドプロンプトに入力してみて、どんな戻り値になっているかを確認する
    date_and_time    = disk_usage.split('\n')[2].split(',')[0].replace("\"", "")
    disk_active_time = disk_usage.split('\n')[2].split(',')[1].replace("\"", "")

    return date_and_time, disk_active_time

def print_and_output_log(log, f):
    print(log.replace("\n", ""))
    f.write(log)

def main():
    # disk情報を取得できるようになるコマンドを実行
    subprocess.run("diskperf -y", shell=True)

    with open("monitor_pc_resource.csv", "w") as f:
        print_and_output_log("Date, CPU Usage[%], Memory Usage[%], Disk Usage[%]\n", f)

        # 5秒に1回しかデータ取得しないので、ピークの使用率には弱い (time.sleepの数値を小さくしても、コマンド実行に時間がかかるので結局5秒程度はかかる)
        # ただし、PC動作が重い時は常にどれかが忙しい状態になっているはずと思うので特に対策しない
        while(True):
            cpu_usage = psutil.cpu_percent()
            mem_usage = psutil.virtual_memory().percent
            date_and_time, disk_active_time = get_disk_active_time()

            print_and_output_log(f"{date_and_time}, {cpu_usage}, {mem_usage}, {disk_active_time}\n", f)

            time.sleep(5)


if __name__ == "__main__":
    main()