# Boredom Killer - MCP Server Guide

A fun MCP server that helps cure boredom with Kanye West quotes, jokes, advice, and trivia. Perfect for tech-savvy urban professionals who need a quick break from their day.

## What's Inside

This MCP server connects to four different APIs to deliver a variety of boredom-curing content:

1. **Kanye West Quotes** - Wisdom and musings from the iconic artist
2. **Chuck Norris Jokes** - Classic Chuck Norris one-liners
3. **Advice Slips** - Random pieces of wisdom for your day
4. **Number Trivia** - Fascinating facts about random numbers

Plus, you can save your favourites in each category and access them later!

## Setup Instructions

### Prerequisites
- Python 3.7+
- Claude Desktop
- An internet connection

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required packages:
   ```bash
   pip install mcp httpx
   ```

3. Save the `bored_mcp.py` file to your computer

### Connecting to Claude Desktop

1. Open Claude Desktop
2. Go to Settings → Developer → Edit Config
3. Add the configuration:

```json
   {
    "mcpServers": {
       "boredom-killer": {
        "name": "Boredom Killer",
        "command": "python",
        "args": ["C:\\Users\\user\\Desktop\\project\\mcp\\mcp-demo\\bored_mcp.py"],
        "description": "Cures boredom with activities, jokes, advice, and trivia"
      }
    }
  }  
```

4. Adjust the path to your script if needed
5. Save and restart Claude Desktop
6. Verify the server is connected in Settings → Developer

## Using with Claude

Once connected, you can ask Claude to use the Boredom Killer in natural language:

### Basic Commands

- "Share a Kanye West quote with me"
- "Tell me a Chuck Norris joke"
- "Give me some advice"
- "Share a random number fact"
- "Give me the full boredom-killing combo"

### Managing Favourites

- "Save that quote to my favourites"
- "Show me my favourite jokes"
- "What advice have I saved?"
- "Clear my saved trivia"
- "Show all my favourites"

### Getting Help

- "What can the Boredom Killer do?"
- "What tools does the Boredom Killer have?"

## Examples

Here are some example interactions:

---

**You**: Share a Kanye West quote with me.

**Claude**: Let me get you a Kanye quote.

Kanye says: "We came into a broken world. And we're the cleanup crew."

---

**You**: Tell me a Chuck Norris joke.

**Claude**: Here's a Chuck Norris joke for you:

Chuck Norris doesn't read books. He stares them down until he gets the information he wants.

---

**You**: Give me the full boredom-killing combo!

**Claude**: I'll prepare the ultimate boredom killer combo for you.

Never cut what you can untie.

73 is the 21st prime number.

Kanye says: "I feel like I'm too busy writing history to read it."

Chuck Norris can delete the Recycling Bin.

---

## Troubleshooting

If you encounter issues:

- Make sure your internet connection is working
- Check that the server is running (you should see it in the terminal)
- Verify Claude Desktop is properly configured
- Restart the server and Claude Desktop

## Extending the Server

Want to add more features? Here are some ideas:

- Add more API integrations (dad jokes, motivational quotes, etc.)
- Create themed combinations (e.g., "Wisdom Combo" with philosophical quotes)
- Add categories for quotes and jokes
- Implement a rating system for your favourites

## Enjoy!

Now you have a fun way to cure boredom with the help of Claude and MCP. The Boredom Killer brings you Kanye wisdom, jokes, advice, and trivia - all through a simple chat interface.
