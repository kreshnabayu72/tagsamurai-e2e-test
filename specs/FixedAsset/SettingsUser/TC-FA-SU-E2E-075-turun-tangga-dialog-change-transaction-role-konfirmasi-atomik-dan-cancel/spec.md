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
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-247: Turun tangga (Staff ke Monitoring & Report): dialog Change Transaction Role sebelum tersimpan

1. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting, Transaction Disposal, dan Role Monitoring & Report
2. Klik `[Submit]`
3. Verifikasi dialog Title `Change Transaction Role` dengan Body bullet `• Mira Anggraini`, kalimat `This will change their role for Disposal to Monitoring & Report in:`, dan bullet `• Finance & Accounting (currently Staff)`
4. Verifikasi dialog ditutup dengan pertanyaan `Are you sure you want to change it?`
5. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Change]` (severity warning)
6. Verifikasi belum ada toast tersimpan saat dialog tampil (tidak ada perubahan tersimpan sebelum konfirmasi)
7. Klik `[Cancel]` pada dialog

### TC-FA-SU-249: Cancel dialog turun tangga membatalkan seluruh Save termasuk grup yang tidak bermasalah

8. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
9. Klik `[+ Assign]` lalu pilih Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, dan Role Monitoring & Report
10. Klik `[Submit]`
11. Klik `[Cancel]` pada dialog
12. Verifikasi tidak ada assignment tersimpan: Finance & Accounting tetap Staff dan IT Infrastructure tidak ditambahkan pada Disposal
13. Verifikasi modal tertutup kembali ke state sebelum Save
14. Verifikasi tidak ada toast tampil
15. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
16. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

### TC-FA-SU-248: Konfirmasi turun tangga: seluruh Save tersimpan sekaligus dan log Remove disusul Assign per grup dengan Old Value masing-masing

17. Catat jumlah entri `Remove` dan `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
18. Buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, dan Role Monitoring & Report
19. Klik `[Submit]`
20. Verifikasi dialog hanya mendaftar grup yang turun tangga (Finance & Accounting), bukan grup baru (IT Infrastructure)
21. Klik `[Change]`
22. Verifikasi modal tertutup
23. Verifikasi toast "Success, Monitoring & Report has been assigned."
24. Verifikasi baris Disposal × Monitoring & Report memuat Finance & Accounting dan IT Infrastructure (grup baru tersimpan bersamaan)
25. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
26. Verifikasi untuk Finance & Accounting tercatat entri `Remove` Field `Disposal — Finance & Accounting — Staff` (`Assigned` ke `—`) dibanding baseline
27. Verifikasi untuk Finance & Accounting tercatat entri `Assign` Field `Disposal — Finance & Accounting — Monitoring & Report` (`—` ke `Assigned`) sesudah entri `Remove`
28. Verifikasi untuk IT Infrastructure tercatat entri `Assign` Field `Disposal — IT Infrastructure — Monitoring & Report`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-FA-SU-247, 249, lalu 248. Dialog TC-FA-SU-247 ditutup dengan `[Cancel]`, TC-FA-SU-249 membatalkan Save dua grup, dan TC-FA-SU-248 (dependensi TC-FA-SU-247) mengonfirmasi dengan `[Change]` sehingga Transaction Role Mira Anggraini hanya berubah satu kali; langkah dependensi TC-FA-SU-247 disalin utuh pada TC-FA-SU-248 (S-04).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 7, 8 dan 17. Baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 15, 16 dan 25 sampai 28. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- TC-FA-SU-249: klausa "tidak ada entri log" pada aksi yang dibatalkan ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12); modal tertutup dan tabel tanpa perubahan menjadi anchor positif.
- Temuan untuk QA:
  - TC-FA-SU-247 butir c ("tidak ada perubahan tersimpan sebelum konfirmasi") tidak punya cara observasi langsung; spec mengasersi belum ada toast tersimpan saat dialog tampil.
  - TC-FA-SU-248 butir b menyebut "IT Infrastructure sebagai assignment baru tersimpan bersamaan" tanpa Verifikasi tersendiri di TC; spec mengasersinya pada tabel dan pada entri log.
  - Post Condition TC-FA-SU-248 butir c dan TC-FA-SU-249 (tiga permukaan log, Settings > Role & Permission) tidak punya langkah observasi di TC selain Tab Changelog; spec mengasersi Tab Changelog saja.
