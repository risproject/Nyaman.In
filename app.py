import os

# Kelas untuk Node dalam Linked List
class Node:
    def __init__(self, property_data):
        self.data = property_data
        self.next = None

# Kelas untuk Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, property_data):
        new_node = Node(property_data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        if not current:
            print("Tidak ada data properti.")
            return
        print("\nDaftar Properti:")
        print(f"{'No.':<5} {'Nama Properti':<25} {'Jenis':<10} {'Alamat':<30} {'Harga':<10} {'Fasilitas':<20} {'Status':<20}")
        print("-" * 120)
        index = 1
        while current:
            print(f"{index:<5} {current.data['Nama Properti']:<25} {current.data['Jenis']:<10} {current.data['Alamat']:<30} {current.data['Harga']:<10} {current.data['Fasilitas']:<20} {current.data['Status']:<20}")
            current = current.next
            index += 1

    def display_by_type(self, property_type):
        current = self.head
        filtered_properties = []
        while current:
            if current.data["Jenis"] == property_type:
                filtered_properties.append(current.data)
            current = current.next
        if not filtered_properties:
            print(f"Tidak ada properti dengan jenis '{property_type}'.")
            return
        print("\nDaftar Properti dengan Jenis", property_type)
        print(f"{'No.':<5} {'Nama Properti':<25} {'Jenis':<10} {'Alamat':<30} {'Harga':<10} {'Fasilitas':<20} {'Status':<20}")
        print("-" * 120)
        for index, property_data in enumerate(filtered_properties, start=1):
            print(f"{index:<5} {property_data['Nama Properti']:<25} {property_data['Jenis']:<10} {property_data['Alamat']:<30} {property_data['Harga']:<10} {property_data['Fasilitas']:<20} {property_data['Status']:<20}")

    def display_sorted_by_price(self):
        current = self.head
        properties = []
        while current:
            properties.append(current.data)
            current = current.next
        sorted_properties = sorted(properties, key=lambda x: x['Harga'])
        if not sorted_properties:
            print("Tidak ada data properti.")
            return
        print("\nDaftar Properti diurutkan berdasarkan Harga Terendah:")
        print(f"{'No.':<5} {'Nama Properti':<25} {'Jenis':<10} {'Alamat':<30} {'Harga':<10} {'Fasilitas':<20} {'Status':<20}")
        print("-" * 120)
        for index, property_data in enumerate(sorted_properties, start=1):
            print(f"{index:<5} {property_data['Nama Properti']:<25} {property_data['Jenis']:<10} {property_data['Alamat']:<30} {property_data['Harga']:<10} {property_data['Fasilitas']:<20} {property_data['Status']:<20}")

    def update(self, property_name, new_data):
        current = self.head
        while current:
            if current.data['Nama Properti'] == property_name:
                current.data.update(new_data)
                print(f"Data properti '{property_name}' berhasil diupdate.")
                return
            current = current.next
        print("Properti tidak ditemukan.")

    def delete(self, property_name):
        current = self.head
        prev = None
        while current:
            if current.data['Nama Properti'] == property_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Data properti '{property_name}' berhasil dihapus.")
                return
            prev = current
            current = current.next
        print("Properti tidak ditemukan.")

    def verify(self, index):
        current = self.head
        current_index = 1
        while current:
            if current_index == index:
                current.data['Status'] = 'Terverifikasi'
                print(f"Data properti '{current.data['Nama Properti']}' telah diverifikasi.")
                return
            current = current.next
            current_index += 1
        print("Indeks tidak valid. Pastikan Anda memasukkan nomor yang benar.")

# Daftar peran yang tersedia
roles = ["mitra", "user", "administrator"]

# Fungsi untuk menampilkan menu login
def login_menu():
    while True:
        print("------------------------------------")
        print("Login sebagai (mitra, user, administrator)")
        user_role = input("Login: ").strip().lower()
        print("------------------------------------")
        
        if user_role in roles:
            os.system('cls' if os.name == 'nt' else 'clear')
            return user_role
        else:
            print("Role tidak valid. Silakan masukkan role yang benar.")

# Menampilkan menu sesuai role
def show_mitra_menu(properties):
    while True:
        print("\nMenu Mitra:")
        print("1. Tambah Properti")
        print("2. Lihat Properti")
        print("3. Update Properti")
        print("4. Hapus Properti")
        print("5. Berganti Role")
        choice = input("Pilih opsi (1-5, ketik 'ESC' untuk kembali): ")

        if 'esc' in choice.lower():
            os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar
            return None  # Kembali ke menu login
            
        if choice == "1":
            # Menambah properti
            property_data = {
                "Nama Properti": input("Nama Properti: "),
                "Jenis": "Kost" if input("Jenis (1: Kost, 2: Kontrakan): ") == "1" else "Kontrakan",
                "Alamat": input("Alamat: "),
                "Harga": int(input("Harga: ")),
                "Fasilitas": input("Fasilitas: "),
                "Status": "Belum Terverifikasi"  # Default status
            }
            properties.append(property_data)
            os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar setelah menambah properti
            print("Properti berhasil ditambahkan.")
            
        elif choice == "2":
            # Melihat properti
            properties.display()
            
        elif choice == "3":
            # Mengupdate properti
            property_name = input("Nama Properti yang ingin diupdate: ")
            new_data = {}
            new_data["Nama Properti"] = input("Nama Properti baru: ")
            new_data["Jenis"] = "Kost" if input("Jenis baru (1: Kost, 2: Kontrakan): ") == "1" else "Kontrakan"
            new_data["Alamat"] = input("Alamat baru: ")
            new_data["Harga"] = int(input("Harga baru: "))
            new_data["Fasilitas"] = input("Fasilitas baru: ")
            properties.update(property_name, new_data)
            
        elif choice == "4":
            # Menghapus properti
            property_name = input("Nama Properti yang ingin dihapus: ")
            properties.delete(property_name)
            
        elif choice == "5":
            return None  # Kembali ke menu login
            
        else:
            print("Opsi tidak valid. Silakan pilih opsi yang benar.")

def show_user_menu(properties):
    while True:
        print("\nMenu User:")
        print("1. Tampilkan Data")
        print("2. Tampilkan berdasarkan jenis (1. Kost 2. Kontrakan)")
        print("3. Tampilkan urutan berdasarkan harga terendah")
        print("4. Berganti Role")
        choice = input("Pilih opsi (1-4, ketik 'ESC' untuk kembali): ")

        if 'esc' in choice.lower():
            os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar
            return None  # Kembali ke menu login
            
        if choice == "1":
            # Tampilkan data properti
            properties.display()
            
        elif choice == "2":
            # Tampilkan berdasarkan jenis
            jenis = input("Masukkan jenis (1: Kost, 2: Kontrakan): ")
            property_type = "Kost" if jenis == "1" else "Kontrakan" if jenis == "2" else None
            if property_type:
                properties.display_by_type(property_type)
            else:
                print("Jenis tidak valid.")
                
        elif choice == "3":
            # Tampilkan urutan berdasarkan harga terendah
            properties.display_sorted_by_price()
            
        elif choice == "4":
            return None  # Kembali ke menu login
            
        else:
            print("Opsi tidak valid. Silakan pilih opsi yang benar.")

def main():
    # Membuat linked list untuk menyimpan properti
    properties = LinkedList()
    
    # Menu login
    role = login_menu()

    if role == "mitra":
        show_mitra_menu(properties)
    elif role == "user":
        show_user_menu(properties)
    elif role == "administrator":
        print("Menu Administrator belum tersedia.")

if __name__ == "__main__":
    main()
