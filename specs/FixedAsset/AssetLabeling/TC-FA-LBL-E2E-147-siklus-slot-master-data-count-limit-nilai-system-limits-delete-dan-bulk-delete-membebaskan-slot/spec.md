---
id: TC-FA-LBL-E2E-147-siklus-slot-master-data-count-limit-nilai-system-limits-delete-dan-bulk-delete-membebaskan-slot
title: "Siklus Slot Master Data Count Limit: Nilai System Limits, Delete, dan Bulk Delete Membebaskan Slot (bagian 1/2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-440
  - TC-FA-LBL-478
coverage:
  web: automated
---

# Siklus Slot Master Data Count Limit: Nilai System Limits, Delete, dan Bulk Delete Membebaskan Slot (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Limit (Pre-setup #11, pengguna `Total Control Limit`; email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Fixture.assetLabeling.akun.totalControlLimit`, `Spectra.env.FA_TC_LIMIT_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_TC_LIMIT_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- State global yang diubah: Master Data Count Limit Company Limit di System Limits (nilai terendah yang diizinkan `Fixture.assetLabeling.batasMinimum`, nilai naik `Fixture.assetLabeling.batasNaik`) dan jumlah katalog label Company Limit. Pelaku perubahan System Limits adalah kemampuan yang disediakan tim FE (S-13). Hook `before` mengatur batas ke `batasMinimum` dan mengisi katalog lewat fixture BE sampai tepat di batas (termasuk label bersih `Free Slot 478 {runId}-147`); hook `after` memulihkan batas dan menghapus seluruh label seed. Setiap TC menuliskan state awal bagiannya di langkah penghubung (P-4). Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.batasMinimum` | `1000` (Master Data Count Limit terendah yang diizinkan) |
  | `Fixture.assetLabeling.batasNaik` | `1100` (nilai batas yang lebih tinggi dari `batasMinimum`) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- Data Dinamis dibuat spec: `Reuse Slot 478 {runId}-147` (Create TC-FA-LBL-478).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-440: Nilai Master Data Count Limit mengikuti System Limits hanya setelah daftar dimuat ulang

1. Klik `[+ Label]`
2. Verifikasi dialog `Label Limit Reached` tampil dengan nilai batas `Fixture.assetLabeling.batasMinimum` dari respons List
3. Klik `[OK]`
4. Naikkan Master Data Count Limit di System Limits ke `Fixture.assetLabeling.batasNaik`
5. Tanpa memuat ulang tab Labels, klik `[+ Label]`
6. Verifikasi dialog `Label Limit Reached` tetap tampil dengan nilai batas semula `Fixture.assetLabeling.batasMinimum`
7. Klik `[OK]`, lalu muat ulang tab Labels
8. Klik `[+ Label]`
9. Verifikasi modal Create Label terbuka karena batas baru lebih tinggi
10. Klik `✕` pada header modal Create Label
11. Pulihkan Master Data Count Limit ke `Fixture.assetLabeling.batasMinimum`, lalu muat ulang tab Labels

### TC-FA-LBL-478: Menghapus label membebaskan slot sehingga Create berikutnya berhasil di batas

12. Klik `[+ Label]`
13. Verifikasi dialog `Label Limit Reached` tampil
14. Klik `[OK]`
15. Ketik Search `Free Slot 478 {runId}-147`, tekan Enter
16. Klik `⋯` pada baris `Free Slot 478 {runId}-147`, lalu klik `Delete`
17. Klik `[Delete]`, lalu tunggu aksi selesai (dialog tertutup)
18. Klik `[+ Label]`
19. Verifikasi modal Create Label terbuka
20. Isi Label Name dengan `Reuse Slot 478 {runId}-147`
21. Klik `[Submit]`
22. Verifikasi toast `Success, label has been created.`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 15 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 4, 10, dan 11 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state tanpa `Verifikasi`; bukan bagian Expected TC.
- P-4 (state global bersama): TC-FA-LBL-440 dan 478 berkelas volume data (katalog sampai batas Master Data Count Limit, kelas e) dan membangun state global yang sama (Master Data Count Limit dan jumlah katalog Company Limit) secara berurutan; hook `before` mengatur state awal dan tiap bagian menulis state awalnya di langkah penghubung.
- Pembagian TC lintas spec: TC-FA-LBL-479 dan 480 (penurunan batas di bawah jumlah label dan Bulk Delete membebaskan slot) ada di spec 180 pada Company Limit yang sama.
- Temuan untuk QA:
  - TC-FA-LBL-440 menyebut "Naikkan Master Data Count Limit di System Limits" tanpa nilai; spec memakai `Fixture.assetLabeling.batasNaik` (lebih tinggi dari batas minimum 1000) dan menyatakannya di Prerequisites.
  - Email akun Total Control Limit tidak tertulis di Pre-setup TC; disediakan tim FE.
  - Pelaku perubahan System Limits tidak disebut TC, PRD, atau LLD; ditulis sebagai kemampuan tim FE (S-13).
