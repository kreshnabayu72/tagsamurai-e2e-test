---
id: TC-AUTH-ACT-E2E-025-email-trigger-admin-console
title: "Activation Email dari Admin Console dan Resend"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-12
  - TC-AUTH-ACT-100
coverage:
  web: automated
---

# Activation Email dari Admin Console dan Resend

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: mail-catcher uji yang dapat dibaca spec (API inbox per alamat); jendela privat browser terpisah dari sesi Admin Console; pemicu job Auto-Archive (F-ACC-07) di environment uji atau toleransi tunggu untuk cleanup.
- Akun aktor: login sbg Role: Total Control (Admin Console) pada entitas Principal, pre-setup `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (baris 2 Tabel Data Uji Pre-setup) (Activate Trial oleh aktor Principal langsung Active); kredensial diambil dari environment variable `AC_TC_PASSWORD` (`Spectra.env.AC_TC_PASSWORD`).
- Hook `before` (lewat API, email bersuffix per run): TC-AUTH-ACT-100 user `Putri Wulandari` (`putriwulandari+{runId}-025@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (dibuat via Global Settings > User > Create User), Activation Email pertamanya terkirim ke mail-catcher, cooldown Resend Activation Email untuk user ini ditunggu eksplisit di langkah sebelum Resend.
- Data yang dibuat lewat UI di spec: TC-AUTH-ACT-12 Client `PT Karya Mandiri Baru {runId}-025` (PIC `Rudi Hartono`, `rudihartono+{runId}-025@qwertysystem.net`) dengan Default User `Fajar Cahyani` (`fajarcahyani+{runId}-025@qwertysystem.net`), lalu term trial pertamanya.
- Plan trial tersedia untuk Activate Trial di `Admin Console > Client Subscription`.
- Hook `after`: batalkan term trial Client `PT Karya Mandiri Baru {runId}-025` yang Active (Cancel Subscription, F-ACCS-04a) sehingga term Archive, polling status Client sampai Archived (job Auto-Archive F-ACC-07 berjalan hourly; environment uji perlu memicu job ini atau hook menunggu hingga batas waktu), lalu hapus Client tersebut beserta Default User-nya (`DELETE /v2/enterprise-management/clients/{id}` dengan body `{companyName: "PT Karya Mandiri Baru {runId}-025", confirm: true}`, diizinkan untuk Client Archived menurut `ACC-LOGIC-04.5`) dan user `Putri Wulandari` (lewat API). Pembersihan tidak berasumsi pembuatan Client berhasil penuh.

## Test Steps

### TC-AUTH-ACT-12: Default User Client baru menerima Activation Email saat subscription pertama Client Active

1. Login sbg Role: Total Control (Admin Console), buka `Admin Console > Client`, klik `[+ New Client]`
2. Isi Popup Create Client: Company Name `PT Karya Mandiri Baru {runId}-025`; PIC Name `Rudi Hartono`, PIC Email `rudihartono+{runId}-025@qwertysystem.net`; Address `Jl. Merdeka No. 10`, Country `Indonesia`, State `DKI Jakarta`, City `Jakarta Pusat`, Postal Code `10110`; Select Group: group root; Default User First Name `Fajar`, Last Name `Cahyani`, Email `fajarcahyani+{runId}-025@qwertysystem.net`, Division `Operations`; lalu klik [Submit]
3. Verifikasi Client `PT Karya Mandiri Baru {runId}-025` dan Default User `Fajar Cahyani` terbentuk; status Default User Not Yet Activated
4. Buka inbox `fajarcahyani+{runId}-025@qwertysystem.net` di mail-catcher
5. Verifikasi Belum ada email aktivasi di inbox `fajarcahyani+{runId}-025@qwertysystem.net` (Client tanpa subscription Active tidak memicu email)
6. Buka `Admin Console > Client Subscription`, jalankan Activate Trial untuk Client `PT Karya Mandiri Baru {runId}-025`
7. Buka inbox `fajarcahyani+{runId}-025@qwertysystem.net` di mail-catcher dan baca email aktivasi yang diterima
8. Verifikasi Email dengan Subject "Activate your TAG Samurai account" diterima di inbox `fajarcahyani+{runId}-025@qwertysystem.net` setelah term trial Active
9. Buka jendela privat baru (tanpa sesi Admin Console), lalu buka link [Activate Account] dari email tersebut di jendela itu
10. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for fajarcahyani+{runId}-025@qwertysystem.net." (alur aktivasi identik dengan user buatan Global Settings > User)
11. Verifikasi Token aktivasi Default User `Fajar Cahyani` Active dan status user Pending Activation

### TC-AUTH-ACT-100: Resend Activation Email dari Admin Console membuat link lama invalid

12. Ambil link aktivasi dari email pertama user `Putri Wulandari` di mail-catcher (link A)
13. Tunggu cooldown Resend Activation Email (60 detik) sejak email terakhir dikirim untuk user `Putri Wulandari`
14. Kembali ke sesi Admin Console, buka `Admin Console > Settings > User`, klik Resend Activation Email untuk `Putri Wulandari`
15. Ambil link aktivasi dari email baru (link B)
16. Buka jendela privat baru (tanpa sesi Admin Console), lalu buka link A di jendela itu
17. Verifikasi `Auth > Account Activation > Invalid Link` varian Expired tampil untuk link A walau belum 24 jam
18. Di jendela privat yang sama, buka link B
19. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for putriwulandari+{runId}-025@qwertysystem.net." untuk link B
20. Verifikasi Token A user `Putri Wulandari` Superseded dan token B Active

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness d (mail-catcher). Akun aktor Admin Console berbeda dari spec lain.
- Setiap link aktivasi dibuka di jendela privat baru tanpa sesi Admin Console; Resend dilakukan dengan kembali ke sesi Admin Console.
- TC-AUTH-ACT-12 mengikuti `admin-console/client` `ACC-LOGIC-05.2`: Activation Email Default User Client terkirim saat term subscription pertama Active, bukan saat Client dibuat; Activate Trial oleh aktor Principal dipakai sebagai pemicu.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
