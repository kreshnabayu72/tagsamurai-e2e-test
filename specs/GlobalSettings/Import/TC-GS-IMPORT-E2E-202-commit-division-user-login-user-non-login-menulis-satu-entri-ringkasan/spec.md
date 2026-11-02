---
id: TC-GS-IMPORT-E2E-202-commit-division-user-login-user-non-login-menulis-satu-entri-ringkasan
title: "Commit Division, User Login, User Non Login menulis satu entri ringkasan ke Changelog Import, System Log, Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-422
  - TC-GS-IMPORT-423
  - TC-GS-IMPORT-424
coverage:
  web: automated
---

# Commit Division, User Login, User Non Login menulis satu entri ringkasan ke Changelog Import, System Log, Activity Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit sungguhan di Client E (pembuat data, destruktif) dan menunggu worker commit nyata (batas tunggu 2 menit per commit) (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E; Sub-Tab Division, User Login, dan User Non Login dibuka di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Produk organisasi Client E: Global Settings dan Fixed Asset. Master data Client E seperti Client A (R4), termasuk Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang`, Position `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor`, `Store Manager`, serta User Login aktif `rina.admin.e`, `budi.manager.e`, `dewi.anggraini.e` (@example.com) sebagai Represented By.
- Data Dinamis (draft commit Client E, disiapkan oleh langkah 1 lewat skrip seed; Client E direset tanpa draft oleh hook `beforeEach` sebelum langkah 1, Kontrak Fixture R1):
  - D-53: draft Division 6 baris `pending` dari `division-commit-6.csv` (Division Name/Code): Finance & Accounting/FIN, Operations/(kosong), IT Support/ITS, Procurement/PRC, Sales/SLS, Legal/LGL.
  - D-54: draft User Login 8 baris `pending` dari `user-login-commit-8.csv` (kolom First Name; Last Name; Email; Division; Position; Employee ID; Access; Active Period; Shift; Overtime Hours): #1 Rizky Pratama / Engineering / Senior Developer / EMP-5001 / `Global Settings;Fixed Asset` / Shift `Siang`; #2 Sinta Maharani / Marketing / Position kosong / `Global Settings` / Active Period H+30 (30 hari setelah hari eksekusi, `YYYY-MM-DD`) / Shift `Siang`; #3 Doni Kurniawan / Finance / Finance Manager / `Fixed Asset` / Shift `Pagi`; #4 Eka Putri / Warehouse / Technician / `Global Settings` / Overtime Hours `1.25`; #5 Fajar Hidayat / Gudang / Supervisor / `Global Settings;Fixed Asset`; #6 Gita Savitri / Gudang / Store Manager / `Global Settings`; #7 Hendra Gunawan / Gudang / Position kosong / `Fixed Asset`; #8 Indah Permata / Finance / Position kosong / `Global Settings`; sel lain kosong. Email tiap baris berbentuk `<nama.depan>.<nama.belakang>+{runId}-202@example.com` (suffix per run; TC menulis tanpa suffix).
  - D-55: draft User Non Login 5 baris `pending` dari `user-non-login-commit-5.csv` (kolom First Name; Last Name; Email; Division; Position; Employee ID; Represented By; Active Period): #1 Joko Santoso / Engineering / Position kosong / Represented By `rina.admin.e@example.com`; #2 Kartika Dewi / Marketing / Supervisor / EMP-6002 / Represented By `budi.manager.e@example.com` / Active Period H+30; #3 Lukman Hakim / Finance / Position kosong / Represented By `dewi.anggraini.e@example.com`; #4 Maya Sari / Warehouse / Position kosong / Represented By `rina.admin.e@example.com`; #5 Nanda Wijaya / Gudang / Position kosong / Represented By `budi.manager.e@example.com`. Email dengan suffix per run seperti D-54.
  - Nama Division literal dipakai karena Client E khusus commit dan Division hasil commit dihapus di hook `after`; asersi tidak bergantung pada nama record.
- Log (baseline S-12): jumlah total entri pada Pagination (Filter Action = `Import Division`, `Import User Login`, atau `Import User Non Login`) dicatat per surface sebelum commit; asersi "bertambah tepat satu" membandingkan dengan baseline itu (0 bila empty state). Total tidak diasersi sebagai angka absolut. Surface: Changelog Import (icon `[Changelog]` di header) dan Activity Log (Global Settings > Activity Log, tab User Action).
- Akun tampil: Modified By `Yoga P` (Total Control Client E: Yoga Permana), format `[First Name] [Last Initial]`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh, D-47): hapus Division, User Login, dan User Non Login hasil commit (D-53, D-54, D-55) di Client E; hapus draft; reset hasil commit terakhir dan penanda Banner Hasil Commit.
- Kemampuan teknis: skrip seed draft D-53 sampai D-55; skrip reset Client E (D-47); worker commit berjalan normal.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Entri ringkasan Division (TC-GS-IMPORT-422)

1. Seed draft Division D-53 (6 baris), User Login D-54 (8 baris), dan User Non Login D-55 (5 baris) di Client E lewat skrip seed, lalu muat ulang halaman Import > Brand
2. Buka Changelog Import, terapkan Filter Action = `Import Division`, lalu catat total entri pada Pagination sebagai baseline Changelog (0 bila empty state)
3. Tutup modal Changelog Import
4. Buka Activity Log (Global Settings > Activity Log) pada tab User Action, terapkan Filter Action = `Import Division`, lalu catat total entri pada Pagination sebagai baseline Activity Log (0 bila empty state)
5. Buka halaman Import > Division
6. Klik `[Import (6)]`
7. Tunggu aksi selesai (permintaan mendapat respons)
8. Muat ulang halaman Import > Division setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
9. Buka Changelog Import, terapkan Filter Action = `Import Division`, lalu baca total entri pada Pagination
10. Verifikasi total Changelog Import bertambah tepat satu dibanding baseline langkah 2
11. Verifikasi baris pertama tabel (sort default Date descending): Action `Import Division` (plain text), Data `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
12. Tutup modal Changelog Import
13. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import Division`, lalu baca total entri pada Pagination
14. Verifikasi total Activity Log bertambah tepat satu dibanding baseline langkah 4
15. Verifikasi baris pertama tabel (sort default Date descending): Action `Import Division` (plain text), Object `Import`, Name `Division`, Field `Import Summary`, Old Value `—`, New Value `6 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`

### Entri ringkasan User Login (TC-GS-IMPORT-423)

16. Buka halaman Import > User Login
17. Buka Changelog Import, terapkan Filter Action = `Import User Login`, lalu catat total entri pada Pagination sebagai baseline Changelog (0 bila empty state)
18. Tutup modal Changelog Import
19. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import User Login`, lalu catat total entri pada Pagination sebagai baseline Activity Log (0 bila empty state)
20. Buka halaman Import > User Login
21. Klik `[Import (8)]`
22. Tunggu aksi selesai (permintaan mendapat respons)
23. Muat ulang halaman Import > User Login setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
24. Buka Changelog Import, terapkan Filter Action = `Import User Login`, lalu baca total entri pada Pagination
25. Verifikasi total Changelog Import bertambah tepat satu dibanding baseline langkah 17
26. Verifikasi baris pertama tabel: Action `Import User Login` (plain text), Data `8 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
27. Tutup modal Changelog Import
28. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import User Login`, lalu baca total entri pada Pagination
29. Verifikasi total Activity Log bertambah tepat satu dibanding baseline langkah 19
30. Verifikasi baris pertama tabel: Action `Import User Login` (plain text), Object `Import`, Name `User Login`, Field `Import Summary`, Old Value `—`, New Value `8 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`

### Entri ringkasan User Non Login (TC-GS-IMPORT-424)

31. Buka halaman Import > User Non Login
32. Buka Changelog Import, terapkan Filter Action = `Import User Non Login`, lalu catat total entri pada Pagination sebagai baseline Changelog (0 bila empty state)
33. Tutup modal Changelog Import
34. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import User Non Login`, lalu catat total entri pada Pagination sebagai baseline Activity Log (0 bila empty state)
35. Buka halaman Import > User Non Login
36. Klik `[Import (5)]`
37. Tunggu aksi selesai (permintaan mendapat respons)
38. Muat ulang halaman Import > User Non Login setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
39. Buka Changelog Import, terapkan Filter Action = `Import User Non Login`, lalu baca total entri pada Pagination
40. Verifikasi total Changelog Import bertambah tepat satu dibanding baseline langkah 32
41. Verifikasi baris pertama tabel: Action `Import User Non Login` (plain text), Data `5 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`
42. Tutup modal Changelog Import
43. Buka Activity Log pada tab User Action, terapkan Filter Action = `Import User Non Login`, lalu baca total entri pada Pagination
44. Verifikasi total Activity Log bertambah tepat satu dibanding baseline langkah 34
45. Verifikasi baris pertama tabel: Action `Import User Non Login` (plain text), Object `Import`, Name `User Non Login`, Field `Import Summary`, Old Value `—`, New Value `5 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Yoga P`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 45 langkah, di atas 35 langkah; tiap blok berpola sama (baseline, commit, tunggu, baca log) dan berdiri sendiri.
- Langkah 8, 23, dan 38 menunggu worker commit nyata (muat ulang tiap 5 detik, batas 2 menit) seperti yang tertulis di TC.
- Langkah 2 dan 4, 17 dan 19, serta 32 dan 34 mencatat baseline sebelum aksi pemicu pertama yang diasersi (S-12).
- Langkah 1 adalah langkah penghubung pembuka (seed draft D-53 sampai D-55; S-03), tanpa `Verifikasi`. Langkah 7, 22, dan 37 adalah langkah penghubung "Tunggu aksi selesai" sesudah `[Import (N)]` (S-03). Langkah 16 dan 31 membuka halaman Import Sub-Tab terkait sebelum membuka Changelog Import, karena langkah sebelumnya membaca Activity Log (S-03). Langkah 3, 12, 18, 27, 33, dan 42 adalah langkah penghubung `Tutup modal Changelog Import` tanpa `Verifikasi`, supaya modal tidak masih terbuka saat Activity Log atau halaman Import dibuka (S-03).
- Temuan untuk QA:
  - Penanda selesai untuk langkah 7, 22, dan 37 (`[Import (N)]`) tidak disebut di TC-GS-IMPORT-422, 423, 424; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
  - TC-GS-IMPORT-422, 423, 424 Post Condition a, b, c (draft dihapus, record tersimpan di halaman master, entri tercatat) tidak punya langkah observasi di TC selain Expected a-b; tidak diasersi terpisah (S-01).
  - TC-GS-IMPORT-423 Data Uji menulis Email tanpa suffix per run (`rizky.pratama@example.com`, dan seterusnya) dan TC-GS-IMPORT-424 sama; spec memakai suffix per run, nama dan Employee ID tetap literal.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
