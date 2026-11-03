---
id: TC-FA-CAID-E2E-007-role-matrix-read-only-modal-dan-download
title: "Role Matrix: Read Only Membuka Modal, Tooltip Disabled, dan Download Code List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-27
  - TC-FA-CAID-28
  - TC-FA-CAID-157
coverage:
  web: automated
---

# Role Matrix: Read Only Membuka Modal, Tooltip Disabled, dan Download Code List

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Akun aktor: Read Only Company Alpha (Pre-setup No 2) `readOnly_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_RO_PASSWORD` (nama env usulan di `suite.md`, perlu konfirmasi tim FE). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dan aset A1 sampai A5 dipulihkan ke baseline B1 di `beforeEach` lewat sesi API Total Control Company Alpha (kemampuan disediakan tim FE).
- Data Pre-setup: No 10 baseline B1 dan B2 (B2 = Separator `- (Dash)`, Initial Company `ABC`, Division Code tercentang di atas B1; di-seed spec ini sebelum TC-FA-CAID-27 lewat sesi API Total Control dan dipulihkan ke B1 oleh `beforeEach` suite berikutnya serta hook `after` suite); No 28 master data ber-Code Company Alpha (dibaca oleh Modal View Code List; tab `Group Codes` memuat `Head Office` (HO), `Jakarta Office` (JKT), dan seterusnya); No 15 entri Changelog L1 sampai L7 (di-seed hook `before` spec ini lewat sesi API Total Control agar tabel Changelog berisi baris; dipakai sebagai precondition TC-FA-CAID-28, tidak diasersi). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis: penangkapan berkas unduhan oleh browser (nama berkas dibaca; isi berkas tidak dibaca) dan pembacaan toast; disediakan tim FE.
- State global: konfigurasi Company Alpha (B2 pada langkah 13), dipulihkan lewat `beforeEach` suite dan hook `after` suite. Entri Changelog tidak dihapus (audit trail permanen). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-28: Read Only membuka Modal View Code List dan Modal Changelog

1. Klik tautan `[View Code List]`
2. Verifikasi modal `Code List Reference` terbuka dan menampilkan tabel pada tab `Group Codes`
3. Tutup modal `Code List Reference` dengan `✕`
4. Klik tombol `[Changelog]`
5. Verifikasi modal `Changelog: Custom Asset ID` terbuka dan menampilkan tabel riwayat
6. Tutup modal `Changelog: Custom Asset ID` dengan `✕`

### TC-FA-CAID-157: Read Only dapat mengunduh Code List

7. Klik tautan `[View Code List]`
8. Klik `Download` pada modal
9. Klik `Download as CSV` pada tab `Group Codes`
10. Verifikasi tidak ada toast
11. Verifikasi berkas `Code-List-Group-Codes.csv` terunduh
12. Tutup modal `Code List Reference` dengan `✕`

### TC-FA-CAID-27: Tooltip alasan pada kontrol Disabled untuk Read Only

13. Ubah konfigurasi Company Alpha ke baseline B2 lewat sesi API Total Control hingga konfigurasi tersimpan
14. Muat ulang halaman (F5)
15. Hover Master Switch
16. Verifikasi tooltip 🔖 `You don't have permission to do this.` tampil pada Master Switch
17. Hover Separator
18. Verifikasi tooltip 🔖 `You don't have permission to do this.` tampil pada Separator
19. Hover checkbox `Group Code`
20. Verifikasi tooltip 🔖 `You don't have permission to do this.` tampil pada checkbox `Group Code`
21. Hover drag handle baris `Group Code`
22. Verifikasi tooltip 🔖 `You don't have permission to do this.` tampil pada drag handle `Group Code`
23. Hover input Initial Company
24. Verifikasi tooltip 🔖 `You don't have permission to do this.` tampil pada input Initial Company

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Langkah buka tab pada ketiga TC dipenuhi hook `beforeEach` suite.
- Urutan TC di spec: TC-FA-CAID-28, 157, lalu 27. Alasan: TC-FA-CAID-28 dan 157 memakai baseline B1 dari hook, sedangkan TC-FA-CAID-27 membutuhkan B2 sehingga diletakkan terakhir dan B2 di-seed sekali (S-10).
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 6, 12 (menutup modal), langkah 13 dan 14 (mengganti baseline lewat sesi API Total Control dan memuat ulang agar form memuat B2), langkah 8 dan 9 (pemicu unduhan; langkah 10 dan 11 diasersi segera), dan hover pada langkah 15, 17, 19, 21, 23 (tooltip diasersi segera sesudah hover, sebelum langkah berikutnya).
- Urutan langkah 10 dan 11 mengikuti bagian 8b butir 11: asersi absence toast diletakkan segera setelah pemicu unduhan (langkah 9 sebagai anchor positif) dan sebelum asersi berkas terunduh.
- Temuan untuk QA:
  - Kolom ACC TC-FA-CAID-28 dan 157 hanya menyebut Pre-setup #2 dan master data #28; TC tidak menyebut apakah entri Changelog (Pre-setup #15) ada pada Company Alpha. Spec men-seed entri Changelog pada Company Alpha agar "tabel riwayat" berisi baris; bila Pre-setup #15 berada di Company Changelog terpisah, TC-FA-CAID-28 butuh akun Read Only di Company itu.
  - Email akun Read Only hanya tertulis sebagai pola `{namaCompany}`; env var password adalah usulan.
  - Post Condition TC-FA-CAID-27, 28, dan 157 kosong; tidak ada yang diasersi.
