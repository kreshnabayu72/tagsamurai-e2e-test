---
id: TC-FA-SU-E2E-165-sub-tab-pending-approvals-setup-column
title: "Sub-tab Pending Approvals: Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-491
  - TC-FA-SU-493
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Setup Column

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
- Tabel parameter "Geser Kolom" (dipakai langkah 5 sampai 6):

| Kolom | Arah | Posisi (sebelum ke sesudah geser) | Posisi akhir tabel |
|---|---|---|---|
| `Transaction ID` | bawah | 1 ke 2 | 4 |
| `Requester` | atas | 3 ke 2 | 1 |
| `Submission Date` | atas | 4 ke 3 | 3 |
| `Transaction` | bawah | 1 ke 2 | 2 |

Urutan awal: `Transaction ID`, `Transaction`, `Requester`, `Submission Date`. Baris diproses dari atas ke bawah secara kumulatif; urutan akhir: `Requester`, `Transaction`, `Submission Date`, `Transaction ID`.
- Kemampuan menghapus preferensi kolom Setup Column di browser (disediakan tim FE): dipakai sebagai langkah pemulihan dan di hook `after` untuk tabel yang konfigurasinya disimpan spec ini (bagian 4 konvensi). Konfigurasi kolom tersimpan per perangkat dan per tabel.

## Test Steps

### TC-FA-SU-491: Geser (drag reorder) Setup Column Sub-tab Pending Approvals kelas Hideable (default tampil)

1. Ketik Search `Budi Santoso`, tekan Enter, lalu klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Klik header kolom Actions (⋯)
4. Klik `Setup Column...`
5. Untuk setiap baris tabel parameter "Geser Kolom" (langkah 5 sampai 6): geser kolom itu satu posisi sesuai kolom Arah pada tabel parameter
6. Verifikasi urutan Live Preview berubah: kolom itu berpindah satu posisi sesuai kolom Posisi pada tabel parameter
7. Klik `[Save]`
8. Untuk setiap baris tabel parameter "Geser Kolom" (langkah 8): Verifikasi kolom itu berada di posisi akhir sesuai tabel parameter pada tabel
9. Tekan F5 pada halaman Detail
10. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
11. Untuk setiap baris tabel parameter "Geser Kolom" (langkah 11): Verifikasi kolom itu tetap berada di posisi akhir setelah F5
12. Pulihkan konfigurasi kolom tabel Pending Approvals: hapus preferensi kolom di browser
13. Tekan F5 pada halaman Detail
14. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals

### TC-FA-SU-493: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column Sub-tab Pending Approvals

15. Klik header kolom Actions (⋯)
16. Klik `Setup Column...`
17. Uncheck kolom `Requester` pada popup Setup Column
18. Geser kolom `Transaction` satu posisi ke bawah
19. Klik icon Pin pada kolom `Transaction ID`
20. Klik `[Reset to Default]`
21. Verifikasi Live Preview kembali ke default modul: visibility, urutan, dan pin
22. Klik `[Save]`
23. Verifikasi tabel memakai konfigurasi default modul setelah `[Save]`
24. Klik header kolom Actions (⋯)
25. Klik `Setup Column...`
26. Uncheck kolom `Requester` pada popup Setup Column
27. Klik ✕ pada popup Setup Column
28. Verifikasi popup tertutup, perubahan dibuang, dan tabel memakai konfigurasi tersimpan terakhir (kolom `Requester` tampil)
29. Klik header kolom Actions (⋯)
30. Klik `Setup Column...`
31. Uncheck kolom `Requester` pada popup Setup Column
32. Tekan Esc
33. Verifikasi popup tertutup, perubahan dibuang, dan tabel memakai konfigurasi tersimpan terakhir (kolom `Requester` tampil)
34. Klik header kolom Actions (⋯)
35. Klik `Setup Column...`
36. Uncheck kolom `Requester` pada popup Setup Column
37. Klik `[Save]`
38. Klik Sub-tab Assigned Assets
39. Verifikasi konfigurasi tabel Sub-tab Assigned Assets tidak berubah: kolom `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Brand`, `Model / Type`, `PIC` tampil dalam urutan default
40. Klik Sub-tab Pending Approvals
41. Verifikasi kolom `Requester` tidak tampil di tabel Sub-tab Pending Approvals (konfigurasi tabel ini tetap tersimpan)
42. Pulihkan konfigurasi kolom tabel Pending Approvals: hapus preferensi kolom di browser
43. Tekan F5 pada halaman Detail
44. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): Search nama `Budi Santoso` serta pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah 5 sampai 6, 8, dan 11 diulang untuk empat baris tabel parameter "Geser Kolom" (bagian 8b butir 7); `Verifikasi` tetap satu per klausa tiap kolom.
- Langkah pemulihan konfigurasi kolom (12 dan 42) dan F5 sesudahnya memulihkan tabel ke default (S-09); hook `after` mengulang pemulihan sebagai cadangan.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (56 langkah, 44 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Pending Approvals (Setup Column), satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-492 (pin dan unpin) ada di spec 168; TC-FA-SU-488 dan 489 (screening) ada di spec 164.
- Temuan untuk QA (S-15):
  - TC-FA-SU-491 tidak menyebut arah geser dan posisi tujuan tiap kolom; spec memakai urutan geser kumulatif pada tabel parameter "Geser Kolom".
  - TC-FA-SU-493 Langkah 2 ("ubah beberapa pengaturan") tidak menyebut pengaturan; spec memakai uncheck `Requester`, geser `Transaction`, dan pin `Transaction ID`. Langkah 6 ("tabel lain yang punya Setup Column") tidak menyebut tabelnya; spec memakai Sub-tab Assigned Assets.
