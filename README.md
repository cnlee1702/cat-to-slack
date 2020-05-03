Cat to Slack
============

Posts cat gifs to your Slack channel on a daily basis and makes your employees happy.


Prerequisites
-------------

- python 3.8.1

Configuration
-------------

Cat to Slack is configured through environment variables:

- `INCOMING_WEBHOOK_URL`

  Incoming webhook URL that you've set up in Slack.

- `CAT_CHANNEL`

  Channel to which the bot will post gifs (ex. `#cats`)

- `CAT_TIMES`

  Comma-separated list of times at which the cat gifs will be posted (ex `10:00,18:00`). These times are in the timezone of the process.

- `TZ`

  Optional timezone name in which the process will be run.