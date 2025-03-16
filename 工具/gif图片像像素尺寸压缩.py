from PIL import Image

# 打开GIF图片
input_gif = "original_image.gif"
output_gif = "compressed_resized.gif"

frames = []
target_size = (231, 200)  # 目标尺寸
with Image.open(input_gif) as img:
    # 提取所有帧并调整大小
    while True:
        frame = img.copy()
        frame = frame.resize(target_size)  # 调整帧大小
        frames.append(frame)
        try:
            img.seek(len(frames))  # 移动到下一帧
        except EOFError:
            break

    # 保存为GIF
    frames[0].save(
        output_gif,
        save_all=True,
        append_images=frames[1:],
        duration=200,
        loop=0,
        optimize=True,
    )

print("GIF尺寸调整完成！")