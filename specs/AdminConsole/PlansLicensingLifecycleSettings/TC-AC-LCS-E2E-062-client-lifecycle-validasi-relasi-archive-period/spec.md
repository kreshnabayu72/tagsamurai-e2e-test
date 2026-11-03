---
id: TC-AC-LCS-E2E-062-client-lifecycle-validasi-relasi-archive-period
title: "Tab Client Lifecycle: Validasi Relasi Archive Period Duration terhadap Purge Warning Email dan Purge Urgent Warning Email"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-309
  - TC-AC-LCS-310
  - TC-AC-LCS-311
  - TC-AC-LCS-312
coverage:
  web: automated
---

# Tab Client Lifecycle: Validasi Relasi Archive Period Duration terhadap Purge Warning Email dan Purge Urgent Warning Email

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Client Lifecycle (Notify Plan Owner Before Event `45`, First Reminder Before Event `30`, Second Reminder Before Event `7`, Final Reminder Before Event `1`, Grace Period Duration `30`, Archive Period Duration `30`, Purge Warning Email `10`, Purge Urgent Warning Email `2`, Post-Purge Retention `730`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Client Lifecycle adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.

## Test Steps

1. Klik tab Client Lifecycle

### TC-AC-LCS-309: Archive Period Duration lebih kecil dari Purge Warning Email menampilkan error relasi

2. Ubah Archive Period Duration dari `30` menjadi `5`
3. Klik area kosong di luar field (blur)
4. Verifikasi inline error (severity danger) pada field Purge Warning Email: "Purge warning cannot exceed archive period duration"
5. Verifikasi `[Save]` disabled

### TC-AC-LCS-310: Purge Warning Email melebihi Archive Period Duration menampilkan error relasi

6. Ubah Archive Period Duration kembali menjadi `30` lalu klik area kosong di luar field (blur)
7. Ubah Purge Warning Email dari `10` menjadi `31`
8. Klik area kosong di luar field (blur)
9. Verifikasi inline error (severity danger) pada field Purge Warning Email: "Purge warning cannot exceed archive period duration"
10. Verifikasi `[Save]` disabled

### TC-AC-LCS-311: Purge Warning Email tepat sama dengan Archive Period Duration diterima

11. Ubah Purge Warning Email kembali menjadi `10` lalu klik area kosong di luar field (blur)
12. Ubah Purge Warning Email dari `10` menjadi `30`
13. Klik area kosong di luar field (blur)
14. Verifikasi tidak ada pesan error relasi pada Purge Warning Email
15. Verifikasi `[Save]` enabled

### TC-AC-LCS-312: Purge Urgent Warning Email melebihi Archive Period Duration menampilkan error relasi

16. Ubah Purge Warning Email kembali menjadi `10` lalu klik area kosong di luar field (blur)
17. Ubah Purge Urgent Warning Email dari `2` menjadi `40`
18. Klik area kosong di luar field (blur)
19. Verifikasi inline error (severity danger) pada field Purge Urgent Warning Email: "Purge urgent warning cannot exceed archive period duration"
20. Verifikasi inline error (severity danger) pada field Purge Warning Email: "Purge warning must be greater than urgent warning" (Purge Warning Email `10` tidak lebih besar dari Purge Urgent Warning Email `40`; pesan relasi tampil pada field pemilik aturan)
21. Verifikasi `[Save]` disabled
22. Ubah Purge Urgent Warning Email kembali menjadi `2` lalu klik area kosong di luar field (blur)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 11, 16, 22 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Langkah penghubung memulihkan nilai tersimpan di antara TC supaya error identik pada Purge Warning Email tidak terbawa dari TC sebelumnya (R-12); langkah terakhir mengembalikan form ke nilai tersimpan agar tidak berakhir dirty (S-09).
- Temuan untuk QA:
  - TC-AC-LCS-309 dan TC-AC-LCS-310 mengasersi pesan error pada field Purge Warning Email dengan teks yang sama pada dua aturan berbeda (batas Archive Period Duration); TC tidak membedakannya (S-15).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
