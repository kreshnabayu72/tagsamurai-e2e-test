---
id: TC-FA-SU-E2E-162-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-1
title: "Sub-tab Pending Approvals: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-480
  - TC-FA-SU-481
  - TC-FA-SU-482
  - TC-FA-SU-483
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Filter dan Kontrol Filter (Bagian 1)

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
- Tabel parameter "Field Filter" (dipakai langkah 14 sampai 21):

| Field | Opsi dropdown (DISTINCT data tabel) | Pilihan | Baris tersisa |
|---|---|---|---|
| `Transaction` | `Assignment`, `Borrow`, `Disposal`, `Transfer` | `Assignment` | `ASG-20260716-0015` (1 baris) |
| `Requester` | `Ahmad D`, `Budi S`, `Citra L`, `Eka W` | `Ahmad D` | `BRW-20260712-0341` (1 baris) |

## Test Steps

### TC-FA-SU-480: Screening Filter Panel Sub-tab Pending Approvals: field, label, placeholder, dan tombol

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Klik icon Filter
4. Verifikasi panel Filter terbuka di bawah Table Tools
5. Verifikasi ikon Filter menjadi gelap
6. Hover icon Filter
7. Verifikasi tooltip `Filter` tampil
8. Verifikasi field berurutan Transaction | Requester | Submission Date
9. Verifikasi field Transaction berupa multi-select searchable dengan placeholder `All transactions`
10. Verifikasi field Requester berupa multi-select searchable dengan placeholder `All requesters`
11. Verifikasi field Submission Date berupa date range picker dengan placeholder `Select date`
12. Verifikasi footer panel menampilkan `[Clear Field]` di kiri dan `[Apply]` di kanan
13. Verifikasi ikon Filter tanpa badge titik selama belum ada filter ter-Apply

### TC-FA-SU-481 dan TC-FA-SU-482: Filter kelas enum Transaction dan kelas fk Requester

14. Untuk setiap baris tabel parameter "Field Filter" (langkah 14 sampai 21): buka dropdown pada field itu
15. Verifikasi opsi dropdown sama dengan DISTINCT data tabel sesuai kolom Opsi pada tabel parameter
16. Centang opsi pada kolom Pilihan
17. Klik `[Apply]`
18. Verifikasi tabel menyisakan baris sesuai kolom Baris tersisa pada tabel parameter
19. Verifikasi chip opsi terpilih tampil di dalam field itu
20. Klik `[Clear Field]` pada field itu
21. Klik `[Apply]`

### TC-FA-SU-483: Filter kelas date: Submission Date

22. Buka date range picker pada field Submission Date
23. Pilih tanggal awal 12/07/26
24. Pilih tanggal akhir 14/07/26
25. Klik `[Apply]`
26. Verifikasi rentang inklusif 12/07/26 sampai 14/07/26 menyisakan `BRW-20260712-0341` dan `TRF-20260714-0088` (2 baris)
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Klik icon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah 14 sampai 21 diulang untuk dua baris tabel parameter "Field Filter" (ekspansi 16 langkah dari 8 langkah nominal, bagian 8b butir 7) dan mencakup TC-FA-SU-481 (Transaction) dan TC-FA-SU-482 (Requester). `[Clear Field]` lalu `[Apply]` di akhir tiap iterasi dan di akhir TC-FA-SU-483 memastikan tiap field diuji terpisah.
- Pembagian TC lintas spec: TC-FA-SU-484 sampai 486 ada di spec 163.
- Temuan untuk QA (S-15):
  - TC-FA-SU-483 tidak menyebut cara membuka date range picker dan memilih tanggal; spec memakai langkah umum "Buka date range picker" lalu memilih tanggal awal dan akhir.
  - TC-FA-SU-480 Expected b tidak menyebut format placeholder date range picker selain `Select date`; spec mengasersi sesuai Expected.
