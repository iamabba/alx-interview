import sys

def print_statistics(stats):
    print("File size:", stats["total_size"])
    for status_code in sorted(stats["status_codes"]):
        if status_code in ["200", "301", "400", "401", "403", "404", "405", "500"]:
            print(f"{status_code}: {stats['status_codes'][status_code]}")

def compute_metrics():
    stats = {
        "total_size": 0,
        "status_codes": {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
    }
    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            line = line.strip()
            parts = line.split()
            if len(parts) >= 7 and parts[5].startswith("GET") and parts[6].isdigit():
                status_code = parts[6]
                file_size = int(parts[7])
                stats["total_size"] += file_size
                if status_code in stats["status_codes"]:
                    stats["status_codes"][status_code] += 1

            if line_count % 10 == 0:
                print_statistics(stats)

    except KeyboardInterrupt:
        print_statistics(stats)

if __name__ == "__main__":
    compute_metrics()
