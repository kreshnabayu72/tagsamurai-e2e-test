---
id: TC-GS-NLU-E2E-111-log-entri-per-baris-bulk-dan-format-kolom-changelog
title: "Log: entri per baris Bulk dan format kolom Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-406
  - TC-GS-NLU-407
  - TC-GS-NLU-408
  - TC-GS-NLU-506
  - TC-GS-NLU-507
coverage:
  web: automated
---

# Log: entri per baris Bulk dan format kolom Changelog

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Admin B: sesi API aktor Total Control kedua, hanya memicu penghapusan (bukan konteks kedua UI). Akun admin kedua tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login API memakai token yang tidak dihitung sebagai sesi web, dinyatakan di `suite.md` (bagian Hook suite).
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE), semua Division `Operations`, Represented By `Ahmad Fauzi`, Email `<nama>+{runId}-111@qwertysystem.net`:
  - TC-GS-NLU-406: `Bulk Aktif Satu {runId}-111` (Inactive manual), `Bulk Aktif Dua {runId}-111` (Inactive manual), `Bulk Aktif Expired {runId}-111` (Inactive, Temporary-expired).
  - TC-GS-NLU-506: `Campur Aktif {runId}-111` (Active), `Skip Penuh Satu {runId}-111` (Active), `Campur Mati {runId}-111` (Inactive), `Batas Hapus Satu {runId}-111` (Active).
  - TC-GS-NLU-507: `Bulk Convert 01 {runId}-111` (Active), `Bulk Convert 02 {runId}-111` (Active), `Batas Hapus Dua {runId}-111` (Active).
- Baseline log: jumlah entri Activity Log aktor Siti Nurhaliza per Action `Activate`, `Deactivate`, `Convert to Login User` dibaca pada langkah awal; kemampuan membaca jumlah entri disediakan tim FE/BE. Jumlah entri Tab Changelog Detail baris `Campur Mati {runId}-111` dicatat sebelum aksi sebagai baseline (S-12).
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-111` yang tersisa (termasuk Login User hasil Convert).
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

1. Buka Global Settings > Activity Log lewat sidebar dan catat jumlah entri aktor Siti Nurhaliza untuk object Non-Login User per Action `Activate`, `Deactivate`, `Convert to Login User` sebagai baseline Activity Log
2. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Campur Mati {runId}-111`, tekan Enter, klik Name baris tersebut, klik tab `Changelog`, dan catat jumlah entri sebagai baseline Changelog `Campur Mati`

### TC-GS-NLU-406: Bulk Activate menulis satu entri per baris berhasil dan tidak untuk baris skip

3. Ketik Search `{runId}-111`, tekan Enter, centang baris `Bulk Aktif Satu {runId}-111`, `Bulk Aktif Dua {runId}-111`, dan `Bulk Aktif Expired {runId}-111`
4. Pilih `Bulk Action` > `Activate`
5. Klik `[Continue]` pada dialog dua kelompok bullet
6. Tunggu aksi selesai (dialog menutup)
7. Ketik Search `Bulk Aktif Satu {runId}-111`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
8. Verifikasi Tab Changelog Detail `Bulk Aktif Satu`: satu entri `Activate` Field `Status`
9. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Bulk Aktif Dua {runId}-111`, tekan Enter, klik Name baris tersebut, lalu klik tab `Changelog`
10. Verifikasi Tab Changelog Detail `Bulk Aktif Dua`: satu entri `Activate` Field `Status`
11. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Bulk Aktif Expired {runId}-111`, tekan Enter, klik Name baris tersebut, lalu klik tab `Changelog`
12. Verifikasi kolom header tabel Tab Changelog Detail `Bulk Aktif Expired` tampil
13. Verifikasi Tab Changelog Detail `Bulk Aktif Expired` tidak memuat entri `Activate` (baris Temporary-expired di-skip)
14. Buka Global Settings > Activity Log lewat sidebar
15. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Activate` bertambah dua dibanding baseline (satu per baris berhasil; jumlah baru menjadi baseline berikutnya)

### TC-GS-NLU-506: Bulk Deactivate menulis satu entri per baris berhasil, tidak untuk baris skip atau gagal

16. Buka sub-tab Non-Login User lewat sidebar
17. Ketik Search `{runId}-111`, tekan Enter, centang baris `Campur Aktif {runId}-111`, `Skip Penuh Satu {runId}-111`, `Campur Mati {runId}-111`, dan `Batas Hapus Satu {runId}-111`
18. Pilih `Bulk Action` > `Deactivate`
19. Di sesi API Admin B (dialog sudah terbuka), hapus `Batas Hapus Satu {runId}-111` hingga penghapusan tersimpan
20. Klik `[Continue]` pada dialog dua kelompok bullet
21. Tunggu aksi selesai (dialog menutup)
22. Ketik Search `Campur Aktif {runId}-111`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
23. Verifikasi Tab Changelog Detail `Campur Aktif`: entri `Deactivate` Field `Status`, Old Value `Active`, New Value `Inactive`
24. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Skip Penuh Satu {runId}-111`, tekan Enter, klik Name baris tersebut, lalu klik tab `Changelog`
25. Verifikasi Tab Changelog Detail `Skip Penuh Satu`: entri `Deactivate` Field `Status`, Old Value `Active`, New Value `Inactive`
26. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Campur Mati {runId}-111`, tekan Enter, klik Name baris tersebut, lalu klik tab `Changelog`
27. Verifikasi kolom header tabel Tab Changelog Detail `Campur Mati` tampil
28. Verifikasi jumlah entri Tab Changelog Detail `Campur Mati` sama dengan baseline (baris skip, sudah Inactive, tidak punya entri baru)
29. Buka sub-tab Non-Login User lewat sidebar, klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka, lalu ketik Search `Batas Hapus Satu {runId}-111`, tekan Enter
30. Verifikasi Modal Changelog agregat: entri `Delete` untuk `Batas Hapus Satu {runId}-111` oleh Admin B tampil
31. Verifikasi Modal Changelog agregat: tidak ada entri `Deactivate` untuk `Batas Hapus Satu {runId}-111` (baris gagal, tidak ada di results)
32. Tutup Modal Changelog dengan `✕`, lalu buka Global Settings > Activity Log lewat sidebar
33. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Deactivate` bertambah tepat dua dibanding baseline, satu per baris berhasil (jumlah baru menjadi baseline berikutnya)

### TC-GS-NLU-507: Bulk Convert menulis satu entri per baris yang berhasil dikonversi, tidak untuk baris gagal

34. Buka sub-tab Non-Login User lewat sidebar
35. Ketik Search `{runId}-111`, tekan Enter, centang baris `Bulk Convert 01 {runId}-111`, `Bulk Convert 02 {runId}-111`, dan `Batas Hapus Dua {runId}-111`
36. Pilih `Bulk Action` > `Convert to Login User`
37. Di sesi API Admin B (dialog sudah terbuka), hapus `Batas Hapus Dua {runId}-111` hingga penghapusan tersimpan
38. Klik `[Convert]`
39. Tunggu aksi selesai (dialog menutup)
40. Buka sub-tab Login User, ketik Search `Bulk Convert 01 {runId}-111`, tekan Enter, klik Name baris tersebut untuk membuka Detail, lalu klik tab `Changelog`
41. Verifikasi Tab Changelog Detail `Bulk Convert 01`: entri `Convert to Login User` Field `User Type`, Old Value `Non Login`, New Value `Login (Pending Activation)`
42. Buka sub-tab Login User, ketik Search `Bulk Convert 02 {runId}-111`, tekan Enter, klik Name baris tersebut, lalu klik tab `Changelog`
43. Verifikasi Tab Changelog Detail `Bulk Convert 02`: entri `Convert to Login User` Field `User Type`, Old Value `Non Login`, New Value `Login (Pending Activation)`
44. Buka sub-tab Non-Login User lewat sidebar, klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka, lalu ketik Search `Batas Hapus Dua {runId}-111`, tekan Enter
45. Verifikasi Modal Changelog agregat: entri `Delete` untuk `Batas Hapus Dua {runId}-111` oleh Admin B tampil
46. Verifikasi Modal Changelog agregat: tidak ada entri `Convert to Login User` untuk `Batas Hapus Dua {runId}-111` (baris gagal, user tidak ditemukan)
47. Tutup Modal Changelog dengan `✕`, lalu buka Global Settings > Activity Log lewat sidebar
48. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Convert to Login User` bertambah tepat dua dibanding baseline, satu per baris berhasil

### TC-GS-NLU-407: Modified By di Changelog memakai format singkat dengan tooltip nama lengkap dan teks biasa

49. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Bulk Aktif Satu {runId}-111`, tekan Enter, klik Name baris tersebut, lalu klik tab `Changelog`
50. Verifikasi Tab Changelog Detail: kolom Modified By entri aksi Siti Nurhaliza berupa teks biasa (bukan badge) `Siti N`
51. Hover kolom Modified By entri aksi Siti Nurhaliza
52. Verifikasi Tab Changelog Detail: tooltip `Siti Nurhaliza` tampil
53. Tutup tooltip dengan memindahkan kursor, buka sub-tab Non-Login User lewat sidebar, lalu klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
54. Verifikasi Modal Changelog agregat: kolom Modified By entri aksi Siti Nurhaliza berupa teks biasa (bukan badge) `Siti N`
55. Hover kolom Modified By entri aksi Siti Nurhaliza
56. Verifikasi Modal Changelog agregat: tooltip `Siti Nurhaliza` tampil

### TC-GS-NLU-408: Kolom Action dan Status di Changelog berupa teks biasa bukan badge

57. Verifikasi Modal Changelog agregat: kolom Action entri `Deactivate` (dari TC-GS-NLU-506) berupa teks biasa tanpa warna badge
58. Verifikasi Modal Changelog agregat: nilai Status `Inactive` pada entri `Deactivate` berupa teks biasa tanpa warna badge
59. Tutup Modal Changelog dengan `✕`, ketik Search `Campur Aktif {runId}-111`, tekan Enter, klik Name baris tersebut, lalu klik tab `Changelog`
60. Verifikasi Tab Changelog Detail: kolom Action entri `Deactivate` berupa teks biasa tanpa warna badge
61. Verifikasi Tab Changelog Detail: nilai Status `Inactive` pada entri `Deactivate` berupa teks biasa tanpa warna badge

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 6, 21, 39 (Tunggu aksi selesai), langkah 3, 17, 35 (Search dan pemilihan baris data milik spec, R-16), serta penutupan modal, hover, dan navigasi sidebar di blok baca-log.
- Urutan TC dalam spec: TC-GS-NLU-406, 506, 507, 407, 408. TC-GS-NLU-407 dan 408 hanya membaca tampilan entri dan memakai entri yang dihasilkan TC-GS-NLU-406 dan 506 (aksi Siti Nurhaliza) di dalam spec ini, sehingga dijalankan sesudah keduanya.
- Baseline (S-12): jumlah entri Activity Log dibaca per Action dan aktor sebelum aksi pertama, lalu tiap asersi memakai selisih terhadap baseline terakhir; Changelog memakai nama record bersuffix `{runId}-111` (baseline nol).
- Di atas 35 langkah, alasan: Alasan jumlah langkah: nominal 61 langkah, dengan 47 langkah berupa blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 prinsip 13 (Smell), sehingga 14 langkah terhitung. Semua blok memeriksa tiga surface log yang sama untuk satu aksi dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-1: TC-GS-NLU-506 dan 507 memuat klausa "tidak ada entri baru" (baris skip atau gagal). Konteksnya bergantung pada state yang dibangun langkah lain di spec ini (seleksi empat atau tiga baris, lalu Admin B menghapus satu baris sebelum submit), sehingga asersi absence tetap di spec ini dengan baseline berjumlah (S-12) dan anchor positif: header kolom Tab Changelog Detail tampil, entri `Delete` oleh Admin B tampil, serta selisih jumlah entri Activity Log. Spec absence 112 tidak memuat aksi Bulk, sehingga TC-GS-NLU-506 dan 507 tidak dirujuk ke sana (S-05).
- Admin B memakai sesi API aktor (langkah 19 dan 37); bukan konteks kedua UI, sehingga tidak memakai `P-2`.
- Temuan untuk QA:
  - TC-GS-NLU-506 dan 507 tidak menyebut akun Admin B; spec menandainya "disediakan tim FE" tanpa mengarang akun.
  - TC-GS-NLU-406 tidak menyebut mekanisme baris yang di-skip sebagai tidak punya entri (selain Temporary-expired); spec memakai anchor header kolom Tab Changelog Detail dan tidak mengasersi isi lain.
  - TC-GS-NLU-407 dan 408 menyebut "Changelog" dan "record terkait" tanpa menunjuk record; spec memakai record hasil TC-GS-NLU-406 dan 506 dalam spec ini.
  - Surface Activity Log tidak dirinci jalur navigasinya di TC; spec memakai Global Settings > Activity Log dan baseline jumlah entri per Action dan aktor.
