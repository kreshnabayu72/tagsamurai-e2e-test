---
id: TC-GS-DIV-E2E-048-setup-column-tabel-reorder-pin-reset-dan-search-kolom-hidden
title: "Setup Column Tabel Division: Reorder, Pin, Reset, dan Search terhadap Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-174
  - TC-GS-DIV-175
  - TC-GS-DIV-176
  - TC-GS-DIV-146
  - TC-GS-DIV-147
coverage:
  web: automated
---

# Setup Column Tabel Division: Reorder, Pin, Reset, dan Search terhadap Kolom Hidden

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Division.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS).
- Data Dinamis (seeding minimal, S-11): Division `Quality Assurance` (QA), anggota Population D-02, satu-satunya Division yang dipakai `Verifikasi` spec ini (TC-GS-DIV-146 dan 147). Di-seed idempotent lewat kemampuan seeding Division lewat API di hook `before` dengan Name dan Code literal (dilewati bila sudah ada); tabel memuat baris Pre-setup ditambah `Quality Assurance`, semuanya pada halaman 1. Nama literal tanpa suffix karena TC mencari baris `Quality Assurance` (Code `QA`) dengan keyword `QA` dan `Quality` (pengecualian S-12 untuk Population Division: seeding idempotent, cleanup milik spec, suite serial). Cleanup di hook `after` hanya menghapus Division yang dibuat spec ini lewat API, tanpa berasumsi seeding berhasil penuh.
- Data uji: kolom `Name`, `Code`, `Last Updated`; keyword `QA` dan `Quality` (TC-GS-DIV-146, 147).
- Preferensi kolom (urutan, visibilitas, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]`; Overlay Column Visibility langsung berlaku (PRD division.md §4.2e; prd-conventions.md §9.3). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- Lebar konten tabel Division harus melebihi lebar viewport (overflow horizontal) supaya scroll horizontal pada TC-GS-DIV-175 teramati. Viewport disempitkan di langkah 15 dan dikembalikan ke ukuran awal di langkah 44; ukuran viewport dipilih tim FE karena TC tidak menyebutnya.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Division dikembalikan ke default (Name, Code, Last Updated tampil berurutan, tanpa pin) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel Division di browser; viewport dikembalikan ke ukuran awal; Search dikosongkan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: drag and drop item kolom pada Popup Setup Column; mengatur viewport; scroll horizontal tabel; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

1. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`

### TC-GS-DIV-174: Setup Column: reorder tiap kolom lewat drag lalu Save

2. Seret `Name` ke posisi pertama
3. Klik `[Save]`
4. Verifikasi kolom `Name` berada di posisi pertama tabel
5. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
6. Seret `Code` ke posisi pertama
7. Klik `[Save]`
8. Verifikasi kolom `Code` berada di posisi pertama tabel
9. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
10. Seret `Last Updated` ke posisi pertama
11. Klik `[Save]`
12. Verifikasi kolom `Last Updated` berada di posisi pertama tabel
13. Muat ulang halaman (F5)
14. Verifikasi urutan terakhir tetap tersimpan: `Last Updated`, `Code`, `Name`

### TC-GS-DIV-175: Setup Column: pin dan unpin tiap kolom lalu Save

15. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
16. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
17. Klik icon pin pada `Name`
18. Klik `[Save]`
19. Scroll tabel secara horizontal
20. Verifikasi kolom `Name` membeku (sticky) saat scroll horizontal
21. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
22. Klik icon pin pada `Name` untuk unpin
23. Klik `[Save]`
24. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
25. Klik icon pin pada `Code`
26. Klik `[Save]`
27. Scroll tabel secara horizontal
28. Verifikasi kolom `Code` membeku (sticky) saat scroll horizontal
29. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
30. Klik icon pin pada `Code` untuk unpin
31. Klik `[Save]`
32. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
33. Klik icon pin pada `Last Updated`
34. Klik `[Save]`
35. Scroll tabel secara horizontal
36. Verifikasi kolom `Last Updated` membeku (sticky) saat scroll horizontal
37. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
38. Klik icon pin pada `Last Updated` untuk unpin
39. Klik `[Save]`
40. Muat ulang halaman (F5)
41. Verifikasi tabel Division termuat dengan sedikitnya satu baris
42. Scroll tabel secara horizontal
43. Verifikasi pin terakhir yang disimpan tetap berlaku: tidak ada kolom yang membeku saat scroll horizontal
44. Kembalikan viewport ke ukuran awal

### TC-GS-DIV-176: Setup Column: Reset to Default mengembalikan susunan default

45. Buka Popup Setup Column lewat header Actions (⋯) lalu `Setup Column...`
46. Klik `[Reset to Default]`
47. Verifikasi preview berurutan `Name`, `Code`, `Last Updated`
48. Verifikasi preview menampilkan seluruh kolom `Name`, `Code`, `Last Updated` visible
49. Verifikasi preview tanpa pin pada kolom mana pun
50. Klik `[Save]`
51. Muat ulang halaman (F5)
52. Verifikasi susunan default bertahan: tabel menampilkan `Name`, `Code`, `Last Updated` berurutan dan seluruhnya visible

### TC-GS-DIV-146: Search tidak mencari kolom yang di-hide

53. Klik header kolom Actions (⋯)
54. Hilangkan centang kolom `Code` pada Overlay Column Visibility
55. Verifikasi baris `Quality Assurance` tampil di tabel (kolom `Code` tersembunyi)
56. Ketik Search `QA`, tekan Enter
57. Verifikasi baris `Quality Assurance` tidak tampil (kolom `Code` yang di-hide tidak dicari)
58. Ganti isi kotak search dengan `Quality`, tekan Enter
59. Verifikasi baris `Quality Assurance` tampil lewat kolom `Name`

### TC-GS-DIV-147: Search kembali mencari kolom setelah di-unhide

60. Klik header kolom Actions (⋯)
61. Centang kembali kolom `Code` pada Overlay Column Visibility
62. Ganti isi kotak search dengan `QA`, tekan Enter
63. Verifikasi baris `Quality Assurance` tampil lewat kolom `Code`
64. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. TC-GS-DIV-30 (Population) mensyaratkan 32 baris; spec men-seed hanya `Quality Assurance` yang dipakai `Verifikasi` (S-11).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 174, 175, 176 (reorder, pin, Reset to Default; Reset TC-GS-DIV-176 memerlukan susunan yang sudah diubah dan disimpan oleh TC-GS-DIV-174), lalu 146 dan 147 (Search terhadap kolom hidden) di akhir karena memakai Overlay Column Visibility pada konfigurasi default hasil reset. Urutan di `tc-division.md` adalah 146, 147, 174, 175, 176.
- Anchor positif (S-03, bagian 8b butir 2): langkah 55 (baris `Quality Assurance` tampil sebelum Search `QA`) mendahului asersi ketiadaan baris pada langkah 57. Langkah 41 (tabel Division termuat dengan sedikitnya satu baris sesudah muat ulang halaman) mendahului asersi ketiadaan kolom membeku pada langkah 43.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka popup untuk TC-GS-DIV-174), langkah 15 dan 44 (menyempitkan dan mengembalikan viewport untuk TC-GS-DIV-175), serta langkah 64 (menutup Search di akhir spec). Langkah pembuka popup yang berulang (5, 9, 16, 21, 24, 29, 32, 37, 45) merupakan prefix berulang. Langkah 22, 30, dan 38 (unpin) merupakan bagian TC-GS-DIV-175 dan sekaligus memulihkan state pin.
- Langkah 1 TC-GS-DIV-147 ("Hilangkan centang kolom `Code`, lalu centang kembali") dipenuhi state hidden dari TC-GS-DIV-146 sehingga hanya langkah centang kembali (langkah 60 dan 61) yang ditulis; Search bar tetap terbuka sejak langkah 56.
- Spec melewati sekitar 35 langkah karena TC-GS-DIV-174 dan TC-GS-DIV-175 menguji tiga kolom dengan blok identik (buka popup, ubah, Save, cek) dan TC-GS-DIV-176, 146, 147 memakai popup dan overlay Setup Column yang sama; satu kelas harness (fungsional) dan satu dataset. Blok 174 dan 175 berdiri sendiri; blok 176 memakai susunan kolom hasil 174 dan 175 (Reset to Default), dan blok 147 memakai state hidden hasil 146. Langkah pembuka popup yang berulang merupakan prefix berulang.
- Pembagian TC lintas spec: TC-GS-DIV-171, 172, 173, 177, 178 (screening, hide, unhide, cancel, kolom terakhir) ada di spec 047; TC-GS-DIV-179 dan 234 (isolasi konfigurasi dengan Modal Changelog) ada di spec 049; TC-GS-DIV-144 (Search Name dan Code) ada di spec 041.
- Temuan untuk QA:
  - TC-GS-DIV-174: Langkah TC tidak memuat muat ulang (F5), tetapi Expected d menyebut "Setelah F5 urutan terakhir tetap tersimpan"; spec menambahkan langkah F5 (langkah 13) mengikuti Expected d. Urutan default `Name` sudah berada di posisi pertama, sehingga seret `Name` ke posisi pertama tidak mengubah urutan.
  - TC-GS-DIV-175: Expected d ("pin terakhir yang disimpan tetap berlaku") ambigu: pin terakhir yang disimpan dapat berarti pin `Last Updated` (sebelum unpin) atau keadaan tanpa pin setelah unpin terakhir. Spec memakai tafsir kedua (mengikuti urutan langkah TC dan pola TC-GS-DIV-173), sehingga persistensi pin aktif lewat F5 tidak teramati. TC juga tidak menyebut ukuran viewport; tim FE perlu menetapkan viewport sempit supaya tabel dapat discroll horizontal.
  - TC-GS-DIV-146: kolom `Code` yang di-hide lewat Overlay Column Visibility; TC tidak menyebut apakah hasil kosong `QA` menampilkan empty state, sehingga hanya ketiadaan baris `Quality Assurance` yang diasersi.
  - TC-GS-DIV-176: Test Data kosong; "Susunan kolom sudah diubah dan disimpan" dipenuhi hasil TC-GS-DIV-174 dan 175 di dalam spec ini.
  - Mekanisme menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
