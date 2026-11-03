---
id: TC-GS-NLU-E2E-084-list-setup-column-bagian-1
title: "List Setup Column bagian 1: overlay Column Visibility, popup Setup Column, sembunyikan kolom, kolom curated, dan reorder drag"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-286
  - TC-GS-NLU-287
  - TC-GS-NLU-288
  - TC-GS-NLU-289
  - TC-GS-NLU-290
coverage:
  web: automated
---

# List Setup Column bagian 1: overlay Column Visibility, popup Setup Column, sembunyikan kolom, kolom curated, dan reorder drag

## Prerequisites

- Mode: FE+BE (backend nyata). Konfigurasi kolom tersimpan di browser (tanpa request tulis ke server).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 13; hanya dibaca, tidak diubah, tanpa suffix): Non-Login User Pre-setup; Custom Field dasar `Blood Type`, `Emergency Phone`, `Badge Note` (Active). Kolom default: Active, Name, Position, Division, Employee ID, Represented By, Last Update (urutan sesuai TC-GS-NLU-286). Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: muat ulang halaman (F5; tidak ada form terbuka sehingga tidak ada dialog `beforeunload`); drag and drop baris di popup Setup Column; penghapusan preferensi kolom di browser di hook `after` (disediakan tim FE), bukan `[Reset to Default]`.
- State global: konfigurasi kolom tabel List Non-Login User; dipulihkan oleh langkah penghubung di akhir tiap TC dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-286: Screening overlay Column Visibility

1. Klik ikon `⋯` pada header kolom Actions
2. Verifikasi overlay memuat kolom Active, Name, Position, Division, Employee ID, Represented By, Last Update dengan checkbox checked dan enabled serta drag handle
3. Verifikasi kolom curated Temporary User, Temporary Until, dan Custom Field aktif unchecked dan enabled
4. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-GS-NLU-287: Screening popup Setup Column

5. Klik `Setup Column...`
6. Verifikasi Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `✕`
7. Verifikasi Body: daftar kolom dengan status centang default, drag handle, ikon Pin, dan Live Preview tabel
8. Verifikasi Footer: `[Reset to Default]` dan `[Save]`, tanpa `[Cancel]`
9. Klik `✕`

### TC-GS-NLU-288: Hapus centang kolom Hideable lalu Save persisten setelah refresh

10. Klik `⋯` header Actions > `Setup Column...`, hapus centang dua kolom pertama (Active dan Name)
11. Verifikasi Live Preview mengikuti perubahan sebelum Save
12. Klik `[Save]`
13. Verifikasi kolom Active dan Name hilang dari tabel
14. Tekan F5
15. Verifikasi pengaturan tetap: kolom Active dan Name tidak tampil
16. Klik `⋯` header Actions > `Setup Column...`, centang kembali kolom Active dan Name, klik `[Save]`

### TC-GS-NLU-289: Centang kolom curated Temporary User, Temporary Until, Custom Field aktif

17. Klik `⋯` header Actions > `Setup Column...`, centang Temporary User, Temporary Until, Blood Type, Emergency Phone, dan Badge Note
18. Klik `[Save]`
19. Verifikasi kolom curated Temporary User, Temporary Until, Blood Type, Emergency Phone, dan Badge Note tampil pada tabel
20. Tekan F5
21. Verifikasi kolom curated tetap tampil setelah refresh
22. Klik `⋯` header Actions > `Setup Column...`, hapus centang kelima kolom curated, klik `[Save]`

### TC-GS-NLU-290: Drag reorder kolom pada Setup Column

23. Klik `⋯` header Actions > `Setup Column...`, drag kolom terakhir (Last Update) ke posisi pertama
24. Verifikasi Live Preview mengikuti urutan baru sebelum Save
25. Klik `[Save]`
26. Verifikasi tabel mengikuti urutan baru: Last Update di posisi pertama
27. Tekan F5
28. Verifikasi urutan baru tetap setelah refresh
29. Klik `⋯` header Actions > `Setup Column...`, drag kolom Last Update kembali ke posisi terakhir, klik `[Save]`

## Notes

- Langkah penghubung (S-03): menutup popup (`✕`) pada TC-GS-NLU-287, dan langkah terakhir tiap TC-GS-NLU-288 sampai TC-GS-NLU-290 yang memulihkan konfigurasi kolom (S-09); hook `after` menghapus preferensi kolom sebagai cadangan.
- Asersi tambahan (S-03): TC-GS-NLU-290 Expected a ("tetap setelah refresh") memuat F5 yang tidak ada di langkah TC; langkah F5 ditambahkan pada TC-GS-NLU-288 sampai TC-GS-NLU-290 untuk mengasersi persistensi.
- Temuan untuk QA:
  - TC-GS-NLU-288 langkah 1 ("dua kolom pertama selain kolom terakhir") ambigu; spec memakai Active dan Name sesuai urutan di TC-GS-NLU-286.
  - TC-GS-NLU-289 menyebut "Custom Field aktif" tanpa daftar; spec memakai tiga Custom Field dasar Pre-setup No. 13.
  - TC-GS-NLU-290 tidak menyebut cara memverifikasi Live Preview dan tabel selain urutan kolom; spec mengasersi posisi pertama kolom Last Update.
