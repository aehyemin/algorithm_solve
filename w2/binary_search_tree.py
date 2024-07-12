# __future__ 미래 버전의 기능을 쓸 수 있음
# __init__ 클래스의 생성자. self 를 첫번째 매개변수로 사용


 







# def search(self,key:Any) -> Any:
#     #키가 key인 노드 검색
#     p = self.root
#     while True:
#         if p is None:
#             return None
#         if key == p.key:
#             return p.value
#         elif key < p.key:
#             p = p.left
#         else :
#             p = p.right
            


# from __future__ import annotations
# from typing import Any, Type

# class Node:
#     def __init__(self, key:Any, value:Any, left:Node =None, right:Node = None):
#         self.key = key
#         self.value = value
#         self.left = left
#         self.right = right 

# class BinarySearchTree:

#     def __init__(self):
#         self.root = None