import os
from pathlib import Path
from markitdown import MarkItDown

def convert_all_to_md():
    # 初始化 MarkItDown 转换器
    md = MarkItDown()

    # 当前目录
    current_dir = Path(".")

    # 需要处理的扩展名
    exts = {".docx", ".pptx", ".xlsx", ".pdf"}

    for file in current_dir.iterdir():
        if file.suffix.lower() in exts and file.is_file():
            try:
                print(f"正在转换: {file.name}")
                result = md.convert(str(file))
                output_file = file.with_suffix(".md")
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(result.text_content)
                print(f"✅ 已生成: {output_file.name}")
            except Exception as e:
                print(f"❌ 转换失败 {file.name}: {e}")

if __name__ == "__main__":
    convert_all_to_md()
