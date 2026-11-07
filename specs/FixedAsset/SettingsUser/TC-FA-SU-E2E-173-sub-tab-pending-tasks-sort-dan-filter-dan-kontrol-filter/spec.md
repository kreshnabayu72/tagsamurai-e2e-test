---
id: TC-FA-SU-E2E-173-sub-tab-pending-tasks-sort-dan-filter-dan-kontrol-filter
title: "Sub-tab Pending Tasks: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-514
  - TC-FA-SU-515
  - TC-FA-SU-516
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Sort dan Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.
- Tabel parameter "Sort kelas date":

| Kolom | Klik 1 (ascending ↑) | Klik 2 (descending ↓) | Klik 3 (netral, default) |
|---|---|---|---|
| Request Date | `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067` | `ASG-20260718-0067`, `BRW-20260716-0372`, `ASG-20260715-0045`, `BRW-20260713-0355`, `BRW-20260712-0346` | `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']`, `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']` |
| Last Updated | `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067` | `ASG-20260718-0067`, `BRW-20260716-0372`, `ASG-20260715-0045`, `BRW-20260713-0355`, `BRW-20260712-0346` | `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']`, `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']` |

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-514: Sort kelas date (Request Date, Last Updated)

2. Untuk setiap baris tabel "Sort kelas date" (langkah 2 sampai 7): klik header kolom baris itu satu kali
3. Verifikasi urutan ascending (↑) sama dengan kolom "Klik 1" baris itu
4. Klik header kolom baris itu kedua kali
5. Verifikasi urutan descending (↓) sama dengan kolom "Klik 2" baris itu
6. Klik header kolom baris itu ketiga kali
7. Verifikasi urutan netral kembali ke default sama dengan kolom "Klik 3" baris itu

### TC-FA-SU-515: Screening Filter Panel

8. Hover icon Filter
9. Verifikasi tooltip `Filter`
10. Klik icon Filter
11. Verifikasi panel terbuka di bawah Table Tools
12. Verifikasi ikon Filter menjadi gelap
13. Verifikasi field berurutan: Transaction (multi-select searchable, placeholder `All transactions`) | Status (multi-select searchable, placeholder `All statuses`) | Group (multi-select searchable, placeholder `All groups`) | PIC (multi-select searchable, placeholder `All PICs`) | Total Asset (Min/Max) | Request Date (date range picker, placeholder `Select date`) | Last Updated (date range picker, placeholder `Select date`)
14. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
15. Verifikasi tanpa badge titik pada ikon Filter selama belum ada filter ter-Apply

### TC-FA-SU-516: Filter kelas enum (Transaction, Status)

16. Buka dropdown Transaction
17. Verifikasi opsi dropdown = DISTINCT data tabel (`Assignment`, `Borrowing`)
18. Centang `Assignment`
19. Klik `[Apply]`
20. Verifikasi `Assignment` menyisakan `ASG-20260715-0045`, `ASG-20260718-0067` (2 baris)
21. Verifikasi chip `Assignment` tampil di dalam field Transaction
22. Klik `[Clear Field]` pada field Transaction
23. Klik `[Apply]`
24. Buka dropdown Status
25. Verifikasi opsi dropdown = DISTINCT data tabel (`Waiting for Acceptance`, `Waiting for Confirmation`)
26. Centang `Waiting for Acceptance`
27. Klik `[Apply]`
28. Verifikasi `Waiting for Acceptance` menyisakan `ASG-20260715-0045`, `ASG-20260718-0067` (2 baris)
29. Verifikasi chip `Waiting for Acceptance` tampil di dalam field Status

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` lalu membuka Detail Budi Santoso (langkah 1); `[Clear Field]` lalu `[Apply]` sebelum Status supaya tiap field diuji terpisah (sesuai langkah TC-FA-SU-516).
- Daftar field Filter Panel pada TC-FA-SU-515 diasersi sebagai satu `Verifikasi` karena daftar disebut utuh dalam satu butir Expected (S-01).
- Langkah berulang per baris tabel parameter: tabel "Sort kelas date" pada langkah 2 sampai 7 (2 iterasi).
- Jumlah langkah: 29 tertulis, 35 dengan ekspansi iterasi.
- Temuan untuk QA:
  - TC-FA-SU-514 Expected a dan b: klik 1 ascending Request Date dan Last Updated sama dengan urutan default sehingga hanya indikator panah ↑ yang membedakannya; spec mengasersi urutan persis seperti TC.
