---
id: TC-FA-TDC-E2E-036-job-latar-j-01-j-02-j-03-tetap-berjalan-saat-suspended-atau-expired
title: "Job Latar J-01, J-02, dan J-03 Tetap Berjalan saat Entitas Suspended atau Expired"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-891
  - TC-FA-TDC-892
  - TC-FA-TDC-893
  - TC-FA-TDC-894
  - TC-FA-TDC-360
coverage:
  web: automated
---

# Job Latar J-01, J-02, dan J-03 Tetap Berjalan saat Entitas Suspended atau Expired

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada dua company uji khusus automation: Company Suspended (entitas client berstatus Suspended) dan Company Expired (entitas client berstatus Expired). Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; nilainya disediakan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada Company Suspended; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (di-seed fixture BE di hook `before`, dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE):
  - Company Suspended: class NB-1 dengan versi Current Effective From Jan 2025 dan versi Scheduled Effective From Jan 2026 yang tercapai (TC-FA-TDC-891); class NB-KHS dengan Last Posted Tax Year kosong (TC-FA-TDC-893); untuk TC-FA-TDC-894 tabel dikosongkan lewat fixture BE (pembuatan seed pada aktivasi modul akuntansi gagal sehingga tab menampilkan Empty State biasa) pada langkah 21.
  - Company Expired: class NB-1 dengan versi Current Effective From Jan 2025 dan versi Scheduled Effective From Jan 2026 yang tercapai (TC-FA-TDC-892); class `KHS-LP` Non-building, Active, Used By 0, Last Posted Tax Year kosong (TC-FA-TDC-360).
- Kendali jam sistem (clock): jam server dan jam browser diatur bersama ke 1 Januari 2026 00:00 Asia/Jakarta (tanggal sistem uji, Time Zone entitas Asia/Jakarta) pada langkah 2, dipulihkan di hook `after` (bagian 6); jam server dan jam browser sinkron.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): memicu job J-01, J-02 lewat penjadwal uji; memicu posting penyusutan fiskal J-03 lewat fixture BE; membaca jumlah entri Changelog per class dan modul (baseline dibaca tepat sebelum pemicu tiap TC, 8b.10, S-12). Status entitas Suspended dan Expired dibentuk fixture BE dan tidak diubah spec ini.
- Entri Changelog yang dibuat saat jam digeser dapat berada di bawah entri lama; asersi memakai selisih jumlah entri terhadap baseline dan mencari baris berdasarkan Class Code dan Field, bukan posisi teratas (S-12, S-14).
- State global: jam server dan browser, data class company uji; dipulihkan di hook `after`.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; kendali jam; seed dan pemulihan lewat API).

## Test Steps

### Company Suspended: J-02 (TC-FA-TDC-891)

1. Catat baseline jumlah entri Changelog untuk NB-1
2. Atur jam server dan jam browser ke 1 Januari 2026 00:00 Asia/Jakarta
3. Picu job J-02
4. Muat ulang halaman dengan F5
5. Verifikasi kolom Effective From baris NB-1 menampilkan `Jan 2026`
6. Klik icon Changelog di toolbar
7. Verifikasi jumlah entri Changelog untuk NB-1 bertambah satu dari baseline
8. Verifikasi Changelog memuat baris Edit NB-1 Field `Current Version` Old Value `Jan 2025` New Value `Jan 2026` dengan Modified By `System`
9. Tutup Popup Changelog

### Company Suspended: J-03 (TC-FA-TDC-893)

10. Catat baseline jumlah entri Changelog untuk NB-KHS
11. Picu posting penyusutan fiskal tahun pajak 2026 untuk NB-KHS lewat fixture BE (J-03)
12. Muat ulang halaman dengan F5
13. Klik Class Code NB-KHS
14. Verifikasi field Last Posted Tax Year NB-KHS bernilai `2026`
15. Verifikasi Class Code NB-KHS Disabled
16. Tutup Drawer dengan `[×]`
17. Klik icon Changelog di toolbar
18. Verifikasi jumlah entri Changelog untuk NB-KHS bertambah satu dari baseline
19. Verifikasi Changelog memuat baris Edit NB-KHS Field `Last Posted Tax Year` Old Value `—` New Value `2026` dengan Modified By `System`
20. Tutup Popup Changelog

### Company Suspended: J-01 (TC-FA-TDC-894)

21. Kosongkan seluruh Tax Depreciation Class (semua status) lewat fixture BE hingga tersimpan
22. Muat ulang halaman dengan F5
23. Catat baseline jumlah entri Changelog modul Tax Depreciation Class
24. Picu job J-01
25. Muat ulang tab Tax Depreciation Class dengan F5
26. Verifikasi tabel memuat tujuh class seed berstatus Active: NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, dan LAND
27. Klik icon Changelog di toolbar
28. Verifikasi jumlah entri Changelog modul bertambah tujuh dari baseline
29. Verifikasi Changelog memuat baris Create untuk tiap class seed dengan Field `Class Code` dan Modified By `System`
30. Tutup Popup Changelog

### Company Expired: J-02 (TC-FA-TDC-892)

31. Logout
32. Login sebagai Total Control pada Company Expired
33. Buka Settings > Accounting > Tax Depreciation Class
34. Catat baseline jumlah entri Changelog untuk NB-1
35. Picu job J-02
36. Muat ulang halaman dengan F5
37. Verifikasi kolom Effective From baris NB-1 menampilkan `Jan 2026`
38. Klik icon Changelog di toolbar
39. Verifikasi jumlah entri Changelog untuk NB-1 bertambah satu dari baseline
40. Verifikasi Changelog memuat baris Edit NB-1 Field `Current Version` Old Value `Jan 2025` New Value `Jan 2026` dengan Modified By `System`
41. Tutup Popup Changelog

### Company Expired: J-03 (TC-FA-TDC-360)

42. Picu posting penyusutan fiskal tahun pajak 2026 untuk `KHS-LP` lewat fixture BE (J-03)
43. Muat ulang halaman dengan F5
44. Klik Class Code `KHS-LP`
45. Verifikasi field Last Posted Tax Year bernilai `2026`
46. Tutup Drawer dengan `[×]`

## Notes

- Langkah penghubung (S-03): langkah 4, 12, 22, 25, 36, dan 43 memuat ulang halaman agar hasil job terbaca; langkah 9, 16, 20, 30, 41, dan 46 menutup popup dan Drawer yang tidak dirty; langkah 21 membentuk precondition TC-FA-TDC-894 lewat fixture BE; langkah 31 sampai 33 adalah ganti akun eksplisit ke Company Expired (S-07). Baris target ditemukan tanpa Search karena tiap company memuat baris pada satu halaman (dinyatakan di Prerequisites).
- Job latar J-01, J-02, dan J-03 (termasuk posting J-03 lewat fixture BE) hanya memicu kondisi yang diuji dan bukan objek asersi; pemicunya adalah langkah aksi tanpa asersi sendiri, dan yang diasersi adalah hasilnya pada entitas Suspended atau Expired (kelas h). Penjadwal uji dan fixture BE disediakan tim FE/BE.
- Baseline blok pertama (langkah 1) dicatat sebelum jam digeser (langkah 2). Baseline blok berikutnya (langkah 10, 23, 34) dicatat saat jam masih digeser karena jam digeser sekali untuk seluruh spec dan baru dipulihkan di hook `after` (versi Scheduled Jan 2026 harus tercapai pada setiap pemicu J-02); baseline berupa hitungan entri, bukan cap waktu, dan baseline serta pemicu tiap blok dibaca pada kondisi jam yang sama, sehingga selisih jumlah (S-12) tidak terpengaruh pergeseran jam. Jam tidak dipulihkan di antara blok (R-10): pemulihan lalu pergeseran ulang hanya menambah langkah tanpa mengubah hitungan entri yang dibandingkan.
- Langkah 8, 19, 29, dan 40: baris dicari berdasarkan Class Code dan Field setelah selisih jumlah entri dibuktikan (S-12, S-14), tidak mengandalkan posisi teratas karena jam digeser.
- TC-FA-TDC-360 memuat Post Condition "satu entri L-10 Modified By System tercatat" tanpa langkah observasi di TC; tidak diasersi (S-01) dan dicatat di Temuan untuk QA.
- Alasan spec melewati sekitar 35 langkah (46 langkah): seluruh blok satu kelas harness (h, job latar pada entitas Suspended atau Expired) dengan pola asersi yang sama. Blok tidak berdiri sepenuhnya sendiri: kelimanya memakai satu pergeseran jam (langkah 2) dan satu sesi per company, sehingga jam tidak digeser ulang per blok dan ganti akun hanya sekali (langkah 31 sampai 33); dataset, baseline, dan job pemicu tiap blok terpisah.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control untuk status Suspended dan Expired.
  - TC-FA-TDC-360 diberi label Automation `Manual Only` (status Suspended diatur dari Admin Console) tetapi preconditionnya Expired; spec memakai status entitas dari fixture BE.
  - TC-FA-TDC-360 memiliki Post Condition tanpa langkah observasi (L-10 Modified By System); tidak diasersi.
  - TC-FA-TDC-891 dan 892 menyebut "baris terbaru NB-1" di Changelog; karena jam digeser, spec mencari baris berdasarkan isinya (S-12).
  - TC-FA-TDC-894 membaca jumlah baris L-01 tujuh class seed dengan satu langkah "lihat baris L-01"; spec mengasersi tujuh entri Create sebagai himpunan.
