---
id: TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama
title: "Overlay Column Visibility dan Modal Setup Column Tabel Custom Field: Screening, Hide, Reorder, Pin, Reset, Penutupan, dan Independensi dari Modal Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-235
  - TC-GS-UCF-236
  - TC-GS-UCF-237
  - TC-GS-UCF-238
  - TC-GS-UCF-508
  - TC-GS-UCF-239
  - TC-GS-UCF-240
  - TC-GS-UCF-509
  - TC-GS-UCF-241
  - TC-GS-UCF-242
  - TC-GS-UCF-243
coverage:
  web: automated
---

# Overlay Column Visibility dan Modal Setup Column Tabel Custom Field: Screening, Hide, Reorder, Pin, Reset, Penutupan, dan Independensi dari Modal Changelog

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.preset14`): 6 Custom Field `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, dan `Joining Date`; dipakai sebagai precondition TC (total 14 field), tidak diasersi.
- Data Dinamis Population D-01 (8 field; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.population`): `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`; Active; Modified By `Sari D`. Di-seed lewat API oleh akun Total Control Client A di hook `before` (mekanisme disediakan tim FE/BE, endpoint tidak ditulis di spec); dipakai sebagai precondition TC (total 14 field), tidak diasersi. Nama literal tanpa suffix (pengecualian Population, S-12); seeding idempotent (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat hook spec ini. Seeding mencatat entri Create pada Modal Changelog sehingga tabel Changelog berisi baris untuk TC-GS-UCF-243.
- Setup Column tabel utama dan Modal Changelog dalam konfigurasi default (tabel utama: 8 kolom terlihat, urutan default, tanpa pin; Modal Changelog: 6 kolom terlihat, urutan default, tanpa pin): hook `before` membersihkan preferensi kolom di cache browser untuk kedua tabel, dan tiap TC yang mengubah konfigurasi memulihkannya di langkah akhir TC.
- Tabel parameter langkah ulang:

  | Kolom Hideable (urutan default) | Urutan seret pada TC-GS-UCF-239 (ke posisi pertama, berurutan) |
  |---|---|
  | `Active` | `Field Name` |
  | `Field Name` | `Data Type` |
  | `Data Type` | `Value Setting` |
  | `Value Setting` | `Placeholder` |
  | `Placeholder` | `Required` |
  | `Required` | `Modified By` |
  | `Modified By` | `Last Updated` |

  Kolom pertama dipakai langkah "untuk setiap kolom Hideable" pada TC-GS-UCF-236, 238, dan 508; kolom kedua dipakai langkah "untuk setiap kolom seret" pada TC-GS-UCF-239. Kolom `Last Updated` tidak termasuk "Kolom Hideable" karena menjadi kolom terakhir yang tersisa.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API field Population yang dibuat hook `before`; pulihkan preferensi visibilitas, urutan, dan pin kolom tabel utama dan Modal Changelog ke default; pulihkan ukuran viewport.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: drag-and-drop item daftar kolom pada Modal Setup Column; mengubah lebar viewport (800px) sehingga tabel dapat digeser horizontal dan memulihkannya; scroll horizontal area tabel dan pembacaan kolom beku; pembacaan state disabled checkbox dan icon Pin beserta tooltip; membersihkan preferensi kolom di cache browser; muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka).
- State global: preferensi kolom (visibilitas, urutan, pin) tersimpan di cache browser per pengguna per tabel; spec memulihkannya di langkah akhir tiap TC yang mengubahnya (langkah 14, 37, 58, 89, dan 111) dan hook `after` sebagai cadangan. Lebar viewport 800px diatur pada langkah 59 dan 90 dan dipulihkan pada langkah 96.

## Test Steps

### TC-GS-UCF-235: Screening Overlay Column Visibility

1. Klik header Column Visibility (`⋯`)
2. Verifikasi Overlay memuat delapan kolom tercentang: `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Required`, `Modified By`, dan `Last Updated`
3. Verifikasi kedelapan kolom di Overlay memiliki drag handle
4. Verifikasi item `Setup Column...` di bagian bawah Overlay
5. Verifikasi Table Tools tidak memuat kontrol Setup Column
6. Tekan Esc untuk menutup Overlay

### TC-GS-UCF-236: Overlay Column Visibility, uncheck kolom langsung diterapkan dan tersimpan

7. Klik header Column Visibility (`⋯`)
8. Untuk setiap kolom Hideable pada tabel Prerequisites (langkah 8 sampai 9): uncheck kolom di Overlay
9. Verifikasi kolom tersebut langsung hilang dari tabel
10. Verifikasi Overlay tidak memiliki tombol Save
11. Muat ulang halaman (F5)
12. Verifikasi kolom `Last Updated` tampil
13. Verifikasi hanya kolom `Last Updated` yang tampil (ketujuh kolom lain tidak tampil)
14. Pulihkan konfigurasi: buka Modal Setup Column lewat `⋯` > `Setup Column...`, klik [Reset to Default], klik [Save]

### TC-GS-UCF-237: Screening Modal Setup Column

15. Klik header Column Visibility (`⋯`), klik `Setup Column...`
16. Verifikasi Header: Title "Setup Column"
17. Verifikasi Header: icon `[✕]`
18. Verifikasi Header: subtitle "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
19. Verifikasi Body memuat delapan kolom berurutan: `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Required`, `Modified By`, dan `Last Updated`
20. Verifikasi tiap kolom di Body memiliki drag handle
21. Verifikasi checkbox tiap kolom di Body tercentang
22. Verifikasi icon Pin pada tiap kolom di Body
23. Verifikasi Live Preview tabel tampil
24. Verifikasi Footer: `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)
25. Verifikasi Footer tidak memiliki tombol `[Cancel]`
26. Verifikasi kolom Checkbox dan Actions tidak muncul sebagai baris Setup Column
27. Klik `[✕]` untuk menutup Modal Setup Column

### TC-GS-UCF-238: Modal Setup Column, hide dan unhide kolom Hideable lalu Save

28. Klik header Column Visibility (`⋯`), klik `Setup Column...`
29. Untuk setiap kolom Hideable pada tabel Prerequisites (langkah 29 sampai 30): uncheck kolom
30. Verifikasi kolom tersebut hilang dari Live Preview
31. Untuk setiap kolom Hideable pada tabel Prerequisites (langkah 31 sampai 32): centang kembali kolom
32. Verifikasi kolom tersebut muncul lagi pada Live Preview pada urutan default
33. Uncheck `Last Updated`, klik [Save]
34. Muat ulang halaman (F5)
35. Verifikasi tabel menampilkan tujuh kolom: `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Required`, dan `Modified By`
36. Verifikasi kolom `Last Updated` tidak tampil
37. Pulihkan konfigurasi: buka Modal Setup Column lewat `⋯` > `Setup Column...`, klik [Reset to Default], klik [Save]

### TC-GS-UCF-508: Kolom Last Updated sebagai kolom terakhir tidak dapat di-uncheck

38. Klik header Column Visibility (`⋯`), klik `Setup Column...`
39. Untuk setiap kolom Hideable pada tabel Prerequisites (langkah 39 sampai 40): uncheck kolom sampai tersisa `Last Updated`
40. Verifikasi kolom tersebut hilang dari Live Preview
41. Hover checkbox `Last Updated`
42. Verifikasi checkbox `Last Updated` tampil dengan status Disabled
43. Verifikasi Tooltip "At least one column must remain visible."
44. Centang kembali `Field Name`
45. Verifikasi checkbox `Last Updated` Enabled kembali
46. Klik `[✕]`
47. Verifikasi Modal Setup Column tertutup tanpa menyimpan
48. Verifikasi tabel tetap menampilkan delapan kolom: `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Required`, `Modified By`, dan `Last Updated`

### TC-GS-UCF-239: Modal Setup Column, drag reorder delapan kolom lalu Save

49. Klik header Column Visibility (`⋯`), klik `Setup Column...`
50. Untuk setiap kolom seret pada tabel Prerequisites (langkah 50 sampai 51): seret kolom ke posisi pertama
51. Verifikasi kolom yang diseret menjadi kolom pertama pada Live Preview
52. Seret `Active` (kolom pada posisi terakhir) ke posisi keempat
53. Verifikasi urutan Live Preview: `Last Updated`, `Modified By`, `Required`, `Active`, `Placeholder`, `Value Setting`, `Data Type`, `Field Name`
54. Klik [Save]
55. Verifikasi tabel menampilkan urutan kolom yang sama
56. Muat ulang halaman (F5)
57. Verifikasi urutan kolom yang sama bertahan setelah muat ulang
58. Pulihkan konfigurasi: buka Modal Setup Column lewat `⋯` > `Setup Column...`, klik [Reset to Default], klik [Save]

### TC-GS-UCF-240: Modal Setup Column, pin dan unpin delapan kolom dengan batas tiga kolom

59. Atur lebar viewport 800px agar tabel dapat digeser horizontal
60. Klik header Column Visibility (`⋯`), klik `Setup Column...`
61. Putaran 1: pin `Active`, `Field Name`, dan `Data Type`
62. Hover icon Pin kolom `Value Setting`
63. Verifikasi icon Pin kolom `Value Setting` Disabled
64. Verifikasi Tooltip "Maximum 3 columns can be pinned at once. Unpin another column first."
65. Klik [Save]
66. Geser tabel horizontal
67. Verifikasi `Active`, `Field Name`, dan `Data Type` membeku di kiri dan tetap saat tabel digeser horizontal
68. Muat ulang halaman (F5), lalu geser tabel horizontal
69. Verifikasi `Active`, `Field Name`, dan `Data Type` tetap membeku di kiri setelah muat ulang
70. Klik header Column Visibility (`⋯`), klik `Setup Column...`
71. Unpin `Active`, lalu hover icon Pin kolom `Value Setting`
72. Verifikasi icon Pin kolom `Value Setting` kembali aktif
73. Unpin `Field Name` dan `Data Type`, klik [Save]
74. Geser tabel horizontal
75. Verifikasi tidak ada kolom yang membeku
76. Putaran 2: klik header Column Visibility (`⋯`), klik `Setup Column...`, pin `Value Setting`, `Placeholder`, dan `Required`, klik [Save]
77. Geser tabel horizontal
78. Verifikasi `Value Setting`, `Placeholder`, dan `Required` membeku di kiri dan tetap saat tabel digeser horizontal
79. Muat ulang halaman (F5), lalu geser tabel horizontal
80. Verifikasi `Value Setting`, `Placeholder`, dan `Required` tetap membeku di kiri setelah muat ulang
81. Klik header Column Visibility (`⋯`), klik `Setup Column...`, unpin `Value Setting`, `Placeholder`, dan `Required`, klik [Save]
82. Geser tabel horizontal
83. Verifikasi tidak ada kolom yang membeku
84. Putaran 3: klik header Column Visibility (`⋯`), klik `Setup Column...`, pin `Modified By` dan `Last Updated`, klik [Save]
85. Geser tabel horizontal
86. Verifikasi `Modified By` dan `Last Updated` membeku di kiri dan tetap saat tabel digeser horizontal
87. Muat ulang halaman (F5), lalu geser tabel horizontal
88. Verifikasi `Modified By` dan `Last Updated` tetap membeku di kiri setelah muat ulang
89. Pulihkan konfigurasi: buka Modal Setup Column lewat `⋯` > `Setup Column...`, klik [Reset to Default], klik [Save]

### TC-GS-UCF-509: Kolom Checkbox dan Actions tetap di tepi tabel saat kolom data digeser

90. Atur lebar viewport 800px
91. Geser area tabel horizontal ke kanan sampai kolom `Last Updated` terlihat
92. Verifikasi kolom data `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Required`, `Modified By`, dan `Last Updated` bergeser mengikuti geseran
93. Verifikasi kolom Checkbox tetap berada di tepi kiri tabel
94. Verifikasi header kolom Actions `⋯` dan menu `⋯` per baris tetap berada di tepi kanan tabel
95. Geser area tabel kembali ke kiri
96. Pulihkan lebar viewport ke ukuran semula

### TC-GS-UCF-241: Reset to Default mengembalikan konfigurasi default

97. Klik header Column Visibility (`⋯`), klik `Setup Column...`
98. Seret `Last Updated` ke posisi pertama, uncheck `Required`, klik [Save]
99. Klik header Column Visibility (`⋯`), klik `Setup Column...`, klik [Reset to Default], klik [Save]
100. Verifikasi kedelapan kolom tampil dengan urutan default: `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Required`, `Modified By`, `Last Updated`

### TC-GS-UCF-242: Tutup Modal Setup Column lewat [✕] atau Esc membuang perubahan

101. Klik header Column Visibility (`⋯`), klik `Setup Column...`, uncheck `Required`
102. Klik `[✕]`
103. Verifikasi kolom `Required` tetap tampil di tabel
104. Klik header Column Visibility (`⋯`), klik `Setup Column...`, uncheck `Required`
105. Tekan Esc
106. Verifikasi kolom `Required` tetap tampil di tabel

### TC-GS-UCF-243: Konfigurasi kolom tabel utama tidak memengaruhi Modal Changelog

107. Klik header Column Visibility (`⋯`), uncheck `Required` dan `Placeholder`, tutup Overlay
108. Klik icon Changelog
109. Verifikasi Modal Changelog menampilkan kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By`
110. Klik `✕` di header untuk menutup Modal Changelog
111. Pulihkan konfigurasi: buka Modal Setup Column lewat `⋯` > `Setup Column...`, klik [Reset to Default], klik [Save]

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 111 langkah nominal; dengan ekspansi blok ulang per kolom (tujuh iterasi pada langkah 8 sampai 9, 29 sampai 30, 31 sampai 32, 39 sampai 40, dan 50 sampai 51) jumlahnya jauh di atas smell sekitar 35 langkah. Alasan: seluruhnya satu topik dan satu dataset (Overlay Column Visibility dan Modal Setup Column tabel utama), satu akun, tanpa mengubah data Custom Field; tiap TC memulai dari konfigurasi default dan memulihkannya di akhir sehingga tetap bermakna bila TC lain gagal. Idiom ulang per kolom mengikuti bagian 8b butir 7 konvensi: parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` diulang satu per kolom.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14, 37, 58, 89, dan 111 (pemulihan konfigurasi ke default yang dituliskan TC sebagai langkah terakhir), langkah 59, 90, dan 96 (lebar viewport 800px dan pemulihannya, lihat Temuan untuk QA), langkah geser tabel horizontal pada TC-GS-UCF-240 dan TC-GS-UCF-509, serta langkah menutup Overlay, Modal Setup Column, dan Modal Changelog.
- Langkah pemulihan menjalankan `[Reset to Default]` dan `[Save]` tanpa `Verifikasi`; `[Save]` Setup Column adalah aksi sisi klien tanpa request tulis ke server sehingga tidak ada langkah "Tunggu aksi selesai" (bagian 8b butir 8).
- TC-GS-UCF-241 langkah 1 ("Ubah urutan dan hide `Required`") tidak menyebut urutan yang diubah; spec menyeret `Last Updated` ke posisi pertama dan meng-uncheck `Required` (lihat Temuan untuk QA).
- Pembagian TC lintas spec: Search tabel utama ada di spec 051; Filter Panel di spec 052; kombinasi Search, Filter, Sort, dan Pagination di spec 053 (TC-GS-UCF-219 ada di sana karena memakai hide kolom pada Filter); Sort di spec 054; Download tabel utama di spec 057 (TC-GS-UCF-247 memakai hide kolom). Setup Column Modal Changelog (TC-GS-UCF-270, 271, 528, 529, 357 sampai 360) ada di spec 065.
- Temuan untuk QA:
  - TC-GS-UCF-240 langkah "geser tabel horizontal" dan TC-GS-UCF-509 butuh tabel yang meluap; TC-GS-UCF-240 tidak menyebut lebar viewport. Spec memakai 800px (sama dengan TC-GS-UCF-509) dan memulihkannya.
  - TC-GS-UCF-241 langkah 1 tidak menyebut urutan yang diubah; spec memilih `Last Updated` ke posisi pertama.
  - TC-GS-UCF-236 menyebut "Muat ulang halaman" tanpa menyebut bahwa konfigurasi tersimpan di cache browser; Catatan TC menyebut cache browser (`prd-conventions.md` §9.3).
  - TC-GS-UCF-235 dan 237 punya Post Condition kosong; TC-GS-UCF-236, 238, 239, 240, 243 menulis Post Condition pemulihan konfigurasi yang juga muncul sebagai langkah terakhir; tidak diasersi.
  - TC-GS-UCF-243 mensyaratkan konfigurasi Modal Changelog default (6 kolom); hook `before` membersihkan preferensi Modal Changelog. Entri Changelog tersedia karena seeding Pre-setup dan Population; isinya tidak diasersi.
  - Email akun dan data Pre-setup dari Tabel Data Uji TC; tidak ada keputusan NC yang berbeda dari API/LLD pada spec ini (Setup Column hanya melalui header `⋯` mengikuti NC-01).
