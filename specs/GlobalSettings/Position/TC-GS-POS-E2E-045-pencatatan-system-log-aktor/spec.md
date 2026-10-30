---
id: TC-GS-POS-E2E-045-pencatatan-system-log-aktor
title: "Pencatatan ke System Log Aktor di Detail User untuk Create, Edit, Delete, dan Bulk Delete Position per Item"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-251
  - TC-GS-POS-305
  - TC-GS-POS-306
  - TC-GS-POS-307
coverage:
  web: automated
---

# Pencatatan ke System Log Aktor di Detail User untuk Create, Edit, Delete, dan Bulk Delete Position per Item

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Spec ini tidak menguji navigasi sehingga `## Test Steps` tidak mengulang langkah buka layar awal.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 12 `Warehouse Supervisor` (in-use oleh user Login aktif `Rina Wulandari`). Position ini hanya dicentang pada Bulk Delete campuran dan dilewati oleh sistem karena in-use; spec ini tidak mengubahnya dan Last Updated-nya tidak berubah (S-06, Position Pre-setup in-use yang hanya dibaca dan diblokir guard).
- Data Dinamis (suffix per run dan nomor spec):
  - `Risk Manager {runId}-045`: dibuat lewat UI pada TC-GS-POS-251, diubah menjadi `Risk Director {runId}-045` pada TC-GS-POS-305, lalu dihapus pada TC-GS-POS-306. Karena nama bersuffix unik per run, baseline entri System Log untuk nama itu adalah nol sebelum aksi.
  - `Compliance Officer {runId}-045` dan `Tax Specialist {runId}-045`: dua Position bebas relasi, di-seed lewat API di hook `before` (fixture baru `Fixture.position.bulkTargets045`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-045` yang masih ada; kembalikan ukuran halaman tabel Position ke 10 dan kosongkan Search tabel.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan jumlah dan kolom entri pada tab System Log di Detail User (Search di tab System Log dipakai untuk menemukan entri berdasarkan Name); ukuran halaman tabel Position 25 tersedia pada paginasi.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-251: System Log aktor, entri Create Position

1. Klik `[+ Position]`
2. Isi Position Name dengan `Risk Manager {runId}-045`
3. Klik `[Submit]`
4. Tunggu aksi selesai (modal tertutup)
5. Buka Global Settings > User, sub-tab User List, ketik Search email Budi Santoso, tekan Enter, buka Detail
6. Klik tab System Log
7. Ketik Search `Risk Manager {runId}-045`, tekan Enter
8. Verifikasi tepat 1 entri untuk Name `Risk Manager {runId}-045`
9. Verifikasi entri tersebut: Action `Create`, Object `Position`, Name `Risk Manager {runId}-045`, Field `Position Name`, Old Value `—`, New Value `Risk Manager {runId}-045`

### TC-GS-POS-305: System Log aktor, entri Edit Position

10. Buka Global Settings > User, klik sub-tab Position
11. Ketik Search `Risk Manager {runId}-045` pada tabel Position, tekan Enter
12. Klik `⋯` pada baris `Risk Manager {runId}-045`, pilih `Edit`
13. Ganti Position Name dengan `Risk Director {runId}-045`
14. Klik `[Save]`
15. Tunggu aksi selesai (modal tertutup)
16. Buka Detail Budi Santoso (Global Settings > User, User List, ketik Search email Budi Santoso, tekan Enter), klik tab System Log
17. Ketik Search `Risk Director {runId}-045`, tekan Enter
18. Verifikasi tepat 1 entri untuk Name `Risk Director {runId}-045`
19. Verifikasi entri tersebut: Action `Edit`, Object `Position`, Name `Risk Director {runId}-045`, Field `Position Name`, Old Value `Risk Manager {runId}-045`, New Value `Risk Director {runId}-045`

### TC-GS-POS-306: System Log aktor, entri Delete Position

20. Buka Global Settings > User, klik sub-tab Position
21. Ketik Search `Risk Director {runId}-045` pada tabel Position, tekan Enter
22. Klik `⋯` pada baris `Risk Director {runId}-045`, pilih `Delete`
23. Klik `[Delete]` pada dialog `Delete Position`
24. Tunggu aksi selesai (dialog tertutup)
25. Buka Detail Budi Santoso (Global Settings > User, User List, ketik Search email Budi Santoso, tekan Enter), klik tab System Log
26. Ketik Search `Risk Director {runId}-045`, tekan Enter
27. Verifikasi tepat 1 entri dengan Action `Delete` untuk Name `Risk Director {runId}-045`
28. Verifikasi entri Delete tersebut: Object `Position`, Name `Risk Director {runId}-045`, Field `Position Name`, Old Value `Risk Director {runId}-045`, New Value `—`

### TC-GS-POS-307: System Log aktor, Bulk Delete satu entri per item yang terhapus

29. Buka Detail Budi Santoso (Global Settings > User, User List, ketik Search email Budi Santoso, tekan Enter), klik tab System Log, ketik Search `Warehouse Supervisor`, tekan Enter, catat jumlah entri sebagai baseline
30. Buka Global Settings > User, klik sub-tab Position
31. Klik `(←)` pada kotak Search tabel
32. Ubah ukuran halaman menjadi 25
33. Centang baris `Compliance Officer {runId}-045`
34. Centang baris `Tax Specialist {runId}-045`
35. Centang baris `Warehouse Supervisor`
36. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
37. Klik `[Continue]` pada dialog `Delete Position`
38. Tunggu aksi selesai (dialog tertutup)
39. Buka Detail Budi Santoso (Global Settings > User, User List, ketik Search email Budi Santoso, tekan Enter), klik tab System Log
40. Ketik Search `Compliance Officer {runId}-045`, tekan Enter
41. Verifikasi tepat 1 entri baru: Action `Delete`, Object `Position`, Name `Compliance Officer {runId}-045`, New Value `—`
42. Ganti isi kotak search dengan `Tax Specialist {runId}-045`, tekan Enter
43. Verifikasi tepat 1 entri baru: Action `Delete`, Object `Position`, Name `Tax Specialist {runId}-045`, New Value `—`
44. Ganti isi kotak search dengan `Warehouse Supervisor`, tekan Enter
45. Verifikasi jumlah entri untuk `Warehouse Supervisor` sama dengan baseline langkah 29 (tidak ada entri untuk `Warehouse Supervisor` dari Bulk Delete ini)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Spec ini kelas pencatatan log; asersi presence dan asersi jumlah ada di spec ini.
- Urutan TC di spec: 251, 305, 306, 307. Satu record `Risk Manager {runId}-045` dipakai berurutan oleh 251, 305, dan 306 (create, rename, delete), sedangkan 307 yang menghapus data lain ditaruh paling akhir. Urutan sama dengan urutan sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10, 20, dan 30 (kembali ke tab Position), langkah 11 dan 21 (mencari baris target), langkah 29 (mengambil baseline jumlah entri `Warehouse Supervisor` sebelum Bulk Delete), langkah 31 (mengosongkan Search lewat `(←)`) dan langkah 32 (mengubah ukuran halaman menjadi 25 agar tiga baris tampil bersama; ukuran dipulihkan ke 10 di hook `after`), serta langkah "Tunggu aksi selesai" (langkah 4, 15, 24, 38). Langkah 5, 16, 25, 29, dan 39 membuka Detail Budi Santoso lewat Search email aktor, bukan lewat nama tampil.
- Langkah "Tunggu aksi selesai" (langkah 4, 15, 24, 38) ditulis tanpa `Verifikasi` sesudah `[Submit]`, `[Save]`, `[Delete]`, atau `[Continue]` yang hasilnya tidak diasersi langsung dan langkah berikutnya pindah surface ke Detail User (konvensi bagian 8b butir 8): langkah 4 dan 15 sesudah `[Submit]` dan `[Save]`, langkah 24 sesudah `[Delete]` (langkah 23), langkah 38 sesudah `[Continue]` (langkah 37).
- Baseline log memakai jumlah entri sebelum aksi (langkah 29 untuk `Warehouse Supervisor`) atau nama bersuffix unik (baseline nol), karena kolom Date System Log tampil pada ketelitian menit (Date Format dan Time Format General Settings) sehingga penanda waktu tidak membedakan entri baru dari entri sesaat sebelum aksi. Entri `Risk Manager`, `Risk Director`, `Compliance Officer`, dan `Tax Specialist` dicari lewat Name bersuffix yang unik per run sehingga baseline-nya nol; untuk TC-GS-POS-305 dan 306, "tepat 1 entri baru (bertambah 1 dari baseline)" diasersi sebagai tepat 1 entri untuk nama itu.
- Pembagian TC lintas spec: asersi "tidak ada entri log" untuk Edit No-Op (TC-GS-POS-308) ada di spec TC-GS-POS-E2E-046. Pencatatan Changelog dan Activity Log untuk Create, Edit, Delete, dan Bulk Delete (TC-GS-POS-242 sampai 245) ada di spec TC-GS-POS-E2E-044.
- P-1 (state berat): Expected b TC-GS-POS-307 ("tidak ada entri untuk `Warehouse Supervisor`") dimiliki aksi Bulk Delete campuran yang sama dengan Expected a (langkah 36 dan 37); kondisi satu item in-use dilewati hanya terbentuk oleh aksi itu, sehingga asersi absence-nya berada di spec ini dengan baseline jumlah entri (langkah 29) dan anchor positif (dua entri Delete pada langkah 41 dan 43). Spec TC-GS-POS-E2E-046 tidak memuat aksi Bulk Delete.
- Spec melewati sekitar 35 langkah (45 langkah). Seluruhnya satu kelas (pencatatan System Log aktor) dengan satu akun; blok baca-log berpola (buka Detail, tab System Log, Search, `Verifikasi`) diulang pada tiap TC dan tidak dihitung ke batas. Blok TC-GS-POS-307 memakai data seeding sendiri dan tetap bermakna bila blok 251 sampai 306 gagal.
- Temuan untuk QA:
  - TC-GS-POS-251, 305, 306, dan 307 mencantumkan butir precondition berlabel `c` dua kali (aktor login dan data record); tidak mengubah langkah.
  - TC tidak menyebut bahwa tab System Log di Detail User punya kolom Search; spec memakai Search untuk menemukan entri berdasarkan Name bersuffix. Bila Search tidak tersedia, entri dicari lewat Name pada tabel.
  - Status kotak Search tabel Position sesudah berpindah ke Detail User dan kembali ke sub-tab Position tidak disebut TC maupun PRD; langkah 31 mengklik `(←)` pada kotak Search dengan asumsi kotak masih terbuka berisi Search `Risk Director {runId}-045` dari langkah 21.
  - TC-GS-POS-307 memakai Position `Warehouse Supervisor` (Pre-setup 12) sebagai item in-use; Position ini tidak berubah dan tidak dihapus.
  - Bentuk aksi Bulk Delete: TC-GS-POS-307 menulis "buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`" dan spec mengikutinya (langkah 36); PRD §4.1 menyebut aksi massal `[Delete]` pada Bulk Action Bar. Bentuk yang benar menunggu konfirmasi QA dari aplikasi.
