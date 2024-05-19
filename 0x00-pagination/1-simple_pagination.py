#!/usr/bin/env python3
"""get_page that takes 2 integer arguments page with default value 1"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """get_page that takes 2 int arg page with default value 1"""
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """get_page that takes 2 int arg page with default value 1"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """get_page that takes 2 int arg page with default value 1"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page that takes 2 int arg page with default value 1"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
