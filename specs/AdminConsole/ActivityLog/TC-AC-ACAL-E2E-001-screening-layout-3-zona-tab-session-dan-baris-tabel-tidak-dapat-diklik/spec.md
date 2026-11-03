---
id: TC-AC-ACAL-E2E-001-screening-layout-3-zona-tab-session-dan-baris-tabel-tidak-dapat-diklik
title: "Screening Layout 3 Zona Tab Session dan Baris Tabel Tidak Dapat Diklik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-01
  - TC-AC-ACAL-16
coverage:
  web: automated
---

# Screening Layout 3 Zona Tab Session dan Baris Tabel Tidak Dapat Diklik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture; nama env `AC_TC_PASSWORD` mengikuti bagian 5 konvensi dan sudah terdaftar di `.env.example` dan `spectra.config.ts`. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log (dipakai sebagai precondition TC dan diasersi sebagai baris pembanding): tab Session memuat sedikitnya dua baris dengan nilai Date berbeda (Pre-setup No 9) dan tab User Action memuat sedikitnya satu baris (Pre-setup No 10). Mekanisme seeding log tidak didefinisikan di TC, PRD, atau LLD yang dibaca; seeding disediakan tim FE/BE (lihat Temuan untuk QA). Tidak ada total entri yang diasersi.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): hover baris tabel (state Hover) dan klik sel tabel; tombol Esc untuk menutup Overlay Column Visibility dan pilihan Rows per page.
- State global: tidak ada yang diubah (spec read-only, tanpa aksi tulis).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-01: Screening 3 zona Tab Session

1. Klik menu Activity Log di sidebar Admin Console
2. Verifikasi Header: Breadcrumb `Activity Log > Session`
3. Verifikasi Header: segmen `Session` pada Breadcrumb bukan link
4. Verifikasi Header: Tab `Session (aktif) | User Action`
5. Verifikasi Header: Table Tools memuat `Search | Filter | Download`
6. Verifikasi Header: Table Tools rata kanan
7. Verifikasi Header: tidak ada tombol create
8. Verifikasi Body: kolom `Date (sortable) | User (sortable) | Employee ID (sortable) | Position (sortable) | Division (sortable) | Activity (sortable) | Status (sortable) | Note (sortable) | IP Address (sortable) | Device / Browser (sortable) | Actions (⋯)`
9. Klik header kolom `⋯`
10. Verifikasi header `⋯` membuka Overlay Column Visibility
11. Tutup Overlay Column Visibility dengan `Esc`
12. Verifikasi Body: sedikitnya dua baris log Session tampil
13. Verifikasi Body: sel kolom Actions (⋯) pada tiap baris kosong
14. Verifikasi Body: tidak ada row action pada tiap baris
15. Verifikasi Body: tidak ada kolom checkbox
16. Verifikasi Body: Date terbaru di atas
17. Verifikasi Footer: pagination `Showing X–Y of Z entries`
18. Verifikasi Footer: Rows per page `10`
19. Buka pilihan Rows per page
20. Verifikasi Footer: pilihan Rows per page `10`, `25`, `50`, `100`
21. Tutup pilihan Rows per page dengan `Esc`
22. Verifikasi Footer: `[← Prev] [Page] [Next →]`

### TC-AC-ACAL-16: Baris tabel tidak dapat diklik, kedua tab

23. Klik sel User pada satu baris tab Session
24. Klik sel Note pada satu baris tab Session
25. Verifikasi tab Session: tidak ada navigasi, popup, atau Detail
26. Arahkan kursor ke sel User pada satu baris
27. Verifikasi tab Session: teks sel tidak bergaya link saat hover
28. Verifikasi tab Session: hover baris menampilkan state Hover (latar berubah dari Default white)
29. Verifikasi tab Session: tidak ada state Selected pada baris setelah klik
30. Klik tab "User Action"
31. Klik sel Name pada satu baris tab User Action
32. Klik sel Object pada satu baris tab User Action
33. Verifikasi tab User Action: tidak ada navigasi, popup, atau Detail
34. Arahkan kursor ke satu baris tab User Action
35. Verifikasi tab User Action: hover baris menampilkan state Hover (latar berubah dari Default white)
36. Verifikasi tab User Action: tidak ada state Selected pada baris setelah klik

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-01, 16). Tidak ada TC hanya-BE di spec ini.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Spec ini 36 langkah (di atas 35 langkah): satu langkah muncul karena S-01 memecah klausa yang digabung. TC-AC-ACAL-01 dan TC-AC-ACAL-16 adalah screening halaman yang sama dengan dataset yang sama; memecahnya menjadi dua spec hanya menambah satu pembukaan halaman tanpa mengurangi langkah, sehingga digabung (bagian 3 konvensi).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 11 (tutup Overlay Column Visibility dengan `Esc`) dan langkah 19 sampai 21 (membuka pilihan Rows per page hanya untuk membuktikan butir Expected TC-01 c, lalu menutupnya).
- Langkah "Verifikasi ... sedikitnya dua baris ... tampil" (langkah 12) adalah `Verifikasi` data pembanding (anchor) untuk asersi universal pada surface yang sama (sel Actions kosong pada tiap baris, langkah 13 dan 14; Date terbaru di atas, langkah 16); Expected TC tidak memuatnya. Expected TC-01 b yang bermajemuk dipecah satu `Verifikasi` per klausa (S-01).
- TC-16 Expected c menyebut "kedua tab" tanpa memerinci tab untuk klausa hover baris; spec mengasersi state Hover dan tidak adanya state Selected di kedua tab.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` (Pre-setup No 1) dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding Data Log (Pre-setup No 9 dan No 10) tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan seeding diminta dari tim FE/BE.
  - TC-01 Expected menyebut header `⋯` pada kolom Actions; spec mengikuti TC.
  - TC-16 Expected c tidak menyebut tab untuk klausa hover baris; spec mengasersi di kedua tab.
