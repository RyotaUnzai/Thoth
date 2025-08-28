from pathlib import Path
from typing import Any

from pydantic import BaseModel


class IconItemModel(BaseModel):
    display_name: str
    asset_version: int
    image_url: Path
    last_author: str
    file_update_time: str
    authors: list[str] 

    @classmethod
    def from_json(cls, data: dict[str, Any], base_dir: Path) -> "IconItemModel":
        image_url = Path(data["image_url"])
        if not image_url.is_absolute():
            image_url = base_dir / image_url
        data = data.copy()
        data["image_url"] = image_url
        return cls(**data)
