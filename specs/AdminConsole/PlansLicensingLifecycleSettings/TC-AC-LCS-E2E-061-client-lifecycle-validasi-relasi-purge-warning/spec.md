---
id: TC-AC-LCS-E2E-061-client-lifecycle-validasi-relasi-purge-warning
title: "Tab Client Lifecycle: Validasi Relasi Purge Warning Email dan Purge Urgent Warning Email"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-306
  - TC-AC-LCS-307
  - TC-AC-LCS-308
  - TC-AC-LCS-346
coverage:
  web: automated
---

# Tab Client Lifecycle: Validasi Relasi Purge Warning Email dan Purge Urgent Warning Email

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

### TC-AC-LCS-306: Purge Warning Email lebih kecil dari Purge Urgent Warning Email menampilkan error relasi

2. Ubah Purge Urgent Warning Email menjadi `15`
3. Klik area kosong di luar field (blur)
4. Verifikasi inline error (severity danger) pada field Purge Warning Email: "Purge warning must be greater than urgent warning"
5. Verifikasi `[Save]` disabled

### TC-AC-LCS-307: Purge Warning Email sama dengan Purge Urgent Warning Email menampilkan error relasi

6. Ubah Purge Urgent Warning Email kembali menjadi `2` lalu klik area kosong di luar field (blur)
7. Ubah Purge Urgent Warning Email menjadi `10`
8. Klik area kosong di luar field (blur)
9. Verifikasi inline error (severity danger) pada field Purge Warning Email: "Purge warning must be greater than urgent warning"
10. Verifikasi `[Save]` disabled

### TC-AC-LCS-308: Memperbaiki relasi Purge Warning Email dan Purge Urgent Warning Email menghapus error dan meng-enable Save

11. Ubah Purge Urgent Warning Email menjadi `15` lalu klik area kosong di luar field (blur)
12. Ubah Purge Warning Email menjadi `25`
13. Klik area kosong di luar field (blur)
14. Verifikasi pesan error relasi hilang
15. Verifikasi `[Save]` enabled

### TC-AC-LCS-346: Purge Warning Email melanggar dua aturan relasi sekaligus menampilkan pesan pertama menurut urutan tabel

16. Ubah Purge Warning Email kembali menjadi `10` lalu klik area kosong di luar field (blur)
17. Ubah Purge Urgent Warning Email kembali menjadi `2` lalu klik area kosong di luar field (blur)
18. Ubah Archive Period Duration menjadi `3`
19. Ubah Purge Urgent Warning Email menjadi `8`
20. Ubah Purge Warning Email menjadi `5`
21. Klik area kosong di luar field (blur)
22. Verifikasi inline error (severity danger) pada field Purge Warning Email: "Purge warning must be greater than urgent warning" (aturan pertama pada tabel §6; aturan batas Archive Period Duration juga dilanggar tetapi tidak ditampilkan bersamaan)
23. Verifikasi inline error (severity danger) pada field Purge Urgent Warning Email: "Purge urgent warning cannot exceed archive period duration" (Purge Urgent Warning Email `8` melebihi Archive Period Duration `3`; pesan relasi tampil pada field pemilik aturan)
24. Verifikasi `[Save]` disabled
25. Ubah Archive Period Duration kembali menjadi `30` lalu klik area kosong di luar field (blur)
26. Ubah Purge Urgent Warning Email kembali menjadi `2` lalu klik area kosong di luar field (blur)
27. Ubah Purge Warning Email kembali menjadi `10` lalu klik area kosong di luar field (blur)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 11, 16, 17, 25, 26, 27 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- TC-AC-LCS-346 (dua aturan relasi dilanggar sekaligus) berada di akhir sesudah TC relasi tunggal. TC-AC-LCS-306 dan TC-AC-LCS-307 menampilkan error identik pada field yang sama sehingga langkah pembersih disisipkan di antaranya (R-12). Tiga langkah terakhir mengembalikan form ke nilai tersimpan agar tidak berakhir dirty (S-09).
- Temuan untuk QA:
  - TC-AC-LCS-308 tidak menyebut cara memverifikasi bahwa error relasi tampil sebelum perbaikan (precondition d); spec tidak menambah asersi itu (S-03).
  - TC-AC-LCS-346 menyebut aturan pertama pada tabel §6 PRD sebagai dasar pesan; urutan aturan itu tidak tertulis di TC (S-15).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
