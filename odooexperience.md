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
6. Tạo User cho từng module
```
# Example for location module:
# Create category inside security folder of location module
<record id="module_location_category" model="ir.module.category">
    <field name="name">Location</field>
</record>

# Create User Group
<record id="group_location_user" model="ir.groups">
    <field name="name">User</field>
    <field name="category_id" ref="module_location_category"/>
    <field name="implied_ids" eval="[(4, ref('base.group_user'))]"/>
</record>

# Create Manager Group
<record id="group_location_manager" model="ir.groups">
    <field name="name">Manager</field>
    <field name="category_id" ref="module_location_category"/>
    <field name="implied_ids" eval="[(4, ref('group_location_user'))]"/>
    <field name="users" eval=[(4, ref('base.user_root')),
                              (4, ref('base.user_admin'))]/>
</record>
```
> Define header of csv
**id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink**
7. dict vals in *create* and *write*
Nếu muốn xét xem field nào đó có giá trị được cung cấp hay không ta cần kiểm tra đầu vào có nó hay không trước khi thực hiện **TODO**
```
# Example
def write(self, vals):
    if not vals.get('lat') and not vals.get('long'):
        return super(Location, self).write(vals)
```
Nghĩa là nếu như khi một location được update nhưng không có thông tin update của tọa độ lat long thì không thực hiện những thao tác tiếp theo với tọa độ.
**Note:**
    - Hàm super create sẽ trả về  True/False nếu việc tạo dữ liệu thành công/không thành công. Hàm super write sẽ trả về record sau khi đã update.
    - Khi thực hiện việc update thông tin của dữ liệu nếu chỉ update một field đơn lẻ thì có thể dùng `write` hay việc gán bình thường. *Nhưng* khi thay đổi thông tin của nhiều field cùng một lúc thì nên dùng `write` vì khi dùng phép gán nhiều lần thì nó sẽ gọi hàm write nhiều lần.
8. **googlemap**
```
import googlemaps

def get_google_map_key_api(self):
    return self.env['ir.config_parameter'].sudo().get_param('google.api_key_geocode')

def get_distance_from_google(self, start, end):
    api_key = self.get_google_map_key_api()

    gmaps = googlemaps.Client(key=api_key)

    origins = (start['lat'], start['long']) if type(start) is dict else (start.lat, state.long)
    destinations = (end['lat'], end['long']) if type(end) is dict else (end.lat, end.long)

    try:
        result = gmaps.distance_matrix(origins=origins, destinations=destinations)
    except Exception as e:
        # TODO
```
9. Sự khác biệt giữa `=`, `like`, `ilike`, `=like`, `=ilike`
    - **=**: 2 chuỗi hoàn toàn giống nhau.
    - **like**: chuỗi bên trái nằm bên trong chuỗi bên phải không phân biệt hoa thường.
    - **=like**: chuỗi bên trái bằng chuỗi bên phải *không* phân biệt hoa thường.
    - **ilike**: chuỗi bên trái nằm bên trong chuỗi bên phải *có* phân biệt hoa thường.
    - **=ilike**: chuỗi bên trái bằng chuỗi bên phải *có* phân biệt hoa thường.
10. Doing with **context**:
    - get context with current woking `self.env.context.get('fields', False)` - Nghĩa là nó sẽ lấy giá trị của fields, nêu không có thì sẽ trả về *False*.
    - Thực hiện một action với context chỉ định `self.env.ref('module.actions).with_context({'fields': value}).action(self)`.
    - Gán biến context `ctx = dict(self._context) or {}`, nghĩa là lấy ra thông tin về context nếu không có thì trả về một dictionary rỗng.
11. Lấy đơn vị tiền tệ cho từng company
```
def _get_currency(self, cr, uid, context=None):
    user_obj = self.pool.get('res.users')
    currency_obj = self.pool.get('res.currency')
    user = user_obj.browse(cr, uid, uid, context=context)

    if user.company_id:
        return user.company_id.currency_id.id
    else:
        return currency_obj.search(cr, uid, [('rate', '=', 1.0)])[0]
```
12. Để check điều kiện ràng buộc các field trong module như ngày thàng bắt đầu nhỏ hơn ngày tháng kết thúc, nên dùng `constraint()` thay cho `onchange()` để bắt sự kiện.
13. Kế thừa một view và muốn thay đổi gì đó ở bản gốc thì chũng ta nên dùng `xpath`, với position như `after, before, replace, attributes`.
14. Differece between **models.Model** and **models.TransientModel**:
    - `models.Model` dùng cho các model chính và sẽ được lưu trong database mãi mãi đến khi có thao tác xóa dữ liệu trong database.
    - `models.TransientModel` dùng cho các model tạm thời (Temporary) như tạo cái *wizard* và nó chỉ được lưu trong một thời gian quy định.
15. Thao tác với dữ liệu
    - `self.env.cr.excute(sql)`
16. Thao tác với cron