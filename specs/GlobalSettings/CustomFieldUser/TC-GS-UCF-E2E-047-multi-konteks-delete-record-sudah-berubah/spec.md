---
id: TC-GS-UCF-E2E-047-multi-konteks-delete-record-sudah-berubah
title: "Multi-Konteks Delete: Record Sudah Dihapus atau Dinonaktifkan Admin Lain di Antara Dialog dan Konfirmasi (Single dan Bulk)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-151
  - TC-GS-UCF-152
  - TC-GS-UCF-153
  - TC-GS-UCF-318
  - TC-GS-UCF-322
coverage:
  web: automated
---

# Multi-Konteks Delete: Record Sudah Dihapus atau Dinonaktifkan Admin Lain di Antara Dialog dan Konfirmasi (Single dan Bulk)

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas multi-konteks (c): dua admin pada Client A yang sama.
- Suite serial (`parallel: false`): spec ini menghapus dan menonaktifkan Custom Field milik sendiri dengan dua pelaku; tidak berjalan bersamaan dengan spec lain.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field pada Sesi A; langkah tidak mengulang pembukaan layar kecuali sesudah berpindah halaman.
- Akun Sesi A (Admin A, sesi UI): Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Akun Admin B (pelaku kedua): Total Control Client A `Nadia Pratama` (Modified By `Nadia P`) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup, fixture baru), kredensial `Spectra.env.GS_TC2_PASSWORD`. Admin B hanya memicu perubahan state (hapus atau nonaktifkan Custom Field) dan hasilnya diasersi di Sesi A, sehingga Admin B memakai sesi API (P-2); kemampuan sesi API Admin B (login dan pemanggilan hapus atau ubah status Custom Field atas nama Admin B hingga tersimpan) disediakan tim FE/BE tanpa mengarang endpoint.
- Data Pre-setup Client A (hanya dibaca): `Employee Grade` (nilai `Grade 5` pada Rahmat Hidayat) sebagai anchor pembanding di Detail User; user `Rahmat Hidayat` (`rahmatHidayat_automated_qaTeam1@qwertysystem.net`). 14 Custom Field Pre-setup dan Population di-seed idempotent oleh hook `before` (disediakan tim FE/BE).
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; fixture baru `Fixture.customFieldUser.multiDelete047`; seluruhnya Text, Active, kecuali dinyatakan lain; mekanisme seeding nilai Custom Field pada User disediakan tim FE/BE, lihat Temuan untuk QA):
  - `Bulk Part A {runId}-047`, `Bulk Part B {runId}-047`, `Bulk Part C {runId}-047` (TC-GS-UCF-151).
  - `Bulk All A {runId}-047`, `Bulk All B {runId}-047` (TC-GS-UCF-152).
  - `Bulk One {runId}-047` (TC-GS-UCF-153).
  - `Double Gone {runId}-047` (TC-GS-UCF-318).
  - `Race Del {runId}-047`: nilai User Rahmat Hidayat = `Gone` (TC-GS-UCF-322).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-047` yang masih ada dan nilai Custom Field milik spec pada Rahmat Hidayat; tutup sesi API Admin B.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: sesi API Admin B (di atas); Search tabel dan Changelog Custom Field dengan filter Action; menunggu toast sukses lama hilang otomatis (jeda pendek, ≤ 4 detik, TC-GS-UCF-489) pada langkah 13, 27, 39, dan 50. Entri Changelog bersifat permanen; asersi entri memakai nama bersuffix `{runId}-047` penuh sehingga baseline entri milik run ini adalah nol.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-UCF-151: Bulk Delete dengan satu item yang sudah dihapus admin lain memproses sisanya dengan toast sebagian

1. [Sesi A] Ketik Search `Bulk Part`, tekan Enter
2. [Sesi A] Centang `Bulk Part A {runId}-047`, `Bulk Part B {runId}-047`, dan `Bulk Part C {runId}-047`
3. [Admin B, sesi API] Hapus `Bulk Part B {runId}-047` hingga tersimpan
4. [Sesi A] Klik `Bulk Action` > `Delete`, klik `[Delete]`
5. [Sesi A] Verifikasi toast sukses: "Success, custom field has been deleted. Some items were skipped."
6. [Sesi A] Verifikasi `Bulk Part A {runId}-047` dan `Bulk Part C {runId}-047` terhapus (hilang dari tabel)
7. [Sesi A] Verifikasi `Bulk Part B {runId}-047` hilang dari tabel (dihapus admin kedua)
8. [Sesi A] Verifikasi Bulk Action Bar hilang dan seleksi di-reset
9. [Sesi A] Klik icon Changelog, pilih filter Action `Delete`, Search `Bulk Part`, tekan Enter
10. [Sesi A] Verifikasi Changelog memuat entri Delete untuk `Bulk Part A {runId}-047` dan `Bulk Part C {runId}-047` oleh `Sari D`
11. [Sesi A] Verifikasi `Bulk Part B {runId}-047` hanya memiliki satu entri Delete, oleh `Nadia P`
12. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-152: Bulk Delete dengan seluruh item sudah dihapus admin lain memberi toast netral

13. [Sesi A] Tunggu toast dari langkah 5 hilang otomatis
14. [Sesi A] Ketik Search `Bulk All`, tekan Enter
15. [Sesi A] Centang `Bulk All A {runId}-047` dan `Bulk All B {runId}-047`
16. [Admin B, sesi API] Hapus `Bulk All A {runId}-047` dan `Bulk All B {runId}-047` hingga tersimpan
17. [Sesi A] Klik `Bulk Action` > `Delete`, klik `[Delete]`
18. [Sesi A] Verifikasi toast netral: "This custom field is no longer available."
19. [Sesi A] Verifikasi tidak ada toast sukses
20. [Sesi A] Verifikasi tidak ada dialog blok
21. [Sesi A] Verifikasi `Bulk All A {runId}-047` dan `Bulk All B {runId}-047` tidak ada di tabel (list di-refresh)
22. [Sesi A] Verifikasi Bulk Action Bar hilang dan seleksi di-reset
23. [Sesi A] Klik icon Changelog, pilih filter Action `Delete`, Search `Bulk All`, tekan Enter
24. [Sesi A] Verifikasi Changelog memuat entri Delete untuk `Bulk All A {runId}-047` dan `Bulk All B {runId}-047` oleh `Nadia P`
25. [Sesi A] Verifikasi entri Delete untuk `Bulk All A {runId}-047` dan `Bulk All B {runId}-047` tidak dilakukan oleh `Sari D`
26. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-153: Bulk Delete dengan satu item yang sudah dihapus admin lain memberi toast netral

27. [Sesi A] Tunggu toast dari langkah 18 hilang otomatis
28. [Sesi A] Ketik Search `Bulk One {runId}-047`, tekan Enter
29. [Sesi A] Centang `Bulk One {runId}-047`
30. [Admin B, sesi API] Hapus `Bulk One {runId}-047` hingga tersimpan
31. [Sesi A] Klik `Bulk Action` > `Delete`
32. [Sesi A] Verifikasi dialog konfirmasi tampil dalam bentuk single (`Delete Custom Field`)
33. [Sesi A] Klik `[Delete]`
34. [Sesi A] Verifikasi toast netral: "This custom field is no longer available."
35. [Sesi A] Verifikasi tidak ada toast sukses
36. [Sesi A] Verifikasi `Bulk One {runId}-047` tidak ada di tabel (list di-refresh)
37. [Sesi A] Verifikasi Bulk Action Bar hilang dan seleksi di-reset
38. [Sesi A] Klik `(←)` pada kotak Search

### TC-GS-UCF-318: Delete single pada field yang sudah dihapus admin lain memberi toast netral tanpa entri log kedua

39. [Sesi A] Tunggu toast dari langkah 34 hilang otomatis
40. [Sesi A] Ketik Search `Double Gone {runId}-047`, tekan Enter
41. [Sesi A] Klik `⋯` pada baris `Double Gone {runId}-047`, pilih `Delete` (dialog Delete terbuka)
42. [Admin B, sesi API] Hapus `Double Gone {runId}-047` hingga tersimpan
43. [Sesi A] Klik `[Delete]`
44. [Sesi A] Verifikasi toast netral: "This custom field is no longer available."
45. [Sesi A] Verifikasi tidak ada toast sukses
46. [Sesi A] Verifikasi `Double Gone {runId}-047` tidak ada di tabel (list di-refresh)
47. [Sesi A] Klik icon Changelog, Search `Double Gone {runId}-047`, tekan Enter
48. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Delete untuk `Double Gone {runId}-047`, dilakukan oleh `Nadia P`
49. [Sesi A] Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-322: Delete berbalapan dengan Deactivate pada field yang sama

50. [Sesi A] Tunggu toast dari langkah 44 hilang otomatis
51. [Sesi A] Ketik Search `Race Del {runId}-047`, tekan Enter
52. [Sesi A] Klik `⋯` pada baris `Race Del {runId}-047`, pilih `Delete` (dialog Delete terbuka)
53. [Admin B, sesi API] Nonaktifkan `Race Del {runId}-047` hingga tersimpan
54. [Sesi A] Klik `[Delete]`
55. [Sesi A] Verifikasi toast sukses: "Success, custom field has been deleted."
56. [Sesi A] Verifikasi baris `Race Del {runId}-047` hilang dari tabel
57. [Sesi A] Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
58. [Sesi A] Verifikasi Detail User Rahmat Hidayat menampilkan `Employee Grade` dengan nilai `Grade 5`
59. [Sesi A] Verifikasi Detail User Rahmat Hidayat tidak menampilkan field `Race Del {runId}-047`
60. [Sesi A] Verifikasi Detail User Rahmat Hidayat tidak menampilkan nilai `Gone`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness: multi-konteks (prinsip 13c); penanda `[Sesi A]` dan `[Admin B, sesi API]` pada tiap langkah.
- Spec melewati sekitar 35 langkah (60 langkah). Seluruhnya satu kelas (multi-konteks delete atas record yang sudah berubah), satu pasangan aktor (Sesi A dan Admin B), dan tiap blok memakai field milik sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Jumlah langkah muncul dari satu `Verifikasi` per klausa Expected dan pembacaan Changelog serta Detail User.
- Urutan TC dalam spec: 151, 152, 153, 318, 322; seluruhnya aksi Delete sehingga tidak ada aksi non-Delete yang menunggu (prinsip 5). Tiap blok mengasersi toast yang identik dengan blok sebelumnya; karena itu langkah 13, 27, 39, 50 menunggu toast lama hilang otomatis (S-09).
- Admin B memakai sesi API (P-2, keputusan 2026-10-21): Admin B hanya memicu perubahan state dan hasilnya (toast, tabel, Changelog) diasersi di Sesi A; langkah pemicu ditulis "hingga tersimpan".
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 14, 28, 40, 51 (Search agar baris target tampil), langkah 9, 23, 47 (membuka Changelog dengan Search/filter), langkah 12, 26, 38, 49 (menutup modal atau Search), langkah 13, 27, 39, 50 (menunggu toast lama hilang), langkah 57 (membuka Detail User).
- Asersi tambahan di luar Expected TC (S-03): langkah 58 (anchor pembanding `Employee Grade` untuk asersi absence di Detail User); langkah 59 dan 60 menjalankan TC-GS-UCF-322 butir b ("Field dan nilai User terhapus"); TC tidak memberi langkah observasi Detail User, sehingga langkah 57 sampai 60 adalah langkah observasi tambahan yang dicatat di sini. Toast pada langkah 5, 18, 34, 44, dan 55 menjadi anchor untuk absence baris di langkah 7, 21, 36, 46, dan 56.
- P-1 (state berat): asersi tidak-ada-entri-log TC-GS-UCF-152 (langkah 25: entri Delete tidak dilakukan oleh `Sari D`) tetap di spec ini, bukan di spec absence 070, karena konteksnya bergantung pada state yang dibangun langkah sebelumnya: pelaku kedua (Admin B) menghapus record di antara pembukaan dialog Delete dan konfirmasi Sesi A. Sesi A memicu aksi Delete sungguhan di spec ini dengan baseline (nama bersuffix `{runId}-047`) dan anchor positif entri `Nadia P` (langkah 24); state itu tidak murah dibentuk ulang di spec 070.
- Pembagian TC lintas spec: Bulk Activate dan Deactivate dengan item sudah dihapus atau berubah (TC-GS-UCF-169, 170, 171, 477, 478, 479, 480, 319, 320) ada di spec 048.
- Temuan untuk QA:
  - TC-GS-UCF-151, 152, 153, 318, dan 322 ditandai `Manual Only — (d)` (dua sesi paralel); spec memakai sesi API Admin B sebagai pemicu dan sesi UI hanya untuk Admin A, sehingga dapat diotomasi.
  - Post Condition tanpa langkah observasi di TC tidak diasersi: TC-GS-UCF-151 ("Bulk Part A, B, C terhapus"). TC-GS-UCF-322 Expected b ("nilai User terhapus") tidak punya langkah observasi di TC; spec menambah langkah 57 sampai 60.
  - TC-GS-UCF-152 butir c ("List di-refresh") dan TC-GS-UCF-151 butir c tidak punya observasi terpisah; spec mengamati lewat hilangnya baris dari tabel.
  - TC-GS-UCF-153 tidak memuat langkah Changelog; spec tidak mengasersi entri log untuk TC itu.
  - TC-GS-UCF-151 sampai 322 memakai nama field tanpa suffix; spec memakai versi bersuffix `{runId}-047`. Mekanisme seeding nilai Custom Field pada User (`Gone`) tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan tim FE/BE.
  - TC-GS-UCF-322 tidak merinci entri Changelog untuk Deactivate admin kedua; tidak diasersi.
