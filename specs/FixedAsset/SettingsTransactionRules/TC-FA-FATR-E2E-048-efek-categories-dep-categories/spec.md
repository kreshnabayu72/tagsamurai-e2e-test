---
id: TC-FA-FATR-E2E-048-efek-categories-dep-categories
title: "Setting dan override mengikuti perubahan Category"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r16", "§4.1#r17", "§4.1#r19", "§4.1#r21", "§4.1#r22", "§4.1#r23", "§4.1#r24", "§4.1#r25", "§4.1#r246", "§4.1#r247", "§9.2#b6", "§9.2#b122", "§9.2#b124", "§9.2#b147", "§9.4.2#r34", "§9.4.2#r55", "§9.2#b35", "§9.2#b36", "EB-EDG-3"]
smoke: ["§9.2#b35", "§9.2#b36", "EB-EDG-3"]
dependsOn:
  - "Settings Categories: hapus, nonaktifkan, dan tambah sub-Category"
trace:
  "§4.1#r16": 8
  "§4.1#r17": 11
  "§4.1#r19": [9, 21, 39]
  "§4.1#r21": 12
  "§4.1#r22": [33, 73]
  "§4.1#r23": [28, 15, 47]
  "§4.1#r24": [38, 59, 67]
  "§4.1#r25": [40, 60, 68]
  "§4.1#r246": [52, 23]
  "§4.1#r247": [53, 54, 24, 25]
  "§9.2#b6": [8, 11]
  "§9.2#b122": 51
  "§9.2#b124": [52, 23]
  "§9.2#b147": 51
  "§9.4.2#r34": [51, 53]
  "§9.4.2#r55": [8, 11, 12]
  "§9.2#b35": 46
  "§9.2#b36": 43
  "EB-EDG-3": 53
anchor: [3, 19]
coverage:
  web: automated
---

# Setting dan override mengikuti perubahan Category

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update); aktor lain yang menjalankan aksi pada Category: `Rudi Hartono {runId}`.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-048-1: Group Name `Field Operations {runId}`; Group tanpa Division.
  - DU-048-2: Category Name `Safety Equipment {runId}`, Max duration `20 Days`; Category leaf dengan Max duration Borrow nilai sendiri, akan menjadi Category induk.
  - DU-048-3: Category Name `Surveying Tools {runId}`, Max duration `16 Days`; Category leaf dengan Max duration Borrow nilai sendiri, akan dihapus.
  - DU-048-4: Category Name `Lab Instruments {runId}`, Max duration `25 Days`; Category leaf dengan Max duration Borrow nilai sendiri, akan dinonaktifkan lalu diaktifkan kembali.
  - DU-048-7: Override Target `Field Operations {runId}`, Scope `Group`, Category `Safety Equipment {runId}`, Transaction `Borrow`, Max duration `10 Days`; override Group pada Category yang akan menjadi induk.
  - DU-048-8: Override Target `Field Operations {runId}`, Scope `Group`, Category `Surveying Tools {runId}`, Transaction `Borrow`, Max duration `9 Days`; override Group pada Category yang akan dihapus.
  - DU-048-9: Changelog Category `Lab Instruments {runId}`, Field `Borrow (Max duration)`, Old `14 Days`, New `25 Days`; entri Changelog lama perubahan Category yang akan dinonaktifkan.
  - DU-048-10: User Name `Rudi Hartono {runId}`, Role `Default User`; akun Default User kedua yang menghapus dan menonaktifkan Category.
  - DU-048-12: Override Target `Field Operations {runId}`, Scope `Group`, Category `Lab Instruments {runId}`, Transaction `Borrow`, Max duration `12 Days`; override Group pada Category yang akan dinonaktifkan.
  - DU-048-13: Changelog Category `Safety Equipment {runId}`, Field `Borrow (Max duration)`, Old `14 Days`, New `20 Days`; entri Changelog lama perubahan Category yang akan menjadi induk.
  - DU-048-14: Changelog Category `Surveying Tools {runId}`, Field `Borrow (Max duration)`, Old `14 Days`, New `16 Days`; entri Changelog lama perubahan Category yang akan dihapus.
  - DU-048-15: Category Name `Calibration Gear {runId}`, Max duration `12 Days`; Category leaf dengan Max duration Borrow nilai sendiri, akan menjadi Category induk saat draft belum disimpan.
  - DU-048-16: Category Name `Test Rigs {runId}`, Max duration `15 Days`; Category leaf dengan Max duration Borrow nilai sendiri, akan dinonaktifkan saat draft belum disimpan.
  - Entri Changelog baru yang diharapkan sesudah Save pada Category `Surveying Tools {runId}`: Field `Borrow (Max duration)`, Old Value `16 Days` dari nilai tersimpan DU-048-3, New Value `18 Days` dari Max duration `18` yang diisi.
- Kondisi:
  - Akun `Rudi Hartono {runId}` aktif dan kredensialnya tersedia untuk login.

## Test Steps
### Category leaf yang menjadi Category induk
1. Masuk sebagai Default User
2. Buka tab `Borrow` pada node Category `Safety Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
3. Verifikasi Max duration `20` sebagai nilai sendiri Category `Safety Equipment {runId}` dan override untuk target `Field Operations {runId}` tampil di tabel Overrides
4. `Rudi Hartono {runId}` menambah sub-Category `Helmets {runId}` pada Category `Safety Equipment {runId}`
5. Buka tab `Borrow` pada node All categories di Fixed Asset > Settings > Transaction Settings
6. Klik header kolom Actions pada tabel Overrides
7. Centang kolom `Category`
8. Verifikasi override untuk target `Field Operations {runId}` pada Category `Safety Equipment {runId}` tetap tersimpan dan tampil di tabel Overrides
9. Verifikasi Sidebar Category Tree tidak menampilkan nilai setting Max duration `20` milik Category `Safety Equipment {runId}`
10. Buka tab `Borrow` pada node Category `Helmets {runId}`
11. Verifikasi semua field Category `Helmets {runId}` bernilai Inherit
12. Verifikasi Max duration efektif Category `Helmets {runId}` bernilai `14` dari Company default, bukan `20` dari Category `Safety Equipment {runId}`
13. Buka dialog Changelog dari header halaman Transaction Settings
14. Ketik Search `Safety Equipment {runId}`, tekan Enter
15. Verifikasi entri Changelog lama untuk Category `Safety Equipment {runId}` dengan Field `Borrow (Max duration)`, Old Value `14 Days`, dan New Value `20 Days` tetap terbaca
16. Klik `(←)` pada kotak Search
17. Tutup dialog Changelog

### Category yang dinonaktifkan lalu diaktifkan kembali
18. Buka tab `Borrow` pada node Category `Lab Instruments {runId}` di Fixed Asset > Settings > Transaction Settings
19. Verifikasi Max duration `25` sebagai nilai sendiri Category `Lab Instruments {runId}`
20. `Rudi Hartono {runId}` menonaktifkan Category `Lab Instruments {runId}`
21. Verifikasi Sidebar Category Tree tidak menampilkan nilai setting Max duration `25` milik Category `Lab Instruments {runId}`
22. Buka tab `Borrow` pada node All categories di Fixed Asset > Settings > Transaction Settings
23. Verifikasi override untuk target `Field Operations {runId}` pada Category `Lab Instruments {runId}` tetap tersimpan dan tampil di tabel Overrides dengan nama target dan Category yang tersimpan
24. Verifikasi `Not applied` tampil pada sel Target baris override untuk target `Field Operations {runId}` pada Category `Lab Instruments {runId}`
25. Verifikasi alasan `This override doesn't apply because its target or category was deleted or deactivated.` tersampaikan pada `Not applied` di sel Target
26. Buka dialog Changelog dari header halaman Transaction Settings
27. Ketik Search `Lab Instruments {runId}`, tekan Enter
28. Verifikasi entri Changelog lama untuk Category `Lab Instruments {runId}` dengan Field `Borrow (Max duration)`, Old Value `14 Days`, dan New Value `25 Days` tetap terbaca
29. Klik `(←)` pada kotak Search
30. Tutup dialog Changelog
31. `Rudi Hartono {runId}` mengaktifkan kembali Category `Lab Instruments {runId}`
32. Buka tab `Borrow` pada node Category `Lab Instruments {runId}` di Fixed Asset > Settings > Transaction Settings
33. Verifikasi Max duration `25` berlaku lagi untuk Category `Lab Instruments {runId}`

### Category yang sedang aktif di area utama dihapus
34. Buka tab `Borrow` pada node Category `Surveying Tools {runId}` di Fixed Asset > Settings > Transaction Settings
35. Isi Max duration dengan `18`
36. Klik tab `Disposal`
37. `Rudi Hartono {runId}` menghapus Category `Surveying Tools {runId}`
38. Verifikasi area utama pindah ke node All categories pada tab pertama yang tersedia, bukan tab `Disposal` yang aktif sebelumnya
39. Verifikasi Sidebar Category Tree tidak menampilkan nilai setting Max duration `16` milik Category `Surveying Tools {runId}`
40. Verifikasi draft Max duration `18` yang belum disimpan untuk Category `Surveying Tools {runId}` tetap di draft
41. Klik `[Save]`
42. Klik `[Save]` pada dialog Save Changes
43. Verifikasi Save tidak ditolak karena draft pada Category `Surveying Tools {runId}` yang sudah dihapus
44. Buka dialog Changelog dari header halaman Transaction Settings
45. Ketik Search `Surveying Tools {runId}`, tekan Enter
46. Verifikasi Changelog memuat entri perubahan Max duration untuk Category `Surveying Tools {runId}` dengan Field `Borrow (Max duration)`, Old Value `16 Days`, dan New Value `18 Days` sebagai nilai tersimpan
47. Verifikasi entri Changelog lama untuk Category `Surveying Tools {runId}` dengan Field `Borrow (Max duration)`, Old Value `14 Days`, dan New Value `16 Days` tetap terbaca
48. Klik `(←)` pada kotak Search
49. Tutup dialog Changelog
50. Buka tab `Borrow` pada node All categories di Fixed Asset > Settings > Transaction Settings
51. Verifikasi override untuk target `Field Operations {runId}` pada Category `Surveying Tools {runId}` tetap tersimpan dan tampil di tabel Overrides
52. Verifikasi nama terakhir Category `Surveying Tools {runId}` tetap tampil bersama target `Field Operations {runId}` pada baris override itu
53. Verifikasi `Not applied` tampil pada sel Target baris override untuk target `Field Operations {runId}` pada Category `Surveying Tools {runId}`
54. Verifikasi alasan `This override doesn't apply because its target or category was deleted or deactivated.` tersampaikan pada `Not applied` di sel Target

### Category yang menjadi Category induk memindahkan area utama dan mempertahankan draft
55. Buka tab `Borrow` pada node Category `Calibration Gear {runId}` di Fixed Asset > Settings > Transaction Settings
56. Isi Max duration dengan `13`
57. Klik tab `Disposal`
58. `Rudi Hartono {runId}` menambah sub-Category `Probes {runId}` pada Category `Calibration Gear {runId}`
59. Verifikasi area utama pindah ke node All categories pada tab pertama yang tersedia, bukan tab `Disposal` yang aktif sebelumnya
60. Verifikasi tombol `[Save]` aktif karena draft Max duration `13` untuk Category `Calibration Gear {runId}` tetap di draft
61. Klik `[Save]`
62. Klik `[Save]` pada dialog Save Changes

### Category yang dinonaktifkan memindahkan area utama dan mempertahankan draft
63. Buka tab `Borrow` pada node Category `Test Rigs {runId}` di Fixed Asset > Settings > Transaction Settings
64. Isi Max duration dengan `11`
65. Klik tab `Disposal`
66. `Rudi Hartono {runId}` menonaktifkan Category `Test Rigs {runId}`
67. Verifikasi area utama pindah ke node All categories pada tab pertama yang tersedia, bukan tab `Disposal` yang aktif sebelumnya
68. Verifikasi tombol `[Save]` aktif karena draft Max duration `11` untuk Category `Test Rigs {runId}` tetap di draft
69. Klik `[Save]`
70. Klik `[Save]` pada dialog Save Changes

### Category induk yang kembali menjadi leaf mempertahankan nilainya
71. `Rudi Hartono {runId}` menghapus sub-Category `Helmets {runId}` dari Category `Safety Equipment {runId}`
72. Buka tab `Borrow` pada node Category `Safety Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
73. Verifikasi Max duration `20` sebagai nilai sendiri Category `Safety Equipment {runId}` tetap `20` sesudah Category kembali menjadi leaf
