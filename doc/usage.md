# Using the Bot

## A list of capabilites and commands

### Server Actions

The bot is able to greet users when they first join the server as well as notify
users when it comes online. This functionality may expand in the future.

### Slash Commands

A majority of the work on this projec has been put into custom slash commands. As you
can probably tell, these commands are invoked by typing `/command <parameters...>`.

The first chart is a list of all the possible command inputs and what number they are
represented by. In my parameter descriptions, I'll be using these numbers. I've provided
them here for reference.

The second chart contains all the currently implemented commands, their parameters
(and what type of input each one takes), and a description of the command's usage.

#### Parameter Types ([source](https://discord.com/developers/docs/interactions/slash-commands#applicationcommandoptiontype>))

| Parameter Type    | Number   |
| ----------------- | :------: |
| SUB_COMMAND       | 1        |
| SUB_COMMAND_GROUP | 2        |
| STRING            | 3        |
| INTEGER           | 4        |
| BOOLEAN           | 5        |
| USER              | 6        |
| CHANNEL           | 7        |
| ROLE              | 8        |
| MENTIONABLE       | 9        |

#### Command List

When reading parameters, make sure you know what the numbers mean (see the chart above)
and know that any parameter name followed by a question mark is **optional**. Most commands
with optional arguments have default parameters for those arguments that will be used if one
is not supplied by the caller. The default values of optional parameters are given with an equal
sign after the parameter type.

**TL;DR:** `<parameter?: 4 = 10>`

* `parameter`: parameter name
* `?`: optional parameter
* `4`: parameter type
* `10`: parameter default value

| Command    | Parameters        | Description |
| ---------- | ----------------- | ----------- |
| `/8ball`   | `<question: 3>`   | Simulate a magic 8-ball. The question parameter is required, but is only for show and isn't used for  anything |
| `/calm`    | None              | Notify the server that a user has entered a calm (zen) state. This command creates and applies the Zen role to the user who invokes it.  |
| `/greet`   | `@<member: 9>`    | Greet a server member. You can use an @-mention, but it isn't required. The username itself is sufficient.     |
| `/info`    | None              | Give info about the server you're on.                                                                          |
| `/ping`    | `<times?: 4 = 1>` | Ping the bot (sends a response with the time it took to recieve the command).                                  |
| `/rage`    | None              | Notify the server that a user has entered a rage state.                                                        |
| `/random`  | `<lower?: 4 = -sys.maxsize> <upper?: 4 = sys.maxsize>` | Pick a random number in the range [`lower`, `upper`]                      |
| `/roll`    | `<count?: 4 = 1> <sides?: 4 = 6>` | Roll `count` `sides`-sided dice (default 1 6-sided die)                                        |
