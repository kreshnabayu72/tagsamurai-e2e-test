---
id: TC-FA-LBL-E2E-048-menutup-form-edit-reload-dan-pindah-route-saat-form-berubah
title: "Menutup Form Edit: Reload dan Pindah Route Saat Form Berubah"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-152
  - TC-FA-LBL-153
coverage:
  web: automated
---

# Menutup Form Edit: Reload dan Pindah Route Saat Form Berubah

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-048`):
  - `Edit Target 152 {runId}-048` (TC-FA-LBL-152)
  - `Edit Target 153 {runId}-048` (TC-FA-LBL-153)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: menangani dialog bawaan browser `beforeunload` (menerima atau membatalkan) pada reload F5 (S-08).
- Item menu lain pada sidebar yang diklik TC-FA-LBL-153: disediakan tim FE (TC tidak menyebut item tertentu).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-152: Form Edit yang berubah memicu konfirmasi bawaan browser saat reload

1. Ketik Search `Edit Target 152 {runId}-048`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 152 {runId}-048`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Reload Edit 152 {runId}-048`
4. Tekan F5
5. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
6. Terima dialog beforeunload sehingga halaman dimuat ulang

### TC-FA-LBL-153: Berpindah route internal saat form Edit berubah memunculkan dialog Unsaved Changes

7. Ketik Search `Edit Target 153 {runId}-048`, tekan Enter
8. Klik `⋯` pada baris `Edit Target 153 {runId}-048`, lalu klik `Edit`
9. Ganti isi Label Name dengan `Route Edit 153 {runId}-048`
10. Klik satu item menu lain pada sidebar
11. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
12. Klik `[Cancel]`
13. Verifikasi tetap berada di form Edit
14. Verifikasi input `Route Edit 153 {runId}-048` dipertahankan
15. Klik item menu lain pada sidebar yang sama lagi, lalu klik `[Leave]`
16. Verifikasi navigasi berlanjut ke halaman item menu yang diklik
17. Verifikasi form Edit tidak lagi tampil
18. Buka kembali Settings > Asset Master > tab Labels
19. Ketik Search `Edit Target 153 {runId}-048`, tekan Enter
20. Verifikasi baris `Edit Target 153 {runId}-048` tampil dengan nama tidak berubah

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 7, 19 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03, S-08): langkah 6, 18 menerima dialog `beforeunload` (form dirty dibuang oleh reload) dan membuka kembali tab Labels untuk memeriksa bahwa TC-FA-LBL-153 tidak menyimpan perubahan.
- TC-FA-LBL-147, 148, dan 150 ada di spec nomor 047; TC-FA-LBL-149 dan 151 ada di spec nomor 161.
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
- Temuan untuk QA:
  - TC-FA-LBL-153 langkah 3 dan 5 menyebut "item menu lain pada sidebar" tanpa menamai item; spec memakai item yang disediakan tim FE.
  - TC-FA-LBL-153 Expected c ("navigasi berlanjut dan form tertutup tanpa menyimpan") tidak punya langkah pengamatan nama; spec membuka kembali tab Labels dan memeriksa nama label seed tidak berubah.
