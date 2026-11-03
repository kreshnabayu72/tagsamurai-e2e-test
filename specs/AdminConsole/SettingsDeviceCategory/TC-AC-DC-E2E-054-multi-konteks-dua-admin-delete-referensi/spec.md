---
id: TC-AC-DC-E2E-054-multi-konteks-dua-admin-delete-referensi
title: "Dua Admin: Referensi Device Name Muncul Setelah Dialog Delete Terbuka"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-139
  - TC-AC-DC-275
coverage:
  web: automated
---

# Dua Admin: Referensi Device Name Muncul Setelah Dialog Delete Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Admin kedua (Pre-setup #9, Maya Putri, Total Control Principal, berhak membuat Device Name): `totalControlDevCat2_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DC_TC2_PASSWORD` (nama env baru; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`, satu arti: password Total Control kedua Admin Console Settings Device Category). Admin kedua bertindak lewat sesi API aktor (hanya memicu perubahan state; tidak ada konteks UI kedua).
- Login akun aktor pertama di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-054`): `Daun {runId}-054` (leaf; TC-139) dan family `Keluarga Fam {runId}-054F` dengan anak `Anak A Fam {runId}-054F` (leaf) dan `Anak B Fam {runId}-054F`, serta cucu `Cucu Fam {runId}-054F` di bawah `Anak B Fam {runId}-054F` (TC-275). Device Name `RACE-1 {runId}-054` (Category `Daun {runId}-054`) dan `DEEP-2 {runId}-054` (Category `Cucu Fam {runId}-054F`) dibuat admin kedua selama spec. Hook `after` menghapus kedua Device Name lalu node milik spec beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: pembuatan Device Name oleh admin kedua lewat sesi API (kolom wajib selain Category tidak disebut TC; disediakan tim FE/BE tanpa endpoint karangan). Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### Referensi muncul setelah cek awal pada leaf (TC-139)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Daun {runId}-054`, klik aksi Delete
3. Admin kedua (sesi API) membuat Device Name `RACE-1 {runId}-054` dengan Category `Daun {runId}-054` hingga tersimpan
4. Tunggu aksi admin kedua selesai
5. Klik `[Delete]` pada dialog konfirmasi
6. Verifikasi dialog blok "Cannot Delete Category" memuat bullet `RACE-1 {runId}-054` dan satu tombol `[OK]`
7. Klik `[OK]`
8. Verifikasi node `Daun {runId}-054` tetap ada
9. Verifikasi tidak ada toast tambahan

### Referensi pada cucu muncul setelah cek awal (TC-275)

10. Expand `Keluarga Fam {runId}-054F` dan `Anak B Fam {runId}-054F`
11. Hover node `Keluarga Fam {runId}-054F`, klik aksi Delete
12. Admin kedua (sesi API) membuat Device Name `DEEP-2 {runId}-054` dengan Category `Cucu Fam {runId}-054F` hingga tersimpan
13. Tunggu aksi admin kedua selesai
14. Klik `[Delete]` pada dialog konfirmasi
15. Verifikasi dialog blok "Cannot Delete Category" memuat bullet `DEEP-2 {runId}-054` dan satu tombol `[OK]`
16. Klik `[OK]`
17. Verifikasi `Keluarga Fam {runId}-054F`, `Anak A Fam {runId}-054F`, `Anak B Fam {runId}-054F`, dan `Cucu Fam {runId}-054F` tetap ada
18. Verifikasi tidak ada toast tambahan
19. Klik ikon Changelog pada header Sidebar Category
20. Ketik Search `{runId}-054`, tekan Enter
21. Verifikasi entri `Create` hasil seeding untuk `Daun {runId}-054` tampil
22. Verifikasi tidak ada entri `Delete` untuk Category milik spec ini (anchor: entri `Create` hasil seeding untuk `Daun {runId}-054` tampil)
23. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 dan 10 (membuka cabang tree), langkah 4 dan 13 (menunggu aksi admin kedua selesai sebelum aksi sesi pertama), langkah 7 dan 16 (`[OK]` menutup dialog blok, bagian Expected TC), langkah 23 (menutup modal Changelog). Search pada modal Changelog (langkah 20) menemukan entri berdasarkan nama bersuffix unik.
- Pelaku kedua memakai sesi API (langkah 3 dan 12) karena hanya memicu perubahan state dan hasil di sesi itu tidak diasersi.
- S-05: klausa "tidak ada entri log" pada TC-139 dan TC-275 dinyatakan sebagai asersi nama bersuffix unik (langkah 22), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Daun` dan `Hapus Keluarga` serta Device Name `RACE-1` dan `DEEP-2`. Spec memakai node dan Device Name milik spec bersuffix `{runId}-054`; teks bullet pada dialog memuat nama Device Name bersuffix.
  - TC-139 dan TC-275 ditandai `Manual Only (d)`; dua pelaku tidak menghambat penulisan.
