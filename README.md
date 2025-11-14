PS C:\Users\IP Slim 3 06\OneDrive\Documents\Python_KKA>                                                          > & "C:\Users\IP Slim 3 06\AppData\Local\Microsoft\WindowsApps\python3.13.exe" "c:/Users/IP Slim 3 06/OneDrive/Documents/Python_KKA/penjualan.py"
      Tanggal    Produk    Kategori    Harga  Jumlah  Pendapatan
0  2024-01-07    Laptop  Elektronik  8000000       1     8000000
1  2024-01-14     Mouse   Aksesoris   150000       2      300000
2  2024-01-21  Keyboard   Aksesoris   250000       4     1000000
3  2024-01-28   Monitor  Elektronik  2000000       9    18000000
4  2024-02-04   Headset   Aksesoris   300000       1      300000
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25 entries, 0 to 24
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Tanggal     25 non-null     object
 1   Produk      25 non-null     object
 2   Kategori    25 non-null     object
 3   Harga       25 non-null     int64
 4   Jumlah      25 non-null     int64
 5   Pendapatan  25 non-null     int64
dtypes: int64(3), object(3)
memory usage: 1.3+ KB
None
Tanggal       0
Produk        0
Kategori      0
Harga         0
Jumlah        0
Pendapatan    0
dtype: int64
Statistik Deskriptif:
              Harga     Jumlah    Pendapatan
count  2.500000e+01  25.000000  2.500000e+01
mean   2.642000e+06   4.520000  1.011000e+07
std    3.459639e+06   2.725191  1.653172e+07
min    1.500000e+05   1.000000  3.000000e+05
25%    2.500000e+05   2.000000  7.500000e+05
50%    3.000000e+05   5.000000  2.700000e+06
75%    2.000000e+06   6.000000  1.000000e+07
max    1.000000e+07   9.000000  7.200000e+07

Produk Terlaris:
Produk
Monitor     33
Keyboard    25
Produk Terlaris:
Produk
Monitor     33
Produk Terlaris:
Produk
Produk Terlaris:
Produk Terlaris:
Produk Terlaris:
Produk Terlaris:
Produk Terlaris:
Produk Terlaris:
Produk Terlaris:
Produk
Monitor     33
Produk Terlaris:
Produk
Monitor     33
Produk Terlaris:
Produk
Produk
Monitor     33
Monitor     33
Keyboard    25
Keyboard    25
Laptop      21
Laptop      21
Mouse       18
Headset     16
Headset     16
Name: Jumlah, dtype: int64
c:\Users\IP Slim 3 06\OneDrive\Documents\Python_KKA\penjualan.py:17: FutureWarning:

The ci parameter is deprecated. Use errorbar=None for the same effect.

  sns.barplot(data=df, x="Produk", y="Pendapatan", estimator=sum,
Data hasil analisis telah disimpan sebagai
PS C:\Users\IP Slim 3 06\OneDrive\Documents\Python_KKA>
