---
id: TC-AC-DS-E2E-158-sinkron-realtime-sesi-lain-register-edit-delete
title: "Sinkron Realtime: Register, Edit, dan Delete oleh Sesi Lain Tercermin pada List tanpa Muat Ulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-509
  - TC-AC-DS-510
  - TC-AC-DS-511
coverage:
  web: automated
---

# Sinkron Realtime: Register, Edit, dan Delete oleh Sesi Lain Tercermin pada List tanpa Muat Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua: Total Control Principal kedua (Budi Kurniawan, Modified By `Budi K`): `totalControlSku2_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC2_PASSWORD` (Pre-setup #2). Dijalankan lewat sesi API aktor (tidak dihitung sesi web); sesi UI pertama (akun #1) yang diasersi. Sesi API aktor (login API password, tidak dihitung sesi web) disediakan tim BE/FE sesuai `suite.md`.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35).
- Data Dinamis (kode literal pada Tabel Data Uji Dinamis TC): SKU `SSE-NEW-01` (Data Dinamis #35) dibuat pelaku kedua; hook `before` menghapus sisa kode itu bila ada dan hook `after` menghapusnya. Target Edit `HHR-ARC-200` dan target Delete `TAG-ARC-OBJ` (Pre-setup #29) dipulihkan fixture BE.
- Pemulihan Pre-setup yang diubah spec (SKU, stok, nama master) ke keadaan awal dilakukan fixture BE yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC; entri Changelog, System Log, dan Activity Log yang terbentuk bersifat permanen (lihat Temuan untuk QA).
- Penantian propagasi: List diamati sampai 10 detik tanpa muat ulang (nilai TC).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-509: Register SKU oleh sesi lain muncul pada List tanpa muat ulang

1. Dengan sesi API pelaku kedua (#2) daftarkan SKU `SSE-NEW-01` (Asset TAG, foto `foto-a.jpg`) hingga tersimpan
2. Amati List sesi pertama tanpa interaksi dan tanpa muat ulang sampai 10 detik
3. Verifikasi baris `SSE-NEW-01` muncul pada List sesi pertama tanpa muat ulang
4. Verifikasi posisi halaman, Search, dan Filter yang aktif tidak berubah (halaman 1, tanpa Search dan tanpa Filter)

### TC-AC-DS-510: Edit SKU oleh sesi lain tercermin pada List tanpa muat ulang

5. Ketik Search `HHR-ARC-200`, tekan Enter
6. Dengan sesi API pelaku kedua (#2) ubah Model/Type `HHR-ARC-200` menjadi `H-SSE` hingga tersimpan
7. Amati List sesi pertama tanpa muat ulang sampai 10 detik
8. Verifikasi badge Model/Type baris `HHR-ARC-200` pada sesi pertama berubah menjadi `H-SSE` tanpa muat ulang

### TC-AC-DS-511: Delete SKU oleh sesi lain menghilangkan baris pada List tanpa muat ulang

9. Ganti isi kotak search dengan `TAG-ARC-OBJ`, tekan Enter
10. Verifikasi baris `TAG-ARC-OBJ` tampil pada List sesi pertama
11. Dengan sesi API pelaku kedua (#2) hapus SKU `TAG-ARC-OBJ` hingga tersimpan
12. Amati List sesi pertama tanpa muat ulang sampai 10 detik
13. Verifikasi baris `TAG-ARC-OBJ` hilang dari List sesi pertama tanpa muat ulang (Search menampilkan "No results found")
14. Klik `(←)` pada kotak Search; pulihkan `HHR-ARC-200` dan `TAG-ARC-OBJ` ke keadaan awal Pre-setup lewat fixture BE

## Notes

- Pelaku kedua memakai sesi API karena hanya memicu perubahan state; hasil diasersi di sesi pertama (keputusan 2026-10-21 dan 2026-10-30), sehingga tidak ada butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung tanpa `Verifikasi`: Search untuk menemukan baris target (R-16) dan langkah 14 (pemulihan data dan penutupan Search, S-09).
- Temuan untuk QA:
  - TC 509 Expected menyebut "tanpa mengubah posisi halaman, Search, atau Filter yang aktif" tetapi langkah TC tidak menyetel halaman, Search, atau Filter aktif; spec memakai keadaan default (halaman 1, tanpa Search dan Filter) sehingga asersi "tidak berubah" lemah.
  - TC 509 sampai 511 diberi Automation Manual Only (d) di TC (dua sesi paralel); spec menjalankannya sebagai FE+BE dengan pelaku kedua lewat sesi API.
  - Absence 511 memakai Verifikasi baris tampil sebelum pemicu sebagai anchor.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
