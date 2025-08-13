import h5py

# 源文件和目标文件路径
source_path = "static7.h5"
target_path = "cm7.h5"

with h5py.File(source_path, "r") as src_file, h5py.File(target_path, "w") as dst_file:
    if "model" in src_file:
        # 遍历 model 组下的所有内容（子数据集/子组）
        for name in src_file["model"]:
            # 将内容从 src_file["model/name"] 复制到 dst_file["name"]
            src_file.copy(src_file["model"][name], dst_file, name=name)
        print("已复制 model 组内的所有内容到目标文件（不保留 model 组本身）")
    else:
        print(f'错误：{source_path} 中未找到 "model" 组')
# 文件会在 with 块结束后自动关闭