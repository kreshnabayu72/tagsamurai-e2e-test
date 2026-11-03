---
id: TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list
title: "Row Action, Kolom Clients, dan Membuka Plan Detail dari Plans List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-9
  - TC-AC-PF-10
  - TC-AC-PF-11
  - TC-AC-PF-12
  - TC-AC-PF-13
  - TC-AC-PF-14
  - TC-AC-PF-15
  - TC-AC-PF-16
coverage:
  web: automated
---

# Row Action, Kolom Clients, dan Membuka Plan Detail dari Plans List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21: default `Growth`, `Growth Plus (old)` archived, custom `Growth Tier` aktif dan `Enterprise Reseller` archived), Dataset Plan R (Pre-setup #30: `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`, Clients 0), Dataset Plan C (Pre-setup #23: `Arsip Custom Satu` archived Clients 0). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Data milik spec (hook `before`, dibuat lewat fixture BE, dihapus di hook `after`): custom plan aktif `Hitung Aktif {runId}-002` dengan lima client dan status subscription PT Hitung Satu Active, PT Hitung Dua Grace, PT Hitung Tiga Waiting for Approval, PT Hitung Empat Pending, PT Hitung Lima Expired; custom plan archived `Hitung Arsip {runId}-002` dengan empat client PT Arsip Satu Active, PT Arsip Dua Expired, PT Arsip Tiga Archive, PT Arsip Empat Purge.
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `Growth Plus (old)`, `Growth Tier`, `Enterprise Reseller`, `Plan Arsip Lama`, `Arsip Custom Satu`) dipakai karena menentukan asersi teks dan opsi row action; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan semua Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (pemulihan Dataset Pre-setup, pembuatan plan dan subscription berstatus tertentu) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-9: Row action tab Default sub-tab Active menampilkan opsi sesuai kondisi baris

1. Klik ikon `⋯` pada baris `Growth` di tab Default sub-tab Active
2. Verifikasi Overlay Row Action memuat `Detail` (ikon `FileInfoLine`, severity dark), `Edit` (ikon `Edit2Line`, severity dark), dan `Archive` (ikon `ArchiveLine`, severity dark)
3. Verifikasi Overlay Row Action tidak memuat `Push Update` dan `Delete`
4. Tekan Esc untuk menutup Overlay Row Action

### TC-AC-PF-10: Row action tab Default sub-tab Archive: plan yang dirujuk subscription non-`Deleted` hanya `Detail`, plan yang tidak dirujuk memuat `Detail` dan `Delete`

5. Klik sub-tab Archive
6. Klik ikon `⋯` pada baris `Growth Plus (old)` (Clients 31)
7. Verifikasi Overlay Row Action pada baris `Growth Plus (old)` hanya memuat `Detail`
8. Tekan Esc untuk menutup Overlay Row Action
9. Klik ikon `⋯` pada baris `Plan Arsip Lama` (Clients 0)
10. Verifikasi Overlay Row Action pada baris `Plan Arsip Lama` memuat `Detail` dan `Delete` (ikon `DeleteBin6Line`, severity danger)
11. Verifikasi Overlay Row Action pada baris `Plan Arsip Lama` tidak memuat `Edit`
12. Tekan Esc untuk menutup Overlay Row Action

### TC-AC-PF-11: Row action tab Custom sub-tab Active menampilkan opsi sesuai kondisi baris

13. Klik tab Custom
14. Klik ikon `⋯` pada baris `Growth Tier`
15. Verifikasi Overlay Row Action memuat `Detail`, `Edit`, dan `Archive`
16. Verifikasi Overlay Row Action tidak memuat `Push Update` dan `Delete`
17. Tekan Esc untuk menutup Overlay Row Action

### TC-AC-PF-12: Row action tab Custom sub-tab Archive: plan yang dirujuk subscription non-`Deleted` hanya `Detail`, plan yang tidak dirujuk memuat `Detail` dan `Delete`

18. Klik sub-tab Archive
19. Klik ikon `⋯` pada baris `Enterprise Reseller` (Clients 6)
20. Verifikasi Overlay Row Action pada baris `Enterprise Reseller` hanya memuat `Detail`
21. Tekan Esc untuk menutup Overlay Row Action
22. Klik ikon `⋯` pada baris `Arsip Custom Satu` (Clients 0)
23. Verifikasi Overlay Row Action pada baris `Arsip Custom Satu` memuat `Detail` dan `Delete` (severity danger)
24. Verifikasi Overlay Row Action pada baris `Arsip Custom Satu` tidak memuat `Edit`
25. Tekan Esc untuk menutup Overlay Row Action

### TC-AC-PF-13: Kolom Clients sub-tab Active menghitung client unik berstatus Active atau Grace, tidak menghitung status lain

26. Klik sub-tab Active
27. Ketik Search `Hitung Aktif {runId}-002`, tekan Enter
28. Verifikasi kolom Clients pada baris `Hitung Aktif {runId}-002` bernilai `2` (hanya PT Hitung Satu berstatus Active dan PT Hitung Dua berstatus Grace)
29. Klik `(←)` pada kotak Search

### TC-AC-PF-14: Kolom Clients sub-tab Archive menghitung historical count lintas status subscription

30. Klik sub-tab Archive
31. Ketik Search `Hitung Arsip {runId}-002`, tekan Enter
32. Verifikasi kolom Clients pada baris `Hitung Arsip {runId}-002` bernilai `4` (historical count lintas status, bukan hanya Active atau Grace)
33. Klik `(←)` pada kotak Search

### TC-AC-PF-15: Klik teks Plan Name pada tab Default membuka Plan Detail plan yang sama

34. Klik tab Default
35. Hover teks `Growth` pada kolom Plan Name
36. Verifikasi warna teks `Growth` berubah ke warna primary Admin Console tanpa garis bawah
37. Klik teks `Growth`
38. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active > Detail untuk `Growth` terbuka pada tab yang sama
39. Verifikasi Tab Overview aktif pada Plan Detail `Growth`

### TC-AC-PF-16: Row action Detail pada tab Custom membuka Plan Detail plan yang sama

40. Klik menu Plans & Licensing > Plans & Features di sidebar
41. Klik tab Custom
42. Klik ikon `⋯` pada baris `Growth Tier`
43. Klik opsi `Detail`
44. Verifikasi halaman Plans & Licensing > Plans & Features > Custom > Active > Detail untuk `Growth Tier` terbuka
45. Verifikasi Tab Overview aktif pada Plan Detail `Growth Tier`

## Notes

- Langkah penghubung (S-03): Esc pada langkah 4, 8, 12, 17, 21, dan 25 menutup Overlay Row Action sebelum langkah berikutnya; klik `(←)` pada langkah 29 dan 33 mengosongkan Search; klik sub-tab dan tab pada langkah 5, 13, 18, 26, 30, dan 34 mengarahkan layar ke tab yang disyaratkan precondition TC; langkah 40 mengembalikan list ke Default > Active. Search pada langkah 27 dan 31 untuk menemukan baris target dicatat sebagai langkah penghubung (R-16).
- TC-AC-PF-13 dan TC-AC-PF-14 memakai plan milik spec bersuffix (`Hitung Aktif {runId}-002`, `Hitung Arsip {runId}-002`) agar pencarian tidak bentrok antar run (S-12); nama literal TC (`Hitung Aktif`, `Hitung Arsip`) dan client dibuat lewat fixture BE.
- Alasan di atas sekitar 35 langkah (45 langkah): seluruh blok memeriksa satu perilaku Plans List (row action, kolom Clients, pembukaan Plan Detail) dengan kelas harness yang sama (fungsional FE+BE), tiap blok berdiri sendiri pada baris datanya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tiap Expected dipecah satu `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - TC-AC-PF-9 dan TC-AC-PF-11: langkah TC menyebut "baris yang diuji" tanpa menunjuk baris. Spec memakai `Growth` (tab Default) dan `Growth Tier` (tab Custom); Expected TC-AC-PF-9 menyebut `Detail`/`Edit`/`Archive` saja sehingga baris Dataset Plan A lain yang memuat `Push Update` tidak diuji.
  - TC-AC-PF-13: Dataset TC hanya menyebut "Plan Custom `Hitung Aktif` tersedia" tanpa baris pada Tabel Data Uji Pre-setup; spec membuatnya sebagai data milik spec (lihat Prerequisites).
  - TC-AC-PF-15: Expected "warna primary Admin Console" tidak menyebut nilai warna; spec mengasersi perubahan warna sesuai TC tanpa nilai tertentu.
