---
id: TC-FA-RP-E2E-280-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-3
title: "State tenant: Client Suspended dan Expired menolak aksi tulis (3/3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-984
  - TC-FA-RP-985
  - TC-FA-RP-986
  - TC-FA-RP-987
  - TC-FA-RP-988
  - TC-FA-RP-989
coverage:
  web: automated
---

# State tenant: Client Suspended dan Expired menolak aksi tulis (3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1: Total Control pada `Client Expired` (Pre-setup #26), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_EXPIRED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor 2: Total Control pada `Client Suspended` (Pre-setup #25), akun disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_SUSPENDED_TC_PASSWORD`. Dipakai sesudah ganti akun (langkah 17). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Env var yang dipakai: `FA_EXPIRED_TC_PASSWORD`, `FA_SUSPENDED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: #26 (`Client Expired`), #25 (`Client Suspended`), #15 (Citra Lestari, Dimas Pranata), #18, #19 (Require Approval Off di semua node), dan #39 (Detail Role `Manage accounting` dan `Manage Open API` terisi; Citra Lestari dengan Create tercentang; Dimas Pranata dan Citra Lestari pada `Manage Open API`). Disiapkan lewat seeding di hook `before`.
- Kemampuan teknis: pengaktifan kembali entitas `Client Suspended` lewat Admin Console pada TC-FA-RP-989 (disediakan tim FE; akun pelaku tidak tertulis di TC, lihat Temuan untuk QA) dan pengunduhan berkas CSV pada TC-FA-RP-987. Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): status tingkat akses, baris peran, nilai Require Approval, dan aturan persetujuan dibaca untuk Expected "tidak ada perubahan data" atau nilai akhir.
- State global: spec mengubah status `Client Suspended` menjadi aktif pada TC-FA-RP-989 (langkah 42). Hook `after` mengembalikan status `Client Suspended` (Suspended) dan menghapus penugasan Total Control Dimas Pranata hasil TC-FA-RP-989; pemulihan dijamin fixture backend yang disediakan tim FE/BE. Status `Client Expired` tidak diubah.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-984: Client Expired menolak Assign Total Control dengan toast baku yang sama

1. Klik `[+ Assign]` di Tab Total Control
2. Centang Dimas Pranata
3. Klik `[Assign]`
4. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.` (satu copy untuk Suspended dan Expired)
5. Verifikasi lewat kemampuan baca Dimas Pranata tidak berstatus Total Control (tidak ada perubahan data)
6. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-985: Client Expired menolak Edit CRUD dengan toast baku yang sama

7. Tunggu toast lama hilang otomatis
8. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
9. Hapus centang Create pada baris Citra Lestari
10. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.` (satu copy untuk Suspended dan Expired)
11. Verifikasi lewat kemampuan baca Create baris Citra Lestari tetap aktif (tidak ada perubahan data)

### TC-FA-RP-986: Client Expired menolak Toggle Require Approval dengan toast baku yang sama

12. Tunggu toast lama hilang otomatis
13. Klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
14. Aktifkan toggle
15. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.` (satu copy untuk Suspended dan Expired)
16. Verifikasi lewat kemampuan baca Require Approval `Disposal` pada `IT Infrastructure` tetap Off (tidak ada perubahan data)

### TC-FA-RP-987: Client Suspended, akses baca tetap terbuka penuh

17. Ganti akun: logout, lalu login sebagai Total Control pada `Client Suspended` dengan `Spectra.env.FA_SUSPENDED_TC_PASSWORD`
18. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab `Total Control`
19. Verifikasi tabel Tab Total Control termuat dengan sedikitnya satu baris
20. Klik Tab `Read Only`
21. Verifikasi tabel Tab Read Only termuat dengan sedikitnya satu baris
22. Klik Tab `Group Manager`
23. Verifikasi tabel Tab Group Manager termuat dengan sedikitnya satu baris
24. Klik Tab `Transaction Role`, klik node `IT Infrastructure`
25. Verifikasi tabel Role Transaksi pada node `IT Infrastructure` termuat dengan sedikitnya satu baris
26. Klik Tab `System`
27. Verifikasi tabel Tab System termuat dengan sedikitnya satu baris
28. Klik Role Name `Manage Open API` pada section Global Role
29. Verifikasi Detail Role `Manage Open API` termuat dengan sedikitnya satu baris
30. Klik ikon Changelog di toolbar Detail Role
31. Verifikasi modal Changelog tampil dan memuat sedikitnya satu entri tanpa penolakan
32. Klik ikon Download lalu `Download as CSV`
33. Verifikasi berkas CSV terunduh tanpa penolakan dan tanpa toast error
34. Tutup modal Changelog

### TC-FA-RP-988: Client Suspended menolak seluruh permintaan Bulk Remove

35. Tunggu toast lama hilang otomatis
36. Centang baris Dimas Pranata dan Citra Lestari
37. Klik `Bulk Action` > `Remove`
38. Klik `[Remove]`
39. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
40. Verifikasi lewat kemampuan baca tidak ada satu baris pun terhapus: baris Dimas Pranata dan Citra Lestari tetap ada pada `Manage Open API`
41. Klik `[Cancel]` pada dialog Bulk Remove

### TC-FA-RP-989: Client yang aktif kembali memulihkan akses tulis tanpa reaktivasi manual

42. Aktifkan kembali entitas `Client Suspended` lewat Admin Console (kemampuan disediakan tim FE)
43. Klik Tab `Total Control`
44. Klik `[+ Assign]` di Tab Total Control, centang Dimas Pranata
45. Klik `[Assign]`
46. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-984 sampai TC-FA-RP-989).
- Urutan TC: blok `Client Expired` (TC-FA-RP-984 sampai 986) lebih dulu karena akun Expired login di hook `before`, lalu satu kali ganti akun ke `Client Suspended`; TC-FA-RP-989 terakhir karena mengaktifkan kembali entitas (aksi yang mengubah state tenant dijalankan di akhir, S-10). Perubahan urutan terhadap nomor TC itu disengaja.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): "Tunggu toast lama hilang otomatis" sebelum tiap toast baku yang sama diasersi lagi (R-12); membuka tab, Detail Role, node, dan sub-tab; menutup popup atau dialog dengan `[Cancel]` (langkah 6 dan 41) agar state tidak dibawa ke TC berikutnya (S-09); menutup modal Changelog; klik Tab `Total Control` sebelum Assign.
- TC-FA-RP-987 menulis "Buka tiap tab" dan "Seluruh data tampil"; spec memetakannya ke satu `Verifikasi` tabel termuat per tab dan Detail Role, ditambah Changelog dan Download.
- Pembagian TC lintas spec: TC-FA-RP-984 sampai TC-FA-RP-989 tidak memuat klausa "tidak ada entri log" pada Expected; asersi absence log untuk aksi ditolak state tenant ada di spec 293 dan 294 (TC-FA-RP-973 sampai TC-FA-RP-982).
- Spec melewati sekitar 35 langkah (46 langkah). Semua blok satu kelas harness (state tenant Expired dan Suspended) dengan satu kali ganti akun; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-RP-987 sendiri membuka enam permukaan baca secara berurutan sehingga langkahnya tidak dapat dikurangi tanpa melewatkan Expected.
- Temuan untuk QA:
  - Akun Total Control pada `Client Suspended` (dan `Client Expired` serta Read Only pada `Client Suspended` bila dipakai) tidak tertulis di Pre-setup #1 sampai #11; email dan password disediakan tim FE (S-11).
  - Expected "tidak ada perubahan data" tidak menyebut cara memeriksanya; spec memakai kemampuan baca state lewat fixture BE (bukan langkah observasi UI).
  - TC tidak menyebut apakah popup atau dialog tetap terbuka setelah penolakan; spec mengikuti pola penolakan lain di TC (popup atau dialog tetap terbuka dengan seleksi dipertahankan) dan menutupnya dengan `[Cancel]`.
  - TC-FA-RP-989 menyebut "Aktifkan kembali entitas lewat Admin Console" tanpa akun pelaku, langkah di Admin Console, atau cara menyegarkan sesi FA sesudahnya; spec menulisnya sebagai kemampuan yang disediakan tim FE dan langsung menuju Assign. TC juga tidak menyebut pemulihan status Suspended sesudahnya; spec memulihkannya di hook `after`.
  - TC-FA-RP-987 memasangkan "Changelog dan Download berfungsi tanpa penolakan" tanpa unduhan spesifik; spec mengunduh CSV dari Detail Role `Manage Open API`.
