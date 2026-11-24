---
id: TC-FA-FATR-E2E-021-changelog-search
title: "Search dan Column Visibility tabel Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r425, §4.1#r428, §4.1#r429, §4.1#r426, §4.1#r427, §4.1#r430, §5#r3, §9.4.2#r53, EB-SRC-2@changelog, EB-SRC-3@changelog, EB-SRC-5@changelog, EB-KOL-2@changelog, §4.1#r424]
smoke: []
dependsOn: []
trace:
  §4.1#r425: 12
  §4.1#r428: [20, 21]
  §4.1#r429: [23, 24]
  §4.1#r426: [14, 15]
  §4.1#r427: [17, 18]
  §4.1#r430: [26, 27]
  §5#r3: [12, 26, 33, 35, 36]
  §9.4.2#r53: 60
  EB-SRC-2@changelog: [45, 46, 54]
  EB-SRC-3@changelog: [56, 58]
  EB-SRC-5@changelog: [68, 72]
  EB-KOL-2@changelog: 80
  §4.1#r424: 54
anchor: [3, 52, 66, 83]
coverage:
  web: automated
---
# Search dan Column Visibility tabel Changelog

## Prerequisites
- Aktor: Total Control `Rina Wulandari`.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-021-1: Changelog Category `Elektronik {runId} > Laptop {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, New Value `30 days`, Action `Edit`, Modified By `Rina W`, Date T0.
  - DU-021-2: Changelog Category `Elektronik {runId} > Proyektor {runId}`, Field `Transfer (Approval type)`, Old Value `Any one approver`, New Value `All approvers (AND)`, Action `Edit`, Modified By `Budi S`, dari Name `Budi Santoso`, Date T0.
  - DU-021-3: Changelog Category `Elektronik {runId} > Laptop {runId}`, Field `Disposal (Allowed disposal types)`, Old Value `Sell, Scrap, Donate, Trade-in`, New Value `Sell, Scrap, Trade-in`, Action `Edit`, Modified By `Rina W`, Date T0.
  - DU-021-4: Changelog Category `Elektronik {runId} > Printer {runId}`, Field `Borrow (Max extensions)`, Old Value `No extension`, New Value `Inherit`, Action `Edit`, Modified By `Rina W`, Date T0.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Search mencocokkan nilai di setiap kolom yang searchable
1. Klik ikon Changelog di header
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi tabel memuat keempat baris data uji: baris Field `Borrow (Max duration)`, baris Field `Transfer (Approval type)`, baris Field `Disposal (Allowed disposal types)`, dan baris Field `Borrow (Max extensions)`
4. Klik tombol filter di toolbar dialog Changelog
5. Klik field `Category` pada panel filter
6. Ketik `{runId}` pada kotak cari opsi Category
7. Pilih opsi `Elektronik {runId} > Laptop {runId}`
8. Pilih opsi `Elektronik {runId} > Proyektor {runId}`
9. Pilih opsi `Elektronik {runId} > Printer {runId}`
10. Klik `[Apply]`
11. Ganti isi kotak search dengan `Edit`, tekan Enter
12. Verifikasi keempat baris data uji tampil karena kolom Action bernilai `Edit` pada semuanya
13. Ganti isi kotak search dengan `Proyektor {runId}`, tekan Enter
14. Verifikasi baris Field `Transfer (Approval type)` tampil
15. Verifikasi baris Field `Borrow (Max duration)`, baris Field `Disposal (Allowed disposal types)`, dan baris Field `Borrow (Max extensions)` tidak tampil
16. Ganti isi kotak search dengan `Approval type`, tekan Enter
17. Verifikasi baris Field `Transfer (Approval type)` tampil
18. Verifikasi baris Field `Borrow (Max duration)`, baris Field `Disposal (Allowed disposal types)`, dan baris Field `Borrow (Max extensions)` tidak tampil
19. Ganti isi kotak search dengan `Any one approver`, tekan Enter
20. Verifikasi baris Field `Transfer (Approval type)` tampil
21. Verifikasi baris Field `Borrow (Max duration)`, baris Field `Disposal (Allowed disposal types)`, dan baris Field `Borrow (Max extensions)` tidak tampil
22. Ganti isi kotak search dengan `30 days`, tekan Enter
23. Verifikasi baris Field `Borrow (Max duration)` tampil
24. Verifikasi baris Field `Transfer (Approval type)`, baris Field `Disposal (Allowed disposal types)`, dan baris Field `Borrow (Max extensions)` tidak tampil
25. Ganti isi kotak search dengan `Budi S`, tekan Enter
26. Verifikasi baris Field `Transfer (Approval type)` tampil
27. Verifikasi baris Field `Borrow (Max duration)`, baris Field `Disposal (Allowed disposal types)`, dan baris Field `Borrow (Max extensions)` tidak tampil
28. Klik `[Clear Field]`
29. Klik `[Apply]`
30. Klik `✕` pada dialog Changelog

### Search memakai substring, tanpa membedakan huruf besar kecil, dan lintas kolom
31. Klik ikon Changelog di header
32. Ketik Search `royekt`, tekan Enter
33. Verifikasi baris Field `Transfer (Approval type)` tampil karena kata kunci berada di tengah Category `Elektronik {runId} > Proyektor {runId}`
34. Ganti isi kotak search dengan `LAPTOP {runId}`, tekan Enter
35. Verifikasi baris Field `Borrow (Max duration)` dan baris Field `Disposal (Allowed disposal types)` tampil
36. Verifikasi baris Field `Transfer (Approval type)` dan baris Field `Borrow (Max extensions)` tidak tampil
37. Klik tombol filter di toolbar dialog Changelog
38. Klik field `Category` pada panel filter
39. Ketik `{runId}` pada kotak cari opsi Category
40. Pilih opsi `Elektronik {runId} > Laptop {runId}`
41. Pilih opsi `Elektronik {runId} > Proyektor {runId}`
42. Pilih opsi `Elektronik {runId} > Printer {runId}`
43. Klik `[Apply]`
44. Ganti isi kotak search dengan `Inherit`, tekan Enter
45. Verifikasi baris Field `Borrow (Max duration)` tampil karena Old Value `Inherit` dan baris Field `Borrow (Max extensions)` tampil karena New Value `Inherit`
46. Verifikasi baris Field `Transfer (Approval type)` dan baris Field `Disposal (Allowed disposal types)` tidak tampil
47. Klik `[Clear Field]`
48. Klik `[Apply]`
49. Klik `✕` pada dialog Changelog

### Search tidak mencari di kolom Date dan karakter khusus dicari sebagai teks
50. Klik ikon Changelog di header
51. Ketik Search `{runId}`, tekan Enter
52. Verifikasi baris Field `Transfer (Approval type)` tampil
53. Ganti isi kotak search dengan tanggal T0 dalam Date Format `dd/MM/yy`, tekan Enter
54. Verifikasi baris Field `Borrow (Max duration)`, baris Field `Transfer (Approval type)`, baris Field `Disposal (Allowed disposal types)`, dan baris Field `Borrow (Max extensions)` tidak tampil karena kolom Date tidak ikut dicari
55. Ganti isi kotak search dengan ` All approvers `, tekan Enter
56. Verifikasi baris Field `Transfer (Approval type)` tampil karena spasi di awal dan akhir kata kunci dibuang dan spasi di tengah dipertahankan
57. Ganti isi kotak search dengan `%`, tekan Enter
58. Verifikasi baris Field `Borrow (Max duration)`, baris Field `Transfer (Approval type)`, baris Field `Disposal (Allowed disposal types)`, dan baris Field `Borrow (Max extensions)` tidak tampil karena `%` dicari sebagai teks
59. Ganti isi kotak search dengan `Zzqx {runId}`, tekan Enter
60. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
61. Klik `✕` pada dialog Changelog

### Kolom searchable yang disembunyikan tidak lagi cocok
62. Klik ikon Changelog di header
63. Klik header kolom Actions pada tabel Changelog
64. Hapus centang kolom `Old Value`
65. Ketik Search `{runId}`, tekan Enter
66. Verifikasi baris Field `Transfer (Approval type)` tampil
67. Ganti isi kotak search dengan `Any one approver`, tekan Enter
68. Verifikasi baris Field `Transfer (Approval type)` tidak tampil karena kolom Old Value disembunyikan
69. Klik header kolom Actions pada tabel Changelog
70. Centang kolom `Old Value`
71. Ganti isi kotak search dengan `Any one approver`, tekan Enter
72. Verifikasi baris Field `Transfer (Approval type)` tampil lagi karena kolom Old Value ditampilkan
73. Klik `✕` pada dialog Changelog

### Konfigurasi kolom bertahan sesudah muat ulang halaman
74. Klik ikon Changelog di header
75. Klik header kolom Actions pada tabel Changelog
76. Hapus centang kolom `Old Value`
77. Klik `✕` pada dialog Changelog
78. Muat ulang halaman
79. Klik ikon Changelog di header
80. Verifikasi kolom `Old Value` tidak tampil pada tabel Changelog
81. Klik header kolom Actions pada tabel Changelog
82. Centang kolom `Old Value`
83. Verifikasi kolom `Old Value` tampil pada tabel Changelog
84. Klik `✕` pada dialog Changelog
