---
id: TC-GS-DIV-E2E-069-sinkron-dropdown-division-form-user-dan-non-login-user
title: "Sinkron Dropdown Division di Form User dan Non-Login User (Create, Rename, Delete)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-250
  - TC-GS-DIV-251
  - TC-GS-DIV-252
  - TC-GS-DIV-253
coverage:
  web: automated
---

# Sinkron Dropdown Division di Form User dan Non-Login User (Create, Rename, Delete)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup dan Population D-02 tidak dipakai dan tidak diubah.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi; seluruh data milik spec ini):
  - `Metro Branch 3 {runId}-069` dengan Code `MTB` (D-15): dibuat spec lewat UI pada langkah 2 (setara dependensi TC-GS-DIV-245). Code `MTB` literal sesuai TC (pengecualian S-12: seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite berjalan serial); hook `before` menghapus lewat API sisa Division bernama `Metro Branch 3 {runId lama}-069` (nama berpola `Metro Branch 3 *-069`, bukan berdasarkan Code saja) yang masih memegang Code `MTB`.
  - `Warehouse {runId}-069`: Division milik spec, di-seed lewat API di hook `before`; di-rename lewat UI menjadi `Warehouse and Distribution {runId}-069` (setara dependensi TC-GS-DIV-109 yang me-rename `Warehouse` Population D-02). Bebas relasi saat di-seed dan menjadi in-use oleh Login User uji `syncuser+{runId}-069@qwertysystem.net`.
  - `Public Relations {runId}-069` (D-10): Division bebas relasi, di-seed lewat API di hook `before`; dihapus lewat UI (setara dependensi TC-GS-DIV-116).
  - Login User uji `syncuser+{runId}-069@qwertysystem.net` dengan Division `Warehouse {runId}-069`, di-seed lewat API di hook `before` (untuk Expected Result b TC-GS-DIV-252). Nilai field wajib lain disediakan tim FE lewat fixture `fixtures/division.json` yang belum ada.
- Kemampuan teknis: seeding Division dan Login User lewat API serta penghapusan Division dan Login User lewat API (sesi API aktor Total Control, `Spectra.env.GS_TC_PASSWORD`); membaca seluruh opsi dropdown Division form Create User dengan menggulir daftar tanpa mengetik pencarian (disediakan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Login User `syncuser+{runId}-069@qwertysystem.net`, lalu Division `Metro Branch 3`, `Warehouse` atau `Warehouse and Distribution`, dan `Public Relations` bersuffix `{runId}-069` bila masih ada.
- Tidak ada state global yang diubah.
- TC-GS-DIV-250, 251, 252, 253: login sebagai Total Control dan berada di Global Settings > User > Division.

## Test Steps

### Dependensi TC-GS-DIV-245, 109, 116: Create, Rename, dan Delete Division

1. Buka Global Settings > User > Tab User List, ketik Search `syncuser+{runId}-069@qwertysystem.net`, tekan Enter, catat Last Update baris user sebagai `{lastUpdateUser}`
2. Buka Global Settings > User > Tab Division, klik [+ Division], isi Division Name `Metro Branch 3 {runId}-069` dan Code `MTB`, klik [Submit]
3. Tunggu aksi selesai
4. Ketik Search `Warehouse {runId}-069`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Edit, ubah Division Name menjadi `Warehouse and Distribution {runId}-069`, klik [Save]
5. Tunggu aksi selesai
6. Ganti isi kotak search dengan `Public Relations {runId}-069`, tekan Enter, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog konfirmasi
7. Tunggu aksi selesai (dialog konfirmasi tertutup)

### TC-GS-DIV-250, 252, 253: dropdown Division form Create User

8. Buka Global Settings > User > Tab User List, klik tombol `[+ User]` (Create User)
9. Buka field dropdown Division
10. Gulir daftar opsi dropdown Division hingga opsi `Metro Branch 3 {runId}-069` terlihat
11. Verifikasi opsi `Metro Branch 3 {runId}-069` tampil pada dropdown Division
12. Gulir daftar opsi dropdown Division hingga opsi `Warehouse and Distribution {runId}-069` terlihat
13. Verifikasi opsi `Warehouse and Distribution {runId}-069` tampil pada dropdown Division
14. Verifikasi opsi `Warehouse {runId}-069` tidak ada pada daftar opsi dropdown Division
15. Verifikasi opsi `Public Relations {runId}-069` tidak ada pada daftar opsi dropdown Division
16. Pilih opsi `Metro Branch 3 {runId}-069` (gulir daftar bila perlu)
17. Verifikasi field Division menampilkan `Metro Branch 3 {runId}-069`
18. Klik `✕` di header form Create User
19. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
20. Klik [Leave]

### TC-GS-DIV-252 Expected Result b: nama baru pada User yang memakai Division

21. Ketik Search `syncuser+{runId}-069@qwertysystem.net`, tekan Enter pada tabel User List
22. Verifikasi kolom Division baris user menampilkan `Warehouse and Distribution {runId}-069`
23. Verifikasi Last Update baris user tidak berubah dari `{lastUpdateUser}` (tanpa perubahan data user)

### TC-GS-DIV-251: dropdown Division form Create Non-Login User

24. Buka Sub-tab Non-Login User, klik tombol `[+ Non-Login User]` (Create Non-Login User)
25. Buka field dropdown Division
26. Ketik `{runId}-069` pada pencarian di dropdown Division
27. Verifikasi opsi `Metro Branch 3 {runId}-069` tampil pada dropdown Division form Create Non-Login User
28. Klik `✕` di header form Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Urutan TC di spec berbeda dari urutan sumber: ketiga mutasi Division (Create TC-GS-DIV-245, Rename TC-GS-DIV-109, Delete TC-GS-DIV-116) dijalankan lebih dulu sebagai dependensi (langkah 2 sampai 7), lalu satu pembukaan form Create User memeriksa TC-GS-DIV-250, 252, dan 253 sekaligus (prinsip 6 dan 8), dan form Create Non-Login User (TC-GS-DIV-251) dibuka terakhir. Penghapusan `Public Relations` ditaruh sebelum pemeriksaan karena hasilnya adalah Precondition TC-GS-DIV-253.
- Dependensi dijalankan sebagai langkah di spec ini atau lewat seeding API, bukan bergantung pada spec lain. Pembuatan, rename, dan penghapusan Division sebagai objek uji ada di spec Create, Edit, dan Delete.
- Opsi dropdown Division form Create User diamati dengan menggulir daftar tanpa mengetik pencarian, karena PRD User mendefinisikan field Division form Create User hanya sebagai `Select division`. Pencarian di dalam dropdown dipakai hanya pada form Create Non-Login User (`Search division...`, `non-login-user.md` `FLD-05`; langkah 26). Dua opsi yang ada (langkah 11 dan 13) menjadi anchor positif bagi dua Verifikasi tidak ada opsi (langkah 14 dan 15).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencatat Last Update user sebagai pembanding langkah 23), langkah 3, 5, dan 7 (menunggu Create, Rename, dan Delete selesai), Search nama Division pada tabel Division sebelum Edit dan Delete (langkah 4 dan 6), menggulir daftar opsi (langkah 10 dan 12), serta langkah 16 sampai 20 (memilih opsi sebagai langkah TC-GS-DIV-250 Expected Result b, lalu menutup form dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`; Verifikasi dialog pada langkah 19 adalah asersi tambahan agar penutupan deterministik, S-08). Form Create Non-Login User pada langkah 24 tidak diisi sehingga tidak dirty; langkah 28 menutupnya lewat `✕` tanpa dialog.
- Langkah 1 membuka Tab User List (layar modul User, bukan layar awal Division) untuk mencatat `{lastUpdateUser}` sebelum aksi Division; layar awal hook `beforeEach` adalah Tab Division.
- Nama tombol `[+ User]` dan `[+ Non-Login User]` mengikuti PRD User (tooltip `Create User`); TC sumber menulis "tombol Create User" dan "tombol Create Non-Login User".
- Temuan untuk QA:
  - PRD User tidak mendefinisikan pencarian di dropdown Division form Create User, sedangkan PRD Non-Login User mendefinisikannya (`non-login-user.md` `FLD-05`); TC-GS-DIV-250, 252, dan 253 tidak menyebut cara mencari opsi, sehingga spec menggulir daftar opsi.
  - TC-GS-DIV-252 Expected Result b ("Pada User yang memakai Division ini nama baru tampil tanpa perubahan data user") tidak menyebut User mana, di surface mana nama baru dilihat, dan cara mengamati "tanpa perubahan data user"; spec memakai Login User hasil seeding, kolom Division dan Last Update pada tabel User List (langkah 21 sampai 23). Precondition TC juga tidak menyebut User yang memakai Division itu.
  - TC-GS-DIV-250 Expected Result b ("Opsi dapat dipilih") tidak menyebut bentuk pemilihan; spec memilih opsi dan memverifikasi nilai field (langkah 16 dan 17).
  - TC-GS-DIV-253 mengasumsikan Division `Public Relations` sudah dihapus lewat TC lain; spec menghapusnya sendiri pada langkah 6 dan 7.
