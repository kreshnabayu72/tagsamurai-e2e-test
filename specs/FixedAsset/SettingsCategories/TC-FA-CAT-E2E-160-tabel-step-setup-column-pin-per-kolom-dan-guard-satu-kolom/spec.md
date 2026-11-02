---
id: TC-FA-CAT-E2E-160-tabel-step-setup-column-pin-per-kolom-dan-guard-satu-kolom
title: "Tabel Step Category Consolidation: Pin dan Unpin Tiap Kolom lewat Setup Column dengan Persistensi, serta Guard Satu Kolom Tersisa"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-568
  - TC-FA-CAT-571
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Pin dan Unpin Tiap Kolom lewat Setup Column dengan Persistensi, serta Guard Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection) hanya dibaca: 8 kategori root `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`.
- Kolom yang di-Pin pada langkah 2 sampai 8 (langkah diulang untuk setiap baris tabel): `Category Name`, `Code`, `Depth`, `Total Asset`, `Status`, `Modified By`, `Last Updated`.
- Kemampuan teknis: lebar viewport browser dibuat cukup sempit agar tabel Step dapat di-scroll horizontal (lebar tidak disebut TC; lihat Temuan untuk QA).
- State yang diubah spec: Pin kolom tabel Step (disimpan lewat `[Save]`). Tiap kolom di-unpin lagi pada langkah 7; konfigurasi kolom dipulihkan dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) di hook `after` suite; kemampuan disediakan tim FE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

1. Klik `[Choose Categories]` pada Alert Category Consolidation

### TC-FA-CAT-568: Pin dan unpin kolom tabel Step lewat popup dan persist (untuk setiap kolom pada tabel Kolom yang di-Pin, langkah 2 sampai 8)

2. Klik header Actions (⋯) > `Setup Column...`, klik icon Pin pada kolom, lalu klik `[Save]`
3. Scroll tabel Step secara horizontal
4. Verifikasi kolom itu tetap di kiri saat scroll horizontal
5. Tekan F5, klik `[Choose Categories]` pada Alert Category Consolidation, lalu scroll tabel Step secara horizontal
6. Verifikasi Pin kolom itu bertahan setelah F5 (kolom tetap di kiri saat scroll horizontal)
7. Klik header Actions (⋯) > `Setup Column...`, klik icon Pin pada kolom itu sekali lagi (unpin), klik `[Save]`, lalu scroll tabel Step secara horizontal
8. Verifikasi kolom itu ikut scroll setelah unpin

### TC-FA-CAT-571: Guard satu kolom tersisa, checkbox disabled dengan tooltip

9. Klik header Actions (⋯) > `Setup Column...`
10. Hilangkan centang semua kolom kecuali `Category Name`
11. Hover checkbox kolom `Category Name`
12. Verifikasi checkbox kolom `Category Name` disabled
13. Verifikasi tooltip `At least one column must remain visible.`
14. Tutup popup Setup Column lewat icon close (✕) tanpa menyimpan

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (14 langkah nominal, Pin tujuh kolom diulang: 7 langkah x 7 = 49, total sekitar 56). Alasan: seluruh blok satu kelas fungsional pada popup Setup Column tabel Step yang sama, berdiri sendiri, dan langkah Pin identik per kolom dengan parameter di butir `Kolom yang di-Pin` (bagian 8b butir 7). Langkah yang diulang: 2 sampai 8.
- Langkah penghubung (S-03, S-09): langkah 1 (membuka wizard), langkah 5 (membuka wizard sesudah F5), langkah 14 (menutup popup tanpa menyimpan).
- Langkah 7 menggabungkan unpin, Save, dan scroll sesuai langkah 4 TC-FA-CAT-568; hasil unpin diasersi pada langkah 8.
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-568 tidak menyebut lebar viewport; scroll horizontal hanya bermakna bila tabel melebihi lebar layar, sehingga viewport sempit menjadi kebutuhan teknis.
  - TC-FA-CAT-568 tidak menyebut cara mengamati "Pin bertahan setelah F5"; spec mengamatinya lewat posisi kolom saat scroll horizontal (urutan langkah 4 TC memasukkan F5 sebelum unpin).
  - TC-FA-CAT-568 langkah 4 ("Tekan F5") tidak menyebut membuka kembali wizard; spec menambah klik `[Choose Categories]` pada langkah 5.
