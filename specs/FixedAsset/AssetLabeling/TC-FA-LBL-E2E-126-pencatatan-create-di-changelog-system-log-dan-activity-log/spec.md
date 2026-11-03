---
id: TC-FA-LBL-E2E-126-pencatatan-create-di-changelog-system-log-dan-activity-log
title: "Pencatatan Create di Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-376
  - TC-FA-LBL-377
  - TC-FA-LBL-378
  - TC-FA-LBL-389
  - TC-FA-LBL-408
coverage:
  web: automated
---

# Pencatatan Create di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label dibuat oleh aksi spec lewat UI, nama bersuffix `{runId}-126`, tanpa seed):
  - `Log Create 376 {runId}-126` (TC-FA-LBL-376; Color `Fixture.assetLabeling.hexValid`)
  - `Log Sys 377 {runId}-126` (TC-FA-LBL-377)
  - `Log Act 378 {runId}-126` (TC-FA-LBL-378)
  - Nama diketik dengan spasi tepi: dua spasi + `Log Trim 389 {runId}-126` + dua spasi (TC-FA-LBL-389)
  - `Plus Log 408 {runId}-126` (TC-FA-LBL-408; dibuat lewat `[➕]` pada popup Create Asset Name)
- Data Pre-setup: tidak ada yang dibaca selain akun aktor.
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.hexValid` | `#10B981` |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Surface log dibaca lewat UI pada Modal Changelog: Labels, Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log, dan Fixed Asset > Activity Log; entri dicari berdasarkan nama label bersuffix unik (baseline nol). Kontrol pencarian pada System Log dan Activity Log disediakan tim FE (lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-126`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-376: Create tercatat di Changelog: satu baris Label Name

1. Klik `[+ Label]`
2. Isi Label Name `Log Create 376 {runId}-126`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
4. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
5. Klik `[Submit]`
6. Tunggu aksi selesai (modal Create Label tertutup)
7. Klik icon Changelog di Table Tools
8. Ketik Search `Log Create 376 {runId}-126` di toolbar Modal Changelog, tekan Enter
9. Verifikasi tepat satu entri baru: Action `Create`, Label Name `Log Create 376 {runId}-126`, Field `Label Name`, Old Value `—`, New Value `Log Create 376 {runId}-126`, Modified By `Sarah J`
10. Verifikasi hasil Search tidak memuat baris dengan Field `Color` untuk Create
11. Verifikasi Action pada entri tampil sebagai teks polos tanpa badge
12. Klik `[✕]` pada Modal Changelog

### TC-FA-LBL-377: Create tercatat di System Log aktor

13. Klik `[+ Label]`
14. Isi Label Name `Log Sys 377 {runId}-126`
15. Klik `[Submit]`
16. Tunggu aksi selesai (modal Create Label tertutup)
17. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
18. Cari entri dengan Name `Log Sys 377 {runId}-126` di System Log
19. Verifikasi entri baru: Action `Create`, Object `Labels`, Name `Log Sys 377 {runId}-126`, Field `Label Name`, Old Value `—`, New Value `Log Sys 377 {runId}-126`
20. Verifikasi kolom System Log `Date | Action | Object | Name | Field | Old Value | New Value` tanpa Modified By

### TC-FA-LBL-378: Create tercatat di Activity Log Fixed Asset

21. Buka Fixed Asset > Settings > Asset Master > tab Labels
22. Klik `[+ Label]`
23. Isi Label Name `Log Act 378 {runId}-126`
24. Klik `[Submit]`
25. Tunggu aksi selesai (modal Create Label tertutup)
26. Buka Fixed Asset > Activity Log
27. Cari entri dengan Name `Log Act 378 {runId}-126` di Activity Log
28. Verifikasi entri baru: Action `Create`, Object `Labels`, Name `Log Act 378 {runId}-126`, Field `Label Name`, Old Value `—`, New Value `Log Act 378 {runId}-126`, Modified By `Sarah J`

### TC-FA-LBL-389: Nama tersimpan ter-trim dipakai di Changelog, System Log, dan Activity Log

29. Buka Fixed Asset > Settings > Asset Master > tab Labels
30. Klik `[+ Label]`
31. Isi Label Name dengan dua spasi + `Log Trim 389 {runId}-126` + dua spasi
32. Klik `[Submit]`
33. Tunggu aksi selesai (modal Create Label tertutup)
34. Klik icon Changelog di Table Tools
35. Ketik Search `Log Trim 389 {runId}-126` di toolbar Modal Changelog, tekan Enter
36. Verifikasi New Value dan Label Name pada entri Create di Changelog adalah `Log Trim 389 {runId}-126` tanpa spasi tepi
37. Klik `[✕]` pada Modal Changelog
38. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
39. Cari entri dengan Name `Log Trim 389 {runId}-126` di System Log
40. Verifikasi New Value dan Name pada entri Create di System Log adalah `Log Trim 389 {runId}-126` tanpa spasi tepi
41. Buka Fixed Asset > Activity Log
42. Cari entri dengan Name `Log Trim 389 {runId}-126` di Activity Log
43. Verifikasi New Value dan Name pada entri Create di Activity Log adalah `Log Trim 389 {runId}-126` tanpa spasi tepi

### TC-FA-LBL-408: Create lewat tombol [➕] tercatat sama seperti [+ Label]

44. Buka Fixed Asset > Settings > Asset Master > tab `Asset Name`
45. Klik `[+ Asset Name]` untuk membuka popup Create Asset Name
46. Klik tombol `[➕]` pada field Default Label untuk membuka modal Create Label
47. Isi Label Name `Plus Log 408 {runId}-126`
48. Klik `[Submit]`
49. Tunggu aksi selesai (modal Create Label tertutup)
50. Klik icon `[✕]` pada popup Create Asset Name
51. Klik tab `Labels`
52. Klik icon Changelog di Table Tools
53. Ketik Search `Plus Log 408 {runId}-126` di toolbar Modal Changelog, tekan Enter
54. Verifikasi satu entri Create identik bentuknya dengan entri langkah 9: Action `Create`, Label Name `Plus Log 408 {runId}-126`, Field `Label Name`, Old Value `—`, New Value `Plus Log 408 {runId}-126`, Modified By `Sarah J`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search pada Modal Changelog, pencarian entri Name pada System Log dan Activity Log, dan penutupan modal adalah langkah untuk menemukan entri milik spec (nama bersuffix unik, baseline nol, S-12); bukan bagian Expected TC. Perpindahan ke System Log atau Activity Log mengosongkan Labels List sehingga langkah "Buka Fixed Asset > Settings > Asset Master > tab Labels" menyiapkan TC berikutnya.
- Langkah "Tunggu aksi selesai" mengikuti 8b butir 8: hasil `[Submit]` tidak diasersi karena Expected TC hanya memuat entri log, dan langkah berikutnya berpindah surface.
- Spec ini melewati 35 langkah (di atas smell: 54 langkah) karena blok baca-log berpola (buka surface, cari entri, Verifikasi kolom log) dikecualikan dari hitungan menurut bagian 3 prinsip 13; selebihnya 30 langkah. Semua blok satu topik (pencatatan Create) dan berdiri sendiri: kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Asersi "tidak ada entri log" untuk aksi yang ditolak, gagal, atau zero-delta ada di spec absence log nomor 132, 133, 134, dan 173 dengan aksi dan baseline masing-masing (S-05).
- Temuan untuk QA:
  - TC-FA-LBL-376 sampai 378 dan 389: Post Condition tidak ada. TC-FA-LBL-377 menyebut kolom System Log "tanpa Modified By" sebagai bagian Expected dan diasersi di langkah 20.
  - Cara mencari entri pada System Log dan Activity Log (Search atau Filter) tidak dijelaskan di TC; spec memakai nama label bersuffix unik dan kontrol pencarian yang tersedia di surface itu (disediakan tim FE).
  - TC-FA-LBL-408 (Pre: pengguna berada di tab Asset Name) tidak menjelaskan alur membuka modal Create Label; spec memakai alur tombol `[➕]` pada popup Create Asset Name seperti dalam Data Dinamis TC dan Expected "identik bentuknya dengan Create lewat `[+ Label]`" ditulis sebagai kesamaan kolom entri dengan langkah 9.
