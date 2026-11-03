---
id: TC-AC-DC-E2E-057-resilience-delete-changelog-download
title: "Resilience: Kegagalan Server saat Delete, Gagal Memuat Changelog, dan Download Changelog Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-144
  - TC-AC-DC-154
  - TC-AC-DC-215
coverage:
  web: automated
---

# Resilience: Kegagalan Server saat Delete, Gagal Memuat Changelog, dan Download Changelog Gagal

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata).
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` melepas intercept yang masih terpasang dan mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE). Riwayat Changelog Pre-setup #17 dan General Settings Pre-setup #19 tidak dipakai langkah spec ini; Changelog yang dibuka memuat entri hasil seeding spec.
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-057`): `Daun {runId}-057` (leaf tanpa Device Name pengacu; TC-144, tidak terhapus). Hook `after` menghapus node itu lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: `Spectra.intercept()` memaksa error 500 pada endpoint delete Category (TC-144), endpoint Changelog Category (TC-154), dan endpoint download Changelog (TC-215); masing-masing intercept dilepas segera setelah pemicunya selesai (nama endpoint diambil tim FE dari `openapi.yaml` dan `low-level-design.md` modul; tidak dikarang di spec ini). Jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).
- Jeda nyata 5 detik (pilihan spec, bukan nilai TC) dipakai untuk mengamati bahwa toast error tidak hilang otomatis.

## Test Steps

### Kegagalan generik saat Delete (TC-144)

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `Daun {runId}-057`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog
6. Paksa endpoint delete Category mengembalikan error 500
7. Hover node `Daun {runId}-057`, klik aksi Delete
8. Klik `[Delete]` pada dialog konfirmasi
9. Verifikasi dialog konfirmasi menutup
10. Verifikasi toast error "Error, failed to delete category."
11. Tunggu 5 detik tanpa menutup toast
12. Verifikasi toast error masih tampil sampai ditutup manual
13. Lepas paksaan error endpoint delete Category
14. Klik tombol tutup pada toast error
15. Verifikasi node `Daun {runId}-057` tetap ada
16. Klik ikon Changelog pada header Sidebar Category
17. Ketik Search `Daun {runId}-057`, tekan Enter
18. Verifikasi jumlah baris hasil Search sama dengan baseline
19. Klik `[×]` pada modal Changelog

### Modal Changelog gagal memuat data (TC-154)

20. Paksa endpoint Changelog Category mengembalikan error 500
21. Klik ikon Changelog pada header Sidebar Category
22. Verifikasi modal menampilkan pesan "Unable to load this data."
23. Verifikasi tidak ada tombol `[Try Again]` pada modal
24. Verifikasi tidak ada teks "No changelog yet" pada modal
25. Lepas paksaan error endpoint Changelog Category
26. Klik `[×]` pada modal Changelog

### Download Changelog gagal (TC-215)

27. Klik ikon Changelog pada header Sidebar Category
28. Paksa endpoint download Changelog mengembalikan error
29. Klik ikon Download, pilih "Download as CSV"
30. Verifikasi toast error "Error, failed to download Changelog-Category."
31. Tunggu 5 detik tanpa menutup toast
32. Verifikasi toast error masih tampil sampai ditutup manual
33. Verifikasi tidak ada file terunduh
34. Lepas paksaan error endpoint download Changelog
35. Klik tombol tutup pada toast error
36. Klik `[×]` pada modal Changelog

## Notes

- Spec ini melewati sekitar 35 langkah (36) tipis. Ketiga TC adalah blok resilience satu kelas harness (kelas b, intercept parsial) yang berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5, 19, 26, 36 (menutup modal Changelog), langkah 6, 13, 20, 25, 28, 34 (memasang dan melepas paksaan error endpoint segera setelah pemicunya selesai, S-09), langkah 11, 31 (jeda 5 detik pilihan spec untuk mengamati toast yang tidak hilang otomatis), langkah 14 dan 35 (menutup toast error manual). Search pada modal Changelog (langkah 3, 17) menemukan entri berdasarkan nama bersuffix unik.
- S-05: klausa "tidak ada entri log" pada TC-144 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4 dan 18), bukan asersi absence kelas g.
- Verifikasi absence "tidak ada file terunduh" (langkah 33) memakai toast error (langkah 30) sebagai anchor positif bahwa respons gagal sudah diproses.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Daun` sebagai target Delete. Spec memakai `Daun {runId}-057` milik spec.
  - Riwayat Changelog Pre-setup #17 dan General Settings Pre-setup #19 disebut sebagai precondition TC-154 dan TC-215 tetapi tidak dipakai Expected; spec tidak memakainya.
  - TC-215 memakai "Download as CSV" sebagai satu-satunya format yang dipaksa gagal; kegagalan "Download as XLSX" tidak diuji.
