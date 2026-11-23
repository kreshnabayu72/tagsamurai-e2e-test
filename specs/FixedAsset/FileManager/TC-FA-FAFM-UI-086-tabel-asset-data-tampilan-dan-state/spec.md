---
id: TC-FA-FAFM-UI-086-tabel-asset-data-tampilan-dan-state
title: "Tabel Asset Data: format sel, nilai kosong, dan state data"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-03", "S-27a", "S-27b", "T-FAFM-02", "EB-TBL-1@tabel-asset-data", "EB-TBL-2@tabel-asset-data", "EB-SRC-6@filter-group-tabel-asset-data", "EB-FLT-6@tabel-asset-data"]
smoke: []
dependsOn: []
trace:
  "S-03": 24
  "S-27a": [23, 24, 26, 27]
  "S-27b": [30, 31]
  "T-FAFM-02": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 21, 62, 63, 65, 66, 68, 70, 72]
  "EB-TBL-1@tabel-asset-data": [23, 26, 30, 33, 34, 36]
  "EB-TBL-2@tabel-asset-data": [12, 13, 14, 15, 16, 17]
  "EB-SRC-6@filter-group-tabel-asset-data": [41, 42, 44, 45]
  "EB-FLT-6@tabel-asset-data": [50, 51, 55, 56, 57, 59, 60]
anchor: [54]
coverage:
  web: automated
---

# Tabel Asset Data: format sel, nilai kosong, dan state data

## Prerequisites
- Aktor: pemegang capability Manage files (Read) dengan scope group `Head Office`, `Branch Bandung`, `Jakarta Selatan Distribution Center`, dan `Server Room`.
- Layar awal: Settings > File Manager, tab `Disposed & Unmanaged Assets`.
- Komponen: Tabel File Manager tab Disposed & Unmanaged Assets
- Data:
  - DU-086-1: Asset Data `Printer HP M404 - 1`, Asset ID `PRN-2026-0001`, Group `Branch Bandung`, Status `Disposed`, Alias Name `Printer Lantai 2`, Brand `HP`, Model / Type `LaserJet M404n`, Category `Printer`, Division `Operasional`, Register Date `2026-03-15`, Last Scanned `2026-10-30`, Data & Log Size `1258291` byte, Files Size `6081741` byte, Total Size `7340032` byte, memiliki foto aset.
    - Register Date yang diharapkan tampil `15/03/26`, dari `2026-03-15` dengan Date Format `dd/MM/yy`.
    - Last Scanned yang diharapkan tampil `30/10/26`, dari `2026-10-30` dengan Date Format `dd/MM/yy`.
    - Data & Log Size yang diharapkan tampil `1.2 MB`, dari `1258291` byte dibulatkan satu desimal.
    - Total Size yang diharapkan tampil `7.0 MB`, dari `7340032` byte.
  - DU-086-2: Asset Data `Scanner Epson DS-530 - 3`, Asset ID `SCN-2026-0003`, Group `Branch Bandung`, Status `Unmanaged`, tanpa foto aset, tanpa Alias Name, tanpa TAG, Brand `Epson`, Model / Type `DS-530`, Category `Scanner`, tanpa Division, Register Date `2026-02-10`, tanpa Last Scanned, Data & Log Size `215040` byte, Files Size `307200` byte, Total Size `522240` byte.
    - Register Date yang diharapkan tampil `10/02/26`, dari `2026-02-10` dengan Date Format `dd/MM/yy`.
  - DU-086-3: Asset Data `Monitor LG 24 - 7`, Asset ID `MON-2026-0007`, Group `Head Office`, Status `Unmanaged`, Alias Name `Monitor Meja Resepsionis`, tanpa TAG, tanpa Brand, tanpa Model / Type, Category `Monitor`, Division `Umum`, Register Date `2026-01-20`, Last Scanned `2026-09-12`, Data & Log Size `421888` byte, Files Size `0` byte, Total Size `421888` byte.
    - Files Size yang diharapkan tampil `0.0 KB`, dari `0` byte.
  - DU-086-4: Asset Data `Server Rack Dell PowerEdge R740 - 2`, Asset ID `SRV-2026-0002`, Group `Jakarta Selatan Distribution Center` (35 karakter), Status `Disposed`, Alias Name `Server Pusat Data`, tanpa TAG, Brand `Dell`, Model / Type `PowerEdge R740`, Category `Environmental Monitoring Equipment` (34 karakter) dengan hierarki `Sensors > Environmental Monitoring Equipment`, Division `Infrastruktur`, Register Date `2025-06-01`, Last Scanned `2026-08-05`, Data & Log Size `858993459200` byte, Files Size `790273982464` byte, Total Size `1649267441664` byte.
    - Group yang diharapkan tampil `Jakarta Sela..ution Center`, dari 12 huruf pertama, `..`, dan 12 huruf terakhir.
    - Category yang diharapkan tampil `Environmenta..ng Equipment`, dari 12 huruf pertama, `..`, dan 12 huruf terakhir.
    - Hover badge Category yang diharapkan menampilkan hierarki `Sensors > Environmental Monitoring Equipment`.
    - Data & Log Size yang diharapkan tampil `800.0 GB`, dari `858993459200` byte.
    - Total Size yang diharapkan tampil `1,536.0 GB`, dari `1649267441664` byte.
  - DU-086-5: Asset Data `Access Point Cisco 9120 - 4`, Asset ID `APT-2026-0004`, Group `Server Room` dengan hierarki `Jakarta Office > Floor 2 > Server Room`, Status `Disposed`, Alias Name `AP Ruang Server`, tanpa TAG, Brand `Cisco`, Model / Type `Catalyst 9120`, Category `Network Device`, Division `Infrastruktur`, Register Date `2025-11-03`, Last Scanned `2026-07-18`, Data & Log Size `524288` byte, Files Size `1048576` byte, Total Size `1572864` byte.
  - DU-086-6: Asset Data `Router Mikrotik RB4011 - 1`, Asset ID `RTR-2026-0001`, Group `Branch Surabaya`, Status `Unmanaged`, di luar scope group aktor.
  - DU-086-7: Daftar Asset Data entitas tanpa aset `Disposed` maupun `Unmanaged`.
  - DU-086-9: Asset Data `Server HPE ProLiant DL380 - 5`, Asset ID `SRV-2026-0005`, Group `Head Office`, Status `Disposed`, Alias Name `Server Cadangan`, TAG bertipe `RFID`, Brand `Hewlett Packard Enterprise Company` (34 karakter), Model / Type `ProLiant DL380 Gen10 Plus Rackmount` (35 karakter), Category `Network Device`, Division `Infrastruktur`, Register Date `2026-04-02`, Last Scanned `2026-10-30`, Data & Log Size `1048576` byte, Files Size `2097152` byte, Total Size `3145728` byte, memiliki foto aset.
    - Brand yang diharapkan tampil `Hewlett Pack..rise Company`, dari 12 huruf pertama, `..`, dan 12 huruf terakhir; hover menampilkan `Hewlett Packard Enterprise Company`.
    - Model / Type yang diharapkan tampil `ProLiant DL3..us Rackmount`, dari 12 huruf pertama, `..`, dan 12 huruf terakhir; hover menampilkan `ProLiant DL380 Gen10 Plus Rackmount`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.
  - K1: tabel berisi DU-086-1 sampai DU-086-5 dan DU-086-9, layout kolom aktor menampilkan kolom bawaan beserta seluruh kolom Curated (`Alias Name`, `TAG`, `Brand`, `Model / Type`, `Category`, `Division`, `Register Date`, `Last Scanned`), dan pohon Group di Filter Panel memuat `Head Office` dan `Branch Bandung` sebagai dua node tingkat atas yang terpisah (bukan induk dan anak).
  - K2: daftar kosong, entitas tanpa aset (DU-086-7), tanpa Search dan Filter aktif.
  - K3: daftar kosong untuk aktor, karena satu-satunya aset (DU-086-6, Group `Branch Surabaya`) berada di luar scope group aktor.
  - K4: tabel berisi DU-086-1 sampai DU-086-5, dan Search `Rak Gudang Timur` tidak cocok dengan satu pun baris sehingga respons kosong.
  - K5: memuat daftar gagal karena error server pada percobaan pertama, dan percobaan berikutnya berhasil memuat DU-086-1 sampai DU-086-5.

## Test Steps

### Format sel dan badge Status
1. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K1
2. Verifikasi baris `Printer HP M404 - 1` menampilkan badge Status `Disposed`
3. Verifikasi baris `Scanner Epson DS-530 - 3` menampilkan badge Status `Unmanaged`
4. Verifikasi baris `Scanner Epson DS-530 - 3` menampilkan gambar placeholder generik pada kolom `Photo`
5. Verifikasi baris `Printer HP M404 - 1` menampilkan `1.2 MB` pada kolom `Data & Log Size`
6. Verifikasi baris `Printer HP M404 - 1` menampilkan `7.0 MB` pada kolom `Total Size`
7. Verifikasi baris `Monitor LG 24 - 7` menampilkan `0.0 KB` pada kolom `Files Size`
8. Verifikasi baris `Server Rack Dell PowerEdge R740 - 2` menampilkan `800.0 GB` pada kolom `Data & Log Size`
9. Verifikasi baris `Server Rack Dell PowerEdge R740 - 2` menampilkan `1,536.0 GB` pada kolom `Total Size`
10. Verifikasi baris `Printer HP M404 - 1` menampilkan `15/03/26` pada kolom `Register Date`
11. Verifikasi baris `Scanner Epson DS-530 - 3` menampilkan `10/02/26` pada kolom `Register Date`

### Nilai kosong tampil sebagai em dash
12. Verifikasi baris `Scanner Epson DS-530 - 3` menampilkan `—` pada kolom `Alias Name`
13. Verifikasi baris `Scanner Epson DS-530 - 3` menampilkan `—` pada kolom `TAG`
14. Verifikasi baris `Scanner Epson DS-530 - 3` menampilkan `—` pada kolom `Division`
15. Verifikasi baris `Scanner Epson DS-530 - 3` menampilkan `—` pada kolom `Last Scanned`
16. Verifikasi baris `Monitor LG 24 - 7` menampilkan `—` pada kolom `Brand`
17. Verifikasi baris `Monitor LG 24 - 7` menampilkan `—` pada kolom `Model / Type`

### Badge Group dan Category dipendekkan, hover Group menampilkan hierarki
18. Verifikasi baris `Server Rack Dell PowerEdge R740 - 2` menampilkan `Jakarta Sela..ution Center` pada kolom `Group`
19. Verifikasi baris `Server Rack Dell PowerEdge R740 - 2` menampilkan `Environmenta..ng Equipment` pada kolom `Category`
20. Arahkan kursor ke badge Group `Server Room` pada baris `Access Point Cisco 9120 - 4`
21. Verifikasi hierarki `Jakarta Office > Floor 2 > Server Room` tampil

### Tab kosong karena entitas tanpa aset
22. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K2
23. Verifikasi judul empty state `No asset data yet`
24. Verifikasi deskripsi empty state `Disposed and unmanaged assets will appear here.`

### Tab kosong karena aset di luar scope aktor
25. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K3
26. Verifikasi judul empty state `No asset data yet`
27. Verifikasi deskripsi empty state `Disposed and unmanaged assets will appear here.`

### Search tanpa hasil menampilkan empty state tersaring
28. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K4
29. Ketik Search `Rak Gudang Timur`, tekan Enter
30. Verifikasi judul empty state `No results found` pada tab Asset Data
31. Verifikasi deskripsi empty state `Try adjusting your search or filter.` pada tab Asset Data

### Gagal memuat bukan empty state dan bisa dimuat ulang
32. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K5
33. Verifikasi pesan `Unable to load this data.` pada tab Asset Data
34. Verifikasi tombol `[Try Again]` pada tab Asset Data
35. Klik `[Try Again]`
36. Verifikasi baris `Printer HP M404 - 1` tampil

### Pencarian di tree Group menyaring saat mengetik dan Enter tidak mengubah hasil
37. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K1
38. Klik ikon `Filter` pada toolbar
39. Klik field `Group` pada Filter Panel
40. Ketik `Head Office` pada kotak pencarian tree tanpa menekan Enter
41. Verifikasi node `Head Office` tampil pada tree Group tabel Asset Data[^drift-1]
42. Verifikasi node `Branch Bandung` tidak tampil pada tree Group tabel Asset Data[^drift-1]
43. Tekan Enter pada kotak pencarian tree
44. Verifikasi node `Head Office` tetap tampil pada tree Group tabel Asset Data[^drift-1]
45. Verifikasi node `Branch Bandung` tetap tidak tampil pada tree Group tabel Asset Data[^drift-1]

### Menyembunyikan kolom tidak menghapus field filter dan tidak membatalkan filter ter-Apply
46. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K1
47. Klik ikon `Filter` pada toolbar
48. Pilih `Disposed` pada field `Status` di Filter Panel
49. Klik `[Apply]`
50. Verifikasi baris `Printer HP M404 - 1` tampil pada tabel
51. Verifikasi baris `Scanner Epson DS-530 - 3` tidak tampil pada tabel
52. Klik header kolom Actions `⋯`
53. Hilangkan centang kolom `Status` pada panel Column Visibility
54. Verifikasi header kolom `Name` tetap tampil pada tabel
55. Verifikasi header kolom `Status` tidak tampil pada tabel
56. Verifikasi baris `Printer HP M404 - 1` tetap tampil pada tabel
57. Verifikasi baris `Scanner Epson DS-530 - 3` tetap tidak tampil pada tabel
58. Klik ikon `Filter` pada toolbar
59. Verifikasi field `Status` tetap ada pada Filter Panel dengan pilihan `Disposed`
60. Verifikasi titik penanda filter aktif tetap tampil pada ikon `Filter` tabel Asset Data

### Last Scanned dan ikon TAG tampil sesuai nilai
61. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K1
62. Verifikasi baris `Printer HP M404 - 1` menampilkan `30/10/26` pada kolom `Last Scanned`
63. Verifikasi baris `Server HPE ProLiant DL380 - 5` menampilkan ikon tipe TAG `RFID` pada kolom `TAG`

### Badge Brand dan Model dipendekkan, hover Brand, Model, dan Category menampilkan nama penuh atau hierarki
64. Tampilkan Tabel File Manager tab Disposed & Unmanaged Assets dengan kondisi K1
65. Verifikasi baris `Server HPE ProLiant DL380 - 5` menampilkan `Hewlett Pack..rise Company` pada kolom `Brand`
66. Verifikasi baris `Server HPE ProLiant DL380 - 5` menampilkan `ProLiant DL3..us Rackmount` pada kolom `Model / Type`
67. Arahkan kursor ke badge Brand `Hewlett Pack..rise Company` pada baris `Server HPE ProLiant DL380 - 5`
68. Verifikasi nama penuh `Hewlett Packard Enterprise Company` tampil
69. Arahkan kursor ke badge Model / Type `ProLiant DL3..us Rackmount` pada baris `Server HPE ProLiant DL380 - 5`
70. Verifikasi nama penuh `ProLiant DL380 Gen10 Plus Rackmount` tampil
71. Arahkan kursor ke badge Category `Environmenta..ng Equipment` pada baris `Server Rack Dell PowerEdge R740 - 2`
72. Verifikasi hierarki `Sensors > Environmental Monitoring Equipment` tampil

[^drift-1]: Drift PRD/foundation vs kontrak komponen. PRD ekspektasi baku EB-SRC-6 dan foundation `prd-conventions.md` §31.3: pencarian tree berjalan saat Enter, bukan real-time. Kontrak `TreeSelect#9`: kotak cari di dialog tree picker menyaring node saat mengetik, node cocok tampil bersama ancestor-nya; `TreeSelect#42`: kotak cari menerima Enter sebagai no-op. Diasersi: kontrak, karena field Group di Filter Panel adalah tree picker dan aturan Enter §31.3 milik kotak cari sidebar tree (SB-7).
