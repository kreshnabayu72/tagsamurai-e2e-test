---
id: TC-FA-LBL-E2E-047-menutup-form-edit-penutupan-bersih-dan-dialog-unsaved-changes-lewat-tombol-tutup
title: "Menutup Form Edit: Penutupan Bersih dan Dialog Unsaved Changes lewat Tombol Tutup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-147
  - TC-FA-LBL-148
  - TC-FA-LBL-150
coverage:
  web: automated
---

# Menutup Form Edit: Penutupan Bersih dan Dialog Unsaved Changes lewat Tombol Tutup

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Tidak ada kasus di spec ini yang menyimpan perubahan.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-047`):
  - `Edit Target 147 {runId}-047` (satu label seed untuk ketiga TC; tidak ada yang disimpan)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: menekan Esc dan klik `[✕]` pada modal Edit Label.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `Edit Target 147 {runId}-047`, tekan Enter

### TC-FA-LBL-147: Menutup form Edit tanpa perubahan lewat ✕ dan Esc tidak memunculkan dialog Unsaved Changes

2. Klik `⋯` pada baris `Edit Target 147 {runId}-047`, lalu klik `Edit`
3. Klik icon `[✕]`
4. Verifikasi modal Edit Label tertutup langsung
5. Verifikasi dialog Unsaved Changes tidak muncul
6. Klik `⋯` pada baris `Edit Target 147 {runId}-047`, lalu klik `Edit`
7. Tekan Esc
8. Verifikasi modal Edit Label tertutup langsung
9. Verifikasi dialog Unsaved Changes tidak muncul

### TC-FA-LBL-150: Form Edit yang diubah lalu dikembalikan identik dengan nilai tersimpan dianggap bersih

10. Klik `⋯` pada baris `Edit Target 147 {runId}-047`, lalu klik `Edit`
11. Ganti isi Label Name dengan `Revert Edit 150 {runId}-047`
12. Ketik ulang Label Name menjadi `Edit Target 147 {runId}-047`
13. Klik icon `[✕]`
14. Verifikasi modal Edit Label tertutup langsung
15. Verifikasi dialog Unsaved Changes tidak muncul

### TC-FA-LBL-148: Menutup form Edit yang berubah lewat ✕ memunculkan dialog Unsaved Changes

16. Klik `⋯` pada baris `Edit Target 147 {runId}-047`, lalu klik `Edit`
17. Ganti isi Label Name dengan `Dirty Edit 148 {runId}-047`
18. Klik icon `[✕]`
19. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]` tampil
20. Klik `[Cancel]`
21. Verifikasi modal Edit Label tetap terbuka
22. Verifikasi input `Dirty Edit 148 {runId}-047` dipertahankan
23. Klik icon `[✕]` lalu klik `[Leave]`
24. Verifikasi modal Edit Label tertutup
25. Verifikasi baris `Edit Target 147 {runId}-047` tampil dengan nama tidak berubah

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-150 ditaruh sebelum TC-FA-LBL-148 supaya kasus bersih mendahului kasus dirty; jumlah buka form sama dengan jumlah penutupan (S-10).
- TC-FA-LBL-149 dan TC-FA-LBL-151 (Esc dan klik backdrop pada form berubah) ada di spec nomor 161; TC-FA-LBL-152 dan TC-FA-LBL-153 (reload dan pindah route) ada di spec nomor 048.
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
