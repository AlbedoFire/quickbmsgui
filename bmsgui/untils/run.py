import subprocess


def run_long_process(command):
    # 启动进程
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True  # 以文本形式输出
    )

    # 实时读取输出
    try:
        while True:
            # 从标准输出读取一行
            output = process.stdout.readline()
            if output:
                print(output.strip())  # 打印输出

            # 检查进程是否结束
            if process.poll() is not None:
                break

        # 获取任何剩余的输出
        remaining_output, _ = process.communicate()
        if remaining_output:
            print(remaining_output.strip())

    except KeyboardInterrupt:
        print("进程被中断")
        process.terminate()

    # 确保进程正常结束
    process.wait()


