---
id: TC-FA-FATR-BE-092-export-isi
title: "Isi berkas Export rules"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§Aturan Logika Modul#r39", "§4.1#r53", "§4.1#r55", "§4.1#r279", "§9.2#b310", "§9.2#b311", "§9.2#b312", "§9.2#b314", "§9.2#b315", "§9.2#b318", "§9.2#b323", "§9.2#b325", "§9.2#b326", "§9.2#b327", "§9.2#b328", "§9.2#b329", "§9.2#b331", "§9.2#b332", "§9.2#b333", "§9.2#b335", "§9.2#b336", "§9.2#b337", "§9.2#b338", "§9.2#b340", "§9.2#b341", "§9.2#b342", "§9.2#b343", "§9.2#b344", "§9.2#b345", "§9.2#b347", "§9.2#b348", "§9.2#b349", "§9.2#b350", "§9.2#b351", "§9.2#b352", "§9.2#b353", "§9.2#b354", "§9.2#b355", "§9.2#b356", "§9.2#b357", "§9.2#b359", "§9.2#b360", "§9.2#b361", "§9.2#b362", "§9.2#b363", "§9.2#b365", "§9.2#b366", "§9.2#b367", "§9.2#b368", "§9.2#b369", "§9.2#b370", "§9.2#b371", "§9.4.2#r49", "§9.10.1#b7", "§9.10.2#b6", "FLD-43"]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#r39": 52
  "§4.1#r53": [21, 33]
  "§4.1#r55": 32
  "§4.1#r279": 43
  "§9.2#b310": [14, 64]
  "§9.2#b311": 38
  "§9.2#b312": [65, 66]
  "§9.2#b314": [5, 60]
  "§9.2#b315": 61
  "§9.2#b318": [52, 62]
  "§9.2#b323": 10
  "§9.2#b325": 15
  "§9.2#b326": 20
  "§9.2#b327": [23, 68]
  "§9.2#b328": [70, 87, 88, 92, 95, 96, 97]
  "§9.2#b329": [37, 71]
  "§9.2#b331": [39, 66]
  "§9.2#b332": [12, 40]
  "§9.2#b333": [41, 42, 43, 74, 75, 76]
  "§9.2#b335": [47, 49, 64, 85]
  "§9.2#b336": [48, 54, 99, 100, 101, 102]
  "§9.2#b337": 48
  "§9.2#b338": [44, 45, 77]
  "§9.2#b340": 16
  "§9.2#b341": 17
  "§9.2#b342": [19, 84]
  "§9.2#b343": [18, 93]
  "§9.2#b344": [67, 87, 95, 96]
  "§9.2#b345": 20
  "§9.2#b347": [21, 46]
  "§9.2#b348": [21, 25]
  "§9.2#b349": [30, 31]
  "§9.2#b350": [28, 103, 104]
  "§9.2#b351": 32
  "§9.2#b352": 29
  "§9.2#b353": [22, 33, 34, 82]
  "§9.2#b354": [27, 40]
  "§9.2#b355": [25, 35, 67, 78]
  "§9.2#b356": [25, 35]
  "§9.2#b357": [11, 12, 13]
  "§9.2#b359": 11
  "§9.2#b360": 14
  "§9.2#b361": [16, 69, 83, 91, 95]
  "§9.2#b362": 36
  "§9.2#b363": [23, 24, 26, 72]
  "§9.2#b365": 13
  "§9.2#b366": 47
  "§9.2#b367": 51
  "§9.2#b368": 50
  "§9.2#b369": 52
  "§9.2#b370": [53, 85]
  "§9.2#b371": [54, 55]
  "§9.4.2#r49": [8, 9]
  "§9.10.1#b7": [37, 42, 53]
  "§9.10.2#b6": 71
  "FLD-43": 105
---
# Isi berkas Export rules

## Prerequisites
- Aktor: Maya Pengelola (DU-092-2), Total Control dengan cakupan seluruh Group; dan Operator Plan (DU-092-21), operator Admin Console di luar entitas.
- Data:
  - DU-092-1: Entitas, entitas khusus spec ini: Name `Entitas Ekspor {runId}`.
  - DU-092-2: User, pengelola Total Control yang mengekspor dan menyimpan: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-092-3: User, pembuat override yang sudah dinonaktifkan: Name `Budi Nonaktif {runId}`; Status `Inactive`.
  - DU-092-4: Category, Category induk tanpa nilai sendiri: Name `Kendaraan {runId}`.
  - DU-092-5: Category, Category leaf yang diekspor, turunan Kendaraan: Name `Mobil Pool {runId}`; Parent `Kendaraan {runId}`; Full path `Kendaraan {runId} > Mobil Pool {runId}`; Require approval `ON`.
  - DU-092-6: Category, Category leaf tingkat atas dengan nilai bergerbang plan tersimpan: Name `Mesin Berat {runId}`; Self service `ON`.
  - DU-092-7: Group, Group target override: Name `Workshop Ekspor {runId}`.
  - DU-092-8: Group, Group target override dengan field bergerbang plan: Name `Gudang Ekspor {runId}`.
  - DU-092-9: Group, Group target override milik pembuat yang sudah dinonaktifkan: Name `Arsip Ekspor {runId}`.
  - DU-092-10: Group, Group yang sudah dihapus sehingga override-nya tidak berlaku: Name `Tim Dihapus Ekspor {runId}`.
  - DU-092-11: Override, override Category Mesin Berat dengan dua field: Scope `Group`; Target `Workshop Ekspor {runId}`; Category `Mesin Berat {runId}`; Transaksi `peminjaman`; Field `Max extensions`; Value `2`; Field 2 `Max assets per borrower (concurrent)`; Value 2 `5`; Created By `Maya Pengelola {runId}`.
  - DU-092-12: Override, override Category Mobil Pool dengan field bergerbang plan: Scope `Group`; Target `Gudang Ekspor {runId}`; Category `Mobil Pool {runId}`; Transaksi `penugasan`; Field `Max assets per assignee (concurrent)`; Value `3`; Field 2 `Require approval`; Value 2 `ON`; Created By `Maya Pengelola {runId}`.
  - DU-092-13: Override, override semua Category pada Group Workshop Ekspor: Scope `Group`; Target `Workshop Ekspor {runId}`; Category `All categories`; Transaksi `peminjaman`; Field `Max extensions`; Value `3`; Created By `Maya Pengelola {runId}`.
  - DU-092-14: Override, override pada Group yang sudah dihapus, tidak berlaku: Scope `Group`; Target `Tim Dihapus Ekspor {runId}`; Category `Mobil Pool {runId}`; Transaksi `penugasan`; Field `Max assets per assignee (concurrent)`; Value `2`; Created By `Maya Pengelola {runId}`.
  - DU-092-15: Override, override yang dibuat pengguna yang sudah dinonaktifkan: Scope `Group`; Target `Arsip Ekspor {runId}`; Category `Mobil Pool {runId}`; Transaksi `penugasan`; Field `Max assets per assignee (concurrent)`; Value `2`; Created By `Budi Nonaktif {runId}`.
  - DU-092-16 sampai DU-092-19 disimpan Maya Pengelola di langkah masing-masing, dan DU-092-20 hanya ada di draft, bukan nilai tersimpan.
  - DU-092-21: User, operator Admin Console yang menerapkan plan kustom pada entitas: Name `Operator Plan {runId}`; Peran `operator Admin Console di luar entitas`.
  - DU-092-22: Plan, plan kustom milik spec ini yang diterapkan Operator Plan: Name `Paket Ekspor {runId}`; Approval Workflow `ON`; Feature Suite Borrowing `Full`; Feature Suite Assignment `Basic`; Feature Suite Transfer `Basic`; Feature Suite Disposal `Full`.
  - DU-092-23: Category, Category leaf tingkat atas yang diekspor pada plan kustom: Name `Truk Ekspor {runId}`.
  - DU-092-25: Group, Group yang sudah dinonaktifkan: Name `Gudang Nonaktif Ekspor {runId}`.
  - DU-092-26: Category, Category yang sudah dihapus sehingga override-nya tidak berlaku: Name `Kategori Dihapus Ekspor {runId}`.
  - DU-092-27: Category, Category yang sudah dinonaktifkan sehingga override-nya tidak berlaku: Name `Kategori Nonaktif Ekspor {runId}`.
  - DU-092-28: User, pembuat override yang sudah dihapus: Name `Citra Dihapus {runId}`; Status `Deleted`.
  - DU-092-29: Group, Group target override milik pembuat yang sudah dihapus: Name `Arsip Dua Ekspor {runId}`.
  - DU-092-30: Override, override Group yang dinonaktifkan: Scope `Group`; Target `Gudang Nonaktif Ekspor {runId}`; Category `Truk Ekspor {runId}`; Transaksi `peminjaman`; Field `Max extensions`; Value `2`; Created By `Maya Pengelola {runId}`.
  - DU-092-31: Override, override pada Category yang sudah dihapus: Scope `Group`; Target `Workshop Ekspor {runId}`; Category `Kategori Dihapus Ekspor {runId}`; Transaksi `peminjaman`; Field `Max extensions`; Value `2`; Created By `Maya Pengelola {runId}`.
  - DU-092-32: Override, override pada Category yang sudah dinonaktifkan: Scope `Group`; Target `Workshop Ekspor {runId}`; Category `Kategori Nonaktif Ekspor {runId}`; Transaksi `peminjaman`; Field `Max extensions`; Value `2`; Created By `Maya Pengelola {runId}`.
  - DU-092-33: Override, override yang dibuat pengguna yang sudah dihapus: Scope `Group`; Target `Arsip Dua Ekspor {runId}`; Category `Mobil Pool {runId}`; Transaksi `penugasan`; Field `Max assets per assignee (concurrent)`; Value `2`; Created By `Citra Dihapus {runId}`.
  - DU-092-24 disimpan Maya Pengelola di langkahnya.
  - DU-092-35 dialokasikan Operator Plan di langkahnya.
  - DU-092-34: Setting, format tanggal dan jam General Settings entitas khusus ini: Date Format `dd MMM yy`; Time Format `12h`.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Ekspor {runId}` (DU-092-1) yang tidak dipakai spec lain, karena yang diasersi adalah nilai Company default dan nilai efektif plan entitas.
  - Plan entitas: Approval Workflow tidak tersedia, Feature Suite Borrowing `Basic`, Feature Suite Assignment `Basic`, Feature Suite Transfer `None`, dan Feature Suite Disposal `Full`; nilai field bergerbang plan pada Category Mobil Pool dan Mesin Berat serta override Gudang Ekspor tersimpan sejak plan masih membuka field itu.
  - Seluruh nilai Company default selain yang disimpan di langkah bernilai default, dan seluruh nilai Category lain Inherit.
  - Date Format `dd MMM yy` dan Time Format `12h` pada General Settings entitas khusus ini, bukan nilai default platform.
  - Max assets per assignee (concurrent) Company default bernilai `0`.
  - Group `Gudang Nonaktif Ekspor {runId}` dan Category `Kategori Nonaktif Ekspor {runId}` berstatus nonaktif, Category `Kategori Dihapus Ekspor {runId}` dan pengguna `Citra Dihapus {runId}` sudah dihapus, dan override pada keempatnya sudah aktif sebelum langkah pertama.
  - Plan kustom `Paket Ekspor {runId}` (DU-092-22) diterapkan Operator Plan pada entitas khusus ini di grup export Truk Ekspor.
  - Addon `Audit` dan addon `Maintenance` belum dialokasikan ke subscription FAMS entitas khusus ini sampai Operator Plan mengalokasikannya (DU-092-35) di grup export addon; subscription entitas berstatus Active.
  - Jumlah entri Activity Log dan versi setting dibaca sebagai selisih terhadap nilai yang dicatat sebelum aksi.

## Test Steps

### Setup: nilai Company default dan Category disimpan sebelum export
1. Maya Pengelola menyimpan Company default dengan Max extensions `0` dan Long missing after `0`
2. Maya Pengelola menyimpan Category `Kendaraan {runId} > Mobil Pool {runId}` dengan Max assets per borrower (concurrent) nilai sendiri `4`
3. Maya Pengelola menyimpan Category `Kendaraan {runId} > Mobil Pool {runId}` dengan Max duration `10`, Allowed assignee: Employee `OFF`, Allowed disposal types `Sell, Scrap`, Min asset age warning `6`, dan Max deviation from book value `25`
4. Maya Pengelola menyimpan Category `Kendaraan {runId} > Mobil Pool {runId}` dengan Allow Borrow `Deny`
5. Verifikasi seluruh penyimpanan diterima dan Allow Borrow Category `Kendaraan {runId} > Mobil Pool {runId}` bernilai `Deny`

### Export Category leaf: cakupan, sheet, dan header
6. Maya Pengelola mencatat versi setting dan jumlah entri Activity Log
7. Maya Pengelola menjalankan Export rules dengan Category `Kendaraan {runId} > Mobil Pool {runId}` terpilih di Sidebar Category Tree
8. Verifikasi berkas Excel terunduh langsung dari satu permintaan Export rules, tanpa langkah konfirmasi tambahan
9. Verifikasi Activity Log bertambah tepat satu entri Export rules dari Maya Pengelola
10. Verifikasi berkas memuat sheet `Rules`, `Overrides`, dan `Info`
11. Verifikasi header kolom sheet Rules berurutan `Category`, `Transaction`, `Field`, `Value`, `Unit`, `Source`
12. Verifikasi header kolom sheet Overrides berurutan `Scope`, `Target`, `Category`, `Transaction`, `Field`, `Value`, `Unit`, `Status`, `Created By`, `Created At`
13. Verifikasi header kolom sheet Info berurutan `Item` dan `Value`

### Sheet Rules Category leaf: baris, nilai, dan sumber
14. Verifikasi seluruh baris sheet Rules berkolom Category `Kendaraan {runId} > Mobil Pool {runId}`, karena cakupan export mengikuti node yang dipilih
15. Verifikasi sheet Rules memuat satu baris per kombinasi Category, Transaction, dan Field
16. Verifikasi kolom Transaction sheet Rules hanya berisi `Borrow`, `Assign`, dan `Disposal`
17. Verifikasi sheet Rules tidak memuat baris untuk transaksi yang level Feature Suite-nya `None`, karena tabnya tidak dapat dibuka pada plan entitas
18. Verifikasi sheet Rules tidak memuat baris Transaction `Damaged & Missing`
19. Verifikasi sheet Rules tidak memuat Field `Send email notifications` dan `Transaction timeout`
20. Verifikasi baris Transaction `Borrow`, Field `Max duration` berisi Value `10`, karena nilai tersimpan bagian yang tersembunyi oleh Allow Borrow `Deny` tetap diekspor
21. Verifikasi baris Transaction `Borrow`, Field `Max duration` berisi Value sebagai sel angka `10` tanpa satuan
22. Verifikasi baris Transaction `Borrow`, Field `Max duration` berisi Unit `days` di kolom terpisah
23. Verifikasi baris Transaction `Borrow`, Field `Max duration` berisi Source `Kendaraan {runId} > Mobil Pool {runId}`, karena nilai efektif disimpan di Category itu
24. Verifikasi baris Transaction `Borrow`, Field `Max assets per borrower (concurrent)` berisi Value `4` dan Source `Kendaraan {runId} > Mobil Pool {runId}`, karena nilai efektif disimpan di Category leaf itu
25. Verifikasi baris Transaction `Borrow`, Field `Max extensions` berisi Value `0` sebagai angka, bukan teks "No extension"
26. Verifikasi baris Transaction `Borrow`, Field `Max extensions` berisi Source `Company default`
27. Verifikasi baris Transaction `Borrow`, Field `Max extensions` berisi Unit `-`, karena field tanpa satuan
28. Verifikasi baris Transaction `Borrow`, Field `Allow Borrow` berisi Value `Deny` sebagai label teks
29. Verifikasi baris Transaction `Borrow`, Field `Allow Borrow` berisi sel kosong ditulis `-` pada kolom Unit
30. Verifikasi baris Transaction `Assign`, Field `Allowed assignee: Employee` berisi Value `Inactive`
31. Verifikasi baris Transaction `Assign`, Field `Allowed assignee: Division` berisi Value `Active`
32. Verifikasi baris Transaction `Disposal`, Field `Allowed disposal types` berisi Value `Sell, Scrap`, dengan nilai berderet dipisah ", "
33. Verifikasi baris Transaction `Disposal`, Field `Min asset age warning` berisi Value `6` dan Unit `months`
34. Verifikasi baris Transaction `Disposal`, Field `Max deviation from book value` berisi Value `25` dan Unit `%`
35. Verifikasi baris Transaction `Borrow`, Field `Max extensions` tidak berisi teks `No extension`, dan tidak ada sel Value berisi teks makna nilai 0 seperti `Unlimited` atau `Off`
36. Verifikasi kolom Field memuat nama field `Max duration`, `Max assets per borrower (concurrent)`, `Max extensions`, `Allow Borrow`, `Allowed assignee: Employee`, `Allowed assignee: Division`, `Allowed disposal types`, `Min asset age warning`, `Max deviation from book value`, dan `Require approval`
37. Verifikasi baris Transaction `Borrow`, Field `Require approval` berisi Value `Active`, yaitu nilai tersimpan field bergerbang plan

### Sheet Overrides Category leaf: baris, status, dan pembuat
38. Verifikasi sheet Overrides memuat override Category `Kendaraan {runId} > Mobil Pool {runId}` dan override All categories yang ikut berlaku, dan tidak memuat override Category `Mesin Berat {runId}`
39. Verifikasi override Group `Gudang Ekspor {runId}` pada Category `Kendaraan {runId} > Mobil Pool {runId}` memuat dua baris, satu per field yang diubah: `Max assets per assignee (concurrent)` dan `Require approval`
40. Verifikasi baris override Group `Workshop Ekspor {runId}` pada All categories berisi Scope `Group`, Category `All categories`, Transaction `Borrow`, Field `Max extensions`, Value `3`, dan Unit `-`
41. Verifikasi baris Field `Max assets per assignee (concurrent)` pada override Group `Gudang Ekspor {runId}` berisi Status `Applied`
42. Verifikasi baris Field `Require approval` pada override Group `Gudang Ekspor {runId}` berisi Status `Not applied`, karena field bergerbang plan
43. Verifikasi baris override Group `Tim Dihapus Ekspor {runId}` berisi Status `Not applied`
44. Verifikasi baris override Group `Arsip Ekspor {runId}` berisi Created By `Budi Nonaktif {runId}`, nama lengkap snapshot pembuat yang sudah dinonaktifkan
45. Verifikasi baris override Group `Workshop Ekspor {runId}` pada All categories berisi Created By `Maya Pengelola {runId}`
46. Verifikasi sel Value pada sheet Overrides berisi nilai asli, yaitu angka `3` pada baris Max extensions tanpa satuan

### Sheet Info Category leaf: baris dan nilai
47. Verifikasi kolom Item sheet Info berurutan: Export time, Exported by, Category, Settings version, Approval Workflow, Feature Suite Borrowing, Feature Suite Assignment, Feature Suite Transfer, Feature Suite Disposal
48. Verifikasi semua baris sheet Info tampil, termasuk Feature Suite Transfer walau levelnya `None`
49. Verifikasi baris Category sheet Info berisi `Kendaraan {runId} > Mobil Pool {runId}`
50. Verifikasi baris Exported by berisi `Maya Pengelola {runId}`, nama lengkap pengguna
51. Verifikasi baris Export time ditulis dengan Date Format `dd MMM yy` dan Time Format `12h`, mengikuti format entitas dan bukan format default platform
52. Verifikasi baris Settings version berisi bilangan bulat yang sama dengan versi setting yang dicatat sebelum export
53. Verifikasi baris Approval Workflow berisi `Not available`
54. Verifikasi baris Feature Suite Borrowing dan Feature Suite Assignment masing-masing berisi `Basic`, dan baris Feature Suite Disposal berisi `Full`
55. Verifikasi baris Feature Suite Transfer berisi `None`

### Berkas memuat nilai tersimpan saat export diminta, bukan draft
56. Maya Pengelola menyimpan Category `Kendaraan {runId} > Mobil Pool {runId}` dengan Min asset age warning `7`
57. Maya Pengelola mengubah Min asset age warning Category `Kendaraan {runId} > Mobil Pool {runId}` menjadi `9` di draft tanpa menyimpan
58. Maya Pengelola mencatat versi setting
59. Maya Pengelola menjalankan Export rules dengan Category `Kendaraan {runId} > Mobil Pool {runId}` terpilih
60. Verifikasi baris Transaction `Disposal`, Field `Min asset age warning` berisi Value `7`, nilai yang tersimpan di server saat export diminta
61. Verifikasi baris itu tidak berisi `9`, karena perubahan draft yang belum disimpan tidak ikut
62. Verifikasi baris Settings version sheet Info sama dengan versi setting yang dicatat, yaitu versi tersimpan saat export diminta

### Export All categories: Company default, semua Category, dan semua override
63. Maya Pengelola menjalankan Export rules dengan All categories terpilih di Sidebar Category Tree
64. Verifikasi baris Category sheet Info berisi `All categories`
65. Verifikasi sheet Rules memuat baris Company default dan baris Category `Kendaraan {runId} > Mobil Pool {runId}` serta Category `Mesin Berat {runId}`
66. Verifikasi sheet Overrides memuat semua override, termasuk dua baris override Group `Workshop Ekspor {runId}` pada Category `Mesin Berat {runId}`
67. Verifikasi baris Category `All categories`, Transaction `Damaged & Missing`, Field `Long missing after` berisi Value `0` dan Unit `days`
68. Verifikasi baris Category `All categories`, Transaction `Damaged & Missing`, Field `Long missing after` berisi Source `Company default`
69. Verifikasi kolom Transaction sheet Rules memuat `Damaged & Missing`
70. Verifikasi Field `Transaction timeout` dan `Send email notifications` hanya muncul pada baris Category `All categories`
71. Verifikasi baris Category `Mesin Berat {runId}`, Transaction `Borrow`, Field `Self service` berisi Value `Active`, yaitu nilai tersimpan field bergerbang plan
72. Verifikasi baris Category `Mesin Berat {runId}`, Transaction `Borrow`, Field `Max extensions` berisi Source `Company default`

### Status override, pembuat yang dihapus, dan nilai nol pada export All categories
73. Maya Pengelola menjalankan Export rules dengan All categories terpilih di Sidebar Category Tree
74. Verifikasi baris override Group `Gudang Nonaktif Ekspor {runId}` pada Category `Truk Ekspor {runId}` berisi Status `Not applied`, karena Group target dinonaktifkan
75. Verifikasi baris override Group `Workshop Ekspor {runId}` pada Category `Kategori Dihapus Ekspor {runId}` berisi Status `Not applied`, karena Category-nya sudah dihapus
76. Verifikasi baris override Group `Workshop Ekspor {runId}` pada Category `Kategori Nonaktif Ekspor {runId}` berisi Status `Not applied`, karena Category-nya dinonaktifkan
77. Verifikasi baris override Group `Arsip Dua Ekspor {runId}` berisi Created By `Citra Dihapus {runId}`, nama lengkap snapshot pembuat yang sudah dihapus
78. Verifikasi baris Category `Kendaraan {runId} > Mobil Pool {runId}`, Transaction `Assign`, Field `Max assets per assignee (concurrent)` berisi Value `0` sebagai angka dan Source `Company default`, bukan teks `Unlimited`

### Export saat plan membuka Transfer, Approval Workflow, dan Duration unit Hours
79. Operator Plan menerapkan plan kustom `Paket Ekspor {runId}` pada entitas, dengan Approval Workflow ON, Feature Suite Borrowing `Full`, Feature Suite Assignment `Basic`, Feature Suite pemindahan `Basic`, dan Feature Suite Disposal `Full`
80. Maya Pengelola menyimpan Category `Truk Ekspor {runId}` dengan Max duration `6` dan Duration unit `Hours`
81. Maya Pengelola menjalankan Export rules dengan Category `Truk Ekspor {runId}` terpilih di Sidebar Category Tree
82. Verifikasi baris Transaction `Borrow`, Field `Max duration` berisi Value `6` dan Unit `hours`
83. Verifikasi kolom Transaction sheet Rules memuat `Transfer`, karena level Feature Suite pemindahan bukan `None`
84. Verifikasi sheet Rules tidak memuat Field `Change Cost Center with Group`, karena Category leaf tidak memuat field khusus All categories
85. Verifikasi baris Approval Workflow sheet Info berisi `Available`

### Export All categories saat plan membuka Transfer
86. Maya Pengelola menjalankan Export rules dengan All categories terpilih di Sidebar Category Tree
87. Verifikasi baris Category `All categories`, Transaction `Transfer`, Field `Change Cost Center with Group` tampil
88. Verifikasi baris Category `All categories`, Transaction `Damaged & Missing`, Field `After photo required` tampil

### Export saat addon `Audit` dan addon `Maintenance` dialokasikan
89. Operator Plan mengalokasikan lisensi addon `Audit` dan addon `Maintenance` (DU-092-35) ke subscription FAMS entitas lewat License Allocation
90. Maya Pengelola menjalankan Export rules dengan Category `Truk Ekspor {runId}` terpilih di Sidebar Category Tree
91. Verifikasi kolom Transaction sheet Rules memuat `Maintenance`, karena addon Maintenance dialokasikan
92. Verifikasi sheet Rules memuat baris Category `Truk Ekspor {runId}`, Transaction `Maintenance`, Field `Photo after`, karena field tab Maintenance muncul per Category seperti field transaksi
93. Verifikasi sheet Rules tidak memuat baris Transaction `Audit`, Field `Grace period`, maupun Field `Require location`, karena export Category leaf tidak memuat field tab `Audit` dan `Geolocation`
94. Maya Pengelola menjalankan Export rules dengan All categories terpilih di Sidebar Category Tree
95. Verifikasi sheet Rules memuat baris Category `All categories`, Transaction `Audit` untuk Field `Grace period`, `Require approval`, `Approval type`, dan `Send email notifications`
96. Verifikasi sheet Rules memuat baris Category `All categories`, Transaction `Audit` dan Transaction `Maintenance` masing-masing untuk Field `Require location`
97. Verifikasi Field `Grace period` dan `Require location` hanya muncul pada baris Category `All categories`, dan tidak muncul pada baris Category `Truk Ekspor {runId}`

### Sheet Info dan nilai label teks sesudah plan kustom diterapkan
98. Maya Pengelola menjalankan Export rules dengan Category `Truk Ekspor {runId}` terpilih di Sidebar Category Tree
99. Verifikasi baris Feature Suite Borrowing sheet Info berisi `Full`
100. Verifikasi baris Feature Suite Assignment sheet Info berisi `Basic`
101. Verifikasi baris Feature Suite Transfer sheet Info berisi `Basic`
102. Verifikasi baris Feature Suite Disposal sheet Info berisi `Full`
103. Verifikasi baris Transaction `Assign`, Field `Allow Assign` berisi Value `Allow` sebagai label teks dan Source `Company default`
104. Verifikasi baris Transaction `Borrow`, Field `Duration unit` berisi Value `Hours` sebagai label teks pilihan tunggal
105. Verifikasi baris Transaction `Disposal`, Field `Max price drop from approved price` berisi Value `10`, Unit `%`, dan Source `Company default`
