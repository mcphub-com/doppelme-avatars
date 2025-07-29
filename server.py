import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/wavesong/api/doppelme-avatars'

mcp = FastMCP('doppelme-avatars')

@mcp.tool()
def list_assets(bodytype_id: Annotated[Union[int, float], Field(description='Body type identification number (e.g. 1101) Default: 1101')],
                assettype: Annotated[str, Field(description='Asset type (e.g. top)')]) -> dict: 
    '''Returns a list of assets available given a bodytype and assettype'''
    url = 'https://doppelme-avatars.p.rapidapi.com/assets/1101/eye'
    headers = {'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'bodytype_id': bodytype_id,
        'assettype': assettype,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_asset_types(bodytype_id: Annotated[Union[int, float], Field(description='Body type identification number (e.g. 1101) Default: 1101')]) -> dict: 
    '''Return list of asset types that are available for the given body type identifier.'''
    url = 'https://doppelme-avatars.p.rapidapi.com/assets/1101'
    headers = {'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'bodytype_id': bodytype_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_body_types() -> dict: 
    '''Returns a list of avatar body types that are available to choose when creating your avatar'''
    url = 'https://doppelme-avatars.p.rapidapi.com/bodytypes'
    headers = {'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def create_avatar(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Create a new DoppelMe avatar. On successful creation, you will receive a doppelme_key. Use this key and the Update Avatar endpoint to specify clothes, hairstyles etc.'''
    url = 'https://doppelme-avatars.p.rapidapi.com/avatar/1101'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_avatar(doppelme_key: Annotated[str, Field(description='The id of the avatar you wish to delete')]) -> dict: 
    '''Delete created avatar.'''
    url = 'https://doppelme-avatars.p.rapidapi.com/avatar/DM123456ABC'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'doppelme_key': doppelme_key,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def add_asset_item(doppelme_key: Annotated[str, Field(description='The identifier of the avatar that you wish to update.')],
                   asset_id: Annotated[Union[int, float], Field(description='The asset_id that you wish to add to your avatar Default: 59')]) -> dict: 
    '''Add an item to your avatar. Note that you can only update avatars that you have created yourself.'''
    url = 'https://doppelme-avatars.p.rapidapi.com/avatar/DM1670714VMJWTG/59'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'doppelme_key': doppelme_key,
        'asset_id': asset_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.put(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def add_asset_colour(doppelme_key: Annotated[str, Field(description='The id of the avatar that you wish to update')],
                     asset_type: Annotated[str, Field(description='Specify the asset type (e.g. top, hair etc.)')],
                     colour: Annotated[str, Field(description='Colour in 6-digit hex format')]) -> dict: 
    '''Set the colour of asset (if asset is colourable). Note that you can only update avatars that you have created yourself.'''
    url = 'https://doppelme-avatars.p.rapidapi.com/avatar/DM1670714VMJWTG/top/FF0000'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'doppelme_key': doppelme_key,
        'asset_type': asset_type,
        'colour': colour,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.put(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def remove_asset(doppelme_key: Annotated[str, Field(description='The identifier of the avatar that you wish to update.')],
                 asset_type: Annotated[str, Field(description='The asset type (e.g.top, hair) to be removed from the avatar')]) -> dict: 
    '''Remove an item from an avatar. Note that you can only update avatars that you have created yourself.'''
    url = 'https://doppelme-avatars.p.rapidapi.com/avatar/DM1670714VMJWTG/top'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'doppelme_key': doppelme_key,
        'asset_type': asset_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.put(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def set_skin_colour(doppelme_key: Annotated[str, Field(description='The id of the avatar that you wish to update')],
                    colour: Annotated[str, Field(description='Colour in 6-digit hex format')]) -> dict: 
    '''Change the skin colour of your avatar. Note that you can only edit avatars that you have created yourself'''
    url = 'https://doppelme-avatars.p.rapidapi.com/avatar/DM1670714VMJWTG/skin/E9CBB9'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'doppelme-avatars.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'doppelme_key': doppelme_key,
        'colour': colour,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.put(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
