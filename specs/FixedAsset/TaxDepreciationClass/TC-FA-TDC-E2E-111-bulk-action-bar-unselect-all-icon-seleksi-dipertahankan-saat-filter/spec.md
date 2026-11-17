---
id: TC-FA-TDC-E2E-111-bulk-action-bar-unselect-all-icon-seleksi-dipertahankan-saat-filter
title: "Bulk Action Bar Unselect All Icon dan Seleksi Dipertahankan saat Filter"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-420
  - TC-FA-TDC-421
  - TC-FA-TDC-422
  - TC-FA-TDC-425
sourceRules: ["FATDC-LOGIC-14l", "§3.6#p1", "FATDC-LOGIC-14k", "§5#b2", "D-01", "FATDC-LOGIC-14e"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-14l": [4, 9]
  "§3.6#p1": [5, 16]
  "FATDC-LOGIC-14k": 10
  "§5#b2": [22, 24]
  "D-01": 26
  "FATDC-LOGIC-14e": 26
anchor: [15, 23]
coverage:
  web: automated
---

# Bulk Action Bar Unselect All Icon dan Seleksi Dipertahankan saat Filter

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset111`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel 25 class dengan 10 baris per halaman (N = 25), memuat NB-3 dan NB-4 berstatus Active dengan Used By 0, NB-OLD berstatus Inactive, dan 22 class lain. Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Dialog Deactivate pada TC-FA-TDC-425 hanya dibuka lalu dibatalkan; tidak ada data yang berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: mencentang checkbox baris dan header; berpindah halaman Pagination; Search tabel (Enter menyaring).
- State global yang diubah: tidak ada (Search dibersihkan dengan langkah eksplisit).

## Test Steps

### TC-FA-TDC-420: Unselect All membatalkan seleksi lintas halaman dan menutup bar

1. Centang checkbox satu baris agar Bulk Action Bar tampil
2. Klik `Select All (25 records)`
3. Klik `Unselect All (25 records)`
4. Verifikasi seluruh seleksi dibatalkan
5. Verifikasi Bulk Action Bar hilang

### TC-FA-TDC-421: Menghapus centang satu baris saat semua terpilih mengembalikan tombol menjadi Select All

6. Centang checkbox satu baris agar Bulk Action Bar tampil
7. Klik `Select All (25 records)`
8. Hapus centang satu baris pada halaman 1
9. Verifikasi tombol berubah kembali menjadi `Select All (25 records)`
10. Verifikasi counter bernilai 24
11. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-422: Icon × pada Bulk Action Bar membatalkan seluruh seleksi

12. Centang checkbox header halaman 1
13. Pindah ke halaman 2 dan centang satu baris
14. Klik icon `×` di Bulk Action Bar
15. Verifikasi seluruh seleksi (termasuk baris di halaman lain) dibatalkan
16. Verifikasi Bulk Action Bar hilang

### TC-FA-TDC-425: Seleksi dipertahankan saat filter diubah dan aksi bulk memproses seluruh seleksi

17. Ketik Search `NB-3`, tekan Enter
18. Centang checkbox baris NB-3
19. Ganti isi kotak search dengan `NB-4`, tekan Enter
20. Centang checkbox baris NB-4
21. Ganti isi kotak search dengan `NB-OLD`, tekan Enter
22. Verifikasi baris NB-OLD tampil di tabel hasil Search
23. Verifikasi counter Bulk Action Bar tetap bernilai 2
24. Verifikasi baris NB-3 dan NB-4 tidak tampil di tabel
25. Klik `Deactivate` pada Bulk Action Bar
26. Verifikasi dialog "Deactivate Tax Depreciation Classes" memuat bullet `• NB-3 – Bukan bangunan – Kelompok 3` dan `• NB-4 – Bukan bangunan – Kelompok 4`
27. Klik `[Cancel]` pada dialog
28. Klik icon `×` di Bulk Action Bar
29. Klik `(←)` pada kotak Search

## Notes

- Urutan TC dalam spec: TC-FA-TDC-420, 421, 422, 425 (TC-FA-TDC-423 dan 424 ada di spec lain). Tabel 25 class memakai 10 baris per halaman sehingga TC-FA-TDC-420 sampai 422 butuh lebih dari satu halaman.
- Langkah penghubung (S-03, R-16): langkah 1 dan 6 (mencentang satu baris agar Bulk Action Bar tampil, karena `Select All` hanya tersedia di bar yang tampil hanya bila ada baris tercentang; langkah 1 TC-FA-TDC-420 dan TC-FA-TDC-421 tidak menyebut cara bar muncul); langkah 17, 19, dan 21 (Search nama baris target; TC-FA-TDC-425 mencentang NB-3 dan NB-4 pada tabel lebih dari satu halaman sehingga baris dicari lewat Search, 8b.13; seleksi bertahan antar Search sesuai Expected TC-FA-TDC-425); langkah 27 dan 28 (menutup dialog dan membersihkan seleksi); langkah terakhir (`(←)` pada Search) mengosongkan Search (S-09); langkah 11 membersihkan seleksi TC-FA-TDC-421.
- Temuan untuk QA:
  - TC-FA-TDC-425 tidak memuat langkah Search untuk menemukan NB-3 dan NB-4 pada tabel 25 class; spec menambah Search sebagai langkah penghubung.
  - TC-FA-TDC-420 dan 421 langkah 1 (`Select All`) tidak menyebut cara memunculkan Bulk Action Bar; spec mencentang satu baris lebih dulu (langkah 1 dan 6). Pola sama dengan TC-FA-TDC-419 (spec 110), 459 (spec 120), 905 dan 907 (spec 122).
  - TC-FA-TDC-422 tidak menyebut baris mana yang dicentang pada halaman 2.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
