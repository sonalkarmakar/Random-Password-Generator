__all__ = [
	"load_markdown",
]

def load_markdown(file_path: str):
	with open(file_path, 'r', encoding="utf-8") as f:
		return f.read()