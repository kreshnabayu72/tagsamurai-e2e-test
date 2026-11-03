---
id: TC-FA-SU-E2E-128-tabel-user-list-download
title: "Tabel User List: Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-361
coverage:
  web: automated
---

# Tabel User List: Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Pengguna Pre-setup berjumlah 25 baris; Search `Budi` dengan Filter Status `Active` menyisakan `Budi Santoso`, `Indra Wijaya`, `Putri Anggraeni`, `Vina Maharani` (4 baris). Keyword tanpa hasil: `zzzzqx` (pilihan spec). Kolom yang di-hide: `Email` (pilihan spec; TC tidak menyebut kolom).
- Kemampuan baca isi berkas unduhan CSV dan XLSX (nama berkas, header kolom, jumlah dan isi baris, encoding, nama sheet) disediakan tim FE.

## Test Steps

### TC-FA-SU-361: Cakupan baris dan kolom Download

1. Klik icon Download, pilih `Download as CSV`
2. Verifikasi berkas memuat seluruh 25 baris (bukan hanya 10 baris halaman aktif) dalam urutan sort aktif
3. Ketik Search `Budi`, tekan Enter
4. Klik ikon Filter, buka dropdown Status, centang `Active`, klik `[Apply]`
5. Klik icon Download, pilih `Download as CSV`
6. Verifikasi berkas hanya memuat baris yang cocok: `Budi Santoso`, `Indra Wijaya`, `Putri Anggraeni`, `Vina Maharani`
7. Klik header ⋯, hapus centang `Email`
8. Klik icon Download, pilih `Download as CSV`
9. Verifikasi tidak ada toast peringatan
10. Verifikasi kolom `Email` tidak ikut berkas
11. Klik header ⋯, centang kembali `Email`
12. Klik icon Download, pilih `Download as CSV`
13. Verifikasi tidak ada toast peringatan
14. Verifikasi kolom `Email` ikut berkas kembali
15. Ganti isi kotak search dengan `zzzzqx`, tekan Enter
16. Verifikasi empty state `No results found` tampil
17. Klik icon Download, pilih `Download as CSV`
18. Verifikasi tidak ada toast
19. Verifikasi berkas hanya memuat baris header kolom yang visible tanpa baris data
20. Klik `(←)` pada kotak Search, klik `[Clear Field]` lalu `[Apply]` pada panel Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 20 (membersihkan Search dan Filter, S-09).
- Asersi absence toast (langkah 9, 13, dan 18) diletakkan tepat sesudah pemilihan `Download as CSV` dan sebelum asersi isi berkas, supaya toast yang hilang otomatis tidak terlewat (bagian 8b butir 5 dan 11).
- Temuan untuk QA (S-15): (1) Expected a TC-FA-SU-361 menyebut berkas memuat "seluruh baris" dalam urutan sort aktif tetapi langkah TC tidak menyebut sort yang aktif; sort default Name ascending dipakai. (2) TC-FA-SU-361 tidak menyebut kolom yang di-hide; spec memakai `Email`.
