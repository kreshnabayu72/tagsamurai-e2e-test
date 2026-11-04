---
id: TC-FA-LIC-E2E-106-changelog-concurrent-user-setup-column-pin-dan-unpin
title: "Setup Column Modal Changelog Concurrent User: Pin dan Unpin per Kolom dan Download CSV serta XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-580
  - TC-FA-LIC-582
coverage:
  web: automated
---

# Setup Column Modal Changelog Concurrent User: Pin dan Unpin per Kolom dan Download CSV serta XLSX

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, pemulihan konfigurasi kolom, pembacaan berkas unduhan): dinyatakan sekali di `suite.md`; spec ini merujuknya. Spec ini menyimpan konfigurasi Setup Column modal Changelog Concurrent User (pin); hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`).
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Concurrent User #31 (4 entri) lewat `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE). Kolom default: Date, Action, User Name, Field, Old Value, New Value, Modified By.

  | Date | Action | User Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Force Logout | Budi Santoso | Session Status | Active | Force Logged Out | Rudi H |
  | 29/09/26 14:20 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |
  | 28/09/26 09:40 | Force Logout | Andi Pratama | Session Status | Active | Force Logged Out | Rudi H |
  | 27/09/26 16:05 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |

- Tabel kolom Setup Column (dipakai langkah 3 sampai 13): Date, Action, User Name, Field, Old Value, New Value, Modified By.
- Kemampuan mengatur lebar viewport browser (disediakan tim FE): viewport disempitkan pada langkah 2 agar tabel dapat digeser horizontal untuk asersi pembekuan kolom (pilihan spec; TC hanya menulis "geser tabel horizontal") dan dipulihkan pada langkah 14.
- Kemampuan membaca berkas unduhan CSV dan XLSX (nama berkas, header, baris, sel) disediakan tim FE.
- State yang diubah spec: konfigurasi kolom tersimpan (pin) dipulihkan per iterasi (Unpin) dan oleh hook `after`; ukuran viewport browser dipulihkan pada langkah 14. Suite berjalan serial (`parallel: false`).
- Pengecualian S-12 [KEPUTUSAN 2026-11-02]: jumlah baris berkas Changelog (langkah 18 dan 24) diasersi absolut (tanpa baseline) karena fixture BE pemulih riwayat Pre-setup #31 juga menghapus entri baru (dinyatakan di `suite.md`); asersi tidak diubah.

## Test Steps

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar

### TC-FA-LIC-580: Pin dan Unpin per kolom Hideable Visible default

2. Sempitkan viewport browser sehingga tabel pada modal dapat digeser horizontal

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 3 sampai 13):

3. Klik header kolom Actions `⋯`, klik `Setup Column...`
4. Klik ikon Pin pada kolom di baris tabel, klik `[Save]`
5. Geser tabel horizontal
6. Verifikasi kolom membeku (sticky) di kiri saat scroll horizontal
7. Muat ulang halaman (F5), buka tab Concurrent User, klik ikon Changelog pada toolbar
8. Verifikasi kolom tetap membeku setelah F5
9. Klik header kolom Actions `⋯`, klik `Setup Column...`
10. Klik ikon Pin pada kolom di baris tabel (Unpin), klik `[Save]`
11. Geser tabel horizontal
12. Verifikasi Unpin melepas pembekuan kolom
13. Gulir tabel kembali ke kiri
14. Pulihkan viewport browser ke ukuran semula

### TC-FA-LIC-582: Download CSV dan XLSX dengan nama Changelog-Concurrent-User, mengikuti Search aktif

15. Klik Download > `Download as CSV`
16. Verifikasi tidak ada toast sukses
17. Verifikasi berkas `Changelog-Concurrent-User.csv` terunduh
18. Verifikasi header berkas CSV `Date,Action,User Name,Field,Old Value,New Value,Modified By` dan 4 baris data
19. Klik Download > `Download as XLSX`
20. Verifikasi tidak ada toast sukses
21. Verifikasi berkas `Changelog-Concurrent-User.xlsx` terunduh
22. Ketik Search `siti`, tekan Enter
23. Klik Download > `Download as CSV`
24. Verifikasi berkas CSV hanya memuat 2 baris data (Siti Rahma)
25. Klik icon panah `(←)` di kiri toolbar, lalu tutup modal dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 2 menyempitkan viewport supaya tabel dapat digeser horizontal sebelum asersi sticky (S-14) dan langkah 14 memulihkannya (S-03); langkah 7 membuka kembali modal sesudah F5 (modal tidak bertahan); langkah 10 (Unpin) dan 13 memulihkan state per iterasi; langkah 25 menutup Search dan modal (S-09).
- Langkah yang diulang per baris tabel kolom: langkah 3 sampai 13 (7 iterasi) (bagian 8b butir 7).
- Spec ini memuat 25 langkah nominal dan sekitar 91 langkah dengan ekspansi. Alasan: dua blok membaca modal yang sama dengan dataset yang sama dan berdiri sendiri; tiap iterasi Pin diakhiri Unpin sehingga kegagalan satu iterasi tidak membuat blok Download kehilangan makna.
- Isi berkas unduhan modal Changelog Concurrent User (urutan baris, nilai sel termasuk Modified By nama lengkap, dan format tanggal General Settings) adalah TC-FA-LIC-619, yang ada di spec `TC-FA-LIC-E2E-155`. Spec ini mengasersi nama berkas, tanpa toast sukses, header, dan jumlah baris berkas (bagian 3 prinsip 13f).
- Temuan untuk QA:
  - TC-FA-LIC-580 langkah 3 ("geser tabel horizontal") tidak menyebut cara membuat tabel dapat digeser; spec mencatat kebutuhan viewport di Prerequisites.
