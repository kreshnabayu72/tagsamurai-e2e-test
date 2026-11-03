---
id: TC-FA-LBL-E2E-043-edit-penutupan-color-picker-overlay-tanpa-menutup-modal-edit
title: "Edit: Penutupan Color Picker Overlay Tanpa Menutup Modal Edit"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-526
coverage:
  web: automated
---

# Edit: Penutupan Color Picker Overlay Tanpa Menutup Modal Edit

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Tidak ada perubahan yang disimpan.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-043`):
  - `Edit Target 526 {runId}-043` (TC-FA-LBL-526)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.hexValid` | `#10B981` |
  | `Fixture.assetLabeling.hex5Digit` | `#12345` |

- Kemampuan teknis: mengetik ke kolom Hex, mengklik Swatch Trigger Color, titik kanvas, dan area kosong di dalam modal di luar overlay, serta menekan Escape.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-526: Edit: Color Picker Overlay ditutup lewat klik Swatch Trigger dan klik di luar tanpa menutup modal Edit

1. Ketik Search `Edit Target 526 {runId}-043`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 526 {runId}-043`, lalu klik `Edit`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
4. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`, lalu klik Swatch Trigger Color
5. Verifikasi overlay tertutup
6. Verifikasi modal Edit Label tetap terbuka
7. Verifikasi warna `Fixture.assetLabeling.hexValid` dipertahankan di Swatch Trigger dan Live Preview
8. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
9. Klik satu titik kanvas, lalu catat kode di kolom Hex sebagai Warna Kanvas
10. Klik area kosong di dalam modal di luar overlay
11. Verifikasi overlay tertutup
12. Verifikasi modal Edit Label tetap terbuka
13. Verifikasi warna Warna Kanvas dipertahankan di Swatch Trigger dan Live Preview
14. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
15. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hex5Digit`
16. Tekan Escape
17. Verifikasi overlay tertutup
18. Verifikasi modal Edit Label tetap terbuka
19. Verifikasi Swatch Trigger dan Live Preview tetap pada Warna Kanvas
20. Verifikasi `[Save]` berstatus enabled
21. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
22. Verifikasi kolom Hex menampilkan Warna Kanvas (kode `Fixture.assetLabeling.hex5Digit` dibuang)
23. Verifikasi inline error `Invalid color format` tidak tampil
24. Tekan Escape untuk menutup Color Picker Overlay
25. Klik icon `[✕]`
26. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` tampil
27. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03, S-08): langkah 24, 25, 27 menutup overlay dan menutup form dirty (warna Warna Kanvas berbeda dari nilai tersimpan) secara deterministik lewat `[✕]`, dialog `Unsaved Changes`, dan `[Leave]`.
- Warna Kanvas adalah kode Hex yang dibaca dari kolom Hex sesudah klik titik kanvas; TC tidak menyebut kode tertentu.
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
- Temuan untuk QA:
  - TC-FA-LBL-526 langkah 4 menyebut "klik satu titik kanvas" tanpa koordinat dan Expected hanya "warna dari titik kanvas"; spec membaca kode Hex hasil klik sebagai nilai pembanding.
