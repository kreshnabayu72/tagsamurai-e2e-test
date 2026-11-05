---
id: TC-FA-SU-E2E-423-pemilih-group-role-target-ber-constraint-node-dalam-dan-luar-constraint-dan-assign-ke-node-dalam
title: "Popup Select Group Group Role Target Ber-constraint: Node Dalam dan Luar Constraint dan Assign ke Node Dalam Constraint"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1114
  - TC-FA-SU-1115
coverage:
  web: automated
---

# Popup Select Group Group Role Target Ber-constraint: Node Dalam dan Luar Constraint dan Assign ke Node Dalam Constraint

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Finance & Accounting dengan anak Accounts Payable; IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa dengan anak Jakarta Selatan Distribution Center) dan seed `FaUserHGT` (Pre-setup #51; varian `FaUserMain`, Home Group tidak dikosongkan). Seed `FaUserHGT` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Gita Permata (Pre-setup #51; Home Group Finance & Accounting; Group Role Manage group pada Finance & Accounting; Transaction Role Disposal × Asset Admin, Disposal × Approver, dan Damaged × Staff). Gita Permata juga akun aktor Pre-setup #20; di spec ini hanya menjadi pengguna target dan sesi aktor tetap Total Control Lina Marlina.
- Data uji: node constraint Finance & Accounting dan descendant Accounts Payable (dalam constraint); node di luar constraint IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa, dan Jakarta Selatan Distribution Center; baris Group Role Manage files; node dicentang Accounts Payable (Assign pada langkah 27 sampai 30).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserHGT` (Pre-setup #51) di hook `before`, untuk memulihkan Gita Permata ke Pre-setup #51 pada langkah 40 dan di hook `after` (grup Accounts Payable pada baris Manage files dihapus); pembacaan jumlah entri `Assign` Object `Group Role` pada Tab Changelog target, Tab System Log aktor, dan Activity Log sebagai baseline sebelum aksi (S-12, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit. Selektor node pohon, status Disabled, dan tooltip disediakan tim FE.
- State global yang diubah: Group Role Gita Permata (Accounts Payable ditambahkan pada baris Manage files, langkah 30); dipulihkan ke Pre-setup #51 lewat seed API pada langkah 40 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script (kunci baru: node Accounts Payable, Region Jawa, Jakarta Selatan Distribution Center, dan penugasan #51).

## Test Steps

### TC-FA-SU-1114: Popup Select Group pada Assign Group Role target ber-constraint: node dalam constraint dapat dipilih, node di luar constraint Disabled dengan tooltip S-45

1. Ketik Search `Gita Permata`, tekan Enter, lalu klik Name `Gita Permata`
2. Klik Tab Role lalu Sub-tab Group Role
3. Klik `[Assign Group]` pada baris Manage files
4. Catat jumlah baris tabel pada popup Assign Group Role sebagai baseline
5. Klik `[+ Assign Group]`
6. Verifikasi Finance & Accounting (node constraint) tidak Disabled dan dapat dicentang
7. Verifikasi Accounts Payable (descendant) tidak Disabled dan dapat dicentang
8. Arahkan kursor ke IT Infrastructure
9. Verifikasi IT Infrastructure tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
10. Arahkan kursor ke Branch Surabaya
11. Verifikasi Branch Surabaya tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
12. Arahkan kursor ke General Affairs
13. Verifikasi General Affairs tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
14. Arahkan kursor ke Logistics Warehouse
15. Verifikasi Logistics Warehouse tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
16. Arahkan kursor ke Region Jawa
17. Verifikasi Region Jawa tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
18. Arahkan kursor ke Jakarta Selatan Distribution Center
19. Verifikasi Jakarta Selatan Distribution Center tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
20. Centang Accounts Payable
21. Klik `[Cancel]` pada popup Select Group
22. Verifikasi popup Select Group tertutup dan popup Assign Group Role tampil kembali
23. Verifikasi tabel popup Assign Group Role memuat jumlah baris yang sama dengan baseline langkah 4 (tidak ada baris bertambah)
24. Klik `[Cancel]` pada popup Assign Group Role

### TC-FA-SU-1115: Assign Group Role ke node dalam constraint pada target ber-constraint: tersimpan dengan toast assigned dan log Assign

25. Catat baseline jumlah entri `Assign` Object `Group Role` Gita Permata pada Tab Changelog target, Tab System Log aktor, dan Activity Log lewat kemampuan baca BE
26. Klik `[Assign Group]` pada baris Manage files
27. Klik `[+ Assign Group]`, centang Accounts Payable, lalu klik `[Select]`
28. Verifikasi Accounts Payable ditambahkan ke tabel popup Assign Group Role
29. Verifikasi pada baris Accounts Payable R tercentang dan Disabled, sedangkan C, U, dan D tidak tercentang
30. Klik `[Save]`
31. Verifikasi popup menutup
32. Verifikasi toast "Success, group role has been assigned." tampil
33. Verifikasi baris Manage files memuat badge Accounts Payable
34. Buka Tab Changelog, Search `Gita Permata`, tekan Enter, lalu muat ulang sampai entri tampil
35. Verifikasi entri `Assign` / Object `Group Role` / Field `Manage files — Accounts Payable` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline langkah 25 pada Tab Changelog
36. Buka Tab System Log aktor dan Search `Gita Permata`, tekan Enter
37. Verifikasi entri `Assign` / Object `Group Role` / Field `Manage files — Accounts Payable` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline langkah 25 pada Tab System Log
38. Buka Activity Log
39. Verifikasi entri `Assign` / Object `Group Role` / Field `Manage files — Accounts Payable` / Old Value `—` / New Value `Assigned` bertambah satu dibanding baseline langkah 25 pada Activity Log
40. Pulihkan Gita Permata ke Pre-setup #51 lewat seed API (Accounts Payable dihapus dari baris Manage files)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 4, 24, 25, 34, 36, 38 dan 40. Search `Gita Permata` pada langkah 1 menemukan baris target (R-16, R-23); Search pada langkah 34 dan 36 adalah pola baca-log. Langkah 24 menutup popup Assign Group Role sebelum TC-FA-SU-1115 membukanya kembali (S-09). Baseline langkah 4 dan 25 mengikuti S-12.
- Verifikasi status node pada langkah 9, 11, 13, 15, 17 dan 19 satu per node memuat tiga sifat yang dinyatakan TC dalam satu butir Expected b: Disabled, tidak dapat dicentang, dan tooltip (elemen "Disabled dengan tooltip", S-01). Hover mendahului tiap asersi tooltip (bagian 8b butir 5). Langkah 6 dan 7 mengasersi Expected a satu per node (tidak Disabled dan dapat dicentang).
- Alasan di atas sekitar 35 langkah (40 nominal, 34 setelah blok baca-log langkah 34 sampai 39 dikeluarkan sesuai bagian 3 prinsip 13): dua TC berbagi aktor, target, dan popup yang sama, tanpa kelas harness. Jumlah langkah dibentuk oleh Expected b yang dipecah satu `Verifikasi` per node (6 node di luar constraint, langkah 8 sampai 19) dan tiga permukaan log (S-01).
- TC-FA-SU-1114 dan TC-FA-SU-1115 hanya di spec ini. Pemilih lain dengan gate yang sama ada di spec 424, 425, dan 426.
- Temuan untuk QA:
  - Copy tooltip S-45 ("This group is outside the user's home group.") masih usulan (NC-27). Spec mengasersi literal TC; ubah bila PM mengganti copy.
  - Seed `FaUserHGT` (Pre-setup #51) wajib disediakan tim FE/BE; kunci fixture baru (node Accounts Payable, Region Jawa, Jakarta Selatan Distribution Center, penugasan #51) dicatat untuk fixture `fixtures/fixed-asset-settings-user.json`.
  - TC-FA-SU-1114 Expected c ("kembali ke popup Assign Group Role tanpa menambah baris") tidak menyebut jumlah baris awal; spec mengasersi dengan baseline jumlah baris tabel popup yang dicatat pada langkah 4.
  - TC-FA-SU-1114 berakhir pada popup Assign Group Role yang masih terbuka; spec menutupnya lewat `[Cancel]` (langkah 24) sebagai langkah penghubung tanpa asersi.
  - TC-FA-SU-1115 Expected a menyebut R tercentang Disabled dan C/U/D tidak tercentang pada baris Accounts Payable tanpa menyebut baris lain; spec mengasersi hanya baris Accounts Payable. Perilaku Save popup Assign Group Role dengan baris Group Role lama di luar constraint tidak ditetapkan PRD dan tidak diasersi.
  - Post Condition TC-FA-SU-1115 (Gita Permata dipulihkan oleh automation baseline) tidak punya langkah observasi dan tidak diasersi.
