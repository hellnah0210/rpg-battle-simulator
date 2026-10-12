class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError ("Invalid quantity")
        else:
            if item_name in self.items:                 # Thêm hoặc cộng dồn vật phẩm
                self.items[item_name] += quantity
            else:
                self.items[item_name] = quantity
                                                             
        pass

    def use_item(self, item_name):
        if item_name not in self.items:            # Kiểm tra vật phẩm có tồn tại không
            print ("Item not found")
        else:                                           # Giảm số lượng đi 1
            self.items[item_name] -= 1
            print(f"Used: {item_name}")
            if self.items[item_name] == 0:              # Xóa nếu số lượng bằng 0
                del self.items[item_name]
                
       

    def show_inventory(self):
        if len(self.items) == 0:                    # Kiểm tra túi đồ trống
            print("Inventory is empty") 
        else:
            print("Inventory:")
            for item_name, quantity in self.items.items():        # Duyệt dictionary để hiển thị
                print(f" {item_name}: {quantity}" )
       