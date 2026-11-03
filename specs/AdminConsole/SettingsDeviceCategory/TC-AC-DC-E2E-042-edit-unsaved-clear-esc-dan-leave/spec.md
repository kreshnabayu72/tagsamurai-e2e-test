---
id: TC-AC-DC-E2E-042-edit-unsaved-clear-esc-dan-leave
title: "Edit Category: Clear Field, Esc pada Input Bersih, Nilai Dikembalikan ke Awal, dan Dialog Unsaved Changes Leave"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-115
  - TC-AC-DC-116
  - TC-AC-DC-264
  - TC-AC-DC-117
coverage:
  web: automated
---

# Edit Category: Clear Field, Esc pada Input Bersih, Nilai Dikembalikan ke Awal, dan Dialog Unsaved Changes Leave

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-042`): `Pemindai {runId}-042` (target Edit; namanya tidak berubah selama spec) dan `Saudara {runId}-042` (node lain sebagai sasaran klik). Hook `after` menghapus keduanya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `Draft Edit` (tidak pernah disimpan sehingga tidak bersuffix).
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-042`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Clear Field mengosongkan input, bukan mengembalikan nilai awal (TC-115)

6. Hover node `Pemindai {runId}-042`, klik aksi Edit
7. Klik `[Clear Field]`
8. Verifikasi input menjadi kosong (bukan kembali ke nilai tersimpan)
9. Verifikasi input inline Edit tetap terbuka
10. Verifikasi fokus kembali ke input
11. Verifikasi tidak ada dialog konfirmasi
12. Ketik ulang `Pemindai {runId}-042` sehingga identik dengan nilai tersimpan

### Esc pada input Edit yang bersih (TC-116)

13. Tekan Esc tanpa mengubah nilai
14. Verifikasi input inline collapse
15. Verifikasi nama node tetap `Pemindai {runId}-042`
16. Verifikasi tidak ada dialog Unsaved Changes

### Nilai diubah lalu dikembalikan identik (TC-264)

17. Hover node `Pemindai {runId}-042`, klik aksi Edit
18. Ubah nilai menjadi `Draft Edit`, lalu ketik ulang `Pemindai {runId}-042` sampai identik dengan nilai awal
19. Tekan Esc
20. Verifikasi input inline collapse
21. Verifikasi tidak ada dialog "You have unsaved changes. Are you sure you want to leave?"

### Dialog Unsaved Changes: Leave (TC-117)

22. Hover node `Pemindai {runId}-042`, klik aksi Edit
23. Ubah nilai menjadi `Draft Edit`, klik node `Saudara {runId}-042`
24. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
25. Klik `[Leave]`
26. Verifikasi input inline Edit tertutup
27. Verifikasi nama node tetap `Pemindai {runId}-042`

### Pemeriksaan akhir tidak ada entri baru

28. Klik ikon Changelog pada header Sidebar Category
29. Ketik Search `{runId}-042`, tekan Enter
30. Verifikasi jumlah baris hasil Search sama dengan baseline
31. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 31 (menutup modal Changelog), langkah 12 (mengembalikan input ke nilai tersimpan setelah `[Clear Field]` agar input bersih untuk TC-116).
- S-05: klausa "tidak ada entri log" pada TC-117 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4 dan 30), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai target Edit dan `Barcode Handheld` sebagai node tujuan klik. Spec memakai node milik spec.
  - TC-115 mengharapkan "nama node di tree belum berubah" saat input terbuka; label node digantikan input saat Edit, sehingga spec mengasersi nama node sesudah input ditutup (langkah 15).
  - TC-117 menulis "berpindah ke node lain" tanpa aksi persis; spec memakai klik pada node `Saudara {runId}-042`.
