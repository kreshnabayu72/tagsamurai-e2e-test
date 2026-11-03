---
id: TC-FA-LBL-E2E-161-menutup-form-edit-klik-backdrop-dan-esc-saat-form-berubah
title: "Menutup Form Edit: Klik Backdrop dan Esc Saat Form Berubah"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-149
  - TC-FA-LBL-151
coverage:
  web: automated
---

# Menutup Form Edit: Klik Backdrop dan Esc Saat Form Berubah

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Tidak ada kasus di spec ini yang menyimpan perubahan.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-161`):
  - `Edit Target 151 {runId}-161` (satu label seed untuk kedua TC; tidak ada yang disimpan)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: klik area gelap di luar modal (backdrop) dan menekan Esc pada modal Edit Label.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `Edit Target 151 {runId}-161`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 151 {runId}-161`, lalu klik `Edit`

### TC-FA-LBL-151: Klik backdrop modal Edit Label tidak menutup modal

3. Klik area gelap di luar modal
4. Verifikasi modal Edit Label tetap terbuka
5. Verifikasi dialog Unsaved Changes tidak muncul
6. Ganti isi Label Name dengan `Backdrop Edit 151 {runId}-161`
7. Klik area gelap di luar modal
8. Verifikasi modal Edit Label tetap terbuka
9. Verifikasi input `Backdrop Edit 151 {runId}-161` dipertahankan
10. Verifikasi dialog Unsaved Changes tidak muncul

### TC-FA-LBL-149: Esc pada form Edit yang berubah memunculkan dialog Unsaved Changes

11. Ganti isi Label Name dengan `Esc Edit 149 {runId}-161`
12. Tekan Esc
13. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
14. Tekan Esc lagi saat dialog tampil
15. Verifikasi dialog tertutup
16. Verifikasi modal Edit Label tetap terbuka
17. Verifikasi input `Esc Edit 149 {runId}-161` dipertahankan
18. Klik icon `[✕]`
19. Verifikasi dialog Unsaved Changes tampil
20. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-151 ditaruh sebelum TC-FA-LBL-149 supaya kasus backdrop pada form bersih mendahului form dirty; kedua TC memakai satu pembukaan modal (satu buka, satu penutupan pada langkah 18, 20, S-10).
- Langkah penghubung (S-03, S-08): langkah 18, 20 menutup form dirty secara deterministik (`[✕]`, dialog `Unsaved Changes`, `[Leave]`) sehingga form tidak berakhir dirty.
- TC-FA-LBL-147, 148, dan 150 ada di spec nomor 047; TC-FA-LBL-152 dan 153 ada di spec nomor 048.
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
