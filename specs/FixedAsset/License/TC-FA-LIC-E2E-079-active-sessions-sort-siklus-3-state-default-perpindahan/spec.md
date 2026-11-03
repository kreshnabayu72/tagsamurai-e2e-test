---
id: TC-FA-LIC-E2E-079-active-sessions-sort-siklus-3-state-default-perpindahan
title: "Active Sessions: Sort Siklus 3-State per Kelas Kolom, Default, Perpindahan Kolom, dan Navigasi Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-86
  - TC-FA-LIC-268
  - TC-FA-LIC-269
  - TC-FA-LIC-270
  - TC-FA-LIC-271
  - TC-FA-LIC-272
coverage:
  web: automated
---

# Active Sessions: Sort Siklus 3-State per Kelas Kolom, Default, Perpindahan Kolom, dan Navigasi Keyboard

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup (tiga fixture sesi, dipulihkan dan diganti oleh fixture BE; identitas dan nilai dirujuk lewat `Fixture.fixedAssetLicense.*`, berkas fixture belum ada, disiapkan tim FE; nilai pada langkah dan tabel di bawah adalah nilai fixture itu):
  - #14: sesi aktif PT Sejahtera, 18 sesi, seat 25 (dipakai TC-FA-LIC-86). Hook `before` menyiapkan fixture ini.
  - #26: tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso; Online Users 5/25. Urutan default (Login Time terbaru lebih dulu): Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso.
  - #30: lima sesi cuplikan #26 ditambah sesi kedua Dewi Lestari (Position Admin Aset, Division Divisi IT, IP Address `192.0.2.100`, macOS, Chrome, Login Time 29/09/26 07:30, Last Activity 29/09/26 07:50); Online Users 6/25.
- Data Dinamis: tidak ada.
- Tabel "Sort per kelas kolom" (parameter langkah 10 sampai 15); klik 3 selalu kembali ke urutan default fixture #26:

  | Kolom | Klik 1 (Ascending `↑`) | Klik 2 (Descending `↓`) |
  |---|---|---|
  | User Name | Andi Pratama, Budi Santoso, Dewi Lestari, Rudi Hartono, Siti Rahma | Siti Rahma, Rudi Hartono, Dewi Lestari, Budi Santoso, Andi Pratama |
  | Email | Andi Pratama, Budi Santoso, Dewi Lestari, Rudi Hartono, Siti Rahma | Siti Rahma, Rudi Hartono, Dewi Lestari, Budi Santoso, Andi Pratama |
  | Position | Dewi Lestari, Rudi Hartono, Siti Rahma, Budi Santoso, Andi Pratama | Andi Pratama, Budi Santoso, Siti Rahma, Rudi Hartono, Dewi Lestari |
  | Division | Dewi Lestari, Siti Rahma, Rudi Hartono, Budi Santoso, Andi Pratama | Andi Pratama, Rudi Hartono, Budi Santoso, Siti Rahma, Dewi Lestari |
  | Device / OS | Andi Pratama, Rudi Hartono, Siti Rahma, Dewi Lestari, Budi Santoso | Dewi Lestari, Budi Santoso, Siti Rahma, Rudi Hartono, Andi Pratama |
  | Browser | Budi Santoso, Dewi Lestari, Andi Pratama, Rudi Hartono, Siti Rahma | Rudi Hartono, Siti Rahma, Andi Pratama, Dewi Lestari, Budi Santoso |
  | Login Time | Budi Santoso, Siti Rahma, Andi Pratama, Dewi Lestari, Rudi Hartono | Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso |
  | Last Activity | Budi Santoso, Andi Pratama, Siti Rahma, Dewi Lestari, Rudi Hartono | Rudi Hartono, Dewi Lestari, Siti Rahma, Andi Pratama, Budi Santoso |

- Konfigurasi kolom: TC-FA-LIC-271 menampilkan kolom `TAG` lewat Column Visibility; hook `after` menghapus preferensi kolom di browser (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, fixture BE pemulih, pemulihan konfigurasi kolom): dinyatakan sekali di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE yang memasang fixture sesi Pre-setup #14 (hook `before`), #26 (langkah 6), dan #30 (langkah 25) bergantian; mengirim tombol keyboard `Tab` dan membaca elemen yang sedang fokus serta atribut ARIA.

## Test Steps

### TC-FA-LIC-86: Urutan fokus keyboard Tabs Bar, toolbar, baris tabel, tombol aksi, paginator

1. Klik tab Concurrent User
2. Muat ulang halaman (F5) supaya fokus berada di awal halaman, lalu tekan Tab berulang
3. Verifikasi fokus berpindah berurutan: Tabs Bar, Search/Filter, baris tabel, tombol aksi individual, Paginator
4. Verifikasi kontainer tab memiliki role `tablist`
5. Verifikasi tiap tab memiliki `role="tab"` dengan atribut `aria-selected`

### Pindah ke fixture sesi Pre-setup #26

6. Terapkan fixture sesi Pre-setup #26 lewat fixture BE
7. Klik menu License pada sidebar, lalu tab Concurrent User

### TC-FA-LIC-270: Sort default Login Time terbaru lebih dulu

8. Verifikasi urutan awal tanpa mengklik header: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso
9. Verifikasi indikator sort aktif pada kolom `Login Time`

### TC-FA-LIC-268 dan TC-FA-LIC-269: Sort siklus 3-state per kelas kolom (alfabetis dan tanggal)

10. Untuk setiap baris tabel "Sort per kelas kolom" (langkah 10 sampai 15): klik header kolom pada baris itu sekali
11. Verifikasi urutan baris klik 1 sesuai tabel dengan indikator `↑`
12. Klik header kolom yang sama sekali lagi
13. Verifikasi urutan baris klik 2 sesuai tabel dengan indikator `↓`
14. Klik header kolom yang sama sekali lagi
15. Verifikasi urutan kembali ke default: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso

### TC-FA-LIC-271: Berpindah kolom mereset kolom sebelumnya dan tidak menghapus Search

16. Klik header kolom Actions `⋯`, lalu centang `TAG` pada overlay Column Visibility
17. Klik header `User Name` sekali
18. Klik header `TAG` sekali
19. Verifikasi kolom `User Name` kembali netral (indikator sort tidak aktif)
20. Verifikasi kolom `TAG` memulai dari Ascending (`↑`)
21. Ketik Search `Safari`, tekan Enter
22. Klik header `TAG` sekali lagi untuk mengubah arah sort
23. Verifikasi kata kunci Search `Safari` tidak direset: kotak Search tetap berisi `Safari` dan tabel tetap tersaring ke Rudi Hartono dan Siti Rahma
24. Klik header `TAG` sekali lagi hingga netral, lalu kosongkan isi kotak search, tekan Enter

### Pindah ke fixture sesi Pre-setup #30

25. Terapkan fixture sesi Pre-setup #30 lewat fixture BE
26. Klik menu License pada sidebar, lalu tab Concurrent User

### TC-FA-LIC-272: Sort IP Address siklus 3-state dengan basis numerik per oktet IPv4

27. Klik header kolom `IP Address` sekali
28. Verifikasi urutan klik 1 `↑`: `192.0.2.45` (Budi Santoso), `192.0.2.52` (Siti Rahma), `192.0.2.77` (Dewi Lestari), `192.0.2.100` (Dewi Lestari), `198.51.100.21` (Andi Pratama), `198.51.100.33` (Rudi Hartono)
29. Verifikasi `192.0.2.100` berada sesudah `192.0.2.77`, bukan sebelum `192.0.2.45`
30. Klik header kolom `IP Address` sekali lagi
31. Verifikasi urutan klik 2 `↓` kebalikan: `198.51.100.33`, `198.51.100.21`, `192.0.2.100`, `192.0.2.77`, `192.0.2.52`, `192.0.2.45`
32. Klik header kolom `IP Address` sekali lagi
33. Verifikasi urutan kembali ke default Login Time terbaru: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Dewi Lestari (sesi kedua), Budi Santoso

## Notes

- Langkah penghubung tanpa `Verifikasi`: dua blok "Pindah ke fixture sesi" (menukar fixture lalu membuka ulang tab lewat sidebar yang mereset Search, Sort, dan Filter), menampilkan kolom `TAG`, dan membersihkan sort serta Search di akhir TC-FA-LIC-271 (S-09).
- Blok ulang: langkah 10 sampai 15 dijalankan 8 kali (6 kolom alfabetis TC-FA-LIC-268 dan 2 kolom tanggal TC-FA-LIC-269). Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: semua blok adalah screening sort satu tabel dengan fixture sesi yang sama, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Fixture TC-FA-LIC-86 (Pre-setup #14, 18 sesi) dan TC-FA-LIC-272 (Pre-setup #30) berbeda dari fixture #26; fixture ditukar lewat langkah penghubung, bukan tersirat.
- Temuan untuk QA: TC-FA-LIC-271 mengklik header `TAG` padahal kolom `TAG` Hidden secara default (TC-FA-LIC-282 mencatat `TAG` tidak tercentang); spec menampilkan kolom `TAG` lebih dulu sebagai langkah penghubung. TC-FA-LIC-271 juga mengharapkan Search `Safari` tanpa menyebut hasil; spec mengasersi hasil `Safari` dari TC-FA-LIC-274 (Rudi Hartono, Siti Rahma). TC-FA-LIC-86 hanya menyebut "tombol aksi individual" tanpa nama tombol, sehingga spec mengasersi urutan kelas elemen saja.
