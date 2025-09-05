# Docker Notification System

A Python application that monitors Docker container events and sends notifications to Discord via webhooks.

## Features

- Real-time monitoring of Docker container events
- Discord notifications with embedded messages
- Role mentions for important alerts
- Configurable via environment variables
- Containerized deployment support

## Prerequisites

- Python 3.7+
- Docker
- Discord webhook URL
- Discord server with role permissions

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Copy the `.env` file and configure your settings:
   ```
   DISCORD_WEBHOOK_URL=your_discord_webhook_url_here
   DISCORD_ROLE_ID=your_discord_role_id_here
   ```

2. Replace the values with your actual Discord webhook URL and role ID

### Getting Discord Webhook URL

1. Go to your Discord server settings
2. Navigate to Integrations > Webhooks
3. Create a new webhook or use an existing one
4. Copy the webhook URL

### Getting Discord Role ID

1. Enable Developer Mode in Discord (User Settings > Advanced > Developer Mode)
2. Right-click on the role you want to mention
3. Select "Copy ID"

## Usage

### Running Locally

```bash
python DockerNotif.py
```

### Running with Docker

```bash
docker build -t docker-notif .
docker run -d --name docker-notif -v /var/run/docker.sock:/var/run/docker.sock docker-notif
```

### Using Setup Script

```bash
./setup.sh
```

## How It Works

1. The application connects to the Docker daemon
2. Listens for container events (start, stop, restart, etc.)
3. Formats event information into Discord embeds
4. Sends notifications to the configured Discord channel
5. Mentions the specified role for alerts

## Event Information

Each notification includes:
- Event type (start, stop, restart, etc.)
- Container name
- Container ID
- Timestamp
- Role mention for immediate attention

## Security Notes

- Keep your `.env` file secure and never commit it to version control
- Ensure your Discord webhook URL is kept private
- The application requires access to Docker socket for monitoring

## Troubleshooting

- Ensure Docker is running and accessible
- Verify Discord webhook URL is correct
- Check that the Discord role ID exists and is valid
- Confirm the bot has permissions to mention the role

## Dependencies

- `docker` - Docker SDK for Python
- `requests` - HTTP library for webhook calls
- `python-dotenv` - Environment variable management