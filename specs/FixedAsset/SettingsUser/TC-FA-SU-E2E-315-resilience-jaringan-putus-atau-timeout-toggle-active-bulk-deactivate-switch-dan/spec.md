---
id: TC-FA-SU-E2E-315-resilience-jaringan-putus-atau-timeout-toggle-active-bulk-deactivate-switch-dan
title: "Resilience Jaringan Putus atau Timeout: Toggle Active, Bulk Deactivate, Switch dan Checkbox Global Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1009
  - TC-FA-SU-1010
  - TC-FA-SU-1011
  - TC-FA-SU-1012
coverage:
  web: automated
---

# Resilience Jaringan Putus atau Timeout: Toggle Active, Bulk Deactivate, Switch dan Checkbox Global Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39).
- Pengguna milik spec (target aksi tulis; dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan; disediakan tim FE):
  - `Gita Permata {runId}-315`, email `gita.permata+{runId}-315@qwertysystem.net`: Active; Global Role Manage accounting dengan Create dan Read tercentang; switch Manage asset ID configuration OFF.
  - `Nanda Pratama {runId}-315`, email `nanda.pratama+{runId}-315@qwertysystem.net`: Active.
  - `Putri Anggraeni {runId}-315`, email `putri.anggraeni+{runId}-315@qwertysystem.net`: Active.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): `Spectra.intercept()` atas respons HTTP (network error tanpa respons) yang dilepas segera setelah pemicu (S-09); kegagalan dipicu di atas backend nyata sehingga spec tetap FE+BE (bagian 6).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum aksi (baseline, S-12) dan sesudah aksi; audit trail permanen sehingga asersi memakai selisih terhadap baseline. Log yang eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- State global dan pemulihan: intercept dilepas segera setelah pemicu tiap blok; ketiga pengguna milik spec dihapus di hook `after`. Efek pada Pre-setup: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1011: Jaringan putus saat switch Global Role

1. Ketik Search `Gita Permata {runId}-315`, tekan Enter, klik nama Gita Permata {runId}-315, lalu buka Tab Role > Sub-tab Global Role
2. Catat jumlah entri log pada Tab Changelog Gita Permata {runId}-315, Tab System Log aktor, dan Activity Log sebagai baseline
3. Pasang `Spectra.intercept()` pada request ubah switch Global Role menjadi network error (drop) tanpa respons
4. Nyalakan switch Manage asset ID configuration
5. Lepas intercept (koneksi dipulihkan)
6. Verifikasi toast error "Error, failed to update role."
7. Verifikasi switch Manage asset ID configuration rollback ke posisi awal (OFF)
8. Verifikasi jumlah entri log pada Tab Changelog Gita Permata {runId}-315, Tab System Log aktor, dan Activity Log sama dengan baseline
9. Nyalakan kembali switch Manage asset ID configuration (ulangi aksi)
10. Verifikasi aksi berhasil dicoba ulang: switch Manage asset ID configuration ON

### TC-FA-SU-1012: Jaringan putus saat checkbox CRUD Global Role

11. Catat jumlah entri log pada Tab Changelog Gita Permata {runId}-315, Tab System Log aktor, dan Activity Log sebagai baseline
12. Pasang `Spectra.intercept()` pada request ubah checkbox CRUD Global Role menjadi network error (drop) tanpa respons
13. Centang Update pada Manage accounting
14. Lepas intercept (koneksi dipulihkan)
15. Verifikasi toast error "Error, failed to update permissions."
16. Verifikasi checkbox Update Manage accounting rollback ke nilai sebelum klik (tidak tercentang)
17. Verifikasi jumlah entri log pada Tab Changelog Gita Permata {runId}-315, Tab System Log aktor, dan Activity Log sama dengan baseline
18. Centang kembali Update pada Manage accounting (ulangi aksi)
19. Verifikasi aksi berhasil dicoba ulang: checkbox Update Manage accounting tercentang

### TC-FA-SU-1010: Jaringan putus saat Bulk Deactivate

20. Kembali ke User List, Ketik Search `{runId}-315`, tekan Enter, lalu centang dua pengguna Active (Nanda Pratama {runId}-315 dan Putri Anggraeni {runId}-315)
21. Catat jumlah entri log pada Tab Changelog Nanda Pratama {runId}-315 dan Putri Anggraeni {runId}-315, Tab System Log aktor, dan Activity Log sebagai baseline
22. Pasang `Spectra.intercept()` pada request Bulk Deactivate menjadi network error (drop) tanpa respons
23. Klik Bulk Action > `[Deactivate]`, lalu klik `[Deactivate]` pada dialog
24. Lepas intercept (koneksi dipulihkan)
25. Verifikasi toast error tampil
26. Verifikasi seleksi dua baris dipertahankan pada Bulk Actions Bar
27. Verifikasi status Nanda Pratama {runId}-315 dan Putri Anggraeni {runId}-315 tetap Active
28. Verifikasi jumlah entri log pada Tab Changelog Nanda Pratama {runId}-315 dan Putri Anggraeni {runId}-315, Tab System Log aktor, dan Activity Log sama dengan baseline
29. Klik Bulk Action > `[Deactivate]`, lalu klik `[Deactivate]` pada dialog (ulangi aksi)
30. Verifikasi aksi berhasil dicoba ulang: Nanda Pratama {runId}-315 dan Putri Anggraeni {runId}-315 berstatus Inactive
31. Ketik Search `Gita Permata {runId}-315`, tekan Enter

### TC-FA-SU-1009: Jaringan putus saat Toggle Active single

32. Catat jumlah entri log pada Tab Changelog Gita Permata {runId}-315, Tab System Log aktor, dan Activity Log sebagai baseline
33. Pasang `Spectra.intercept()` pada request ubah status aktif menjadi network error (drop) tanpa respons
34. Klik sakelar Active baris Gita Permata {runId}-315, lalu klik `[Deactivate]`
35. Lepas intercept (koneksi dipulihkan)
36. Verifikasi toast error "Error, failed to deactivate user."
37. Verifikasi sakelar Active baris Gita Permata {runId}-315 kembali ke posisi awal (ON)
38. Verifikasi jumlah entri log pada Tab Changelog Gita Permata {runId}-315, Tab System Log aktor, dan Activity Log sama dengan baseline
39. Klik sakelar Active baris Gita Permata {runId}-315, lalu klik `[Deactivate]` (ulangi aksi)
40. Verifikasi aksi berhasil dicoba ulang: Gita Permata {runId}-315 berstatus Inactive

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah (TC-FA-SU-1011, 1012, 1010, 1009) supaya aksi ulang yang berhasil pada Gita Permata tidak menghalangi blok berikutnya: Deactivate Gita (TC-FA-SU-1009) dijalankan terakhir.
- Intercept dipasang sebelum aksi dan dilepas segera sesudah klik pemicu (S-09), sehingga asersi toast dan rollback dibaca sesudah koneksi pulih. Langkah "ulangi aksi" TC sumber ditulis sebagai aksi dan `Verifikasi` hasilnya (Expected c).
- TC-FA-SU-1009 sampai 1012 Expected "tidak ada entri log" pada aksi yang gagal ditulis sebagai asersi jumlah dengan baseline di spec fungsional (bagian 3, asersi jumlah bukan kelas g).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 2, 11, 21, 31, 32. Langkah 1, 20, dan 31 juga Search untuk menemukan baris target milik spec (R-16).
- Spec ini 40 langkah (di atas smell 35 langkah, dihitung dengan ekspansi). Alasan: seluruh blok satu kelas harness (fault injection, kelas b) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Setiap blok mengulang pola yang sama (baseline, intercept, aksi, toast, rollback, jumlah entri, ulangi aksi).
- Temuan untuk QA:
  - Expected a TC-FA-SU-1010 menulis "Dialog tetap terbuka (atau seleksi dipertahankan)" dan tidak menyebut teks toast error; spec mengasersi seleksi dipertahankan dan toast error tanpa teks.
  - TC-FA-SU-1010 tidak menyebut pengguna yang dicentang; spec memakai Nanda Pratama dan Putri Anggraeni (Active, tidak dipakai blok lain).
  - Langkah Uji 1 keempat TC menyebut "Intercept request aksi menjadi network error (drop)" dan Langkah 3 "Pulihkan koneksi dan ulangi aksi" tanpa menyebut kapan toast diamati; spec mengamati toast sesudah koneksi dipulihkan.
  - Post Condition keempat TC ("Tidak ada perubahan tersimpan...") bertentangan dengan Langkah 3 yang mengulang aksi hingga berhasil; spec mengasersi keadaan tepat sesudah kegagalan (Expected a dan b) dan hasil ulangi aksi (Expected c).
