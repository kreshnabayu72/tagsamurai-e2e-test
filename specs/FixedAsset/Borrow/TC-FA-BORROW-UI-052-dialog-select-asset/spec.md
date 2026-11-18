---
id: TC-FA-BORROW-UI-052-dialog-select-asset
title: "Dialog Select Asset menampilkan kolom, baris Not ready beralasan, dan error tanpa pilihan"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1d#r5", "§4.1d#r6", "§4.1d#r7", "§4.1d#r8", "§4.1d#r9", "§4.1d#r10", "§4.1d#r11", "§4.1d#r12", "§4.1d#r13", "§4.1d#r14", "§4.1d#r15", "§4.1d#r16", "§4.1d#p6", "EB-TBL-9@dialog-select-asset"]
smoke: []
dependsOn: []
trace:
  "§4.1d#r5": [2, 5, 8, 9]
  "§4.1d#r6": [2, 5, 10, 11]
  "§4.1d#r7": [2, 5, 13]
  "§4.1d#r8": [2, 5, 15, 16, 17, 19]
  "§4.1d#r9": [2, 5, 20, 21, 23]
  "§4.1d#r10": [2, 5, 25, 26, 28]
  "§4.1d#r11": [3, 6, 61, 62]
  "§4.1d#r12": [3, 6, 63, 65]
  "§4.1d#r13": [2, 5, 30, 31, 32, 33, 35]
  "§4.1d#r14": [2, 5, 35, 37, 38, 39, 40]
  "§4.1d#r15": [3, 6, 66, 67]
  "§4.1d#r16": [2, 5, 42, 43, 45, 46, 48]
  "§4.1d#p6": [46, 50, 53, 54, 55]
  "EB-TBL-9@dialog-select-asset": [69, 71, 72]
anchor: []
coverage:
  web: automated
---
# Dialog Select Asset menampilkan kolom, baris Not ready beralasan, dan error tanpa pilihan

## Prerequisites
- Aktor: Aktor Borrow dalam cakupan Group `Head Office`.
- Layar awal: halaman Borrow Request dengan dialog Select Asset sudah terbuka.
- Komponen: Dialog Select Asset
- Data:
  - DU-052-1: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Photo tersedia, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, TAG `Non TAG`, Category `Laptop` dengan hierarki `IT Equipment > Laptop`, Max Duration `3 days`, Approval `Auto (≤ 3 days)`, Label `Fragile`, `Priority`, dan `Warranty`, Max extensions `2`, Eligibility `Ready`.
  - DU-052-2: Aset `Projector Epson EB-X06 - 14`, Asset ID `PRJ-2026-0014`, tanpa Photo, Brand dan Model/Type kosong, Group `Head Office`, TAG `Non TAG`, Max Duration `3 days`, Approval `Needs approval`, tanpa Label, Eligibility `Ready`.
  - DU-052-3: Aset `Excavator PC200 - 4`, Asset ID `EXC-2026-0010`, Brand `Komatsu Indonesia Heavy Equipment` (33 karakter) dengan badge `Komatsu Indo..vy Equipment`, Model/Type `PC200`, Group `Head Office`, TAG bertipe `QR`, Max Duration `7 days`, Approval `Needs approval (all must approve)`, Eligibility `Ready`.
  - DU-052-4: Aset `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Group `Branch Surabaya`, Max Duration `14 days`, Approval `Needs approval`, Eligibility `Not ready` dengan alasan `Rudi Hartono can't borrow assets from Branch Surabaya.` (dari template `[Borrower] can't borrow assets from [Group].`).
  - DU-052-5: Aset `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Group `Head Office`, Max Duration `1 day`, Approval `Auto (≤ 1 day)`, Eligibility `Ready`.
  - DU-052-6: Aset `Camera Sony A7 IV - 1`, Asset ID `CAM-2026-0001`, Brand `Sony`, Model/Type `A7 IV`, Group `Jakarta Selatan Distribution Center` (35 karakter) dengan badge `Jakarta Sela..ution Center` dan hierarki `Region Jawa > Jakarta Selatan Distribution Center`, Max Duration `1 hour`, Approval `Needs approval`, Eligibility `Ready`.
  - DU-052-7: Aset `Tripod Manfrotto - 3`, Asset ID `TRI-2026-0003`, Group `Head Office`, Max Duration `4 hours`, Approval `Needs approval`, Eligibility `Ready`.
- Kondisi:
  - K1: dialog Select Asset memuat DU-052-1 sampai DU-052-7 untuk Borrower `Rudi Hartono`, belum ada baris terpilih, dan Setup Column memakai pengaturan bawaan.

## Test Steps

### Kolom bawaan tampil dan kolom curated tersembunyi
1. Tampilkan Dialog Select Asset dengan kondisi K1
2. Verifikasi tabel memuat kolom Photo, Name, Asset ID, Brand, Model/Type, Group, Max Duration, Approval, dan Eligibility
3. Verifikasi tabel tidak memuat kolom TAG, Category, dan Label
4. Klik ikon `⋯` pada header kolom Actions
5. Verifikasi panel Column Visibility mencentang Photo, Name, Asset ID, Brand, Model/Type, Group, Max Duration, Approval, dan Eligibility
6. Verifikasi panel Column Visibility tidak mencentang TAG, Category, dan Label

### Kolom Photo dan Name
7. Tampilkan Dialog Select Asset dengan kondisi K1
8. Verifikasi sel Photo baris `Laptop Dell Latitude 5420 - 10` menampilkan foto aset
9. Verifikasi sel Photo baris `Projector Epson EB-X06 - 14` menampilkan gambar placeholder standar karena aset tanpa foto
10. Verifikasi sel Name baris `Laptop Dell Latitude 5420 - 10` menampilkan `Laptop Dell Latitude 5420 - 10`
11. Verifikasi sel Name tidak berupa tautan ke detail aset

### Kolom Asset ID
12. Tampilkan Dialog Select Asset dengan kondisi K1
13. Verifikasi sel Asset ID baris `Laptop Dell Latitude 5420 - 10` menampilkan `LPT-2026-0010`

### Kolom Brand dan Model/Type menampilkan badge dengan nama penuh saat hover
14. Tampilkan Dialog Select Asset dengan kondisi K1
15. Verifikasi sel Brand baris `Laptop Dell Latitude 5420 - 10` menampilkan badge `Dell`
16. Verifikasi sel Brand baris `Projector Epson EB-X06 - 14` menampilkan `—`
17. Verifikasi sel Brand baris `Excavator PC200 - 4` menampilkan badge `Komatsu Indo..vy Equipment`
18. Arahkan kursor ke badge Brand baris `Excavator PC200 - 4`
19. Verifikasi nama Brand penuh `Komatsu Indonesia Heavy Equipment` tersampaikan pada badge itu
20. Verifikasi sel Model/Type baris `Laptop Dell Latitude 5420 - 10` menampilkan badge `Latitude 5420`
21. Verifikasi sel Model/Type baris `Projector Epson EB-X06 - 14` menampilkan `—`
22. Arahkan kursor ke badge Model/Type baris `Laptop Dell Latitude 5420 - 10`
23. Verifikasi nama Model/Type penuh `Latitude 5420` tersampaikan pada badge itu

### Kolom Group menampilkan badge dengan hierarki penuh
24. Tampilkan Dialog Select Asset dengan kondisi K1
25. Verifikasi sel Group baris `Laptop Dell Latitude 5420 - 10` menampilkan badge `Head Office`
26. Verifikasi sel Group baris `Camera Sony A7 IV - 1` menampilkan badge `Jakarta Sela..ution Center`
27. Arahkan kursor ke badge Group baris `Camera Sony A7 IV - 1`
28. Verifikasi hierarki penuh `Region Jawa > Jakarta Selatan Distribution Center` tersampaikan pada badge itu

### Kolom Max Duration menampilkan satuan tunggal atau jamak
29. Tampilkan Dialog Select Asset dengan kondisi K1
30. Verifikasi sel Max Duration baris `Meeting Mic Set - 2` menampilkan `1 day`
31. Verifikasi sel Max Duration baris `Laptop Dell Latitude 5420 - 10` menampilkan `3 days`
32. Verifikasi sel Max Duration baris `Camera Sony A7 IV - 1` menampilkan `1 hour`
33. Verifikasi sel Max Duration baris `Tripod Manfrotto - 3` menampilkan `4 hours`
34. Arahkan kursor ke sel Max Duration baris `Laptop Dell Latitude 5420 - 10`
35. Verifikasi Max extensions `2` dan bukti foto yang diminta tersampaikan pada sel itu

### Kolom Approval menampilkan aturan efektif aset
36. Tampilkan Dialog Select Asset dengan kondisi K1
37. Verifikasi sel Approval baris `Laptop Dell Latitude 5420 - 10` menampilkan `Auto (≤ 3 days)`
38. Verifikasi sel Approval baris `Meeting Mic Set - 2` menampilkan `Auto (≤ 1 day)`
39. Verifikasi sel Approval baris `Projector Epson EB-X06 - 14` menampilkan `Needs approval`
40. Verifikasi sel Approval baris `Excavator PC200 - 4` menampilkan `Needs approval (all must approve)`

### Kolom Eligibility dan baris yang tidak bisa dipilih
41. Tampilkan Dialog Select Asset dengan kondisi K1
42. Verifikasi sel Eligibility baris `Laptop Dell Latitude 5420 - 10` menampilkan badge `Ready`
43. Verifikasi sel Eligibility baris `Toyota Avanza - 6` menampilkan badge `Not ready`
44. Arahkan kursor ke badge Eligibility baris `Toyota Avanza - 6`
45. Verifikasi alasan penuh `Rudi Hartono can't borrow assets from Branch Surabaya.` tersampaikan pada badge itu
46. Verifikasi checkbox baris `Toyota Avanza - 6` disabled
47. Arahkan kursor ke checkbox baris `Toyota Avanza - 6`
48. Verifikasi alasan `Rudi Hartono can't borrow assets from Branch Surabaya.` tersampaikan pada checkbox yang disabled

### Kolom awal checkbox untuk banyak pilihan dan kolom Actions kosong
49. Tampilkan Dialog Select Asset dengan kondisi K1
50. Verifikasi checkbox baris `Laptop Dell Latitude 5420 - 10` aktif
51. Centang baris `Laptop Dell Latitude 5420 - 10`
52. Centang baris `Projector Epson EB-X06 - 14`
53. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan baris `Projector Epson EB-X06 - 14` sama-sama tercentang
54. Verifikasi tabel Select Asset memuat kolom Actions
55. Verifikasi sel Actions baris `Laptop Dell Latitude 5420 - 10` kosong tanpa aksi baris

### Kolom curated muncul setelah diaktifkan
56. Tampilkan Dialog Select Asset dengan kondisi K1
57. Klik ikon `⋯` pada header kolom Actions
58. Centang TAG pada panel Column Visibility
59. Centang Category pada panel Column Visibility
60. Centang Label pada panel Column Visibility
61. Verifikasi sel TAG baris `Excavator PC200 - 4` menampilkan satu ikon untuk TAG Type `QR`
62. Verifikasi sel TAG baris `Laptop Dell Latitude 5420 - 10` menampilkan `—` karena aset `Non TAG`
63. Verifikasi sel Category baris `Laptop Dell Latitude 5420 - 10` menampilkan badge `Laptop`
64. Arahkan kursor ke badge Category baris `Laptop Dell Latitude 5420 - 10`
65. Verifikasi hierarki penuh `IT Equipment > Laptop` tersampaikan pada badge itu
66. Verifikasi sel Label baris `Laptop Dell Latitude 5420 - 10` menampilkan badge `Fragile` dan `Priority` berurutan A–Z, diikuti chip penanda satu label lain yang tidak muat
67. Verifikasi sel Label baris `Projector Epson EB-X06 - 14` menampilkan `—`

### Konfirmasi tanpa pilihan menampilkan error inline
68. Tampilkan Dialog Select Asset dengan kondisi K1
69. Verifikasi tombol konfirmasi `Select` pada dialog tidak disabled
70. Klik tombol konfirmasi `Select` tanpa memilih baris
71. Verifikasi error inline `You must pick an asset` tampil di atas tombol footer
72. Verifikasi dialog Select Asset tetap terbuka dan tidak ada aset yang dikirim ke form
