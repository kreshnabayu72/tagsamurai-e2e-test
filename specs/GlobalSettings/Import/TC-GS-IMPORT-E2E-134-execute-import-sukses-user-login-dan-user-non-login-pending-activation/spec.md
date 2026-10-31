---
id: TC-GS-IMPORT-E2E-134-execute-import-sukses-user-login-dan-user-non-login-pending-activation
title: "Execute Import sukses: User Login dan User Non Login (Pending Activation, Temporary User, detail user, entri Changelog Import)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-356
  - TC-GS-IMPORT-357
coverage:
  web: automated
---

# Execute Import sukses: User Login dan User Non Login (Pending Activation, Temporary User, detail user, entri Changelog Import)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Client E); langkah pertama berpindah ke Tab User Login.
- Client E khusus commit: produk organisasi Global Settings dan Fixed Asset; Date Format `dd MMM yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`. Master data Pre-setup seperti Client A (Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang`; Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor`; Custom Field Active `Shift` Dropdown (`Pagi`, `Siang`, `Malam`), `Shift Notes`, `Overtime Hours` (Numeric 2 desimal), `Emergency Phone`, `Join Date`). User Login aktif Client E (Pre-setup): `rina.admin.e@example.com`, `budi.manager.e@example.com`, `dewi.anggraini.e@example.com`.
- Data Dinamis (fixture baru; nama dan email literal dari berkas TC karena Client E dedicated commit dan direset sesuai D-47):
  - `Fixture.import.userLoginCommit8` (user-login-commit-8.csv, D-54): draft User Login 8 baris `pending`, kolom First Name, Last Name, Email, Division, Position, Employee ID, Access, Active Period, Shift, Overtime Hours: #1 Rizky Pratama / rizky.pratama@example.com / Engineering / Senior Developer / EMP-5001 / `Global Settings;Fixed Asset` / Shift `Siang`; #2 Sinta Maharani / sinta.maharani@example.com / Marketing / Position kosong / `Global Settings` / Active Period H+30 (30 hari setelah hari eksekusi, format YYYY-MM-DD, dihitung hook saat penyiapan) / Shift `Siang`; #3 Doni Kurniawan / doni.kurniawan@example.com / Finance / Finance Manager / `Fixed Asset` / Shift `Pagi`; #4 Eka Putri / eka.putri@example.com / Warehouse / Technician / `Global Settings` / Overtime Hours `1.25`; #5 Fajar Hidayat / fajar.hidayat@example.com / Gudang / Supervisor / `Global Settings;Fixed Asset`; #6 Gita Savitri / gita.savitri@example.com / Gudang / Store Manager / `Global Settings`; #7 Hendra Gunawan / hendra.gunawan@example.com / Gudang / Position kosong / `Fixed Asset`; #8 Indah Permata / indah.permata@example.com / Finance / Position kosong / `Global Settings`; sel lain kosong.
  - `Fixture.import.userNonLoginCommit5` (user-non-login-commit-5.csv, D-55): draft User Non Login 5 baris `pending`, kolom First Name, Last Name, Email, Division, Position, Employee ID, Represented By, Active Period: #1 Joko Santoso / joko.santoso@example.com / Engineering / Position kosong / Represented By `rina.admin.e@example.com`; #2 Kartika Dewi / kartika.dewi@example.com / Marketing / Supervisor / EMP-6002 / Represented By `budi.manager.e@example.com` / Active Period H+30; #3 Lukman Hakim / lukman.hakim@example.com / Finance / Position kosong / `dewi.anggraini.e@example.com`; #4 Maya Sari / maya.sari@example.com / Warehouse / Position kosong / `rina.admin.e@example.com`; #5 Nanda Wijaya / nanda.wijaya@example.com / Gudang / Position kosong / `budi.manager.e@example.com`; sel lain kosong.
- Kemampuan teknis yang disediakan tim FE/BE: penyiapan draft Client E lewat fixture dengan Active Period H+30 dihitung dari hari eksekusi; reset Client E sesuai D-47 (hapus User Login dan User Non Login hasil commit, hapus draft, reset hasil commit terakhir dan penanda Banner Hasil Commit); worker commit normal (tunggu commit selesai dengan batas 2 menit, muat ulang tiap 5 detik).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47 dan pulihkan sesi ke akun default suite. Hook `afterEach` suite juga mereset Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- State global: Client E berubah permanen oleh commit dan dipulihkan oleh reset D-47; suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `GS_CLIENTE_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-356: Import 8 baris User Login

1. Buka Tab User Login pada halaman Import, siapkan draft User Login 8 baris (user-login-commit-8.csv, D-54) di Client E lewat fixture, lalu muat ulang halaman Import > User Login
2. Catat baseline: buka Changelog Import (icon [Changelog] di header halaman), baca total pada teks Pagination (0 bila empty state), lalu tutup modal
3. Klik [Import (8)]
4. Muat ulang halaman Import > User Login setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
5. Verifikasi Dropzone tampil menggantikan Staging Table
6. Verifikasi Unsaved Banner tidak tampil
7. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil di atas halaman dengan tombol `[×]`
8. Buka halaman User > User List > Login User
9. Atur Rows per page 100
10. Verifikasi halaman User > User List > Login User Client E memuat 8 user baru: Rizky Pratama, Sinta Maharani, Doni Kurniawan, Eka Putri, Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata
11. Verifikasi kedelapan user baru berstatus aktivasi `Pending Activation`
12. Buka Detail user `Rizky Pratama`
13. Verifikasi Detail `Rizky Pratama`: Division `Engineering`
14. Verifikasi Detail `Rizky Pratama`: Position `Senior Developer`
15. Verifikasi Detail `Rizky Pratama`: Employee ID `EMP-5001`
16. Verifikasi Detail `Rizky Pratama`: Access `Global Settings` dan `Fixed Asset`
17. Verifikasi Detail `Rizky Pratama`: Custom Field Shift `Siang`
18. Buka Detail user `Sinta Maharani`
19. Verifikasi Detail `Sinta Maharani` tercatat sebagai Temporary User
20. Verifikasi Detail `Sinta Maharani`: Temporary Until sama dengan tanggal Active Period pada berkas (H+30)
21. Buka Detail user `Doni Kurniawan`
22. Verifikasi Detail `Doni Kurniawan`: Position `Finance Manager`
23. Verifikasi Detail `Doni Kurniawan`: Access `Fixed Asset`
24. Verifikasi Detail `Doni Kurniawan`: Custom Field Shift `Pagi`
25. Buka Detail user `Eka Putri`
26. Verifikasi Detail `Eka Putri`: Custom Field Overtime Hours `1.25`
27. Buka halaman Import > User Login
28. Buka Changelog Import (icon [Changelog] di header halaman)
29. Verifikasi total pada teks Pagination Changelog Import bertambah tepat satu dibanding baseline
30. Verifikasi entri teratas (sort default Date descending): Action `Import User Login`, Data `8 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
31. Tutup modal Changelog Import dan reset Client E sesuai D-47 lewat fixture

### TC-GS-IMPORT-357: Import 5 baris User Non Login

32. Buka Tab User Non Login pada halaman Import, siapkan draft User Non Login 5 baris (user-non-login-commit-5.csv, D-55) di Client E lewat fixture, lalu muat ulang halaman Import > User Non Login
33. Catat baseline: buka Changelog Import, baca total pada teks Pagination (0 bila empty state), lalu tutup modal
34. Klik [Import (5)]
35. Muat ulang halaman Import > User Non Login setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
36. Verifikasi Dropzone tampil menggantikan Staging Table
37. Verifikasi Unsaved Banner tidak tampil
38. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil di atas halaman dengan tombol `[×]`
39. Buka halaman User > User List > Non-Login User
40. Verifikasi halaman User > User List > Non-Login User Client E memuat 5 user baru: Joko Santoso, Kartika Dewi, Lukman Hakim, Maya Sari, Nanda Wijaya
41. Verifikasi kelima user baru berstatus `active`
42. Buka Detail user `Joko Santoso`
43. Verifikasi Detail `Joko Santoso`: Division `Engineering`
44. Verifikasi Detail `Joko Santoso`: Represented By `rina.admin.e@example.com`
45. Buka Detail user `Kartika Dewi`
46. Verifikasi Detail `Kartika Dewi`: Position `Supervisor`
47. Verifikasi Detail `Kartika Dewi`: Employee ID `EMP-6002`
48. Verifikasi Detail `Kartika Dewi`: Represented By `budi.manager.e@example.com`
49. Verifikasi Detail `Kartika Dewi` tercatat sebagai Temporary User
50. Verifikasi Detail `Kartika Dewi`: Temporary Until sama dengan tanggal Active Period pada berkas (H+30)
51. Buka halaman Import > User Non Login
52. Buka Changelog Import (icon [Changelog] di header halaman)
53. Verifikasi total pada teks Pagination Changelog Import bertambah tepat satu dibanding baseline
54. Verifikasi entri teratas (sort default Date descending): Action `Import User Non Login`, Data `5 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-356, 357).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 32 (penyiapan draft sebagai precondition TC lewat fixture dan berpindah Tab); langkah 2 dan 33 (baseline jumlah entri Changelog Import sebelum aksi pemicu pertama yang diasersi, S-12); langkah 31 (menutup modal dan reset Client E sesuai D-47 sebelum TC berikutnya); langkah 9 (Rows per page 100 agar kedelapan user baru tampil). Pembukaan Detail user adalah aksi observasi.
- Baseline Changelog: total Changelog tidak diasersi sebagai angka absolut; entri yang diasersi dicari sebagai entri teratas sesuai sort default Date descending setelah total bertambah tepat satu (S-12).
- Tanggal H+30: dihitung hook penyiapan dari hari eksekusi dan ditulis ke berkas (YYYY-MM-DD); Temporary Until dibandingkan dengan tanggal itu. Pre-setup Client E menetapkan Date Format `dd MMM yy`, sehingga tampilan tanggal di Detail mengikuti format itu.
- Spec ini di atas sekitar 35 langkah (54 langkah). Alasan: dua blok homogen (siapkan draft, Import, tunggu commit, periksa banner, periksa daftar user dan Detail user, periksa Changelog Import) yang berdiri sendiri dengan draft dan reset Client E sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: commit Brand, Measurement, Position, Division di spec 133; Partial Commit di spec 135.
- Temuan untuk QA:
  - TC-GS-IMPORT-356 Expected d hingga g tidak menyebut nilai default untuk field Detail user yang tidak diisi berkas; spec hanya mengasersi field yang disebut TC.
  - TC-GS-IMPORT-356 menyebut "status aktivasi `Pending Activation`" tanpa menyebut label kolom di Login User; spec mengasersi status per user tanpa menyebut nama kolom.
  - TC-GS-IMPORT-356 dan 357 tidak merujuk D-47 pada kolom D-ref meski Post Condition dan Kontrak Fixture R1 menyatakan reset Client E; dicatat sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-356 mencantumkan produk organisasi Client E (Global Settings dan Fixed Asset) pada Precondition tanpa langkah yang memverifikasinya; spec menuliskannya sebagai Pre-setup.
  - TC-GS-IMPORT-356 dan 357 bertanda FE Test `Need API` tanpa menyebut endpoint; spec tidak menyebut endpoint (S-13).
  - Baseline Changelog tidak ada pada TC; spec menambah langkah baseline (S-12) sebagai langkah penghubung.
