import re
import datetime

LOG_PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR|DEBUG) (.+)"

def parse_logs(file_path):
    """ Reads and parses the log file. """
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line.strip())
            if match:
                timestamp, log_level, message = match.groups()
                logs.append((datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"), log_level, message))
            else:
                print(f"Skipping malformed log entry: {line.strip()}")
    return logs

def count_log_levels(logs):
    """ Counts occurrences of each log level. """
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0}
    for _, log_level, _ in logs:
        log_counts[log_level] += 1
    return log_counts

def find_most_recent(logs, level):
    """ Finds the most recent log entry for a given level. """
    filtered_logs = [log for log in logs if log[1] == level]
    return max(filtered_logs, default=None, key=lambda x: x[0])

def filter_by_date(logs, start_date, end_date):
    """ Filters logs by date range, ignoring timestamps. """
    start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    filtered_logs = [log for log in logs if start_dt <= log[0].date() <= end_dt]

    with open("filtered_logs.txt", "w") as f:
        for log in filtered_logs:
            f.write(f"{log[0].strftime('%Y-%m-%d %H:%M:%S')} {log[1]} {log[2]}\n")
    
    return filtered_logs


if __name__ == "__main__":
    logs = parse_logs("logs.txt")
    
    
    log_counts = count_log_levels(logs)
    print("Log Level Counts:")
    for level, count in log_counts.items():
        print(f"{level}: {count}")


    level = input("Enter log level to search: ").strip().upper()
    if level in log_counts:
        recent_log = find_most_recent(logs, level)
        if recent_log:
            print("Most Recent", level, "Entry:")
            print(f"{recent_log[0].strftime('%Y-%m-%d %H:%M:%S')} {recent_log[1]} {recent_log[2]}")
        else:
            print(f"No logs found for level {level}")
    else:
        print("Invalid log level entered.")


    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()
    filtered_logs = filter_by_date(logs, start_date, end_date)
    if filtered_logs:
        print(f"Filtered Logs (Saved to filtered_logs.txt):")
        for log in filtered_logs:
            print(f"{log[0].strftime('%Y-%m-%d %H:%M:%S')} {log[1]} {log[2]}")
    else:
        print("No logs found in the given date range.")
