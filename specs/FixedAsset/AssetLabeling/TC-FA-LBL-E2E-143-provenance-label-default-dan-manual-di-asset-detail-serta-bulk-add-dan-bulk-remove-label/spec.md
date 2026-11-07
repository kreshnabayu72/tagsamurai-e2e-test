---
id: TC-FA-LBL-E2E-143-provenance-label-default-dan-manual-di-asset-detail-serta-bulk-add-dan-bulk-remove-label
title: "Provenance Label Default dan Manual di Asset Detail serta Bulk Add dan Bulk Remove Label"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-425
  - TC-FA-LBL-426
  - TC-FA-LBL-427
  - TC-FA-LBL-428
coverage:
  web: automated
---

# Provenance Label Default dan Manual di Asset Detail serta Bulk Add dan Bulk Remove Label

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Extra (Pre-setup #56: salinan label Pre-setup #12 plus seed tambahan) untuk keempat TC (425, 426, 427, 428), `Fixture.assetLabeling.akun.totalControlExtra`. Akun, `namaCompany`, dan nama env password belum ada, disediakan tim FE (tidak diisi di spec; sama dengan spec Extra lain). Akun ini juga memegang role Update pada Manage Asset & TAG (precondition TC-FA-LBL-425). Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec. Hook `after` suite mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, dibuat di Company Extra, bersuffix `{runId}-143`, Color `Fixture.assetLabeling.warnaSeed`; aset dan Asset Name milik spec mengikuti pola Pre-setup #27 dan #28 agar data Pre-setup tidak berubah, S-06). Total Asset hanya bisa dinilai lewat selisih sebelum dan sesudah; TC tidak memiliki langkah observasi Total Asset sehingga tidak diasersi (S-01):
  - TC-FA-LBL-425: label `Manual Rm 425 {runId}-143` terpasang manual pada aset Active `Rm Asset 425 {runId}-143`.
  - TC-FA-LBL-426: Asset Name `Prov Item {runId}-143` dengan Default Label `Lock Default {runId}-143`; aset Active `Prov Asset {runId}-143` memiliki `Lock Default {runId}-143` ber-source default dan label manual `Manual Rm 426 {runId}-143`.
  - TC-FA-LBL-427: label `Bulk Add 427 {runId}-143`; aset Active `Add Asset A 427 {runId}-143` sudah memilikinya (manual) dan aset Active `Add Asset B 427 {runId}-143` belum memilikinya.
  - TC-FA-LBL-428: label `Mixed Field Kit {runId}-143` menjadi Default Label Asset Name `Mixed Item {runId}-143`; aset `Mixed Asset {runId}-143 A` memiliki label itu ber-source manual (Asset Name lain) dan aset `Mixed Asset {runId}-143 B` (Asset Name `Mixed Item {runId}-143`) ber-source default.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- State global: tidak ada yang diubah. Data Pre-setup tidak dipakai atau diubah; keempat TC memakai data milik spec. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (data Dinamis TC-FA-LBL-425, 426, 427, dan 428; termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-425: Melepas label manual dari Asset Detail

1. Buka Fixed Asset > Asset List, ketik Search `Rm Asset 425 {runId}-143`, tekan Enter, lalu buka Asset Detail baris `Rm Asset 425 {runId}-143`
2. Klik `✕` pada chip label manual seed `Manual Rm 425 {runId}-143`
3. Verifikasi chip `Manual Rm 425 {runId}-143` terlepas
4. Verifikasi toast `Success, Label has been removed.`

### TC-FA-LBL-426: Chip default tanpa ikon ✕ di Asset Detail

5. Buka Fixed Asset > Asset List, ketik Search `Prov Asset {runId}-143`, tekan Enter, lalu buka Asset Detail baris itu
6. Verifikasi chip `Lock Default {runId}-143` tampil tanpa ikon `✕`
7. Verifikasi chip label manual `Manual Rm 426 {runId}-143` tampil dengan ikon `✕`

### TC-FA-LBL-427: Bulk Add Label atas aset yang sudah memilikinya

8. Buka Fixed Asset > Asset List, ketik Search `427 {runId}-143`, tekan Enter, lalu centang baris `Add Asset A 427 {runId}-143` dan `Add Asset B 427 {runId}-143`
9. Klik `[🏷 Add Label]`, pilih `Bulk Add 427 {runId}-143`, lalu terapkan
10. Verifikasi toast `Success, Label has been added.`
11. Verifikasi tidak ada error
12. Buka Asset Detail `Add Asset A 427 {runId}-143`
13. Verifikasi `Add Asset A 427 {runId}-143` tetap memiliki satu relasi `Bulk Add 427 {runId}-143`
14. Kembali ke Asset List lalu buka Asset Detail `Add Asset B 427 {runId}-143`
15. Verifikasi `Add Asset B 427 {runId}-143` mendapat satu relasi `Bulk Add 427 {runId}-143`

### TC-FA-LBL-428: Bulk Remove Label pada aset campuran default dan manual

16. Buka Fixed Asset > Asset List, ketik Search `Mixed Asset {runId}-143`, tekan Enter, lalu centang baris `Mixed Asset {runId}-143 A` dan `Mixed Asset {runId}-143 B`
17. Klik `[🏷 Remove Label]`, pilih `Mixed Field Kit {runId}-143`, lalu terapkan
18. Verifikasi toast `Success, Label has been removed.`
19. Verifikasi relasi default pada `Mixed Asset {runId}-143 B` dilewati tanpa rincian item yang dilewati
20. Buka Asset Detail `Mixed Asset {runId}-143 A`
21. Verifikasi `Mixed Field Kit {runId}-143` terlepas dari `Mixed Asset {runId}-143 A`
22. Kembali ke Asset List lalu buka Asset Detail `Mixed Asset {runId}-143 B`
23. Verifikasi `Mixed Asset {runId}-143 B` tetap memiliki `Mixed Field Kit {runId}-143` ber-source default

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 5, 8, 16 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 12, 14, 20, 22 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Urutan: keempat TC memakai label dan aset seed milik spec sendiri (S-06), sehingga urutan mengikuti TC dan tidak ada TC yang menumpang data TC lain.
- Bulk Add dan Bulk Remove pada TC-FA-LBL-500 dan Form Edit Aset TC-FA-LBL-523 ada di spec 176 (data `Lock Default` terkunci).
- Temuan untuk QA:
  - Post Condition TC-FA-LBL-425 ("Total Asset `Manual Rm 425` berkurang satu"), TC-FA-LBL-427 ("Total Asset tidak menghitung ganda"), dan TC-FA-LBL-428 ("Total Asset berkurang satu") tidak memiliki langkah observasi di TC sehingga tidak diasersi (S-01); Total Asset di Company Extra hanya bisa dinilai lewat selisih sebelum dan sesudah.
  - TC-FA-LBL-427 Expected "tidak ada error" tidak menyebut bentuk error; spec memeriksa tidak adanya toast atau dialog error setelah terapkan.
  - TC-FA-LBL-428 Expected "dilewati tanpa rincian dilewati" tidak menyebut permukaan; spec memeriksa toast hasil tidak memuat rincian item yang dilewati.
  - TC-FA-LBL-425 dan 427 memakai aset Pre-setup #57 (`Laptop Dell - 1`, `Laptop Dell - 2`) serta label `Manual Rm 425` dan `Finance Department` pada TC; keduanya mengubah data itu dan tidak ada pemulihan, sehingga spec memakai label dan aset milik spec bersuffix `{runId}-143` (`Manual Rm 425 {runId}-143`, `Rm Asset 425 {runId}-143`, `Bulk Add 427 {runId}-143`, `Add Asset A/B 427 {runId}-143`; nama diadakan spec, bukan dari TC) dengan perilaku yang sama (S-06; T-304).
  - TC-FA-LBL-426 dan 428 memakai aset Pre-setup #27 dan #28 pada TC (`Locked Item - 21`, `Mixed Asset - 22`, `Mixed Asset - 23`); spec memakai data milik spec dengan pola yang sama (S-06). TC-FA-LBL-426 menyebut chip label manual tanpa nama label; spec memakai label manual seed `Manual Rm 426 {runId}-143` (nama diadakan spec, bukan dari TC).
