---
id: TC-GS-USER-E2E-143-pencatatan-handheld-assign-unassign-check-out-check-in
title: "Pencatatan Assign Handheld, Check Out Handheld, Check In Handheld, dan Unassign Handheld di Changelog, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-888
  - TC-GS-USER-889
  - TC-GS-USER-890
  - TC-GS-USER-891
coverage:
  web: automated
---

# Pencatatan Assign Handheld, Check Out Handheld, Check In Handheld, dan Unassign Handheld di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE (kelas harness d: perangkat Handheld Reader dan modul Hardware).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Siti Nurhaliza (No. 2) sebagai pelaku dan pemilik Tab System Log; Division `Finance` (No. 23). Data target Pre-setup No. 10 sampai 21 tidak dipakai sebagai target aksi dan tidak diubah (S-06).
- Data Dinamis (suffix `{runId}-143`; di-seed lewat API di hook `before`; HK8 dan HK1):
  - `John Doe {runId}-143` (Email `johndoe+{runId}-143@qwertysystem.net`): Activated, Active, Division `Finance`, Access `Fixed Asset`, menggantikan John Doe No. 18. Dipakai berurutan pada TC-GS-USER-888, 890, 891, dan 889; baris log dibedakan lewat Action.
  - Handheld `Scanner 1 {runId}-143` di Hardware > Handheld: belum ter-assign pada awal spec (menggantikan Handheld `Scanner 1` pada TC).
- Kemampuan teknis (HK8, disediakan tim FE/BE; endpoint dan UI Hardware > Handheld tidak disebut di TC, PRD, dan LLD yang dirujuk spec ini): seeding Handheld Reader dan keadaan awal ter-assign lewat API; aksi Assign, Check Out, Check In, dan Unassign Handheld di Hardware > Handheld dengan akun Total Control (termasuk simulasi Check Out dan Check In "oleh" user target).
- State global yang diubah: status Handheld `Scanner 1 {runId}-143` (ter-assign, Check Out, Check In, lalu Unassign) dipulihkan oleh TC-GS-USER-889 dan oleh cleanup. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): lepas assign Handheld `Scanner 1 {runId}-143` dari `John Doe {runId}-143` bila masih ter-assign, lalu hapus Handheld dan user seed lewat API. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-888: Log Assign Handheld field Handheld

2. Buka Hardware > Handheld, klik icon Search, ketik `Scanner 1 {runId}-143`, tekan Enter
3. Assign Handheld `Scanner 1 {runId}-143` ke `John Doe {runId}-143` di Hardware > Handheld
4. Tunggu aksi selesai (Handheld `Scanner 1 {runId}-143` tercatat ter-assign ke `John Doe {runId}-143`)
5. Buka Modal Changelog User, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
6. Verifikasi Modal Changelog User: baris dengan Action `Assign Handheld`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `—`, New Value `Scanner 1 {runId}-143`, Modified By `Siti N`
7. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Assign Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
8. Buka Detail `John Doe {runId}-143` > Tab `Changelog`
9. Verifikasi Tab Changelog Detail `John Doe {runId}-143`: baris dengan Action `Assign Handheld`, Field `Handheld`, Old Value `—`, New Value `Scanner 1 {runId}-143`, Modified By `Siti N`
10. Verifikasi Tab Changelog Detail `John Doe {runId}-143`: tepat 1 baris dengan Action `Assign Handheld` (tidak duplikat)
11. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
12. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Assign Handheld`, Object `User`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `—`, New Value `Scanner 1 {runId}-143`
13. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Assign Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
14. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
15. Verifikasi Activity Log: baris dengan Action `Assign Handheld`, Object `User`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `—`, New Value `Scanner 1 {runId}-143`, Modified By `Siti N`
16. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Assign Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
17. Verifikasi Activity Log: baris `Assign Handheld` untuk `John Doe {runId}-143` berasal dari aksi di modul Hardware (Hardware > Handheld) dan tercatat di surface Global Settings

### TC-GS-USER-890: Log Check Out Handheld field Handheld

18. Buka Hardware > Handheld, klik icon Search, ketik `Scanner 1 {runId}-143`, tekan Enter
19. Check Out Handheld `Scanner 1 {runId}-143` oleh `John Doe {runId}-143`
20. Tunggu aksi selesai (status Handheld `Scanner 1 {runId}-143` menjadi Check Out)
21. Buka Modal Changelog User, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
22. Verifikasi Modal Changelog User: baris dengan Action `Check Out Handheld`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `—`, New Value `Scanner 1 {runId}-143`, Modified By `Siti N`
23. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Check Out Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
24. Buka Detail `John Doe {runId}-143` > Tab `Changelog`
25. Verifikasi Tab Changelog Detail `John Doe {runId}-143`: baris dengan Action `Check Out Handheld`, Field `Handheld`, Old Value `—`, New Value `Scanner 1 {runId}-143`, Modified By `Siti N`
26. Verifikasi Tab Changelog Detail `John Doe {runId}-143`: tepat 1 baris dengan Action `Check Out Handheld` (tidak duplikat)
27. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
28. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Check Out Handheld`, Object `User`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `—`, New Value `Scanner 1 {runId}-143`
29. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Check Out Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
30. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
31. Verifikasi Activity Log: baris dengan Action `Check Out Handheld`, Object `User`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `—`, New Value `Scanner 1 {runId}-143`, Modified By `Siti N`
32. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Check Out Handheld` untuk `John Doe {runId}-143` (tidak duplikat)

### TC-GS-USER-891: Log Check In Handheld field Handheld

33. Buka Hardware > Handheld, klik icon Search, ketik `Scanner 1 {runId}-143`, tekan Enter
34. Check In Handheld `Scanner 1 {runId}-143` oleh `John Doe {runId}-143`
35. Tunggu aksi selesai (status Handheld `Scanner 1 {runId}-143` kembali Check In)
36. Buka Modal Changelog User, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
37. Verifikasi Modal Changelog User: baris dengan Action `Check In Handheld`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `Scanner 1 {runId}-143`, New Value `—`, Modified By `Siti N`
38. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Check In Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
39. Buka Detail `John Doe {runId}-143` > Tab `Changelog`
40. Verifikasi Tab Changelog Detail `John Doe {runId}-143`: baris dengan Action `Check In Handheld`, Field `Handheld`, Old Value `Scanner 1 {runId}-143`, New Value `—`, Modified By `Siti N`
41. Verifikasi Tab Changelog Detail `John Doe {runId}-143`: tepat 1 baris dengan Action `Check In Handheld` (tidak duplikat)
42. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
43. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Check In Handheld`, Object `User`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `Scanner 1 {runId}-143`, New Value `—`
44. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Check In Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
45. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
46. Verifikasi Activity Log: baris dengan Action `Check In Handheld`, Object `User`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `Scanner 1 {runId}-143`, New Value `—`, Modified By `Siti N`
47. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Check In Handheld` untuk `John Doe {runId}-143` (tidak duplikat)

### TC-GS-USER-889: Log Unassign Handheld field Handheld

48. Buka Hardware > Handheld, klik icon Search, ketik `Scanner 1 {runId}-143`, tekan Enter
49. Unassign Handheld `Scanner 1 {runId}-143` dari `John Doe {runId}-143` di Hardware > Handheld
50. Tunggu aksi selesai (Handheld `Scanner 1 {runId}-143` tidak lagi ter-assign)
51. Buka Modal Changelog User, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
52. Verifikasi Modal Changelog User: baris dengan Action `Unassign Handheld`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `Scanner 1 {runId}-143`, New Value `—`, Modified By `Siti N`
53. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Unassign Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
54. Buka Detail `John Doe {runId}-143` > Tab `Changelog`
55. Verifikasi Tab Changelog Detail `John Doe {runId}-143`: baris dengan Action `Unassign Handheld`, Field `Handheld`, Old Value `Scanner 1 {runId}-143`, New Value `—`, Modified By `Siti N`
56. Verifikasi Tab Changelog Detail `John Doe {runId}-143`: tepat 1 baris dengan Action `Unassign Handheld` (tidak duplikat)
57. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
58. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Unassign Handheld`, Object `User`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `Scanner 1 {runId}-143`, New Value `—`
59. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Unassign Handheld` untuk `John Doe {runId}-143` (tidak duplikat)
60. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe {runId}-143`, tekan Enter
61. Verifikasi Activity Log: baris dengan Action `Unassign Handheld`, Object `User`, Name `John Doe {runId}-143`, Field `Handheld`, Old Value `Scanner 1 {runId}-143`, New Value `—`, Modified By `Siti N`
62. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Unassign Handheld` untuk `John Doe {runId}-143` (tidak duplikat)

## Notes

- Mode: FE+BE (kelas harness d). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Baris log dikenali lewat nama bersuffix `{runId}-143` yang unik per run, Action, dan Field, bukan posisi teratas dan bukan penanda waktu (S-12). Seluruh TC memakai satu user dan satu Handheld seed yang belum ter-assign pada awal spec, sehingga tiap Action (`Assign Handheld`, `Check Out Handheld`, `Check In Handheld`, `Unassign Handheld`) baru muncul pada TC yang memicunya.
- Surface disebut satu per satu pada tiap TC: Modal Changelog User, Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. Expected "Tepat 1 baris per surface (tidak duplikat)" diasersi sebagai jumlah baris dengan Action dan nama yang sama sesudah `Verifikasi` isi baris pada surface yang sama.
- Urutan TC di spec: 888, 890, 891, 889. Check Out (890) dan Check In (891) membutuhkan Handheld yang sudah ter-assign dan keluar-masuk berurutan, sehingga Unassign (889), yang melepas Handheld, berada paling akhir (bagian 3 prinsip 5). Check In mengikuti Check Out pada Handheld yang sama.
- Pembagian TC lintas spec: seluruh TC di spec ini memverifikasi pencatatan yang berhasil; tidak ada asersi absence kelas g.
- Spec melewati sekitar 35 langkah (62 langkah). Alasan: seluruh blok satu kelas harness (pencatatan log dengan Handheld) dan satu dataset seed milik spec; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) mendominasi jumlah langkah dan tidak dihitung ke batas ukuran (bagian 3 konvensi); blok berurutan pada Handheld yang sama karena Check Out, Check In, dan Unassign hanya bermakna setelah Assign.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 5, 8, 11, 14, 18 sampai 21, 24, 27, 30, 33 sampai 36, 39, 42, 45, 48 sampai 51, 54, 57, 60. Frasa "Buka ..." pada langkah baca-log mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau menu Activity Log), menutup Modal Changelog User dengan `✕`, dan, untuk Detail, Search nama pada User List lalu klik Name. Pembukaan Detail `Siti Nurhaliza` mengikuti pola yang sama. Search Handheld di Hardware > Handheld adalah bagian dari langkah aksi yang sama.
- Temuan untuk QA:
  - TC-GS-USER-888 sampai 891: Langkah Uji tidak menjelaskan UI Hardware > Handheld (label aksi Assign, Unassign, Check Out, Check In dan dialog bila ada); spec menulis aksi apa adanya. Seeding Handheld dan keadaan awal tidak punya sumber di TC, PRD, dan LLD; disediakan tim FE/BE.
  - TC-GS-USER-889: Langkah Uji tidak menyebut lokasi aksi Unassign; spec memakai Hardware > Handheld seperti TC-GS-USER-888.
  - TC-GS-USER-890 dan 891: "Check Out/In Handheld `Scanner 1` oleh John Doe" tidak menjelaskan siapa yang melakukan aksi (admin di Hardware atau John Doe di perangkat), padahal Modified By `Siti N`; spec menganggap aksi dilakukan akun aktor Total Control di Hardware > Handheld atas nama John Doe.
  - TC-GS-USER-888 Expected f ("Dicatat dari modul Hardware") diasersi sebagai kesimpulan pada Activity Log; modul sumber aksi ditentukan oleh langkah aksi di Hardware > Handheld.
  - TC-GS-USER-888 sampai 891 memakai John Doe Pre-setup (No. 18) sebagai target tulis; spec memakai padanan seed bersuffix (S-06).
