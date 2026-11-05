---
id: TC-FA-SU-E2E-427-assign-transaction-role-ke-node-dalam-constraint-dan-penugasan-lama-di-luar-constraint-tidak-dimigrasi
title: "Assign Transaction Role ke Node Dalam Constraint dan Penugasan Lama di Luar Constraint Tampil, Tercentang, dan Dapat Dicabut"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1120
  - TC-FA-SU-1121
coverage:
  web: automated
---

# Assign Transaction Role ke Node Dalam Constraint dan Penugasan Lama di Luar Constraint Tampil, Tercentang, dan Dapat Dicabut

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Finance & Accounting dengan anak Accounts Payable; IT Infrastructure, Branch Surabaya, dan grup lain) dan seed `FaUserHGT` (Pre-setup #51; varian `FaUserMain`, Home Group tidak dikosongkan). Seed `FaUserHGT` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Gita Permata (Pre-setup #51; Home Group Finance & Accounting; Transaction Role Disposal × Asset Admin pada Finance & Accounting, Disposal × Approver pada Accounts Payable, dan Damaged × Staff pada IT Infrastructure sebagai penugasan lama di luar constraint). Gita Permata juga akun aktor Pre-setup #20; di spec ini hanya menjadi pengguna target dan sesi aktor tetap Total Control Lina Marlina.
- Data uji: TC-FA-SU-1120 menugaskan Group Finance & Accounting, Transaction Transfer, Role Monitoring & Report (langkah 5); TC-FA-SU-1121 mencabut IT Infrastructure dari baris Damaged × Staff (langkah 24 sampai 28).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserHGT` (Pre-setup #51) di hook `before`, untuk memulihkan Gita Permata ke Pre-setup #51 pada langkah 33 dan di hook `after` (baris Transfer × Monitoring & Report dihapus dan baris Damaged × Staff pada IT Infrastructure dikembalikan); pembacaan jumlah entri `Assign` Object `Transaction Role` pada Tab Changelog target, Tab System Log aktor, dan Activity Log serta jumlah entri `Remove` Object `Transaction Role` pada Tab Changelog target sebagai baseline sebelum aksi (S-12, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit. Selektor node pohon, status Disabled, status tercentang, dan tooltip disediakan tim FE.
- State global yang diubah: Transaction Role Gita Permata (baris Transfer × Monitoring & Report ditambahkan pada langkah 6; baris Damaged × Staff dicabut pada langkah 28); dipulihkan ke Pre-setup #51 lewat seed API pada langkah 33 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script (kunci baru: node Accounts Payable dan penugasan #51).

## Test Steps

### TC-FA-SU-1120: Assign Transaction Role ke node dalam constraint pada target ber-constraint: tersimpan dengan toast assigned dan log Assign

1. Catat baseline jumlah entri `Assign` Object `Transaction Role` Gita Permata pada Tab Changelog target, Tab System Log aktor, dan Activity Log lewat kemampuan baca BE
2. Ketik Search `Gita Permata`, tekan Enter, lalu klik Name `Gita Permata`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Klik `[+ Assign]`
5. Pilih Group Finance & Accounting, Transaction Transfer, Role Monitoring & Report
6. Klik `[Submit]`
7. Verifikasi modal tertutup
8. Verifikasi toast "Success, Monitoring & Report has been assigned." tampil
9. Verifikasi tabel menampilkan baris Transfer × Monitoring & Report dengan badge Finance & Accounting
10. Buka Tab Changelog, Search `Gita Permata`, tekan Enter, lalu muat ulang sampai entri tampil
11. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Transfer — Finance & Accounting — Monitoring & Report` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline langkah 1 pada Tab Changelog
12. Buka Tab System Log aktor dan Search `Gita Permata`, tekan Enter
13. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Transfer — Finance & Accounting — Monitoring & Report` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline langkah 1 pada Tab System Log
14. Buka Activity Log
15. Verifikasi entri `Assign` / Object `Transaction Role` / Field `Transfer — Finance & Accounting — Monitoring & Report` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline langkah 1 pada Activity Log

### TC-FA-SU-1121: Penugasan Transaction Role lama di luar constraint tidak dimigrasi: tetap tampil, tercentang di popup Assign Group, dan dapat dicabut centangnya

16. Buka Settings > User lewat sidebar, ketik Search `Gita Permata`, tekan Enter, lalu klik Name `Gita Permata`
17. Klik Tab Role lalu Sub-tab Transaction Role
18. Catat baseline jumlah entri `Remove` Object `Transaction Role` Gita Permata pada Tab Changelog target lewat kemampuan baca BE
19. Verifikasi baris Damaged × Staff dengan badge IT Infrastructure tampil walau Home Group Gita Permata Finance & Accounting (tidak dimigrasi dan tidak dicabut)
20. Klik `[Assign Group]` pada baris Damaged × Staff
21. Verifikasi IT Infrastructure tercentang dan tidak Disabled
22. Arahkan kursor ke Branch Surabaya
23. Verifikasi Branch Surabaya (di luar constraint, belum ter-assign) Disabled dan tooltip "This group is outside the user's home group." tampil
24. Hapus centang IT Infrastructure
25. Verifikasi `[Save]` Enabled
26. Klik `[Save]`
27. Verifikasi dialog Remove Transaction Role (D-07) tampil
28. Klik `[Remove]`
29. Verifikasi toast "Success, Staff has been removed." tampil
30. Verifikasi baris Damaged × Staff hilang dari tabel
31. Buka Tab Changelog, Search `Gita Permata`, tekan Enter, lalu muat ulang sampai entri tampil
32. Verifikasi entri `Remove` / Object `Transaction Role` / Field `Damaged — IT Infrastructure — Staff` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline langkah 18 pada Tab Changelog
33. Pulihkan Gita Permata ke Pre-setup #51 lewat seed API (baris Transfer × Monitoring & Report dihapus dan baris Damaged × Staff pada IT Infrastructure dikembalikan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 10, 12, 14, 16, 17, 18, 31 dan 33. Search `Gita Permata` pada langkah 2 dan 16 menemukan baris target (R-16, R-23); Search pada langkah 10, 12, dan 31 adalah pola baca-log. Langkah 16 membuka layar secara eksplisit sesudah pindah ke Activity Log (S-14). Baseline langkah 1 dan 18 mengikuti S-12 dan dicatat sebelum aksi pemicu tiap TC.
- Expected a TC-FA-SU-1120 ("modal tertutup dan toast tampil") dan Expected a TC-FA-SU-1121 ("tampil walau Home Group ... tidak dimigrasi dan tidak dicabut") masing-masing satu `Verifikasi` per klausa (S-01). Pencabutan pada TC-FA-SU-1121 adalah pencabutan manual: entri `Remove` Tab Changelog (langkah 32) mencatatnya, berbeda dari pencabutan akibat constraint yang silent.
- Hover mendahului asersi tooltip (bagian 8b butir 5, langkah 22 dan 23). Verifikasi Branch Surabaya memuat "Disabled dengan tooltip" dalam satu butir Expected (S-01).
- TC-FA-SU-1120 dan TC-FA-SU-1121 hanya di spec ini.
- Temuan untuk QA:
  - Copy tooltip S-45 ("This group is outside the user's home group.") masih usulan (NC-27). Spec mengasersi literal TC; ubah bila PM mengganti copy.
  - Seed `FaUserHGT` (Pre-setup #51) wajib disediakan tim FE/BE; kunci fixture baru (node Accounts Payable dan penugasan #51 Gita Permata) dicatat untuk fixture `fixtures/fixed-asset-settings-user.json`.
  - Post Condition TC-FA-SU-1121 menyebut entri `Remove` di tiga permukaan (Tab Changelog target, Tab System Log aktor, Activity Log), sedangkan langkah observasi TC hanya "Amati tabel dan Tab Changelog" dan Expected e hanya menyebut "tercatat satu kali"; spec mengasersi Tab Changelog saja (S-01, S-15). Tab System Log aktor dan Activity Log tidak diasersi untuk TC itu.
  - TC-FA-SU-1120 Expected c menyebut "tercatat satu kali di tiga permukaan log"; spec mengasersi pertambahan tepat satu entri terhadap baseline pada ketiga permukaan.
  - TC-FA-SU-1121 Expected b: perilaku Save popup Assign Group dengan baris lama di luar constraint tidak ditetapkan PRD selain yang disebut TC (dialog D-07 pada pencabutan); spec tidak mengasersi hal lain.
  - Post Condition kedua TC (Gita Permata dipulihkan oleh automation baseline) tidak punya langkah observasi dan tidak diasersi.
