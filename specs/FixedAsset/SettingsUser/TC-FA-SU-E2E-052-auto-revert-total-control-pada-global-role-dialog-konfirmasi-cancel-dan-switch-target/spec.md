---
id: TC-FA-SU-E2E-052-auto-revert-total-control-pada-global-role-dialog-konfirmasi-cancel-dan-switch-target
title: "Auto-Revert Total Control pada Global Role: Dialog, Konfirmasi, Cancel, dan Switch Target Bertier"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-173
  - TC-FA-SU-174
  - TC-FA-SU-175
  - TC-FA-SU-177
  - TC-FA-SU-178
coverage:
  web: automated
---

# Auto-Revert Total Control pada Global Role: Dialog, Konfirmasi, Cancel, dan Switch Target Bertier

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun pengamat notifikasi (langkah 48): Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; penugasan #23): target Lina Marlina (Total Control) dengan Global Role Manage accounting ON dan Update tercentang (nilai awal mengikuti TC-FA-SU-175). Seed API memulihkan tier Total Control dan penugasan Lina di hook `before` dan `after` (Catatan TC).
- Baseline log: hook `before` mencatat jumlah entri `Auto-Revert` dan `Edit` Lina di Tab Changelog target, Tab System Log aktor, dan Activity Log (kemampuan baca disediakan tim FE/BE; bagian 8b butir 10). Entri log muncul eventual (NC-03): pemeriksaan memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Kemampuan teknis (disediakan tim FE/BE): pencatat request jaringan halaman untuk memeriksa tidak ada request simpan sebelum konfirmasi; jalur navigasi ke Tab System Log aktor, Activity Log, dan panel notifikasi (tidak disebut TC); seed API untuk memulihkan tier Lina; kemampuan baca BE untuk jumlah notifikasi in-app Lina Marlina (baseline per penerima tepat sebelum pemicu dan pembacaan sesudahnya dari sumber yang sama, bagian 8b butir 10).
- State global dan pemulihan: tier Total Control Lina dilepas oleh blok TC-FA-SU-174 dan dipulihkan lewat seed API di hook `after`; entri `Auto-Revert` dan `Edit` bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-173: Edit Global Role target Total Control menyimpang dari pola baku

1. Ketik Search `Lina Marlina`, tekan Enter di User List, klik nama Lina Marlina, lalu buka Tab Role > Sub-tab Global Role
2. Hapus centang Update pada baris Manage accounting
3. Verifikasi dialog Title `Remove Total Control` dengan Body bullet `• Lina Marlina`, kalimat `This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?`
4. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` (filled danger) pada dialog
5. Verifikasi tidak ada request simpan yang terkirim sebelum konfirmasi
6. Klik `[Cancel]`

### TC-FA-SU-175: Cancel dialog Auto-Revert Total Control

7. Hapus centang Update pada baris Manage accounting
8. Klik `[Cancel]`
9. Verifikasi dialog tertutup
10. Verifikasi checkbox Update baris Manage accounting kembali tercentang
11. Hapus centang Update pada baris Manage accounting
12. Klik `[×]` pada dialog
13. Verifikasi dialog tertutup
14. Verifikasi checkbox Update baris Manage accounting kembali tercentang
15. Verifikasi tidak ada request simpan yang terkirim
16. Verifikasi banner `This user has Total Control access.` tetap tampil
17. Buka Tab Changelog Lina Marlina
18. Verifikasi jumlah entri `Edit` dan `Auto-Revert` Lina di Tab Changelog sama dengan baseline (tidak ada entri log)

### TC-FA-SU-178: Switch Global Role pada target bertier memicu dialog Auto-Revert

19. Buka Tab Role > Sub-tab Global Role Lina Marlina
20. Matikan switch pada baris Manage accounting
21. Verifikasi dialog Auto-Revert Title `Remove Total Control` tampil sebelum perubahan disimpan
22. Klik `[Cancel]`
23. Verifikasi switch Manage accounting kembali ke posisi semula (ON)

### TC-FA-SU-174: Konfirmasi Auto-Revert Total Control

24. Catat jumlah notifikasi in-app view-only Auto-Revert Lina Marlina lewat kemampuan baca BE sebagai baseline
25. Hapus centang Update pada baris Manage accounting
26. Klik `[Remove]`
27. Verifikasi toast "Success, permissions have been updated. Lina Marlina is no longer Total Control."
28. Verifikasi checkbox Update baris Manage accounting tersimpan tidak tercentang
29. Verifikasi banner `This user has Total Control access.` hilang dari Sub-tab Global Role
30. Klik Sub-tab Group Role
31. Verifikasi banner `This user has Total Control access.` hilang dari Sub-tab Group Role
32. Kembali ke User List, ketik Search `Lina Marlina`, tekan Enter
33. Verifikasi badge Role baris Lina Marlina berganti label jumlah role (bukan `Total Control`)
34. Buka Detail Lina Marlina > Tab Changelog, muat ulang sampai entri tampil
35. Verifikasi entri `Auto-Revert` / Object `Total Control` / Field `Access Level` / Old Value `Total Control` / New Value `—` tercatat satu kali di Tab Changelog
36. Verifikasi entri `Edit` untuk permission yang diubah tercatat satu kali di Tab Changelog dengan Modified By `Ahmad D`
37. Buka Tab System Log aktor, muat ulang sampai entri tampil
38. Verifikasi entri `Auto-Revert` dan entri `Edit` Lina tercatat satu kali (selisih 1 dari baseline) di Tab System Log aktor
39. Buka Activity Log, muat ulang sampai entri tampil
40. Verifikasi entri `Auto-Revert` dan entri `Edit` Lina tercatat satu kali (selisih 1 dari baseline) di Activity Log

### TC-FA-SU-177: Auto-Revert tidak mengubah peran individual dan tier tidak kembali

41. Kembali ke User List, ganti isi kotak search dengan `Lina Marlina`, tekan Enter
42. Buka Detail Lina Marlina > Tab Role > Sub-tab Global Role
43. Verifikasi switch Manage accounting tetap ON dan checkbox Update tidak tercentang sesuai hasil edit (peran individual tidak berubah)
44. Centang kembali Update pada baris Manage accounting
45. Verifikasi banner `This user has Total Control access.` tidak muncul kembali
46. Kembali ke User List, ketik Search `Lina Marlina`, tekan Enter
47. Verifikasi badge Role baris Lina Marlina tetap label jumlah role (tier Total Control tidak pulih)

### TC-FA-SU-174 (butir d): Notifikasi in-app diterima target

48. Ganti akun: logout, login sebagai Total Control Lina Marlina (`Spectra.env.FA_TC_PASSWORD`), lalu buka panel notifikasi
49. Verifikasi jumlah notifikasi in-app view-only Auto-Revert Lina Marlina bertambah tepat satu dibanding baseline langkah 24 (dibaca lewat kemampuan baca BE yang sama)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Urutan: TC-FA-SU-174 dikerjakan sesudah TC-FA-SU-173, 175, dan 178 karena TC-FA-SU-174 melepas tier Total Control yang dipakai ketiganya; TC-FA-SU-177 mengikuti TC-FA-SU-174 langsung karena Langkah Uji 1 TC-FA-SU-177 ("Selesaikan Auto-Revert Lina Marlina") dipenuhi oleh langkah 25 sampai 26 (S-04). Butir d TC-FA-SU-174 diasersi di akhir karena membutuhkan ganti akun ke Lina Marlina.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 32, dan 46 (Search untuk menemukan baris target, R-16), langkah 17, 19, 30, 34, 37, 39, dan 42 (membuka sub-tab atau surface log), langkah 48 (ganti akun eksplisit, S-07), langkah 24 (mencatat baseline notifikasi in-app Lina Marlina lewat kemampuan baca BE, bagian 8b butir 10).
- Langkah penghubung Search (R-16, S-03; bagian 8b butir 9 dan 13): langkah 41 mencari baris target dengan nama persis sebelum aksi pada baris itu, tanpa `Verifikasi`; tabel User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman).
- Asersi tambahan di luar Expected TC: langkah 5 dan 15 (tidak ada request simpan) menerjemahkan Expected c TC-FA-SU-173 dan Expected b TC-FA-SU-175; langkah 43 menerjemahkan Expected a TC-FA-SU-177; langkah 47 menerjemahkan Expected b ("tidak memulihkan tier") lewat badge Role di User List.
- Spec ini 49 langkah. Alasan melewati sekitar 35 langkah: seluruh blok satu topik (Auto-Revert Total Control pada target yang sama, Lina Marlina) dengan satu aktor dan satu pembukaan halaman Detail; blok TC-FA-SU-173, 175, dan 178 tidak mengubah state, blok TC-FA-SU-174 dan 177 berurutan karena TC-FA-SU-177 bergantung pada TC-FA-SU-174.
- Temuan untuk QA:
  - Expected c TC-FA-SU-177 ("penetapan kembali tier hanya lewat Settings > Role & Permission") adalah pernyataan aturan tanpa gejala yang dapat diamati di Langkah Uji; tidak diasersi.
  - Post Condition TC-FA-SU-173, 175, 177, dan 178 serta Post Condition TC-FA-SU-174 butir a sampai c tidak punya langkah observasi tersendiri dan tidak diasersi di luar Expected (S-01). Butir d Expected TC-FA-SU-174 membutuhkan sesi Lina Marlina (target); spec memakai ganti akun, bukan konteks kedua.
  - TC-FA-SU-174 Langkah Uji 4 ("buka panel notifikasi sebagai Lina Marlina") tidak menyebut jalur ke panel notifikasi; copy Title dan Body notifikasi dimiliki `fixed-asset/notification` sehingga hanya diasersi bahwa notifikasi diterima (Catatan TC).
  - Expected b TC-FA-SU-174 menyebut "badge Role di User List berganti label jumlah Role" tanpa angka; spec tidak mengasersi angka.
