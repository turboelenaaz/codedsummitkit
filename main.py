"""logger_eff7fb - Generator pipeline."""
import itertools, json
PIPE_ID = "logger_eff7fb"
def source(n: int):
    for i in range(n): yield {"seq": i, "pipe": PIPE_ID}
def transform(stream):
    for item in stream: yield {**item, "doubled": item["seq"] * 2, "even": item["seq"] % 2 == 0}
def sink(stream, limit: int = 5) -> list:
    return list(itertools.islice(stream, limit))
def main():
    pipeline = sink(transform(source(100)))
    print(f"[{PIPE_ID}] Pipeline output ({len(pipeline)} items):")
    for item in pipeline: print(f"  {json.dumps(item)}")
if __name__ == "__main__":
    main()
