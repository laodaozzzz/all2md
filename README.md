# all2md

[English](#english) | [中文](#中文)

---

## English

Batch convert common document formats to Markdown. Powered by [markitdown](https://github.com/microsoft/markitdown).

### Supported Formats

| Format | Extension |
|--------|-----------|
| Word | `.docx` |
| PowerPoint | `.pptx` |
| Excel | `.xlsx` |
| PDF | `.pdf` |

### Installation

```bash
pip install markitdown
```

### Usage

Place `all2md.py` in the target folder, then run:

```bash
python all2md.py
```

The script scans the current directory for all supported files and generates a `.md` file for each.

### Example

```
📁 my_docs/
├── report.docx
├── slides.pptx
├── data.xlsx
└── all2md.py
```

After running:

```
📁 my_docs/
├── report.docx
├── report.md        ← generated
├── slides.pptx
├── slides.md        ← generated
├── data.xlsx
├── data.md          ← generated
└── all2md.py
```

---

## 中文

批量将常见文档格式转换为 Markdown。基于 [markitdown](https://github.com/microsoft/markitdown)。

### 支持格式

| 格式 | 扩展名 |
|------|--------|
| Word | `.docx` |
| PowerPoint | `.pptx` |
| Excel | `.xlsx` |
| PDF | `.pdf` |

### 安装

```bash
pip install markitdown
```

### 使用

将 `all2md.py` 放到目标文件夹，然后运行：

```bash
python all2md.py
```

脚本会扫描当前目录下所有支持的文件，转换后生成同名 `.md` 文件。

### 示例

```
📁 my_docs/
├── report.docx
├── slides.pptx
├── data.xlsx
└── all2md.py
```

运行后：

```
📁 my_docs/
├── report.docx
├── report.md        ← 生成
├── slides.pptx
├── slides.md        ← 生成
├── data.xlsx
├── data.md          ← 生成
└── all2md.py
```

---

## License

MIT
