---
id: TC-AC-PF-E2E-117-global-settings-refresh-f5-back-esc
title: "Global Settings: Refresh F5, Tombol Back, dan Esc Saat Form Dirty atau Bersih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-667
  - TC-AC-PF-674
  - TC-AC-PF-740
  - TC-AC-PF-745
coverage:
  web: automated
---

# Global Settings: Refresh F5, Tombol Back, dan Esc Saat Form Dirty atau Bersih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini, lihat Temuan untuk QA).
- State global: suite serial (`parallel: false`). Global FAMS Settings adalah singleton (S-06, pengecualian 2026-10-30): nilai `5` dan `2` dipulihkan lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after`. Spec ini tidak menyimpan perubahan apa pun; form yang dirty dikembalikan ke nilai tersimpan pada langkah 6, 13, dan 22 (S-09).
- Kemampuan teknis (disediakan tim FE/BE): dialog `beforeunload` bawaan browser pada F5 dapat dibatalkan oleh spec (user tetap di halaman); tombol Back browser dan tombol Esc dapat dijalankan spec (S-08).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-667: Refresh F5 saat form dirty

1. Klik tab `Global Settings`
2. Ubah `Max custom fields per asset name` menjadi `9`
3. Tekan F5
4. Verifikasi Konfirmasi bawaan browser (`beforeunload`) muncul karena form dirty (teks ditentukan browser)
5. Batalkan konfirmasi bawaan browser sehingga pengguna tetap di halaman
6. Kembalikan `Max custom fields per asset name` ke nilai tersimpan `5`

### TC-AC-PF-674: Tombol Back browser saat form dirty

7. Ubah `Max custom fields per asset name` menjadi `9`
8. Klik tombol Back browser
9. Verifikasi Dialog dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
10. Klik `[Cancel]`
11. Verifikasi Pengguna tetap berada di tab Global Settings
12. Verifikasi `Max custom fields per asset name` bernilai `9`
13. Kembalikan `Max custom fields per asset name` ke nilai tersimpan `5`

### TC-AC-PF-740: Esc saat form dirty

14. Klik tab `Default`
15. Klik tab `Global Settings`
16. Ubah `Max custom fields per asset name` menjadi `9`
17. Tekan Esc
18. Verifikasi Dialog dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
19. Klik `[Cancel]`
20. Verifikasi Pengguna tetap berada di form Global Settings
21. Verifikasi `Max custom fields per asset name` tetap `9` (input dipertahankan)
22. Kembalikan `Max custom fields per asset name` ke nilai tersimpan `5`

### TC-AC-PF-745: Esc saat form bersih

23. Klik tab `Default`
24. Klik tab `Global Settings`
25. Tekan Esc tanpa mengubah apa pun
26. Verifikasi Halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung
27. Verifikasi Tidak ada dialog `Unsaved Changes`

## Notes

- Langkah penghubung (S-03): klik tab `Global Settings` sebagai precondition TC-AC-PF-667 dan TC-AC-PF-674 (langkah 1), klik tab `Default` lalu tab `Global Settings` sebagai precondition TC-AC-PF-740 dan TC-AC-PF-745 (langkah 14, 15, 23, 24), dan pengembalian field ke nilai tersimpan (langkah 6, 13, 22).
- Pembagian TC lintas spec: TC-AC-PF-735, TC-AC-PF-762, dan TC-AC-PF-763 ada di spec 118.
- Temuan untuk QA:
  - Tabel Pre-setup TC tidak memuat baris bernomor untuk nilai awal Global FAMS Settings (`5` dan `2`); nilai itu hanya tertulis di precondition tiap TC. Spec memakai S-06 pengecualian 2026-10-30 (singleton, pemulihan lewat Fixture BE).
  - TC-AC-PF-667 tidak menyatakan tindakan sesudah konfirmasi `beforeunload` muncul; spec membatalkannya agar pengguna tetap di halaman, lalu mengembalikan field (S-09).
  - TC-AC-PF-674 tidak menyatakan halaman tujuan tombol Back browser; spec hanya mengasersi dialog dan hasil `[Cancel]`.
