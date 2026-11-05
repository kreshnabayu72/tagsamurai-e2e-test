---
id: TC-FA-SU-E2E-417-dialog-d-06-hanya-node-yang-sama-node-lain-naik-tangga-dan-cancel-membatalkan-seluruh-save
title: "Dialog D-06 Hanya Mendaftar Node yang Sama, Node Lain Naik Tangga Otomatis, dan Cancel Membatalkan Seluruh Save"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1108
coverage:
  web: automated
---

# Dialog D-06 Hanya Mendaftar Node yang Sama, Node Lain Naik Tangga Otomatis, dan Cancel Membatalkan Seluruh Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserOV` (varian `FaUserMain`, Pre-setup #49; disediakan tim FE/BE sebelum eksekusi lewat seed API di hook `before`) dengan pohon grup (Pre-setup #21; Jakarta Selatan Distribution Center adalah descendant Region Jawa).
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Rina Susanti (Logistics Warehouse pada Pre-setup #43/#49) dikosongkan lewat seed API di hook `before` supaya Region Jawa dan Jakarta Selatan Distribution Center (langkah 5 dan 20) tidak Disabled oleh gate Home Group constraint dan Assign Disposal × Staff pada kedua node tidak ditolak `422` (V-09); seed pemulihan Pre-setup #49 pada langkah 32 dan di hook `after` memulihkan penugasan Transaction Role dengan Home Group tetap kosong; Home Group Rina Susanti dipulihkan ke Logistics Warehouse hanya di hook `after`. Seed per target disediakan tim FE/BE.
- Pengguna target: Rina Susanti (Pre-setup #49) tanpa Global Role dan Group Role dengan 5 penugasan Transaction Role: Disposal × Asset Admin (Region Jawa), Disposal × Approver (Region Jawa), Disposal × Monitoring & Report (Jakarta Selatan Distribution Center), Damaged × Staff (Finance & Accounting), dan Transfer × Monitoring & Report (Jakarta Selatan Distribution Center). Rina Susanti juga akun aktor Read Only (Pre-setup #5) pada suite ini; di spec ini ia hanya target dan sesi aktor tetap Total Control Lina Marlina.
- Data uji: Disposal pada Region Jawa (Asset Admin, turun ke Staff) dan Jakarta Selatan Distribution Center (Monitoring & Report, naik ke Staff), Role Staff (langkah 5 dan 20).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserOV` (Pre-setup #49) di hook `before`, untuk memulihkan Rina Susanti ke Pre-setup #49 pada langkah 32 dan di hook `after` (baris Disposal × Asset Admin Region Jawa harus utuh kembali karena spec lain, termasuk spec Remove baris Asset Admin Region Jawa, bergantung padanya); pembacaan jumlah entri Object `Transaction Role` Tab Changelog target sebagai baseline sebelum aksi (bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Rina Susanti (Disposal × Asset Admin Region Jawa dan Disposal × Monitoring & Report Jakarta Selatan Distribution Center beralih ke Disposal × Staff); dipulihkan ke Pre-setup #49 lewat seed API pada langkah 32 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada (node Jakarta Selatan Distribution Center dan penugasan #49) dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1108: Dialog D-06 hanya mendaftar node dengan penurunan tangga pada node yang sama; node lain dalam Save yang sama naik tangga otomatis dan Cancel membatalkan seluruh Save

1. Catat baseline Object `Transaction Role` Rina Susanti pada Tab Changelog lewat kemampuan baca BE: jumlah seluruh entri
2. Ketik Search `Rina Susanti`, tekan Enter, lalu klik Name `Rina Susanti`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Klik `[+ Assign]`
5. Pilih Group Region Jawa dan Jakarta Selatan Distribution Center, Transaction Disposal, Role Staff
6. Klik `[Submit]`
7. Verifikasi dialog D-06 Title `Change Transaction Role` tampil
8. Verifikasi dialog mendaftar `• Region Jawa (currently Asset Admin)`
9. Verifikasi dialog tidak mendaftar Jakarta Selatan Distribution Center (naik tangga)
10. Verifikasi daftar dialog tidak dipengaruhi penugasan Approver Region Jawa maupun role di ancestor atau descendant lain: tidak ada bullet selain Region Jawa
11. Klik `[Cancel]`
12. Verifikasi dialog tertutup
13. Verifikasi Region Jawa tetap Asset Admin: baris Disposal × Asset Admin memuat Region Jawa
14. Verifikasi Jakarta Selatan Distribution Center tetap Monitoring & Report: baris Disposal × Monitoring & Report memuat Jakarta Selatan Distribution Center
15. Verifikasi tidak ada toast
16. Buka Tab Changelog, Search `Rina Susanti`, tekan Enter, lalu muat ulang
17. Verifikasi jumlah seluruh entri Object `Transaction Role` sama dengan baseline langkah 1
18. Klik Tab Role lalu Sub-tab Transaction Role
19. Klik `[+ Assign]`
20. Pilih Group Region Jawa dan Jakarta Selatan Distribution Center, Transaction Disposal, Role Staff
21. Klik `[Submit]`
22. Klik `[Change]`
23. Verifikasi baris Disposal × Staff memuat Region Jawa dan Jakarta Selatan Distribution Center (kedua node tersimpan sekaligus)
24. Verifikasi baris Disposal × Asset Admin hilang
25. Verifikasi baris Disposal × Monitoring & Report hilang
26. Buka Tab Changelog, Search `Rina Susanti`, tekan Enter, lalu muat ulang sampai entri tampil
27. Verifikasi jumlah seluruh entri Object `Transaction Role` bertambah tepat empat dibanding baseline langkah 1 (tidak ada entri per descendant)
28. Verifikasi untuk Region Jawa tercatat entri `Remove` Field `Disposal — Region Jawa — Asset Admin`
29. Verifikasi untuk Region Jawa tercatat entri `Assign` Field `Disposal — Region Jawa — Staff`
30. Verifikasi untuk Jakarta Selatan Distribution Center tercatat entri `Remove` Field `Disposal — Jakarta Selatan Distribution Center — Monitoring & Report`
31. Verifikasi untuk Jakarta Selatan Distribution Center tercatat entri `Assign` Field `Disposal — Jakarta Selatan Distribution Center — Staff`
32. Pulihkan Rina Susanti ke Pre-setup #49 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 16, 18, 26 dan 32. Baseline log mengikuti S-12 dan dicatat sekali sebelum aksi pemicu pertama; `[Cancel]` tidak mengubah jumlah entri sehingga baseline yang sama berlaku bagi `[Change]` (langkah 17 membuktikannya). Search `Rina Susanti` pada langkah 2 adalah langkah penghubung untuk menemukan baris target (R-16, R-23); Search pada langkah 16 dan 26 adalah pola baca-log Tab Changelog. Langkah 18 sampai 21 mengulang langkah 3 sampai 6 sesuai "Ulangi langkah 2 sampai 4" pada TC.
- Anchor 8b butir 2: dialog D-06 tampil (langkah 7) menjadi anchor bagi Jakarta Selatan Distribution Center tidak didaftar (langkah 9) dan tidak ada bullet lain (langkah 10); baris Disposal × Asset Admin dan Disposal × Monitoring & Report tetap ada (langkah 13, 14) menjadi anchor bagi tidak ada toast (langkah 15); baris Disposal × Staff tampil (langkah 23) menjadi anchor bagi baris Asset Admin dan Monitoring & Report hilang (langkah 24, 25). "Tidak ada entri log" pada `[Cancel]` ditulis sebagai asersi jumlah terhadap baseline (bagian 3 prinsip 13 butir g, S-12), bukan asersi absence.
- Pembacaan log (S-14): empat entri baru jatuh dalam menit yang sama; spec mengasersi himpunan empat baris teratas tanpa mengandalkan urutan di antaranya, sehingga kata "lalu" (`Remove` lalu `Assign` per node) pada Expected d tidak diasersi sebagai urutan.
- Pembagian TC: TC-FA-SU-1108 hanya ada di spec ini; spec 418 (TC-FA-SU-1111) membutuhkan baris Disposal × Asset Admin Region Jawa utuh sedangkan langkah 22 spec ini mengubahnya, sehingga seed `FaUserOV` dipulihkan pada langkah 32 dan di hook `after`, dan spec 418 menyeed ulang Pre-setup #49 di hook `before`.
- Pre-setup #50 diterapkan hanya pada Rina Susanti (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih Region Jawa dan Jakarta Selatan Distribution Center di luar Home Group Logistics Warehouse. Penugasan Transaction Role tetap sesuai Pre-setup #49. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - Post Condition TC-FA-SU-1108 menyebut pasangan entri tercatat pada Tab Changelog target, Tab System Log aktor, dan Activity Log, sedangkan langkah observasi TC hanya "Amati tabel dan Tab Changelog"; spec mengasersi Tab Changelog saja (S-01, S-15). Tab System Log aktor dan Activity Log tidak diasersi.
  - Expected d menulis `Remove` "lalu" `Assign`; urutan antar entri yang jatuh pada menit yang sama tidak dapat diasersi (kolom Date berketelitian menit). Mohon dikonfirmasi apakah urutan perlu diasersi lewat sumber lain.
  - Seed Pre-setup #49 (`FaUserOV`) harus disediakan tim FE/BE; Rina Susanti juga akun aktor Read Only (Pre-setup #5) sehingga di spec ini hanya dipakai sebagai target.
  - NC-25 (Open Item PRD #4: Remove Approver terhadap approver terdaftar, D-09 jamak) dan NC-26 (Open Item PRD #5: PIC lewat ancestor) tidak diasersi di spec ini.
