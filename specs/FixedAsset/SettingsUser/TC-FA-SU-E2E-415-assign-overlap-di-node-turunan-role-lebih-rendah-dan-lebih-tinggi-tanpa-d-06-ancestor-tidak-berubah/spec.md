---
id: TC-FA-SU-E2E-415-assign-overlap-di-node-turunan-role-lebih-rendah-dan-lebih-tinggi-tanpa-d-06-ancestor-tidak-berubah
title: "Assign Overlap di Node Turunan: Role Lebih Rendah dan Lebih Tinggi Tersimpan Tanpa D-06 dan Baris Ancestor Tidak Berubah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1105
  - TC-FA-SU-1106
coverage:
  web: automated
---

# Assign Overlap di Node Turunan: Role Lebih Rendah dan Lebih Tinggi Tersimpan Tanpa D-06 dan Baris Ancestor Tidak Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21; Accounts Payable adalah descendant Finance & Accounting) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini (Pre-setup #39): Disposal × Staff pada Finance & Accounting dan Borrowing & Assignment × Approver pada Finance & Accounting.
- Data uji: TC-FA-SU-1105 menugaskan Disposal × Monitoring & Report pada Accounts Payable (langkah 5 sampai 6); TC-FA-SU-1106 menugaskan Disposal × Asset Admin pada Accounts Payable (langkah 25 sampai 26). Langkah berulang 4 sampai 6 dan 24 sampai 26 memakai parameter itu.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed API untuk memulihkan Transaction Role Mira Anggraini ke Pre-setup #39 (di hook `before`, pada langkah 20, dan di hook `after`); pembacaan jumlah entri Object `Transaction Role` Tab Changelog target (total dan entri `Remove`) sebagai baseline sebelum aksi (bagian 8b butir 10); pembacaan hak efektif Mira Anggraini per Jenis Transaksi dan node lewat API resolusi hak (disediakan tim BE; hak efektif tidak dibaca lewat UI Settings > User). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini (baris Disposal × Monitoring & Report lalu Disposal × Asset Admin pada Accounts Payable ditambahkan); dipulihkan ke Pre-setup #39 lewat seed API pada langkah 20, langkah 39, dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada (node Accounts Payable dan penugasan #39) dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1105: Overlap dengan role lebih rendah di node turunan: tersimpan tanpa D-06, baris ancestor tidak berubah dan tidak dikurangi, satu entri log

1. Catat baseline Object `Transaction Role` Mira Anggraini pada Tab Changelog lewat kemampuan baca BE: jumlah seluruh entri dan jumlah entri `Remove`
2. Ketik Search `Mira Anggraini`, tekan Enter, lalu klik Name `Mira Anggraini`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Klik `[+ Assign]`
5. Pilih Group Accounts Payable, Transaction Disposal, Role Monitoring & Report
6. Klik `[Submit]`
7. Verifikasi toast "Success, Monitoring & Report has been assigned." tampil
8. Verifikasi modal tertutup
9. Verifikasi tidak ada dialog D-06 maupun dialog konfirmasi lain
10. Verifikasi baris Disposal × Staff tetap dengan badge Finance & Accounting (tidak diganti, tidak berpindah)
11. Verifikasi baris baru Disposal × Monitoring & Report muncul dengan badge Accounts Payable
12. Verifikasi tidak ada baris yang diproyeksikan untuk descendant
13. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
14. Verifikasi jumlah seluruh entri Object `Transaction Role` bertambah tepat satu dibanding baseline langkah 1 (tidak ada entri per descendant)
15. Verifikasi entri `Assign` Field `Disposal — Accounts Payable — Monitoring & Report` tercatat
16. Verifikasi jumlah entri `Remove` sama dengan baseline langkah 1 (tidak ada entri `Remove` untuk Staff pada Finance & Accounting)
17. Baca hak efektif Mira Anggraini pada Disposal untuk Finance & Accounting dan Accounts Payable lewat API resolusi hak
18. Verifikasi hak efektif Disposal pada Finance & Accounting tetap Staff (penugasan Monitoring & Report di node turunan tidak mengurangi hak ancestor)
19. Verifikasi hak efektif Disposal pada Accounts Payable = Staff (rung tertinggi yang mencakup)
20. Pulihkan Mira Anggraini ke Pre-setup #39 lewat seed API (baris Disposal × Monitoring & Report dihapus)

### TC-FA-SU-1106: Overlap dengan role lebih tinggi di node turunan: bukan naik tangga, role ancestor tidak diganti dan tanpa entri Remove

21. Buka Settings > User lewat sidebar, ketik Search `Mira Anggraini`, tekan Enter, lalu klik Name `Mira Anggraini`
22. Klik Tab Role lalu Sub-tab Transaction Role
23. Catat baseline Object `Transaction Role` Mira Anggraini pada Tab Changelog lewat kemampuan baca BE: jumlah seluruh entri dan jumlah entri `Remove`
24. Klik `[+ Assign]`
25. Pilih Group Accounts Payable, Transaction Disposal, Role Asset Admin
26. Klik `[Submit]`
27. Verifikasi toast "Success, Asset Admin has been assigned." tampil
28. Verifikasi tidak ada dialog (tersimpan langsung)
29. Verifikasi baris Disposal × Staff tetap dengan badge Finance & Accounting
30. Verifikasi baris baru Disposal × Asset Admin memuat Accounts Payable
31. Verifikasi Staff pada Finance & Accounting tidak diganti otomatis: baris Disposal × Asset Admin tidak memuat Finance & Accounting
32. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
33. Verifikasi jumlah seluruh entri Object `Transaction Role` bertambah tepat satu dibanding baseline langkah 23
34. Verifikasi entri `Assign` Field `Disposal — Accounts Payable — Asset Admin` tercatat
35. Verifikasi jumlah entri `Remove` sama dengan baseline langkah 23 (tidak ada pasangan `Remove` role lama)
36. Baca hak efektif Mira Anggraini pada Disposal untuk Finance & Accounting dan Accounts Payable lewat API resolusi hak
37. Verifikasi hak efektif Disposal pada Accounts Payable = Asset Admin
38. Verifikasi hak efektif Disposal pada Finance & Accounting = Staff
39. Pulihkan Mira Anggraini ke Pre-setup #39 lewat seed API (baris Disposal × Asset Admin dihapus)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 13, 20, 21, 22, 23, 32 dan 39. Baseline log mengikuti S-12 dan dicatat ulang sebelum aksi pemicu tiap TC (langkah 1 dan 23). Search `Mira Anggraini` pada langkah 2 dan 21 adalah langkah penghubung untuk menemukan baris target (R-16, R-23); langkah 21 membuka User List lewat sidebar karena pemulihan seed pada langkah 20 mengubah data yang ditampilkan Detail. Search pada langkah 13 dan 32 adalah pola baca-log Tab Changelog.
- Pemulihan lewat seed API (langkah 20 dan 39) memulihkan Pre-setup #39 antar TC dan pada akhir spec (S-06, S-09).
- Anchor 8b butir 2: toast tampil (langkah 7 dan 27) menjadi anchor bagi tidak ada dialog (langkah 9 dan 28); baris Disposal × Staff Finance & Accounting dan baris baru Accounts Payable tampil (langkah 10, 11 dan 29, 30) menjadi anchor bagi tidak ada baris proyeksi descendant (langkah 12) dan tidak ada baris Disposal × Asset Admin untuk Finance & Accounting (langkah 31). "Tidak ada entri `Remove`" dan "tidak ada entri per descendant" ditulis sebagai asersi jumlah terhadap baseline (bagian 3 prinsip 13 butir g, S-12), bukan asersi absence; entri `Assign` yang tercatat (langkah 15 dan 34) membaca baris teratas setelah selisih jumlah dibuktikan (S-14).
- Alasan di atas sekitar 35 langkah (39): dua TC adalah variasi aksi yang sama (Assign Disposal pada Accounts Payable, descendant Finance & Accounting) untuk satu aktor, satu target, dan seed Pre-setup #39 yang sama, tanpa kelas harness; blok berulang ada pada langkah 4 sampai 6 dan 24 sampai 26 dengan parameter di Prerequisites tanpa langkah bersyarat. Jumlah langkah dibentuk oleh Expected yang dipecah satu `Verifikasi` per klausa (S-01): 1105 memuat 13 klausa, 1106 memuat 12 klausa.- Temuan untuk QA:
  - Hak efektif (TC-FA-SU-1105 butir d dan TC-FA-SU-1106 butir d) diasersi lewat API resolusi hak, bukan UI Settings > User; kemampuan itu harus disediakan tim BE dan TC tidak menyebut nama endpoint-nya.
  - NC-25 (Open Item PRD #4: Remove Approver terhadap approver terdaftar, D-09 jamak) dan NC-26 (Open Item PRD #5: PIC lewat ancestor) tidak diasersi di spec ini.
  - TC-FA-SU-1105 butir b ("tidak ada baris yang diproyeksikan untuk descendant") tidak menyebut bentuk baris proyeksi; spec mengasersi tidak ada baris tambahan selain baris Disposal × Staff dan baris Disposal × Monitoring & Report yang disebut TC.
  - Peringkat rung (Staff lebih tinggi daripada Monitoring & Report, Asset Admin lebih tinggi daripada Staff) mengikuti Expected TC; spec tidak menambah asersi urutan rung di luar yang ditulis TC.
  - Post Condition kedua TC (Mira Anggraini dipulihkan oleh automation baseline) tidak punya langkah observasi dan tidak diasersi.
