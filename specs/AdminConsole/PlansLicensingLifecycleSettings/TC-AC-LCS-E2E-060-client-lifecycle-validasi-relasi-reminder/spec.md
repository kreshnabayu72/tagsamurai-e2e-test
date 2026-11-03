---
id: TC-AC-LCS-E2E-060-client-lifecycle-validasi-relasi-reminder
title: "Tab Client Lifecycle: Validasi Relasi Reminder First, Second, dan Final"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-300
  - TC-AC-LCS-301
  - TC-AC-LCS-302
  - TC-AC-LCS-303
  - TC-AC-LCS-304
  - TC-AC-LCS-305
coverage:
  web: automated
---

# Tab Client Lifecycle: Validasi Relasi Reminder First, Second, dan Final

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

### TC-AC-LCS-300: First Reminder Before Event lebih kecil dari Second Reminder Before Event menampilkan error relasi

2. Ubah Second Reminder Before Event menjadi `40`
3. Klik area kosong di luar field (blur)
4. Verifikasi inline error (severity danger) pada field First Reminder Before Event: "First reminder must be greater than second reminder"
5. Verifikasi `[Save]` disabled

### TC-AC-LCS-301: First Reminder Before Event sama dengan Second Reminder Before Event menampilkan error relasi

6. Ubah Second Reminder Before Event kembali menjadi `7` lalu klik area kosong di luar field (blur)
7. Ubah Second Reminder Before Event menjadi `30`
8. Klik area kosong di luar field (blur)
9. Verifikasi inline error (severity danger) pada field First Reminder Before Event: "First reminder must be greater than second reminder"
10. Verifikasi `[Save]` disabled

### TC-AC-LCS-302: Memperbaiki relasi First Reminder Before Event dan Second Reminder Before Event menghapus error dan meng-enable Save

11. Ubah Second Reminder Before Event menjadi `40` lalu klik area kosong di luar field (blur)
12. Ubah First Reminder Before Event menjadi `50`
13. Klik area kosong di luar field (blur)
14. Verifikasi pesan error relasi hilang
15. Verifikasi `[Save]` enabled

### TC-AC-LCS-303: Second Reminder Before Event lebih kecil dari Final Reminder Before Event menampilkan error relasi

16. Ubah Second Reminder Before Event kembali menjadi `7` lalu klik area kosong di luar field (blur)
17. Ubah Final Reminder Before Event menjadi `10`
18. Klik area kosong di luar field (blur)
19. Verifikasi inline error (severity danger) pada field Second Reminder Before Event: "Second reminder must be greater than final reminder"
20. Verifikasi `[Save]` disabled

### TC-AC-LCS-304: Second Reminder Before Event sama dengan Final Reminder Before Event menampilkan error relasi

21. Ubah Final Reminder Before Event kembali menjadi `1` lalu klik area kosong di luar field (blur)
22. Ubah Final Reminder Before Event menjadi `7`
23. Klik area kosong di luar field (blur)
24. Verifikasi inline error (severity danger) pada field Second Reminder Before Event: "Second reminder must be greater than final reminder"
25. Verifikasi `[Save]` disabled

### TC-AC-LCS-305: Memperbaiki relasi Second Reminder Before Event dan Final Reminder Before Event menghapus error dan meng-enable Save

26. Ubah Final Reminder Before Event menjadi `10` lalu klik area kosong di luar field (blur)
27. Ubah Second Reminder Before Event menjadi `20`
28. Klik area kosong di luar field (blur)
29. Verifikasi pesan error relasi hilang
30. Verifikasi `[Save]` enabled
31. Ubah First Reminder Before Event kembali menjadi `30` lalu klik area kosong di luar field (blur)
32. Ubah Second Reminder Before Event kembali menjadi `7` lalu klik area kosong di luar field (blur)
33. Ubah Final Reminder Before Event kembali menjadi `1` lalu klik area kosong di luar field (blur)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 11, 16, 21, 26, 31, 32, 33 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Dua TC berurutan dengan error inline identik pada field yang sama (TC-AC-LCS-300 dan TC-AC-LCS-301, TC-AC-LCS-303 dan TC-AC-LCS-304) diberi langkah pembersih di antaranya (R-12). Precondition TC-AC-LCS-302 dan TC-AC-LCS-305 (error relasi tampil) dibangun oleh langkah penghubung sebelum perbaikan. Tiga langkah terakhir mengembalikan form ke nilai tersimpan agar tidak berakhir dirty (S-09).
- Temuan untuk QA:
  - TC-AC-LCS-302 dan TC-AC-LCS-305 tidak menyebut cara memverifikasi bahwa error relasi tampil sebelum perbaikan (precondition d); spec tidak menambah asersi itu (S-03).
  - Nilai awal First Reminder Before Event, Second Reminder Before Event, dan Final Reminder Before Event pada tiap TC bergantung pada urutan perubahan nilai di TC sebelumnya; TC tidak menyatakan urutan itu, sehingga spec menambahkan langkah pemulihan nilai sebagai langkah penghubung (S-15).
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
