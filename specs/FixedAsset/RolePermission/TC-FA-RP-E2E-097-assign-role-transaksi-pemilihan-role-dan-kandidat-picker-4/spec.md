---
id: TC-FA-RP-E2E-097-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-4
title: "Assign Role Transaksi: pemilihan role dan kandidat picker (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1123
  - TC-FA-RP-1124
coverage:
  web: automated
---

# Assign Role Transaksi: pemilihan role dan kandidat picker (4/4)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19 (Nadia Putri Asset Admin, Oscar Pratama Monitoring & Report, Putri Wulandari Staff, Pandu Wijaya Approver pada `IT Infrastructure` sub-tab Disposal), #1 (Admin Utama, Default User; untuk TC-FA-RP-1124 tanpa Home Group lewat seed API sebagai precondition TC, tidak diasersi), dan pool #15 (Ahmad Fauzi sebagai kandidat Standard pembanding). Spec ini hanya membaca picker.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (Home Group Admin Utama (Pre-setup #1)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-1123: Pemegang role lain pada tangga yang sama dan pemegang Approver tetap tampil di picker role tangga

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Ketik Search `Putri Wulandari`, tekan Enter
4. Verifikasi Putri Wulandari ada di daftar picker (Staff)
5. Ganti isi kotak search dengan `Oscar Pratama`, tekan Enter
6. Verifikasi Oscar Pratama ada di daftar picker (Monitoring & Report)
7. Ganti isi kotak search dengan `Pandu Wijaya`, tekan Enter
8. Verifikasi Pandu Wijaya ada di daftar picker (Approver)
9. Ganti isi kotak search dengan `Nadia Putri`, tekan Enter
10. Verifikasi empty state `No results found` tampil sehingga Nadia Putri tidak ada di daftar picker (Asset Admin)
11. Tutup popup Assign
12. Klik `[+ Assign]` pada section Staff
13. Ketik Search `Nadia Putri`, tekan Enter
14. Verifikasi Nadia Putri ada di daftar picker (Asset Admin)
15. Tutup popup Assign
16. Klik `[+ Assign]` pada section Approver
17. Ketik Search `Nadia Putri`, tekan Enter
18. Verifikasi Nadia Putri ada di daftar picker (Asset Admin, role tangga)
19. Ganti isi kotak search dengan `Pandu Wijaya`, tekan Enter
20. Verifikasi empty state `No results found` tampil sehingga Pandu Wijaya tidak ada di daftar picker (Approver)
21. Tutup popup Assign

### TC-FA-RP-1124: Default User tidak muncul di picker Assign Role Transaksi pada keempat role

22. Pulihkan state lewat seed API: Admin Utama (Default User) tanpa Home Group (constraint) sehingga lolos gate Home Group di group mana pun, dan tetap dikecualikan karena Default User
23. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
24. Klik `[+ Assign]` pada section Asset Admin
25. Ketik Search `Admin Utama`, tekan Enter
26. Verifikasi empty state `No results found` tampil sehingga Admin Utama tidak ada di daftar picker (Default User)
27. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
28. Verifikasi Ahmad Fauzi ada di daftar picker
29. Tutup popup Assign
30. Klik `[+ Assign]` pada section Monitoring & Report
31. Ketik Search `Admin Utama`, tekan Enter
32. Verifikasi empty state `No results found` tampil sehingga Admin Utama tidak ada di daftar picker (Default User)
33. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
34. Verifikasi Ahmad Fauzi ada di daftar picker
35. Tutup popup Assign
36. Klik `[+ Assign]` pada section Staff
37. Ketik Search `Admin Utama`, tekan Enter
38. Verifikasi empty state `No results found` tampil sehingga Admin Utama tidak ada di daftar picker (Default User)
39. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
40. Verifikasi Ahmad Fauzi ada di daftar picker
41. Tutup popup Assign
42. Klik `[+ Assign]` pada section Approver
43. Ketik Search `Admin Utama`, tekan Enter
44. Verifikasi empty state `No results found` tampil sehingga Admin Utama tidak ada di daftar picker (Default User)
45. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
46. Verifikasi Ahmad Fauzi ada di daftar picker
47. Tutup popup Assign

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-1123, TC-FA-RP-1124).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; pemulihan state seed (langkah 22); menutup popup Assign antar section (S-09); mencari kandidat satu per satu lewat Search picker untuk menemukan baris target (R-16).
- Asersi absence kandidat memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2); pembanding positif adalah Ahmad Fauzi pada section yang sama (TC-FA-RP-1124) atau kandidat lain yang ada (TC-FA-RP-1123).
- Pembagian TC lintas spec: TC-FA-RP-318 (aktor pemegang Manage user & role) ada di spec 301; TC-FA-RP-317 dan TC-FA-RP-1121 sampai TC-FA-RP-1122 ada di spec 096.
- Temuan untuk QA:
  - TC-FA-RP-1124 menyebut Admin Utama tanpa Home Group (constraint) lewat seed API sehingga lolos gate Home Group di group mana pun dan tetap dikecualikan karena Default User; spec memakai seed itu sebagai precondition dan tidak mengasersinya.
  - TC-FA-RP-1123 Expected c menyebut Nadia Putri "role tangga" sebagai penjelasan; hanya keberadaan di daftar yang diasersi.
- Spec ini 47 langkah, di atas smell 35 langkah. Alasan: dua blok satu kelas pada popup Assign Role Transaksi yang sama, semuanya baca-saja (langkah Search kandidat berulang per baris data, bagian 8b butir 7); tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
