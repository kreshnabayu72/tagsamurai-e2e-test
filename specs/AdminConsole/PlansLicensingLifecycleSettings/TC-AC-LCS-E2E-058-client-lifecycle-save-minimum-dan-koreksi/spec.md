---
id: TC-AC-LCS-E2E-058-client-lifecycle-save-minimum-dan-koreksi
title: "Tab Client Lifecycle: Save Nilai Minimum dan Koreksi Nilai Salah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-214
  - TC-AC-LCS-221
coverage:
  web: automated
---

# Tab Client Lifecycle: Save Nilai Minimum dan Koreksi Nilai Salah

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

### TC-AC-LCS-221: memperbaiki nilai yang salah menghapus pesan error dan meng-enable Save

2. Isi Notify Plan Owner Before Event dengan `0`
3. Klik area kosong di luar field (blur)
4. Verifikasi pesan error rentang tampil pada Notify Plan Owner Before Event
5. Verifikasi `[Save]` disabled
6. Isi Notify Plan Owner Before Event dengan `46`
7. Klik area kosong di luar field (blur)
8. Verifikasi pesan error hilang
9. Verifikasi `[Save]` enabled

### TC-AC-LCS-214: Save tab Client Lifecycle dengan nilai minimum yang valid

10. Ubah Notify Plan Owner Before Event menjadi `1`, lalu klik area kosong di luar field (blur)
11. Ubah First Reminder Before Event menjadi `3`, lalu klik area kosong di luar field (blur)
12. Ubah Second Reminder Before Event menjadi `2`, lalu klik area kosong di luar field (blur)
13. Ubah Final Reminder Before Event menjadi `1`, lalu klik area kosong di luar field (blur)
14. Ubah Grace Period Duration menjadi `1`, lalu klik area kosong di luar field (blur)
15. Ubah Archive Period Duration menjadi `2`, lalu klik area kosong di luar field (blur)
16. Ubah Purge Warning Email menjadi `2`, lalu klik area kosong di luar field (blur)
17. Ubah Purge Urgent Warning Email menjadi `1`, lalu klik area kosong di luar field (blur)
18. Ubah Post-Purge Retention menjadi `1`, lalu klik area kosong di luar field (blur)
19. Verifikasi tidak ada pesan error pada seluruh field yang diisi
20. Klik `[Save]`
21. Verifikasi toast sukses "Success, client lifecycle settings have been saved."
22. Verifikasi tab refresh: field memuat Notify Plan Owner Before Event `1`, First Reminder Before Event `3`, Second Reminder Before Event `2`, Final Reminder Before Event `1`, Grace Period Duration `1`, Archive Period Duration `2`, Purge Warning Email `2`, Purge Urgent Warning Email `1`, Post-Purge Retention `1`
23. Verifikasi `[Save]` disabled

## Notes

- Urutan TC: 221, 214 (koreksi nilai salah yang diblokir sebelum Save nilai minimum yang sukses, S-10).
- Langkah penghubung (S-03): langkah 1 (pembukaan tab, pemulihan atau penyiapan state, dan pemuatan ulang halaman; tanpa `Verifikasi`).
- Langkah 10 sampai 18 menyertakan blur sesuai TC-AC-LCS-214 langkah 1 sampai 9 ("lalu blur") sebelum asersi absence pada langkah 19, karena validasi rentang muncul saat blur (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LCS-221 menyebut "pesan error rentang" tanpa teks pesan; spec mengasersi keberadaan pesan tanpa mengutip teksnya (S-02).
  - Post Condition TC-AC-LCS-214 (nilai Client Lifecycle tersimpan sesuai Data Uji) setara dengan `Verifikasi` nilai tersimpan; tidak ada asersi tambahan.
  - Fixture BE untuk memulihkan konfigurasi tab, menyimpan nilai non-default, dan menyiapkan precondition tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13, R-19).
