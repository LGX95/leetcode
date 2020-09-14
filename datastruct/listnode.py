#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Data Struct of ListNode
"""

from __future__ import annotations  # for ListNode type hint
from typing import List, Optional


class ListNode:
    """Definition for singly-linked list.
    """
    def __init__(self, val: int = 0, nxt: Optional[ListNode] = None):
        self.val = val
        self.next = nxt

    def __str__(self):
        return f'{self.val} -> {self.next}'

    @classmethod
    def from_list(cls, array: List[int]) -> Optional[ListNode]:
        curr = dummy = cls()
        for i in array:
            curr.next = cls(i)
            curr = curr.next
        return dummy.next
