---
id: TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client
title: "Login with OTP Identik untuk Berbagai Plan dan Entitas"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-144
  - TC-AUTH-OTP-145
  - TC-AUTH-OTP-146
  - TC-AUTH-OTP-147
  - TC-AUTH-OTP-148
  - TC-AUTH-OTP-149
  - TC-AUTH-OTP-150
coverage:
  web: automated
---

# Login with OTP Identik untuk Berbagai Plan dan Entitas

## Prerequisites

- Mode: FE+BE.
- Tanpa login pada semua langkah uji: Login with OTP berjalan di halaman publik tanpa sesi aktif di jendela privat.
- Akun aktor seeding: Total Control (Admin Console), pre-setup `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.AC_TC_PASSWORD`. Akun ini dipakai hook untuk membuat Client (baris TC-AUTH-OTP-144 sampai 147) dan user, bukan oleh langkah uji.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Environment variable: `AC_TC_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji.
- Hook `before` (seeding API) membuat user profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada) dengan suffix per run `+{runId}-042`, masing-masing di Client (plan sesuai baris) atau entitas yang disebut, dengan term subscription Active untuk Client. Hook `after` membersihkan data yang dibuat hook (tetap jalan walau seeding gagal sebagian): untuk baris Client (TC-AUTH-OTP-144 sampai 147) batalkan term Active, lalu hapus Client beserta user-nya; untuk baris Distributor, Partner, dan Principal (TC-AUTH-OTP-148 sampai 150) hanya hapus user yang dibuat hook, sedangkan entitasnya tidak dihapus.
- Client yang dibuat hook `before` untuk TC-AUTH-OTP-144 sampai 147 (plan sesuai baris, term subscription Active) adalah data yang dibuat spec dan dibersihkan di hook `after` (batalkan term Active, lalu hapus Client beserta user-nya): `Client Uji Starter {runId}-042` (TC-AUTH-OTP-144), `Client Uji Growth {runId}-042` (TC-AUTH-OTP-145), `Client Uji Professional {runId}-042` (TC-AUTH-OTP-146), `Client Uji Enterprise {runId}-042` (TC-AUTH-OTP-147). TC sumber tidak menyebut nama Client; nama ini ditetapkan spec.
- Fixture entitas Distributor, Partner, dan Principal (TC-AUTH-OTP-148 sampai 150) belum ada: TC dan Pre-setup tidak menyebut nama entitas pemilik user. Entitas Distributor, Partner, dan Principal yang sudah ada di environment automation harus ditetapkan tim FE, dan akun aktor Total Control (Admin Console) (`AC_TC_PASSWORD`) harus berwenang membuat user pada entitas itu. Nama entitas tidak ditulis di spec.
- Tabel "Dimensi yang diuji" (langkah dilakukan untuk setiap baris tabel):

| TC | Dimensi | User | Email |
|---|---|---|---|
| TC-AUTH-OTP-144 | Client plan Starter | `Dimas Utami` | `dimasutami+{runId}-042@qwertysystem.net` |
| TC-AUTH-OTP-145 | Client plan Growth | `Lestari Safitri` | `lestarisafitri+{runId}-042@qwertysystem.net` |
| TC-AUTH-OTP-146 | Client plan Professional | `Bayu Hakim` | `bayuhakim+{runId}-042@qwertysystem.net` |
| TC-AUTH-OTP-147 | Client plan Enterprise | `Intan Tanjung` | `intantanjung+{runId}-042@qwertysystem.net` |
| TC-AUTH-OTP-148 | Entitas Distributor | `Yoga Rahmawati` | `yogarahmawati+{runId}-042@qwertysystem.net` |
| TC-AUTH-OTP-149 | Entitas Partner | `Sari Nugroho` | `sarinugroho+{runId}-042@qwertysystem.net` |
| TC-AUTH-OTP-150 | Entitas Principal | `Eko Aditya` | `ekoaditya+{runId}-042@qwertysystem.net` |

## Test Steps

### Plan Starter, Growth, Professional, Enterprise dan entitas Distributor, Partner, Principal (TC-AUTH-OTP-144 sampai 150), lakukan untuk setiap baris tabel

1. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Verifikasi tidak ada pembatasan, upsell, atau pesan plan atau entitas pada halaman Request OTP
3. Ketik email user baris tabel pada field Email
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Request OTP]
6. Verifikasi toast sukses: "Success, the code has been sent."
7. Verifikasi halaman Verify OTP tampil
8. Verifikasi tidak ada pembatasan, upsell, atau pesan plan atau entitas pada halaman Verify OTP
9. Ketik 6 digit kode OTP dari email pada kotak digit
10. Verifikasi browser dialihkan ke Portal — Product Hub
11. Verifikasi sesi aktif untuk user baris tabel
12. Tutup jendela privat

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec Role Matrix gaya dimensi (konvensi bagian 3a): tabel "Dimensi yang diuji" dan langkah identik per baris; cara skrip menjalankan banyak baris (perulangan di dalam satu `it()` atau beberapa kali run) diputuskan di tahap script. Spec ini 12 langkah per putaran, dijalankan 7 kali.
- Butir a TC-AUTH-OTP-144 sampai 150 ("alur dan tampilan sama dengan dimensi lain") diasersi lewat toast, halaman Verify OTP, dan pengalihan ke Portal — Product Hub yang sama pada setiap putaran (langkah 6, 7, 10), tanpa langkah perbandingan lintas baris. Butir b ("tidak ada pembatasan, upsell, atau pesan plan atau entitas") diasersi pada halaman Request OTP (langkah 2) dan Verify OTP (langkah 8), yaitu saat masing-masing halaman tampil (S-14).
- Client berstatus Suspended dan Expired (TC-AUTH-OTP-151 dan 152, kelas harness h) ada di E2E-048.
- Langkah penghubung (S-03): menutup jendela privat ditulis sebagai aksi tanpa `Verifikasi`.
- Temuan untuk QA: (1) TC-AUTH-OTP-144 sampai 150 tidak menyebut cara membuat user pada entitas Distributor, Partner, dan Principal; spec menyerahkannya ke seeding hook, dan TC juga tidak menyebut entitas Distributor, Partner, atau Principal yang menjadi pemilik user maupun cara membersihkannya; spec memakai entitas yang sudah ada di environment (fixture belum ada, lihat Prerequisites) dan hanya menghapus user seeding; kewenangan akun aktor Total Control (Admin Console) membuat user di entitas itu juga tidak dinyatakan TC. (2) Butir b TC-AUTH-OTP-148 sampai 150 menyebut "tidak ada pembatasan atau pesan khusus entitas" tanpa kata "upsell"; spec memakai satu rumusan yang sama untuk semua baris tabel ("pembatasan, upsell, atau pesan plan atau entitas").
