# Need Tex / pdfjam
# Use for pdf margin

import subprocess
from pathlib import Path

def margin_pdf(input_pdf, margin_top, margin_right, margin_bottom, margin_left):
    # 移除路径中的额外引号
    input_pdf = input_pdf.strip("'\"")  # 去掉单引号和双引号

    # 自动生成输出文件路径
    input_path = Path(input_pdf)
    output_pdf = input_path.parent / f"{input_path.stem}-1{input_path.suffix}"

    # 动态生成 margin_size 字符串
    margin_size = f"{margin_left}cm {margin_top}cm {margin_right}cm {margin_bottom}cm"

    # 构建pdfjam命令
    command = [
        "pdfjam",
        "--fitpaper", "true",
        "--trim", margin_size,
        input_pdf,  # 使用处理后的路径
        "-o", str(output_pdf)
    ]

    # 执行命令
    try:
        subprocess.run(command, check=True)
        print(f"PDF已成功处理并保存到 {output_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"处理PDF时出错: {e}")
    except FileNotFoundError:
        print("未找到 pdfjam 命令，请确保已安装 pdfjam 或 Tex 包。")

if __name__ == "__main__":
    # 获取用户输入的边距值
    print("请输入边距值（单位：cm）：")
    margin_top = input("Top Margin (Default: 0cm): ") or "0"
    margin_right = input("Right Margin (Default: -5cm): ") or "-5"
    margin_bottom = input("Bottom Margin (Default: 0cm): ") or "0"
    margin_left = input("Left Margin (Default: 0cm): ") or "0"

    # 获取用户输入的文件路径
    input_pdf = input("PDF Path: ")

    # 处理PDF
    margin_pdf(input_pdf, margin_top, margin_right, margin_bottom, margin_left)