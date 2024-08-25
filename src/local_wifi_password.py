import subprocess
from typing import List

def run_command(keywords: List[str]) -> List[str]:
    """Runs a shell command and returns the output as a list of lines."""
    return subprocess.check_output(keywords).decode('utf-8').splitlines()

def extract_value_from_row(row: str) -> str:
    """Extracts and returns the value after the colon in a given row."""
    return row.split(":", 1)[1].strip()

def get_wifi_profiles(data: List[str]) -> List[str]:
    """Extracts Wi-Fi profile names from the command output data."""
    key_sentence = "All User Profile"
    profiles = []

    for row in data:
        if key_sentence in row:
            profile = extract_value_from_row(row)
            profiles.append(profile)

    return profiles

def get_profile_key_content(profile: str) -> List[str]:
    """Retrieves the Wi-Fi profile key content using the provided profile name."""
    keywords = ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']
    data = run_command(keywords)
    key_contents = []

    for row in data:
        if "Key Content" in row:
            key_content = extract_value_from_row(row)
            key_contents.append(key_content)

    return key_contents

def display_profile_key(profile: str, key_content: str) -> None:
    """Displays the Wi-Fi profile and its key content."""
    print(f"{profile:<30}| {key_content}")

def main() -> None:
    keywords = ['netsh', 'wlan', 'show', 'profiles']
    data = run_command(keywords)
    profiles = get_wifi_profiles(data)

    for profile in profiles:
        key_contents = get_profile_key_content(profile)
        if key_contents:
            display_profile_key(profile, key_contents[0])
        else:
            display_profile_key(profile, "No key content found")

if __name__ == "__main__":
    main()
