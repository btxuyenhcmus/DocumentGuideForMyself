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
