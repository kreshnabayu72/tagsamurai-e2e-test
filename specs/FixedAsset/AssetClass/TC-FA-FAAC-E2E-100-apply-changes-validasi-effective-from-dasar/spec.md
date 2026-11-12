---
id: TC-FA-FAAC-E2E-100-apply-changes-validasi-effective-from-dasar
title: "Apply Changes: Validasi Effective From Kosong, Periode Closed, dan Bulan Tanpa Accounting Period"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-316
  - TC-FA-FAAC-317
  - TC-FA-FAAC-318
coverage:
  web: automated
---

# Apply Changes: Validasi Effective From Kosong, Periode Closed, dan Bulan Tanpa Accounting Period

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-ASSETS` dipakai aset: 1 Asset Name dengan 5 aset aktif, Method Straight Line, Useful Life 60, belum pernah diposting, tanpa versi Scheduled. Accounting Period M-1 (bulan sebelum bulan berjalan M; mis. Sep 2026 bila M = Oct 2026) berstatus Closed (seed Pre-setup relatif tanggal run sesuai NC-16) dan bulan masa depan yang belum memiliki Accounting Period (bulan pasti ditetapkan seed oleh tim FE/BE).
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser sinkron dan tidak digeser spec ini. Kemampuan membaca nilai tersimpan Useful Life lewat fixture BE disediakan tim FE/BE.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: versi Scheduled yang dibuat TC-318 pada `B-ASSETS` dihapus dan Useful Life tetap 60.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-ASSETS`, tekan Enter
2. Klik link Class Code `B-ASSETS` di tabel
3. Klik tab `Depreciation`
4. Ubah Useful Life menjadi 48
5. Klik `Save`

### TC-FA-FAAC-316: Effective From dikosongkan ditolak

6. Kosongkan Effective From
7. Klik `Apply`
8. Verifikasi caption `Effective from must not be empty`
9. Verifikasi dialog `Apply Changes` tetap terbuka
10. Verifikasi tidak ada data tersimpan (Useful Life tersimpan tetap 60, dibaca lewat fixture BE)

### TC-FA-FAAC-317: Effective From pada bulan Accounting Period Closed ditolak

11. Pilih Effective From M-1 (bulan sebelum bulan berjalan yang Accounting Period-nya Closed; mis. `Sep 2026` bila M = Oct 2026)
12. Verifikasi caption langsung saat memilih: `Period <M-1> is closed. Choose a later month.` dengan `<M-1>` = MMM yyyy bulan Closed (mis. `Period Sep 2026 is closed. Choose a later month.` bila M = Oct 2026)
13. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
14. Klik `Apply`
15. Verifikasi `Apply` tidak menyimpan (dialog tetap terbuka dan Useful Life tersimpan tetap 60, dibaca lewat fixture BE)
16. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-318: Effective From pada bulan tanpa Accounting Period tidak ditolak

17. Pilih Effective From bulan masa depan yang belum memiliki Accounting Period
18. Verifikasi dialog `Apply Changes` masih tampil dengan Effective From berisi bulan yang dipilih
19. Verifikasi tidak ada caption V-24
20. Klik `Apply`
21. Verifikasi toast sukses `Success, asset class has been updated.`
22. Klik breadcrumb `Asset Class`
23. Klik `(←)` pada kotak Search

## Notes

1. Satu sesi edit Detail `B-ASSETS` dipakai bersama untuk ketiga TC: langkah TC nomor 1 sampai 4 identik dan dijalankan sekali di langkah 2 sampai 5. Urutan: validasi yang diblokir (TC-316, TC-317) lebih dulu, lalu Apply yang menyimpan versi Scheduled di akhir (TC-318).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 13 (baseline Changelog, S-12), langkah 22 (kembali ke tabel), dan langkah 23 (mengosongkan Search).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. S-05 dan P-1: Expected "tanpa log" pada TC-317 diasersi di spec ini (langkah 16) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class.
5. Temuan untuk QA: Expected TC-318 ("Tidak ada caption V-24") diasersi sebagai absence caption dengan anchor dialog `Apply Changes` yang masih tampil (langkah 18); TC tidak menyebut bulan masa depan yang dipakai. Langkah 11 dan 12 memakai tepat bulan M-1 (satu-satunya bulan Closed pada seed); bulan lain bisa Open sehingga caption tidak muncul.
