---
id: TC-GS-GSET-E2E-034-changelog-column-visibility-dan-setup-column-screening-pencarian-batal
title: "Changelog General Settings: Panel Column Visibility, Setup Column Screening, Pencarian Kolom, dan Tutup Tanpa Simpan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-84
  - TC-GS-GSET-87
  - TC-GS-GSET-89
  - TC-GS-GSET-94
coverage:
  web: automated
---

# Changelog General Settings: Panel Column Visibility, Setup Column Screening, Pencarian Kolom, dan Tutup Tanpa Simpan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`).
- Seeding di hook `before` (precondition TC "Changelog berisi baris riwayat", dipakai sebagai precondition TC, tidak diasersi): satu PUT `/v2/enterprise-management/general-settings` (full-replace, `global-settings/general-settings/API/openapi.yaml`) oleh sesi API Budi Santoso yang mengubah `sessionIdleTimeout` dari 30 ke 60 menit sehingga Changelog memuat sedikitnya satu baris Field `Session Idle Timeout` (`30 minutes` ke `1 hour`), lalu satu PUT yang mengembalikan nilai ke 30 menit. Total entri Changelog tidak pernah diasersi sebagai angka (audit trail permanen).
- Data uji: kolom Changelog `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` (semua Hideable, default visible); kata kunci pencarian kolom `Modified`; kolom yang di-uncheck: `Field` (TC-94).
- Konfigurasi kolom Modal Changelog (visibilitas, urutan, pin) tersimpan per pengguna di cache browser dan baru permanen setelah `[Save]` (PRD general-settings.md §4.2c). Spec ini tidak menyimpan konfigurasi (Modal Setup Column selalu ditutup tanpa `[Save]`), jadi tidak ada langkah pemulihan; hook `after` (tetap jalan walau spec gagal di tengah) mengembalikan konfigurasi kolom Changelog ke default lewat penghapusan preferensi kolom Changelog di browser (mekanisme disediakan tim FE; TC, PRD, dan LLD tidak mendefinisikannya).
- Kemampuan teknis: mengarahkan kursor ke header kolom untuk membaca tooltip; menekan `Esc` pada modal; membaca dan menghapus preferensi kolom di penyimpanan browser.
- Suite berjalan serial (`parallel: false`): konfigurasi kolom Changelog bersifat state bersama dengan spec Setup Column dan Download lain.

## Test Steps

### TC-GS-GSET-84: Panel Column Visibility Changelog dan item Setup Column

1. Klik icon Changelog di pojok kanan atas halaman
2. Arahkan kursor ke header kolom Actions (⋯) di tabel Changelog
3. Verifikasi tooltip header `Column Visibility`
4. Klik header kolom Actions (⋯)
5. Verifikasi panel dropdown tampil dengan daftar kolom berurutan Date, Action, Field, Old Value, New Value, Modified By
6. Verifikasi tiap kolom pada panel memiliki kontrol show/hide
7. Verifikasi tiap kolom pada panel memiliki kontrol reorder cepat
8. Verifikasi item `Setup Column...` di bagian bawah panel

### TC-GS-GSET-87: Screening Modal Setup Column Changelog

9. Klik item `Setup Column...` pada panel
10. Verifikasi Header: Title `Setup Column`
11. Verifikasi Header: info text `Manage column visibility, reorder, and freeze columns.`
12. Verifikasi Header: tombol `[✕]`
13. Verifikasi Body: Search Input dengan placeholder `Search column name...`
14. Verifikasi Body: 6 baris kolom berurutan Date, Action, Field, Old Value, New Value, Modified By
15. Verifikasi Body: checkbox Hideable pada keenam baris tercentang
16. Verifikasi Body: checkbox pada keenam baris enabled
17. Verifikasi Body: drag handle pada tiap baris
18. Verifikasi Body: kontrol Pin/Unpin pada tiap baris
19. Verifikasi Body: Live Preview tabel Changelog tampil
20. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`
21. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-GSET-89: Setup Column: pencarian nama kolom

22. Ketik `Modified` di Search Input `Search column name...`
23. Verifikasi daftar kolom menyempit ke `Modified By`
24. Hapus kata kunci dari Search Input
25. Verifikasi keenam kolom tampil kembali

### TC-GS-GSET-94: Setup Column: tombol X atau Esc membuang perubahan yang belum disimpan

26. Hilangkan centang kolom `Field`
27. Klik `[✕]`
28. Verifikasi Modal Setup Column tertutup
29. Verifikasi tidak ada dialog konfirmasi tambahan
30. Verifikasi kolom `Field` tetap tampil di tabel
31. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`
32. Hilangkan centang kolom `Field`
33. Tekan `Esc`
34. Verifikasi Modal Setup Column tertutup
35. Verifikasi tidak ada dialog konfirmasi tambahan
36. Verifikasi kolom `Field` tetap tampil di tabel

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE (Changelog dimuat dari backend nyata; konfigurasi kolom tersimpan di browser).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC dalam spec: 84, 87 (screening), 89, 94. TC-92 dan TC-95 ada di spec 054. Urutan di `tc-general-settings.md`: 84, 87, 88, 89, 90, 91, 92, 93, 94, 95.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog) dan langkah 24 (menghapus kata kunci sebagai aksi TC-89). Langkah 9 melanjutkan panel yang masih terbuka dari TC-84; langkah 22 sampai 26 melanjutkan Modal Setup Column yang masih terbuka dari TC-87 (langkah 1 TC-89 dan TC-94 "Buka Setup Column" dipenuhi langkah 9). Langkah 31 membuka kembali modal karena modal tertutup sesudah `[✕]`.
- Asersi tambahan (konkretisasi, S-03): langkah 28 dan 29 serta 34 dan 35 memecah satu klausa Expected TC-94 ("modal tertutup tanpa konfirmasi tambahan") menjadi dua `Verifikasi` (S-01).
- Langkah 5 sampai 8 dan 10 sampai 21 dipecah satu `Verifikasi` per klausa Expected (S-01); drag handle, checkbox, dan Pin/Unpin pada baris Setup Column tetap dipisah per klausa.
- Spec 36 langkah, hampir pada ambang sekitar 35 langkah, tanpa ekspansi dan satu kelas harness (fungsional: UI Setup Column, tanpa fault injection atau multi-konteks). Blok 89 dan 94 meneruskan modal yang terbuka dari blok 87, dan blok 84 adalah pintu masuk panel bersama, sehingga keempat blok tidak dipisah lagi. Spec ini tidak menyimpan konfigurasi kolom.
- Pembagian TC lintas spec: TC-GS-GSET-92 dan 95 (kolom visible terakhir, Reset to Default belum disimpan) ada di spec 054; TC-GS-GSET-88, 90, 91, dan 93 (Pin/Unpin, hide/unhide dengan Save, reorder, Reset to Default dengan Save) ada di spec 035; TC-GS-GSET-70 (Search terhadap kolom hidden) di spec 028; TC-GS-GSET-100 dan 159 (Download terhadap kolom visible) di spec 036; TC-GS-GSET-85, 86, 96 di spec 027.
- Temuan untuk QA:
  - TC-GS-GSET-94: TC tidak menyebut cara mengembalikan konfigurasi kolom; spec ini tidak menyimpan konfigurasi sehingga tidak ada yang dipulihkan (hook `after` tetap sebagai cadangan; mekanisme menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE).
  - TC-GS-GSET-84: Expected b menyebut "show/hide dan reorder cepat" tanpa menyebut bentuk kontrol (checkbox dan drag handle); spec mengasersi keberadaan kontrol per kolom tanpa menyebut bentuknya.
