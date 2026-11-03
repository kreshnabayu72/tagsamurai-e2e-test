---
id: TC-FA-LBL-E2E-162-edit-live-preview-dan-clear-field
title: "Edit: Live Preview dan Clear Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-132
  - TC-FA-LBL-133
coverage:
  web: automated
---

# Edit: Live Preview dan Clear Field

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Tidak ada kasus di spec ini yang menyimpan perubahan.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-162`):
  - `Edit Target 133 {runId}-162` (satu label seed untuk kedua TC; tidak ada yang disimpan)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.warnaDefault` | `#3B82F6` (warna default sesudah [Clear Field]) |
  | `Fixture.assetLabeling.hexValid` | `#10B981` |

- Kemampuan teknis: mengetik ke Label Name dan kolom Hex serta menekan Esc.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `Edit Target 133 {runId}-162`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 133 {runId}-162`, lalu klik `Edit`

### TC-FA-LBL-133: Edit: Clear Field mengosongkan nama dan mengembalikan warna ke default, bukan ke nilai tersimpan

3. Ketik `Dirty 133` di Label Name
4. Klik `[Clear Field]`
5. Verifikasi Label Name kosong
6. Verifikasi Color menjadi `Fixture.assetLabeling.warnaDefault` (bukan `Fixture.assetLabeling.warnaSeed` nilai tersimpan)
7. Verifikasi tidak ada dialog konfirmasi
8. Verifikasi modal Edit Label tetap terbuka
9. Verifikasi `[Save]` berstatus disabled

### TC-FA-LBL-132: Edit: Live Preview mengikuti nama dan warna yang diubah

10. Ganti isi Label Name dengan `Preview Edit 132 {runId}-162`
11. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
12. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
13. Verifikasi Live Preview menampilkan chip `Preview Edit 132 {runId}-162` berlatar `Fixture.assetLabeling.hexValid`
14. Tekan Esc untuk menutup Color Picker Overlay
15. Klik icon `[✕]`
16. Verifikasi dialog Unsaved Changes tampil
17. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03, S-08): langkah 14, 15, 17 menutup overlay dan menutup form dirty secara deterministik (`[✕]`, dialog `Unsaved Changes`, `[Leave]`).
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-133 ditaruh sebelum TC-FA-LBL-132; keduanya memakai satu pembukaan modal dan satu label seed karena tidak ada yang disimpan.
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
- Temuan untuk QA:
  - TC-FA-LBL-132 Expected "secara instan" tidak terukur; spec mengasersi Live Preview sesudah nama dan warna diubah tanpa batas waktu.
  - TC-FA-LBL-133 langkah 2 hanya berbunyi "Ketik `Dirty 133` di Label Name" tanpa menyebut apakah teks menambah atau mengganti nama tersimpan; hasil sesudah `[Clear Field]` sama untuk keduanya.
