---
id: TC-FA-ASTL-UI-076-dialog-edit-purchase-interaksi
title: "Mekanik form: Saving, Unsaved, Clear Field, toast"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-20", "T-27", "T-28", "§6#r9", "EB-FB-1@edit-purchase", "EB-FB-2@edit-purchase", "EB-FB-3@edit-purchase", "EB-FRM-1@edit-purchase", "EB-FRM-2@edit-purchase", "EB-FRM-3@edit-purchase", "EB-FRM-7@edit-purchase", "EB-ERR-1@edit-purchase"]
smoke: []
dependsOn: []
trace:
  "T-20": [20, 29]
  "T-27": [25]
  "T-28": [2, 4, 6, 10]
  "§6#r9": [25, 34, 89, 90]
  "EB-FB-1@edit-purchase": [20, 25, 29]
  "EB-FB-2@edit-purchase": [43, 59, 62, 66, 71]
  "EB-FB-3@edit-purchase": [10, 11]
  "EB-FRM-1@edit-purchase": [15, 16, 18, 21]
  "EB-FRM-2@edit-purchase": [42, 46, 52, 56, 58, 61, 65, 68, 70]
  "EB-FRM-3@edit-purchase": [38, 39]
  "EB-FRM-7@edit-purchase": [47, 73, 74, 75, 78, 80]
  "EB-ERR-1@edit-purchase": [25, 26, 27, 30, 34, 35, 84, 85, 89, 90]
anchor: []
coverage:
  web: automated
---
# Mekanik form: Saving, Unsaved, Clear Field, toast

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Edit Purchase
- Data:
  - DU-076-1: Aset `Laptop Pro 16 - 1`, Asset ID `AST-0001`, Group `IT`, Purchase Date `10/03/26`, Purchase Cost `18.500.000,00`, Document No. `INV-2026-0301`.
  - DU-076-2: Aset `Laptop Pro 16 - 2`, Asset ID `AST-0002`, Group `IT`, Purchase Cost `18.500.000,00`.
  - DU-076-3: Aset `Kursi Kerja - 3`, Asset ID `AST-0074`, Group `GA`, Purchase `Pending` dengan field Purchase kosong, custom field Purchasing wajib `Contract number` kosong.
  - DU-076-4: Document No. `INV-2026-0302`.
  - DU-076-5: Purchase Cost Bulk `18.500.000,00`.
  - DU-076-6: Purchase Cost Bulk yang berbeda dari nilai tersimpan `19.000.000,00`.
  - Alert yang diharapkan untuk aset berjejak Posted: `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`
  - Pesan yang diharapkan untuk custom field wajib kosong: `Contract number must not be empty`, dari nama field `Contract number`.
- Kondisi:
  - K1: satu aset terpilih, DU-076-1; simpan berhasil.
  - K2: satu aset terpilih, DU-076-1; simpan berhasil setelah respons tertunda.
  - K3: satu aset terpilih, DU-076-1; simpan pertama gagal karena error server, simpan berikutnya berhasil.
  - K4: satu aset terpilih, DU-076-1; simpan gagal karena timeout atau jaringan terputus.
  - K5: Bulk, seleksi DU-076-1 dan DU-076-2; Purchase Cost yang diisi sama dengan nilai tersimpan pada kedua aset, sehingga server menjawab tanpa perubahan.
  - K6: satu aset terpilih, DU-076-3.
  - K7: satu aset terpilih, DU-076-1; simpan ditolak server dengan `422` karena aset berjejak Posted, versi dan status aset tidak berubah sejak dialog dibuka.
  - K8: Bulk, seleksi DU-076-1 dan DU-076-2; simpan gagal karena timeout atau jaringan terputus.

## Test Steps

### Save aktif hanya selama ada perubahan
1. Tampilkan Dialog Edit Purchase dengan kondisi K1
2. Verifikasi `[Save]` Disabled karena belum ada perubahan
3. Isi Document No. `INV-2026-0302`
4. Verifikasi `[Save]` aktif
5. Isi Document No. `INV-2026-0301`
6. Verifikasi `[Save]` Disabled kembali karena nilai dikembalikan ke nilai awal

### Bulk tanpa perubahan nilai
7. Tampilkan Dialog Edit Purchase dengan kondisi K5
8. Isi `Purchase Cost (per asset)` `18.500.000,00`
9. Klik `[Save]`
10. Verifikasi toast `No changes to save.` tampil
11. Verifikasi dialog `Edit Purchase` tertutup

### Simpan satu kali dengan toast sukses
12. Tampilkan Dialog Edit Purchase dengan kondisi K2
13. Isi Document No. `INV-2026-0302`
14. Klik `[Save]`
15. Verifikasi `[Save]` tidak bisa diklik selama permintaan berjalan
16. Verifikasi seluruh kontrol form, tombol `[Clear Field]`, dan tombol tutup `✕` Disabled selama permintaan berjalan
17. Klik `[Save]` sekali lagi saat permintaan masih berjalan
18. Verifikasi permintaan simpan hanya terkirim satu kali
19. Respons simpan berhasil diterima
20. Verifikasi toast `Success, purchase data has been saved.` tampil
21. Verifikasi dialog `Edit Purchase` tertutup

### Kegagalan server mempertahankan form
22. Tampilkan Dialog Edit Purchase dengan kondisi K3
23. Isi Document No. `INV-2026-0302`
24. Klik `[Save]`
25. Verifikasi toast `Error, failed to save purchase data.` tampil
26. Verifikasi dialog `Edit Purchase` tetap terbuka dengan Document No. `INV-2026-0302` dan `[Save]` aktif kembali
27. Verifikasi toast `Error, failed to save purchase data.` tidak memiliki tombol aksi seperti `[Try Again]`
28. Klik `[Save]`
29. Verifikasi toast `Success, purchase data has been saved.` tampil
30. Verifikasi dialog `Edit Purchase` tertutup dan simpan berhasil tepat satu kali

### Timeout mempertahankan form
31. Tampilkan Dialog Edit Purchase dengan kondisi K4
32. Isi Document No. `INV-2026-0302`
33. Klik `[Save]`
34. Verifikasi toast `Connection problem. Please try again.` tampil
35. Verifikasi dialog `Edit Purchase` tetap terbuka dengan Document No. `INV-2026-0302` dan `[Save]` aktif kembali

### Clear Field mengosongkan semua field tanpa prompt
36. Tampilkan Dialog Edit Purchase dengan kondisi K1
37. Klik `[Clear Field]`
38. Verifikasi field Purchase Date, Purchase Cost, dan Document No. kosong, bukan kembali ke nilai tersimpan
39. Verifikasi dialog `Edit Purchase` tetap terbuka dan dialog `Unsaved Changes` tidak tampil

### Menutup form bersih
40. Tampilkan Dialog Edit Purchase dengan kondisi K1
41. Klik `✕` pada dialog
42. Verifikasi dialog `Edit Purchase` tertutup tanpa dialog `Unsaved Changes`
43. Verifikasi tidak ada toast yang tampil
44. Tampilkan Dialog Edit Purchase dengan kondisi K1
45. Tekan Esc
46. Verifikasi dialog `Edit Purchase` tertutup tanpa dialog `Unsaved Changes`
47. Verifikasi fokus kembali ke pemicu dialog
48. Tampilkan Dialog Edit Purchase dengan kondisi K1
49. Isi Document No. `INV-2026-0302`
50. Isi Document No. `INV-2026-0301`
51. Klik `✕` pada dialog
52. Verifikasi dialog `Edit Purchase` tertutup tanpa dialog `Unsaved Changes` karena nilai kembali identik dengan nilai awal

### Menutup form kotor meminta konfirmasi
53. Tampilkan Dialog Edit Purchase dengan kondisi K1
54. Isi Document No. `INV-2026-0302`
55. Klik `✕` pada dialog
56. Verifikasi dialog `Unsaved Changes` dengan pesan `You have unsaved changes. Are you sure you want to leave?`, tombol `[Leave]`, dan tombol `[Cancel]` tampil
57. Tekan Esc
58. Verifikasi dialog `Unsaved Changes` tertutup dan dialog `Edit Purchase` tetap terbuka dengan Document No. `INV-2026-0302`
59. Verifikasi tidak ada toast yang tampil
60. Klik area backdrop di luar dialog `Edit Purchase`
61. Verifikasi dialog `Edit Purchase` tetap terbuka dengan Document No. `INV-2026-0302` dan dialog `Unsaved Changes` tidak tampil
62. Verifikasi tidak ada toast yang tampil
63. Klik `✕` pada dialog
64. Klik `[Cancel]` pada dialog `Unsaved Changes`
65. Verifikasi dialog `Edit Purchase` tetap terbuka dengan Document No. `INV-2026-0302`
66. Verifikasi tidak ada toast yang tampil
67. Tekan Esc
68. Verifikasi dialog `Unsaved Changes` dengan pesan `You have unsaved changes. Are you sure you want to leave?`, tombol `[Leave]`, dan tombol `[Cancel]` tampil
69. Klik `[Leave]` pada dialog `Unsaved Changes`
70. Verifikasi dialog `Edit Purchase` tertutup
71. Verifikasi tidak ada toast yang tampil

### Aksesibilitas form
72. Tampilkan Dialog Edit Purchase dengan kondisi K6
73. Verifikasi fokus berada di dalam dialog `Edit Purchase`
74. Verifikasi field `Contract number` diumumkan sebagai wajib
75. Verifikasi tombol tutup `✕` memiliki nama aksesibel
76. Isi Document No. `INV-2026-0302`
77. Klik `[Save]`
78. Verifikasi pesan `Contract number must not be empty` tampil dan terkait sebagai deskripsi field `Contract number`
79. Tekan Tab berulang sampai fokus berpindah melewati kontrol terakhir dialog
80. Verifikasi fokus tetap berada di dalam dialog `Edit Purchase`

### Penolakan server karena aset berjejak Posted
81. Tampilkan Dialog Edit Purchase dengan kondisi K7
82. Isi Document No. `INV-2026-0302`
83. Klik `[Save]`
84. Verifikasi alert inline `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.` tampil di dalam dialog
85. Verifikasi dialog `Edit Purchase` tetap terbuka dengan Document No. `INV-2026-0302`

### Timeout pada Bulk mempertahankan dialog dan seleksi
86. Tampilkan Dialog Edit Purchase dengan kondisi K8
87. Isi `Purchase Cost (per asset)` `19.000.000,00`
88. Klik `[Save]`
89. Verifikasi toast `Connection problem. Please try again.` tampil setelah `[Save]` pada Bulk
90. Verifikasi dialog `Edit Purchase` tetap terbuka dengan teks `2 assets selected`, bullet `Laptop Pro 16 - 1` dan `Laptop Pro 16 - 2`, `Purchase Cost (per asset)` `19.000.000,00`, dan `[Save]` aktif kembali
