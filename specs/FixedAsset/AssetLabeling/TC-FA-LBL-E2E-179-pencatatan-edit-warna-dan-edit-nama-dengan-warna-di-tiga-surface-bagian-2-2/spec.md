---
id: TC-FA-LBL-E2E-179-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface-bagian-2-2
title: "Pencatatan Edit Warna dan Edit Nama dengan Warna di Tiga Surface (bagian 2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-385
  - TC-FA-LBL-386
  - TC-FA-LBL-387
coverage:
  web: automated
---

# Pencatatan Edit Warna dan Edit Nama dengan Warna di Tiga Surface (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-179`):
  - `Log Edit 385 {runId}-179` (TC-FA-LBL-385)
  - `Log Edit 386 {runId}-179` (TC-FA-LBL-386)
  - `Log Edit 387 {runId}-179` (TC-FA-LBL-387)
  - Nama sesudah perubahan: `Log Both 385 {runId}-179`, `Log Both 386 {runId}-179`, `Log Both 387 {runId}-179`
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.hexValid` | `#10B981` |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Surface log dibaca lewat UI pada Modal Changelog: Labels, Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log, dan Fixed Asset > Activity Log; entri dicari berdasarkan nama label bersuffix unik (baseline nol). Kontrol pencarian pada System Log dan Activity Log disediakan tim FE (lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-179`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-385: Edit nama dan warna sekaligus menghasilkan dua baris di Changelog

1. Ketik Search `Log Edit 385 {runId}-179`, tekan Enter
2. Klik `⋯` pada baris `Log Edit 385 {runId}-179`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Log Both 385 {runId}-179`
4. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
5. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
6. Klik `[Save]`
7. Tunggu aksi selesai (modal Edit Label tertutup)
8. Klik icon Changelog di Table Tools
9. Ketik Search `Log Both 385 {runId}-179` di toolbar Modal Changelog, tekan Enter
10. Verifikasi entri Edit dengan Field `Label Name`: Old Value `Log Edit 385 {runId}-179`, New Value `Log Both 385 {runId}-179`
11. Verifikasi entri Edit dengan Field `Color`: Old Value `Fixture.assetLabeling.warnaSeed`, New Value `Fixture.assetLabeling.hexValid`
12. Verifikasi hasil Search memuat tepat dua entri Edit (tidak hilang salah satu dan tidak ganda)
13. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-386: Edit nama dan warna sekaligus menghasilkan dua baris di System Log aktor

14. Ketik Search `Log Edit 386 {runId}-179`, tekan Enter
15. Klik `⋯` pada baris `Log Edit 386 {runId}-179`, lalu klik `Edit`
16. Ganti isi Label Name dengan `Log Both 386 {runId}-179`
17. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
18. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
19. Klik `[Save]`
20. Tunggu aksi selesai (modal Edit Label tertutup)
21. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
22. Cari entri dengan Name `Log Both 386 {runId}-179` di System Log
23. Verifikasi dua entri Edit untuk Field `Label Name` dan Field `Color` dengan Name `Log Both 386 {runId}-179`

### TC-FA-LBL-387: Edit nama dan warna sekaligus menghasilkan dua baris di Activity Log

24. Buka Fixed Asset > Settings > Asset Master > tab Labels
25. Ketik Search `Log Edit 387 {runId}-179`, tekan Enter
26. Klik `⋯` pada baris `Log Edit 387 {runId}-179`, lalu klik `Edit`
27. Ganti isi Label Name dengan `Log Both 387 {runId}-179`
28. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
29. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
30. Klik `[Save]`
31. Tunggu aksi selesai (modal Edit Label tertutup)
32. Buka Fixed Asset > Activity Log
33. Cari entri dengan Name `Log Both 387 {runId}-179` di Activity Log
34. Verifikasi dua entri Edit untuk Field `Label Name` dan Field `Color` dengan Name `Log Both 387 {runId}-179`, masing-masing Modified By `Sarah J`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target pada Labels List, Search pada Modal Changelog, pencarian entri Name pada System Log dan Activity Log, dan penutupan modal adalah langkah penghubung (nama bersuffix unik, baseline nol, S-12). Perpindahan ke System Log atau Activity Log mengosongkan Labels List sehingga langkah "Buka Fixed Asset > Settings > Asset Master > tab Labels" (langkah 24) menyiapkan TC berikutnya.
- Langkah "Tunggu aksi selesai" mengikuti 8b butir 8: hasil aksi tidak diasersi karena Expected TC hanya memuat entri log, dan langkah berikutnya berpindah surface.
- Asersi "tidak ada entri log" untuk aksi yang ditolak, gagal, atau zero-delta ada di spec absence log nomor 132, 133, 134, dan 173 dengan aksi dan baseline masing-masing (S-05).
- Pembagian TC lintas spec: pencatatan Edit warna saja (TC-FA-LBL-382, 383, 384) ada di spec 128.
- Temuan untuk QA:
  - TC-FA-LBL-385 sampai 387: Post Condition tidak ada. Expected TC-FA-LBL-386 dan 387 tidak merinci Old Value dan New Value; spec mengikuti TC dan hanya mengasersi Action, Field, Name, dan Modified By yang disebut.
  - Cara mencari entri pada System Log dan Activity Log (Search atau Filter) tidak dijelaskan di TC; spec memakai nama label bersuffix unik dan kontrol pencarian yang tersedia di surface itu (disediakan tim FE).
