---
id: TC-AC-DC-E2E-045-delete-dialog-leaf-dan-cancel
title: "Delete Category: Dialog Konfirmasi Leaf, Cancel, Klik Backdrop, dan Esc"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-127
  - TC-AC-DC-131
  - TC-AC-DC-133
coverage:
  web: automated
---

# Delete Category: Dialog Konfirmasi Leaf, Cancel, Klik Backdrop, dan Esc

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-045`): `Daun {runId}-045` (leaf tanpa Device Name pengacu; tidak pernah dihapus oleh spec ini). Hook `after` menghapus node itu lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `Daun {runId}-045`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Dialog konfirmasi Delete leaf (TC-127)

6. Hover node `Daun {runId}-045`, klik aksi Delete
7. Verifikasi judul dialog "Delete Category" tanpa tanda tanya
8. Verifikasi isi dialog diawali bullet `Daun {runId}-045` lalu kalimat "Are you sure you want to delete it? This action cannot be undone."
9. Verifikasi dua tombol `[Cancel]` dan `[Delete]`
10. Verifikasi tombol `[Delete]` bergaya destruktif
11. Verifikasi node `Daun {runId}-045` belum terhapus

### Cancel tidak menghapus apa pun (TC-131)

12. Klik `[Cancel]`
13. Verifikasi dialog tertutup
14. Verifikasi node `Daun {runId}-045` masih ada di tree
15. Verifikasi tidak ada toast

### Klik backdrop dan Esc (TC-133)

16. Hover node `Daun {runId}-045`, klik aksi Delete
17. Klik area backdrop di luar dialog
18. Verifikasi dialog tetap terbuka
19. Tekan Esc
20. Verifikasi dialog tertutup setara `[Cancel]`
21. Verifikasi node `Daun {runId}-045` tidak terhapus

### Pemeriksaan akhir tidak ada entri baru

22. Klik ikon Changelog pada header Sidebar Category
23. Ketik Search `Daun {runId}-045`, tekan Enter
24. Verifikasi jumlah baris hasil Search sama dengan baseline
25. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 25 (menutup modal Changelog).
- S-05: klausa "tidak ada entri log" pada TC-131 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4 dan 24), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Daun` sebagai target Delete dan menyebut Device Name Pre-setup #15 sebagai precondition TC-127 tanpa memakainya pada langkah atau Expected. Spec memakai `Daun {runId}-045` milik spec dan tidak memakai Device Name Pre-setup #15.
  - TC-127 mengharapkan gaya destruktif tombol `[Delete]` tanpa menyebut tokennya; spec mengasersi sesuai teks TC.
