---
id: TC-FA-SU-E2E-161-sub-tab-pending-approvals-search-dan-sort
title: "Sub-tab Pending Approvals: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-475
  - TC-FA-SU-476
  - TC-FA-SU-477
  - TC-FA-SU-478
  - TC-FA-SU-479
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#25): Detail Budi Santoso dengan Sub-tab Pending Approvals 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #25 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC:

| Transaction ID | Transaction | Requester | Submission Date |
|---|---|---|---|
| `BRW-20260712-0341` | `Borrow` | `Ahmad D` | 12/07/26 |
| `TRF-20260714-0088` | `Transfer` | `Citra L` (Citra Lestari) | 14/07/26 |
| `DSP-20260715-0022` | `Disposal` | `Eka W` | 15/07/26 |
| `ASG-20260716-0015` | `Assignment` | `Budi S` | 16/07/26 |
| `BRW-20260718-0007` | `Borrow` | `Citra L` (Citra Lestari) | 18/07/26 |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Kolom Sort" (dipakai langkah 17 sampai 22):

| Kolom | Klik 1 ascending (↑) | Klik 2 descending (↓) |
|---|---|---|
| `Transaction ID` | `ASG-20260716-0015`, `BRW-20260712-0341`, `BRW-20260718-0007`, `DSP-20260715-0022`, `TRF-20260714-0088` | `TRF-20260714-0088`, `DSP-20260715-0022`, `BRW-20260718-0007`, `BRW-20260712-0341`, `ASG-20260716-0015` |
| `Transaction` | `ASG-20260716-0015`, `BRW-20260712-0341`, `BRW-20260718-0007`, `DSP-20260715-0022`, `TRF-20260714-0088` | `TRF-20260714-0088`, `DSP-20260715-0022`, `BRW-20260712-0341`, `BRW-20260718-0007`, `ASG-20260716-0015` |
| `Requester` | `BRW-20260712-0341`, `ASG-20260716-0015`, `TRF-20260714-0088`, `BRW-20260718-0007`, `DSP-20260715-0022` | `DSP-20260715-0022`, `TRF-20260714-0088`, `BRW-20260718-0007`, `ASG-20260716-0015`, `BRW-20260712-0341` |
| `Submission Date` | `BRW-20260712-0341`, `TRF-20260714-0088`, `DSP-20260715-0022`, `ASG-20260716-0015`, `BRW-20260718-0007` | `BRW-20260718-0007`, `ASG-20260716-0015`, `DSP-20260715-0022`, `TRF-20260714-0088`, `BRW-20260712-0341` |

Baris diidentifikasi lewat Transaction ID. Klik ketiga mengembalikan urutan default Submission Date ascending: `BRW-20260712-0341`, `TRF-20260714-0088`, `DSP-20260715-0022`, `ASG-20260716-0015`, `BRW-20260718-0007`.

## Test Steps

### TC-FA-SU-475: Guard kolom non-searchable: Submission Date

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Ketik Search `12/07/26`, tekan Enter
4. Verifikasi empty state `No results found` tampil karena Search tidak mencocokkan kolom Submission Date (penyaringan kolom ini hanya lewat Filter Panel)
5. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-476: Search Sub-tab Pending Approvals terikat visibilitas kolom Transaction ID: hide lalu unhide

6. Ganti isi kotak search dengan `TRF-2026`, tekan Enter
7. Verifikasi keyword `TRF-2026` menyisakan `TRF-20260714-0088`
8. Klik header Actions (⋯)
9. Uncheck kolom Transaction ID pada overlay Column Visibility
10. Ganti isi kotak search dengan `TRF-2026`, tekan Enter
11. Verifikasi tabel tidak menampilkan baris
12. Klik header Actions (⋯)
13. Check kolom Transaction ID pada overlay Column Visibility
14. Ganti isi kotak search dengan `TRF-2026`, tekan Enter
15. Verifikasi keyword `TRF-2026` menyisakan `TRF-20260714-0088`
16. Klik `(←)` pada kotak Search

### TC-FA-SU-477: Sort kelas teks dan badge, TC-FA-SU-478: kelas user, dan TC-FA-SU-479: kelas date

17. Untuk setiap baris tabel parameter "Kolom Sort" (langkah 17 sampai 22): klik header kolom itu satu kali
18. Verifikasi urutan baris ascending (↑) sesuai kolom Klik 1 ascending pada tabel parameter
19. Klik header kolom itu kedua kali
20. Verifikasi urutan baris descending (↓) sesuai kolom Klik 2 descending pada tabel parameter
21. Klik header kolom itu ketiga kali
22. Verifikasi urutan baris netral kembali ke default Submission Date ascending

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah 17 sampai 22 diulang untuk empat baris tabel parameter "Kolom Sort" (ekspansi 24 langkah dari 6 langkah nominal, bagian 8b butir 7) dan mencakup TC-FA-SU-477 (Transaction ID, Transaction), TC-FA-SU-478 (Requester), dan TC-FA-SU-479 (Submission Date); `Verifikasi` tetap satu per klausa tiap kolom.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (40 langkah, 22 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Pending Approvals, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-471 sampai 474 ada di spec 160.
- Temuan untuk QA (S-15):
  - TC-FA-SU-479 klik 1 ascending menghasilkan urutan yang sama dengan default (Submission Date ascending), sehingga klik 1 tidak dapat dibedakan dari default lewat urutan baris saja; spec mengasersi urutan sesuai Expected TC.
  - TC-FA-SU-478 Expected menulis urutan dengan Transaction ID baris, bukan nama Requester; nilai Requester per baris diturunkan dari TC-FA-SU-482 dan 473.
  - TC-FA-SU-475 mengasumsikan kotak Search terbuka dari langkah sebelumnya; spec membuka Search lewat langkah "Ketik Search" yang atomik.
