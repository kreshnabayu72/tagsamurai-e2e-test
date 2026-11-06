---
id: TC-FA-RP-E2E-094-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-1
title: "Assign Role Transaksi: pemilihan role dan kandidat picker (1/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-308
  - TC-FA-RP-309
  - TC-FA-RP-310
  - TC-FA-RP-311
  - TC-FA-RP-312
coverage:
  web: automated
---

# Assign Role Transaksi: pemilihan role dan kandidat picker (1/4)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18 (pohon Group), #19 (Seed Role Transaksi `IT Infrastructure` sub-tab Disposal; `Data Center` tanpa baris penugasan manual tetapi tercakup penugasan `IT Infrastructure`), #17 (Gunawan Halim, Home Group `Data Center`, Active, Activated), dan pool #15 (Ahmad Fauzi, Budi Santoso, Dimas Pranata).
- State awal per blok (seed API, disediakan tim FE/BE): Gunawan Halim tanpa role Role Transaksi pada node `Data Center` sub-tab `Disposal` untuk TC-FA-RP-308 sampai TC-FA-RP-311 (dipulihkan lewat langkah 7, 14, dan 21 karena Assign sebelumnya memberi Gunawan Halim role tangga yang akan memicu dialog turun tangga); Ahmad Fauzi, Budi Santoso, dan Dimas Pranata tanpa role pada `IT Infrastructure` untuk TC-FA-RP-312.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Role Transaksi pada `Data Center` dan `IT Infrastructure` sub-tab `Disposal` (Pre-setup #19)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-308: Assign Asset Admin ke satu user pada node `Data Center` sub-tab Disposal

1. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Centang Gunawan Halim, lalu klik `[Assign]`
4. Verifikasi muncul toast sukses: `Success, Asset Admin has been assigned.`
5. Verifikasi baris Gunawan Halim tampil pada tabel section Asset Admin dengan Position dan Division terisi
6. Verifikasi section role lain pada node `Data Center` tidak berubah: tetap tanpa penugasan

### TC-FA-RP-309: Assign Monitoring & Report ke satu user pada node `Data Center` sub-tab Disposal

7. Pulihkan state lewat seed API: lepas penugasan Gunawan Halim pada node `Data Center` sub-tab `Disposal`, lalu muat ulang halaman
8. Klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
9. Klik `[+ Assign]` pada section Monitoring & Report
10. Centang Gunawan Halim, lalu klik `[Assign]`
11. Verifikasi muncul toast sukses: `Success, Monitoring & Report has been assigned.`
12. Verifikasi baris Gunawan Halim tampil pada tabel section Monitoring & Report dengan Position dan Division terisi
13. Verifikasi section role lain pada node `Data Center` tidak berubah: tetap tanpa penugasan

### TC-FA-RP-310: Assign Staff ke satu user pada node `Data Center` sub-tab Disposal

14. Pulihkan state lewat seed API: lepas penugasan Gunawan Halim pada node `Data Center` sub-tab `Disposal`, lalu muat ulang halaman
15. Klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
16. Klik `[+ Assign]` pada section Staff
17. Centang Gunawan Halim, lalu klik `[Assign]`
18. Verifikasi muncul toast sukses: `Success, Staff has been assigned.`
19. Verifikasi baris Gunawan Halim tampil pada tabel section Staff dengan Position dan Division terisi
20. Verifikasi section role lain pada node `Data Center` tidak berubah: tetap tanpa penugasan

### TC-FA-RP-311: Assign Approver ke satu user pada node `Data Center` sub-tab Disposal

21. Pulihkan state lewat seed API: lepas penugasan Gunawan Halim pada node `Data Center` sub-tab `Disposal`, lalu muat ulang halaman
22. Klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
23. Klik `[+ Assign]` pada section Approver
24. Centang Gunawan Halim, lalu klik `[Assign]`
25. Verifikasi muncul toast sukses: `Success, Approver has been assigned.`
26. Verifikasi baris Gunawan Halim tampil pada tabel section Approver dengan Position dan Division terisi
27. Verifikasi section role lain pada node `Data Center` tidak berubah: tetap tanpa penugasan

### TC-FA-RP-312: Assign tiga user ke Approver menghasilkan satu toast tunggal

28. Tunggu toast lama hilang otomatis
29. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
30. Klik `[+ Assign]` pada section Approver
31. Centang Ahmad Fauzi, Budi Santoso, dan Dimas Pranata, lalu klik `[Assign]`
32. Verifikasi muncul satu toast sukses: `Success, Approver has been assigned.`
33. Verifikasi ketiga baris tampil pada section Approver

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-308, TC-FA-RP-309, TC-FA-RP-310, TC-FA-RP-311, TC-FA-RP-312).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; pemulihan state seed antar blok (langkah 7, 14, 21); "Tunggu toast lama hilang otomatis" sebelum asersi hitungan toast tunggal (R-12).
- Pola toast PRD `Success, [Role Name] has been assigned.` pada Expected d TC-FA-RP-308 adalah penjelasan pola, bukan klausa terpisah; toast tiap role diasersi pada masing-masing blok.
- "Section role lain tidak berubah" diasersi sebagai section lain tetap tanpa penugasan, berdasarkan Pre-setup #19 (`Data Center` tanpa baris penugasan manual; baris hanya literal pada node penugasan).
- Urutan blok TC-FA-RP-308 sampai TC-FA-RP-311 mengikuti nomor TC; pemulihan antar blok mencegah dialog turun tangga ketika Gunawan Halim sudah memegang role tangga.
- Temuan untuk QA:
  - Post Condition TC-FA-RP-308 sampai TC-FA-RP-311 (penugasan mencakup node `Data Center` beserta descendant `Rack A1` secara query-time, baris hanya tampil pada node `Data Center`; log `Assign` tercatat) tidak memuat langkah observasi dan tidak diasersi (S-01).
  - TC-FA-RP-308 sampai TC-FA-RP-311 tidak menyebut hasil tangga ketika Gunawan Halim sudah memegang role lain; spec memulihkan state antar blok.
  - TC-FA-RP-312 tidak menyebut apakah ketiga user sudah memegang role pada node tersebut; spec mengasumsikan tanpa role.
