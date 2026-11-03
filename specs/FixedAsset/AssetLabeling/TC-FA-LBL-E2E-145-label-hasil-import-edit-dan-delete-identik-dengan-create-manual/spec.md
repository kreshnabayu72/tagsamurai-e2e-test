---
id: TC-FA-LBL-E2E-145-label-hasil-import-edit-dan-delete-identik-dengan-create-manual
title: "Label Hasil Import: Edit dan Delete Identik dengan Create Manual"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-435
  - TC-FA-LBL-436
coverage:
  web: automated
---

# Label Hasil Import: Edit dan Delete Identik dengan Create Manual

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (label hasil Import Asset Name `[Create Missing Labels]` milik spec, dibuat di hook `before` lewat fixture BE yang meniru jalur Import sehingga Color awal `Fixture.assetLabeling.warnaImportAwal`; bersuffix `{runId}-145`): `Import Edit 435 {runId}-145` dan label bersih `Import Del 436 {runId}-145`.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaImportAwal` | `#3B82F6` (Color awal label hasil Import) |
  | `Fixture.assetLabeling.hexHijau` | `#10B981` |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- Kemampuan teknis tambahan (disediakan tim FE/BE): pembuatan label lewat jalur Import `[Create Missing Labels]` untuk seed (Pre-setup #14 tersedia).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-435: Label hasil Import dapat di-Edit identik dengan label Create manual

1. Ketik Search `Import Edit 435 {runId}-145`, tekan Enter
2. Klik `⋯` pada baris `Import Edit 435 {runId}-145`, lalu klik `Edit`
3. Verifikasi Color Hex label hasil Import awal adalah `Fixture.assetLabeling.warnaImportAwal`
4. Ganti isi Label Name dengan `Import Edit 435 Baru {runId}-145`
5. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
6. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexHijau`
7. Klik `[Save]`
8. Verifikasi toast `Success, label has been updated.`
9. Buka Modal Changelog, lalu ketik Search `Import Edit 435 Baru {runId}-145`, tekan Enter
10. Verifikasi Changelog memuat entri Edit Field `Label Name` untuk label `Import Edit 435 Baru {runId}-145`
11. Verifikasi Changelog memuat entri Edit Field `Color` dengan New Value `Fixture.assetLabeling.hexHijau`
12. Tutup Modal Changelog

### TC-FA-LBL-436: Label hasil Import yang bersih dapat dihapus identik dengan label Create manual

13. Ganti isi kotak search dengan `Import Del 436 {runId}-145`, tekan Enter
14. Klik `⋯` pada baris `Import Del 436 {runId}-145`, lalu klik `Delete`
15. Verifikasi dialog `Delete Label` tampil
16. Klik `[Delete]`
17. Verifikasi toast `Success, label has been deleted.`
18. Verifikasi baris `Import Del 436 {runId}-145` hilang dari tabel

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 9, 13 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 12 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Temuan untuk QA:
  - TC-FA-LBL-435 Expected "Changelog memuat dua entri Edit (Label Name dan Color)" tidak menyebut Old Value dan New Value Label Name; spec mengasersi entri Label Name dan New Value Color saja.
  - TC-FA-LBL-435 Expected "warna awal label hasil Import adalah `#3B82F6`" tidak menyebut permukaan; spec memeriksa Color Hex pada popup Edit sebelum diubah.
  - TC-FA-LBL-435 dan 436 tidak menyebut cara pembuatan label hasil Import selain `[Create Missing Labels]`; spec menyiapkannya lewat kemampuan teknis tim FE/BE (S-13).
