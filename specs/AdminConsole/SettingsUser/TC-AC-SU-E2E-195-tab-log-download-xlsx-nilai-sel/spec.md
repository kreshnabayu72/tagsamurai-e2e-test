---
id: TC-AC-SU-E2E-195-tab-log-download-xlsx-nilai-sel
title: "Tab Changelog, System Log, User Log, dan Responsibilities: Download XLSX dan Nilai Sel"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-401
  - TC-AC-SU-423
  - TC-AC-SU-439
  - TC-AC-SU-365
coverage:
  web: automated
---

# Tab Changelog, System Log, User Log, dan Responsibilities: Download XLSX dan Nilai Sel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-195` (email `janesmith+{runId}-195@qwertysystem.net`) dengan: Changelog sedikitnya 2 entri (Action `Assign` dan Action lain, dengan Old Value atau New Value kosong pada sedikitnya satu entri); System Log (user sebagai aktor) sedikitnya 2 entri (Object `User` dan Object lain, dengan Old Value atau New Value kosong pada sedikitnya satu entri); User Log sedikitnya 2 sesi dengan Date tanggal 02 bulan berjalan dan tanggal lain, dengan sedikitnya satu nilai kosong; Responsibilities 2 Pending Approval (satu Transaction `Device Allocation` dan satu Transaction lain, masing-masing dengan Submission Date terisi sehingga format tanggal pada berkas dapat diasersi).
- Kemampuan teknis: pembacaan isi berkas XLSX (nilai sel, format tanggal, sel kosong) oleh tim FE (binary buffer, kelas f); kemampuan seed entri Changelog, System Log, User Log, dan Pending Approval Responsibilities disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus.

## Test Steps

### TC-AC-SU-401: Download Tab Changelog sebagai XLSX dengan search atau filter aktif

1. Ketik Search `Jane Smith {runId}-195` pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `Changelog`
3. Klik icon Filter
4. Pilih `Assign` di field `Action`
5. Klik `[Apply]`
6. Klik icon Download
7. Klik `Download as XLSX`
8. Verifikasi tidak ada toast sukses
9. Verifikasi file `Changelog-Jane-Smith-{runId}-195.xlsx` terunduh
10. Verifikasi sedikitnya satu baris data pada file
11. Verifikasi setiap baris data pada file memiliki Action `Assign`
12. Verifikasi kolom Date pada file mengikuti Date Format General Settings
13. Verifikasi sel yang bernilai kosong `—` di tabel ditulis `-` pada file
14. Klik icon Filter
15. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-423: Download Tab System Log sebagai XLSX dengan search atau filter aktif

16. Klik tab `System Log`
17. Klik icon Filter
18. Pilih `User` di field `Object`
19. Klik `[Apply]`
20. Klik icon Download
21. Klik `Download as XLSX`
22. Verifikasi tidak ada toast sukses
23. Verifikasi file `System-Log-Jane-Smith-{runId}-195.xlsx` terunduh
24. Verifikasi sedikitnya satu baris data pada file
25. Verifikasi setiap baris data pada file memiliki Object `User`
26. Verifikasi kolom Date pada file mengikuti Date Format General Settings
27. Verifikasi sel yang bernilai kosong `—` di tabel ditulis `-` pada file
28. Klik icon Filter
29. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-439: Download Tab User Log sebagai XLSX dengan search atau filter aktif

30. Klik tab `User Log`
31. Klik icon Filter
32. Pilih rentang `Date` tanggal 02 sampai tanggal 02
33. Klik `[Apply]`
34. Klik icon Download
35. Klik `Download as XLSX`
36. Verifikasi tidak ada toast sukses
37. Verifikasi file `User-Log-Jane-Smith-{runId}-195.xlsx` terunduh
38. Verifikasi sedikitnya satu baris data pada file
39. Verifikasi setiap baris data pada file memiliki Date tanggal `02`
40. Verifikasi kolom Date pada file mengikuti Date Format General Settings
41. Verifikasi sel yang bernilai kosong `—` di tabel ditulis `-` pada file
42. Klik icon Filter
43. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-365: Download Tab Responsibilities sebagai XLSX dengan search atau filter aktif

44. Klik tab `Responsibilities (2)`
45. Klik icon Filter
46. Pilih `Device Allocation` di field `Transaction`
47. Klik `[Apply]`
48. Klik icon Download
49. Klik `Download as XLSX`
50. Verifikasi tidak ada toast sukses
51. Verifikasi file `Pending-Approvals-Jane-Smith-{runId}-195.xlsx` terunduh
52. Verifikasi sedikitnya satu baris data pada file
53. Verifikasi setiap baris data pada file memiliki Transaction `Device Allocation`
54. Verifikasi tanggal pada file mengikuti format General Settings
55. Klik icon Filter
56. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji. Klik tab `System Log`, `User Log`, dan `Responsibilities (2)` serta `[Clear Field]` lalu `[Apply]` setelah tiap blok adalah langkah penghubung (S-09).
- Asersi absence toast sukses diletakkan segera setelah pemicu `Download as XLSX` dan sebelum asersi berkas (bagian 8b butir 11).
- Spec ini memuat TC-401, TC-423, TC-439, dan TC-365 karena Expected-nya mengasersi nilai sel berkas XLSX (format tanggal; sel kosong ditulis `-` untuk TC-401, TC-423, TC-439), yang termasuk kelas f (binary buffer). TC-400 ada di spec 112, TC-422 di spec 119, TC-438 di spec 124, TC-364 serta nama berkas dan jumlah baris TC-365 di spec 102.
- Temuan untuk QA:
  - TC-365 menyebut nama berkas `Pending-Approvals-Jane-Smith.xlsx`; spec menulis `Pending-Approvals-Jane-Smith-{runId}-195.xlsx`.
  - Konflik TC-365 Expected b dan PRD §4.1.4: Expected b menyebut nilai kosong `—` ditulis `-`, sedangkan tabel Responsibilities pada PRD §4.1.4 hanya menyebut `—` untuk Requester pada sub-menu TAG Stock dan Client Subscription, dan kolom lain tidak pernah kosong. Pada filter `Device Allocation` tidak ada sel kosong yang dapat diasersi, sehingga spec hanya mengasersi format tanggal (Expected b bagian pertama) dan tidak mengasersi sel kosong. Keputusan owner TC diperlukan: Expected b dikoreksi atau diberi baris dengan sel kosong.
  - Nama berkas pada TC (mis. `Changelog-Jane-Smith.csv`) diturunkan dari nama user dengan spasi diganti `-`; dengan nama bersuffix, spec menulis nama berkas dengan suffix `{runId}-NNN`. Aturan penamaan berkas untuk nama yang memuat suffix tidak dinyatakan di TC.
  - TC-439 menyebut 'baris Date `02`' tanpa bulan; spec memakai rentang tanggal 02 sampai 02 bulan berjalan. Nilai Date Format General Settings tidak tertulis di TC; asersi format tanggal dibaca dari General Settings entitas Principal.
  - Expected 'nilai kosong `—` ditulis `-`' tidak menyatakan sel pada kolom mana; spec mengasersi semua sel yang bernilai `—` di tabel.
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (56 langkah nominal, sekitar 56 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-365 juga ada di `sourceTc` spec 102. Spec ini mengasersi nilai sel berkas (kelas f); spec 102 mengasersi nama berkas dan jumlah baris.
