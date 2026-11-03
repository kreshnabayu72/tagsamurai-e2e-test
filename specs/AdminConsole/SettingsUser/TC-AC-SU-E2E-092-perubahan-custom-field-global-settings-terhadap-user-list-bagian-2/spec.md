---
id: TC-AC-SU-E2E-092-perubahan-custom-field-global-settings-terhadap-user-list-bagian-2
title: "Perubahan Custom Field di Global Settings terhadap User List dan Detail User (bagian 2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-609
  - TC-AC-SU-613
  - TC-AC-SU-612
  - TC-AC-SU-611
  - TC-AC-SU-610
coverage:
  web: automated
---

# Perubahan Custom Field di Global Settings terhadap User List dan Detail User (bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Custom Field User milik spec (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-092`): `Blood Type {runId}-092` (Dropdown, Active), `Locker No {runId}-092` (Text, Active), `Shirt Size {runId}-092` (Dropdown, Active). State Custom Field User adalah state global; hook `after` menghapus ketiga field dan memulihkan Custom Field User ke keadaan awal (suite serial).
- Data Dinamis (nama bersuffix `{runId}-092`): `Mike Tan {runId}-092` (`Blood Type {runId}-092` = `O`, `Locker No {runId}-092` = `A12`), `Jane Smith {runId}-092` (`Blood Type {runId}-092` = `O`).
- Langkah di Global Settings > User > Custom Field dijalankan lewat UI Global Settings oleh aktor yang sama (akses Total Control).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-609: Custom Field di-deactivate tersembunyi dari Setup Column dan accordion, nilai kembali saat activate

1. Buka Global Settings > User > Custom Field
2. Nonaktifkan (Deactivate) `Blood Type {runId}-092`, klik konfirmasi
3. Tunggu aksi selesai
4. Buka Settings > User
5. Klik `⋯` pada header Actions, klik `[Setup Column]`
6. Verifikasi `Locker No {runId}-092` ada di Setup Column
7. Verifikasi `Blood Type {runId}-092` tidak ada di Setup Column
8. Klik icon (X) pada popup
9. Ketik Search `Mike Tan {runId}-092`, tekan Enter
10. Buka Detail `Mike Tan {runId}-092`, expand accordion Custom Field
11. Verifikasi accordion menampilkan `Locker No {runId}-092: A12`
12. Verifikasi `Blood Type {runId}-092` tidak ada di accordion
13. Buka Global Settings > User > Custom Field
14. Aktifkan (Activate) `Blood Type {runId}-092`, klik konfirmasi
15. Tunggu aksi selesai
16. Buka Settings > User, klik `⋯` pada header Actions, klik `[Setup Column]`
17. Verifikasi `Blood Type {runId}-092` muncul lagi di Setup Column
18. Klik icon (X) pada popup
19. Ketik Search `Mike Tan {runId}-092`, tekan Enter
20. Buka Detail `Mike Tan {runId}-092`, expand accordion Custom Field
21. Verifikasi accordion menampilkan `Blood Type {runId}-092: O`

### TC-AC-SU-613: Accordion Custom Field Detail User saat field di-deactivate lalu di-activate kembali

22. Buka Global Settings > User > Custom Field
23. Nonaktifkan (Deactivate) `Blood Type {runId}-092`, klik konfirmasi
24. Tunggu aksi selesai
25. Buka Settings > User
26. Ketik Search `Jane Smith {runId}-092`, tekan Enter
27. Buka Detail `Jane Smith {runId}-092`, expand accordion Custom Field
28. Verifikasi baris `Locker No {runId}-092` tampil di accordion
29. Verifikasi baris `Blood Type {runId}-092` tidak tampil di accordion
30. Buka Global Settings > User > Custom Field
31. Aktifkan (Activate) `Blood Type {runId}-092`, klik konfirmasi
32. Tunggu aksi selesai
33. Buka Settings > User
34. Ketik Search `Jane Smith {runId}-092`, tekan Enter
35. Buka Detail `Jane Smith {runId}-092`
36. Muat ulang halaman Detail dengan F5
37. Expand accordion Custom Field
38. Verifikasi baris `Blood Type {runId}-092: O` tampil kembali dengan nilai lama

### TC-AC-SU-612: Rename Custom Field tercermin pada label kolom dan accordion

39. Buka Settings > User, klik `⋯` pada header Actions, klik `[Setup Column]`
40. Centang `Blood Type {runId}-092`, klik `[Save]`
41. Buka Global Settings > User > Custom Field
42. Ubah nama `Blood Type {runId}-092` menjadi `Blood Group {runId}-092`
43. Tunggu aksi selesai
44. Buka Settings > User
45. Verifikasi header kolom `Blood Group {runId}-092`
46. Ketik Search `Mike Tan {runId}-092`, tekan Enter
47. Buka Detail `Mike Tan {runId}-092`, expand accordion Custom Field
48. Verifikasi label accordion `Blood Group {runId}-092`
49. Verifikasi nilai accordion tetap `O`

### TC-AC-SU-611: Data Type Custom Field diubah mengosongkan nilai di accordion

50. Buka Global Settings > User > Custom Field
51. Ubah Data Type `Locker No {runId}-092` menjadi Numeric, klik konfirmasi
52. Tunggu aksi selesai
53. Buka Settings > User
54. Ketik Search `Mike Tan {runId}-092`, tekan Enter
55. Buka Detail `Mike Tan {runId}-092`, expand accordion Custom Field
56. Verifikasi accordion menampilkan `Locker No {runId}-092: —`

### TC-AC-SU-610: Custom Field dihapus di Global Settings hilang permanen dari Setup Column dan accordion

57. Buka Global Settings > User > Custom Field
58. Hapus (Delete) `Shirt Size {runId}-092`, klik konfirmasi
59. Tunggu aksi selesai
60. Buka Settings > User, klik `⋯` pada header Actions, klik `[Setup Column]`
61. Verifikasi `Locker No {runId}-092` ada di Setup Column
62. Verifikasi `Shirt Size {runId}-092` tidak ada di Setup Column
63. Klik icon (X) pada popup
64. Ketik Search `Mike Tan {runId}-092`, tekan Enter
65. Buka Detail `Mike Tan {runId}-092`, expand accordion Custom Field
66. Verifikasi accordion menampilkan label `Locker No {runId}-092`
67. Verifikasi accordion tidak menampilkan `Shirt Size {runId}-092`

## Notes

- Urutan spec berbeda dari urutan TC: TC-613 sesudah TC-609 karena keduanya memakai `Blood Type {runId}-092` aktif, TC-612 (rename) sesudah keduanya, TC-611 dan TC-610 (mengubah Data Type dan menghapus) di akhir (S-10).
- Langkah penghubung (S-03): icon (X) menutup popup tanpa menyimpan; langkah Setup Column di TC-612 memenuhi precondition ("kolomnya ditampilkan"); "Ketik Search `<nama bersuffix>`, tekan Enter" mendahului tiap Buka Detail untuk menemukan baris target, termasuk Buka Detail sebelum muat ulang F5 pada TC-613 (langkah 33 sampai 37, R-16); "Tunggu aksi selesai" setelah tiap aksi konfirmasi Global Settings (Deactivate, Activate, Delete, Rename, ubah Data Type) memberi waktu aksi selesai sebelum pindah ke Settings > User (bagian 8b butir 8); tanpa `Verifikasi`.
- Tiap asersi absence (opsi Setup Column, baris accordion) didahului `Verifikasi` pembanding pada surface yang sama: `Locker No {runId}-092` yang masih ada di Setup Column dan accordion (bagian 8b butir 2).
- TC-610 `Verifikasi` section Custom Field tidak tampil bila tidak ada field lain: field `Blood Type {runId}-092` dan `Locker No {runId}-092` milik spec masih ada sehingga bagian ini tidak diasersi.
- Alasan di atas ±35 langkah: kelima TC adalah dampak Custom Field User terhadap User List dan Detail dengan dataset sama.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-092` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-609 sampai TC-613 memakai Custom Field `Blood Type`, `Shirt Size`, dan `Locker No` literal; spec memakai field milik spec bernama bersuffix (S-06, S-12).
  - TC-610 Expected (b) "section Custom Field tidak tampil bila tidak ada field lain" tidak dapat diasersi karena field lain milik spec masih ada.
