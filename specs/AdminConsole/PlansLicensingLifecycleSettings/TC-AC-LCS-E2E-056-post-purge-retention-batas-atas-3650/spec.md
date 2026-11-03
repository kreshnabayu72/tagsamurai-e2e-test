---
id: TC-AC-LCS-E2E-056-post-purge-retention-batas-atas-3650
title: "Post-Purge Retention: Batas Atas 3650 Ditolak di Atas dan Diterima pada Maksimum"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-210
  - TC-AC-LCS-211
  - TC-AC-LCS-314
  - TC-AC-LCS-327
coverage:
  web: automated
---

# Post-Purge Retention: Batas Atas 3650 Ditolak di Atas dan Diterima pada Maksimum

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Data Pre-setup (Pre-setup 7): ketujuh tab Lifecycle Settings pada nilai default; tab yang dipakai spec ini: Client Lifecycle (Notify Plan Owner Before Event `45`, First Reminder Before Event `30`, Second Reminder Before Event `7`, Final Reminder Before Event `1`, Grace Period Duration `30`, Archive Period Duration `30`, Purge Warning Email `10`, Purge Urgent Warning Email `2`, Post-Purge Retention `730`). Hook `beforeEach` suite memulihkannya lewat Fixture BE. Spec tidak membuat entitas.
- Flag Guided Tooltip halaman Lifecycle Settings sudah disetel oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan konfigurasi tab (disediakan tim FE/BE).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).
- State global: konfigurasi tab Client Lifecycle adalah pengaturan platform-wide; suite berjalan serial (`parallel: false`). Pemulihan: hook `beforeEach` dan `after` suite memulihkan ketujuh tab ke nilai default lewat Fixture BE.
- Efek samping: setiap `[Save]` atau `[Reset to Default]` menambah entri Changelog permanen tab ini; spec tidak membaca Changelog dan tidak mengasersi angka entri.

## Test Steps

1. Klik tab Client Lifecycle

### TC-AC-LCS-210: Field Post-Purge Retention diisi 3651 (di atas maksimum 3,650) menampilkan error rentang

2. Pilih seluruh isi field Post-Purge Retention lalu ketik `3651`
3. Klik area kosong di luar field (blur)
4. Verifikasi inline error text (severity danger) di bawah field Post-Purge Retention: "Value must be between 1 and 3,650"
5. Verifikasi `[Save]` disabled

### TC-AC-LCS-314: Post-Purge Retention diterima pada nilai 3650 tanpa terikat Archive Period Duration

6. Ubah Post-Purge Retention menjadi `3650`
7. Klik area kosong di luar field (blur)
8. Verifikasi tidak ada pesan error
9. Verifikasi `[Save]` enabled

### TC-AC-LCS-327: Post-Purge Retention diisi 3650 diterima

10. Ubah Post-Purge Retention kembali menjadi `730` lalu klik area kosong di luar field (blur)
11. Ubah Post-Purge Retention menjadi `3650`
12. Klik area kosong di luar field (blur)
13. Verifikasi tidak ada pesan error
14. Verifikasi `[Save]` enabled

### TC-AC-LCS-211: Save Post-Purge Retention pada nilai maksimum 3,650

15. Ubah Post-Purge Retention kembali menjadi `730` lalu klik area kosong di luar field (blur)
16. Ubah Post-Purge Retention menjadi `3650`, lalu klik area kosong di luar field (blur)
17. Verifikasi tidak ada pesan error rentang pada Post-Purge Retention saat nilai `3650` diisi
18. Klik `[Save]`
19. Verifikasi toast sukses "Success, client lifecycle settings have been saved."
20. Verifikasi `[Save]` disabled setelah tab refresh
21. Muat ulang halaman dengan F5 lalu klik tab Client Lifecycle
22. Verifikasi Post-Purge Retention bernilai `3650` (nilai tersimpan)

## Notes

- Urutan TC: 210, 314, 327, 211 (penolakan di atas batas dan penerimaan tanpa Save lebih dulu; Save nilai maksimum di akhir, S-10).
- Langkah penghubung (S-03): langkah 1, 10, 15 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Langkah 16 menyertakan blur sesuai TC-AC-LCS-211 langkah 1 ("lalu blur") sebelum asersi absence pada langkah 17, karena validasi rentang muncul saat blur (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LCS-210, TC-AC-LCS-211, TC-AC-LCS-314, dan TC-AC-LCS-327 menguji nilai 3650 (diterima pada maksimum) dengan Expected yang hampir sama; TC-AC-LCS-314 dan TC-AC-LCS-327 identik dalam langkah dan Expected (tumpang tindih). Spec tetap menulis tiap TC sebagai bagian terpisah.
  - Post Condition TC-AC-LCS-211 (Post-Purge Retention tersimpan `3650`) setara dengan `Verifikasi` nilai sesudah F5; tidak ada asersi tambahan.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
