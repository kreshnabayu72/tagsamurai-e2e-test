---
id: TC-FA-RP-E2E-095-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-2
title: "Assign Role Transaksi: pemilihan role dan kandidat picker (2/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-313
  - TC-FA-RP-314
  - TC-FA-RP-315
  - TC-FA-RP-316
coverage:
  web: automated
---

# Assign Role Transaksi: pemilihan role dan kandidat picker (2/4)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19, #17 (Gunawan Halim Home Group `Data Center`, Joko Santoso Home Group `IT Infrastructure`, Hesti Rahma Home Group `Logistics Warehouse`, Indra Kusuma tanpa Home Group; semuanya Active, Activated), #16 (Siti Rahayu Inactive, Eka Saputra Pending Activation, Fitri Handayani Pending Email Confirmation), #12 (Maya Anggraeni, Read Only), dan pool #15 (Ahmad Fauzi). Pada TC-FA-RP-316 ketiga user #16 ditugaskan sebagai Staff `IT Infrastructure` sub-tab `Disposal` (satu-satunya aksi tulis spec ini).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Staff pada `IT Infrastructure` sub-tab `Disposal` (Siti Rahayu, Eka Saputra, Fitri Handayani dilepas)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-313: Kandidat Role Transaksi harus terafiliasi group: node Data Center

1. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Ketik Search `Gunawan Halim`, tekan Enter
4. Verifikasi Gunawan Halim ada di daftar picker (Home Group sama dengan node)
5. Ganti isi kotak search dengan `Indra Kusuma`, tekan Enter
6. Verifikasi Indra Kusuma ada di daftar picker (tanpa Home Group memenuhi syarat di group mana pun)
7. Ganti isi kotak search dengan `Joko Santoso`, tekan Enter
8. Verifikasi empty state `No results found` tampil sehingga Joko Santoso tidak ada di daftar picker (Home Group `IT Infrastructure` adalah ancestor, bukan node atau descendant)
9. Ganti isi kotak search dengan `Hesti Rahma`, tekan Enter
10. Verifikasi empty state `No results found` tampil sehingga Hesti Rahma tidak ada di daftar picker
11. Tutup popup Assign

### TC-FA-RP-314: Kandidat Role Transaksi harus terafiliasi group: node IT Infrastructure mencakup descendant

12. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
13. Klik `[+ Assign]` pada section Asset Admin
14. Ketik Search `Gunawan Halim`, tekan Enter
15. Verifikasi Gunawan Halim ada di daftar picker (Home Group `Data Center` adalah descendant dari node)
16. Ganti isi kotak search dengan `Joko Santoso`, tekan Enter
17. Verifikasi Joko Santoso ada di daftar picker
18. Ganti isi kotak search dengan `Hesti Rahma`, tekan Enter
19. Verifikasi empty state `No results found` tampil sehingga Hesti Rahma tidak ada di daftar picker
20. Tutup popup Assign

### TC-FA-RP-315: Picker Approver menolak user bukan Active dan Activated serta Read Only

21. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
22. Klik `[+ Assign]` pada section Approver
23. Ketik Search `Siti Rahayu`, tekan Enter
24. Verifikasi empty state `No results found` tampil sehingga Siti Rahayu tidak ada di daftar picker (Inactive)
25. Ganti isi kotak search dengan `Eka Saputra`, tekan Enter
26. Verifikasi empty state `No results found` tampil sehingga Eka Saputra tidak ada di daftar picker (Pending Activation)
27. Ganti isi kotak search dengan `Fitri Handayani`, tekan Enter
28. Verifikasi empty state `No results found` tampil sehingga Fitri Handayani tidak ada di daftar picker (Pending Email Confirmation)
29. Ganti isi kotak search dengan `Maya Anggraeni`, tekan Enter
30. Verifikasi empty state `No results found` tampil sehingga Maya Anggraeni tidak ada di daftar picker (Read Only)
31. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
32. Verifikasi Ahmad Fauzi ada di daftar picker (Active, Activated)
33. Tutup popup Assign

### TC-FA-RP-316: Picker Asset Admin, Monitoring & Report, dan Staff menerima Status dan Activation Status apa pun

34. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
35. Klik `[+ Assign]` pada section Staff
36. Ketik Search `Siti Rahayu`, tekan Enter
37. Verifikasi Siti Rahayu ada di daftar picker
38. Centang Siti Rahayu
39. Ganti isi kotak search dengan `Eka Saputra`, tekan Enter
40. Verifikasi Eka Saputra ada di daftar picker
41. Centang Eka Saputra
42. Ganti isi kotak search dengan `Fitri Handayani`, tekan Enter
43. Verifikasi Fitri Handayani ada di daftar picker
44. Centang Fitri Handayani
45. Klik `[Assign]`
46. Verifikasi muncul toast sukses: `Success, Staff has been assigned.`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-313, TC-FA-RP-314, TC-FA-RP-315, TC-FA-RP-316).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; menutup popup Assign antar blok (S-09); mencari kandidat satu per satu lewat Search picker untuk menemukan baris target (R-16).
- Asersi absence kandidat memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2); ketiga TC absence kandidat (TC-FA-RP-313, TC-FA-RP-314, TC-FA-RP-315) tidak punya aksi tulis.
- Temuan untuk QA:
  - TC-FA-RP-316 pada langkah uji ketiga mencentang tiga user tanpa Search; spec mencari tiap user lewat Search picker lalu mencentangnya. Bila seleksi tidak bertahan antar Search, langkah uji itu menjadi ambigu (S-15).
  - TC-FA-RP-316 tidak menyebut aksi atas Asset Admin dan Monitoring & Report padahal skenario menyebut ketiganya; spec mengikuti langkah TC yang hanya memakai section Staff.
  - TC-FA-RP-313 Expected b menyebut Indra Kusuma "memenuhi syarat di group mana pun"; asersi hanya keberadaannya di daftar.
- Spec ini 46 langkah, di atas smell 35 langkah. Alasan: empat blok satu kelas pada popup Assign Role Transaksi yang sama (langkah Search kandidat berulang per baris data, bagian 8b butir 7); tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
