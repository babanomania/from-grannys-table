import os
import requests
import json
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class ImageSearchToolInput(BaseModel):
    """Input schema for ImageSearchTool."""
    argument: str = Field(..., description="query for searching images from Unsplash")

class ImageSearchTool(BaseTool):
    name: str = "search_public_images"
    description: str = "Search for CC0 licensed images from Unsplash"

    args_schema: Type[BaseModel] = ImageSearchToolInput

    def _run(self, argument: str) -> dict:
        url = f"https://api.unsplash.com/search/photos?query={argument}&client_id={os.getenv('UNSPLASH_ACCESS_KEY')}&per_page=1"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            if data['results']:
                return {
                    "url": data['results'][0]['urls']['regular'],
                    "attribution": f"Photo by {data['results'][0]['user']['name']} on Unsplash"
                }
        return None