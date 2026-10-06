---
id: TC-GS-POS-E2E-024-bulk-delete-campuran-dan-terblokir
title: Bulk Delete campuran, seluruhnya terblokir, dan collapse ke dialog blokir
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-27
  - TC-GS-POS-28
  - TC-GS-POS-244
coverage:
  web: automated
---

# Bulk Delete campuran, seluruhnya terblokir, dan collapse ke dialog blokir

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`, yaitu Role Total Control yang
  memegang capability Manage user and role dengan huruf C, U, dan D. Kolom checkbox dan Bulk Action Bar
  hanya tampil bagi role yang memegang capability Delete.
- `Fixture.globalSettingsPosition.bulkDelete.mixedSafeTarget` adalah Position bebas relasi untuk
  campuran, yaitu `Sales Representative`.
- `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` adalah Position
  `HR Business Partner` yang sudah direferensikan user bawaan `Rina Wijaya`.
- `Fixture.globalSettingsPosition.positions.seed.financeManager` adalah Position
  `Finance Manager` yang sudah direferensikan user bawaan `Budi Santoso`. Seed kedua ini diperlukan
  karena skenario seluruhnya terblokir butuh minimal dua Position yang sedang dipakai.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.title` adalah title Dialog 3, yaitu
  `Delete Positions`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.groupWillDelete` adalah heading kelompok
  yang akan dihapus, yaitu `The following will be deleted:`
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.groupWillSkip` adalah heading kelompok
  yang akan dilewati, yaitu `The following are still in use and will be skipped:`
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.bodyQuestion` adalah kalimat penutup
  Dialog 3, yaitu `Are you sure you want to continue? This action cannot be undone.`
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.actions.cancel` adalah tombol batal,
  yaitu `Cancel`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.actions.continue` adalah tombol
  konfirmasi, yaitu `Continue`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeletePartialSkipped` adalah toast untuk Delete
  yang sebagian berhasil, yaitu `Success, position has been deleted. Some items were skipped (still
  in use).`
- `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title` adalah title Dialog 2, yaitu
  `Cannot Delete Data`.
- `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.body` adalah kalimat penutup Dialog 2,
  yaitu `These positions are still in use. Remove the references before deleting.`
- `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok` adalah tombol tunggal Dialog 2,
  yaitu `OK`.
- PRD §4.2d menetapkan Dialog 2 sebagai satu dialog untuk row-action single maupun bulk yang seluruhnya
  terblokir, dan pembedanya hanya jumlah bullet. PRD juga melarang memakai Dialog 3 dengan kelompok
  `will be deleted` kosong untuk kasus seluruhnya terblokir.
- Dialog 3 memakai kata `continue?` sebagai kalimat penutup dan tombol `Continue`, sedangkan Dialog 4
  memakai kata `them` dan tombol `Delete`. Perbedaan itu yang membuat dua dialog homogen dan campuran
  tidak tertukar.
- Konvensi platform menetapkan bahwa kondisi seluruh item terblokir adalah validasi pre-flight. Tidak
  ada request yang dikirim, tidak ada state yang berubah, dan seleksi tidak di-reset supaya user bisa
  membaca pesan error lalu menyesuaikan pilihannya.
- Jumlah entri log pada tiga surface dihitung di awal setiap subbagian supaya item yang di-skip tidak
  tertukar dengan item yang dihapus.

## Test Steps

### Bulk Delete campuran, sebagian aman dan sebagian terblokir

1. Verifikasi tabel memuat `Fixture.globalSettingsPosition.bulkDelete.mixedSafeTarget`
2. Verifikasi tabel memuat `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
3. Verifikasi `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` sedang direferensikan
   user, sehingga memang masuk kelompok yang dilewati
4. Catat jumlah entri log pada tiga surface sebelum subbagian ini
5. Centang checkbox pada baris
   `Fixture.globalSettingsPosition.bulkDelete.mixedSafeTarget`
6. Centang checkbox pada baris
   `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
7. Verifikasi counter pada bar menunjukkan jumlah dua
8. Klik tombol aksi massa pada bar
9. Verifikasi dialog yang tampil adalah Dialog 3 dengan title
   `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.title`
10. Verifikasi dialog memuat kelompok
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.groupWillDelete`
11. Verifikasi kelompok tersebut memuat satu bullet untuk
    `Fixture.globalSettingsPosition.bulkDelete.mixedSafeTarget`
12. Verifikasi dialog memuat kelompok
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.groupWillSkip`
13. Verifikasi kelompok tersebut memuat satu bullet untuk
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
14. Verifikasi kedua kelompok tampil berurutan, yaitu kelompok yang akan dihapus lebih dulu
15. Verifikasi urutan di dalam dialog mengikuti urutan seleksi, bukan urutan alfabet
16. Verifikasi body dialog memuat kalimat
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.bodyQuestion`
17. Verifikasi kalimat penutup memakai kata `continue`, bukan `delete them`
18. Verifikasi tombol konfirmasi berlabel
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.actions.continue`, yaitu
    `Continue`, bukan `Delete`
19. Verifikasi dialog tidak memuat bullet untuk item lain di luar dua item terpilih
20. Verifikasi kedua kelompok nama ditampilkan penuh di dalam container yang bisa digulir
21. Klik tombol `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.actions.continue`
22. Verifikasi toast
    `Fixture.globalSettingsPosition.captions.modal.bulkDeletePartialSkipped` muncul
23. Verifikasi toast itu menyebutkan ada item yang dilewati karena masih dipakai
24. Verifikasi dialog tertutup
25. Verifikasi baris
    `Fixture.globalSettingsPosition.bulkDelete.mixedSafeTarget` tidak lagi ada di tabel
26. Verifikasi baris
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` tetap ada di tabel
27. Verifikasi jumlah total Position berkurang satu, bukan dua
28. Verifikasi Bulk Action Bar langsung hilang setelah aksi ter-commit
29. Verifikasi seluruh checkbox baris kembali unchecked, termasuk baris yang di-skip
30. Verifikasi jumlah entri log Changelog bertambah satu entri untuk
    `Fixture.globalSettingsPosition.bulkDelete.mixedSafeTarget`
31. Verifikasi tidak ada entri log Delete untuk
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`, karena item yang dilewati tidak
    dicatat sebagai mutasi
32. Verifikasi jumlah entri log Activity Log bertambah satu
33. Verifikasi jumlah entri System Log bertambah satu
34. Muat ulang halaman
35. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.mixedSafeTarget` tetap tidak ada
36. Verifikasi `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` tetap ada

### Bulk Delete dengan seluruh item terpilih sedang dipakai

37. Verifikasi tabel memuat `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
38. Verifikasi tabel memuat `Fixture.globalSettingsPosition.positions.seed.financeManager`
39. Verifikasi kedua Position tersebut sedang direferensikan user
40. Catat jumlah entri log pada tiga surface sebelum subbagian ini
41. Centang checkbox pada baris
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
42. Centang checkbox pada baris
    `Fixture.globalSettingsPosition.positions.seed.financeManager`
43. Verifikasi counter pada bar menunjukkan jumlah dua
44. Klik tombol aksi massa pada bar
45. Verifikasi dialog yang langsung tampil adalah Dialog 2 dengan title
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title`
46. Verifikasi dialog blokir muncul tanpa dialog konfirmasi sebelumnya, sehingga user tidak sempat
    menekan tombol konfirmasi apa pun
47. Verifikasi dialog memuat satu bullet untuk
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
48. Verifikasi dialog memuat satu bullet untuk
    `Fixture.globalSettingsPosition.positions.seed.financeManager`
49. Verifikasi setiap bullet ditandai masih dipakai
50. Verifikasi dialog memuat kalimat
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.body`
51. Verifikasi dialog tidak memuat kelompok
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.groupWillDelete`, karena memakai
    kelompok kosong akan menyesatkan user
52. Verifikasi dialog tidak memuat kelompok
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.groupWillSkip`
53. Verifikasi dialog hanya punya satu tombol, yaitu
    `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok`
54. Verifikasi dialog tidak punya tombol `Cancel` maupun `Continue`
55. Verifikasi tidak ada toast yang muncul saat dialog tampil
56. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok`
57. Verifikasi dialog tertutup
58. Verifikasi tidak ada toast sukses yang muncul
59. Verifikasi kedua Position tersebut tetap ada di tabel
60. Verifikasi jumlah total Position tidak berubah
61. Verifikasi jumlah entri log pada tiga surface tidak bertambah
62. Verifikasi Bulk Action Bar masih tampil dengan seleksi yang sama
63. Verifikasi counter pada bar masih menampilkan jumlah dua, karena blokir terjadi sebelum request dan
    seleksi tidak boleh di-reset
64. Kosongkan checkbox pada baris
    `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
65. Verifikasi counter berkurang menjadi satu
66. Verifikasi user bisa melanjutkan dengan sisa seleksi tanpa harus mencentang ulang dari awal

### Bulk Action Bar dengan satu item terblokir collapse ke dialog blokir single

67. Verifikasi baris `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` ada di tabel
68. Verifikasi baris tersebut sedang direferensikan user
69. Centang checkbox pada baris
   `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner` saja
70. Verifikasi Bulk Action Bar muncul
71. Verifikasi counter pada bar memakai bentuk singular untuk satu baris terpilih
72. Klik tombol aksi massa pada bar
73. Verifikasi dialog yang tampil adalah Dialog 2 dengan title
   `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title`
74. Verifikasi dialog memuat tepat satu bullet untuk
   `Fixture.globalSettingsPosition.positions.seed.hrBusinessPartner`
75. Verifikasi dialog tidak memuat bullet untuk item lain, karena tidak ada item lain yang terpilih
76. Verifikasi dialog tidak memakai framing dua kelompok milik Dialog 3, yaitu tidak ada heading
   `The following will be deleted:` maupun
   `The following are still in use and will be skipped:`
77. Verifikasi dialog yang tampil identik dengan dialog hasil klik opsi `Delete` pada row action untuk
   Position yang sama
78. Verifikasi dialog hanya punya satu tombol `OK`
79. Klik tombol `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.actions.ok`
80. Verifikasi dialog tertutup
81. Verifikasi baris tersebut tetap ada di tabel
82. Verifikasi jumlah entri log tidak bertambah

## Notes

- Spec ini adalah pasangan spec 023. Spec 023 menguji Dialog 4 dan Dialog 1, sedangkan spec ini
  menguji Dialog 3 dan Dialog 2 untuk jalur bulk.
- Yang membedakan Dialog 2 dan Dialog 3 bukan judulnya, melainkan ada tidaknya dua kelompok. Dialog 2
  untuk kasus seluruhnya terblokir tidak boleh memakai kelompok kosong, karena itu akan memberi
  kesan ada yang akan dihapus padahal tidak ada.
- Langkah 15 memeriksa urutan bullet mengikuti urutan seleksi. Urutan alfabet tidak disebutkan di PRD,
  sehingga spec ini hanya memeriksa bahwa urutan yang tampil konsisten dengan urutan pilihan user.
- Langkah 18 memeriksa tombol `Continue` pada Dialog 3 dan bukan `Delete`. Tombol `Delete` milik
  Dialog 4, dan pemakaiannya di Dialog 3 membuat user mengira tidak ada yang dilewati.
- Langkah 30 dan 31 memeriksa logging per item yang benar-benar terhapus. Item yang dilewati bukan
  mutasi, jadi tidak boleh punya entri Delete. Kesalahan di sini membuat audit trail berisi entri
  untuk operasi yang tidak pernah terjadi.
- Konvensi platform dengan sengaja tidak mereset seleksi pada kondisi seluruh item terblokir, supaya
  user bisa mengosongkan satu centang dan mencoba lagi. Langkah 62 sampai 66 menguji aturan itu dari
  sisi yang paling jarang dipakai, yaitu langsung melanjutkan tanpa centang ulang.
- Subbagian ketiga menguji collapse pada Dialog 2, bukan Dialog 1. Kalau sistem salah memilih dialog
  berdasarkan jumlah item terpilih saja tanpa memeriksa status in-use, kasus ini akan salah menampilkan
  Dialog 1 dan user akan menekan tombol Delete untuk data yang sedang dipakai.
- Kedua seed yang dipakai di subbagian kedua memang harus dipakai user, dan relasi itu dibuat permanen
  oleh tim FE. Spec ini tidak pernah melepas relasi itu, supaya spec 007 dan spec 023 yang juga memakai
  `HR Business Partner` tetap punya prasyarat yang sama.
