---
id: TC-FA-CF-E2E-031-scope-specific-asset-name-create
title: "Scope Specific Asset Name pada Create"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-91
  - TC-FA-CF-92
  - TC-FA-CF-93
  - TC-FA-CF-94
coverage:
  web: automated
---

# Scope Specific Asset Name pada Create

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup (hanya dibaca): Asset Name `Generator` dan `Pump` Company Alpha (Pre-setup #11).
- Data dinamis (dibuat lewat UI oleh spec ini): D-1 `Scope Two {runId}-031` (Scope `Generator`, `Pump`); D-2 `Scope Rm {runId}-031` (Scope `Generator`). Nilai yang hanya diketik dan tidak pernah tersimpan: `Scope Empty {runId}-031`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-031`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-91: Memilih Scope Specific Asset Name menampilkan input multi-select Asset Name

1. Klik `[+ Custom Field]`
2. Pilih radio Scope `Specific Asset Name`
3. Verifikasi multi-select chip input pemilihan Asset Name tampil dengan placeholder `Select asset names`
4. Verifikasi input Asset Name tampil tanpa helper
5. Verifikasi input Asset Name wajib diisi minimal satu pilihan (label `Scope *` bertanda wajib)

#### TC-FA-CF-92: Scope Specific tanpa Asset Name ditolak saat Submit

6. Klik `[Clear Field]`
7. Isi Field Name `Scope Empty {runId}-031` dan Data Type `Text`
8. Pilih Scope `Specific Asset Name` tanpa memilih Asset Name
9. Klik `[Submit]`
10. Verifikasi pesan inline `Please select at least one asset name` tampil
11. Verifikasi modal tetap terbuka

#### TC-FA-CF-93: Scope Specific dengan dua Asset Name tersimpan sebagai himpunan

12. Klik `[Clear Field]`
13. Isi Field Name `Scope Two {runId}-031` dan Data Type `Text`
14. Pilih Scope `Specific Asset Name` dengan Asset Name `Pump` dan `Generator`
15. Klik `[Submit]`
16. Verifikasi toast sukses: "Success, custom field has been created."
17. Ketik Search `Scope Two {runId}-031`, tekan Enter
18. Verifikasi kolom Scope baris `Scope Two {runId}-031` menampilkan badge `Generator` lalu `Pump` (urut abjad)

#### TC-FA-CF-94: Chip Asset Name dihapus dari input sebelum Submit mengubah himpunan Scope

19. Klik `[+ Custom Field]`
20. Pilih Scope `Specific Asset Name` dengan `Pump` dan `Generator`
21. Hapus chip `Pump`
22. Isi Field Name `Scope Rm {runId}-031` dan Data Type `Text`
23. Klik `[Submit]`
24. Ganti isi kotak search dengan `Scope Rm {runId}-031`, tekan Enter
25. Verifikasi kolom Scope baris `Scope Rm {runId}-031` hanya menampilkan badge `Generator`
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` di antara kasus yang hanya mengetik (halaman yang sama dipakai berulang), Search untuk menemukan baris target (R-16), dan `Klik (←)` untuk mereset Search.
- Field Dinamis bernama bersuffix `{runId}-031` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Temuan untuk QA: TC-FA-CF-91 butir b ('Input wajib minimal satu pilihan') tidak punya cara teramati langsung; spec mengasersi penanda wajib pada label `Scope *` dan penegakannya diasersi pada TC-FA-CF-92.
