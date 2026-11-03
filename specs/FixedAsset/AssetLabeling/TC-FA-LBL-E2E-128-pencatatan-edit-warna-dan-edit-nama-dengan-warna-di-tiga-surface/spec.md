---
id: TC-FA-LBL-E2E-128-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface
title: "Pencatatan Edit Warna dan Edit Nama dengan Warna di Tiga Surface (bagian 1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-382
  - TC-FA-LBL-383
  - TC-FA-LBL-384
coverage:
  web: automated
---

# Pencatatan Edit Warna dan Edit Nama dengan Warna di Tiga Surface (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-128`):
  - `Log Edit 382 {runId}-128` (TC-FA-LBL-382)
  - `Log Edit 383 {runId}-128` (TC-FA-LBL-383)
  - `Log Edit 384 {runId}-128` (TC-FA-LBL-384)
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.hexValid` | `#10B981` |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Surface log dibaca lewat UI pada Modal Changelog: Labels, Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log, dan Fixed Asset > Activity Log; entri dicari berdasarkan nama label bersuffix unik (baseline nol). Kontrol pencarian pada System Log dan Activity Log disediakan tim FE (lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-128`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-382: Edit warna tercatat di Changelog: satu baris Color

1. Ketik Search `Log Edit 382 {runId}-128`, tekan Enter
2. Klik `⋯` pada baris `Log Edit 382 {runId}-128`, lalu klik `Edit`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
4. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
5. Klik `[Save]`
6. Tunggu aksi selesai (modal Edit Label tertutup)
7. Klik icon Changelog di Table Tools
8. Ketik Search `Log Edit 382 {runId}-128` di toolbar Modal Changelog, tekan Enter
9. Verifikasi satu entri Edit: Label Name `Log Edit 382 {runId}-128`, Field `Color`, Old Value `Fixture.assetLabeling.warnaSeed`, New Value `Fixture.assetLabeling.hexValid`
10. Verifikasi hasil Search tidak memuat baris untuk Field `Label Name`
11. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-383: Edit warna tercatat di System Log aktor

12. Ketik Search `Log Edit 383 {runId}-128`, tekan Enter
13. Klik `⋯` pada baris `Log Edit 383 {runId}-128`, lalu klik `Edit`
14. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
15. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
16. Klik `[Save]`
17. Tunggu aksi selesai (modal Edit Label tertutup)
18. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
19. Cari entri dengan Name `Log Edit 383 {runId}-128` di System Log
20. Verifikasi satu entri: Action `Edit`, Object `Labels`, Name `Log Edit 383 {runId}-128`, Field `Color`, Old Value `Fixture.assetLabeling.warnaSeed`, New Value `Fixture.assetLabeling.hexValid`

### TC-FA-LBL-384: Edit warna tercatat di Activity Log

21. Buka Fixed Asset > Settings > Asset Master > tab Labels
22. Ketik Search `Log Edit 384 {runId}-128`, tekan Enter
23. Klik `⋯` pada baris `Log Edit 384 {runId}-128`, lalu klik `Edit`
24. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
25. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
26. Klik `[Save]`
27. Tunggu aksi selesai (modal Edit Label tertutup)
28. Buka Fixed Asset > Activity Log
29. Cari entri dengan Name `Log Edit 384 {runId}-128` di Activity Log
30. Verifikasi satu entri: Action `Edit`, Object `Labels`, Name `Log Edit 384 {runId}-128`, Field `Color`, Old Value `Fixture.assetLabeling.warnaSeed`, New Value `Fixture.assetLabeling.hexValid`, Modified By `Sarah J`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target pada Labels List, Search pada Modal Changelog, pencarian entri Name pada System Log dan Activity Log, dan penutupan modal adalah langkah penghubung (nama bersuffix unik, baseline nol, S-12). Perpindahan ke System Log atau Activity Log mengosongkan Labels List sehingga langkah "Buka Fixed Asset > Settings > Asset Master > tab Labels" (langkah 21) menyiapkan TC berikutnya.
- Langkah "Tunggu aksi selesai" mengikuti 8b butir 8: hasil aksi tidak diasersi karena Expected TC hanya memuat entri log, dan langkah berikutnya berpindah surface.
- Asersi "tidak ada entri log" untuk aksi yang ditolak, gagal, atau zero-delta ada di spec absence log nomor 132, 133, 134, dan 173 dengan aksi dan baseline masing-masing (S-05).
- Pembagian TC lintas spec: pencatatan Edit nama dan warna sekaligus (TC-FA-LBL-385, 386, 387) ada di spec 179.
- Temuan untuk QA:
  - TC-FA-LBL-382 sampai 384: Post Condition tidak ada.
  - Cara mencari entri pada System Log dan Activity Log (Search atau Filter) tidak dijelaskan di TC; spec memakai nama label bersuffix unik dan kontrol pencarian yang tersedia di surface itu (disediakan tim FE).
