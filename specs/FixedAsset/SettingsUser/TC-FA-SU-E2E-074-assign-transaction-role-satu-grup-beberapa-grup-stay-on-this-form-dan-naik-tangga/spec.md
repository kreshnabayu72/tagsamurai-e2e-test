---
id: TC-FA-SU-E2E-074-assign-transaction-role-satu-grup-beberapa-grup-stay-on-this-form-dan-naik-tangga
title: "Assign Transaction Role: Satu Grup, Beberapa Grup, Stay on This Form, dan Naik Tangga"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-243
  - TC-FA-SU-244
  - TC-FA-SU-245
  - TC-FA-SU-246
coverage:
  web: automated
---

# Assign Transaction Role: Satu Grup, Beberapa Grup, Stay on This Form, dan Naik Tangga

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini; Transaction Role awal Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting.
- Data uji: Transfer × Asset Admin pada Finance & Accounting (TC-FA-SU-243 dan 245); Damaged × Monitoring & Report pada Finance & Accounting dan IT Infrastructure (TC-FA-SU-244); Damaged × Asset Admin pada Finance & Accounting (TC-FA-SU-245, "data lain"); Disposal × Asset Admin pada Finance & Accounting (naik tangga dari Staff, TC-FA-SU-246).
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini ke Pre-setup #39 (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target, Tab System Log aktor, dan Activity Log sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini; dipulihkan ke Pre-setup #39 lewat seed API pada langkah penghubung dan di hook `after`. Checkbox `Stay on this form after submitting` dikembalikan tidak tercentang sebelum spec berakhir.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Mira Anggraini (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node IT Infrastructure (langkah 14) tidak Disabled oleh gate Home Group constraint; Home Group Mira Anggraini dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-243: Assign Transaction Role baru ke satu grup: toast, baris baru, dan log Assign

1. Catat jumlah entri `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog target, Tab System Log aktor, dan Activity Log sebagai baseline
2. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting, Transaction Transfer, dan Role Asset Admin
3. Klik `[Submit]`
4. Verifikasi modal tertutup
5. Verifikasi toast "Success, Asset Admin has been assigned."
6. Verifikasi tabel menampilkan baris Transfer × Asset Admin dengan badge Finance & Accounting
7. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
8. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Transfer — Finance & Accounting — Asset Admin` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline pada Tab Changelog
9. Buka Tab System Log aktor dan Search `Mira Anggraini`, tekan Enter
10. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Transfer — Finance & Accounting — Asset Admin` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline pada Tab System Log
11. Buka Activity Log
12. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Transfer — Finance & Accounting — Asset Admin` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline pada Activity Log

### TC-FA-SU-244: Assign ke beberapa grup dalam satu Save: satu toast bentuk tunggal dan satu entri log per grup

13. Catat jumlah entri `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
14. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting dan IT Infrastructure, Transaction Damaged, dan Role Monitoring & Report
15. Tunggu toast lama hilang otomatis
16. Klik `[Submit]`
17. Verifikasi toast "Success, Monitoring & Report has been assigned." tampil satu kali
18. Verifikasi tabel menampilkan satu baris Damaged × Monitoring & Report dengan dua badge grup
19. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
20. Verifikasi satu entri `Assign` per (Jenis Transaksi × Group) tercatat pada Tab Changelog (Damaged — Finance & Accounting — Monitoring & Report dan Damaged — IT Infrastructure — Monitoring & Report)
21. Verifikasi jumlah entri `Assign` baru pada Tab Changelog tepat dua dibanding baseline

### TC-FA-SU-245: Checkbox Stay on this form after submitting: Submit sukses mengosongkan form tanpa menutup modal

22. Pulihkan Transaction Role Mira Anggraini ke Pre-setup #39 lewat seed API
23. Buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role dan klik `[+ Assign]`
24. Centang `Stay on this form after submitting`
25. Isi Group Finance & Accounting, Transaction Transfer, dan Role Asset Admin lalu klik `[Submit]`
26. Verifikasi toast sukses tampil
27. Verifikasi modal tetap terbuka
28. Verifikasi Group kosong (tombol berlabel `Select Group`)
29. Verifikasi Transaction kosong
30. Verifikasi Role kosong
31. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
32. Klik `[✕]` pada modal
33. Klik `[+ Assign]` untuk membuka modal baru tanpa mencentang `Stay on this form after submitting`
34. Isi Group Finance & Accounting, Transaction Damaged, dan Role Asset Admin lalu klik `[Submit]`
35. Verifikasi modal menutup otomatis setelah sukses

### TC-FA-SU-246: Naik tangga (Staff ke Asset Admin): role lama diganti otomatis tanpa konfirmasi dan log Remove disusul Assign

36. Pulihkan Transaction Role Mira Anggraini ke Pre-setup #39 lewat seed API
37. Catat jumlah entri `Remove`, `Assign`, dan `Edit` Object `Transaction Role` Mira Anggraini pada Tab Changelog target, Tab System Log aktor, dan Activity Log sebagai baseline
38. Buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting, Transaction Disposal, dan Role Asset Admin
39. Klik `[Submit]`
40. Verifikasi tidak ada dialog konfirmasi
41. Verifikasi modal tertutup
42. Verifikasi toast "Success, Asset Admin has been assigned."
43. Verifikasi baris Disposal × Staff untuk Finance & Accounting hilang (grup berpindah)
44. Verifikasi baris Disposal × Asset Admin memuat Finance & Accounting
45. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
46. Verifikasi entri `Remove` / Object `Transaction Role` / Field `Disposal — Finance & Accounting — Staff` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline pada Tab Changelog
47. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Disposal — Finance & Accounting — Asset Admin` / Old Value `—` / New Value `Assigned` tercatat sesudah entri `Remove` pada Tab Changelog
48. Verifikasi tidak ada entri `Edit` baru dibanding baseline pada Tab Changelog
49. Buka Tab System Log aktor dan Search `Mira Anggraini`, tekan Enter
50. Verifikasi entri `Remove` / Object `Transaction Role` / Field `Disposal — Finance & Accounting — Staff` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline pada Tab System Log
51. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Disposal — Finance & Accounting — Asset Admin` / Old Value `—` / New Value `Assigned` tercatat sesudah entri `Remove` pada Tab System Log
52. Verifikasi tidak ada entri `Edit` baru dibanding baseline pada Tab System Log
53. Buka Activity Log
54. Verifikasi entri `Remove` / Object `Transaction Role` / Field `Disposal — Finance & Accounting — Staff` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline pada Activity Log
55. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Disposal — Finance & Accounting — Asset Admin` / Old Value `—` / New Value `Assigned` tercatat sesudah entri `Remove` pada Activity Log
56. Verifikasi tidak ada entri `Edit` baru dibanding baseline pada Activity Log

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 13, 15, 22, 36 dan 37. Pemulihan lewat seed API memulihkan Pre-setup #39 sebelum TC berikutnya mengandalkannya (S-09); "Tunggu toast lama hilang otomatis" mendahului hitungan toast (R-12); baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 7 sampai 12, 19 sampai 21 dan 45 sampai 56. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16). Asersi jumlah "tidak ada entri `Edit`" pada TC-FA-SU-246 memakai baseline dan anchor positif entri `Remove` dan `Assign` pada surface yang sama (bagian 3 prinsip 13 butir g, S-12).
- Jumlah langkah 56, di atas smell 35 langkah: 35 langkah di luar blok baca-log berpola (21 langkah, tidak dihitung pada smell bagian 3 prinsip 13); seluruh blok satu topik (Assign Transaction Role lewat modal yang sama pada pengguna yang sama) dan satu kelas harness, dan tiap TC berdiri sendiri karena Transaction Role Mira Anggraini dipulihkan antar TC.
- Pre-setup #50 diterapkan hanya pada Mira Anggraini (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih IT Infrastructure (langkah 14); Home Group Mira Anggraini dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - TC-FA-SU-245 mengulang kombinasi Transfer × Asset Admin yang sudah diassign TC-FA-SU-243 dan tidak menyebut pemulihannya; spec memulihkan Transaction Role Mira lewat seed API sebelum TC-FA-SU-245. TC-FA-SU-245 butir b ("modal menutup otomatis tanpa Stay") tidak menyebut pengaturan awal checkbox pada modal baru; spec membuka modal baru tanpa mencentang checkbox dan mengasumsikan modal baru dimulai tanpa centang.
  - TC-FA-SU-245 butir a menyebut "toast sukses" tanpa teks; spec hanya mengasersi toast sukses tampil.
  - TC-FA-SU-244 butir c tidak menyebut permukaan log selain Tab Changelog (langkah 5); spec mengasersi Tab Changelog saja. Post Condition TC-FA-SU-244 dan 245 serta butir Settings > Role & Permission (TC-FA-SU-243, 244, 246) tidak punya langkah observasi di TC dan tidak diasersi.
