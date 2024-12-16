# Instagram Password Reset API Tool

This tool is a Python script designed to interact with Instagram's password reset API. It simulates sending a password reset request for an account and provides clear feedback on the operation's outcome, using color-coded messages.

## Features

- **Dynamic Input**: Prompts the user to input an email or username for password reset.
- **Status Feedback**:
  - **Green Text**: Indicates a successful request, showing the status code and input details.
  - **Red Text**: Indicates a failure, with details about the status code and reason for the failure.
- **Error Handling**: Handles common HTTP errors, such as timeouts and failed requests, gracefully.

## Requirements

- Python 3.7+
- Required libraries:
  - `requests`: For making HTTP requests.
  - `termcolor`: For color-coded terminal output.

Install dependencies using pip:
```bash
pip install requests termcolor
```

## Usage

1. Clone or download the script to your local machine.
2. Run the script using Python:
   ```bash
   python script_name.py
   ```
3. Enter the email or username of the Instagram account when prompted:
   ```
   Enter your email or username: example_username
   ```
4. Observe the output:
   - **Success Example**:
     ```
     200 | example_username | successfully sent reset mail
     ```
   - **Failure Example**:
     ```
     408 | Request timeout | The server did not respond in time
     ```

## How It Works

1. The script sends a POST request to Instagram's password reset API endpoint (`/api/v1/web/accounts/account_recovery_send_ajax/`).
2. The request includes:
   - Required headers, such as `User-Agent`, `X-Csrftoken`, and others.
   - A payload containing the `email_or_username` field.
3. The response is analyzed:
   - A 200 status code triggers a success message.
   - Any other status code or exception triggers a failure message, with details.

## Example Output

### Success
```bash
200 | example_username | successfully sent reset mail
```

### Failure (Timeout)
```bash
408 | Request timeout | The server did not respond in time
```

### Failure (Other Errors)
```bash
400 | Request failed | Invalid email or username
```

## Notes

- **Educational Purpose Only**: Ensure you comply with Instagram's API policies and terms of service.
- **Session Validity**: The script requires valid session headers (e.g., `csrftoken`, `Cookie`) to work. These values are static and might need to be updated for the script to function.

## License

This tool is distributed for educational purposes and is not affiliated with Instagram. Use responsibly.
