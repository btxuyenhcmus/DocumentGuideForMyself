# Một số lưu ý khi phát triễn dự án odoo
1. Khi chỉ cần lấy id của một record thông qua **env** thì nên dùng `_search`
```
# example:
order_line = self.env['sale.order.line']._search([('name', '=', str)], limit=1)

# Result:
This will return for you an integer array [id]
```
2. Khi bạn cần lấy một record thông qua **env** thì nên dùng `search` vì khi gọi `search` thì nó sẽ gọi hàm `_search` trước tiên rồi sẽ gọi hàm `browse` để load các record tương ứng với các *id* trả về từ hàm `_search`.
```
# Example:
order_line = self.env['sale.order.line'].search([('name', '=', str)], limit=1)

# Result:
This will return for you an object array [sale.order.line(id, )]
```
3. Khi viết các button write state cho các record thì cần lưu ý kiểm tra điều kiện trước khi `write` vì khi có nhiều client cùng lúc tác động nếu không check điều kiện dẫn đến bị `write` nhiều lần.
```
# Example
# Don't right:
self.write({
    'state': received,
})

# Right:
self.filtered({lambda rec: rec.state == 'draft'}).write({
    'state': received
})
```
> Vì khi có nhiều client cùng truy cập một pages, khi client thứ nhất write trạng thái của record nhưng bên client thứ 2 vì còn lưu cache nên button đó không mất đi và vẫn thực hiện được action của button. Code như trên để tránh được việc đó.
4. Khi cần lấy những dòng dữ liệu trong fields **one2many** với điều kiện đơn giản thì thay vì dùng **loop** ta nên dùng *filtered*
```
# Practice with calculating number of line in order have state is done
count = len(self.order_line_ids.filtered(lambda line: line.state == 'done'))

# It will return an number that less greater than len(self.order_line_ids)
```
Đế lấy ra danh sách id, hay name hay bất cứ thuộc tính nào ta có thể dùng mapped
```
self.order_line_ids.filtered(lambda line: line.state == 'done').mapped('product_id')
```
5. Các thao tác với fields **one2many** đặc biệt:
    - (0, 0, { values }) link to a new record that needs to be created with the given values dictionary
    - (1, ID, { values }) update the linked record with id = ID (write *values* on it)
    - (2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
    - (3, ID) cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
    - (4, ID) link to existing record with id = ID (adds a relationship)
    - (5) unlink all (like using (3, ID) fr all linked records)
    - (6, 0, [IDs]) replace the list of linked IDs (like using (5) then (4, ID) for each ID in the list of IDs)
```
# Example
tracking.receipt_line_ids = [(0, 0, {
    'name': name,
    'product_id': product_id.id,
    'state': 'received
})]
```