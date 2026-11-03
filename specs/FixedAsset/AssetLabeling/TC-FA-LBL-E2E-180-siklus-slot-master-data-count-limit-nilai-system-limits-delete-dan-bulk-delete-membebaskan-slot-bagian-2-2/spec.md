---
id: TC-FA-LBL-E2E-180-siklus-slot-master-data-count-limit-nilai-system-limits-delete-dan-bulk-delete-membebaskan-slot-bagian-2-2
title: "Siklus Slot Master Data Count Limit: Nilai System Limits, Delete, dan Bulk Delete Membebaskan Slot (bagian 2/2)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-479
  - TC-FA-LBL-480
coverage:
  web: automated
---

# Siklus Slot Master Data Count Limit: Nilai System Limits, Delete, dan Bulk Delete Membebaskan Slot (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Limit (Pre-setup #11, pengguna `Total Control Limit`; email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Fixture.assetLabeling.akun.totalControlLimit`, `Spectra.env.FA_TC_LIMIT_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_TC_LIMIT_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- State global yang diubah: Master Data Count Limit Company Limit di System Limits (nilai terendah yang diizinkan `Fixture.assetLabeling.batasMinimum`, nilai naik `Fixture.assetLabeling.batasNaik`) dan jumlah katalog label Company Limit. Pelaku perubahan System Limits adalah kemampuan yang disediakan tim FE (S-13). Hook `before` mengatur batas ke `batasMinimum` dan mengisi katalog lewat fixture BE sampai tepat di batas (termasuk label bersih `Free A 480 {runId}-180` dan `Free B 480 {runId}-180`); hook `after` memulihkan batas dan menghapus seluruh label seed. Setiap TC menuliskan state awal bagiannya di langkah penghubung (P-4). Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.batasMinimum` | `1000` (Master Data Count Limit terendah yang diizinkan) |
  | `Fixture.assetLabeling.batasNaik` | `1100` (nilai batas yang lebih tinggi dari `batasMinimum`) |
  | `Fixture.assetLabeling.jumlahKatalog479` | `1005` (jumlah label pada TC-FA-LBL-479) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- Data Dinamis dibuat spec: `Reuse Bulk 480 {runId}-180` (Create TC-FA-LBL-480); lima label tambahan `Extra 479 n {runId}-180` (n = 1 sampai 5) di-seed fixture BE pada TC-FA-LBL-479.
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-479: Menurunkan Master Data Count Limit di bawah jumlah label yang ada tidak memangkas data tetapi menahan Create

1. Atur katalog menjadi `Fixture.assetLabeling.jumlahKatalog479` label dengan Master Data Count Limit `Fixture.assetLabeling.batasNaik` lewat fixture BE, lalu muat ulang tab Labels
2. Turunkan Master Data Count Limit di System Limits ke `Fixture.assetLabeling.batasMinimum`, lalu simpan
3. Tanpa memuat ulang tab Labels, klik `[+ Label]`
4. Verifikasi modal Create Label terbuka karena respons List terakhir masih membawa batas semula
5. Klik `✕` pada header modal Create Label
6. Muat ulang tab Labels
7. Verifikasi seluruh label yang ada tetap tampil dan tidak ada yang terhapus (jumlah total pada pagination tetap `Fixture.assetLabeling.jumlahKatalog479`)
8. Klik `[+ Label]`
9. Verifikasi dialog `Label Limit Reached` tampil dengan nilai batas baru `Fixture.assetLabeling.batasMinimum`
10. Klik `[OK]`
11. Naikkan kembali Master Data Count Limit ke `Fixture.assetLabeling.batasNaik`, lalu muat ulang tab Labels
12. Klik `[+ Label]`
13. Verifikasi modal Create Label terbuka
14. Klik `✕` pada header modal Create Label

### TC-FA-LBL-480: Bulk Delete membebaskan slot sehingga Create berhasil lagi

15. Atur katalog tepat di batas `Fixture.assetLabeling.batasMinimum` dengan Master Data Count Limit `Fixture.assetLabeling.batasMinimum` lewat fixture BE (menghapus label tambahan TC-FA-LBL-479), lalu muat ulang tab Labels
16. Ketik Search `480 {runId}-180`, tekan Enter
17. Centang baris `Free A 480 {runId}-180` dan `Free B 480 {runId}-180`
18. Klik `Bulk Action` lalu klik `Delete`
19. Klik `[Delete]` pada dialog `Delete Labels`, lalu tunggu aksi selesai (dialog tertutup)
20. Klik `[+ Label]`
21. Verifikasi modal Create Label terbuka
22. Isi Label Name dengan `Reuse Bulk 480 {runId}-180`
23. Klik `[Submit]`
24. Verifikasi toast `Success, label has been created.`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 16 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 1, 2, 5, 11, 14, dan 15 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- P-4 (state global bersama): TC-FA-LBL-479 dan 480 berkelas volume data (katalog sampai batas Master Data Count Limit, kelas e) dan membangun state global yang sama (Master Data Count Limit dan jumlah katalog Company Limit) secara berurutan; hook `before` mengatur state awal dan tiap bagian menulis state awalnya di langkah penghubung.
- Pembagian TC lintas spec: TC-FA-LBL-440 dan 478 (nilai batas mengikuti System Limits dan Delete membebaskan slot) ada di spec 147 pada Company Limit yang sama.
- Temuan untuk QA:
  - TC-FA-LBL-479 menyebut "Master Data Count Limit awal lebih tinggi dari 1005" tanpa nilai; spec memakai `batasNaik` (1100).
  - Email akun Total Control Limit tidak tertulis di Pre-setup TC; disediakan tim FE.
  - Pelaku perubahan System Limits tidak disebut TC, PRD, atau LLD; ditulis sebagai kemampuan tim FE (S-13).
