---
id: TC-FA-LBL-E2E-058-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-2-3
title: "Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-180
  - TC-FA-LBL-190
  - TC-FA-LBL-204
coverage:
  web: automated
---

# Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 2/3)

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Volume (Pre-setup #10, Company Volume), `Fixture.assetLabeling.totalControlVolume.email`; email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE. Password `Spectra.env.FA_TC_VOLUME_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha) dan memulihkan Selection Limit ke nilai awal.
- Data Pre-setup (hanya dibaca, tidak diubah): Company Volume (#10) dengan 120 label `Project Tag 1` sampai `Project Tag 120` (log Create tersedia). Data Dinamis: tidak ada. Page size awal tabel 10 baris.
- Selection Limit di atas 120, diatur di hook `before` spec ini bila nilai awalnya 120 atau kurang dan dipulihkan di hook `after`. Kemampuan mengubah dan memulihkan System Limits disediakan tim FE (TC, PRD, dan LLD tidak menyebut akun pelaku perubahannya).
- Kelas harness e (volume data, 120 label): spec ini hanya memuat TC volume Company Volume dan tidak memuat TC kelas harness lain.
- State global: Selection Limit di System Limits (lihat butir sebelumnya); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LBL-180: Select All server memilih semua baris lintas halaman lalu berubah menjadi Unselect All

1. Centang satu baris
2. Klik `Select All (120 records)`
3. Verifikasi counter `120 Labels selected`
4. Verifikasi tombol berubah menjadi `Unselect All`
5. Pindah ke halaman 2
6. Verifikasi baris di halaman 2 tetap tercentang
7. Klik `Unselect All`
8. Verifikasi seluruh seleksi dibatalkan dan centang hilang
9. Verifikasi Bulk Action Bar hilang

### TC-FA-LBL-204: Seleksi bertahan saat pindah halaman, Search, Filter, dan Sort berubah

10. Centang dua baris pertama di halaman 1 dan catat nama keduanya (baris X dan baris Y)
11. Pindah ke halaman 2
12. Verifikasi counter `2 Labels selected`
13. Ketik Search `Project Tag 9`, tekan Enter
14. Verifikasi counter `2 Labels selected`
15. Klik `(←)` pada kotak Search
16. Verifikasi counter `2 Labels selected`
17. Klik header kolom `Label` sampai urutan Descending
18. Verifikasi counter `2 Labels selected`
19. Ketik Search nama baris X, tekan Enter
20. Verifikasi baris X tercentang
21. Ganti isi kotak search dengan nama baris Y, tekan Enter
22. Verifikasi baris Y tercentang
23. Klik `(←)` pada kotak Search
24. Klik ikon `×`

### TC-FA-LBL-190: Dialog bulk memuat seluruh nama tanpa diringkas dalam container scrollable

25. Atur page size 25
26. Centang 12 label pertama
27. Klik `Bulk Action` lalu klik `Delete`
28. Verifikasi seluruh 12 nama tampil sebagai bullet terurut abjad A sampai Z dalam container scrollable
29. Verifikasi dialog tidak memuat ringkasan `[N] items are selected.` maupun `...and N more`
30. Klik `[Cancel]`
31. Klik ikon `×`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 10 mencatat nama dua baris yang dicentang supaya keduanya dapat dicari kembali sesudah Sort; langkah 19 dan langkah sesudahnya (Search nama baris X dan Y) menampilkan kembali kedua baris untuk Verifikasi centangnya (Search untuk menemukan baris target, R-16); klik `(←)`, klik `[Cancel]`, dan klik ikon `×` membersihkan Search, dialog, dan seleksi (S-09).
- Sort Descending dari TC-FA-LBL-204 tidak dipulihkan sebelum TC-FA-LBL-190 karena TC-FA-LBL-190 tidak bergantung pada urutan tabel selain 12 baris pertama yang dicentang.
- Pembagian TC lintas spec: TC-FA-LBL-178, TC-FA-LBL-179, TC-FA-LBL-181, dan TC-FA-LBL-182 ada di spec 057; TC-FA-LBL-183 dan TC-FA-LBL-184 (Selection Limit 100) ada di spec 164.
- Temuan untuk QA:
  - TC-FA-LBL-204 Expected ("kedua baris tetap tercentang ketika tampil kembali") tidak menyebut cara menampilkan kembali kedua baris sesudah Sort Descending; spec mencarinya lewat Search nama baris. Langkah 3 TC menyebut "Search" dan judul menyebut Filter, tetapi Filter tidak punya langkah di TC; Filter tidak diuji di spec ini.
  - TC-FA-LBL-190 langkah 1 ("12 label pertama") tidak menyebut urutan tabel; spec mencentang 12 baris pertama sesuai urutan tampil.
  - Email akun `Total Control Volume` tidak tertulis di Pre-setup #10.
