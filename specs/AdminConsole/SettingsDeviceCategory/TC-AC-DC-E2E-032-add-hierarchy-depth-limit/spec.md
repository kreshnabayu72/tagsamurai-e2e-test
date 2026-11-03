---
id: TC-AC-DC-E2E-032-add-hierarchy-depth-limit
title: "Add Subcategory: Batas Hierarchy Depth Limit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-91
  - TC-AC-DC-92
coverage:
  web: automated
---

# Add Subcategory: Batas Hierarchy Depth Limit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- State global yang diubah: Hierarchy Depth Limit entitas uji (Pre-setup #18, nilai awal 50) diset 5 di hook `before` spec ini dan dipulihkan ke 50 di hook `after`. Kemampuan mengubah Hierarchy Depth Limit pada Lifecycle Settings lewat sesi API aktor disediakan tim FE/BE (TC tidak menyebut endpoint; tidak dikarang di spec ini). Suite berjalan serial.
- Data Pre-setup #14 hanya dibaca dan tidak diubah: rantai `Hardware` > `Smart Fixed Reader` > `Rantai L3` > `Rantai L4` > `Rantai L5` (kedalaman 3 sampai 5). Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec: `Batas Lima {runId}-032` (dibuat TC-92 di bawah `Rantai L4`); dihapus di hook `after` lewat sesi API aktor. Entri Changelog hasil cleanup bersifat permanen dan tidak dihapus.

## Test Steps

### Add pada parent di batas limit diblokir (TC-91)

1. Expand `Hardware`, `Smart Fixed Reader`, `Rantai L3`, `Rantai L4` sampai `Rantai L5` terlihat
2. Hover node `Rantai L5` (kedalaman 5), klik aksi `+ Subcategory`
3. Verifikasi dialog blok dengan judul "Cannot Add Category", isi "You've reached the platform limit of 5 levels. Contact support if you need a higher limit.", dan satu tombol `[OK]`
4. Klik `[OK]`
5. Verifikasi input inline Add tidak dibuka
6. Verifikasi tidak ada node baru di bawah `Rantai L5`

### Add pada parent satu tingkat di bawah limit berhasil (TC-92)

7. Hover node `Rantai L4` (kedalaman 4), klik aksi `+ Subcategory`
8. Verifikasi input inline Add terbuka
9. Verifikasi tidak ada dialog blok
10. Ketik `Batas Lima {runId}-032`, klik `[Submit]`
11. Verifikasi toast sukses "Success, category has been created."
12. Verifikasi node `Batas Lima {runId}-032` (kedalaman 5) muncul di bawah `Rantai L4`

## Notes

- S-03, langkah penghubung: langkah 4 (menutup dialog blok dengan `[OK]` yang juga diasersi sebagai bagian Expected TC-91).
- Verifikasi absence pada langkah 6 memakai dialog blok pada langkah 3 dan node `Rantai L5` yang terlihat sebagai anchor positif.
- Temuan untuk QA:
  - TC-91 mengharapkan "tidak ada node baru" tanpa menyebut entri log; spec tidak mengasersi log.
  - Mekanisme pengaturan Hierarchy Depth Limit (Lifecycle Settings) untuk precondition TC-91 dan TC-92 tidak disebut TC; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
