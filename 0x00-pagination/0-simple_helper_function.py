#!/usr/bin/env python3
"""index_range that takes 2 integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range that takes 2 integer arguments page and page_size"""
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
