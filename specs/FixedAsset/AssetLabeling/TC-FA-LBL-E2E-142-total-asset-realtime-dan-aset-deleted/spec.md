---
id: TC-FA-LBL-E2E-142-total-asset-realtime-dan-aset-deleted
title: "Total Asset Realtime dan Aset Deleted"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-423
  - TC-FA-LBL-424
  - TC-FA-LBL-434
coverage:
  web: automated
---

# Total Asset Realtime dan Aset Deleted

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-142`, Color `Fixture.assetLabeling.warnaSeed`; aset milik spec mengikuti pola Pre-setup #13 agar aset Pre-setup tidak berubah, S-06):
  - TC-FA-LBL-423: label `Count 423 {runId}-142` (Total Asset 0) dan aset `Count Monitor {runId}-142` berstatus Waiting for Approval (pola `Monitor LG - 4`).
  - TC-FA-LBL-424: label `Count Del 424 {runId}-142` tertempel pada satu aset Active `Count Zebra {runId}-142` (pola `Scanner Zebra - 9`).
  - TC-FA-LBL-434: label `Purge 434 {runId}-142` tertempel pada satu aset `Count Purge {runId}-142` yang sudah berstatus Deleted (pola Pre-setup #13).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- Penghapusan aset dan penghapusan permanen aset memakai modul Asset (Fixed Asset > Asset List); langkah rinci aksi itu tidak ditulis TC (lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-423: Total Asset bertambah dan berkurang realtime saat label dilampirkan dan dilepas

1. Buka Fixed Asset > Asset List, ketik Search `Count Monitor {runId}-142`, tekan Enter, lalu buka Asset Detail baris itu
2. Buka dropdown penugasan label, pilih `Count 423 {runId}-142`, lalu terapkan (lampirkan)
3. Buka Fixed Asset > Settings > Asset Master > tab Labels, lalu ketik Search `Count 423 {runId}-142`, tekan Enter
4. Verifikasi Total Asset `Count 423 {runId}-142` bernilai `1`
5. Buka Drawer `Count 423 {runId}-142`
6. Verifikasi Drawer memuat aset `Count Monitor {runId}-142`
7. Tutup Drawer
8. Buka Asset Detail `Count Monitor {runId}-142`, lalu klik `✕` pada chip `Count 423 {runId}-142` untuk melepas label
9. Muat ulang tab Labels, lalu ketik Search `Count 423 {runId}-142`, tekan Enter
10. Verifikasi Total Asset `Count 423 {runId}-142` kembali `0`

### TC-FA-LBL-424: Aset yang berubah menjadi Deleted tidak lagi dihitung di Total Asset dan Drawer

11. Ganti isi kotak search dengan `Count Del 424 {runId}-142`, tekan Enter
12. Verifikasi Total Asset `Count Del 424 {runId}-142` bernilai `1` (dicatat sebelum aset dihapus)
13. Hapus aset `Count Zebra {runId}-142` lewat modul Asset
14. Muat ulang tab Labels, lalu ketik Search `Count Del 424 {runId}-142`, tekan Enter
15. Verifikasi Total Asset `Count Del 424 {runId}-142` berubah menjadi `0`
16. Buka Drawer `Count Del 424 {runId}-142`
17. Verifikasi Drawer menampilkan state kosong `No assets tagged`
18. Tutup Drawer

### TC-FA-LBL-434: Aset yang dihapus permanen tidak memengaruhi Total Asset label

19. Ganti isi kotak search dengan `Purge 434 {runId}-142`, tekan Enter
20. Verifikasi Total Asset `Purge 434 {runId}-142` bernilai `0` (sebelum penghapusan permanen)
21. Hapus permanen aset `Count Purge {runId}-142` lewat modul Asset
22. Muat ulang tab Labels, lalu ketik Search `Purge 434 {runId}-142`, tekan Enter
23. Verifikasi Total Asset `Purge 434 {runId}-142` bernilai `0` (sesudah penghapusan permanen)
24. Klik `⋯` pada baris `Purge 434 {runId}-142`, lalu klik `Delete`
25. Verifikasi dialog `Delete Label` tampil
26. Klik `[Delete]`
27. Verifikasi toast `Success, label has been deleted.`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 3, 9, 11, 14, 19, 22 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 1, 7, 8, 13, 18, 21 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Total Asset `Count Del 424` bernilai `1` sebelum aset dihapus dan Total Asset `Purge 434` bernilai `0` sebelum penghapusan permanen ditulis sebagai `Verifikasi` karena Expected TC menyebut nilai awal itu.
- Toast `Success, label has been deleted.` pada TC-FA-LBL-434 mengikuti toast Delete label di TC-FA-LBL-431; Expected TC-FA-LBL-434 hanya menyebut "label dapat dihapus lewat dialog `Delete Label`".
- Temuan untuk QA:
  - TC-FA-LBL-424 dan 434 menyebut "hapus aset lewat modul Asset" dan "hapus permanen" tanpa langkah rinci; spec menulisnya sebagai aksi pada modul Asset dan kemampuan teknis tim FE/BE (S-13).
  - TC-FA-LBL-423 sampai 434 memakai aset Pre-setup (`Monitor LG - 4`, `Scanner Zebra - 9`); spec memakai aset milik spec dengan pola status yang sama (S-06).
