---
id: TC-FA-SU-E2E-075-turun-tangga-dialog-change-transaction-role-konfirmasi-atomik-dan-cancel
title: "Turun Tangga: Dialog Change Transaction Role, Konfirmasi Atomik, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-247
  - TC-FA-SU-248
  - TC-FA-SU-249
coverage:
  web: automated
---

# Turun Tangga: Dialog Change Transaction Role, Konfirmasi Atomik, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini; Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting.
- Data uji: turun tangga Disposal dari Staff ke Monitoring & Report pada Finance & Accounting (TC-FA-SU-247); Finance & Accounting (turun) dan IT Infrastructure (baru) pada TC-FA-SU-248 dan 249.
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini ke Pre-setup #39 (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini (Disposal beralih ke Monitoring & Report dan IT Infrastructure ditambahkan oleh TC-FA-SU-248); dipulihkan ke Pre-setup #39 lewat seed API di hook `after`.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Mira Anggraini (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node IT Infrastructure (langkah 10 dan 19) tidak Disabled oleh gate Home Group constraint; Home Group Mira Anggraini dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-247: Turun tangga (Staff ke Monitoring & Report): dialog Change Transaction Role sebelum tersimpan

1. Ketik Search `Mira Anggraini`, tekan Enter, lalu buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting, Transaction Disposal, dan Role Monitoring & Report
2. Klik `[Submit]`
3. Verifikasi dialog Title `Change Transaction Role` dengan Body bullet `• Mira Anggraini`, kalimat `This will change their role for Disposal to Monitoring & Report in:`, dan bullet `• Finance & Accounting (currently Staff)`
4. Verifikasi dialog ditutup dengan pertanyaan `Are you sure you want to change it?`
5. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Change]` (severity warning)
6. Verifikasi dialog muncul karena penurunan pada node yang sama saja (Finance & Accounting) dan tidak memuat bullet node lain (penugasan di ancestor atau descendant tidak memicunya; pemicu ancestor dan descendant diuji pada TC-FA-SU-1108 dan TC-FA-SU-1105)
7. Verifikasi belum ada toast tersimpan saat dialog tampil (tidak ada perubahan tersimpan sebelum konfirmasi)
8. Klik `[Cancel]` pada dialog

### TC-FA-SU-249: Cancel dialog turun tangga membatalkan seluruh Save termasuk grup yang tidak bermasalah

9. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
10. Klik `[+ Assign]` lalu pilih Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, dan Role Monitoring & Report
11. Klik `[Submit]`
12. Klik `[Cancel]` pada dialog
13. Verifikasi tidak ada assignment tersimpan: Finance & Accounting tetap Staff dan IT Infrastructure tidak ditambahkan pada Disposal
14. Verifikasi modal tertutup kembali ke state sebelum Save
15. Verifikasi tidak ada toast tampil
16. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
17. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

### TC-FA-SU-248: Konfirmasi turun tangga: seluruh Save tersimpan sekaligus dan log Remove disusul Assign per grup dengan Old Value masing-masing

18. Catat jumlah entri `Remove` dan `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
19. Kembali ke User List, ganti isi kotak search dengan `Mira Anggraini`, tekan Enter, lalu buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, dan Role Monitoring & Report
20. Klik `[Submit]`
21. Verifikasi dialog hanya mendaftar grup yang turun tangga (Finance & Accounting), bukan grup baru (IT Infrastructure)
22. Klik `[Change]`
23. Verifikasi modal tertutup
24. Verifikasi toast "Success, Monitoring & Report has been assigned."
25. Verifikasi baris Disposal × Monitoring & Report memuat Finance & Accounting dan IT Infrastructure (grup baru tersimpan bersamaan)
26. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
27. Verifikasi untuk Finance & Accounting tercatat entri `Remove` Field `Disposal — Finance & Accounting — Staff` (`Assigned` ke `—`) dibanding baseline
28. Verifikasi untuk Finance & Accounting tercatat entri `Assign` Field `Disposal — Finance & Accounting — Monitoring & Report` (`—` ke `Assigned`) sesudah entri `Remove`
29. Verifikasi untuk IT Infrastructure tercatat entri `Assign` Field `Disposal — IT Infrastructure — Monitoring & Report`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-FA-SU-247, 249, lalu 248. Dialog TC-FA-SU-247 ditutup dengan `[Cancel]`, TC-FA-SU-249 membatalkan Save dua grup, dan TC-FA-SU-248 (dependensi TC-FA-SU-247) mengonfirmasi dengan `[Change]` sehingga Transaction Role Mira Anggraini hanya berubah satu kali; langkah dependensi TC-FA-SU-247 disalin utuh pada TC-FA-SU-248 (S-04).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 8, 9 dan 18. Baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 16, 17 dan 26 sampai 29. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- TC-FA-SU-249: klausa "tidak ada entri log" pada aksi yang dibatalkan ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12); modal tertutup dan tabel tanpa perubahan menjadi anchor positif.
- Pre-setup #50 diterapkan hanya pada Mira Anggraini (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih IT Infrastructure (langkah 10 dan 19); Home Group Mira Anggraini dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Search nama pengguna target pada User List digabung dalam langkah buka Detail (langkah 1 dan 19): langkah penghubung untuk menemukan baris target karena User List memuat 25 pengguna pada 3 halaman (R-16, bagian 8b butir 13); langkah 19 mengganti isi kotak search yang masih berisi nama sebelumnya (bagian 8b butir 9).
- Temuan untuk QA:
  - TC-FA-SU-247 butir d diperbarui: dialog hanya karena penurunan pada node yang sama. Data Mira Anggraini (Pre-setup #39) tidak memuat penugasan ancestor atau descendant Finance & Accounting pada Disposal, sehingga spec hanya mengasersi bahwa dialog memuat Finance & Accounting saja; kasus overlap ancestor dan descendant ada di E2E-415 dan E2E-417.
  - TC-FA-SU-247 butir c ("tidak ada perubahan tersimpan sebelum konfirmasi") tidak punya cara observasi langsung; spec mengasersi belum ada toast tersimpan saat dialog tampil.
  - TC-FA-SU-248 butir b menyebut "IT Infrastructure sebagai assignment baru tersimpan bersamaan" tanpa Verifikasi tersendiri di TC; spec mengasersinya pada tabel dan pada entri log.
  - Post Condition TC-FA-SU-248 butir c dan TC-FA-SU-249 (tiga permukaan log, Settings > Role & Permission) tidak punya langkah observasi di TC selain Tab Changelog; spec mengasersi Tab Changelog saja.
