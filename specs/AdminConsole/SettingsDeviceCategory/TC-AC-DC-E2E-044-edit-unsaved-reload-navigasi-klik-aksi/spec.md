---
id: TC-AC-DC-E2E-044-edit-unsaved-reload-navigasi-klik-aksi
title: "Edit Category: Reload, Navigasi Internal, dan Klik Aksi Node Lain dengan Input Berisi Perubahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-120
  - TC-AC-DC-121
  - TC-AC-DC-261
coverage:
  web: automated
---

# Edit Category: Reload, Navigasi Internal, dan Klik Aksi Node Lain dengan Input Berisi Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-044`): `Pemindai {runId}-044` (target Edit; namanya tidak berubah selama spec) dan `Saudara {runId}-044` (node lain sebagai sasaran klik aksi). Hook `after` menghapus keduanya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `Draft Edit` (tidak pernah disimpan sehingga tidak bersuffix).
- Kemampuan teknis: dialog `beforeunload` bawaan browser dapat ditangani oleh skrip (diterima untuk melanjutkan reload atau dibatalkan untuk tetap di halaman) dan kemampuan itu disediakan tim FE. Item menu navigasi lain pada sidebar aplikasi (TC-121) tidak disebut TC; tujuannya dipilih tim FE. Jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-044`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Reload saat input Edit berisi perubahan (TC-120)

6. Hover node `Pemindai {runId}-044`, klik aksi Edit
7. Ubah nilai menjadi `Draft Edit`, tekan F5
8. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul sebelum halaman dimuat ulang
9. Pilih tetap di halaman pada konfirmasi browser
10. Verifikasi input Edit tetap terbuka dengan nilai `Draft Edit`

### Navigasi internal: Cancel lalu Leave (TC-121)

11. Klik item menu navigasi lain di sidebar aplikasi
12. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
13. Klik `[Cancel]`
14. Verifikasi pengguna tetap di halaman Settings > Device > Device Name
15. Verifikasi input Edit terbuka berisi `Draft Edit`
16. Klik item menu navigasi yang sama di sidebar aplikasi
17. Klik `[Leave]`
18. Verifikasi navigasi berlanjut ke halaman tujuan

### Klik aksi pada node lain: Leave (TC-261)

19. Buka Settings > Device > Device Name, lalu expand `Hardware` dan `Handheld Reader`
20. Verifikasi nama node tetap `Pemindai {runId}-044`
21. Hover node `Pemindai {runId}-044`, klik aksi Edit
22. Ubah nilai menjadi `Draft Edit`
23. Hover node `Saudara {runId}-044`, klik aksi Edit
24. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
25. Klik `[Leave]`
26. Verifikasi input Edit pada `Pemindai {runId}-044` tertutup
27. Verifikasi nama node tetap `Pemindai {runId}-044`

### Pemeriksaan akhir tidak ada entri baru

28. Klik ikon Changelog pada header Sidebar Category
29. Ketik Search `{runId}-044`, tekan Enter
30. Verifikasi jumlah baris hasil Search sama dengan baseline
31. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 dan 19 (membuka cabang tree; langkah 19 juga kembali ke halaman Device Name setelah navigasi), langkah 5 dan 31 (menutup modal Changelog), langkah 16 (klik item menu yang sama untuk mengulang navigasi setelah Cancel).
- Input Edit pada langkah 6 sampai 15 dibiarkan terbuka dengan `Draft Edit` oleh TC-120 dan dipakai sebagai input dirty untuk TC-121, sehingga `Draft Edit` tidak diketik ulang; sesudah langkah 18 halaman ditinggalkan sehingga input dirty itu berakhir lewat `[Leave]`.
- S-05: klausa "nama node tidak berubah dan tidak ada entri log" pada TC-121 dan TC-261 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 20, 27, 30), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC-121 menyebut "item menu navigasi lain di sidebar aplikasi" tanpa nama item; tujuan dipilih tim FE.
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` dan `Barcode Handheld`. Spec memakai node milik spec.
  - Nama node pada TC-120 dan TC-121 tidak teramati saat input terbuka karena label node digantikan input; spec mengasersinya setelah kembali ke halaman (langkah 20).
