---
id: TC-FA-SU-E2E-418-remove-baris-pada-node-ancestor-dialog-d-07a-generik-dan-satu-entri-log
title: "Remove Baris pada Node Ancestor: Dialog D-07a Generik Tanpa Daftar Descendant, Hanya Node Itu Dicabut, dan Satu Entri Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1111
coverage:
  web: automated
---

# Remove Baris pada Node Ancestor: Dialog D-07a Generik Tanpa Daftar Descendant, Hanya Node Itu Dicabut, dan Satu Entri Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserOV` (varian `FaUserMain`, Pre-setup #49; disediakan tim FE/BE sebelum eksekusi lewat seed API di hook `before`) dengan pohon grup (Pre-setup #21; Jakarta Selatan Distribution Center adalah descendant Region Jawa).
- Pengguna target: Rina Susanti (Pre-setup #49) tanpa Global Role dan Group Role dengan 5 penugasan Transaction Role: Disposal × Asset Admin (Region Jawa), Disposal × Approver (Region Jawa), Disposal × Monitoring & Report (Jakarta Selatan Distribution Center), Damaged × Staff (Finance & Accounting), dan Transfer × Monitoring & Report (Jakarta Selatan Distribution Center). Rina Susanti juga akun aktor Read Only (Pre-setup #5) pada suite ini; di spec ini ia hanya target dan sesi aktor tetap Total Control Lina Marlina.
- Data uji: baris dicabut Disposal × Asset Admin pada Region Jawa; baris tetap Disposal × Monitoring & Report (Jakarta Selatan Distribution Center) dan Disposal × Approver.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserOV` (Pre-setup #49) di hook `before`, untuk memulihkan Rina Susanti ke Pre-setup #49 pada langkah 18 dan di hook `after` (baris Disposal × Asset Admin Region Jawa harus utuh sebelum spec ini berjalan; spec lain yang mengubahnya, termasuk spec 417, memulihkannya sendiri); pembacaan jumlah entri Object `Transaction Role` Tab Changelog target (total) sebagai baseline sebelum aksi (bagian 8b butir 10); pembacaan hak efektif Rina Susanti per Jenis Transaksi dan node lewat API resolusi hak (disediakan tim BE; hak efektif tidak dibaca lewat UI Settings > User). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Rina Susanti (baris Disposal × Asset Admin Region Jawa dicabut); dipulihkan ke Pre-setup #49 lewat seed API pada langkah 18 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada (node Jakarta Selatan Distribution Center dan penugasan #49) dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1111: Remove baris pada node ancestor: dialog D-07 generik tanpa daftar descendant, hanya node itu dicabut, penugasan turunan tetap, satu entri log

1. Catat baseline Object `Transaction Role` Rina Susanti pada Tab Changelog lewat kemampuan baca BE: jumlah seluruh entri
2. Ketik Search `Rina Susanti`, tekan Enter, lalu klik Name `Rina Susanti`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Klik ⋯ pada baris Disposal × Asset Admin lalu klik `Remove`
5. Verifikasi dialog Title `Remove Transaction Role` (D-07a) tampil
6. Verifikasi Body bullet `• Rina Susanti`
7. Verifikasi kalimat `This user will lose the selected transaction role.`
8. Verifikasi penutup `Are you sure you want to remove it?`
9. Verifikasi dialog tidak memuat daftar penugasan atau node descendant yang kehilangan cakupan
10. Klik `[Remove]`
11. Verifikasi toast "Success, Asset Admin has been removed." tampil
12. Verifikasi baris Disposal × Asset Admin hilang
13. Verifikasi baris Disposal × Monitoring & Report (Jakarta Selatan Distribution Center) tetap
14. Verifikasi baris Disposal × Approver tetap
15. Buka Tab Changelog, Search `Rina Susanti`, tekan Enter, lalu muat ulang sampai entri tampil
16. Verifikasi jumlah seluruh entri Object `Transaction Role` bertambah tepat satu dibanding baseline langkah 1
17. Verifikasi entri `Remove` Field `Disposal — Region Jawa — Asset Admin` tercatat
18. Verifikasi tidak ada entri baru untuk Jakarta Selatan Distribution Center atau node descendant lain
19. Baca hak efektif Rina Susanti pada Disposal untuk Jakarta Selatan Distribution Center lewat API resolusi hak
20. Verifikasi hak efektif Disposal pada Jakarta Selatan Distribution Center turun ke Monitoring & Report (sisa penugasan yang mencakup)
21. Pulihkan Rina Susanti ke Pre-setup #49 lewat seed API (baris Disposal × Asset Admin Region Jawa dikembalikan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 15 dan 21. Baseline log mengikuti S-12. Search `Rina Susanti` pada langkah 2 adalah langkah penghubung untuk menemukan baris target (R-16, R-23); Search pada langkah 15 adalah pola baca-log Tab Changelog.
- Anchor 8b butir 2: dialog D-07a tampil dengan Title, Body, kalimat, dan penutup (langkah 5 sampai 8) menjadi anchor bagi tidak ada daftar penugasan atau node descendant (langkah 9); baris Disposal × Approver dan Monitoring & Report tetap tampil (langkah 13, 14) berdampingan dengan baris Asset Admin hilang (langkah 12, beranchor toast sukses langkah 11); entri `Remove` yang tercatat (langkah 17) menjadi anchor bagi tidak ada entri untuk descendant (langkah 18), yang juga dibatasi oleh selisih jumlah tepat satu (langkah 16, asersi jumlah menurut bagian 3 prinsip 13 butir g dan S-12).
- Pembagian TC: baris Disposal × Asset Admin Region Jawa utuh dibutuhkan TC-FA-SU-1111, sedangkan spec 417 (TC-FA-SU-1108) mengubahnya; seed `FaUserOV` dipulihkan di antara kedua spec dan spec ini menyeed ulang Pre-setup #49 di hook `before`.
- Temuan untuk QA:
  - Hak efektif (TC-FA-SU-1111 butir d) diasersi lewat API resolusi hak, bukan UI Settings > User; kemampuan itu harus disediakan tim BE dan TC tidak menyebut nama endpoint-nya.
  - TC-FA-SU-1111 menguji Remove pada Asset Admin; NC-25 (Open Item PRD #4: Remove Approver terhadap approver terdaftar, D-09 jamak) dan NC-26 (Open Item PRD #5: PIC lewat ancestor) tidak diasersi di spec ini.
  - Seed Pre-setup #49 (`FaUserOV`) harus disediakan tim FE/BE; Rina Susanti juga akun aktor Read Only (Pre-setup #5) sehingga di spec ini hanya dipakai sebagai target.
  - Post Condition TC-FA-SU-1111 (Rina Susanti dipulihkan oleh automation baseline) tidak punya langkah observasi dan tidak diasersi.
