---
id: TC-GS-UCF-E2E-027-master-data-count-limit-create
title: "Master Data Count Limit: [+ Custom Field] Diblokir saat Limit Tercapai, Create di Batas, Edit di Batas, Slot Dibebaskan Delete, Limit Dibaca Dinamis, dan Limit Diturunkan di Bawah Jumlah Field"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-87
  - TC-GS-UCF-364
  - TC-GS-UCF-453
  - TC-GS-UCF-302
  - TC-GS-UCF-435
  - TC-GS-UCF-88
  - TC-GS-UCF-464
  - TC-GS-UCF-90
coverage:
  web: automated
---

# Master Data Count Limit: [+ Custom Field] Diblokir saat Limit Tercapai, Create di Batas, Edit di Batas, Slot Dibebaskan Delete, Limit Dibaca Dinamis, dan Limit Diturunkan di Bawah Jumlah Field

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`): spec mengubah state global Master Data Count Limit dan volume Custom Field entitas Client Limit. Nilai awal limit dan volume dicatat di hook `before` dan dipulihkan di hook `after`.
- Akun (password hanya lewat env var, tidak ditulis di spec atau fixture):
  - Akun aktor (login di hook `before`): Total Control Client Limit (Wulan Sari) `totalControl_automated_qaTeam4@qwertysystem.net` (Pre-setup), `Spectra.env.GS_LIMIT_TC_PASSWORD`. Master Data Count Limit 1.000, Selection Limit 100.
  - Pemicu perubahan limit: Total Control (Principal) Hendra Wijaya `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`; mengubah System Limits Client Limit pada TC-GS-UCF-302 dan 435 sebagai pemicu state saja (P-2), lewat mekanisme yang disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD modul ini).
  - Hook `after` mengembalikan sesi ke akun default suite.
- Layar awal Global Settings > User > Custom Field (Client Limit) dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup Client Limit (fixture backend): Custom Field `Lim 001` sampai `Lim 999` bertipe Text (kecuali `Lim 010` bertipe Dropdown dan `Lim 500` untuk spec 028). Volume dan limit tiap blok diatur backend sebelum blok itu ("disediakan tim BE"; TC menyatakan "volume diatur backend sebelum TC" dan TC tidak mengandalkan sisa volume TC sebelumnya):
  - TC-GS-UCF-87, 364, 453: limit 1.000, tepat 1.000 Custom Field; untuk TC-GS-UCF-453 `Lim 010` bertipe Dropdown dan field lain bertipe Text.
  - TC-GS-UCF-302: limit 1.000, tepat 1.000 field; lalu limit dinaikkan 1.100 oleh Principal dan backend mengatur jumlah menjadi tepat 1.100 field.
  - TC-GS-UCF-435: limit 1.100, tepat 1.050 Custom Field; lalu limit diturunkan Principal menjadi 1.000.
  - TC-GS-UCF-88: limit 1.000, tepat 999 Custom Field.
  - TC-GS-UCF-464: limit 1.000, tepat 1.000 Custom Field (limit tercapai); `Lim 002` menjadi target Edit Placeholder.
  - TC-GS-UCF-90: limit 1.000, tepat 1.000 Custom Field (limit tercapai).
- Data Dinamis milik spec (nama bersuffix `{runId}-027`; fixture baru `Fixture.customFieldUser.limit027`; Text, Active, Required No): `Limit Raise {runId}-027` (TC-GS-UCF-302), `Limit 1000 {runId}-027` dan `Limit 1001 {runId}-027` (TC-GS-UCF-88; `Limit 1001 {runId}-027` tidak tersimpan), `Slot Free {runId}-027` (TC-GS-UCF-90).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API Custom Field bersuffix `{runId}-027` yang masih ada; kembalikan Master Data Count Limit Client Limit ke 1.000 dan volume ke nilai awal (dikembalikan Principal dan backend); pulihkan `Lim 001` bila terhapus oleh TC-GS-UCF-90 dan Placeholder `Lim 002` ke nilai awal bila diubah oleh TC-GS-UCF-464 (disediakan tim BE).
- Kemampuan teknis: membaca total jumlah Custom Field entitas Client Limit (dari total record tabel atau respons list; kemampuan disediakan tim FE/BE); ukuran halaman 100 dan navigasi ke halaman 11 pada tabel.
- State global yang diubah: Master Data Count Limit dan volume Custom Field Client Limit (dipulihkan seperti di atas); flag Guided Tooltip dikelola hook suite.

## Test Steps

### TC-GS-UCF-87: Klik [+ Custom Field] saat Master Data Count Limit tercapai

1. Atur backend: limit 1.000 dan tepat 1.000 Custom Field
2. Muat ulang halaman (F5)
3. Verifikasi `[+ Custom Field]` tampil
4. Verifikasi `[+ Custom Field]` enabled
5. Klik `[+ Custom Field]`
6. Verifikasi dialog `Limit Reached` (warning) dengan body `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.` dan tombol `[OK]` saja tanpa CTA upgrade
7. Verifikasi dialog muncul segera saat klik tanpa langkah tambahan
8. Klik `[OK]`
9. Verifikasi dialog tertutup
10. Verifikasi form `New Custom Field` tidak terbuka

### TC-GS-UCF-364: Klik [+ Custom Field] dengan Search aktif saat Master Data Count Limit tercapai tetap menampilkan dialog limit

11. Verifikasi tabel menampilkan sedikitnya satu baris sebelum Search
12. Ketik Search `Lim 002`, tekan Enter
13. Verifikasi List hanya menampilkan baris `Lim 002` (jauh di bawah 1.000 baris)
14. Klik `[+ Custom Field]`
15. Verifikasi dialog `Limit Reached` (warning) dengan body `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.` dan tombol `[OK]` saja
16. Verifikasi dialog tampil walau hasil Search kurang dari batas
17. Klik `[OK]`
18. Verifikasi dialog tertutup
19. Verifikasi form `New Custom Field` tidak terbuka
20. Verifikasi Search `Lim 002` tetap aktif
21. Klik `(←)` pada kotak Search

### TC-GS-UCF-453: Klik [+ Custom Field] dengan Filter aktif saat Master Data Count Limit tercapai tetap menampilkan dialog limit

22. Verifikasi tabel menampilkan sedikitnya satu baris sebelum Filter
23. Klik Filter, pilih Data Type `Dropdown`, klik `[Apply]`
24. Verifikasi List hanya menampilkan `Lim 010` (jauh di bawah 1.000 baris)
25. Klik `[+ Custom Field]`
26. Verifikasi dialog `Limit Reached` (warning) dengan body `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.` dan tombol `[OK]` saja tanpa CTA upgrade
27. Verifikasi dialog tampil walau hasil Filter kurang dari batas
28. Klik `[OK]`
29. Verifikasi dialog tertutup
30. Verifikasi form `New Custom Field` tidak terbuka
31. Verifikasi Filter Data Type `Dropdown` tetap aktif
32. Hapus chip filter Data Type `Dropdown`

### TC-GS-UCF-302: Master Data Count Limit dibaca dari System Limits tanpa hardcode

33. Klik `[+ Custom Field]`
34. Verifikasi dialog `Limit Reached` memuat `{limit}` = `1000` (`You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.`)
35. Klik `[OK]`
36. Principal menaikkan Master Data Count Limit Client Limit menjadi 1.100
37. Muat ulang halaman (F5)
38. Klik `[+ Custom Field]`
39. Verifikasi form `New Custom Field` terbuka
40. Isi Field Name `Limit Raise {runId}-027`, Data Type `Text`, klik `[Submit]`
41. Verifikasi toast sukses: "Success, custom field has been created."
42. Atur backend: jumlah menjadi tepat 1.100 Custom Field
43. Klik `[+ Custom Field]`
44. Verifikasi dialog `Limit Reached` memuat `{limit}` = `1100` (`You've reached the platform limit of 1100 custom fields. Contact support if you need a higher limit.`)
45. Klik `[OK]`

### TC-GS-UCF-435: Master Data Count Limit diturunkan di bawah jumlah field, data tetap ada dan Create ditolak

46. Atur backend: limit 1.100 dan tepat 1.050 Custom Field
47. Principal menurunkan Master Data Count Limit Client Limit menjadi 1.000
48. Muat ulang tab Custom Field, ubah page size menjadi 100, pindah ke halaman 11
49. Verifikasi halaman 11 memuat 50 baris (1.050 Custom Field tidak terhapus oleh penurunan limit)
50. Klik `[+ Custom Field]`
51. Verifikasi dialog `Limit Reached` (warning) dengan body `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.` dan tombol `[OK]` saja
52. Klik `[OK]`
53. Verifikasi dialog tertutup
54. Verifikasi form `New Custom Field` tidak terbuka

### TC-GS-UCF-88: Create ke-N di batas berhasil lalu ke-(N+1) ditolak dengan Stay on form

55. Atur backend: limit 1.000 dan tepat 999 Custom Field
56. Muat ulang halaman (F5)
57. Klik `[+ Custom Field]`
58. Centang `Stay on this form after submitting`
59. Isi Field Name `Limit 1000 {runId}-027`, Data Type `Text`, klik `[Submit]`
60. Verifikasi toast sukses: "Success, custom field has been created."
61. Verifikasi popup tetap terbuka
62. Isi Field Name `Limit 1001 {runId}-027`, Data Type `Text`, klik `[Submit]`
63. Verifikasi dialog `Limit Reached` (warning) dengan body `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.` dan tombol `[OK]` saja tanpa CTA upgrade
64. Klik `[OK]`
65. Verifikasi popup tetap terbuka
66. Verifikasi Field Name `Limit 1001 {runId}-027` dipertahankan
67. Klik `[✕]`
68. Verifikasi dialog `Unsaved Changes` tampil
69. Klik `[Leave]`
70. Ketik Search `{runId}-027`, tekan Enter
71. Verifikasi baris `Limit 1000 {runId}-027` tampil di tabel
72. Verifikasi `Limit 1001 {runId}-027` tidak dibuat (tidak ada di tabel)
73. Klik `(←)` pada kotak Search

### TC-GS-UCF-464: Edit field tidak memicu dialog limit saat Master Data Count Limit tercapai

74. Atur backend: limit 1.000 dan tepat 1.000 Custom Field
75. Muat ulang halaman (F5)
76. Ketik Search `Lim 002`, tekan Enter
77. Klik `⋯` pada baris `Lim 002`, pilih `Edit`
78. Ubah Placeholder menjadi `At limit`
79. Klik `[Save]`
80. Verifikasi tidak ada dialog `Limit Reached`
81. Verifikasi toast sukses: "Success, custom field has been updated."
82. Verifikasi kolom Placeholder baris `Lim 002` menampilkan `At limit`
83. Klik `(←)` pada kotak Search

### TC-GS-UCF-90: Menghapus satu field membebaskan slot sehingga Create berhasil lagi

84. Atur backend: limit 1.000 dan tepat 1.000 Custom Field
85. Muat ulang halaman (F5)
86. Ketik Search `Lim 001`, tekan Enter
87. Klik `⋯` pada baris `Lim 001`, pilih `Delete`, klik `[Delete]`
88. Verifikasi toast sukses: "Success, custom field has been deleted."
89. Klik `(←)` pada kotak Search
90. Klik `[+ Custom Field]`
91. Isi Field Name `Slot Free {runId}-027`, Data Type `Text`, klik `[Submit]`
92. Verifikasi toast sukses: "Success, custom field has been created."
93. Verifikasi jumlah total Custom Field kembali 1.000

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Kelas: volume data (kelas e, bagian 3 prinsip 13e; volume 999 sampai 1.100 field, ambang 100 baris), dengan pemicu perubahan limit oleh Principal (P-2). Volume 999 sampai 1.100 field dibangun backend.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 93 langkah (di atas smell sekitar 35 langkah): seluruhnya satu kelas (Master Data Count Limit pada Create dan Edit), satu akun aktor (Total Control Client Limit), dan tiap blok mengatur limit dan volume sendiri di awal blok ("Atur backend ..."), sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Urutan TC: blok baca saja pada limit tercapai (TC-GS-UCF-87, 364, 453), perubahan limit (TC-GS-UCF-302, 435), Create di batas (TC-GS-UCF-88), Edit di batas (TC-GS-UCF-464), dan Delete paling akhir (TC-GS-UCF-90, prinsip 5). Urutan berbeda dari TC sumber (87, 88, 90, 364, 453, 435, 302, 464) karena tiap blok mengatur ulang volume dan Delete menghabisi data.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Atur backend ..." (pengaturan limit dan volume oleh tim BE), muat ulang halaman (F5), Search `Lim 002`, `Lim 001`, `{runId}-027` serta `(←)` yang menutup Search, menghapus chip filter, dan langkah Principal (pemicu state, P-2). Tidak ada asersi atas tampilan sesi Principal.
- Dialog `Limit Reached` ditulis dengan nilai `{limit}` tersubstitusi (`1000` atau `1100`, angka polos tanpa pemisah ribuan) sesuai Expected TC.
- Pada TC-GS-UCF-88 `Limit 1001 {runId}-027` tidak tersimpan: absence baris `Limit 1001` memakai anchor positif baris `Limit 1000 {runId}-027` pada Search yang sama (butir 2 konvensi 8b).
- Pembagian TC lintas spec: TC-GS-UCF-454 (field Inactive ikut terhitung di batas) ada di spec 028; TC-GS-UCF-89 (dua admin berebut slot terakhir) ada di spec 029.
- Temuan untuk QA:
  - TC-GS-UCF-87, 88, 90, 364, 453, 435, 302: volume 999, 1.000, 1.050, dan 1.100 field serta Master Data Count Limit diatur backend dan Principal; TC dan PRD tidak menyebut mekanismenya sehingga ditulis "disediakan tim BE" dan "disediakan tim FE/BE" (S-13). Akun Principal pemicu (Hendra Wijaya) tertulis di Pre-setup TC.
  - TC-GS-UCF-302: Post Condition "Master Data Count Limit Client Limit dikembalikan Principal ke 1.000" tanpa langkah observasi; tidak diasersi dan dipulihkan di hook `after`. Langkah 4 TC mengatur jumlah tepat 1.100 sesudah Create `Limit Raise`; spec menuliskannya sebagai langkah "Atur backend".
  - TC-GS-UCF-435: Post Condition "Master Data Count Limit Client Limit dan volume dikembalikan backend" tanpa langkah observasi; tidak diasersi.
  - TC-GS-UCF-90: Expected c "Jumlah field kembali 1.000" membutuhkan pembacaan total record; kemampuannya disediakan tim FE/BE. TC memakai `Lim 001` (fixture backend) sebagai target Delete; spec menghapusnya karena TC mendefinisikan aksi itu dan memulihkannya di hook `after`.
  - TC-GS-UCF-87, 88, 364, 453: keputusan NC-20 (respons List membawa ceiling; dialog `Limit Reached` tampil saat klik `[+ Custom Field]`) berbeda dari API/LLD, yang hanya mengembalikan ceiling pada `409` saat Submit; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan.
  - TC-GS-UCF-453: Data Uji `Lim 010` bertipe Dropdown diatur backend sebelum TC.
  - TC-GS-UCF-464 mengubah `Lim 002` (fixture backend Client Limit); Placeholder awalnya dipulihkan hook `after`, mekanisme pemulihan dan pengaturan volume 1.000 field tidak didefinisikan di TC sehingga disediakan tim BE.
