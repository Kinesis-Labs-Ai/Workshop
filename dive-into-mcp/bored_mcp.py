# This is an MCP demo. Read the README.md attached to the repo if you don't know how to run it. 
# You would have installed basic stuff, and let the client handle everything else. 


import httpx
import random
import asyncio
from mcp.server.fastmcp import FastMCP, Context

# Initialize our MCP server with a friendly name
mcp = FastMCP("Boredom Killer")

# API endpoints
KANYE_API = "https://api.kanye.rest/"
CHUCK_NORRIS_API = "https://api.chucknorris.io/jokes/random"
ADVICE_API = "https://api.adviceslip.com/advice"
NUMBERS_API = "http://numbersapi.com/random/trivia"

# Dictionary to track favorites
favorites = {"quotes": [], "jokes": [], "advice": [], "trivia": []}


@mcp.tool()
async def kanye_wast_quotes(ctx: Context) -> str:
    """Gets a random Kanye West quote to inspire or amuse."""
    ctx.info("Finding you a Kanye West quote...")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(KANYE_API)

            if response.status_code != 200:
                return "Sorry, I couldn't get a Kanye quote right now."

            data = response.json()
            quote = data.get("quote", "")

            return f"Kanye says: {quote}"
    except Exception as e:
        return f"Error getting a Kanye quote: {str(e)}"


@mcp.tool()
async def chuck_norris_joke(ctx: Context) -> str:
    """Gets a random Chuck Norris joke."""
    ctx.info("Finding a Chuck Norris joke...")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(CHUCK_NORRIS_API)

            if response.status_code != 200:
                return "Chuck Norris is too busy right now for jokes."

            data = response.json()
            joke = data.get("value", "")

            return f"Joke: {joke}"
    except Exception as e:
        return f"Error getting a joke: {str(e)}"


@mcp.tool()
async def get_advice(ctx: Context) -> str:
    """Gets a random piece of advice."""
    ctx.info("Finding some wisdom for you...")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(ADVICE_API)

            if response.status_code != 200:
                return "The advice guru is meditating. Try again later."

            data = response.json()
            advice = data.get("slip", {}).get("advice", "")

            return f"Advice: {advice}"
    except Exception as e:
        return f"Error getting advice: {str(e)}"


@mcp.tool()
async def number_trivia(ctx: Context) -> str:
    """Gets a random number fact."""
    ctx.info("Finding a cool number fact...")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(NUMBERS_API)

            if response.status_code != 200:
                return "The numbers aren't adding up right now. Try again later."

            # Response is plain text
            trivia = response.text

            return f"Trivia: {trivia}"
    except Exception as e:
        return f"Error getting number trivia: {str(e)}"


@mcp.tool()
async def boredom_combo(ctx: Context) -> str:
    """Gets a random combination of Kanye quote, joke, advice, and number trivia."""
    ctx.info("Preparing the ultimate boredom killer combo...")

    tasks = [
        kanye_wast_quotes(ctx),
        chuck_norris_joke(ctx),
        get_advice(ctx),
        number_trivia(ctx),
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Filter out any errors
    valid_results = []
    for result in results:
        if isinstance(result, Exception):
            continue
        if isinstance(result, str):
            valid_results.append(result)

    if not valid_results:
        return "Everything's broken today. Maybe being bored isn't so bad after all?"

    # Shuffle the results for variety
    random.shuffle(valid_results)

    return "\n\n".join(valid_results)


@mcp.tool()
def save_favorite(category: str, content: str) -> str:
    """Save a favorite quote, joke, advice, or trivia."""
    if category.lower() not in ["quote", "joke", "advice", "trivia"]:
        return f"Unknown category: {category}. Please use 'quote', 'joke', 'advice', or 'trivia'."

    category_plural = f"{category.lower()}s"
    if category_plural == "advices":
        category_plural = "advice"

    if content in favorites[category_plural]:
        return f"This {category} is already in your favorites!"

    favorites[category_plural].append(content)
    return f"Added to your favorite {category_plural}!"


@mcp.tool()
def get_favorites(category: str = "") -> str:
    """Get your saved favorites by category or all."""
    if not category:
        # Return all favorites
        result = "Your Favorites:\n\n"

        for cat, items in favorites.items():
            if items:
                result += f"--- {cat.upper()} ---\n"
                for i, item in enumerate(items, 1):
                    result += f"{i}. {item}\n"
                result += "\n"

        if result == "Your Favorites:\n\n":
            return "You don't have any favorites saved yet."

        return result

    # Return specific category
    category_plural = f"{category.lower()}s"
    if category_plural == "advices":
        category_plural = "advice"
    elif category.lower() == "quote":
        category_plural = "quotes"

    if category_plural not in favorites:
        return f"Unknown category: {category}. Please use 'quote', 'joke', 'advice', or 'trivia'."

    if not favorites[category_plural]:
        return f"You don't have any favorite {category_plural} saved yet."

    result = f"Your Favorite {category_plural.upper()}:\n\n"
    for i, item in enumerate(favorites[category_plural], 1):
        result += f"{i}. {item}\n"

    return result


@mcp.tool()
def clear_favorites(category: str = "") -> str:
    """Clear your saved favorites by category or all."""
    if not category:
        # Clear all favorites
        for cat in favorites:
            favorites[cat] = []
        return "All favorites cleared!"

    # Clear specific category
    category_plural = f"{category.lower()}s"
    if category_plural == "advices":
        category_plural = "advice"
    elif category.lower() == "quote":
        category_plural = "quotes"

    if category_plural not in favorites:
        return f"Unknown category: {category}. Please use 'quote', 'joke', 'advice', or 'trivia'."

    favorites[category_plural] = []
    return f"Your favorite {category_plural} have been cleared!"


@mcp.resource("info://about")
def get_info() -> str:
    """Get information about this MCP server."""
    return """
     Boredom Killer MCP Server  
    
    This server helps cure boredom with Kanye West quotes, Chuck Norris jokes, 
    life advice, and number trivia.
    
    Available tools:
    
    - kanye_wast_quotes() - Gets a Kanye West quote
    - chuck_norris_joke() - Tells a Chuck Norris joke
    - get_advice() - Offers a piece of wisdom
    - number_trivia() - Shares an interesting fact about a random number
    - boredom_combo() - Gives you all of the above at once!
    
    Favorites Management:
    - save_favorite(category, content) - Save a favorite item
    - get_favorites(category) - View your saved favorites
    - clear_favorites(category) - Clear your favorites
    
    Example categories: "quote", "joke", "advice", "trivia"
    Leave category blank to affect all categories.
    """


# Run the server
if __name__ == "__main__":
    print(" Starting Boredom Killer MCP Server ")
    print(
        "This server helps cure boredom with Kanye West quotes, jokes, advice, and trivia."
    )
    print("Connect to it from Claude Desktop to start fighting boredom!")
    mcp.run()
