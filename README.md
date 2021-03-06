# DiscordServerBot

## A Discord server bot that can be run inside a Docker container

### Downloading

You can download the project in one of three ways: by cloning the project from
[GitHub](https://github.com/Ryan-M-Smith/DiscordServerBot), by pulling the latest Docker image from my
[Docker Hub](https://hub.docker.com/r/ryanmsmith144/discordserverbot), or by pulling an image from [GitHub
Packages](https://github.com/Ryan-M-Smith?tab=packages&repo_name=DiscordServerBot).

```sh
# Clone from GitHub
git clone https://github.com/Ryan-M-Smith/DiscordServerBot.git

# Pull from Docker Hub (pulls tag latest by default)
docker pull ryansmith144/discordserverbot

# To pull a specific tag (I don't suggest using latest):
docker pull ryanmsmith144/discordserverbot:<tagname>

# To pull from GitHub packages.
docker pull ghcr.io/ryan-m-smith/discordserverbot:<tagname>
```

### Prerequisites

**Python Version:** If you use the Docker container, by default the code is built using Python 3.6. I chose
to default it to this to support users with older Python versions. You can change this and use a newer version
simply by modifying the Dockerfile and uncommenting the version you want. Be sure to comment out the other one though,
unless you want to fetch more than one Python version.

**Packages:** To run the bot, you'll need to have all of the `pip`/PyPi packages installed. If you plan to run the
code with Docker, you'll also need to have  `docker` and `docker-compose` installed. No matter what method you choose,
all `pip` requirements will be automatically installed (by either `setup.py` or `docker-compose`).

### Supported Platforms

The code should work fine on Linux, macOS, and Windows computers.

### Running

To run a Discord bot, you need a Discord account and a registered Discord application. You'll also need access to a server
where you have member access or higher. There's a tutorial [here](https://discordpy.readthedocs.io/en/latest/discord.html)
that can help you with all the setup (i.e., getting a bot set up on your server). Technically, this isn't a bot. It's code
that runs using a bot on your server and allows it to do certain things.

Before you run the project, you need to put your bot's token and the name of your server into the `.env` file
in the project's root directory. When you do this, your `.env` should look like this:

```sh
DISCORD_TOKEN=<YOUR_TOKEN> # There shouldn't be quotes around this
DISCORD_SERVER="My Server's Name" # Quotes are okay here
```

If you're using the Docker image, just reproduce the `.env` file above in your home directory, or wherever is most
convenient for you.

If you plan to use any method involving Docker, consider these things:

* Make sure `docker` and `docker-compose` are installed on your system
* Enable the `docker` service with `sudo systemctl enable --now docker`
* If you want to be able to run Docker without sudo, run `sudo groupadd docker` then
  `sudo usermod -aG docker $USER`

Once you have everything downloaded and set up, you can choose to run the project by:

1. Pull and run an image of the Docker container from Docker Hub
    * Run `docker run -p 80:80 ryanmsmith144/discordserverbot:<TAGNAME> --env-file /path/to/env/file`
      * You can use whatever port and tag you choose
      * You can make a `.env` file on your system and put the necessary information in there,
        or you can use `--env` and pass in everything in the command itself. If you plan to
        make your own `.env` file, see the one in the root directory of this project for a
        template.

2. Building an image of the project's Docker container and running it

    * Clone the repo and `cd` into the directory
    * Run `docker-compose up` to build and run the project
      * The code runs forever, so use `ctrl+c` to exit
      * Once you close the container, use `docker run --env-file .env serverbot` to run
      * Should you ever need to rebuild, run `docker-compose up --build`

3. Using `setup.py install` and running a Python application

    * Run `python3 setup.py install`
      * Run this as root (`sudo`) to install the program in the `/usr/local/lib/.../site-packages`
      * Run this with the `--user` flag to install the program in `~/.local/lib/.../site-packages`
    * Run `serverbot` in your terminal

### Capabilities

The bot can perform actions within your server (like greeting users) as well as custom slash (/)
commands. To learn more about what the bot can do, see
[usage.md](https://github.com/Ryan-M-Smith/DiscordServerBot/blob/master/doc/usage.md).

### More Info

To learn more about the project, see
[software-info.md](https://github.com/Ryan-M-Smith/DiscordServerBot/blob/master/doc/software-info.md).
