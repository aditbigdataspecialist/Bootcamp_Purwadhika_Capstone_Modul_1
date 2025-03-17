#lib rary yang dipakai
from tabulate import tabulate
import json

#membaca file json
with open("dataset.json", "r") as jsonFile:
    data_alat_tulis = json.load(jsonFile)

#read menu
def read_menu():
    while True:
        print(f'''read menu
            
List Menu :
1. Tampilkan seluruh data alat tulis.
2. Cari alat tulis berdasarkan id data.
3. Kambali ke menu utama.

            ''')
        while True:
            #try and except digunakan untuk menanggulangi eror sehingga program tidak akan force stop
            try:
                menu = int(input('Masukan angka menu yang ingin dijalankan : '))
                break
            except Exception as e:
                print(f'''input salah karena {e}''')
        if menu == 1 :
            menampilkan_seluruh_data()
        elif menu == 2:
            cari_data()
        elif menu == 3:
            input_keputusan=input('apakah anda ingin kembali kemenu utama (ya/tidak) : ')
            if input_keputusan in 'ya':
                menu_utama()
            else:
                read_menu()

        else:
            print(f'''
                  
opsi yang anda masukan tidak tersedia
                  
                  ''')
            
#(bagian read menu) tampilkan seluruh data
def menampilkan_seluruh_data():
    if data_alat_tulis != []:
        headers = data_alat_tulis[0].keys()
        #convert [{},{}] ke [[],[]]
        data = []
        for item in data_alat_tulis:
            data.append([*item.values()])
        #convert str.lower ke str.title
        for i in data:
            for j in i:
                if type(j)==str:
                    value = i.index(j)
                    i[value] = j.title()
        input_tampilan_data = input('Anda ingin data diurutkan secara ascending(data terbesar ke terkecil) / descending(data terkecil ke terbesar) : ')
        #soerting data ascending
        if input_tampilan_data in 'ascending':
            input_tampilan_data_ascending = input('tampilan data diurutkan dari terkecil ke terbesar berdasarkan id/harga/stock : ')
            #menampil kan data dalam bentuk tabel secara ascending berdsarkan id
            if input_tampilan_data_ascending in 'id':
                urut_menurut_id = sorted(data, key=lambda x: x[0])
                print(tabulate(urut_menurut_id, headers=headers, tablefmt='grid'))
            #menampil kan data dalam bentuk tabel secara ascending berdsarkan harga
            elif input_tampilan_data_ascending in 'harga':
                urut_menurut_harga = sorted(data, key=lambda x: x[2])
                print(tabulate(urut_menurut_harga, headers=headers, tablefmt='grid'))
            #menampil kan data dalam bentuk tabel secara ascending berdsarkan stock
            elif input_tampilan_data_ascending in 'stock':
                urut_menurut_stock = sorted(data, key=lambda x: x[3])
                print(tabulate(urut_menurut_stock, headers=headers, tablefmt='grid'))
        #sorting data descending
        else:
            input_tampilan_data_descending = input('tampilan data diurutkan dari terbesar ke terkecil berdasarkan id/harga/stock : ')
            #menampil kan data dalam bentuk tabel secara descending berdsarkan id
            if input_tampilan_data_descending in 'id':
                urut_menurut_id = sorted(data, key=lambda x: x[0],reverse=True)
                print(tabulate(urut_menurut_id, headers=headers, tablefmt='grid'))
            #menampil kan data dalam bentuk tabel secara descending berdsarkan harga
            elif input_tampilan_data_descending in 'harga':
                urut_menurut_harga = sorted(data, key=lambda x: x[2],reverse=True)
                print(tabulate(urut_menurut_harga, headers=headers, tablefmt='grid'))
            #menampil kan data dalam bentuk tabel secara descending berdsarkan stock
            elif input_tampilan_data_descending in 'stock':
                urut_menurut_stock = sorted(data, key=lambda x: x[3],reverse=True)
                print(tabulate(urut_menurut_stock, headers=headers, tablefmt='grid'))
    else:
        print('tidak terdapat data apapun')

#(bagian read menu) mencari data sesuai dengan primary key
def cari_data():
    list_pencarian = []
    if data_alat_tulis != []:
        while True:
            try:
                #input primary key
                pencarian = int(input('masukan id alat tulis : '))
                break
            except Exception as e:
                print(f'''input salah karena {e}''')
        for i in range(len(data_alat_tulis)):
            if pencarian == data_alat_tulis[i]['id']:
                list_pencarian.append({'id':data_alat_tulis[i]['id'],'nama':data_alat_tulis[i]['nama'],'harga':data_alat_tulis[i]['harga'],'stock':data_alat_tulis[i]['stock'],'tempet_penyimpanan':data_alat_tulis[i]['tempat_penyimpanan']})
        #bila list pencarian tidak kosong maka list pencarian akan menampilkan tabel sesuai dengan primary key
        if list_pencarian !=[]: #list_pencarian berisi data sesuai primary key
            print(f'''hasil pencarian sebagai berikut''')
            headers = list_pencarian[0].keys()
            data = []
            for item in list_pencarian:
                data.append([*item.values()])
            for i in data:
                for j in i:
                    if type(j)==str:
                        value = i.index(j)
                        i[value] = j.title()
            #menampilkan data dalam bentuk tabel berdasarkan primary key
            print(tabulate(data, headers=headers, tablefmt='grid'))
        else:
            print('pencarian tidak ditemukan')
    else:
        print('tidak terdapat data apapun')
#end off read menu

#create menu
def create_menu():
    while True:
        print(f'''create menu
            
List Menu :
1. Input jumlah data yang ingin ditambahkan
2. Kambali ke menu utama.

            ''')
        while True:
            try:
                menu = int(input('Masukan angka menu yang ingin dijalankan : '))
                break
            except Exception as e:
                print(f'''input salah karena {e}''')
        if menu == 1 :
            while True:
                try:
                    jumlah_data = int(input('Berapa jumlah data yang ingin anda tambahkan :'))
                    break
                except Exception as e:
                    print(f'''input salah karena {e}''')
            for i in range(jumlah_data):
                tambah_data()
        elif menu == 2:
            input_keputusan=input('apakah anda ingin kembali kemenu utama (ya/tidak) : ')
            if input_keputusan in 'ya':
                menu_utama()
            else:
                create_menu()

        else:
            print(f'''
                  
opsi yang anda masukan tidak tersedia
                  
                  ''')
            
#(bagian dari create menu)function untuk menambah data. data akan langsung tersimpan ke dataset
def tambah_data():
    list_pencarian = [] 
    while True:    
        try:
            #inout primary key
            input_id = int(input('masukan id alat tulis : '))
            if input_id ==0:
                print('input harus lebih bear dari 0')
                continue
            else:
                break
        except Exception as e:
            print(f'''input salah karena {e}''')
    for i in range(len(data_alat_tulis)):
        if input_id == data_alat_tulis[i]['id']:
            list_pencarian.append(data_alat_tulis[i]['id'])
    #bila primary key tidak duplikat proses menambah data akan dilanjutkan
    if list_pencarian ==[]: # bila duplikat list pencarian berisi data id yang sudah ada
        print('id tidak duplikat lanjut ke proses penambahan data')
        #input nama
        while True:
            list_pencarian_2 = []
            input_nama = input("masukan nama alat tulis dengan format 'nama_merek' : ").lower()#data str akan dirubag menjadi lower agar data yang dihasilkan lebuh rapih
            if len(input_nama)<3:
                print('tidak boleh kurang dari 3 huruf')#bila panjang string dari input kurang dari 3 maka user akan diminta input ulang
                continue
            else:
                for i in range(len(data_alat_tulis)):
                    if input_nama == data_alat_tulis[i]['nama']:
                        list_pencarian_2.append(data_alat_tulis[i]['nama'])
                if list_pencarian_2 ==[]:#bila tedapat nama yang sama dengan id yang berbeda maka user akan diminta menginputkan nama ulang
                    break
                else:
                    print('nama tidak boleh duplikat')
                    print(list_pencarian_2)
                    continue
        #input harga
        while True:
            try:
                input_harga = int(input('masukan harga alat tulis : '))
                if input_harga ==0:
                    print('input harus lebih besar dari 0')
                    continue
                else:
                    break
            except Exception as e:
                print(f'''input salah karena {e}''')
        #input stock
        while True:
            try:
                input_stock = int(input('masukan stock alat tulis : '))
                if input_stock ==0:
                    print('input harus lebih besar dari 0')
                    continue
                else:
                    break
            except Exception as e:
                print(f'''input salah karena {e}''')
        #input tempat penyimpanan
        while True:
            print(f'''pilih tempat penyimpanan anda
1. rak 1
2. rak 2
3. rak 3 ''')
            try:
                input_pilihan_tempat_penyimpanan = int(input('masukan tempat penyimpanan : '))
                if input_pilihan_tempat_penyimpanan ==1:
                    input_tempat_penyimpanan = 'rak 1'
                elif input_pilihan_tempat_penyimpanan ==2:
                    input_tempat_penyimpanan = 'rak 2'
                elif input_pilihan_tempat_penyimpanan ==3:
                    input_tempat_penyimpanan = 'rak 3'
                else:
                    print('tidak ada tempat penyimpanan dengan input tersebut')
                    continue
                break
            except Exception as e:
                print(f'''input salah karena {e}''')
        #input keputusan apakah data yang telah diinputkan akan disimpan atau tidak
        input_keputusan = input('apakah anda akan menyimpan data (ya/tidak) : ')
        if input_keputusan in'ya':
            data_alat_tulis.append({'id':input_id,'nama':input_nama,'harga':input_harga,'stock':input_stock,'tempat_penyimpanan':input_tempat_penyimpanan})
            print('data berhasil ditambahkan')
            #data yang ditambahkan akan langsung disimpan dalam bentuk json
            with open("dataset.json", "w") as jsonFile:
                json.dump(data_alat_tulis, jsonFile)
        elif input_keputusan in 'tidak':
            print('data tidak jadi ditambahkan')

    else:
        print('data telah tersedia')
#end of create menu

#update menu
def update_menu():
    while True:
        print(f'''update menu
            
List Menu :
1. Input jumlahdata yang ingin anda update.
2. Kambali ke menu utama.

            ''')
        
        while True:
            try:
                menu = int(input('Masukan angka menu yang ingin dijalankan : '))
                break
            except Exception as e:
                print(f'''input salah karena {e}''')

        if menu == 1 :
            jumlah_data = int(input('Berapa jumlah data yang ingin anda update : '))
            for i in range(jumlah_data):
                update_data()
        elif menu == 2:
            input_keputusan=input('apakah anda ingin kembali kemenu utama (ya/tidak) : ')
            if input_keputusan in 'ya':
                menu_utama()
            else:
                update_menu()
        else:
            print(f'''
                  
opsi yang anda masukan tidak tersedia
                  
                  ''')
            
#(bagian dari update menu) function untuk mengupdate data. data akan langsung tersimpan ke dataset
def update_data():
    list_pencarian = []
    while True:
        try:
            #input primary key
            id_alat_tulis = int(input('masukan id alat tulis : '))
            break
        except Exception as e:
            print(f'''input salah karena {e}''')

    for i in range(len(data_alat_tulis)):
        if id_alat_tulis == data_alat_tulis[i]['id']:
            list_pencarian.append(i)#bila primary key ditemukan list akan berisi indeks dari id yang tersedia
    #bila primary key ditemukan proses update data akan di lanjutkan
    if list_pencarian ==[]:
        print('data tidak tersedia')
    else:
        print('data tersedia lanjut ke proses update data')
        print('berikut ini adalah data yang akan di update')
        headers = data_alat_tulis[0].keys()
        data = []
        for item in [data_alat_tulis[list_pencarian[0]]]:
            data.append([*item.values()])
        for i in data:
            for j in i:
                if type(j)==str:
                    value = i.index(j)
                    i[value] = j.title()
        print(tabulate(data, headers=headers, tablefmt='grid'))
        input_keputusan_update = input('apakah anda aka melakukan update pada data tersebut ? (ya/tidak) : ')
        if input_keputusan_update in 'ya':
            #user memilih kolom mana yang akan di update nama/harga/stock/tempat penyimpanan
            input_kolom_update = input('kolom yang akan anda up date : ').lower()
            # update kolom nama
            if input_kolom_update in 'nama':
                while True:
                    list_pencarian_2 = []
                    input_nama = input("masukan nama alat tulis dengan format 'nama_merek' : ").lower()
                    if len(input_nama)<3:
                        print('tidak boleh kurang dari 3 huruf')
                        continue
                    else:
                        for i in range(len(data_alat_tulis)):
                            if input_nama == data_alat_tulis[i]['nama']:
                                list_pencarian_2.append(data_alat_tulis[i]['nama'])
                        if list_pencarian_2 ==[]:
                            break
                        else:
                            print('nama tidak boleh duplikat')
                            continue
                input_keputusan = input('apakah anda akan menyimpan data (ya/tidak) : ')
                if input_keputusan in'ya':
                    data_alat_tulis[list_pencarian[0]]['nama']=input_nama
                    print('data berhasil diubah')
                    headers = data_alat_tulis[0].keys()
                    data = []
                    for item in [data_alat_tulis[list_pencarian[0]]]:
                        data.append([*item.values()])
                    for i in data:
                        for j in i:
                            if type(j)==str:
                                value = i.index(j)
                                i[value] = j.title()
                    print(tabulate(data, headers=headers, tablefmt='grid'))#menampilkan data yang telah di update dalam bentuk tabel
                    print('data berhasil di update')
                elif input_keputusan in 'tidak':
                    print('data tidak jadi ditambahkan')
            #update kolom harga
            elif input_kolom_update in 'harga':
                while True:
                    try:
                        input_harga = int(input('masukan harga alat tulis : '))
                        if input_harga ==0:
                            print('input harus lebih besar dari 0')
                            continue
                        else:
                            break
                    except Exception as e:
                        print(f'''input salah karena {e}''')
                input_keputusan = input('apakah anda akan menyimpan data (ya/tidak) : ')
                if input_keputusan in'ya':
                    data_alat_tulis[list_pencarian[0]]['harga']=input_harga
                    print('data berhasil diubah')
                    headers = data_alat_tulis[0].keys()
                    data = []
                    for item in [data_alat_tulis[list_pencarian[0]]]:
                        data.append([*item.values()])
                    for i in data:
                        for j in i:
                            if type(j)==str:
                                value = i.index(j)
                                i[value] = j.title()
                        
                    print(tabulate(data, headers=headers, tablefmt='grid'))#menampilkan data yang telah di update
                    print('data berhasil di update')
                elif input_keputusan in 'tidak':
                    print('data tidak jadi ditambahkan')
            #update kolom stock
            elif input_kolom_update in 'stock':
                while True:
                    try:
                        input_stock = int(input('masukan stock alat tulis : '))
                        if input_stock ==0:
                            print('input harus lebih besar dari 0')
                            continue
                        else:
                            break
                    except Exception as e:
                        print(f'''input salah karena {e}''')
                input_keputusan = input('apakah anda akan menyimpan data (ya/tidak) : ')
                if input_keputusan in'ya':
                    data_alat_tulis[list_pencarian[0]]['stock']=input_stock
                    print('data berhasil diubah')
                    headers = data_alat_tulis[0].keys()
                    data = []
                    for item in [data_alat_tulis[list_pencarian[0]]]:
                        data.append([*item.values()])
                    for i in data:
                        for j in i:
                            if type(j)==str:
                                value = i.index(j)
                                i[value] = j.title()
                        
                    print(tabulate(data, headers=headers, tablefmt='grid'))#menampilkan data yang telah di update
                    print('data berhasil di update')
                elif input_keputusan in 'tidak':
                    print('data tidak jadi ditambahkan')
            #update kolom tempat penyim panan
            elif input_kolom_update in 'tempat penyimpanan' or 'tempat_penyimpanan':
                while True:
                    print(f'''pilih tempat penyimpanan anda
1. rak 1
2. rak 2
3. rak 3 ''')
                    try:
                        input_pilihan_tempat_penyimpanan = int(input('masukan tempat penyimpanan : '))
                        if input_pilihan_tempat_penyimpanan ==1:
                            input_tempat_penyimpanan = 'rak 1'
                        elif input_pilihan_tempat_penyimpanan ==2:
                            input_tempat_penyimpanan = 'rak 2'
                        elif input_pilihan_tempat_penyimpanan ==3:
                            input_tempat_penyimpanan = 'rak 3'
                        else:
                            print('tidak ada tempat penyimpanan dengan input tersebut')
                            continue
                        break
                    except Exception as e:
                        print(f'''input salah karena {e}''')
                input_keputusan = input('apakah anda akan menyimpan data (ya/tidak) : ')
                if input_keputusan in'ya':
                    data_alat_tulis[list_pencarian[0]]['tempat_penyimpanan']=input_tempat_penyimpanan
                    print('data berhasil diubah')
                    headers = data_alat_tulis[0].keys()
                    data = []
                    for item in [data_alat_tulis[list_pencarian[0]]]:
                        data.append([*item.values()])
                    for i in data:
                        for j in i:
                            if type(j)==str:
                                value = i.index(j)
                                i[value] = j.title()
                        
                    print(tabulate(data, headers=headers, tablefmt='grid'))#menampilkan data yang telah di update
                    print('data berhasil di update')
                elif input_keputusan in 'tidak':
                    print('data tidak jadi ditambahkan')
            #setelah melakukan update data data akan langsung disimpan pada dataset dalam bentuk json
            with open("dataset.json", "w") as jsonFile:
                json.dump(data_alat_tulis, jsonFile)
        else:
            print('update tidak jadi dilakukan')
#end of update menu

#delet menu
def delet_menu():
    while True:
        print(f'''delet menu
            
List Menu :
1. Masukan jumlahdata yang ingin anda delet.
2. Kambali ke menu utama.

            ''')
        
        while True:
            try:
                menu = int(input('Masukan angka menu yang ingin dijalankan : '))
                break
            except Exception as e:
                print(f'''input salah karena {e}''')

        
        if menu == 1 :
            jumlah_data = int(input('Berapa jumlah data yang ingin anda delet :'))
            for i in range(jumlah_data):
                delet_data()
        elif menu == 2:
            input_keputusan=input('apakah anda ingin kembali kemenu utama (ya/tidak) : ')
            if input_keputusan in 'ya':
                menu_utama()
            else:
                delet_menu()
        else:
            print(f'''
                  
opsi yang anda masukan tidak tersedia
                  
                  ''')
#(bagian dari dellet menu) function untuk menghapus data. perubahan data akan langsung tersimpan ke dataset
def delet_data():
    list_pencarian = []

    while True:
        try:
            id_alat_tulis = int(input('masukan id alat tulis : '))
            break
        except Exception as e:
            print(f'''input salah karena {e}''')
    
    for i in range(len(data_alat_tulis)):
        if id_alat_tulis == data_alat_tulis[i]['id']:
            list_pencarian.append(i)
    if list_pencarian ==[]:#bila primary key ditemukan list pencarian akan berisi indeks dari id yang tersedia
        print('data tidak tersedia')
    else:
        #bila primary key tersedia proses delet akan dilanjutkan
        print('data tersedia lanjut ke proses delet data')
        print('berikut adalah data yang akan anda delet')
        headers = data_alat_tulis[0].keys()
        data = []
        for item in [data_alat_tulis[list_pencarian[0]]]:
            data.append([*item.values()])
        for i in data:
            for j in i:
                if type(j)==str:
                    value = i.index(j)
                    i[value] = j.title()
        print(tabulate(data, headers=headers, tablefmt='grid'))
        input_keputusan = input('apakah anda yakin akan menghapus data (ya/tidak) : ')
        if input_keputusan in 'ya':
            del data_alat_tulis[list_pencarian[0]]
            input('data berhasil di hapus')
            #data yang dirubah akan langsung disimpan ke dataset dalam bentuk jsson
            with open("dataset.json", "w") as jsonFile:
                json.dump(data_alat_tulis, jsonFile)
        else:
            print('data tidak jadi di hapus')
#end of dellete menu

#main menu
def menu_utama():
    while True:
        print(f'''Gudang alat tulis
            
List Menu :
1. read menu
2. create menu
3. update menu
4. delet menu
5. exit program
            ''')
        while True:
            try:
                menu = int(input('Masukan angka menu yang ingin dijalankan : '))
                break
            except Exception as e:
                print(f'''input salah karena {e}''')
        if menu == 1 :
            read_menu()
        elif menu == 2:
            create_menu()
        elif menu == 3:
            update_menu()
        elif menu == 4:
            delet_menu()
        elif menu == 5:
            with open("dataset.json", "w") as jsonFile:
                json.dump(data_alat_tulis, jsonFile)
            quit()
        else:
            print(f'''
                  
opsi yang anda masukan tidak tersedia
                  
                  ''')
#end main menu

menu_utama()