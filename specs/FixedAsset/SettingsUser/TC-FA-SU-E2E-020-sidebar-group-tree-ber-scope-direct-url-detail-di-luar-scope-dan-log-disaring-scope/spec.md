---
id: TC-FA-SU-E2E-020-sidebar-group-tree-ber-scope-direct-url-detail-di-luar-scope-dan-log-disaring-scope
title: "Sidebar Group Tree Ber-scope, Direct URL Detail di Luar Scope, dan Log Disaring Scope"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-61
  - TC-FA-SU-62
  - TC-FA-SU-63
  - TC-FA-SU-64
  - TC-FA-SU-65
coverage:
  web: automated
---

# Sidebar Group Tree Ber-scope, Direct URL Detail di Luar Scope, dan Log Disaring Scope

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role Group (Update) (Sinta Dewi, Pre-setup #6); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control (Lina Marlina). Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (satu blok per aktor karena ganti akun menuntut Step eksplisit):

| Aktor | Pre-setup | Nama | Email | Env password |
|---|---|---|---|---|
| Manage user & role Group (Update) | #6 | Sinta Dewi | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURGR_UPD_PASSWORD` |
| Total Control | #1 | Lina Marlina | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Nama env `FA_MURGR_UPD_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20), pohon grup (#21: All Groups > Finance & Accounting (anak: Accounts Payable), IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa (anak: Jakarta Selatan Distribution Center)), Changelog (#27), System Log Budi Santoso 7 baris (#28; Name target: Hana Kusuma, Oscar Pranata, Lina Marlina, Eka Wulandari), Transaction Admin Log Budi Santoso 5 baris (#29), Global Settings (#38). Scope Sinta Dewi: Finance & Accounting dan turunannya; pengguna dalam scope: Ahmad Dahlan, Budi Santoso, Citra Lestari, Gita Permata, Lina Marlina, Nanda Pratama, Oscar Pranata, Putri Anggraeni, Sinta Dewi, Teguh Prakoso, Umar Faruq, Wawan Setiawan. Pengguna di luar scope: Indra Wijaya, Eka Wulandari, Rudi Hartono, Rina Susanti, Qori Akbar, Doni Prasetyo, Hana Kusuma.
- Data Dinamis (TC-FA-SU-63, hook `before`, dihapus di hook `after`): satu pengguna "Pengguna Revoke" bernama `Fa Revoke {runId}-020` dengan email `fa-revoke+{runId}-020@qwertysystem.net` yang memegang App Access FAMS pada Client `FaUserMain`, dibuat lewat seed API (kemampuan disediakan tim FE/BE). Pengguna ini dipakai sebagai target pencabutan App Access, bukan pengguna Pre-setup (S-06).
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; mengetik URL di address bar; hover; Download CSV dengan pembacaan isi berkas (nilai sel) disediakan tim FE; sesi API Principal Automation (Pre-setup #12) untuk mencabut App Access FAMS dan memulihkannya (kemampuan disediakan tim FE).
- State global yang diubah: App Access FAMS Pengguna Revoke (dicabut pada TC-FA-SU-63); hook `after` memulihkan atau menghapus pengguna itu lewat seed API. Data Pre-setup tidak diubah.

## Test Steps

### TC-FA-SU-61: Sidebar Group Tree hanya memuat node dalam scope aktor ber-scope grup

1. Klik Expand All pada Sidebar Group Tree
2. Verifikasi Sidebar Group Tree memuat node Finance & Accounting dan Accounts Payable
3. Verifikasi node `All Groups` tampil dan mewakili seluruh scope aktor
4. Verifikasi node IT Infrastructure, Branch Surabaya, General Affairs, dan Logistics Warehouse tidak tampil
5. Ganti akun: logout lalu login sebagai Total Control (Lina Marlina)
6. Buka Settings > User dari sidebar
7. Klik Expand All pada Sidebar Group Tree
8. Verifikasi Sidebar Group Tree memuat seluruh node: All Groups, Finance & Accounting, Accounts Payable, IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa, dan Jakarta Selatan Distribution Center

### TC-FA-SU-63: Direct URL Detail pengguna tanpa App Access FAMS

9. Cabut App Access FAMS Pengguna Revoke di Global Settings lewat sesi API Principal Automation hingga pencabutan tersimpan
10. Buka Detail Pengguna Revoke lewat Product Selector Global Settings
11. Verifikasi toast netral "This user is no longer available."
12. Verifikasi aktor dikembalikan ke User List
13. Verifikasi tidak ada data FAMS Pengguna Revoke yang dirender (header Detail tidak tampil)

### TC-FA-SU-62: Direct URL Detail pengguna di luar scope

14. Ganti akun: logout lalu login sebagai Manage user & role Group (Update) (Sinta Dewi)
15. Buka Settings > User dari sidebar
16. Ketik URL Detail Indra Wijaya langsung di address bar
17. Verifikasi toast error "You don't have permission to do this."
18. Verifikasi header dan tab Detail User tidak dirender dan area konten kosong
19. Verifikasi tidak ada redirect (URL tetap URL Detail Indra Wijaya)
20. Verifikasi tidak ada data Indra Wijaya yang tampil di halaman

### TC-FA-SU-64: Tab System Log dan Tab Transaction Admin Log disaring menurut scope aktor

21. Buka Settings > User dari sidebar
22. Ketik Search `Budi Santoso`, tekan Enter
23. Buka Detail Budi Santoso lalu Tab System Log
24. Verifikasi baris dengan Name Oscar Pranata dan Lina Marlina tampil
25. Verifikasi baris dengan Name Hana Kusuma dan Eka Wulandari tidak tampil
26. Buka dropdown filter Name
27. Verifikasi opsi Oscar Pranata dan Lina Marlina tampil
28. Verifikasi opsi Hana Kusuma dan Eka Wulandari tidak tampil
29. Tutup dropdown dengan menekan Esc
30. Buka dropdown filter Group
31. Verifikasi sedikitnya satu opsi Group tampil
32. Verifikasi opsi IT Infrastructure, Branch Surabaya, General Affairs, dan Logistics Warehouse tidak tampil
33. Tutup dropdown dengan menekan Esc
34. Klik icon Download pada Tab System Log lalu pilih CSV
35. Verifikasi berkas CSV terunduh
36. Verifikasi isi berkas CSV memuat baris dengan Name Oscar Pranata dan Lina Marlina
37. Verifikasi isi berkas CSV tidak memuat baris dengan Name Hana Kusuma dan Eka Wulandari
38. Buka Tab Transaction Admin Log
39. Verifikasi sedikitnya satu baris tampil
40. Verifikasi seluruh baris yang tampil memiliki Name atau Group dalam scope Finance & Accounting

### TC-FA-SU-65: Modal Combined Changelog disaring menurut scope aktor

41. Buka Settings > User dari sidebar
42. Klik icon Changelog di Table Tools User List
43. Verifikasi modal Combined Changelog memuat entri pengguna Budi Santoso
44. Verifikasi seluruh entri yang tampil milik pengguna target dalam row scope Finance & Accounting
45. Buka filter User Name
46. Verifikasi opsi Budi Santoso tampil
47. Verifikasi opsi Indra Wijaya, Eka Wulandari, Rudi Hartono, Rina Susanti, Qori Akbar, dan Doni Prasetyo tidak tampil
48. Tutup dropdown dengan menekan Esc
49. Klik Download pada modal Combined Changelog
50. Verifikasi berkas `Changelog-User` terunduh
51. Verifikasi isi berkas memuat entri pengguna Budi Santoso
52. Verifikasi isi berkas tidak memuat entri Indra Wijaya, Eka Wulandari, Rudi Hartono, Rina Susanti, Qori Akbar, dan Doni Prasetyo
53. Tutup modal Combined Changelog dengan ✕

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Spec melewati sekitar 35 langkah (53 langkah). Alasan: seluruh blok satu kelas (fungsional scope aktor ber-scope grup, hanya membaca kecuali TC-FA-SU-63), lima TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan tiap blok log membaca surface berbeda.
- Urutan TC: TC-FA-SU-63 ditaruh sebelum TC-FA-SU-62 karena aktor Total Control sudah aktif sesudah TC-FA-SU-61 (menghindari satu ganti akun tambahan); TC-FA-SU-62, 64, dan 65 memakai akun Sinta Dewi berurutan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 7 (Expand All agar node turunan terbuka), 6, 15, 21, dan 41 (membuka Settings > User), 22 (Search nama baris target sebelum Buka Detail, R-16, bagian 8b butir 13), 29, 33, dan 48 (menutup dropdown dengan Esc), 53 (menutup modal).
- Langkah 2 adalah anchor positif untuk asersi absence node langkah 4; langkah 24 untuk langkah 25; langkah 27 untuk langkah 28; langkah 31 untuk langkah 32; langkah 36 untuk langkah 37; langkah 43 dan 46 untuk langkah 47 dan 52 (bagian 8b butir 2).
- Langkah 9 memicu pelaku kedua (Principal Automation) lewat sesi API sehingga bukan konteks kedua kelas c dan tidak memakai `P-2`.
- Langkah 34 sampai 37 dan 49 sampai 52 (Download): kemampuan membaca isi berkas disediakan tim FE.
- Temuan untuk QA:
  - TC-FA-SU-61 Expected c dan TC-FA-SU-64 Expected c serta TC-FA-SU-65 Expected c menyebut Default User, Total Control, Read Only, dan Manage global user & role melihat seluruh data, tetapi langkah TC hanya memuat satu aktor kedua (Total Control pada TC-FA-SU-61) atau tidak memuat aktor kedua; asersi untuk aktor selain Total Control pada TC-FA-SU-61, dan seluruh klausa c pada TC-FA-SU-64 dan 65, tidak ditulis karena tidak ada langkahnya.
  - TC-FA-SU-61 Expected b menyebut node di luar scope "tidak tampil sehingga tidak dapat diklik" tanpa langkah klik; spec mengasersi ketiadaan node saja. TC-FA-SU-61 tidak menyebut Region Jawa dan Jakarta Selatan Distribution Center pada Expected b walau berada di luar scope Finance & Accounting; spec mengasersi empat node yang disebut TC.
  - TC-FA-SU-63 langkah 2 menyebut "Product Selector Global Settings" tanpa menyebut langkah rinci membuka Detail; spec menulisnya apa adanya. TC tidak menyebut pengguna sasaran; spec memakai pengguna Data Dinamis. Expected b "User List yang di-refresh" tidak punya cara observasi sehingga hanya "aktor dikembalikan ke User List" yang diasersi.
  - TC-FA-SU-64 dan 65: data Pre-setup #28 hanya memuat Name target Hana Kusuma, Oscar Pranata, Lina Marlina, dan Eka Wulandari; opsi Group dan baris Transaction Admin Log tidak disebut sehingga asersi Group dan Transaction Admin Log dibuat generik. Pre-setup #27 (Changelog) hanya memuat riwayat Budi Santoso, jadi entri pengguna di luar scope tidak ada; asersi absence pada langkah 47 dan 52 dapat lolos tanpa data pembanding. Usulan: tambah entri Changelog untuk pengguna di luar scope pada Pre-setup. TC-FA-SU-64 langkah 4 (Download CSV) tidak menyebut tab asal unduhan; spec mengunduh dari Tab System Log saja.
  - TC-FA-SU-64 Expected a "baris yang Name atau Group-nya berada dalam scope" tidak menyebut kolom Name/Group untuk Transaction Admin Log; asersi langkah 40 memakai Name atau Group dalam scope Finance & Accounting.
  - Email akun #6 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
