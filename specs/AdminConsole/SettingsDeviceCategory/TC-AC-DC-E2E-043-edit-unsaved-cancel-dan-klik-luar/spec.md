---
id: TC-AC-DC-E2E-043-edit-unsaved-cancel-dan-klik-luar
title: "Edit Category: Dialog Unsaved Changes Cancel, Esc, Klik Area Luar Tree, dan Esc Leave"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-118
  - TC-AC-DC-119
  - TC-AC-DC-258
  - TC-AC-DC-262
coverage:
  web: automated
---

# Edit Category: Dialog Unsaved Changes Cancel, Esc, Klik Area Luar Tree, dan Esc Leave

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-043`): `Pemindai {runId}-043` (target Edit; namanya tidak berubah selama spec) dan `Saudara {runId}-043` (node lain sebagai sasaran klik). Hook `after` menghapus keduanya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `Draft Edit` (tidak pernah disimpan sehingga tidak bersuffix).
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-043`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Cancel mempertahankan input dan nilai (TC-118)

6. Hover node `Pemindai {runId}-043`, klik aksi Edit
7. Ubah nilai menjadi `Draft Edit`, klik node `Saudara {runId}-043`
8. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
9. Klik `[Cancel]`
10. Verifikasi dialog tertutup
11. Verifikasi input Edit tetap terbuka dengan nilai `Draft Edit` dipertahankan

### Esc pada input yang berisi perubahan: Cancel (TC-258)

12. Tekan Esc pada input yang masih berisi `Draft Edit`
13. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
14. Klik `[Cancel]`
15. Verifikasi dialog tertutup
16. Verifikasi input Edit tetap terbuka dengan nilai `Draft Edit`

### Klik area di luar tree: Cancel (TC-262)

17. Klik area konten tabel Device Name di luar sidebar
18. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
19. Klik `[Cancel]`
20. Verifikasi dialog tertutup
21. Verifikasi input Edit tetap terbuka dengan nilai `Draft Edit`

### Esc pada input yang berisi perubahan: Leave (TC-119)

22. Tekan Esc pada input yang masih berisi `Draft Edit`
23. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
24. Klik `[Leave]`
25. Verifikasi input collapse
26. Verifikasi nama node tetap `Pemindai {runId}-043`

### Pemeriksaan akhir tidak ada entri baru

27. Klik ikon Changelog pada header Sidebar Category
28. Ketik Search `{runId}-043`, tekan Enter
29. Verifikasi jumlah baris hasil Search sama dengan baseline
30. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 30 (menutup modal Changelog).
- Urutan TC dalam spec: TC-118, TC-258, TC-262 memakai satu input Edit yang sama yang dibiarkan terbuka dengan `Draft Edit` sehingga nilai itu tidak diketik ulang; TC-119 (Leave, menutup input) ditaruh terakhir agar input tidak perlu dibuka ulang dan dipulihkan.
- S-05: klausa "nama node belum berubah dan tidak ada entri log" pada TC-118, TC-258, TC-262, TC-119 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 26, 29), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai target Edit dan `Barcode Handheld` sebagai node tujuan klik. Spec memakai node milik spec.
  - TC-118 menulis "berpindah ke node lain" tanpa aksi persis; spec memakai klik pada node `Saudara {runId}-043`.
  - TC-118 mengharapkan "nama node di tree belum berubah" saat input terbuka; label node digantikan input saat Edit, sehingga spec mengasersi nama node sesudah input ditutup (langkah 26).
