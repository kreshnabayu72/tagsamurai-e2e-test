---
id: TC-FA-LBL-E2E-127-pencatatan-edit-nama-di-tiga-surface
title: "Pencatatan Edit Nama di Tiga Surface dan Pembaruan Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-379
  - TC-FA-LBL-380
  - TC-FA-LBL-381
  - TC-FA-LBL-388
  - TC-FA-LBL-406
coverage:
  web: automated
---

# Pencatatan Edit Nama di Tiga Surface dan Pembaruan Modified By

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-127`):
  - `Log Edit 379 {runId}-127` (TC-FA-LBL-379)
  - `Log Edit 380 {runId}-127` (TC-FA-LBL-380)
  - `Log Edit 381 {runId}-127` (TC-FA-LBL-381)
  - `Log Edit 388 {runId}-127` (TC-FA-LBL-388)
  - `Log Edit 406 {runId}-127` (TC-FA-LBL-406)
- Role yang diuji pada TC-FA-LBL-406: Full-CRUD Company Alpha (Pre-setup #7) `fullCrud_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.fullCrud`, password `Spectra.env.FA_FULLCRUD_PASSWORD`; dipakai lewat langkah Ganti akun (langkah 38), lalu Total Control Company Alpha kembali lewat langkah Ganti akun (langkah 45).
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.hexValid` | `#10B981` |
  | `Fixture.assetLabeling.fullCrud.modifiedByDisplay` | nama tampil Full-CRUD pada kolom Modified By berformat `[First Name] [Last Initial]` (R-14) |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Surface log dibaca lewat UI pada Modal Changelog: Labels, Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log, dan Fixed Asset > Activity Log; entri dicari berdasarkan nama label bersuffix unik (baseline nol). Kontrol pencarian pada System Log dan Activity Log disediakan tim FE (lihat Temuan untuk QA). Jam server dan jam browser sinkron untuk asersi Last Updated (S-12).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-127`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` dan `Spectra.env.FA_FULLCRUD_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-379: Edit nama tercatat di Changelog: satu baris Label Name

1. Ketik Search `Log Edit 379 {runId}-127`, tekan Enter
2. Klik `⋯` pada baris `Log Edit 379 {runId}-127`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Log Edit 379 Baru {runId}-127`
4. Klik `[Save]`
5. Tunggu aksi selesai (modal Edit Label tertutup)
6. Klik icon Changelog di Table Tools
7. Ketik Search `Log Edit 379 Baru {runId}-127` di toolbar Modal Changelog, tekan Enter
8. Verifikasi satu entri Edit: Label Name `Log Edit 379 Baru {runId}-127` (nama sesudah perubahan), Field `Label Name`, Old Value `Log Edit 379 {runId}-127`, New Value `Log Edit 379 Baru {runId}-127`
9. Verifikasi hasil Search tidak memuat baris untuk Field `Color`
10. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-380: Edit nama tercatat di System Log aktor

11. Ganti isi kotak search dengan `Log Edit 380 {runId}-127`, tekan Enter
12. Klik `⋯` pada baris `Log Edit 380 {runId}-127`, lalu klik `Edit`
13. Ganti isi Label Name dengan `Log Edit 380 Baru {runId}-127`
14. Klik `[Save]`
15. Tunggu aksi selesai (modal Edit Label tertutup)
16. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
17. Cari entri dengan Name `Log Edit 380 Baru {runId}-127` di System Log
18. Verifikasi satu entri: Action `Edit`, Object `Labels`, Name `Log Edit 380 Baru {runId}-127`, Field `Label Name`, Old Value `Log Edit 380 {runId}-127`, New Value `Log Edit 380 Baru {runId}-127`

### TC-FA-LBL-381: Edit nama tercatat di Activity Log

19. Buka Fixed Asset > Settings > Asset Master > tab Labels
20. Ketik Search `Log Edit 381 {runId}-127`, tekan Enter
21. Klik `⋯` pada baris `Log Edit 381 {runId}-127`, lalu klik `Edit`
22. Ganti isi Label Name dengan `Log Edit 381 Baru {runId}-127`
23. Klik `[Save]`
24. Tunggu aksi selesai (modal Edit Label tertutup)
25. Buka Fixed Asset > Activity Log
26. Cari entri dengan Name `Log Edit 381 Baru {runId}-127` di Activity Log
27. Verifikasi satu entri: Action `Edit`, Object `Labels`, Name `Log Edit 381 Baru {runId}-127`, Field `Label Name`, Old Value `Log Edit 381 {runId}-127`, New Value `Log Edit 381 Baru {runId}-127`, Modified By `Sarah J`

### TC-FA-LBL-388: Edit hanya kapitalisasi nama tercatat sebagai perubahan nyata

28. Buka Fixed Asset > Settings > Asset Master > tab Labels
29. Ketik Search `Log Edit 388 {runId}-127`, tekan Enter
30. Klik `⋯` pada baris `Log Edit 388 {runId}-127`, lalu klik `Edit`
31. Ganti isi Label Name dengan `LOG EDIT 388 {runId}-127`
32. Klik `[Save]`
33. Tunggu aksi selesai (modal Edit Label tertutup)
34. Klik icon Changelog di Table Tools
35. Ketik Search `LOG EDIT 388 {runId}-127` di toolbar Modal Changelog, tekan Enter
36. Verifikasi satu entri Edit: Field `Label Name`, Old Value `Log Edit 388 {runId}-127`, New Value `LOG EDIT 388 {runId}-127`
37. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-406: Edit nyata memperbarui Modified By dan Last Updated, Edit zero-delta tidak

38. Ganti akun: Logout, login sebagai Full-CRUD `Fixture.assetLabeling.akun.fullCrud` (`Spectra.env.FA_FULLCRUD_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
39. Ketik Search `Log Edit 406 {runId}-127`, tekan Enter
40. Klik `⋯` pada baris `Log Edit 406 {runId}-127`, lalu klik `Edit`
41. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
42. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
43. Klik `[Save]`
44. Tunggu aksi selesai (modal Edit Label tertutup), lalu catat waktu simpan
45. Ganti akun: Logout, login sebagai Total Control Company Alpha `Fixture.assetLabeling.akun.totalControl` (`Spectra.env.FA_LBL_TC_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
46. Ketik Search `Log Edit 406 {runId}-127`, tekan Enter
47. Verifikasi Modified By baris `Log Edit 406 {runId}-127` adalah `Fixture.assetLabeling.fullCrud.modifiedByDisplay`
48. Verifikasi Last Updated baris `Log Edit 406 {runId}-127` sesuai waktu simpan (toleransi satu menit)
49. Klik `⋯` pada baris `Log Edit 406 {runId}-127`, lalu klik `Edit`
50. Klik `[Save]` tanpa mengubah nama maupun warna
51. Tunggu aksi selesai (modal Edit Label tertutup)
52. Verifikasi Modified By baris `Log Edit 406 {runId}-127` tetap seperti pada langkah 47
53. Verifikasi Last Updated baris `Log Edit 406 {runId}-127` tetap seperti pada langkah 48

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target pada Labels List, Search pada Modal Changelog, pencarian entri Name pada System Log dan Activity Log, dan penutupan modal adalah langkah penghubung (nama bersuffix unik, baseline nol, S-12). Search pada Labels List diganti ke nama baru sesudah rename agar baris yang tersimpan tampil.
- Langkah "Tunggu aksi selesai" mengikuti 8b butir 8: hasil `[Save]` tidak diasersi dan langkah berikutnya berpindah surface.
- Langkah 38 dan 45 adalah Ganti akun eksplisit (S-07); hook `after` suite mengembalikan sesi ke akun default suite.
- Spec ini melewati 35 langkah (di atas smell: 53 langkah) karena blok baca-log berpola dikecualikan menurut bagian 3 prinsip 13; selebihnya 40 langkah. Semua blok satu topik (pencatatan Edit nama dan pembaruan Modified By hasil Edit) dan berdiri sendiri.
- Asersi "tidak ada entri log" untuk aksi yang ditolak, gagal, atau zero-delta ada di spec absence log nomor 132, 133, 134, dan 173 dengan aksi dan baseline masing-masing (S-05).
- Temuan untuk QA:
  - TC-FA-LBL-379 sampai 381 dan 388: Post Condition tidak ada. TC-FA-LBL-406 Expected a menyebut Last Updated "waktu simpan" tanpa menyatakan cara membaca waktu itu; spec mencatat waktu sesudah aksi dan membandingkan dengan toleransi satu menit (S-12).
  - TC-FA-LBL-406 menyatakan Modified By sebagai "pengguna Full-CRUD" tanpa nama tampil; spec memakai nilai fixture berformat `[First Name] [Last Initial]` (R-14).
