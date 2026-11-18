---
id: TC-FA-BORROW-UI-051-dialog-select-borrower
title: "Dialog Select Borrower menampilkan kolom, kandidat Blocked, dan error tanpa pilihan"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1e#p3", "§4.1e#r1", "§4.1e#r2", "§4.1e#r3", "§4.1e#r4", "§4.1e#r5", "§4.1e#r6", "§4.1e#r7", "§4.1e#r8", "§4.1e#r9", "§4.1e#r10", "§4.1e#r11", "§4.1e#r12", "§4.1e#p4", "§4.1e#p6", "EB-TBL-9@dialog-select-borrower"]
smoke: []
dependsOn: []
trace:
  "§4.1e#p3": [2, 3]
  "§4.1e#r1": [5, 8, 9]
  "§4.1e#r2": [5, 11, 12]
  "§4.1e#r3": [5, 11, 13]
  "§4.1e#r4": [5, 11, 14]
  "§4.1e#r5": [5, 16, 17, 19]
  "§4.1e#r6": [5, 21, 22]
  "§4.1e#r7": [5, 24, 25, 26, 28]
  "§4.1e#r8": [5, 30, 31, 33, 35, 37]
  "§4.1e#r9": [6, 44]
  "§4.1e#r10": [6, 45]
  "§4.1e#r11": [6, 46, 47]
  "§4.1e#r12": [6, 48, 49]
  "§4.1e#p4": [52, 53, 56, 57, 58]
  "§4.1e#p6": [60, 61]
  "EB-TBL-9@dialog-select-borrower": [63, 65, 66]
anchor: [51]
coverage:
  web: automated
---
# Dialog Select Borrower menampilkan kolom, kandidat Blocked, dan error tanpa pilihan

## Prerequisites
- Aktor: Aktor Borrow dalam cakupan Group `Head Office`.
- Layar awal: halaman Borrow Request dengan dialog Select Borrower sudah terbuka.
- Komponen: Dialog Select Borrower
- Data:
  - DU-051-1: Karyawan `Budi Santoso`, Email `budi.santoso@example.com`, Position `Staff`, Division `IT`, Home Group `Head Office`, Status `Active`, Active Borrows `15 assets`, Eligibility `Blocked` dengan alasan `Budi Santoso can borrow up to 10 assets at a time.` (dari template `[Name] can borrow up to [Max] assets at a time.`), Activation Status `Activated`, Temporary User `No`, Temporary Until kosong, TAG kosong.
  - DU-051-2: Karyawan `Budi Setiawan`, Email `budi.setiawan@example.com`, Position `Staff`, Division `Finance`, Home Group `Branch Surabaya`, Status `Active`, Active Borrows `0 assets`, Eligibility `Can borrow`, Activation Status `Activated`, Temporary User `No`, Temporary Until kosong, TAG `TAG-0007`.
  - DU-051-3: Karyawan `Joko Susilo`, Email `joko.susilo@example.com`, Position `Operator`, Division `Warehouse`, Home Group `Head Office`, Status `Active`, Active Borrows `0 assets`, Eligibility `Can borrow`, tanpa akun login dan PIC `Rudi Hartono`, TAG kosong.
  - DU-051-4: Karyawan `Wawan`, Email `wawan@example.com`, Position `Operator`, Division `Warehouse`, Home Group kosong, Status `Active`, Active Borrows `0 assets`, Eligibility `Blocked` dengan alasan `No login account and no PIC. Set a PIC in Users first.`, tanpa akun login dan tanpa PIC.
  - DU-051-5: Karyawan `Sari Dewi`, Email `sari.dewi@example.com`, Position `Analyst`, Division `Finance`, Home Group `Head Office`, Status `Active`, Active Borrows `2 assets`, Eligibility `Can borrow`.
  - DU-051-6: Karyawan `Rudi Hartono`, Email `rudi.hartono@example.com`, Position `Supervisor`, Division `Warehouse`, Home Group `Head Office`, Status `Active`, Active Borrows `5 assets`, Eligibility `Can borrow`.
  - DU-051-7: Karyawan `Andi Pratama`, Email `andi.pratama@example.com`, Position `Operator`, Division `Warehouse`, Home Group `Branch Surabaya`, Status `Active`, Active Borrows `1 asset` dengan aset aktif `Projector Epson EB-X06 - 14`, Eligibility `Blocked` karena punya baris Overdue untuk aset `PRJ-2026-0014`.
  - DU-051-8: Karyawan `Dewi Lestari`, Email `dewi.lestari@example.com`, Position `Staff`, Division `Operations`, Home Group `East Distribution Center` dengan hierarki `Region Java > East Distribution Center`, Status `Active`, Active Borrows `6 assets`, Eligibility `Can borrow`, Activation Status `Activated`, Temporary User `Yes`, Temporary Until terisi satu tanggal.
  - DU-051-9: Karyawan `Eko Prasetyo`, Email, Position, dan Division kosong, Home Group `Head Office`, Status `Active`, Active Borrows `0 assets`, Eligibility `Can borrow`.
- Kondisi:
  - K1: dialog Select Borrower memuat DU-051-1 sampai DU-051-9, belum ada baris terpilih, dan Setup Column memakai pengaturan bawaan.

## Test Steps

### Kolom bawaan tampil dan kolom curated tersembunyi
1. Tampilkan Dialog Select Borrower dengan kondisi K1
2. Verifikasi tabel memuat kolom Name, Email, Position, Division, Home Group, Status, Active Borrows, dan Eligibility
3. Verifikasi tabel tidak memuat kolom Activation Status, Temporary User, Temporary Until, dan TAG
4. Klik ikon `⋯` pada header kolom Actions
5. Verifikasi panel Column Visibility mencentang Name, Email, Position, Division, Home Group, Status, Active Borrows, dan Eligibility
6. Verifikasi panel Column Visibility tidak mencentang Activation Status, Temporary User, Temporary Until, dan TAG

### Kolom Name menampilkan avatar dan nama
7. Tampilkan Dialog Select Borrower dengan kondisi K1
8. Verifikasi sel Name baris `Budi Santoso` memuat avatar dan nama `Budi Santoso` dalam satu sel
9. Verifikasi sel Name terisi pada kesembilan baris

### Kolom Email, Position, dan Division menampilkan nilai atau tanda kosong
10. Tampilkan Dialog Select Borrower dengan kondisi K1
11. Verifikasi baris `Budi Santoso` menampilkan Email `budi.santoso@example.com`, Position `Staff`, dan Division `IT`
12. Verifikasi sel Email baris `Eko Prasetyo` menampilkan `—`
13. Verifikasi sel Position baris `Eko Prasetyo` menampilkan `—`
14. Verifikasi sel Division baris `Eko Prasetyo` menampilkan `—`

### Kolom Home Group menampilkan badge dengan hierarki penuh
15. Tampilkan Dialog Select Borrower dengan kondisi K1
16. Verifikasi sel Home Group baris `Budi Santoso` menampilkan badge `Head Office`
17. Verifikasi sel Home Group baris `Wawan` menampilkan `—` karena Home Group belum di-set
18. Arahkan kursor ke badge Home Group baris `Dewi Lestari`
19. Verifikasi hierarki penuh `Region Java > East Distribution Center` tersampaikan pada badge itu

### Kolom Status menampilkan badge Active
20. Tampilkan Dialog Select Borrower dengan kondisi K1
21. Verifikasi sel Status baris `Budi Santoso` menampilkan badge `Active`
22. Verifikasi sel Status terisi `Active` pada kesembilan baris

### Kolom Active Borrows menampilkan jumlah aset beserta daftarnya
23. Tampilkan Dialog Select Borrower dengan kondisi K1
24. Verifikasi sel Active Borrows baris `Budi Santoso` menampilkan `15 assets`
25. Verifikasi sel Active Borrows baris `Andi Pratama` menampilkan `1 asset`
26. Verifikasi sel Active Borrows baris `Wawan` menampilkan `0 assets`
27. Arahkan kursor ke sel Active Borrows baris `Andi Pratama`
28. Verifikasi daftar aset aktif `Projector Epson EB-X06 - 14` tersampaikan pada sel itu

### Kolom Eligibility menampilkan Can borrow atau Blocked beserta alasannya
29. Tampilkan Dialog Select Borrower dengan kondisi K1
30. Verifikasi sel Eligibility baris `Budi Setiawan` menampilkan badge `Can borrow`
31. Verifikasi sel Eligibility baris `Budi Santoso` menampilkan badge `Blocked`
32. Arahkan kursor ke badge Eligibility baris `Budi Santoso`
33. Verifikasi alasan `Budi Santoso can borrow up to 10 assets at a time.` tersampaikan pada badge itu
34. Arahkan kursor ke badge Eligibility baris `Wawan`
35. Verifikasi alasan `No login account and no PIC. Set a PIC in Users first.` tersampaikan pada badge itu
36. Arahkan kursor ke badge Eligibility baris `Andi Pratama`
37. Verifikasi alasan pada badge itu menyebut aset Overdue `PRJ-2026-0014` dan meminta aset itu dikembalikan lebih dulu

### Kolom curated muncul setelah diaktifkan
38. Tampilkan Dialog Select Borrower dengan kondisi K1
39. Klik ikon `⋯` pada header kolom Actions
40. Centang Activation Status pada panel Column Visibility
41. Centang Temporary User pada panel Column Visibility
42. Centang Temporary Until pada panel Column Visibility
43. Centang TAG pada panel Column Visibility
44. Verifikasi sel Activation Status baris `Budi Setiawan` menampilkan `Activated`
45. Verifikasi sel Temporary User baris `Budi Setiawan` menampilkan `No` dan baris `Dewi Lestari` menampilkan `Yes`
46. Verifikasi sel Temporary Until baris `Dewi Lestari` terisi tanggal sesuai format tanggal General Settings
47. Verifikasi sel Temporary Until baris `Budi Setiawan` menampilkan `—`
48. Verifikasi sel TAG baris `Budi Setiawan` menampilkan `TAG-0007`
49. Verifikasi sel TAG baris `Joko Susilo` menampilkan `—`

### Radio hanya untuk baris yang bisa dipilih dan kolom Actions kosong
50. Tampilkan Dialog Select Borrower dengan kondisi K1
51. Verifikasi radio baris `Budi Setiawan` aktif
52. Verifikasi radio baris `Budi Santoso` disabled karena Eligibility `Blocked`
53. Verifikasi radio baris `Andi Pratama` disabled karena Eligibility `Blocked`
54. Pilih radio baris `Budi Setiawan`
55. Pilih radio baris `Sari Dewi`
56. Verifikasi hanya radio baris `Sari Dewi` yang terpilih
57. Verifikasi kolom Actions ada pada tabel
58. Verifikasi sel Actions baris `Sari Dewi` kosong tanpa aksi baris

### Nama yang mirip dibedakan oleh Email dan Division
59. Tampilkan Dialog Select Borrower dengan kondisi K1
60. Verifikasi baris `Budi Santoso` dan baris `Budi Setiawan` sama-sama memiliki Position `Staff`
61. Verifikasi baris `Budi Santoso` dibedakan dari baris `Budi Setiawan` oleh Email `budi.santoso@example.com` dan `budi.setiawan@example.com`, serta Division `IT` dan `Finance`

### Konfirmasi tanpa pilihan menampilkan error inline
62. Tampilkan Dialog Select Borrower dengan kondisi K1
63. Verifikasi tombol konfirmasi dialog tidak disabled
64. Klik tombol konfirmasi dialog tanpa memilih baris
65. Verifikasi error inline `You must pick a user` tampil di atas tombol footer
66. Verifikasi dialog Select Borrower tetap terbuka dan tidak ada Borrower yang dikirim ke form
