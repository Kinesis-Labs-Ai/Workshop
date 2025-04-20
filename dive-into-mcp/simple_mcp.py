from mcp.server.fastmcp import FastMCP

# Initialize our MCP server with a friendly name
mcp = FastMCP("Simple Boredom Test")


@mcp.tool()
def hello_world() -> str:
    """A simple hello world test."""
    return "Hello from MCP server!"


@mcp.resource("info://about")
def get_info() -> str:
    """Get information about this MCP server."""
    return "This is a simple test server."


# Run the server
if __name__ == "__main__":
    print("Starting simple test server...")
    mcp.run(port=8000)
