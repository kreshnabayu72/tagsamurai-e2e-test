---
id: TC-FA-ASSIGN-UI-115-dialog-mark-as-unassigned
title: "Dialog Mark as Unassigned: pilihan hasil dan Reason"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-ASG-26, FLD-ASG-20, FLD-ASG-21, "EB-FRM-1@mark-as-unassigned", "EB-FRM-7@mark-as-unassigned", "EB-FRM-4@reason-mark-unassigned"]
smoke: []
dependsOn: []
trace:
  D-ASG-26: [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 19, 20, 21, 22, 23]
  FLD-ASG-20: [6, 7, 13, 15, 20]
  FLD-ASG-21: [26, 31, 40, 45]
  "EB-FRM-1@mark-as-unassigned": [50, 51, 53]
  "EB-FRM-7@mark-as-unassigned": [55, 56, 57, 59, 61]
  "EB-FRM-4@reason-mark-unassigned": [26, 28, 31, 33, 37, 40, 42, 45, 47]
anchor: []
coverage:
  web: automated
---
# Dialog Mark as Unassigned: pilihan hasil dan Reason

## Prerequisites
- Aktor: Asset Admin pada Group `Head Office`.
- Layar awal: halaman daftar aset pada level None, tempat aksi `Mark as Unassigned` tersedia pada baris dan bulk.
- Komponen: Dialog Mark as Unassigned
- Data:
  - DU-115-1: Aset Assigned Name `Laptop Dell Latitude 5420 - 4`, Assignee `Budi Santoso`, Assigned since `12 Oct 2026`.
  - DU-115-2: Aset Assigned Name `Printer HP M404 - 3`, Assignee `Finance · PIC Sari Dewi`, Assigned since `03 Oct 2026`.
  - DU-115-3: Aset Assigned Name `Laptop Dell Latitude 5420 - 10`, Assignee `Budi Santoso`, Assigned since `12 Oct 2026`.
  - DU-115-4: Aset Assigned Name `Toyota Avanza - 6`, Assignee `Sari Dewi`, Assigned since `05 Oct 2026`.
  - DU-115-5: Aset bukan Assigned Name `Aset belum ditugaskan {n}`; jumlah 2.
  - DU-115-6: Aset penugasan Aktor sendiri Name `Aset penugasan sendiri {n}`; jumlah 3.
  - DU-115-7: Reason Reason `PenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifan`.
  - DU-115-8: Reason Reason `PenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanx`.
  - DU-115-9: Reason Reason ` PenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifan `.
  - DU-115-10: Reason Reason `Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegan`.
  - DU-115-11: Reason Reason `PénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPenonaktif𝒜n`.
- Kondisi:
  - K1: level None; dialog dibuka untuk satu aset DU-115-1.
  - K2: level None; dialog dibuka untuk satu aset DU-115-2 (Assignee Division); teks yang diharapkan `Finance · PIC Sari Dewi`.
  - K3: level None; dialog dibuka dari bulk atas tujuh aset terpilih, yaitu DU-115-3, DU-115-4, 2 aset DU-115-5, dan 3 aset DU-115-6; teks yang diharapkan `2 assets skipped because they aren't assigned.` dan `3 assets skipped because they're yours.`, dari jumlah DU-115-5 dan DU-115-6.
  - K4: seperti K1; simpan lambat.
  - K5: seperti K1; dialog dibuka dari baris aset DU-115-1.

## Test Steps

### Satu aset: isi dialog dan pilihan hasil
1. Tampilkan Dialog Mark as Unassigned dengan kondisi K1
2. Verifikasi judul dialog `Mark as Unassigned`
3. Verifikasi dialog memuat nama aset `Laptop Dell Latitude 5420 - 4`
4. Verifikasi dialog memuat Assignee `Budi Santoso`
5. Verifikasi dialog memuat Assigned since `12 Oct 2026`
6. Verifikasi pilihan hasil `Unassigned`, `Missing`, dan `Damaged` tampil
7. Verifikasi pilihan hasil `Unassigned` terpilih secara default
8. Verifikasi dialog memuat field Reason
9. Verifikasi dialog tidak memuat scan dan foto
10. Verifikasi dialog memuat tombol `[Cancel]` dan `[Mark as Unassigned]`

### Memilih hasil Missing atau Damaged
11. Tampilkan Dialog Mark as Unassigned dengan kondisi K1
12. Pilih hasil `Missing`
13. Verifikasi hasil `Missing` terpilih dan `Unassigned` tidak lagi terpilih
14. Pilih hasil `Damaged`
15. Verifikasi hasil `Damaged` terpilih dan `Missing` tidak lagi terpilih

### Satu aset Division menampilkan Division dan PIC
16. Tampilkan Dialog Mark as Unassigned dengan kondisi K2
17. Verifikasi dialog memuat Assignee `Finance · PIC Sari Dewi`

### Bulk: daftar aset diproses tanpa pilihan hasil
18. Tampilkan Dialog Mark as Unassigned dengan kondisi K3
19. Verifikasi dialog memuat daftar aset Assigned `Laptop Dell Latitude 5420 - 10` dan `Toyota Avanza - 6`
20. Verifikasi dialog tidak memuat pilihan hasil karena hasilnya selalu Unassigned
21. Verifikasi dialog memuat field Reason
22. Verifikasi dialog memuat teks `2 assets skipped because they aren't assigned.`
23. Verifikasi dialog memuat teks `3 assets skipped because they're yours.` sebagai baris kedua

### Reason tepat di batas panjang diterima
24. Tampilkan Dialog Mark as Unassigned dengan kondisi K1
25. Isi Reason `PenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifan` (360 karakter)
26. Verifikasi isi field Reason memuat 360 karakter
27. Klik `[Mark as Unassigned]`
28. Verifikasi dialog Mark as Unassigned tertutup

### Reason satu karakter melewati batas dipotong pada batas
29. Tampilkan Dialog Mark as Unassigned dengan kondisi K1
30. Isi Reason `PenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanx` (361 karakter)
31. Verifikasi isi field Reason terpotong tepat pada 360 karakter
32. Klik `[Mark as Unassigned]`
33. Verifikasi dialog Mark as Unassigned tertutup

### Reason tepat di batas dengan spasi tepi diterima
34. Tampilkan Dialog Mark as Unassigned dengan kondisi K1
35. Isi Reason ` PenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifanPenonaktifan `
36. Klik `[Mark as Unassigned]`
37. Verifikasi dialog Mark as Unassigned tertutup

### Reason tepat di batas dengan spasi tengah diterima
38. Tampilkan Dialog Mark as Unassigned dengan kondisi K1
39. Isi Reason `Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegang. Aset dikembalikan oleh pemegan` (360 karakter)
40. Verifikasi isi field Reason memuat 360 karakter termasuk spasi tengah
41. Klik `[Mark as Unassigned]`
42. Verifikasi dialog Mark as Unassigned tertutup

### Reason tepat di batas dengan huruf beraksen dan karakter non-BMP diterima
43. Tampilkan Dialog Mark as Unassigned dengan kondisi K1
44. Isi Reason `PénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPénonaktifanPenonaktif𝒜n` (360 karakter)
45. Verifikasi isi field Reason memuat 360 karakter
46. Klik `[Mark as Unassigned]`
47. Verifikasi dialog Mark as Unassigned tertutup

### Saving: tombol aksi masuk loading dan klik kedua tidak mengirim request kedua
48. Tampilkan Dialog Mark as Unassigned dengan kondisi K4
49. Klik `[Mark as Unassigned]`
50. Verifikasi `[Mark as Unassigned]` masuk saving state dan disabled
51. Verifikasi seluruh kontrol form termasuk ikon penutup disabled selama menunggu respons Mark as Unassigned
52. Klik `[Mark as Unassigned]` sekali lagi
53. Verifikasi permintaan terkirim satu kali

### Aksesibilitas form
54. Tampilkan Dialog Mark as Unassigned dengan kondisi K5
55. Verifikasi fokus masuk ke dalam dialog saat dialog terbuka
56. Verifikasi pilihan hasil memiliki `aria-required`
57. Verifikasi ikon penutup memiliki label aksesibel
58. Tekan Tab sebanyak jumlah kontrol di dialog ditambah satu
59. Verifikasi fokus tetap berada di dalam dialog
60. Klik `[Cancel]`
61. Verifikasi fokus kembali ke pemicu dialog Mark as Unassigned
