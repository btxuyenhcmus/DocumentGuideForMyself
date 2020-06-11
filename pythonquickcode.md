# Python: trick gắn dọn cần ghi nhớ
Trong bài viết này, mình xin giới thiệu 1 số thủ thuật hay mà mình biết trong Python

1. Đảo ngược chuỗi trong python
```
>>> a = "codementor"
>>> print("Reverse is", a[::-1])
Reverse is rotnemedoc
```
2. Chuyển vị một ma trận
```
>>> mat = [[1, 2, 3], [4, 5, 6]]
>>> zip(*mat)
[(1, 4), (2, 5), (3, 6)]
```
3. Lưu trữ tất cả 3 giá trị của 1 list vào 3 biến mới
```
>>> a = [1, 2, 3]
>>> x, y, z = a
>>> x
1
>>> y
2
>>> z
3
```
4. Tạo một chuỗi đơn từ các phần tử trong mảng
```
>>> a = ["bui", "trong", "xuyen"]
>>> print(" ".join(a))
bui trong xuyen
```
5. Gọp 2 list lại với nhau thành 1 list tuple
```
...
>>> for x, y in zip(list1, list2):
....    print(x, y)
....
```
6. Hoán đổi 2 số chỉ trên một dòng code
```
>>> a, b = b, a
```
7. In ra **n** lần một **chuỗi** cố định
```
>>> print("xuyen" * 3)
xuyenxuyenxuyen
```
8. **Gán giá trị với điều kiện**
```
>>> True and 4 or 3
4
>>> False and 4 or 3
3
```
9. Chuyển đổi ma trận thành một single list
```
>>> a = [[1, 2], [3, 4], [5, 6]]
>>> import itertools
>>> list(itertools.chain.from_iterable(a))
[1, 2, 3, 4, 5, 6]
```
10. So sánh kép
```
>>> n = 10
>>> 1 < n <20
True
>>> 1 > n <= 9
False
```
11. **Phép gán 1 biến đi kèm với điều kiện**
```
def small(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)
>>> small(1, 0, 1)
1
```
12. **Toán từ `_`**
Toán tử  `_` sẽ trả về kết quả của biển thức cuối cùng được thực hiện
```
>>> 2 + 1
3
>>> _
3
>>> print(_)
3
```
13. Đơn giản hóa điều kiện if
```
>>> if m in list:
....    ...
>>> if m not in list:
....    ...
>>> if any(list):
....    ...
>>> if all(line.split is False for line in purchase.order_line):
....    ...
```
14. Enum trong pỵthon
```
class Shapes:
    Circle, Square, Triangle, Quadrangle = range(4)
>>> print(Shapes.Circle)
0
```
15. **Lambda** function
Lambda là một anonymous function *(hàm ẩn danh)* nó có thể khai báo, định nghĩa ở bất kỳ đâu và không có khả năng tái sử dụng.
- Lambda chỉ tổn tại trong phạm vi của biến mà nó được định nghĩa, vì vậy nếu như biến đó vượt ra ngoài phạm vi thif hàm này cũng không còn tác dụng nữa.
- Lambda thường được dùng để gán vào biến, hay được gán vào hàm, class như một tham số.
```
lambda agruments_list: expression

>>> add = lambda a, b: a + b
# call lambda
add(3, 4)
```
16. Tạo nhanh một list
```
>>> list = [key for key in range(5)]
[1, 2, 3, 4, 5]
>>> list = [1 for key in ranges(5)]
[1, 1, 1, 1, 1]
>>> list = [(key * 2 + 1) for key in range(5)]
[1, 3, 5, 7, 9]
```
17. Tìm giá trị lặp lại nhiều nhất trong list
```
>>> test = [4, 1, 2, 3, 2, 2, 3, 1, 4, 4, 4]
>>> max(set(test), key=test.count)
4
```
18. Đếm số lần xuất hiện trong list
```
>>> from collections import Counter
>>> mylist = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
>>> print(Counter(mylist))
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
```
19. Enumerate
```
>>> for key, value in enumerate(iterable):
....    print(key, value)
```
20. **switch**
Trong python không có `switch..case` nhưng ta có thể dùng dictionary để giái quyết vấn đề tương tự switch này.
```
>>> stdcalc = {'sum': lambda x, y: x + y, 'subtract': lambda x, y: x - y}
>>> print(stdcalc['sum'](9, 3))
12
>>> print(stdcalc['subtract'](9, 3))
6
```
21. Cách đọc datetime từ excel cho python
```
>>> from datetime import datetime
>>> serial = 43111.0
>>> seconds = (serial - 25569) * 86400
>>> date = datetime.fromtimestamp(seconds)
>>> datetime(2018, 1, 11, 0, 0)
```

