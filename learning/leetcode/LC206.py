# -*- coding: utf-8 -*-
# LeetCode 206 - 反转链表
# 运行: python learning/leetcode/LC206.py
#
# 题目: 把 1 -> 2 -> 3 -> 4 -> None  变成  4 -> 3 -> 2 -> 1 -> None
#
# ============================================================
# 第一步: 什么是链表？（从零讲）
# ============================================================
#
# 链表就像「火车」——每节车厢（Node）装着货（data），
# 但它只知道下一节车厢是谁（next），不知道整辆车的样子。
#
#   车厢1       车厢2       车厢3       终点
#   [1|●]  →   [2|●]  →   [3|●]  →   None
#    ↑ 车厢号    ↑ 车厢号    ↑ 车厢号    ↑ 没了=结尾
#
#   ● = next指针 = 指向下一节车厢


class Node:
    """链表的一节「车厢」"""
    def __init__(self, val):
        self.val = val    # 车厢里装的货（数据）
        self.next = None  # 指向下一节车厢（默认没有下一节）

    def __repr__(self):
        return f"Node({self.val})"


# ============================================================
# 第二步: 徒手造一条链表
# ============================================================

# 造 3 节车厢: 1 → 2 → 3 → None
a = Node(1)
b = Node(2)
c = Node(3)

# 把它们连起来
a.next = b   # 1 后面是 2
b.next = c   # 2 后面是 3
# c.next 默认为 None，表示终点

# 这个 a 就是「头节点」，顺着 a 一路 .next 就能走完整个链表
print("原链表:")
node = a
while node:
    print(f"  {node.val}", end="")
    if node.next:
        print(" → ", end="")
    node = node.next
print(" → None")
# 输出: 1 → 2 → 3 → None


# ============================================================
# 第三步: 反转链表（核心）
# ============================================================
#
# 目标: 把 a(1)→b(2)→c(3)→None 变成 c(3)→b(2)→a(1)→None
#
# 关键想法（一句话）:
#   让每个节点的 next 掉头，指向前一个节点！
#
# 准备 3 根「手指」指着不同的车厢:
#   prev  ← 已经掉好头的部分的头
#   curr  ← 正在掉头的那个车厢
#   nxt   ← 还没处理的下一节车厢（提前记好，别弄丢了）
#
# 图解过程（读代码时对照着看）:
#
#   初始状态:
#         prev=None    curr=a(1)     nxt=??
#         (空的)       ↓             ↓
#                      [1|●]→[2|●]→[3|●]→None
#
#   第1步: 记下下一节 nxt = curr.next  (拍照存证，免得回头找不到了)
#   第2步: 让当前车厢掉头 curr.next = prev  (1.next 从指向2 变成指向None)
#   第3步: prev 往前走一步  prev = curr
#   第4步: curr 往前走一步  curr = nxt
#
#         完成后:
#         None←[1]    prev=1    curr=2    nxt=2
#
#   然后循环重复上面的4步...直到 curr 走到 None（链表尽头）
#
#   最终: None←[1]←[2]←[3]  ← 全部掉头完成
#                       ↑ prev 指向新的头


def reverse_list(head):
    """反转链表，返回新的头节点"""
    prev = None   # 上一个节点（一开始没有，就是 None）
    curr = head   # 当前节点（从头开始）

    while curr is not None:  # 只要还没走完
        nxt = curr.next      # ① 拍照：记下下一个节点
        curr.next = prev     # ② 掉头：让当前节点指向前一个
        prev = curr          # ③ 前进一步
        curr = nxt           # ④ 前进一步

    # 循环结束时 curr = None，prev 就是新的头
    return prev


# 测试
new_head = reverse_list(a)

print("\n反转后:")
node = new_head
while node:
    print(f"  {node.val}", end="")
    if node.next:
        print(" → ", end="")
    node = node.next
print(" → None")
# 期望输出: 3 → 2 → 1 → None


# ============================================================
# 第四步: LeetCode 官方格式
# ============================================================
#
# LeetCode 给你的是头节点 head，你要返回新的头节点。
# 上面那个 reverse_list 就是 LeetCode 能直接提交的答案。
# 下面是 LeetCode 上的最终版本：

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next   # 存好下一个
            curr.next = prev  # 掉头
            prev = curr       # 往前走
            curr = nxt        # 往前走
        return prev


# ============================================================
# 第五步: 慢慢看每一步发生了什么
# ============================================================
print("\n" + "=" * 50)
print("慢动作回放：每一步的细节")
print("=" * 50)

# 重新造一条链表
a2 = Node(1)
b2 = Node(2)
c2 = Node(3)
a2.next = b2
b2.next = c2

prev = None
curr = a2
step = 0

while curr:
    step += 1
    nxt = curr.next  # 拍照存证
    print(f"\n第{step}步:")
    print(f"  当前车厢 curr = {curr.val}")
    print(f"  它的下一节 nxt = {nxt.val if nxt else 'None'} ← 提前记下，别丢了")
    print(f"  掉头前: {curr.val}.next → {curr.next.val if curr.next else 'None'}")
    curr.next = prev  # 掉头
    print(f"  掉头后: {curr.val}.next → {prev.val if prev else 'None'} ← 指回去了！")
    prev = curr
    curr = nxt
    print(f"  移动后: prev={prev.val}, curr={curr.val if curr else 'None'}")

print(f"\n反转完成！新头是 prev = {prev.val}")
print("顺着新头走一遍验证一下...")

node = prev
parts = []
while node:
    parts.append(str(node.val))
    node = node.next
print("  " + " -> ".join(parts) + " -> None [OK]")


# ============================================================
# 记忆口诀
# ============================================================
print("\n" + "=" * 50)
print("四句口诀，记住反转链表:")
print("  记下下一个（nxt = curr.next）")
print("  掉头指向前（curr.next = prev）")
print("  前进一步（prev = curr）")
print("  再进一步（curr = nxt）")
print("=" * 50)
