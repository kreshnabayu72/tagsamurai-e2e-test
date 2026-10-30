---
id: TC-GS-PROFILE-E2E-020-change-password-penolakan-server-aturan-policy
title: "Change Password: penolakan server per aturan Password Policy (enam aturan)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-93
  - TC-GS-PROFILE-94
  - TC-GS-PROFILE-95
  - TC-GS-PROFILE-96
  - TC-GS-PROFILE-97
  - TC-GS-PROFILE-98
coverage:
  web: automated
---

# Change Password: penolakan server per aturan Password Policy (enam aturan)

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Pre-setup #7 `passwordProfile_automated_{namaCompany}@qwertysystem.net` (Maya Anggraini; Total Control; password aktif `Passw0rd!Old`; Time Format 24 jam; timezone Asia/Jakarta), kredensial `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Akun ini bukan akun default suite.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Environment variable: `Spectra.env.GS_PROFILE_PWD_PASSWORD` (login akun #7 di hook `before` spec dan Current Password benar). Password tidak ditulis di spec atau fixture.
- Data input uji (`Fixture.myProfile.changePassword`, literal input yang ditolak, bukan kredensial) ada di tabel "Data penolakan Policy". New Password dan Confirm New Password selalu bernilai sama.

| TC | Aturan yang dilanggar | New Password dan Confirm New Password |
|---|---|---|
| TC-GS-PROFILE-93 | "Minimum 8 characters" | `Ab1!xyz` |
| TC-GS-PROFILE-94 | "One uppercase (A-Z)" | `ab1!xyzw` |
| TC-GS-PROFILE-95 | "One lowercase (a-z)" | `AB1!XYZW` |
| TC-GS-PROFILE-96 | "One number (0-9)" | `Ab!!xyzw` |
| TC-GS-PROFILE-97 | "One special character" | `Ab1xyzwq` |
| TC-GS-PROFILE-98 | "Password cannot contain spaces" | `Ab1! xyzw` |

- Kemampuan baca state BE (disediakan tim FE/BE, tanpa endpoint karangan): jumlah sesi aktif akun Pre-setup #7. Nilainya dicatat sebagai baseline di langkah pertama dan dibandingkan di setiap `Verifikasi` "tidak ada sesi yang di-invalidate".
- Current Password benar sehingga server mengevaluasi Policy dan menolaknya; counter Change Password tidak berubah dan tidak ada password yang berubah. Satu pembukaan modal untuk keenam TC; New Password dan Confirm New Password diganti di antara kasus.

## Test Steps

1. Catat jumlah sesi aktif akun Pre-setup #7 lewat kemampuan baca state BE sebagai baseline
2. Klik [Change Password]
3. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
### Penolakan server per aturan (TC-GS-PROFILE-93 sampai 98)
Untuk setiap baris tabel "Data penolakan Policy" (langkah 4 sampai 10), lakukan:
4. Ganti isi New Password dengan nilai kolom "New Password dan Confirm New Password"
5. Ganti isi Confirm New Password dengan nilai yang sama
6. Klik [Save]
7. Verifikasi caption merah sesuai kolom "Aturan yang dilanggar" tampil di bawah New Password
8. Verifikasi checklist real-time tetap tampil tanpa perubahan warna menjadi merah
9. Verifikasi modal Change Password tetap terbuka
10. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline (tidak ada sesi yang di-invalidate)
### Menutup modal yang terisi
11. Klik [✕]
12. Verifikasi dialog "Unsaved Changes" dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
13. Klik [Leave]

## Notes

- Pembagian TC: TC-GS-PROFILE-93 sampai 98 berada di spec ini. Langkah 4 sampai 10 diulang untuk enam baris tabel "Data penolakan Policy"; nilai tiap iterasi hanya di tabel Prerequisites.
- Langkah penghubung (S-03): mengganti New Password dan Confirm New Password di antara baris tabel membersihkan caption baris sebelumnya karena tiap submit menggantinya dengan caption aturan yang baru. Tiga langkah penutup memulihkan form dirty (S-08, S-09).
- Spec ini di atas smell 35 langkah (dengan ekspansi enam iterasi sekitar 40 langkah). Alasan: seluruh blok satu pola penolakan server atas Policy pada modal dan akun yang sama, satu kelas harness; langkah terbanyak berasal dari ekspansi enam iterasi dan satu `Verifikasi` per klausa Expected (S-01). Tiap iterasi mandiri.
- Temuan untuk QA:
  - TC-GS-PROFILE-93 sampai 98: Post Condition "Counter Change Password tetap 0" tidak punya langkah observasi di TC, jadi tidak diasersi.
  - TC-GS-PROFILE-93 sampai 98: Expected "Tidak ada sesi yang di-invalidate" tidak memberi cara memeriksa; spec memakai kemampuan baca jumlah sesi aktif akun #7 yang disediakan tim FE/BE.
