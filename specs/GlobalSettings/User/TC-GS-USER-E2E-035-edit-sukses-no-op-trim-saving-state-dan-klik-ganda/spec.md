---
id: TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda
title: "Edit User Sukses: No-Op, Trim Spasi, Happy Path Nama, Klik Ganda [Save], dan Saving State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-184
  - TC-GS-USER-185
  - TC-GS-USER-173
  - TC-GS-USER-174
  - TC-GS-USER-175
  - TC-GS-USER-192
  - TC-GS-USER-193
coverage:
  web: automated
---

# Edit User Sukses: No-Op, Trim Spasi, Happy Path Nama, Klik Ganda [Save], dan Saving State

## Prerequisites

- Mode: FE+BE, dengan intercept parsial di atas backend nyata (TC-GS-USER-192).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup yang dipakai: Position `Staff`, `Supervisor`, `Finance Manager` (No. 22), Division `Finance` (No. 23), Custom Field `Blood Type` dengan nilai `A` (No. 24), dan produk `Fixed Asset` (No. 26); hanya dibaca. Spec tidak mengubah atau menghapus data Pre-setup (Dewi Lestari No. 12 diganti user seed milik spec, S-06).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD):
  - U-1: First Name `Dewi`, Last Name `Lestari {runId}-035` (Name `Dewi Lestari {runId}-035`), Email `dewilestari+{runId}-035@qwertysystem.net`, Employee ID `EMP-{runId}-035`, Position `Staff`, Division `Finance`, Access `Fixed Asset` dan `Global Settings`, Active ON, Temporary User aktif dengan Temporary Until +30 hari dari tanggal seeding, Custom Field `Blood Type` `A`, tanpa TAG. Satu user dipakai berurutan oleh semua TC.
  - Cleanup di hook `after` (tidak berasumsi seeding atau rename berhasil penuh): hapus U-1 lewat API (nama awal `Dewi Lestari {runId}-035`, nama akhir `Dewiana Lestari Putri {runId}-035`, atau Email `dewilestari+{runId}-035@qwertysystem.net`), dan lepas intercept respons Edit bila masih terpasang.
- Jam server dan jam browser sinkron (asersi Last Update TC-GS-USER-184 dibandingkan dengan waktu aksi dengan toleransi satu menit, S-12).
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons request Edit User (TC-GS-USER-192) lalu melepasnya (nama endpoint ditentukan tim FE di tahap script); double-click; hover tombol; membaca jumlah toast yang tampil; memuat ulang halaman (F5); membaca jumlah dan isi entri Tab Changelog di Detail.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-USER-185: Edit No-Op, Save tanpa perubahan

1. Klik icon Search, ketik `Dewi Lestari {runId}-035`, tekan Enter
2. Klik Name `Dewi Lestari {runId}-035` untuk membuka Detail
3. Buka Tab Changelog
4. Catat jumlah entri Tab Changelog (baseline)
5. Kembali ke User List
6. Klik icon Search, ketik `Dewi Lestari {runId}-035`, tekan Enter
7. Buka row action baris `Dewi Lestari {runId}-035` lalu klik `Edit`
8. Klik `[Save]` tanpa mengubah apa pun
9. Verifikasi toast `No changes to save.`
10. Verifikasi tidak ada toast sukses update `Success, user has been updated.`
11. Verifikasi Popup Edit tertutup
12. Klik Name `Dewi Lestari {runId}-035` untuk membuka Detail
13. Buka Tab Changelog
14. Verifikasi Tab Changelog tidak bertambah entri: jumlah entri sama dengan baseline langkah 4
15. Kembali ke User List
16. Klik icon Search, ketik `Dewi Lestari {runId}-035`, tekan Enter

### TC-GS-USER-173, TC-GS-USER-174, dan TC-GS-USER-175: spasi awal/akhir ter-trim saat disimpan

17. Buka row action baris `Dewi Lestari {runId}-035` lalu klik `Edit`
18. Ubah First Name menjadi `  Dewi  ` (spasi di awal dan akhir)
19. Ubah Last Name menjadi `  Lestari {runId}-035  ` (spasi di awal dan akhir)
20. Ubah Employee ID menjadi `  EMP-0200-{runId}-035  ` (spasi di awal dan akhir)
21. Klik `[Save]`
22. Verifikasi toast sukses: `Success, user has been updated.`
23. Buka row action baris `Dewi Lestari {runId}-035` lalu klik `Edit`
24. Verifikasi First Name tersimpan `Dewi` tanpa spasi awal/akhir
25. Verifikasi Last Name tersimpan `Lestari {runId}-035` tanpa spasi awal/akhir
26. Verifikasi Employee ID tersimpan `EMP-0200-{runId}-035` tanpa spasi awal/akhir

### TC-GS-USER-184: Edit happy path ubah First Name dan Last Name

27. Ubah First Name `Dewi` menjadi `Dewiana`
28. Ubah Last Name `Lestari {runId}-035` menjadi `Lestari Putri {runId}-035`
29. Klik `[Save]`
30. Verifikasi Popup Edit tertutup
31. Verifikasi toast sukses: `Success, user has been updated.`
32. Catat waktu aksi (sesudah `[Save]`)
33. Verifikasi sel Name `Dewiana Lestari Putri {runId}-035`
34. Verifikasi Modified By `Siti N`
35. Verifikasi Last Update sama dengan waktu aksi yang dicatat (toleransi 1 menit)
36. Muat ulang halaman (F5)
37. Klik icon Search, ketik `Dewiana Lestari Putri {runId}-035`, tekan Enter
38. Klik Name `Dewiana Lestari Putri {runId}-035` untuk membuka Detail
39. Verifikasi Access tetap `Fixed Asset` dan `Global Settings`
40. Verifikasi switch Active tetap ON
41. Verifikasi Temporary tetap aktif dengan Temporary Until +30 hari seperti seed
42. Verifikasi TAG tetap tidak terpasang
43. Verifikasi Custom Field `Blood Type` tetap `A`
44. Kembali ke User List
45. Klik icon Search, ketik `Dewiana Lestari Putri {runId}-035`, tekan Enter

### TC-GS-USER-193: Double-click [Save] hanya satu update

46. Buka row action baris `Dewiana Lestari Putri {runId}-035` lalu klik `Edit`
47. Ubah Position ke `Supervisor`
48. Tunggu toast lama hilang otomatis
49. Double-click `[Save]`
50. Verifikasi hanya 1 toast sukses `Success, user has been updated.`
51. Klik Name `Dewiana Lestari Putri {runId}-035` untuk membuka Detail
52. Buka Tab Changelog
53. Verifikasi Tab Changelog hanya 1 baris `Edit | Position`
54. Kembali ke User List
55. Klik icon Search, ketik `Dewiana Lestari Putri {runId}-035`, tekan Enter

### TC-GS-USER-192: Tombol [Save] saving state saat request berjalan

56. Buka row action baris `Dewiana Lestari Putri {runId}-035` lalu klik `Edit`
57. Pasang intercept yang menahan respons request Edit User sampai dilepas
58. Ubah Position ke `Finance Manager`
59. Hover `[Save]`
60. Verifikasi hover state tombol `[Save]` terlihat
61. Klik `[Save]`
62. Verifikasi tombol `[Save]` dalam keadaan loading
63. Verifikasi tombol `[Save]` disabled sampai respons diterima
64. Lepas intercept respons Edit User
65. Tunggu aksi selesai

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md` (TC-GS-USER-184, 185, 173, 174, 175, 192, 193). Mode FE+BE; kelas harness: Edit sukses pada satu user seed.
- Urutan TC di spec: 185, 173/174/175, 184, 193, 192. Urutan sumber (184, 185, 173, 174, 175, 192, 193) diubah karena: TC-GS-USER-185 (No-Op) dijalankan lebih dulu agar baseline Changelog belum memuat entri Edit; TC-GS-USER-193 membutuhkan Tab Changelog dengan tepat satu baris `Edit | Position`, sehingga dijalankan sebelum TC-GS-USER-192 yang juga mengubah Position; TC-GS-USER-192 berisi intercept dan berjalan paling akhir.
- TC-GS-USER-173, 174, dan 175 (trim First Name, Last Name, Employee ID) dijalankan dalam satu Edit dan satu `[Save]` karena hanya berbeda field dan tidak menambah alur baru (bagian 2 dan bagian 3 butir 9); satu nilai khusus per field. Nilai uji Last Name dan Employee ID diberi suffix (`  Lestari {runId}-035  ` dan `  EMP-0200-{runId}-035  `) agar Name tetap unik per run dan Employee ID tidak bentrok; nilai trim yang dibandingkan memakai suffix yang sama. Nilai tersimpan dibaca dengan membuka Edit lagi (langkah 23 sampai 26), dan form yang sama dilanjutkan untuk TC-GS-USER-184 (langkah 27 sampai 29).
- Asersi jumlah Tab Changelog (TC-GS-USER-185 dan 193) memakai baseline dan hitungan baris, bukan asersi absence kelas g (bagian 3 prinsip 13, S-05).
- Langkah buka layar User List tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`). Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 7 (Search, membuka Detail, mencatat baseline, kembali), 15 dan 16, 32 (mencatat waktu aksi sesudah `[Save]`, S-12), 36 sampai 38 dan 44 sampai 45 (muat ulang, membuka Detail, kembali, search ulang; langkah 36 sampai 38 adalah "Refresh, buka Detail" TC-GS-USER-184), 48 (menunggu toast lama hilang sebelum hitungan toast, R-12), 54 dan 55, 64 dan 65 (melepas intercept dan Tunggu aksi selesai).
- Pembagian TC lintas spec: TC-GS-USER-173 sampai 175, 184, 185, 192, dan 193 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-184 Post Condition b (tampilan user di Fixed Asset > Settings > User) tidak punya langkah observasi di TC; tidak diasersi.
  - TC-GS-USER-184 butir c ("tetap seperti sebelum Edit") tidak menyebut nilai awal; spec membandingkan dengan nilai seed. Precondition TC tidak menyebut user tanpa TAG; spec memakai user seed tanpa TAG sehingga "TAG tetap" berarti tidak terpasang.
  - TC-GS-USER-193 butir b ("hanya 1 baris `Edit | Position`") tidak menyebut format baris Changelog; spec memakai teks TC.
  - TC-GS-USER-192 precondition c ("network throttle") tidak menyebut mekanisme; spec memakai intercept yang menahan respons.
  - TC-GS-USER-173 sampai 175 menyebut nilai literal tanpa suffix (`  Lestari  `, `  EMP-0200  `); spec memakai nilai bersuffix demi keunikan per run.
- Spec melewati sekitar 35 langkah (65 langkah) karena memuat satu kelas (Edit sukses pada satu layar dan satu user seed), banyak langkah adalah membuka Detail/Tab Changelog dan kembali, dan tiap blok TC berdiri sendiri dengan penjelasan di atas (kegagalan satu blok tidak membuat blok lain kehilangan makna).
