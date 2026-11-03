---
id: TC-FA-RP-E2E-100-role-transaksi-node-exact-sub-tab-dan-remove-1
title: "Role Transaksi: node exact, sub-tab, dan Remove (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-326
  - TC-FA-RP-327
  - TC-FA-RP-328
  - TC-FA-RP-329
coverage:
  web: automated
---

# Role Transaksi: node exact, sub-tab, dan Remove (1/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19 (Nadia Putri Asset Admin, Oscar Pratama Monitoring & Report, Putri Wulandari Staff, Pandu Wijaya Approver pada `IT Infrastructure` sub-tab Disposal; `Data Center` dan `Helpdesk` tanpa penugasan). Aksi tulis spec ini hanya Remove Nadia Putri pada langkah akhir.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Asset Admin Nadia Putri pada `IT Infrastructure` sub-tab `Disposal`), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-326: Penugasan berlaku pada exact node dan tidak diwariskan ke descendant atau sibling

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Verifikasi Nadia Putri tampil sebagai Asset Admin pada node `IT Infrastructure`
3. Klik node `Data Center` di Sidebar Group Tree
4. Verifikasi section Asset Admin pada node `Data Center` menampilkan empty state `No Asset Admin assigned`
5. Klik node `Helpdesk` di Sidebar Group Tree
6. Verifikasi section Asset Admin pada node `Helpdesk` menampilkan empty state `No Asset Admin assigned`

### TC-FA-RP-327: Penugasan pada satu sub-tab tidak muncul di sub-tab lain pada node yang sama

7. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
8. Klik sub-tab `Damaged`
9. Verifikasi sub-tab `Damaged` termuat: section Asset Admin tampil
10. Verifikasi section Asset Admin sub-tab `Damaged` pada `IT Infrastructure` tidak memuat Nadia Putri (penugasan Disposal)

### TC-FA-RP-328: Dialog Remove Role Transaksi: judul per role dan copy

11. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
12. Klik `[⋯]` baris Pandu Wijaya (Approver) lalu `Remove`
13. Verifikasi dialog severity danger: Title `Remove Approver`; Body `• Pandu W` diikuti `This user will no longer be assigned to this role for IT Infrastructure.`; tombol `[Cancel]` dan `[Remove]`
14. Klik `[Cancel]`
15. Verifikasi dialog tertutup tanpa perubahan: baris Pandu Wijaya tetap ada
16. Klik `[⋯]` baris Nadia Putri (Asset Admin) lalu `Remove`
17. Verifikasi dialog severity danger: Title `Remove Asset Admin`; Body `• Nadia P` diikuti `This user will no longer be assigned to this role for IT Infrastructure.`; tombol `[Cancel]` dan `[Remove]`
18. Klik `[Cancel]`
19. Verifikasi dialog tertutup tanpa perubahan: baris Nadia Putri tetap ada
20. Klik `[⋯]` baris Oscar Pratama (Monitoring & Report) lalu `Remove`
21. Verifikasi dialog severity danger: Title `Remove Monitoring & Report`; Body `• Oscar P` diikuti `This user will no longer be assigned to this role for IT Infrastructure.`; tombol `[Cancel]` dan `[Remove]`
22. Klik `[Cancel]`
23. Verifikasi dialog tertutup tanpa perubahan: baris Oscar Pratama tetap ada
24. Klik `[⋯]` baris Putri Wulandari (Staff) lalu `Remove`
25. Verifikasi dialog severity danger: Title `Remove Staff`; Body `• Putri W` diikuti `This user will no longer be assigned to this role for IT Infrastructure.`; tombol `[Cancel]` dan `[Remove]`
26. Klik `[Cancel]`
27. Verifikasi dialog tertutup tanpa perubahan: baris Putri Wulandari tetap ada

### TC-FA-RP-329: Confirm Remove Asset Admin: baris dihapus dan toast sukses

28. Klik `[⋯]` baris Nadia Putri lalu `Remove`
29. Klik `[Remove]`
30. Verifikasi muncul toast sukses: `Success, Asset Admin has been removed.`
31. Verifikasi baris Nadia Putri hilang dari section Asset Admin

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-326, TC-FA-RP-327, TC-FA-RP-328, TC-FA-RP-329).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; dialog Remove tiap role dibatalkan dengan `[Cancel]` sebelum role berikutnya (S-09). Asersi hanya-baca (TC-FA-RP-326, TC-FA-RP-327, dan TC-FA-RP-328) diletakkan sebelum aksi Remove (TC-FA-RP-329) yang menghapus data di akhir (S-10).
- Asersi tambahan yang tidak ada di TC: `Verifikasi` sub-tab `Damaged` termuat dan section Asset Admin tampil (langkah 9) sebagai anchor positif untuk asersi absence Nadia Putri (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition TC-FA-RP-329 (log `Remove` tercatat, lihat Section 5) tidak memuat langkah observasi dan tidak diasersi (S-01).
  - TC-FA-RP-328 Expected c menyebut Cancel menutup dialog tanpa perubahan; spec mengasersi dialog tertutup dan baris tetap ada pada tiap role.
