class User: 
    def __init__(self, id_user, username, password, email, nomor_telepon): 
        self.id_user = id_user 
        self.username = username 
        self.password = password 
        self.email = email 
        self.nomor_telepon = nomor_telepon 
 
    def update_profile(self, username=None, email=None, 
nomor_telepon=None): 
        """Update user profile""" 
        if username: 
            self.username = username 
        if email: 
            self.email = email 
        if nomor_telepon: 
            self.nomor_telepon = nomor_telepon 
        print("Profile updated successfully.") 
 
    def view_properties(self, properties): 
        """View list of properties (Kos or Kontrakan)""" 
        for property_item in properties: 
            property_item.display_details() 
 
    def book_property(self, property_item): 
        """Method for booking a property""" 
        print(f"{self.username} booked {property_item.nama}.") 
 
class Property: 
    def __init__(self, id_property, nama, id_mitra, nomor_telepon, 
fasilitas, alamat, harga, foto): 
        self.id_property = id_property 
        self.nama = nama 
        self.id_mitra = id_mitra 
        self.nomor_telepon = nomor_telepon 
        self.fasilitas = fasilitas 
        self.alamat = alamat 
        self.harga = harga 
        self.foto = foto 
 
    def update_info(self, fasilitas=None, alamat=None, harga=None): 
        """Update property information""" 
        if fasilitas: 
            self.fasilitas = fasilitas 
        if alamat: 
            self.alamat = alamat 
        if harga: 
            self.harga = harga 
        print(f"Information for {self.nama} updated.") 
 
    def display_details(self): 
        """Display property details""" 
        print(f"Nama: {self.nama}, Harga: {self.harga}, Alamat: 
{self.alamat}, Fasilitas: {self.fasilitas}") 
 
class Kos(Property): 
    pass 
 
class Kontrakan(Property): 
    pass 
 
class Admin: 
    def __init__(self, id_admin, username, password, email, nomor_telepon): 
        self.id_admin = id_admin 
        self.username = username 
        self.password = password 
        self.email = email 
        self.nomor_telepon = nomor_telepon 
 
    def add_property(self, property_list, new_property): 
        """Add a new property (Kos or Kontrakan) to the system""" 
        property_list.append(new_property) 
        print(f"New property {new_property.nama} added by admin 
{self.username}.") 
 
    def remove_property(self, property_list, property_id): 
        """Remove a property by ID""" 
        property_list[:] = [p for p in property_list if p.id_property != 
property_id] 
        print(f"Property with ID {property_id} removed by admin 
{self.username}.") 
 
class Mitra: 
    def __init__(self, id_mitra, nama_mitra, nomor_telepon, email, alamat, 
password, nomor_rekening): 
        self.id_mitra = id_mitra 
        self.nama_mitra = nama_mitra 
        self.nomor_telepon = nomor_telepon 
        self.email = email 
        self.alamat = alamat 
        self.password = password 
        self.nomor_rekening = nomor_rekening 
 
    def add_property(self, property_list, new_property): 
        """Add a new property (Kos or Kontrakan)""" 
        property_list.append(new_property) 
        print(f"New property {new_property.nama} added by mitra 
{self.nama_mitra}.") 
 
    def update_property(self, property_item, fasilitas=None, alamat=None, 
harga=None): 
        """Update property information""" 
        property_item.update_info(fasilitas=fasilitas, alamat=alamat, 
harga=harga) 
        print(f"Property {property_item.nama} updated by mitra 
{self.nama_mitra}.") 
 
user1 = User(id_user=1, username="Paez", password="password123", 
email="@Gmail.com", nomor_telepon="08123456789") 
 
property1 = Property(id_property=101, nama="Kos Harmoni", id_mitra=201, 
nomor_telepon="08123456789", 
                     fasilitas="AC, WiFi", alamat="Jalan Mawar No. 10", 
harga=1500000, foto="foto_kos.jpg") 
 
admin1 = Admin(id_admin=1, username="admin_user", password="adminpass", 
email="admin@example.com", nomor_telepon="08987654321") 
 
properties = [] 
admin1.add_property(properties, property1) 
 
user1.view_properties(properties) 
 
user1.book_property(property1) 