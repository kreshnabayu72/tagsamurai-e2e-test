---
id: TC-FA-FAAC-E2E-100-apply-changes-validasi-effective-from-dasar
title: "Apply Changes: Validasi Effective From Kosong"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-316
sourceRules: ["V-23", "§[F-FAAC-02] Edit Asset Class#b2"]
smoke: []
dependsOn: []
trace:
  "V-23": 8
  "§[F-FAAC-02] Edit Asset Class#b2": [9, 10]
coverage:
  web: automated
---

# Apply Changes: Validasi Effective From Kosong

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-ASSETS` dipakai aset: 1 Asset Name dengan 5 aset aktif, Method Straight Line, Useful Life 60, belum pernah diposting, tanpa versi Scheduled.
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser sinkron dan tidak digeser spec ini. Kemampuan membaca nilai tersimpan Useful Life lewat fixture BE disediakan tim FE/BE.
- State: spec tidak menyimpan perubahan; Useful Life `B-ASSETS` tetap 60 dan tanpa versi Scheduled.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
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
11. Klik `[Cancel]` pada dialog `Apply Changes`
12. Klik breadcrumb `Asset Class`
13. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
14. Klik `[Leave]`
15. Klik `(←)` pada kotak Search

## Notes

1. Satu sesi edit Detail `B-ASSETS` dipakai untuk TC-316: langkah TC nomor 1 sampai 4 dijalankan di langkah 2 sampai 5.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 11 (menutup dialog `Apply Changes` tanpa menyimpan), langkah 12 dan 14 (menutup form Detail yang dirty lewat dialog `Unsaved Changes`, S-08; langkah 13 adalah `Verifikasi` dialog yang diwajibkan S-08), dan langkah 15 (mengosongkan Search).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. TC-FA-FAAC-317 dan TC-FA-FAAC-318 dihapus dari TC; blok dan trace-nya dihapus dari spec ini. Langkah 11 sampai 15 menggantikan penutupan sesi yang sebelumnya terjadi lewat Apply sukses TC-318 (bukan langkah TC).
