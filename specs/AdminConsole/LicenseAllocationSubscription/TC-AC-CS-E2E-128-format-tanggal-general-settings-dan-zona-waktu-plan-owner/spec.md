---
id: TC-AC-CS-E2E-128-format-tanggal-general-settings-dan-zona-waktu-plan-owner
title: "Format Tanggal General Settings dan Zona Waktu Plan Owner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-470
  - TC-AC-CS-471
  - TC-AC-CS-473
coverage:
  web: automated
---

# Format Tanggal General Settings dan Zona Waktu Plan Owner

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun ganti akun di tengah spec (Test Steps memuat langkah Logout dan login eksplisit): Total Control Distributor (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data Pre-setup baca-saja: `SUBS-20260101-00001` (#61: Client PT Sejahtera, FAMS, Professional, Active, 01/01/26 sampai 31/12/26, Plan Owner PT Maju Bersama); entri Changelog seed (Pre-setup #84) bercap `2026-08-19 11:50` UTC+07:00, dirujuk lewat `Fixture.license-allocation-subscription.changelogEntry1150`.
- Data milik spec (TC-AC-CS-473): Client baru milik spec `Client Zona Waktu+{runId}-128` untuk Add Subscription Distributor, dibuat lewat API di hook `before` dan dibersihkan di hook `after` bersama term yang dibuat (S-06, S-12).
- State global yang diubah (suite serial): General Settings Principal PT ABC (Date Format `dd/MM/yy` menjadi `M/d/yy`, Time Format 24-hour menjadi 12-hour, Timezone `Asia/Jakarta UTC+07:00` tetap), serta jam server dan jam browser (TC-AC-CS-473, absolut `19/08/26 00:30` Asia/Jakarta, tanggal acuan uji `19/08/26`). General Settings dipulihkan ke `dd/MM/yy` dan 24-hour oleh fixture backend yang disediakan tim FE/BE di hook `after`; jam dipulihkan di langkah penghubung dan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): mengatur Date Format dan Time Format General Settings; mengatur jam server dan jam browser absolut (fixture waktu); membuat Client lewat API.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-470: Format tanggal General Settings pada tabel List dan input filter tanggal

1. Atur Date Format `M/d/yy` dan Time Format 12-hour pada General Settings Principal PT ABC hingga tersimpan
2. Klik menu `Client Subscription` di sidebar
3. Ketik Search `SUBS-20260101-00001`, tekan Enter
4. Verifikasi kolom Start Date baris `SUBS-20260101-00001` menampilkan `1/1/26`
5. Verifikasi kolom End Date baris `SUBS-20260101-00001` menampilkan `12/31/26`
6. Klik ikon Filter
7. Pilih Start Date rentang `1/1/26` sampai `1/1/26`
8. Verifikasi input filter date picker menampilkan tanggal terpilih dalam format `M/d/yy`
9. Kosongkan filter Start Date dan tutup Filter Panel
10. Klik `(←)` pada kotak Search

### TC-AC-CS-471: Format tanggal dan zona waktu pada Modal Changelog

11. Klik ikon Changelog
12. Buka filter Date dan pilih rentang tanggal `8/19/26` sampai `8/19/26`
13. Verifikasi kolom Date entri seed `2026-08-19 11:50` UTC+07:00 menampilkan `8/19/26 11:50 AM` pada zona Asia/Jakarta
14. Verifikasi input filter Date memakai format tanggal `M/d/yy`
15. Klik `[✕]` pada Modal Changelog

### TC-AC-CS-473: Perbandingan Start Date memakai zona waktu General Settings plan owner

16. Logout
17. Login sebagai Total Control Distributor `Eko Saputra`
18. Buka menu `Allocation > Client Subscription`
19. Atur jam server dan jam browser ke `19/08/26 00:30` Asia/Jakarta
20. Klik `[+ Subscription]`
21. Pilih Client milik spec, Product, dan Plan
22. Isi Duration `1` dan Start Date `19/08/26`
23. Klik `[Submit]`
24. Tunggu aksi selesai (dialog/modal tertutup)
25. Ketik Search `Client Zona Waktu+{runId}-128`, tekan Enter
26. Verifikasi Start Date `19/08/26` diterima sebagai hari ini (tanpa error validasi Start Date)
27. Verifikasi term hasil Submit berstatus Active (bukan Pending)
28. Verifikasi tampilan tanggal term mengikuti zona waktu tampilan staf yang login
29. Pulihkan jam server dan jam browser

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-484, 485, dan 487 (konfigurasi platform yang dibaca live) ada di spec 160.
- Urutan TC berbeda dari urutan sumber (470, 471, 473): TC-AC-CS-473 dijalankan terakhir supaya hanya terjadi satu pergantian akun (S-07).
- Langkah penghubung (S-03): langkah 2 (memuat ulang List sesudah mengubah General Settings), langkah 3 (Search untuk menemukan baris target, R-16), langkah 9 dan 10 (mengosongkan filter dan Search), langkah 12 (Filter Date Changelog ke 19/08/26 supaya entri seed tampil di halaman pertama; dipindah sebelum langkah 13 yang memverifikasinya), langkah 15 (menutup modal), langkah 18 (membuka List sesudah login), langkah 24 (menunggu aksi selesai), langkah 25 (Search untuk menemukan term milik spec, R-16), dan langkah 29 (memulihkan jam sebelum aksi berikutnya, S-09).
- Langkah 16 dan 17 adalah ganti akun eksplisit (Logout sebagai bagian ganti akun).
- Temuan untuk QA:
  - TC-AC-CS-471 tidak menyebut entri Changelog mana yang bercap `2026-08-19 11:50`; spec memakai entri seed yang disediakan tim FE/BE (S-13).
  - TC-AC-CS-473 Expected c ("Tampilan tanggal tetap mengikuti zona staf") tidak menyebut zona tampilan staf maupun nilai tanggal yang tampil; asersi ditulis tanpa nilai (S-02).
  - TC-AC-CS-473 tidak menyebut Pay From dan nilai Plan/Client; spec memakai data milik spec dan nilai bawaan form.
  - TC-AC-CS-473 Expected a tidak menyebut toast sukses; spec tidak mengasersinya.
  - TC-AC-CS-470 dan TC-AC-CS-471 menyebut pengubahan General Settings sebagai precondition tanpa langkah; spec memakai kemampuan yang disediakan tim FE/BE.
