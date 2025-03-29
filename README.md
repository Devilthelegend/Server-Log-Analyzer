Overview

The Server Log Analyzer is a Python-based tool that processes log files to:

Count occurrences of each log level (INFO, WARNING, ERROR, DEBUG).

Retrieve the most recent log entry for a specified log level.

Filter logs within a given date range and save the results to a file.

Features

Parses logs from a text file (logs.txt).

Counts log levels and displays their occurrences.

Finds and prints the most recent log entry for a specific log level.

Filters logs based on user-defined start and end dates.

Saves filtered logs to filtered_logs.txt.

Requirements

Ensure you have Python 3.12.2 or later installed.

Install Dependencies

This script only relies on Python’s built-in modules. However, ensure you have Python installed by running:

python --version

Setup Instructions

Clone the repository or download the script files.

git clone https://github.com/Devilthelegend/Server-Log-Analyzer.git
cd Server-Log-Analyzer


Ensure that your log file (logs.txt) is placed in the project directory.

Run the script:

python log_analyzer.py

Usage Instructions

The script will automatically parse logs.txt and display log level counts.

Enter a log level (INFO, WARNING, ERROR, DEBUG) when prompted.

The most recent entry for the selected log level will be displayed.

Enter the start and end dates (YYYY-MM-DD) to filter logs.

The filtered logs will be displayed and saved in filtered_logs.txt.

Expected Output Example

Log Level Counts:
INFO: 2
WARNING: 2
ERROR: 2
DEBUG: 1
Enter log level to search: ERROR
Most Recent ERROR Entry:
2025-01-10 09:35:20 ERROR Timeout occurred
Enter start date (YYYY-MM-DD): 2025-01-10
Enter end date (YYYY-MM-DD): 2025-01-10
Filtered Logs (Saved to filtered_logs.txt):
2025-01-10 09:23:45 INFO Application started
2025-01-10 09:25:00 WARNING Disk space low
2025-01-10 09:26:30 ERROR Unable to connect to database
2025-01-10 09:30:15 INFO User logged in
2025-01-10 09:35:20 ERROR Timeout occurred
2025-01-10 09:40:05 WARNING CPU usage high

Troubleshooting

Ensure logs.txt is formatted correctly with timestamps, log levels, and messages.

If you get an error related to date parsing, check your date input format (YYYY-MM-DD).

If no logs appear in the filtered results, verify the date range in logs.txt.

License

This project is licensed under the MIT License.

Author

Pratik Jagzap
Email: pratikjagzap530@gmail.com
