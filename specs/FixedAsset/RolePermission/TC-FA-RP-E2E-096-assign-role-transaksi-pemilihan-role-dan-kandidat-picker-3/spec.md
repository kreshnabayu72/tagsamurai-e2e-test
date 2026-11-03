---
id: TC-FA-RP-E2E-096-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-3
title: "Assign Role Transaksi: pemilihan role dan kandidat picker (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-317
  - TC-FA-RP-319
  - TC-FA-RP-1121
  - TC-FA-RP-1122
coverage:
  web: automated
---

# Assign Role Transaksi: pemilihan role dan kandidat picker (3/4)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19 (Nadia Putri Asset Admin, Oscar Pratama Monitoring & Report, Putri Wulandari Staff, Pandu Wijaya Approver pada `IT Infrastructure` sub-tab Disposal; Nadia Putri tanpa penugasan pada sub-tab Damaged), #3 (Rina Wulandari, Total Control), #12 (Maya Anggraeni, Read Only), dan pool #15 (Ahmad Fauzi). Spec ini hanya membaca picker dan tidak mengubah data.

## Test Steps

### TC-FA-RP-317: Picker Role Transaksi bagi Total Control: aktor dikecualikan, Total Control dan Read Only lain tetap tampil kecuali Approver Read Only

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Ketik Search `Siti Rahmawati`, tekan Enter
4. Verifikasi empty state `No results found` tampil sehingga Siti Rahmawati tidak ada di daftar picker (aktor dikecualikan)
5. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
6. Verifikasi Rina Wulandari ada di daftar picker
7. Ganti isi kotak search dengan `Maya Anggraeni`, tekan Enter
8. Verifikasi Maya Anggraeni ada di daftar picker
9. Tutup popup Assign
10. Klik `[+ Assign]` pada section Approver
11. Ketik Search `Rina Wulandari`, tekan Enter
12. Verifikasi Rina Wulandari ada di daftar picker
13. Ganti isi kotak search dengan `Maya Anggraeni`, tekan Enter
14. Verifikasi empty state `No results found` tampil sehingga Maya Anggraeni tidak ada di daftar picker (Read Only)
15. Tutup popup Assign

### TC-FA-RP-319: Kandidat yang sudah memegang role yang sama pada node dan jenis transaksi yang sama dikecualikan

16. Klik `[+ Assign]` pada section Asset Admin
17. Ketik Search `Nadia Putri`, tekan Enter
18. Verifikasi empty state `No results found` tampil sehingga Nadia Putri tidak ada di daftar picker (sudah Asset Admin pada `IT Infrastructure` sub-tab Disposal)
19. Tutup popup Assign

### TC-FA-RP-1121: Picker mengecualikan user yang sudah memegang role yang sama pada node dan jenis transaksi yang sama

20. Klik `[+ Assign]` pada section Monitoring & Report
21. Ketik Search `Oscar Pratama`, tekan Enter
22. Verifikasi empty state `No results found` tampil sehingga Oscar Pratama tidak ada di daftar picker
23. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
24. Verifikasi Ahmad Fauzi ada di daftar picker
25. Tutup popup Assign
26. Klik `[+ Assign]` pada section Staff
27. Ketik Search `Putri Wulandari`, tekan Enter
28. Verifikasi empty state `No results found` tampil sehingga Putri Wulandari tidak ada di daftar picker
29. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
30. Verifikasi Ahmad Fauzi ada di daftar picker
31. Tutup popup Assign
32. Klik `[+ Assign]` pada section Approver
33. Ketik Search `Pandu Wijaya`, tekan Enter
34. Verifikasi empty state `No results found` tampil sehingga Pandu Wijaya tidak ada di daftar picker (baris assignment manual)
35. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
36. Verifikasi Ahmad Fauzi ada di daftar picker
37. Tutup popup Assign

### TC-FA-RP-1122: Pemegang role yang sama pada jenis transaksi lain di node yang sama tetap tampil di picker

38. Klik `[+ Assign]` pada section Asset Admin
39. Ketik Search `Nadia Putri`, tekan Enter
40. Verifikasi empty state `No results found` tampil sehingga Nadia Putri tidak ada di daftar picker
41. Tutup popup Assign
42. Klik sub-tab `Damaged`
43. Klik `[+ Assign]` pada section Asset Admin
44. Ketik Search `Nadia Putri`, tekan Enter
45. Verifikasi Nadia Putri ada di daftar picker (penugasan Disposal tidak mengecualikan pada jenis transaksi lain)
46. Tutup popup Assign

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-317, TC-FA-RP-319, TC-FA-RP-1121, TC-FA-RP-1122).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; menutup popup Assign antar section dan antar blok (S-09); mencari kandidat satu per satu lewat Search picker untuk menemukan baris target (R-16).
- Asersi absence kandidat memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2); pembanding positif tersedia pada kandidat yang ada (Rina Wulandari, Ahmad Fauzi).
- Temuan untuk QA:
  - TC-FA-RP-1121 menyebut Pandu Wijaya sebagai "baris assignment manual" tanpa menjelaskan pembedanya dengan Approver derivatif; spec mencari Pandu Wijaya sebagai kandidat Approver yang tidak boleh tampil.
  - TC-FA-RP-319 dan TC-FA-RP-1122 bergantung pada penugasan Nadia Putri dari Pre-setup #19; keduanya dibaca tanpa mengubah state.
- Spec ini 46 langkah, di atas smell 35 langkah. Alasan: empat blok satu kelas pada popup Assign Role Transaksi yang sama, semuanya baca-saja (langkah Search kandidat berulang per baris data, bagian 8b butir 7); tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
