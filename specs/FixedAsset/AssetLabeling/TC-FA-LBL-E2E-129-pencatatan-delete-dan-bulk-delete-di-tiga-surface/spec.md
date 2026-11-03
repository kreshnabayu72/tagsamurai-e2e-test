---
id: TC-FA-LBL-E2E-129-pencatatan-delete-dan-bulk-delete-di-tiga-surface
title: "Pencatatan Delete dan Bulk Delete di Tiga Surface"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-390
  - TC-FA-LBL-391
  - TC-FA-LBL-392
  - TC-FA-LBL-393
  - TC-FA-LBL-394
  - TC-FA-LBL-395
coverage:
  web: automated
---

# Pencatatan Delete dan Bulk Delete di Tiga Surface

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label bersih milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-129`):
  - `Log Delete 390 {runId}-129`, `Log Delete 391 {runId}-129`, `Log Delete 392 {runId}-129` (TC-FA-LBL-390 sampai 392)
  - `Log Bulk A 393 {runId}-129` dan `Log Bulk B 393 {runId}-129` (TC-FA-LBL-393)
  - `Log Bulk A 394 {runId}-129` dan `Log Bulk B 394 {runId}-129` (TC-FA-LBL-394)
  - `Log Bulk A 395 {runId}-129` dan `Log Bulk B 395 {runId}-129` (TC-FA-LBL-395)
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Surface log dibaca lewat UI pada Modal Changelog: Labels, Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log, dan Fixed Asset > Activity Log; entri dicari berdasarkan nama label bersuffix unik (baseline nol). Kontrol pencarian pada System Log dan Activity Log disediakan tim FE (lihat Temuan untuk QA). Search pada Labels List memakai potongan nama `<nomor TC> {runId}-129` yang sama-sama dimiliki kedua label Bulk A dan Bulk B.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-129`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-390: Delete tercatat di Changelog

1. Ketik Search `Log Delete 390 {runId}-129`, tekan Enter
2. Klik `⋯` pada baris `Log Delete 390 {runId}-129`, lalu klik `Delete`
3. Klik `[Delete]` pada dialog D-01
4. Tunggu aksi selesai (dialog D-01 tertutup)
5. Klik icon Changelog di Table Tools
6. Ketik Search `Log Delete 390 {runId}-129` di toolbar Modal Changelog, tekan Enter
7. Verifikasi satu entri Delete: Label Name `Log Delete 390 {runId}-129`, Field `Label Name`, Old Value `Log Delete 390 {runId}-129`, New Value `—`
8. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-391: Delete tercatat di System Log aktor

9. Ganti isi kotak search dengan `Log Delete 391 {runId}-129`, tekan Enter
10. Klik `⋯` pada baris `Log Delete 391 {runId}-129`, lalu klik `Delete`
11. Klik `[Delete]` pada dialog D-01
12. Tunggu aksi selesai (dialog D-01 tertutup)
13. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
14. Cari entri dengan Name `Log Delete 391 {runId}-129` di System Log
15. Verifikasi satu entri: Action `Delete`, Object `Labels`, Name `Log Delete 391 {runId}-129`, Field `Label Name`, Old Value `Log Delete 391 {runId}-129`, New Value `—`

### TC-FA-LBL-392: Delete tercatat di Activity Log

16. Buka Fixed Asset > Settings > Asset Master > tab Labels
17. Ketik Search `Log Delete 392 {runId}-129`, tekan Enter
18. Klik `⋯` pada baris `Log Delete 392 {runId}-129`, lalu klik `Delete`
19. Klik `[Delete]` pada dialog D-01
20. Tunggu aksi selesai (dialog D-01 tertutup)
21. Buka Fixed Asset > Activity Log
22. Cari entri dengan Name `Log Delete 392 {runId}-129` di Activity Log
23. Verifikasi satu entri: Action `Delete`, Object `Labels`, Name `Log Delete 392 {runId}-129`, Field `Label Name`, Old Value `Log Delete 392 {runId}-129`, New Value `—`, Modified By `Sarah J`

### TC-FA-LBL-393: Bulk Delete tercatat satu entri Delete per label dengan Date sama di Changelog

24. Buka Fixed Asset > Settings > Asset Master > tab Labels
25. Ketik Search `393 {runId}-129`, tekan Enter
26. Centang baris `Log Bulk A 393 {runId}-129`
27. Centang baris `Log Bulk B 393 {runId}-129`
28. Klik `Bulk Action` lalu klik `Delete`
29. Klik `[Delete]` pada dialog D-03
30. Tunggu aksi selesai (dialog D-03 tertutup)
31. Klik icon Changelog di Table Tools
32. Ketik Search `393 {runId}-129` di toolbar Modal Changelog, tekan Enter
33. Verifikasi dua entri Delete: satu untuk `Log Bulk A 393 {runId}-129` dan satu untuk `Log Bulk B 393 {runId}-129`, masing-masing Field `Label Name`, Old Value nama label, New Value `—`
34. Verifikasi kedua entri tampil berurutan dengan Date (ketelitian menit) yang sama
35. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-394: Bulk Delete tercatat per label di System Log aktor

36. Ganti isi kotak search dengan `394 {runId}-129`, tekan Enter
37. Centang baris `Log Bulk A 394 {runId}-129`
38. Centang baris `Log Bulk B 394 {runId}-129`
39. Klik `Bulk Action` lalu klik `Delete`
40. Klik `[Delete]` pada dialog D-03
41. Tunggu aksi selesai (dialog D-03 tertutup)
42. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
43. Cari entri dengan Name `394 {runId}-129` di System Log
44. Verifikasi dua entri Delete untuk Name `Log Bulk A 394 {runId}-129` dan `Log Bulk B 394 {runId}-129`

### TC-FA-LBL-395: Bulk Delete tercatat per label di Activity Log

45. Buka Fixed Asset > Settings > Asset Master > tab Labels
46. Ketik Search `395 {runId}-129`, tekan Enter
47. Centang baris `Log Bulk A 395 {runId}-129`
48. Centang baris `Log Bulk B 395 {runId}-129`
49. Klik `Bulk Action` lalu klik `Delete`
50. Klik `[Delete]` pada dialog D-03
51. Tunggu aksi selesai (dialog D-03 tertutup)
52. Buka Fixed Asset > Activity Log
53. Cari entri dengan Name `395 {runId}-129` di Activity Log
54. Verifikasi dua entri Delete untuk Name `Log Bulk A 395 {runId}-129` dan `Log Bulk B 395 {runId}-129` dengan Modified By `Sarah J`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target pada Labels List, Search pada Modal Changelog, pencarian entri Name pada System Log dan Activity Log, dan penutupan modal adalah langkah penghubung (nama bersuffix unik, baseline nol, S-12). Perpindahan ke System Log atau Activity Log mengosongkan Labels List sehingga langkah "Buka Fixed Asset > Settings > Asset Master > tab Labels" menyiapkan TC berikutnya.
- Langkah "Tunggu aksi selesai" mengikuti 8b butir 8: hasil aksi tidak diasersi karena Expected TC hanya memuat entri log, dan langkah berikutnya berpindah surface.
- Spec ini di atas smell (54 langkah) karena blok baca-log berpola dikecualikan menurut bagian 3 prinsip 13; selebihnya 35 langkah. Semua blok satu topik (pencatatan Delete dan Bulk Delete) dan berdiri sendiri.
- Asersi "tidak ada entri log" untuk aksi yang ditolak, gagal, atau zero-delta ada di spec absence log nomor 132, 133, 134, dan 173 dengan aksi dan baseline masing-masing (S-05).
- Temuan untuk QA:
  - TC-FA-LBL-393 mengharapkan kedua entri 'tampil berurutan dengan Date (ketelitian menit) yang sama'; kolom Date di UI berketelitian menit sehingga yang teramati hanya kesamaan menit, bukan kesamaan stempel waktu sebenarnya (detik atau milidetik). Spec mengasersi kesamaan Date pada ketelitian menit dan urutan tampil berurutan.
  - TC-FA-LBL-390 sampai 395: Post Condition tidak ada. Dialog Bulk Delete label bersih memakai D-03 (Pre-setup TC section 3d); TC-FA-LBL-393 sampai 395 tidak menyebut nama dialog dan tombol konfirmasinya, spec mengikuti dialog D-03 dengan `[Delete]`.
  - Cara mencari entri pada System Log dan Activity Log (Search atau Filter) tidak dijelaskan di TC; spec memakai nama label bersuffix unik dan kontrol pencarian yang tersedia di surface itu (disediakan tim FE).
