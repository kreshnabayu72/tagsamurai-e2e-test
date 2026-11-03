---
id: TC-AC-ACHA-E2E-021-alokasi-id-urutan-dan-reset-tanggal
title: "Allocation ID: Nomor Urut Sekuensial pada Hari yang Sama dan Reset pada Pergantian Tanggal Server"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-146
  - TC-AC-ACHA-147
coverage:
  web: automated
---

# Allocation ID: Nomor Urut Sekuensial pada Hari yang Sama dan Reset pada Pergantian Tanggal Server

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `PT ABC` (Admin Pratama, Pre-setup #21), `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, `AC_TC_PASSWORD`). Password tidak ditulis di spec.
- Data Pre-setup: Client #10 `PT Manufaktur Unggul`. Principal tanpa wallet sehingga tidak ada saldo yang berubah.
- Data Dinamis: empat alokasi `Completed` dibuat (Category NFC, Client `PT Manufaktur Unggul`, Quantity 1 untuk semuanya). Efek: kuota NFC Client `PT Manufaktur Unggul` bertambah 4; modul tanpa Delete sehingga alokasi tidak dihapus.
- State global: jam server digeser lewat fixture API Pre-setup #20 (disediakan tim FE/BE; mekanisme tidak tertulis di TC) ke `22 Dec 2026 10:00` (UTC+7) pada blok pertama, ke `22 Dec 2026 23:59` pada blok kedua, lalu `23 Dec 2026 00:01`. Hanya jam server yang digeser: nomor urut Allocation ID dihitung di server dan UI tidak diasersi berbasis jam klien. Jam server dipulihkan di hook `after` yang tetap berjalan walau spec gagal.
- Kondisi data: belum ada transaksi bertanggal `22 Dec 2026` dan `23 Dec 2026` pada tiap awal blok (fixture API Pre-setup #20 memastikan dan memulihkannya; hook `before` dan langkah penghubung antar blok); tanpa kondisi ini nomor urut berbeda dari Expected.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server (state global).
- Kemampuan teknis: kemampuan membaca Allocation ID dari baris teratas List; sesi UI dan sesi API aktor tetap valid selama jam server digeser (dinyatakan di `suite.md`).
- Hook suite: flag Guided Tooltip, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column, dan seed 30 baris dinyatakan di `suite.md`. Hook `after` memulihkan jam server dan seed lewat fixture Pre-setup #20 (Lampiran A butir A-11).

## Test Steps

### Nomor urut sekuensial pada hari yang sama (TC-AC-ACHA-146)

1. Geser jam server ke `22 Dec 2026 10:00` (UTC+7) lewat fixture API Pre-setup #20; pastikan belum ada transaksi bertanggal `22 Dec 2026`
2. Buka Allocation > Device Allocation
3. Klik `[+ Allocation]`
4. Pilih Category `TAG - NFC`, Client `PT Manufaktur Unggul`, isi Quantity `1`
5. Klik `[Submit]` (alokasi pertama)
6. Verifikasi Allocation ID pada baris teratas List adalah `HALC-20261222-00001`
7. Klik `[+ Allocation]`
8. Pilih Category `TAG - NFC`, Client `PT Manufaktur Unggul`, isi Quantity `1`
9. Klik `[Submit]` (alokasi kedua dengan isian yang sama)
10. Verifikasi Allocation ID pada baris teratas List adalah `HALC-20261222-00002` (nomor urut sekuensial 5 digit)

### Reset nomor urut pada pergantian tanggal server (TC-AC-ACHA-147)

11. Kembalikan state tanggal: pastikan belum ada transaksi bertanggal `22 Dec 2026` dan `23 Dec 2026` lewat fixture API Pre-setup #20
12. Geser jam server ke `22 Dec 2026 23:59` (UTC+7) lewat fixture API Pre-setup #20
13. Buka Allocation > Device Allocation
14. Klik `[+ Allocation]`
15. Pilih Category `TAG - NFC`, Client `PT Manufaktur Unggul`, isi Quantity `1`
16. Klik `[Submit]` (alokasi pertama)
17. Verifikasi Allocation ID pada baris teratas List adalah `HALC-20261222-00001`
18. Geser jam server ke `23 Dec 2026 00:01` (UTC+7) lewat fixture API Pre-setup #20
19. Klik `[+ Allocation]`
20. Pilih Category `TAG - NFC`, Client `PT Manufaktur Unggul`, isi Quantity `1`
21. Klik `[Submit]` (alokasi kedua)
22. Verifikasi Allocation ID pada baris teratas List adalah `HALC-20261223-00001` (nomor urut direset ke `00001` pada tanggal baru)
23. Pulihkan jam server ke waktu nyata lewat fixture API Pre-setup #20

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec ini kelas d (harness eksternal: time-travel jam server); TC-146 dan TC-147 sama-sama kelas d dan berbagi harness yang sama sehingga berada dalam satu spec.
- Jam server dipulihkan di akhir spec dan di hook `after`.
- Urutan blok geser jam (S-10): kedua blok (TC-146, TC-147) menggeser jam server dan mengikuti nomor TC; tidak ada blok non-jam yang perlu dipindah ke awal. Jam dipulihkan di langkah 23 dan di hook `after` (suite.md), dan blok kedua dimulai dari state tanggal yang dipulihkan fixture (langkah 11) sehingga efek pergeseran jam blok pertama pada transaksi lain dinetralkan sebelum blok kedua.
- Langkah penghubung (S-03): penyetelan jam server dan penyiapan state tanggal lewat fixture, pembukaan halaman Device Allocation sesudah perubahan jam, serta pemulihan jam di akhir spec.
- TC-146 dan TC-147 memakai tanggal yang sama (`22 Dec 2026`) sehingga Expected `HALC-20261222-00001` pada TC-147 hanya terpenuhi bila transaksi bertanggal `22 Dec 2026` dari TC-146 tidak ada; spec menuliskan langkah penghubung "pastikan belum ada transaksi bertanggal ..." sebagai kemampuan fixture yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Pengecualian S-12 nama literal: nama Client Pre-setup literal (sudah ada di environment); Allocation ID literal di Expected TC (`HALC-20261222-00001`, `HALC-20261222-00002`, `HALC-20261223-00001`) disalin dari TC karena tanggal server digeser.
- Temuan untuk QA:
  - TC-146 dan TC-147 menggunakan tanggal yang sama dan keduanya mengharapkan nomor urut `00001`; tanpa penghapusan atau penyaringan transaksi bertanggal 22 Dec 2026 di antara kedua TC, TC-147 mendapatkan `00003`. Fixture Pre-setup #20 hanya mendefinisikan "pergeseran jam server"; kemampuan membersihkan transaksi bertanggal uji tidak tertulis.
  - Run berulang pada environment yang sama juga membuat transaksi bertanggal 22 Dec 2026 dan 23 Dec 2026 yang tidak dapat dihapus (tanpa Delete); precondition "belum ada transaksi pada tanggal itu" tidak dapat dipenuhi tanpa kemampuan pembersihan yang disediakan tim BE.
  - TC-147 Expected tidak menyebut apakah jam browser juga digeser; spec hanya menggeser jam server.
  - Post Condition kedua TC (kuota Client, panel Stock Balance Summary) tidak punya langkah observasi di TC dan tidak diasersi.
