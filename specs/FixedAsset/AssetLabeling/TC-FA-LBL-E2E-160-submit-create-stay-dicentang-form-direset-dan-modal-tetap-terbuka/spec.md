---
id: TC-FA-LBL-E2E-160-submit-create-stay-dicentang-form-direset-dan-modal-tetap-terbuka
title: "Submit Create dengan Stay Dicentang: Form Direset dan Modal Tetap Terbuka"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-86
coverage:
  web: automated
---

# Submit Create dengan Stay Dicentang: Form Direset dan Modal Tetap Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Suffix nama bersuffix spec ini: `{runId}-160` (`{runId}` hanya digit).
- Label yang dibuat: `Batch One 86 {runId}-160` dan `Batch Two 86 {runId}-160`.
- Label yang dibuat spec ini (nama bersuffix `{runId}-160`) dihapus di hook `after` lewat sesi API aktor.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog dan menghapus label.

## Test Steps

### TC-FA-LBL-86: Submit Create dengan Stay dicentang mereset form dan membiarkan modal terbuka

1. Klik `[+ Label]`
2. Centang `Stay on this form after submitting`
3. Isi Label Name `Batch One 86 {runId}-160`
4. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
5. Kosongkan kolom Hex lalu ketik `#10B981`
6. Klik `[Submit]`
7. Verifikasi toast `Success, label has been created.` untuk `Batch One 86 {runId}-160`
8. Verifikasi Label Name kosong
9. Verifikasi Color kembali `#3B82F6`
10. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
11. Verifikasi modal tetap terbuka
12. Isi Label Name `Batch Two 86 {runId}-160`
13. Klik `[Submit]`
14. Verifikasi toast `Success, label has been created.` untuk `Batch Two 86 {runId}-160`
15. Verifikasi Label Name kosong
16. Verifikasi Color kembali `#3B82F6`
17. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
18. Verifikasi modal tetap terbuka
19. Klik icon `[✕]`
20. Ketik Search `86 {runId}-160`, tekan Enter
21. Verifikasi kedua label `Batch One 86 {runId}-160` dan `Batch Two 86 {runId}-160` tampil di tabel
22. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 19 (menutup modal lewat `[✕]`; form sudah ter-reset sehingga tidak ada dialog `Unsaved Changes`), langkah 20 (Search untuk menemukan baris target, R-16), dan langkah 22 (mengosongkan Search).
- Pada Submit kedua TC hanya mengisi Label Name; warna kembali ke `#3B82F6` (default) dan diasersi pada Expected a.
- Temuan untuk QA: TC-FA-LBL-86 Post Condition "Dua label tersimpan" sudah tercakup Expected b; tidak ada langkah observasi tambahan.
