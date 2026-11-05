---
id: TC-FA-SU-E2E-391-remove-baris-grup-pola-group-manager-dari-popup-dan-perubahan-non-pola-tanpa-auto-revert
title: "Remove Baris Grup Pola Group Manager dari Popup (Dialog D-05c) dan Perubahan Non-Pola Tanpa Auto-Revert"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1083
  - TC-FA-SU-1084
coverage:
  web: automated
---

# Remove Baris Grup Pola Group Manager dari Popup (Dialog D-05c) dan Perubahan Non-Pola Tanpa Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager (Pre-setup #48). Hanya untuk TC-FA-SU-1084 (menambah Branch Surabaya pada Manage files): Putri Anggraeni ber-Home Group Finance & Accounting (Pre-setup #43/#48), sehingga Branch Surabaya di luar constraint dan Disabled di pemilih Group (tooltip S-45); sesuai Catatan TC (Home Group constraint FI-32), target tanpa Home Group memakai seed `FaUserNoHG` (Pre-setup #50), diterapkan per target: hanya Home Group Putri Anggraeni yang dikosongkan lewat seed API pada langkah 28; penugasan lain tidak berubah. Seed `FaUserNoHG` wajib disediakan tim FE/BE sebelum eksekusi. TC-FA-SU-1083 tetap pada Pre-setup #48 apa adanya.
- Pengguna target: Putri Anggraeni, Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update) (Pre-setup #48).
- Data uji: TC-FA-SU-1083 menghapus grup Accounts Payable dari Manage files; TC-FA-SU-1084 menambah Branch Surabaya (di luar subtree) pada Manage files, menghapus centang Delete pada Branch Surabaya, lalu menghapus baris Manage user & role × Finance & Accounting.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48 dan mengosongkan Home Group Putri Anggraeni (Pre-setup #50 per target) pada langkah 28; pembacaan jumlah entri Tab Changelog Putri Anggraeni sebelum aksi sebagai baseline (bagian 8b butir 10), termasuk saat popup masih terbuka (langkah 18 sampai 19). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager, baris pola, penugasan non-pola, dan Home Group (dikosongkan pada langkah 28) Putri Anggraeni; dipulihkan ke Pre-setup #48 (termasuk Home Group Finance & Accounting) lewat seed API pada langkah penghubung (langkah 28 dan 57) dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1083: Remove baris grup pola Group Manager dari popup: dialog D-05c varian pemicu Remove, Cancel mempertahankan popup, dan konfirmasi melepas GM

1. Ketik Search `Putri Anggraeni`, tekan Enter
2. Catat jumlah entri Tab Changelog Putri Anggraeni sebagai baseline
3. Klik Name `Putri Anggraeni`
4. Klik Tab Role lalu Sub-tab Group Role
5. Klik `[Assign Group]` pada baris Manage files
6. Klik ikon hapus pada baris Accounts Payable
7. Klik `[Save]`
8. Verifikasi dialog Title `Remove Group Manager` tampil sebelum penyimpanan
9. Verifikasi Body `These users will lose Group Manager access:`
10. Verifikasi Body bullet `• Putri Anggraeni`
11. Verifikasi penutup `Are you sure you want to remove it?`
12. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` tampil
13. Verifikasi dialog Remove Group Role biasa tidak tampil
14. Klik `[Cancel]`
15. Verifikasi dialog tertutup dan popup Assign Group Role Manage files tampil kembali
16. Verifikasi baris Accounts Payable tetap terhapus secara lokal di popup
17. Verifikasi tidak ada toast
18. Baca jumlah entri Tab Changelog Putri Anggraeni lewat kemampuan baca BE
19. Verifikasi jumlah entri Tab Changelog Putri Anggraeni sama dengan baseline (tidak ada entri log)
20. Klik `[Save]`
21. Klik `[Remove]` pada dialog `Remove Group Manager`
22. Verifikasi toast "Success, permissions have been updated. Putri Anggraeni is no longer Group Manager for Finance & Accounting." (T-06b)
23. Verifikasi status Group Manager terlepas (banner Group Manager hilang di Sub-tab Group Role)
24. Verifikasi baris Accounts Payable pada Manage files terhapus oleh aksi aktor sendiri
25. Verifikasi seluruh baris pola Group Manager lain pada Finance & Accounting dan Accounts Payable di Sub-tab Group Role (Group Role katalog selain Manage user & role) tetap tersimpan sebagai baris biasa
26. Klik Sub-tab Transaction Role
27. Verifikasi seluruh baris pola Transaction Role Asset Admin dan Approver pada seluruh Jenis Transaksi di Finance & Accounting dan Accounts Payable tetap tersimpan sebagai baris biasa
28. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API, lalu kosongkan Home Group Putri Anggraeni (varian Pre-setup #50 per target)

### TC-FA-SU-1084: Perubahan non-pola pada target Group Manager tidak memicu Auto-Revert: Assign Group di luar subtree, edit baris di luar subtree, dan penghapusan baris Manage user & role

29. Catat jumlah entri `Auto-Revert` pada Tab Changelog Putri Anggraeni dan jumlah entri `Remove (via Group Manager)` pada modal Changelog Group Role sebagai baseline
30. Buka Settings > User lewat sidebar
31. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
32. Klik Tab Role, klik Sub-tab Group Role, lalu klik `[Assign Group]` pada baris Manage files
33. Klik `[+ Assign Group]`
34. Centang Branch Surabaya lalu klik `[Select]`
35. Klik `[Save]`
36. Verifikasi toast "Success, group role has been assigned."
37. Verifikasi dialog Auto-Revert tidak tampil
38. Verifikasi Branch Surabaya pada Manage files bukan baris pola (tidak terkunci)
39. Buka ulang popup Assign Group Role Manage files
40. Hapus centang Delete pada Branch Surabaya
41. Klik `[Save]`
42. Verifikasi toast "Success, group role has been updated."
43. Verifikasi dialog Auto-Revert tidak tampil
44. Tunggu toast lama hilang otomatis
45. Buka popup Assign Group Role Manage user & role
46. Verifikasi ikon hapus pada baris Finance & Accounting Manage user & role tidak terkunci
47. Klik ikon hapus pada Finance & Accounting
48. Klik `[Save]`
49. Verifikasi toast "Success, group role has been updated."
50. Verifikasi dialog Auto-Revert tidak tampil
51. Verifikasi banner Group Manager tetap tampil
52. Verifikasi seluruh baris pola Group Manager pada Finance & Accounting dan Accounts Payable tidak berubah
53. Buka Tab Changelog, ketik Search `Putri Anggraeni`, tekan Enter, lalu muat ulang sampai entri tampil
54. Verifikasi tidak ada entri `Auto-Revert` baru dibanding baseline pada Tab Changelog Putri Anggraeni
55. Buka Sub-tab Group Role lalu klik Changelog icon
56. Verifikasi modal Group Role tidak memuat entri `Remove (via Group Manager)` baru dibanding baseline
57. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 18, 26, 28, 29, 30, 31, 44, 53, 55 dan 57. Search `Putri Anggraeni` pada langkah 1, 31 dan 53 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09). Langkah 44 menjaga toast identik langkah 42 dan 49 tidak tertukar (R-12).
- Alasan di atas sekitar 35 langkah: seluruh TC satu topik (aksi popup Assign Group Role pada target Group Manager Putri Anggraeni dengan aktor Default User yang sama), tiap TC mengubah state sendiri dan dipulihkan (langkah 28 dan 57) sebelum TC berikutnya bergantung padanya, dan kegagalan satu TC tidak membuat TC lain kehilangan makna; langkah banyak karena Expected bermajemuk (dialog D-05c enam klausa, toast, banner, baris pola di dua sub-tab) yang wajib satu `Verifikasi` per klausa (S-01).
- Langkah pola baca-log: langkah 53 sampai 56.
- Absence pada langkah 17 dan 19 (TC-FA-SU-1083 butir b: tidak ada toast, tidak ada entri log) serta langkah 54 dan 56 (TC-FA-SU-1084 butir d: tidak ada entri `Auto-Revert` dan `Remove (via Group Manager)`) ditulis sebagai `Verifikasi` berbaseline di spec ini dengan butir `P-1` (S-05): asersinya melekat pada state berat Group Manager Putri (Pre-setup #48) dan aksi tulis milik TC itu sendiri. Anchor positifnya adalah dialog yang sempat tampil (langkah 8) dan toast sukses (langkah 36, 42, 49). Spec absence tidak memuat aksi nyata untuk kedua TC ini.
- Langkah 18 membaca log lewat kemampuan baca BE karena Tab Changelog tidak dapat dibuka tanpa meninggalkan popup yang sedang dirty.
- Temuan untuk QA:
  - TC-FA-SU-1084 Precondition tidak menyebut Pre-setup #50 sedangkan Putri Anggraeni ber-Home Group, sehingga Branch Surabaya akan Disabled (S-45) dan penugasan ditolak 422 V-09; spec mengikuti Catatan TC (Home Group constraint FI-32) dan memakai seed `FaUserNoHG` (Pre-setup #50) per target, bukan seluruh 25 pengguna. Mohon dikonfirmasi bila #50 harus diterapkan penuh atau Precondition TC diperbarui.
  - Tombol `[Remove]` pada dialog D-05c varian pemicu Remove ditandai "copy usulan, perlu persetujuan PM" (`settings-role-permission` Open Item #7d), sedangkan label tombol pada TC lain di modul yang sama memakai `[Revoke]` (D-10/D-05); spec memakai `[Remove]` apa adanya dari TC. Mohon dikonfirmasi.
  - TC-FA-SU-1083 Expected butir b menyebut "tidak ada request simpan" tanpa langkah observasi request; spec mengasersi toast tidak ada dan jumlah entri log sama dengan baseline, bukan request.
  - TC-FA-SU-1083 Expected butir c menyebut baris pola GM lain tetap tersimpan "(Group Role katalog selain Manage user & role dan Transaction Role Asset Admin serta Approver seluruh Jenis Transaksi)" tanpa baris pembanding; spec mengasersi keberadaannya pada Sub-tab Group Role dan Transaction Role, dan baris Accounts Payable pada Manage files terhapus oleh aksi aktor sendiri.
  - TC-FA-SU-1083 Post Condition butir b (entri `Auto-Revert` pada tiga surface log dan notifikasi in-app ke Putri Anggraeni) tidak punya langkah observasi dan tidak diasersi.
  - TC-FA-SU-1084 Expected butir a ("grup di luar subtree penugasan GM bukan baris pola") tidak menyebut cara teramati di UI; spec mengasersi Branch Surabaya tidak terkunci.
  - TC-FA-SU-1084 Expected butir d ("tidak ada entri `Auto-Revert` dan tidak ada entri `Remove (via Group Manager)`") tidak menyebut surface log; spec memakai Tab Changelog target untuk `Auto-Revert` dan modal Changelog Group Role untuk `Remove (via Group Manager)`.
  - TC-FA-SU-1084 Post Condition (entri `Assign`, `Edit`, `Remove` Object `Group Role` pada tiga surface log) tidak punya langkah observasi dan tidak diasersi.
  - Kalimat `Their Group Manager role assignments in this group and its sub-groups will also be removed.` tidak ada lagi pada copy D-05c varian pemicu Remove (TC-FA-SU-1083 butir a); spec tidak mengasersinya. Copy D-05 masih usulan (PM, `settings-role-permission` Open Item #7d).
