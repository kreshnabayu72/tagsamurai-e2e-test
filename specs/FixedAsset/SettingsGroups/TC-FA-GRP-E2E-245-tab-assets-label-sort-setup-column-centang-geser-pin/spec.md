---
id: TC-FA-GRP-E2E-245-tab-assets-label-sort-setup-column-centang-geser-pin
title: "Tab Assets Label: Sort Kolom +N more dan Setup Column (Centang, Geser, Pin)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1178
  - TC-FA-GRP-1179
  - TC-FA-GRP-1180
  - TC-FA-GRP-1181
coverage:
  web: automated
---

# Tab Assets Label: Sort Kolom +N more dan Setup Column (Centang, Geser, Pin)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Multi Label Node (Pre-setup tambahan, Tabel Dinamis No 9, level 1) berisi hanya aset L1 (Finance, Fragile, Priority), L2 (Fragile, Priority), L3 (Priority), L4 (tanpa label), L5 (Finance); status aset bervariasi. Warehouse A (Tabel A, Assignable) berisi 24 aset aktif variasi Brand, Model/Type, Category, Label, dan status. Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Lebar viewport diatur supaya tabel Tab Assets dapat di-scroll horizontal (dipakai asersi pin/scroll horizontal); hook `after` memulihkan viewport (S-03).

## Test Steps

### TC-FA-GRP-1178: Sort Tab Assets by kolom Label (+N more)

1. Ketik Search `Multi Label Node`, tekan Enter
2. Buka Detail Multi Label Node (Tab Assets)
3. Buka Popup Setup Column
4. Centang Label
5. Klik [Save]
6. Klik header Label 1×
7. Verifikasi urutan Ascending (jumlah label paling sedikit dulu): L4, L5, L3, L2, L1 (L5 sebelum L3: jumlah sama, label pertama `Finance` < `Priority`)
8. Klik header Label 2×
9. Verifikasi urutan Descending (jumlah label paling banyak dulu): L1, L2, L3, L5, L4 (L3 sebelum L5: jumlah sama, tiebreaker label pertama Z→A)
10. Verifikasi badge di dalam sel tetap urut A–Z
11. Klik header Label 3×
12. Verifikasi urutan kembali ke default tabel (Name A→Z)
13. Tutup Popup Detail Group

### TC-FA-GRP-1179: Setup Column Tab Assets, centang kolom curated Label

14. Kosongkan Search dengan klik `✕`, lalu ketik Search `Warehouse A`, tekan Enter
15. Buka Detail Warehouse A (Tab Assets)
16. Buka Popup Setup Column
17. Uncheck Label
18. Klik [Save]
19. Buka Popup Setup Column
20. Centang Label
21. Verifikasi Live Preview langsung menampilkan kolom Label
22. Klik [Save]
23. Verifikasi kolom Label tampil di tabel
24. Refresh F5
25. Ketik Search `Warehouse A`, tekan Enter
26. Buka Detail Warehouse A (Tab Assets)
27. Verifikasi konfigurasi bertahan setelah F5: kolom Label tampil di tabel

### TC-FA-GRP-1180: Setup Column Tab Assets, geser (drag) kolom Label

28. Buka Popup Setup Column
29. Uncheck Label
30. Klik [Save]
31. Buka Popup Setup Column
32. Centang Label
33. Drag Label ke posisi setelah Brand
34. Verifikasi urutan Live Preview mengikuti posisi baru
35. Klik [Save]
36. Verifikasi urutan kolom tabel berubah mengikuti posisi baru
37. Refresh F5
38. Ketik Search `Warehouse A`, tekan Enter
39. Buka Detail Warehouse A (Tab Assets)
40. Verifikasi urutan kolom tabel bertahan setelah F5

### TC-FA-GRP-1181: Setup Column Tab Assets, pin kolom Label

41. Buka Popup Setup Column
42. Uncheck Label
43. Klik [Save]
44. Buka Popup Setup Column
45. Centang Label
46. Klik icon Pin Label
47. Klik [Save]
48. Atur lebar viewport supaya tabel Tab Assets dapat di-scroll horizontal
49. Scroll tabel horizontal
50. Verifikasi kolom Label membeku (sticky) saat scroll horizontal
51. Refresh F5
52. Ketik Search `Warehouse A`, tekan Enter
53. Buka Detail Warehouse A (Tab Assets)
54. Scroll tabel horizontal
55. Verifikasi pin kolom Label bertahan setelah F5
56. Buka Popup Setup Column
57. Klik icon Pin Label untuk unpin
58. Klik [Save]
59. Scroll tabel horizontal
60. Verifikasi kolom Label kembali ikut scroll

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): menutup Popup Detail Group; mengembalikan kolom Label ke unchecked lewat Setup Column (Uncheck Label, [Save]) sebelum TC-1179, TC-1180, dan TC-1181 supaya tiap TC mulai dari Label unchecked; membuka ulang Detail Warehouse A sesudah Refresh F5; scroll horizontal ulang sesudah F5. TC-1178 diletakkan pertama karena memakai Multi Label Node, lalu blok Warehouse A.
- Spec ini 60 langkah, di atas smell 35 langkah: satu kelas (fungsional Setup Column dan Sort Tab Assets), tiap blok TC berdiri sendiri (mulai dari state kolom yang dipulihkan di antara blok), dan kegagalan satu blok tidak menghilangkan makna blok lain; langkah dominan berupa Verifikasi per klausa dan pemulihan kolom.
- Langkah penghubung (S-03): "Atur lebar viewport ..." sebelum scroll horizontal pertama supaya tabel dapat di-scroll horizontal (asersi pin sticky); hook `after` memulihkan viewport.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA (S-15): (1) TC-1178 membutuhkan kolom Label tampil (precondition d) tetapi langkah TC tidak memuat pencentangan; spec menambah langkah penghubung Setup Column. (2) TC tidak menyatakan apakah konfigurasi Setup Column berlaku lintas group; spec mengasumsikan per akun. (3) TC-1180 "drag Label ke posisi lain" tidak menyebut posisi; spec memakai setelah Brand. (4) TC tidak menyatakan apakah Popup Detail Group tetap terbuka sesudah F5; spec membuka ulang. (5) TC-1181 tidak menyebut langkah buka Popup Setup Column untuk unpin; ditambahkan.
