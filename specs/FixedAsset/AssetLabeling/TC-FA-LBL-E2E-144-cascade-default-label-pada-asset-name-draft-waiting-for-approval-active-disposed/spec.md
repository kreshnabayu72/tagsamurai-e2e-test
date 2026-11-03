---
id: TC-FA-LBL-E2E-144-cascade-default-label-pada-asset-name-draft-waiting-for-approval-active-disposed
title: "Cascade Default Label pada Asset Name (Draft, Waiting for Approval, Active, Disposed)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-429
  - TC-FA-LBL-430
  - TC-FA-LBL-431
  - TC-FA-LBL-432
coverage:
  web: automated
---

# Cascade Default Label pada Asset Name (Draft, Waiting for Approval, Active, Disposed)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-144`, Color `Fixture.assetLabeling.warnaSeed`; Asset Name dan aset milik spec mengikuti pola Pre-setup #14 agar data Pre-setup tidak berubah, S-06):
  - TC-FA-LBL-429: Asset Name `Promote Item {runId}-144` dengan aset Active `Promote Asset {runId}-144` yang memiliki label `Promote 429 {runId}-144` ber-source manual.
  - TC-FA-LBL-430 sampai 432: Asset Name `Cascade Item {runId}-144` dengan aset `Cascade Draft {runId}-144` (Draft), `Cascade Waiting {runId}-144` (Waiting for Approval), `Cascade Active {runId}-144` (Active), dan `Cascade Disposed {runId}-144` (Disposed).
  - Label bersih `Cascade 430 {runId}-144` (TC-FA-LBL-430).
  - Label `Cascade Rm 431 {runId}-144` sebagai Default Label `Cascade Item {runId}-144` yang sudah tertempel default pada aset Draft, Waiting for Approval, dan Active (TC-FA-LBL-431).
  - Label `Disposed Lock 432 {runId}-144` sebagai Default Label `Cascade Item {runId}-144` yang tertempel default pada satu aset `Cascade Locked {runId}-144` berstatus Disposed (sebelumnya Active) (TC-FA-LBL-432).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-429: Menetapkan label sebagai Default Label mempromosikan relasi manual menjadi default terkunci

1. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik `⋯` pada baris `Promote Item {runId}-144`, lalu klik `Edit`
2. Tambahkan `Promote 429 {runId}-144` ke Default Label
3. Klik `[Save]`, lalu tunggu aksi selesai (popup Edit Asset Name tertutup)
4. Buka Fixed Asset > Asset List, ketik Search `Promote Asset {runId}-144`, tekan Enter, lalu buka Asset Detail baris itu
5. Verifikasi chip `Promote 429 {runId}-144` pada aset tidak lagi memiliki ikon `✕` (terkunci)
6. Buka Fixed Asset > Settings > Asset Master > tab Labels, lalu ketik Search `Promote 429 {runId}-144`, tekan Enter
7. Verifikasi Total Asset `Promote 429 {runId}-144` bernilai `1` (relasi tidak digandakan)

### TC-FA-LBL-430: Cascade Default Label menambah relasi default pada aset Draft, Waiting for Approval, Active

8. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik `⋯` pada baris `Cascade Item {runId}-144`, lalu klik `Edit`
9. Tambahkan `Cascade 430 {runId}-144` ke Default Label
10. Klik `[Save]`, lalu tunggu aksi selesai (popup Edit Asset Name tertutup)
11. Buka Fixed Asset > Settings > Asset Master > tab Labels, lalu ketik Search `Cascade 430 {runId}-144`, tekan Enter
12. Verifikasi Total Asset `Cascade 430 {runId}-144` bernilai `3`
13. Buka Drawer `Cascade 430 {runId}-144`
14. Verifikasi Drawer memuat tiga aset `Cascade Draft {runId}-144`, `Cascade Waiting {runId}-144`, dan `Cascade Active {runId}-144`
15. Verifikasi aset Disposed `Cascade Disposed {runId}-144` tidak memiliki label itu (tidak tampil di Drawer)
16. Tutup Drawer

### TC-FA-LBL-431: Mengeluarkan label dari Default Label melepas relasi default pada aset Draft, Waiting for Approval, Active

17. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik `⋯` pada baris `Cascade Item {runId}-144`, lalu klik `Edit`
18. Keluarkan `Cascade Rm 431 {runId}-144` dari Default Label
19. Klik `[Save]`, lalu tunggu aksi selesai (popup Edit Asset Name tertutup)
20. Buka Fixed Asset > Settings > Asset Master > tab Labels, lalu ketik Search `Cascade Rm 431 {runId}-144`, tekan Enter
21. Verifikasi Total Asset `Cascade Rm 431 {runId}-144` bernilai `0`
22. Buka Drawer `Cascade Rm 431 {runId}-144`
23. Verifikasi Drawer menampilkan state kosong `No assets tagged` (chip hilang dari ketiga aset)
24. Tutup Drawer
25. Klik `⋯` pada baris `Cascade Rm 431 {runId}-144`, lalu klik `Delete`
26. Verifikasi dialog konfirmasi `Delete Label` tampil
27. Klik `[Delete]`
28. Verifikasi toast `Success, label has been deleted.`

### TC-FA-LBL-432: Relasi default pada aset Disposed tidak dilepas dan label tetap tidak dapat dihapus

29. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik `⋯` pada baris `Cascade Item {runId}-144`, lalu klik `Edit`
30. Keluarkan `Disposed Lock 432 {runId}-144` dari Default Label
31. Klik `[Save]`, lalu tunggu aksi selesai (popup Edit Asset Name tertutup)
32. Buka Fixed Asset > Settings > Asset Master > tab Labels, lalu ketik Search `Disposed Lock 432 {runId}-144`, tekan Enter
33. Verifikasi Total Asset `Disposed Lock 432 {runId}-144` tetap `1` (aset Disposed tetap menghitung)
34. Klik `⋯` pada baris `Disposed Lock 432 {runId}-144`, lalu klik `Delete`
35. Verifikasi dialog `Cannot Delete Label` dengan baris `This label is assigned to 1 asset.` tampil
36. Verifikasi baris Default Label tidak tampil pada dialog karena hitungan 0
37. Tutup dialog `Cannot Delete Label`
38. Verifikasi label `Disposed Lock 432 {runId}-144` tidak terhapus (baris tetap tampil)

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 4, 6, 11, 20, 32 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 1, 8, 16, 17, 24, 29, 37 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Ukuran spec (38 langkah, di atas smell 35 langkah): keempat TC satu topik (cascade Default Label pada Asset Name), satu akun, dan berbagi satu Asset Name seed `Cascade Item` dengan empat aset berstatus berbeda sehingga memisahkannya melipatgandakan seeding aset bersatus; tiap blok memakai label seed sendiri dan berdiri sendiri, jadi kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-431 Expected a "chip hilang dari ketiga aset" tidak menyebut permukaan; spec mengamatinya lewat Drawer `Cascade Rm 431` yang menampilkan `No assets tagged` bersama Total Asset `0`.
  - TC-FA-LBL-431 langkah 3 (Delete) memakai dialog `Delete Label`; Expected b menyebut toast `Success, label has been deleted.`.
  - TC-FA-LBL-432 Expected b menyebut "label tidak terhapus" tanpa langkah observasi; spec memeriksa baris tetap tampil setelah dialog ditutup.
  - Precondition TC memakai Asset Name dan aset Pre-setup #14 (`Laptop Dell`, `Cascade Item`); spec memakai Asset Name dan aset milik spec dengan pola yang sama (S-06).
