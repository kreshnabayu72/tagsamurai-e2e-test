---
id: TC-FA-SU-E2E-044-resend-penolakan-cooldown-dari-tampilan-basi-dan-status-berubah-setelah-halaman-dimuat
title: "Resend: Penolakan Cooldown dari Tampilan Basi dan Status Berubah Setelah Halaman Dimuat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-145
  - TC-FA-SU-149
coverage:
  web: automated
---

# Resend: Penolakan Cooldown dari Tampilan Basi dan Status Berubah Setelah Halaman Dimuat

## Prerequisites

- Mode: FE+BE.
- Akun aktor (Admin A, sesi UI): Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua (Admin B, Pre-setup #13): akun yang sama dengan sesi API aktor (lihat `suite.md`); hanya memicu perubahan state sehingga tidak memakai sesi UI kedua.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; layanan #37): Hana Kusuma `hana.kusuma@corp.id` (Pending Activation). Cooldown Resend Hana belum berjalan saat spec dimulai dan saat langkah 14 (dipulihkan lewat seed API).
- Kemampuan teknis (disediakan tim FE/BE): mail-catcher dengan baseline jumlah email per alamat `hana.kusuma@corp.id` (R-11); kemampuan baca jumlah entri log Tab Changelog target; penyelesaian aktivasi Hana lewat tautan email sebagai pengguna target dengan sesi API pengguna itu (tautan aktivasi diambil dari inbox mail-catcher); seed API untuk mengembalikan Hana ke Pending Activation.
- State global dan pemulihan: status Hana berubah menjadi Activated pada langkah 18 dan dipulihkan lewat seed API di hook `after`; cooldown Resend Hana dipulihkan lewat seed API di hook `after`; entri log Resend bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-145: Penolakan server karena cooldown pada Resend single

1. Ketik Search `Hana`, tekan Enter di User List (Admin A)
2. Klik ⋯ pada baris Hana Kusuma
3. Verifikasi `Resend Activation Email` Enabled di menu ⋯ baris Hana Kusuma pada tampilan Admin A
4. Admin B (sesi API) mengirim Resend Activation Email untuk Hana Kusuma hingga cooldown tersimpan
5. Tunggu aksi selesai: permintaan sesi API Admin B selesai dan cooldown Hana tersimpan
6. Admin A klik `Resend Activation Email` di menu ⋯ baris Hana Kusuma pada tampilan basi
7. Verifikasi tidak ada toast error yang tampil
8. Klik ⋯ pada baris Hana Kusuma lagi, hover `Resend Activation Email`
9. Verifikasi `Resend Activation Email` pada baris Hana Kusuma langsung Disabled dengan tooltip "Please wait [Seconds] seconds before resending." dengan `[Seconds]` antara 1 dan 60
10. Verifikasi jumlah email aktivasi ke `hana.kusuma@corp.id` di mail-catcher bertambah tepat satu dibanding baseline (email dari Admin B saja)
11. Buka Detail Hana Kusuma > Tab Changelog, muat ulang sampai entri tampil
12. Verifikasi entri `Resend Activation Email` dari Admin B tampil di Tab Changelog Hana Kusuma
13. Verifikasi jumlah entri `Resend Activation Email` di Tab Changelog Hana Kusuma bertambah tepat satu dibanding baseline (tidak ada entri baru dari klik Admin A)

### TC-FA-SU-149: Status berubah setelah halaman dimuat lalu Resend

14. Pulihkan Hana Kusuma ke Pending Activation tanpa cooldown lewat seed API
15. Muat ulang halaman User List, ketik Search `Hana`, tekan Enter
16. Klik ⋯ pada baris Hana Kusuma
17. Verifikasi `Resend Activation Email` Enabled di menu ⋯ baris Hana Kusuma pada tampilan Admin A
18. Hana Kusuma menyelesaikan aktivasi lewat tautan email (sesi API pengguna target) hingga status `Activated` tersimpan
19. Tunggu aksi selesai: permintaan sesi API pengguna target selesai
20. Catat baseline jumlah email ke `hana.kusuma@corp.id` di mail-catcher
21. Admin A klik `Resend Activation Email` di menu ⋯ baris Hana Kusuma pada tampilan basi
22. Verifikasi dialog Title `User Updated`, Body `This user was changed by someone else. Please review.`, dan tombol `[OK]` tampil
23. Klik `[OK]`
24. Verifikasi baris Hana Kusuma tampil di User List
25. Verifikasi badge `Pending Activation` tidak tampil pada baris Hana Kusuma
26. Klik ⋯ pada baris Hana Kusuma
27. Verifikasi menu ⋯ baris Hana Kusuma memuat `Detail`
28. Verifikasi `Resend Activation Email` tidak tampil di menu ⋯ baris Hana Kusuma
29. Verifikasi jumlah email ke `hana.kusuma@corp.id` di mail-catcher sama dengan baseline langkah 20 (tidak ada email terkirim)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Pembagian TC lintas spec: TC-FA-SU-147 (visibilitas aksi Resend menurut status) ada di spec 058.
- Pelaku kedua lewat sesi API (R-20): langkah 4 dan 18 hanya memicu perubahan state dan bukan objek asersi; tidak memakai `P-2` (keputusan 2026-10-30).
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 15 (Search untuk menemukan baris target, R-16), langkah 5 dan 19 (menunggu aksi pelaku kedua selesai, bagian 8b butir 8), langkah 11 (membuka Tab Changelog), langkah 14 (memulihkan Hana lewat seed API), dan langkah 20 (mencatat baseline email).
- Asersi tambahan di luar Expected TC: langkah 3 dan 17 (tombol masih Enabled pada tampilan basi) adalah prasyarat "tampilan basi, tombol masih Enabled" Expected a TC-FA-SU-145 dan TC-FA-SU-149; langkah 12, 24, dan 27 adalah anchor positif bagi asersi absence atau jumlah berikutnya (bagian 8b butir 2).
- Temuan untuk QA:
  - Expected c TC-FA-SU-145 ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Tab Changelog target (langkah 11 sampai 13).
  - Post Condition TC-FA-SU-149 ("tidak ada entri log baru") tidak punya langkah observasi dan tidak diasersi (S-01, S-05).
  - TC-FA-SU-149 langkah 2 ("selesaikan aktivasi lewat tautan email di sesi lain") tidak menyebut cara tautan diperoleh; spec mengasumsikan tautan dari mail-catcher dan penyelesaian lewat sesi API pengguna target sebagai kemampuan "disediakan tim FE/BE" (S-13).
  - Tooltip pada Expected b TC-FA-SU-145 hanya menulis "sisa detik cooldown" tanpa nilai; spec memakai template NC-02 dengan `[Seconds]` antara 1 dan 60.
