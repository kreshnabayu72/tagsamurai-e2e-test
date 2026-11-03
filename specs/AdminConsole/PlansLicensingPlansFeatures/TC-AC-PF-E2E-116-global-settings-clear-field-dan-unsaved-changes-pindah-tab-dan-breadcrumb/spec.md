---
id: TC-AC-PF-E2E-116-global-settings-clear-field-dan-unsaved-changes-pindah-tab-dan-breadcrumb
title: "Global Settings: Clear Field dan Dialog Unsaved Changes Saat Pindah Tab dan Klik Breadcrumb"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-294
  - TC-AC-PF-295
  - TC-AC-PF-296
coverage:
  web: automated
---

# Global Settings: Clear Field dan Dialog Unsaved Changes Saat Pindah Tab dan Klik Breadcrumb

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini, lihat Temuan untuk QA).
- State global: suite serial (`parallel: false`). Global FAMS Settings adalah singleton (S-06, pengecualian 2026-10-30): nilai `5` dan `2` dipulihkan lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after`. Spec ini tidak menyimpan perubahan apa pun; semua perubahan form dibuang lewat `[Clear Field]` atau `[Leave]`.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca nilai tersimpan Global FAMS Settings untuk asersi "nilai tersimpan".
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-294: Clear Field mengembalikan kedua input tanpa dialog

1. Klik tab `Global Settings`
2. Ubah `Max custom fields per asset name` menjadi `9` dan `Max depreciation methods (Multi Depreciation tier)` menjadi `7`
3. Klik `[Clear Field]`
4. Verifikasi `Max custom fields per asset name` kembali bernilai `5`
5. Verifikasi `Max depreciation methods (Multi Depreciation tier)` kembali bernilai `2`
6. Verifikasi Tidak ada dialog konfirmasi
7. Verifikasi Tidak ada dialog `Unsaved Changes`

### TC-AC-PF-295: Unsaved Changes saat pindah ke tab Default

8. Ubah `Max custom fields per asset name` menjadi `9`
9. Klik tab `Default`
10. Verifikasi Dialog dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
11. Klik `[Cancel]`
12. Verifikasi Dialog tertutup
13. Verifikasi Pengguna tetap berada di tab Global Settings
14. Verifikasi `Max custom fields per asset name` bernilai `9`
15. Klik tab `Default`
16. Klik `[Leave]`
17. Verifikasi Navigasi dilanjutkan: halaman Plans & Licensing > Plans & Features > Default > Active tampil
18. Verifikasi Perubahan dibuang: nilai tersimpan `Max custom fields per asset name` tetap `5`

### TC-AC-PF-296: Unsaved Changes saat klik breadcrumb Plans & Features

19. Klik tab `Global Settings`
20. Ubah `Max custom fields per asset name` menjadi `9`
21. Klik segmen `Plans & Features` pada breadcrumb
22. Verifikasi Dialog dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
23. Klik `[Cancel]`
24. Verifikasi Dialog tertutup
25. Verifikasi Pengguna tetap berada di tab Global Settings
26. Verifikasi `Max custom fields per asset name` bernilai `9`
27. Klik segmen `Plans & Features` pada breadcrumb
28. Klik `[Leave]`
29. Verifikasi Navigasi dilanjutkan: halaman Plans & Licensing > Plans & Features > Default > Active tampil
30. Verifikasi Perubahan dibuang: nilai tersimpan `Max custom fields per asset name` tetap `5`

## Notes

- Langkah penghubung (S-03): klik tab `Global Settings` sebagai precondition TC-AC-PF-294 dan TC-AC-PF-296 (langkah 1 dan 19). Langkah "Ulangi aksi pemicu lalu klik `[Leave]`" pada TC ditulis sebagai dua langkah (pemicu ulang, lalu `[Leave]`).
- Pembagian TC lintas spec: TC-AC-PF-297 dan TC-AC-PF-298 ada di spec 129; TC-AC-PF-290 sampai TC-AC-PF-293 ada di spec 115.
- Temuan untuk QA:
  - Tabel Pre-setup TC tidak memuat baris bernomor untuk nilai awal Global FAMS Settings (`5` dan `2`); nilai itu hanya tertulis di precondition tiap TC. Spec memakai S-06 pengecualian 2026-10-30 (singleton, pemulihan lewat Fixture BE).
  - TC-AC-PF-295 dan TC-AC-PF-296 Expected butir c ("nilai tersimpan tetap `5`") tidak menyatakan cara membaca nilai tersimpan; spec memakai kemampuan baca nilai tersimpan yang disediakan tim FE/BE tanpa endpoint karangan (langkah 18 dan 30).
