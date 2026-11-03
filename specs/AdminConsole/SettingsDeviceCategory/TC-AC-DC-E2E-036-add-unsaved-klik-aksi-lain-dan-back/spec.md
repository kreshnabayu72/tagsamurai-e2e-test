---
id: TC-AC-DC-E2E-036-add-unsaved-klik-aksi-lain-dan-back
title: "Add Subcategory: Dialog Unsaved Changes saat Klik Aksi Node Lain, Klik Area Luar Tree, dan Tombol Back Browser"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-259
  - TC-AC-DC-260
  - TC-AC-DC-267
coverage:
  web: automated
---

# Add Subcategory: Dialog Unsaved Changes saat Klik Aksi Node Lain, Klik Area Luar Tree, dan Tombol Back Browser

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-036`): `Induk {runId}-036` dengan satu anak `Anak Awal {runId}-036` (node lain sebagai sasaran klik aksi dan pembanding). Hook `after` menghapus `Induk {runId}-036` beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `Draft Name` (tidak pernah disimpan sehingga tidak bersuffix).
- Kemampuan teknis: halaman Admin Console lain yang dibuka sebelum Settings > Device (riwayat untuk tombol Back browser) dipilih tim FE karena TC tidak menyebut halamannya. Jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Persiapan riwayat browser dan baseline Changelog

1. Buka halaman Admin Console lain sebagai halaman sebelumnya untuk tombol Back browser
2. Buka Settings > Device > Device Name
3. Expand `Hardware` lalu `Handheld Reader`
4. Klik ikon Changelog pada header Sidebar Category
5. Ketik Search `{runId}-036`, tekan Enter
6. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
7. Klik `[×]` pada modal Changelog

### Klik aksi pada node lain: Leave (TC-259)

8. Hover node `Induk {runId}-036`, klik aksi `+ Subcategory`
9. Ketik `Draft Name` pada input
10. Hover node `Anak Awal {runId}-036`, klik aksi `+ Subcategory`
11. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
12. Klik `[Leave]`
13. Verifikasi input Add pada `Induk {runId}-036` tertutup tanpa menyimpan

### Klik area di luar tree: Cancel (TC-260)

14. Hover node `Induk {runId}-036`, klik aksi `+ Subcategory`
15. Ketik `Draft Name` pada input
16. Klik area konten tabel Device Name di luar sidebar
17. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
18. Klik `[Cancel]`
19. Verifikasi dialog tertutup
20. Verifikasi input inline Add tetap terbuka dengan nilai `Draft Name`

### Tombol Back browser: Cancel (TC-267)

21. Tekan tombol Back browser
22. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
23. Klik `[Cancel]`
24. Verifikasi pengguna tetap di Settings > Device > Device Name
25. Verifikasi input inline Add tetap terbuka dengan nilai `Draft Name`
26. Klik `[Clear Field]`, tekan Esc

### Pemeriksaan akhir tidak ada node dan tidak ada entri baru

27. Verifikasi `Induk {runId}-036` hanya memuat anak `Anak Awal {runId}-036`
28. Klik ikon Changelog pada header Sidebar Category
29. Ketik Search `{runId}-036`, tekan Enter
30. Verifikasi jumlah baris hasil Search sama dengan baseline
31. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 dan 2 (membentuk riwayat browser untuk TC-267 agar Back kembali ke halaman sebelumnya), langkah 3 (membuka cabang tree), langkah 7 dan 31 (menutup modal Changelog), langkah 26 (memulihkan input yang dirty ke keadaan bersih lalu menutupnya tanpa dialog).
- Urutan TC-267 di akhir karena satu input yang dibiarkan terbuka oleh TC-260 dipakai sebagai input dirty untuk Back; `Draft Name` tidak diketik ulang.
- S-05: klausa "tidak ada node baru dan tidak ada entri log" pada TC-259, TC-260, TC-267 dinyatakan sebagai asersi jumlah dengan baseline (langkah 6, 27, 30), bukan asersi absence kelas g.
- Pembagian TC lintas spec: TC-273 (Add lewat sub-tab Device SKU) ada di spec 093.
- Temuan untuk QA:
  - TC-267 menyebut precondition "halaman Admin Console lain" tanpa menyebut halamannya.
  - TC-259 menyebut "klik aksi pada node lain" tetapi hasil `+ Subcategory` pada node tujuan setelah `[Leave]` (apakah input baru terbuka) tidak disebut Expected; spec tidak mengasersinya.
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` dan `Barcode Handheld`. Spec memakai `Induk {runId}-036` dan `Anak Awal {runId}-036` milik spec.
