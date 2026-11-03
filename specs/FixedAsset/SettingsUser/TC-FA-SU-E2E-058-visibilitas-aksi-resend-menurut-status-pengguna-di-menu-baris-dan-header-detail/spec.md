---
id: TC-FA-SU-E2E-058-visibilitas-aksi-resend-menurut-status-pengguna-di-menu-baris-dan-header-detail
title: "Visibilitas Aksi Resend Menurut Status Pengguna di Menu Baris dan Header Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-147
coverage:
  web: automated
---

# Visibilitas Aksi Resend Menurut Status Pengguna di Menu Baris dan Header Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; layanan #37): Gita Permata (Activated), Hana Kusuma (Pending Activation), dan Indra Wijaya (Pending Email Confirmation). Cooldown Resend belum berjalan; spec tidak mengirim Resend sehingga tidak ada state yang berubah.
- State global dan pemulihan: tidak ada state global dan tidak ada data yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-147: Resend Activation hanya untuk Pending Activation dan Resend Confirmation hanya untuk Pending Email Confirmation

1. Ketik Search `Gita`, tekan Enter di User List
2. Klik ⋯ pada baris Gita Permata
3. Verifikasi menu ⋯ baris Gita Permata memuat `Detail`
4. Verifikasi `Resend Activation Email` tidak tampil di menu ⋯ baris Gita Permata
5. Verifikasi `Resend Confirmation Email` tidak tampil di menu ⋯ baris Gita Permata
6. Ganti isi kotak search dengan `Hana`, tekan Enter, klik ⋯ pada baris Hana Kusuma
7. Verifikasi menu ⋯ baris Hana Kusuma memuat `Resend Activation Email`
8. Verifikasi `Resend Confirmation Email` tidak tampil di menu ⋯ baris Hana Kusuma
9. Ganti isi kotak search dengan `Indra`, tekan Enter, klik ⋯ pada baris Indra Wijaya
10. Verifikasi menu ⋯ baris Indra Wijaya memuat `Resend Confirmation Email`
11. Verifikasi `Resend Activation Email` tidak tampil di menu ⋯ baris Indra Wijaya
12. Klik nama Indra Wijaya untuk membuka Detail
13. Verifikasi header Detail Indra Wijaya menampilkan tombol `[Resend Confirmation Email]`
14. Verifikasi tombol `[Resend Activation Email]` tidak tampil di header Detail Indra Wijaya
15. Kembali ke User List, ketik Search `Hana`, tekan Enter, klik nama Hana Kusuma
16. Verifikasi header Detail Hana Kusuma menampilkan tombol `[Resend Activation Email]`
17. Verifikasi tombol `[Resend Confirmation Email]` tidak tampil di header Detail Hana Kusuma
18. Kembali ke User List, ketik Search `Gita`, tekan Enter, klik nama Gita Permata
19. Verifikasi header Detail Gita Permata tampil dengan nama Gita Permata
20. Verifikasi tombol `[Resend Activation Email]` tidak tampil di header Detail Gita Permata
21. Verifikasi tombol `[Resend Confirmation Email]` tidak tampil di header Detail Gita Permata

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC lintas spec: TC-FA-SU-145 dan 149 (tampilan basi dan status berubah) ada di spec 044.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 6, 9, 15, dan 18 (Search untuk menemukan baris target, R-16), langkah 12 (membuka Detail).
- Asersi tambahan di luar Expected TC: langkah 3 (menu memuat `Detail`), langkah 7, 10, 13, 16, dan 19 adalah anchor positif bagi asersi absence di langkah sesudahnya (bagian 8b butir 2); langkah 13 dan 16 juga memenuhi Expected c ("header Detail mengikuti aturan yang sama").
- Temuan untuk QA:
  - Langkah 2 TC-FA-SU-147 menyebut "buka Detail ketiganya dan amati header" tetapi Expected c menyebut "header Detail mengikuti aturan yang sama" tanpa merinci tombol header per pengguna; spec mengasersi tombol header yang sesuai status dan absennya tombol jenis lain.
  - Post Condition TC-FA-SU-147 bernilai `-`; tidak diasersi.
