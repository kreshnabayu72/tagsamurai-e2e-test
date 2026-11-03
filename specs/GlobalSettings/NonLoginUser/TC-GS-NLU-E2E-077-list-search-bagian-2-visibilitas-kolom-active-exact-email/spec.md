---
id: TC-GS-NLU-E2E-077-list-search-bagian-2-visibilitas-kolom-active-exact-email
title: "List Search bagian 2: Search terikat visibilitas kolom, kolom Active exact, email bukan kolom, kolom curated dan Custom Field, nama lengkap Represented By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-262
  - TC-GS-NLU-263
  - TC-GS-NLU-264
  - TC-GS-NLU-265
  - TC-GS-NLU-266
  - TC-GS-NLU-465
coverage:
  web: automated
---

# List Search bagian 2: Search terikat visibilitas kolom, kolom Active exact, email bukan kolom, kolom curated dan Custom Field, nama lengkap Represented By

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 13; hanya dibaca, tidak diubah, tanpa suffix): Non-Login User `Budi Kurniawan` (Operations, Represented By Ahmad Fauzi, `budi.kurniawan@qwertysystem.net`, Active), `Rina Marlina` (Temporary User `Yes`), `Joko Susilo` dan `Agus Salim` (Inactive); Custom Field dasar `Blood Type` (Dropdown A/B/O/AB, Active). Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis (di-seed hook `before` lewat API, mekanisme disediakan tim FE/BE; dihapus hook `after`): Non-Login User `Darah AB {runId}-077` (Division `Operations`, Represented By `Ahmad Fauzi`, Blood Type `AB`, Active). Dipakai TC-GS-NLU-266 karena Pre-setup tidak menyebut record bernilai Blood Type `AB`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengaturan ukuran halaman (opsi 10/25/50/100); penghapusan preferensi kolom di browser di hook `after` (disediakan tim FE; spec ini menyimpan konfigurasi kolom lewat Setup Column).
- State global: konfigurasi kolom tabel (kolom Temporary User dan Blood Type diaktifkan lewat Setup Column); dipulihkan oleh langkah penghubung dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-262: Search terikat visibilitas kolom

1. Klik `⋯` pada header kolom Actions, hapus centang kolom Division, tutup overlay Column Visibility
2. Ketik Search `Operations`, tekan Enter
3. Verifikasi baris yang hanya cocok lewat Division tidak ditemukan (empty state `No results found` tampil)
4. Klik `⋯` pada header kolom Actions, centang kembali kolom Division, tutup overlay Column Visibility
5. Ganti isi kotak search dengan `Operations`, tekan Enter
6. Verifikasi baris dengan Division `Operations` ditemukan (sedikitnya satu baris tampil)

### TC-GS-NLU-263: Search kolom Active memakai pencocokan exact atas teks status

7. Ganti isi kotak search dengan `Inactive`, tekan Enter
8. Verifikasi hanya baris Inactive yang tampil: baris `Joko Susilo` dan `Agus Salim` tampil dan seluruh baris hasil berstatus Inactive
9. Ganti isi kotak search dengan `Active`, tekan Enter
10. Verifikasi hanya baris Active yang tampil: sedikitnya satu baris tampil dan seluruh baris hasil berstatus Active
11. Verifikasi baris Inactive tidak ikut walau `Inactive` memuat teks `active`: baris `Joko Susilo` dan `Agus Salim` tidak tampil

### TC-GS-NLU-264: Alamat email tidak dapat dicari karena bukan kolom tabel

12. Ganti isi kotak search dengan `budi.kurniawan@`, tekan Enter
13. Verifikasi `No results found` (Email tidak termasuk kolom List)

### TC-GS-NLU-265: Search pada kolom curated Temporary User yang visible

14. Klik `(←)` pada kotak Search, ubah ukuran halaman menjadi 50
15. Klik `⋯` header Actions > `Setup Column...`, centang kolom Temporary User, klik `[Save]`
16. Ketik Search `Yes`, tekan Enter
17. Verifikasi baris Temporary User `Rina Marlina` ditemukan melalui kolom Temporary User
18. Klik `⋯` header Actions > `Setup Column...`, hapus centang kolom Temporary User, klik `[Save]`
19. Ganti isi kotak search dengan `Yes`, tekan Enter
20. Verifikasi `No results found` (kolom yang disembunyikan tidak dicari)
21. Klik `(←)` pada kotak Search, ubah ukuran halaman menjadi 10

### TC-GS-NLU-266: Search pada kolom Custom Field aktif non-tanggal yang visible

22. Klik `⋯` header Actions > `Setup Column...`, centang kolom Blood Type, klik `[Save]`
23. Ketik Search `AB`, tekan Enter
24. Verifikasi baris dengan Blood Type `AB` ditemukan (`Darah AB {runId}-077`)
25. Klik `⋯` header Actions > `Setup Column...`, hapus centang kolom Blood Type, klik `[Save]`

### TC-GS-NLU-465: Search nama lengkap Represented By menemukan baris walau sel menampilkan bentuk singkat

26. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
27. Verifikasi baris yang Represented By-nya Ahmad Fauzi tampil (mis. `Budi Kurniawan`)
28. Verifikasi sel Represented By menampilkan `Ahmad F`
29. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): menutup overlay Column Visibility, `(←)` yang mengosongkan Search, mengubah ukuran halaman ke 50 lalu 10 (supaya baris `Rina Marlina` termuat pada hasil `Yes`), dan memulihkan kolom Blood Type pada langkah 25. Kolom Temporary User dipulihkan di dalam TC-GS-NLU-265. Search untuk menemukan baris target dicatat di sini (R-16).
- Asersi tambahan (S-03): empty state `No results found` pada TC-GS-NLU-262 menjadi anchor positif asersi absence (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-NLU-266 tidak menyebut record bernilai Blood Type `AB` di Pre-setup (No. 11 dan 13 hanya menyebut Blood Type `O` untuk `Rina Marlina`); spec men-seed record milik sendiri bernama `Darah AB {runId}-077`.
  - TC-GS-NLU-262 tidak menyebut cara menutup overlay Column Visibility; spec menulisnya sebagai langkah penghubung.
  - TC-GS-NLU-265 Expected a menyebut `Rina Marlina` ditemukan; hasil Search `Yes` mencakup seluruh Temporary User sehingga spec menaikkan ukuran halaman ke 50.
  - Spec ini menyimpan konfigurasi kolom lewat Setup Column, tetapi `suite.md` belum mendaftarkannya pada daftar spec Setup Column.
