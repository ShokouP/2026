/*
 * LeetCode 206 - Reverse Linked List (反转链表)
 *
 * 题目: Input:  1 -> 2 -> 3 -> 4 -> 5 -> nullptr
 *       Output: 5 -> 4 -> 3 -> 2 -> 1 -> nullptr
 *
 * 编译: /c/msys64/mingw64/bin/g++ -std=c++17 -o lc206.exe LC206.cpp
 * 运行: ./lc206.exe
 *
 * ============================================================
 * 第一讲: 什么是链表？
 * ============================================================
 *
 * 链表就是「火车」。
 *
 *   [1|->]     [2|->]     [3|->]     [4|->]     [5|  ]
 *   车厢         车厢        车厢       车厢        车厢
 *   ^data       ^data       ^data      ^data       ^data
 *       ^next       ^next       ^next       ^next      ^next = nullptr (终点)
 *
 * 每节车厢（Node）只知道自己:
 *   1. 装着什么东西 (val)
 *   2. 下一节车厢在哪 (next 指针)
 *
 * 关键区别:
 *   Python: self.val, self.next, None
 *   C++:    val, next (是 node* 类型的指针), nullptr
 *           要用 new 创建节点，用指针来指
 *
 * ============================================================
 * 第二讲: C++ 里的指针是什么？
 * ============================================================
 *
 * 指针 = 一张写着「某个东西的位置」的便签纸
 *
 *   int x = 42;       // x 是一块内存，装着 42
 *   int* p = &x;      // p 是一张便签纸，写着 "x 在 XXXX 号位置"
 *   cout << *p;       // *p = "我去便签上写的地址把东西取出来" → 42
 *   cout << p;        // p  = "便签上写的地址本身" → 0x7ffe...
 *
 * 在链表里:
 *   Node* node = new Node(1);  // 火车站调度员说"新车厢1号停到D-3站台"
 *   node->val = 1;             // 去D-3站台，打开车厢，放1进去
 *   node->next = nextNode;     // 把下一节车厢的站台号写在车门上
 *
 *   -> 就是「先去便签上的地址，再进门拿东西」，Python 里的 . 的指针版
 *
 * ============================================================
 */

#include <iostream>
#include <vector>
using namespace std;


// --------- 定义车厢 ----------
struct ListNode {
    int val;            // 车厢里的货
    ListNode *next;     // 下一节车厢的站台号（指针）

    // C++ 的「造车厢说明书」(构造函数)
    // Python: def __init__(self, val=0, next=None)
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *n) : val(x), next(n) {}
};


// ============================================================
// 第三讲: 造一条链表（和 Python 对比）
// ============================================================

// Python 版:
//   a = Node(1); b = Node(2); c = Node(3)
//   a.next = b; b.next = c

ListNode* makeList(vector<int> nums) {
    // 虚拟头节点(dummy)技巧: 先造一节空车厢，最后去掉
    // 好处: 不用单独处理「链表还是空的」情况
    ListNode dummy(0);          // 空车厢，不开出门，只是造车指挥所
    ListNode* tail = &dummy;   // tail 指着最后一节车厢（一开始只有指挥所）

    for (int val : nums) {
        tail->next = new ListNode(val);   // 新车厢挂上去
        tail = tail->next;                // tail 移到新车厢
    }

    return dummy.next;  // 返回真正的第一节车厢（甩掉指挥所）
}

// 打印链表
void printList(ListNode* head) {
    if (!head) {
        cout << "[empty]" << endl;
        return;
    }
    ListNode* curr = head;
    while (curr) {
        cout << curr->val;
        if (curr->next) cout << " -> ";
        curr = curr->next;
    }
    cout << " -> nullptr" << endl;
}


// ============================================================
// 第四讲: 反转链表（核心算法）
// ============================================================
/*
 * 一句话: 让每个节点的箭头（next）反着指
 *
 * 看下面这个图（从左向右读）:
 *
 *   nullptr <- 1 <- 2 <- 3   本质就是 node.next 方向变了
 *
 * 怎么做? 需要 3 根手指同时指着不同地方:
 *
 *   prev  ← 已经掉好头的那些车厢的头
 *   curr  ← 正在掉头的车厢
 *   nxt   ← 下一节还没处理的车厢（提前记住，免得弄丢了）
 *
 * 初始状态:
 *   prev = nullptr     (还没开始掉头，所以「已经掉好头的链」是空的)
 *   curr = head        (从第一节开始)
 *
 * 循环每次做 4 件事:
 *   1. nxt = curr->next      拍照: 把下一节提前记下
 *   2. curr->next = prev     掉头: 让当前车厢的箭头指向后面
 *   3. prev = curr           前移
 *   4. curr = nxt            前移
 *
 * 图解一步:
 *
 *   掉头前:   prev=nullptr    curr=[1|->2]    nxt=??
 *            nullptr          [1|->] [2|->] [3|->] nullptr
 *
 *   第1步:    nxt = [2]       ← 拍照，记住下一节位置
 *   第2步:    1 -> nullptr    ← 反向！
 *            nullptr <- [1]      [2|->] [3|->] nullptr
 *
 *   第3步:    prev = [1]
 *   第4步:    curr = [2]
 *
 *   重复上面 4 步，直到 curr == nullptr（走到尽头）
 *   最后 prev 就是新的头节点
 */

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;   // 已经掉头完成的部分的头
    ListNode* curr = head;      // 正在处理的节点

    while (curr != nullptr) {
        ListNode* nxt = curr->next;   // 1. 拍照存好下一个
        curr->next = prev;             // 2. 掉头！指向前一个
        prev = curr;                   // 3. prev 前进
        curr = nxt;                    // 4. curr 前进
    }

    return prev;  // 新的头
}


// ============================================================
// 第五讲: LeetCode 提交格式
// ============================================================

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }

        return prev;
    }
};


// ============================================================
// 第六讲: 慢动作回放
// ============================================================
void slowMotionDemo() {
    cout << "\n===========================================" << endl;
    cout << "慢动作回放: 反转 [1, 2, 3]" << endl;
    cout << "===========================================" << endl;

    ListNode* a = new ListNode(1);
    ListNode* b = new ListNode(2);
    ListNode* c = new ListNode(3);
    a->next = b;
    b->next = c;

    cout << "初始链表: ";
    printList(a);

    ListNode* prev = nullptr;
    ListNode* curr = a;
    int step = 0;

    while (curr) {
        step++;
        ListNode* nxt = curr->next;  // 1. 拍照
        cout << "\n第" << step << "步:" << endl;
        cout << "  curr = " << curr->val << endl;
        cout << "  它的 next = " << (nxt ? to_string(nxt->val) : "nullptr");
        cout << "  ← 拍照存好，别丢了" << endl;
        cout << "  掉头前: " << curr->val << ".next -> ";
        cout << (curr->next ? to_string(curr->next->val) : "nullptr") << endl;

        curr->next = prev;           // 2. 掉头

        cout << "  掉头后: " << curr->val << ".next -> ";
        cout << (prev ? to_string(prev->val) : "nullptr");
        cout << "  ← 箭头反过来了！" << endl;

        prev = curr;                 // 3. 前进
        curr = nxt;                  // 4. 前进

        cout << "  移动后: prev=" << prev->val;
        cout << ", curr=" << (curr ? to_string(curr->val) : "nullptr") << endl;
    }

    cout << "\n反转完成! 新头 = " << prev->val << endl;
    cout << "验证: ";
    printList(prev);

    // 清理内存（C++ 需要自己删，Python 不需要）
    ListNode* node = prev;
    while (node) {
        ListNode* tmp = node;
        node = node->next;
        delete tmp;
    }
}


// ============================================================
// 口诀
// ============================================================

int main() {
    cout << "===========================================" << endl;
    cout << "LeetCode 206 -- Reverse Linked List" << endl;
    cout << "===========================================" << endl;

    // 造一条链表: [1, 2, 3, 4, 5]
    ListNode* head = makeList({1, 2, 3, 4, 5});

    cout << "\n原链表: ";
    printList(head);

    // 反转
    head = reverseList(head);

    cout << "反转后: ";
    printList(head);

    // 慢动作回放
    slowMotionDemo();

    // 清理内存
    while (head) {
        ListNode* tmp = head;
        head = head->next;
        delete tmp;
    }

    cout << "\n===========================================" << endl;
    cout << "四句口诀:" << endl;
    cout << "  拍照存好下一个 (nxt = curr->next)" << endl;
    cout << "  箭头反着指     (curr->next = prev)" << endl;
    cout << "  挪一步         (prev = curr)" << endl;
    cout << "  再挪一步       (curr = nxt)" << endl;
    cout << "===========================================" << endl;

    return 0;
}
