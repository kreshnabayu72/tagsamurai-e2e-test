---
id: TC-FA-SU-E2E-316-resilience-jaringan-putus-atau-timeout-save-group-role-submit-transaction-role-resend
title: "Resilience Jaringan Putus atau Timeout: Save Group Role, Submit Transaction Role, Resend, dan Select Edit Home Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1013
  - TC-FA-SU-1014
  - TC-FA-SU-1015
  - TC-FA-SU-1016
coverage:
  web: automated
---

# Resilience Jaringan Putus atau Timeout: Save Group Role, Submit Transaction Role, Resend, dan Select Edit Home Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39), layanan terkendali (#37: Hana Kusuma Pending Activation). Target: Wawan Setiawan (Group Role Manage files), Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting), Hana Kusuma, dan Gita Permata (Home Group Finance & Accounting).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): `Spectra.intercept()` atas respons HTTP (network error tanpa respons) yang dilepas segera setelah pemicu (S-09); kegagalan dipicu di atas backend nyata sehingga spec tetap FE+BE (bagian 6).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum aksi (baseline, S-12) dan sesudah aksi; audit trail permanen sehingga asersi memakai selisih terhadap baseline. Log yang eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan status aktif, penugasan peran, dan Home Group pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC; dijalankan sebagai langkah penghubung dan di hook `after` (cadangan).
- Mail-catcher dengan baseline jumlah email per alamat (R-11, S-12) untuk Hana Kusuma (disediakan tim FE). Jam server dan jam browser diatur bersama: precondition cooldown Resend Hana Kusuma belum berjalan dipenuhi di hook `before` dengan jam, dan hook `after` memajukan jam 61 detik lalu memulihkannya supaya cooldown yang dimulai langkah 33 tidak terbawa ke spec lain (R-10).
- State global dan pemulihan: intercept dilepas segera setelah pemicu tiap blok; data Pre-setup dipulihkan lewat seed API pada langkah penghubung terakhir dan di hook `after`; jam server dan jam browser dimajukan di hook `after` lalu dipulihkan. Efek pada Pre-setup: Last Updated dan Modified By Wawan Setiawan, Mira Anggraini, dan Gita Permata berubah, satu email Resend terkirim ke Hana Kusuma, dan entri log permanen bertambah dari aksi ulang yang berhasil. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1013: Jaringan putus saat Save popup Assign Group Role

1. Ketik Search `Wawan`, tekan Enter, klik nama Wawan Setiawan, lalu buka Tab Role > Sub-tab Group Role
2. Catat jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
3. Buka popup Assign Group Role Manage files dan centang Delete pada Branch Surabaya
4. Pasang `Spectra.intercept()` pada request Save Group Role menjadi network error (drop) tanpa respons
5. Klik `[Save]`
6. Lepas intercept (koneksi dipulihkan)
7. Verifikasi popup Assign Group Role tetap terbuka
8. Verifikasi centang Delete pada Branch Surabaya dipertahankan
9. Verifikasi toast error "Error, failed to save group role."
10. Verifikasi jumlah entri log pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sama dengan baseline
11. Klik `[Save]` (ulangi aksi)
12. Verifikasi aksi berhasil dicoba ulang: popup tertutup dan Delete pada Branch Surabaya tersimpan pada Sub-tab Group Role

### TC-FA-SU-1014: Jaringan putus saat Submit modal Assign Transaction Role

13. Kembali ke User List, ketik Search `Mira`, tekan Enter, klik nama Mira Anggraini, lalu buka Tab Role > Sub-tab Transaction Role
14. Catat jumlah entri log pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sebagai baseline
15. Klik `[+ Assign]` dan isi Transfer × Asset Admin pada Finance & Accounting
16. Pasang `Spectra.intercept()` pada request Submit Transaction Role menjadi network error (drop) tanpa respons
17. Klik `[Submit]`
18. Lepas intercept (koneksi dipulihkan)
19. Verifikasi modal Assign Transaction Role tetap terbuka
20. Verifikasi isian Transfer × Asset Admin pada Finance & Accounting dipertahankan
21. Verifikasi toast error "Error, failed to assign Asset Admin."
22. Verifikasi jumlah entri log pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sama dengan baseline
23. Klik `[Submit]` (ulangi aksi)
24. Verifikasi aksi berhasil dicoba ulang: baris Transfer × Asset Admin pada Finance & Accounting tampil pada Sub-tab Transaction Role

### TC-FA-SU-1015: Jaringan putus saat Resend Activation Email

25. Kembali ke User List
26. Catat jumlah entri log pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log serta jumlah email yang diterima Hana Kusuma di mail-catcher sebagai baseline
27. Pasang `Spectra.intercept()` pada request Resend menjadi network error (drop) tanpa respons
28. Klik `⋯` pada baris Hana Kusuma lalu Resend Activation Email
29. Lepas intercept (koneksi dipulihkan)
30. Verifikasi toast error "Error, failed to send activation email to Hana Kusuma."
31. Verifikasi tombol Resend kembali Enabled tanpa cooldown
32. Verifikasi jumlah entri log pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log sama dengan baseline
33. Klik `⋯` pada baris Hana Kusuma lalu Resend Activation Email (ulangi aksi)
34. Verifikasi aksi berhasil dicoba ulang: jumlah email yang diterima Hana Kusuma bertambah satu dari baseline

### TC-FA-SU-1016: Jaringan putus saat Select Edit Home Group

35. Catat jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
36. Buka popup Edit Home Group Gita Permata dan pilih IT Infrastructure
37. Pasang `Spectra.intercept()` pada request Select Edit Home Group menjadi network error (drop) tanpa respons
38. Klik `[Select]`
39. Lepas intercept (koneksi dipulihkan)
40. Verifikasi Home Group Gita Permata pada tabel kembali ke nilai server (Finance & Accounting)
41. Verifikasi toast error "Error, failed to update home group."
42. Verifikasi jumlah entri log pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sama dengan baseline
43. Buka popup Edit Home Group Gita Permata, pilih IT Infrastructure, lalu klik `[Select]` (ulangi aksi)
44. Verifikasi aksi berhasil dicoba ulang: Home Group Gita Permata pada tabel menjadi IT Infrastructure
45. Pulihkan Wawan Setiawan (Group Role Manage files), Mira Anggraini (Transaction Role), dan Home Group Gita Permata ke Pre-setup lewat seed API

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Intercept dipasang sebelum aksi dan dilepas segera sesudah klik pemicu (S-09); toast dan rollback dibaca sesudah koneksi pulih. Langkah "ulangi aksi" TC sumber ditulis sebagai aksi dan `Verifikasi` hasilnya (Expected c).
- Expected "tidak ada entri log" pada aksi yang gagal ditulis sebagai asersi jumlah dengan baseline di spec fungsional (bagian 3, asersi jumlah bukan kelas g).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 2, 13, 14, 25, 26, 35, 45.
- Spec ini 45 langkah (di atas smell 35 langkah, dihitung dengan ekspansi). Alasan: seluruh blok satu kelas harness (fault injection, kelas b), berdiri sendiri, dan memakai pengguna target sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; setiap blok mengulang pola yang sama (baseline, intercept, aksi, toast, rollback, jumlah entri, ulangi aksi).
- Temuan untuk QA:
  - TC-FA-SU-1014 tidak menyebut pengguna target modal Assign; spec memakai Mira Anggraini (Pre-setup #39 memuat Disposal × Staff, sehingga Transfer × Asset Admin pada Finance & Accounting adalah baris baru).
  - TC-FA-SU-1013 tidak menyebut apakah popup tetap terbuka sesudah aksi diulang berhasil; spec mengasersi popup tertutup dan hasil tersimpan.
  - Post Condition keempat TC ("Tidak ada perubahan tersimpan...") bertentangan dengan Langkah 3 yang mengulang aksi hingga berhasil; spec mengasersi keadaan tepat sesudah kegagalan (Expected a dan b) dan hasil ulangi aksi (Expected c).
  - Expected a TC-FA-SU-1015 "Tombol Resend kembali Enabled tanpa cooldown" dan precondition cooldown belum berjalan bergantung pada jam; kemampuan pengaturan jam disediakan tim FE.
