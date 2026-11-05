---
id: TC-FA-SU-E2E-416-assign-overlap-ancestor-setelah-turunan-dan-assign-group-menambah-descendant
title: "Assign Overlap: Penugasan Ancestor Setelah Turunan Tanpa D-06, dan Assign Group Menambah Descendant pada Baris yang Ancestor-nya Sudah Tersimpan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1107
  - TC-FA-SU-1110
coverage:
  web: automated
---

# Assign Overlap: Penugasan Ancestor Setelah Turunan Tanpa D-06, dan Assign Group Menambah Descendant pada Baris yang Ancestor-nya Sudah Tersimpan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserOV` (varian `FaUserMain`, Pre-setup #49; disediakan tim FE/BE sebelum eksekusi lewat seed API di hook `before`) dengan pohon grup (Pre-setup #21; Jakarta Selatan Distribution Center adalah descendant Region Jawa).
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Rina Susanti (Logistics Warehouse pada Pre-setup #43/#49) dikosongkan lewat seed API di hook `before` supaya Region Jawa (langkah 5) dan Jakarta Selatan Distribution Center (langkah 23) tidak Disabled oleh gate Home Group constraint dan Assign Transfer × Asset Admin pada Region Jawa dan Assign Group pada baris Disposal × Approver tidak ditolak `422` (V-09); seed pemulihan Pre-setup #49 pada langkah 18, langkah 35, dan di hook `after` memulihkan penugasan Transaction Role dengan Home Group tetap kosong; Home Group Rina Susanti dipulihkan ke Logistics Warehouse hanya di hook `after`. Seed per target disediakan tim FE/BE.
- Pengguna target: Rina Susanti (Pre-setup #49) tanpa Global Role dan Group Role dengan 5 penugasan Transaction Role: Disposal × Asset Admin (Region Jawa), Disposal × Approver (Region Jawa), Disposal × Monitoring & Report (Jakarta Selatan Distribution Center), Damaged × Staff (Finance & Accounting), dan Transfer × Monitoring & Report (Jakarta Selatan Distribution Center). Rina Susanti juga akun aktor Read Only (Pre-setup #5) pada suite ini; di spec ini ia hanya target dan sesi aktor tetap Total Control Lina Marlina.
- Data uji: TC-FA-SU-1107 menugaskan Transfer × Asset Admin pada Region Jawa (ancestor, langkah 5); TC-FA-SU-1110 menambah Jakarta Selatan Distribution Center (descendant) pada baris Disposal × Approver (langkah 23).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserOV` (Pre-setup #49) di hook `before`, untuk memulihkan Rina Susanti ke Pre-setup #49 pada langkah 18, langkah 35, dan di hook `after`; pembacaan jumlah entri Object `Transaction Role` Tab Changelog target (total dan entri `Remove`) sebagai baseline sebelum aksi (bagian 8b butir 10); pembacaan hak efektif Rina Susanti per Jenis Transaksi dan node lewat API resolusi hak (disediakan tim BE; hak efektif tidak dibaca lewat UI Settings > User). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Rina Susanti (baris Transfer × Asset Admin ditambahkan, lalu Jakarta Selatan Distribution Center ditambahkan pada baris Disposal × Approver); dipulihkan ke Pre-setup #49 lewat seed API pada langkah 18, langkah 35, dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada (node Jakarta Selatan Distribution Center dan penugasan #49) dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1107: Overlap dengan penugasan di ancestor setelah turunan: role turunan tidak ikut diganti dan tidak ada D-06

1. Catat baseline Object `Transaction Role` Rina Susanti pada Tab Changelog lewat kemampuan baca BE: jumlah seluruh entri dan jumlah entri `Remove`
2. Ketik Search `Rina Susanti`, tekan Enter, lalu klik Name `Rina Susanti`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Klik `[+ Assign]`
5. Pilih Group Region Jawa, Transaction Transfer, Role Asset Admin
6. Klik `[Submit]`
7. Verifikasi toast "Success, Asset Admin has been assigned." tampil
8. Verifikasi tidak ada dialog D-06 dan tidak ada dialog konfirmasi
9. Verifikasi baris Transfer × Monitoring & Report tetap dengan badge Jakarta Selatan Distribution Center
10. Verifikasi baris baru Transfer × Asset Admin memuat Region Jawa
11. Buka Tab Changelog, Search `Rina Susanti`, tekan Enter, lalu muat ulang sampai entri tampil
12. Verifikasi jumlah seluruh entri Object `Transaction Role` bertambah tepat satu dibanding baseline langkah 1 (tidak ada entri per descendant)
13. Verifikasi entri `Assign` Field `Transfer — Region Jawa — Asset Admin` tercatat
14. Verifikasi jumlah entri `Remove` sama dengan baseline langkah 1 (tidak ada `Remove` untuk Monitoring & Report pada Jakarta Selatan Distribution Center)
15. Baca hak efektif Rina Susanti pada Transfer untuk Region Jawa dan Jakarta Selatan Distribution Center lewat API resolusi hak
16. Verifikasi hak efektif Transfer pada Region Jawa = Asset Admin
17. Verifikasi hak efektif Transfer pada Jakarta Selatan Distribution Center = Asset Admin (rung tertinggi yang mencakup)
18. Pulihkan Rina Susanti ke Pre-setup #49 lewat seed API (baris Transfer × Asset Admin dihapus)

### TC-FA-SU-1110: Assign Group menambah descendant pada baris yang node ancestor-nya sudah tersimpan: tidak Disabled, tanpa D-06 atau D-07, satu entri log

19. Buka Settings > User lewat sidebar, ketik Search `Rina Susanti`, tekan Enter, lalu klik Name `Rina Susanti`
20. Klik Tab Role lalu Sub-tab Transaction Role
21. Catat baseline Object `Transaction Role` Rina Susanti pada Tab Changelog lewat kemampuan baca BE: jumlah seluruh entri
22. Klik `[Assign Group]` pada baris Disposal × Approver
23. Centang Jakarta Selatan Distribution Center
24. Verifikasi Region Jawa tercentang
25. Verifikasi Jakarta Selatan Distribution Center tidak Disabled dan dapat dicentang
26. Verifikasi preview scope mendaftar Jakarta Selatan Distribution Center
27. Klik `[Save]`
28. Verifikasi toast "Success, Approver has been assigned." tampil
29. Verifikasi tidak ada dialog D-06 maupun D-07
30. Verifikasi kolom Group baris Disposal × Approver menampilkan dua badge berurut A-Z: Jakarta Selatan Distribution Center dan Region Jawa
31. Buka Tab Changelog, Search `Rina Susanti`, tekan Enter, lalu muat ulang sampai entri tampil
32. Verifikasi jumlah seluruh entri Object `Transaction Role` bertambah tepat satu dibanding baseline langkah 21
33. Verifikasi entri `Assign` Field `Disposal — Jakarta Selatan Distribution Center — Approver` tercatat
34. Verifikasi Region Jawa tidak dicatat ulang: tidak ada entri baru Field `Disposal — Region Jawa — Approver`
35. Pulihkan Rina Susanti ke Pre-setup #49 lewat seed API (Jakarta Selatan Distribution Center dicabut dari baris Disposal × Approver)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 11, 18, 19, 20, 21, 31 dan 35. Baseline log mengikuti S-12 dan dicatat ulang sebelum aksi pemicu tiap TC (langkah 1 dan 21). Search `Rina Susanti` pada langkah 2 dan 19 adalah langkah penghubung untuk menemukan baris target (R-16, R-23); langkah 19 membuka User List lewat sidebar karena pemulihan seed pada langkah 18 mengubah data yang ditampilkan Detail. Search pada langkah 11 dan 31 adalah pola baca-log Tab Changelog.
- Pemulihan lewat seed API (langkah 18 dan 35) memulihkan Pre-setup #49 antar TC dan pada akhir spec (S-06, S-09).
- Anchor 8b butir 2: toast tampil (langkah 7 dan 28) menjadi anchor bagi tidak ada dialog (langkah 8 dan 29). "Tidak ada entri per descendant", "tidak ada `Remove`", dan "Region Jawa tidak dicatat ulang" ditulis sebagai asersi jumlah terhadap baseline (bagian 3 prinsip 13 butir g, S-12), didahului entri `Assign` yang tercatat (langkah 13 dan 33; S-14). Langkah 34 diasersi sebagai himpunan satu entri baru yang sudah diidentifikasi pada langkah 33, bukan sebagai kelas absence.
- Pre-setup #50 diterapkan hanya pada Rina Susanti (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih Region Jawa dan Jakarta Selatan Distribution Center di luar Home Group Logistics Warehouse. Penugasan Transaction Role tetap sesuai Pre-setup #49. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - Hak efektif (TC-FA-SU-1107 butir d) diasersi lewat API resolusi hak, bukan UI Settings > User; kemampuan itu harus disediakan tim BE dan TC tidak menyebut nama endpoint-nya.
  - Preview scope (TC-FA-SU-1110 butir a): PRD tidak menetapkan format atau copy preview scope; spec mengasersi longgar bahwa preview mendaftar Jakarta Selatan Distribution Center sebagai daftar node (langkah 26). Selektor dan format perlu dikonfirmasi tim FE.
  - Seed Pre-setup #49 (`FaUserOV`) harus disediakan tim FE/BE; Rina Susanti juga akun aktor Read Only (Pre-setup #5) sehingga di spec ini hanya dipakai sebagai target.
  - NC-25 (Open Item PRD #4: Remove Approver terhadap approver terdaftar, D-09 jamak) dan NC-26 (Open Item PRD #5: PIC lewat ancestor) tidak diasersi di spec ini.
  - Post Condition kedua TC (Rina Susanti dipulihkan oleh automation baseline) tidak punya langkah observasi dan tidak diasersi.
