---
id: TC-FA-LBL-E2E-130-snapshot-log-immutable-label-hasil-import-dan-kolom-tiap-surface
title: "Snapshot Log Immutable, Label Hasil Import, dan Kolom Tiap Surface"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-404
  - TC-FA-LBL-405
  - TC-FA-LBL-407
  - TC-FA-LBL-411
coverage:
  web: automated
---

# Snapshot Log Immutable, Label Hasil Import, dan Kolom Tiap Surface

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (milik spec, nama bersuffix `{runId}-130`):
  - Label seed bersih (dibuat lewat fixture BE di hook `before` melalui jalur yang menulis entri Create; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label): `Snap A 404 {runId}-130` (TC-FA-LBL-404), `Snap Del 405 {runId}-130` (TC-FA-LBL-405)
  - Nama sesudah perubahan: `Snap B 404 {runId}-130`, `Snap C 404 {runId}-130` (TC-FA-LBL-404), `Snap Del 405 X {runId}-130` (TC-FA-LBL-405)
  - Default Label `Imported Label 407 {runId}-130` belum ada di katalog. Pembuat berkas Import Asset Name per run (kemampuan disediakan tim FE/BE, Pre-setup #14; TC-FA-LBL-407) menyusun berkas yang memuat Asset Name bersuffix `{runId}-130` dengan Default Label `Imported Label 407 {runId}-130`; Import `[Create Missing Labels]` membuat label itu dan relasi Asset Name dengan Default Label (data hasil Import, milik spec ini)
- Data Pre-setup: Import Asset Name (Pre-setup #14), hanya akun aktor dan berkas Import yang dibaca.
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.warnaDefault` | `#3B82F6` (warna default label hasil Import) |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Surface log dibaca lewat UI pada Modal Changelog: Labels, Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log, dan Fixed Asset > Activity Log; entri dicari berdasarkan nama label bersuffix unik (baseline nol). Kontrol pencarian pada System Log dan Activity Log disediakan tim FE (lihat Temuan untuk QA). Import Asset Name dengan opsi `[Create Missing Labels]` dijalankan lewat UI tab Asset Name (kontrol Import mengikuti TC `import/`; lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` lebih dulu menghapus Asset Name hasil Import (bersuffix `{runId}-130`, beserta relasi Default Label ke `Imported Label 407 {runId}-130`) lewat fixture BE, karena label yang menjadi Default Label dari sebuah Asset Name tidak dapat dihapus; sesudah itu menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-130`, termasuk yang sudah berganti nama dan label hasil Import) lewat fixture BE berdasarkan ID, tanpa berasumsi seed atau Import berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-404: Rename kedua kali tidak mengubah entri lama (snapshot immutability)

1. Ketik Search `Snap A 404 {runId}-130`, tekan Enter
2. Klik `⋯` pada baris `Snap A 404 {runId}-130`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Snap B 404 {runId}-130`
4. Klik `[Save]`
5. Tunggu aksi selesai (modal Edit Label tertutup)
6. Ganti isi kotak search dengan `Snap B 404 {runId}-130`, tekan Enter
7. Klik `⋯` pada baris `Snap B 404 {runId}-130`, lalu klik `Edit`
8. Ganti isi Label Name dengan `Snap C 404 {runId}-130`
9. Klik `[Save]`
10. Tunggu aksi selesai (modal Edit Label tertutup)
11. Klik icon Changelog di Table Tools
12. Ketik Search `404 {runId}-130` di toolbar Modal Changelog, tekan Enter
13. Verifikasi entri rename pertama tetap Old Value `Snap A 404 {runId}-130` dan New Value `Snap B 404 {runId}-130`
14. Verifikasi entri rename kedua Old Value `Snap B 404 {runId}-130` dan New Value `Snap C 404 {runId}-130`
15. Verifikasi kolom Label Name entri pertama tetap `Snap B 404 {runId}-130` dan entri kedua `Snap C 404 {runId}-130` (nama sesudah perubahan saat itu)
16. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-405: Entri log tetap setelah label dihapus

17. Ganti isi kotak search dengan `Snap Del 405 {runId}-130`, tekan Enter
18. Klik `⋯` pada baris `Snap Del 405 {runId}-130`, lalu klik `Edit`
19. Ganti isi Label Name dengan `Snap Del 405 X {runId}-130`
20. Klik `[Save]`
21. Tunggu aksi selesai (modal Edit Label tertutup)
22. Ganti isi kotak search dengan `Snap Del 405 X {runId}-130`, tekan Enter
23. Klik `⋯` pada baris `Snap Del 405 X {runId}-130`, lalu klik `Delete`
24. Klik `[Delete]` pada dialog D-01
25. Tunggu aksi selesai (dialog D-01 tertutup)
26. Klik icon Changelog di Table Tools
27. Ketik Search `{runId}-130` di toolbar Modal Changelog, tekan Enter
28. Verifikasi entri Create, Edit, dan Delete label itu tampil dengan nilai asli saat peristiwa: Create `Snap Del 405 {runId}-130`, Edit Old Value `Snap Del 405 {runId}-130` New Value `Snap Del 405 X {runId}-130`, Delete Old Value `Snap Del 405 X {runId}-130`
29. Klik icon Filter di toolbar Modal Changelog dan buka dropdown Label Name
30. Verifikasi dropdown filter Label Name masih menampilkan opsi `Snap Del 405 X {runId}-130`
31. Tekan Esc untuk menutup dropdown, lalu klik `[✕]` pada Modal Changelog

### TC-FA-LBL-407: Label hasil Import [Create Missing Labels] tercatat sebagai Create biasa dengan warna default

32. Buka Fixed Asset > Settings > Asset Master > tab `Asset Name`
33. Jalankan Import Asset Name dengan berkas berisi Default Label `Imported Label 407 {runId}-130` yang belum ada dan pilih opsi `[Create Missing Labels]`
34. Tunggu aksi selesai (Import selesai)
35. Klik tab `Labels`
36. Klik icon Changelog di Table Tools
37. Ketik Search `Imported Label 407 {runId}-130` di toolbar Modal Changelog, tekan Enter
38. Verifikasi satu entri Create di Changelog untuk `Imported Label 407 {runId}-130`: Field `Label Name`, Old Value `—`, New Value `Imported Label 407 {runId}-130`, tanpa qualifier `(Import)`
39. Klik `[✕]` pada Modal Changelog
40. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
41. Cari entri dengan Name `Imported Label 407 {runId}-130` di System Log
42. Verifikasi satu entri Create di System Log aktor untuk `Imported Label 407 {runId}-130`: Field `Label Name`, Old Value `—`, New Value `Imported Label 407 {runId}-130`, tanpa qualifier `(Import)`
43. Buka Fixed Asset > Activity Log
44. Cari entri dengan Name `Imported Label 407 {runId}-130` di Activity Log
45. Verifikasi satu entri Create di Activity Log untuk `Imported Label 407 {runId}-130`: Field `Label Name`, Old Value `—`, New Value `Imported Label 407 {runId}-130`, tanpa qualifier `(Import)`
46. Buka Fixed Asset > Settings > Asset Master > tab Labels
47. Ketik Search `Imported Label 407 {runId}-130`, tekan Enter
48. Verifikasi baris `Imported Label 407 {runId}-130` berwarna default `Fixture.assetLabeling.warnaDefault`
49. Verifikasi kolom Modified By baris `Imported Label 407 {runId}-130` menampilkan pengguna yang menjalankan Import (`Sarah J`)

### TC-FA-LBL-411: Kolom tabel per surface log sesuai definisi PRD

50. Klik icon Changelog di Table Tools
51. Ketik Search `{runId}-130` di toolbar Modal Changelog, tekan Enter
52. Verifikasi header Changelog: `Date | Action | Label Name | Field | Old Value | New Value | Modified By`
53. Klik `[✕]` pada Modal Changelog
54. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
55. Verifikasi header System Log: `Date | Action | Object | Name | Field | Old Value | New Value`
56. Cari entri dengan Name `Imported Label 407 {runId}-130` di System Log
57. Verifikasi kolom Object entri bernilai `Labels` di System Log
58. Buka Fixed Asset > Activity Log
59. Verifikasi header Activity Log: `Date | Action | Object | Name | Field | Old Value | New Value | Modified By`
60. Cari entri dengan Name `Imported Label 407 {runId}-130` di Activity Log
61. Verifikasi kolom Object entri bernilai `Labels` di Activity Log

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target pada Labels List, Search pada Modal Changelog, pencarian entri Name pada System Log dan Activity Log, dan penutupan modal adalah langkah penghubung (nama bersuffix unik, baseline nol, S-12). Perpindahan ke System Log atau Activity Log mengosongkan Labels List sehingga langkah "Buka Fixed Asset > Settings > Asset Master > tab Labels" menyiapkan TC berikutnya.
- Langkah "Tunggu aksi selesai" mengikuti 8b butir 8: hasil aksi tidak diasersi karena Expected TC hanya memuat entri log, dan langkah berikutnya berpindah surface.
- Spec ini melewati 35 langkah (di atas smell: 61 langkah) karena blok baca-log berpola dikecualikan menurut bagian 3 prinsip 13; selebihnya 31 langkah. Semua blok satu topik (pencatatan, snapshot, dan kolom surface log) dan berdiri sendiri.
- Urutan TC: TC-FA-LBL-411 di akhir karena memakai entri Create hasil Import TC-FA-LBL-407 sebagai baris bernilai Object `Labels` pada System Log dan Activity Log.
- Asersi "tidak ada entri log" untuk aksi yang ditolak, gagal, atau zero-delta ada di spec absence log nomor 132, 133, 134, dan 173 dengan aksi dan baseline masing-masing (S-05).
- Temuan untuk QA:
  - TC-FA-LBL-404, 405, 407, dan 411: Post Condition tidak ada. TC-FA-LBL-405 menyebut entri Create ada; entri itu hanya ada bila seed memakai jalur yang menulis log Create, sehingga seeding label itu bergantung pada kemampuan fixture BE yang disediakan tim FE/BE.
  - Cleanup hasil Import TC-FA-LBL-407 (menghapus Asset Name dan relasi Default Label lewat fixture BE sebelum menghapus label) serta kemampuan pembuat berkas Import per run bergantung pada dukungan tim FE/BE; menunggu konfirmasi FE/BE (D-11, F-307).
  - TC-FA-LBL-407 tidak merinci langkah UI Import (halaman, berkas, dan tombol); spec menulis satu langkah aksi Import dan mekanisme rincinya mengikuti TC `import/` yang memilikinya.
  - Cara mencari entri pada System Log dan Activity Log (Search atau Filter) tidak dijelaskan di TC; spec memakai nama label bersuffix unik dan kontrol pencarian yang tersedia di surface itu (disediakan tim FE).
