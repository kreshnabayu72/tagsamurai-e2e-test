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
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, pemulihan konfigurasi kolom, pembacaan berkas unduhan): dinyatakan sekali di `suite.md`; spec ini merujuknya. Spec ini menyimpan konfigurasi Setup Column modal Changelog Concurrent User (pin); hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`).
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Concurrent User #31 (4 entri) lewat `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE). Kolom default: Date, Action, User Name, Field, Old Value, New Value, Modified By.

  | Date | Action | User Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Force Logout | Budi Santoso | Session Status | Active | Force Logged Out | Rudi H |
  | 29/09/26 14:20 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |
  | 28/09/26 09:40 | Force Logout | Andi Pratama | Session Status | Active | Force Logged Out | Rudi H |
  | 27/09/26 16:05 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |

- Tabel kolom Setup Column (dipakai langkah 2 sampai 12): Date, Action, User Name, Field, Old Value, New Value, Modified By.
- Lebar viewport menampilkan tabel yang dapat digeser horizontal (disediakan tim FE untuk asersi pembekuan kolom).
- Kemampuan membaca berkas unduhan CSV dan XLSX (nama berkas, header, baris, sel) disediakan tim FE.
- State yang diubah spec: konfigurasi kolom tersimpan (pin) dipulihkan per iterasi (Unpin) dan oleh hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar

### TC-FA-LIC-580: Pin dan Unpin per kolom Hideable Visible default

Untuk setiap baris tabel "Tabel kolom Setup Column" (langkah 2 sampai 12):

2. Klik header kolom Actions `⋯`, klik `Setup Column...`
3. Klik ikon Pin pada kolom di baris tabel, klik `[Save]`
4. Geser tabel horizontal
5. Verifikasi kolom membeku (sticky) di kiri saat scroll horizontal
6. Muat ulang halaman (F5), buka tab Concurrent User, klik ikon Changelog pada toolbar
7. Verifikasi kolom tetap membeku setelah F5
8. Klik header kolom Actions `⋯`, klik `Setup Column...`
9. Klik ikon Pin pada kolom di baris tabel (Unpin), klik `[Save]`
10. Geser tabel horizontal
11. Verifikasi Unpin melepas pembekuan kolom
12. Gulir tabel kembali ke kiri

### TC-FA-LIC-582: Download CSV dan XLSX dengan nama Changelog-Concurrent-User, mengikuti Search aktif

13. Klik Download > `Download as CSV`
14. Verifikasi tidak ada toast sukses
15. Verifikasi berkas `Changelog-Concurrent-User.csv` terunduh
16. Verifikasi header berkas CSV `Date,Action,User Name,Field,Old Value,New Value,Modified By` dan 4 baris data
17. Verifikasi Modified By pada berkas ditulis nama lengkap (`Rudi Hartono`, `Dewi Lestari`)
18. Klik Download > `Download as XLSX`
19. Verifikasi tidak ada toast sukses
20. Verifikasi berkas `Changelog-Concurrent-User.xlsx` terunduh
21. Ketik Search `siti`, tekan Enter
22. Klik Download > `Download as CSV`
23. Verifikasi berkas CSV hanya memuat 2 baris data (Siti Rahma)
24. Klik icon panah `(←)` di kiri toolbar, lalu tutup modal dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 6 membuka kembali modal sesudah F5 (modal tidak bertahan); langkah 9 (Unpin) dan 12 memulihkan state per iterasi; langkah 24 menutup Search dan modal (S-09).
- Langkah yang diulang per baris tabel kolom: langkah 2 sampai 12 (7 iterasi) (bagian 8b butir 7).
- Spec ini memuat 24 langkah nominal dan sekitar 84 langkah dengan ekspansi. Alasan: dua blok membaca modal yang sama dengan dataset yang sama dan berdiri sendiri; tiap iterasi Pin diakhiri Unpin sehingga kegagalan satu iterasi tidak membuat blok Download kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-582 butir b dan c memeriksa isi berkas (kelas f: header, jumlah baris, nilai Modified By) di spec fungsional; spec mengikuti TC. Nama berkas, header, dan jumlah baris adalah asersi fungsional (bagian 3 prinsip 13f); nilai sel Modified By lengkap termasuk isi berkas.
  - TC-FA-LIC-580 langkah 3 ("geser tabel horizontal") tidak menyebut cara membuat tabel dapat digeser; spec mencatat kebutuhan viewport di Prerequisites.
