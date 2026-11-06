---
id: TC-FA-SU-E2E-393-group-manager-bersarang-dialog-d-05c-satu-penugasan-dan-dialog-d-05d-dua-penugasan
title: "Group Manager Bersarang: Dialog D-05c untuk Satu Penugasan dan Dialog D-05d untuk Dua Penugasan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1086
  - TC-FA-SU-1087
coverage:
  web: automated
---

# Group Manager Bersarang: Dialog D-05c untuk Satu Penugasan dan Dialog D-05d untuk Dua Penugasan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit di langkah 46): Group Manager Oscar Pranata (Pre-setup #9), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_GM_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager (Pre-setup #48).
- Pengguna target: Oscar Pranata, varian #48: Group Manager IT Infrastructure, Accounts Payable, dan Finance & Accounting (Accounts Payable tercakup dua penugasan) dengan baris pola Group Manager pada ketiga node.
- Data uji: TC-FA-SU-1087 menghapus centang Update pada Finance & Accounting (node dicakup hanya penugasan Finance & Accounting) pada popup Assign Group Role Manage group; TC-FA-SU-1086 menghapus centang Update pada Accounts Payable (node dicakup dua penugasan) pada popup yang sama.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Oscar Pranata ke Pre-setup #48; pembacaan jumlah entri `Auto-Revert` Tab Changelog Oscar Pranata dan jumlah notifikasi in-app Oscar Pranata sebelum aksi sebagai baseline (bagian 8b butir 10). Entri log dan notifikasi muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager, baris pola, dan penugasan Oscar Pranata; dipulihkan ke Pre-setup #48 lewat seed API pada langkah penghubung (langkah 20 dan 45) dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1087: Group Manager bersarang: penyimpangan pada node yang hanya dicakup satu penugasan melepas penugasan itu saja, penugasan GM lain tetap, dan seluruh baris dipertahankan

1. Ketik Search `Oscar Pranata`, tekan Enter, lalu klik Name `Oscar Pranata`
2. Klik Tab Role lalu Sub-tab Group Role
3. Klik `[Assign Group]` pada baris Manage group
4. Hapus centang Update pada Finance & Accounting
5. Klik `[Save]`
6. Verifikasi dialog D-05c singular Title `Remove Group Manager` tampil
7. Verifikasi Body bullet `• Oscar Pranata`
8. Verifikasi dialog tidak memuat kalimat `This change will remove Group Manager status for these groups:` (bukan D-05d)
9. Klik `[Remove]`
10. Verifikasi toast "Success, permissions have been updated. Oscar Pranata is no longer Group Manager for Finance & Accounting." (T-06b)
11. Verifikasi penugasan Group Manager Finance & Accounting terlepas
12. Verifikasi seluruh baris pola Group Role pada node Finance & Accounting (termasuk baris Manage group yang diedit) tetap tersimpan sebagai baris biasa
13. Verifikasi baris pola Group Role pada Accounts Payable tidak berubah
14. Verifikasi baris pola Group Role IT Infrastructure tidak berubah
15. Verifikasi banner `This user is a Group Manager for: Accounts Payable, IT Infrastructure.`
16. Klik Sub-tab Transaction Role
17. Verifikasi seluruh baris pola Transaction Role pada node Finance & Accounting tetap tersimpan sebagai baris biasa
18. Verifikasi baris pola Transaction Role pada Accounts Payable tidak berubah
19. Verifikasi baris pola Transaction Role IT Infrastructure tidak berubah
20. Pulihkan Oscar Pranata ke Pre-setup #48 lewat seed API

### TC-FA-SU-1086: Group Manager bersarang: penyimpangan baris pola bersama melepas kedua penugasan GM dalam satu dialog D-05d dan satu toast T-06c

21. Catat jumlah entri `Auto-Revert` pada Tab Changelog Oscar Pranata dan jumlah notifikasi in-app Oscar Pranata (dibaca setelah notifikasi hasil TC-FA-SU-1087 tercatat) sebagai baseline
22. Buka Settings > User lewat sidebar
23. Ketik Search `Oscar Pranata`, tekan Enter, lalu klik Name `Oscar Pranata`
24. Klik Tab Role, klik Sub-tab Group Role, lalu klik `[Assign Group]` pada baris Manage group
25. Hapus centang Update pada Accounts Payable
26. Klik `[Save]`
27. Verifikasi satu dialog D-05d Title `Remove Group Manager` tampil
28. Verifikasi Body bullet `• Oscar Pranata`
29. Verifikasi kalimat `This change will remove Group Manager status for these groups:`
30. Verifikasi bullet `• Accounts Payable` dan `• Finance & Accounting`
31. Verifikasi penutup `Are you sure you want to remove it?`
32. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil
33. Tunggu toast lama hilang otomatis
34. Klik `[Remove]`
35. Verifikasi satu toast "Success, permissions have been updated. Oscar Pranata is no longer Group Manager." (T-06c)
36. Verifikasi kedua penugasan Group Manager (Accounts Payable dan Finance & Accounting) terlepas
37. Verifikasi seluruh baris pola Group Role pada node Finance & Accounting dan Accounts Payable (termasuk baris Manage group × Accounts Payable yang diedit, Update tidak dicentang) tetap tersimpan sebagai baris biasa
38. Verifikasi baris pola Group Role IT Infrastructure tidak berubah
39. Verifikasi banner `This user is a Group Manager for: IT Infrastructure.`
40. Klik Sub-tab Transaction Role
41. Verifikasi seluruh baris pola Transaction Role pada node Finance & Accounting dan Accounts Payable tetap tersimpan sebagai baris biasa
42. Verifikasi baris pola Transaction Role IT Infrastructure tidak berubah
43. Buka Tab Changelog, ketik Search `Oscar Pranata`, tekan Enter, lalu muat ulang sampai entri tampil
44. Verifikasi satu entri `Auto-Revert` Object `Group Manager` per penugasan (Accounts Payable dan Finance & Accounting), dua entri bertambah dibanding baseline pada Tab Changelog Oscar Pranata
45. Pulihkan Oscar Pranata ke Pre-setup #48 lewat seed API
46. Logout lalu login sebagai Group Manager Oscar Pranata
47. Buka panel notifikasi lalu muat ulang sampai notifikasi tampil
48. Verifikasi dua notifikasi in-app view-only (satu per grup: Accounts Payable dan Finance & Accounting) bertambah dibanding baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-FA-SU-1087 ditulis lebih dulu dari TC-FA-SU-1086 (urutan TC sumber dibalik): baseline notifikasi TC-FA-SU-1086 dicatat sesudah TC-FA-SU-1087 selesai dan dipulihkan, sehingga satu kali ganti akun ke Oscar Pranata di langkah terakhir cukup untuk menghitung notifikasi TC-FA-SU-1086 tanpa tercampur notifikasi TC-FA-SU-1087.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 16, 20, 21, 22, 23, 33, 40, 43, 45, 46 dan 47. Search `Oscar Pranata` pada langkah 1, 23 dan 43 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log dan notifikasi mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09). Langkah 33 menjaga hitungan "satu toast" tidak tercampur toast TC-FA-SU-1087 (R-12).
- Alasan di atas sekitar 35 langkah: kedua TC satu topik (Group Manager bersarang pada target dan aktor yang sama, Oscar Pranata dan Default User), tiap TC mengubah state sendiri dan dipulihkan (langkah 20 dan 45) sebelum TC berikutnya, dan kegagalan satu TC tidak membuat TC lain kehilangan makna; langkah banyak karena Expected bermajemuk (dialog, toast, banner, dan baris pola di dua sub-tab) yang wajib satu `Verifikasi` per klausa (S-01).
- Langkah pola baca-log: langkah 43 dan 44. Langkah terakhir spec mengganti akun ke Group Manager Oscar Pranata (ganti akun eksplisit, S-07).
- TC-FA-SU-1087 Post Condition (satu entri `Auto-Revert` dan satu notifikasi) tidak punya langkah observasi dan tidak diasersi.
- Temuan untuk QA:
  - Oscar Pranata di Pre-setup #9 memegang Group Manager pada IT Infrastructure dan Accounts Payable, sedangkan TC-FA-SU-1086 dan TC-FA-SU-1087 memakai varian #48 (ditambah Finance & Accounting dan Home Group dikosongkan). Spec memakai #48; angka turunan Role Oscar (48 = 6 × 2 + 2 × 9 × 2 di Pre-setup #43) tidak diasersi karena perilaku hitung belum diputuskan PM (PRD Open Item 3).
  - Dialog D-05c singular (TC-FA-SU-1087) dan D-05d (TC-FA-SU-1086) ditandai "copy usulan, perlu persetujuan PM" untuk varian Role Transaksi (PRD 12 #1 `settings-role-permission`). Body D-05d pada TC-FA-SU-1086 tidak memuat kalimat penutup D-05c edit CRUD `Their individual role permissions will remain as edited.`; spec mengikuti TC dan tidak menambahkan kalimat itu.
  - TC-FA-SU-1087 Expected butir a menyebut Body hanya bullet `• Oscar Pranata` tanpa kalimat pembuka; spec hanya mengasersi Title, bullet, dan bahwa kalimat daftar grup D-05d tidak ada.
  - TC-FA-SU-1086 Expected butir d ("satu notifikasi per grup") tidak menyebut teks notifikasi maupun cara menghitungnya; spec memakai baseline jumlah notifikasi dan panel notifikasi Oscar Pranata.
  - TC-FA-SU-1086 Post Condition butir b (dua entri `Auto-Revert` pada Tab System Log aktor dan Activity Log) tidak punya langkah observasi dan tidak diasersi; hanya Tab Changelog target yang diasersi (langkah 44).
  - TC-FA-SU-1086 Expected butir c menyebut "penugasan GM IT Infrastructure tidak berubah" tanpa cara observasi terpisah; spec mengasersinya lewat banner (langkah 39).
