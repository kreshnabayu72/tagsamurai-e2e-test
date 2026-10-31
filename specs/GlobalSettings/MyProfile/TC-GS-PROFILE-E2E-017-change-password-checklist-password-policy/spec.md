---
id: TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy
title: "Change Password: checklist Password Policy real-time dan batas 72 karakter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-75
  - TC-GS-PROFILE-76
  - TC-GS-PROFILE-77
  - TC-GS-PROFILE-78
  - TC-GS-PROFILE-79
  - TC-GS-PROFILE-80
  - TC-GS-PROFILE-81
  - TC-GS-PROFILE-82
  - TC-GS-PROFILE-83
coverage:
  web: automated
---

# Change Password: checklist Password Policy real-time dan batas 72 karakter

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Pre-setup #7 `passwordProfile_automated_{namaCompany}@qwertysystem.net` (Maya Anggraini; Total Control; password aktif `Passw0rd!Old`; Time Format 24 jam; timezone Asia/Jakarta), kredensial `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Akun ini bukan akun default suite.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Environment variable: `Spectra.env.GS_PROFILE_PWD_PASSWORD` (login akun #7 di hook `before` spec dan Current Password TC-GS-PROFILE-83), `Spectra.env.PROFILE_PASSWORD_72` (password uji 72 karakter `Ab1!` + 68 huruf `x`, dipasang sebagai password baru TC-GS-PROFILE-83; nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data input uji (`Fixture.myProfile.changePassword`, literal input yang tidak dikirim, bukan kredensial): 73 karakter `Ab1!` + 69 huruf `x` (TC-GS-PROFILE-82) dan `Ab1!xyzw` (TC-GS-PROFILE-81); nilai TC-GS-PROFILE-75 sampai 80 ada di tabel "Data checklist".

| TC | Baris checklist | New Password awal | New Password akhir |
|---|---|---|---|
| TC-GS-PROFILE-75 | "Minimum 8 characters" | `Ab1!xyz` | `Ab1!xyzw` |
| TC-GS-PROFILE-76 | "One uppercase (A-Z)" | `ab1!xyzw` | `Ab1!xyzw` |
| TC-GS-PROFILE-77 | "One lowercase (a-z)" | `AB1!XYZW` | `Ab1!xyzW` |
| TC-GS-PROFILE-78 | "One number (0-9)" | `Ab!!xyzw` | `Ab1!xyzw` |
| TC-GS-PROFILE-79 | "One special character" | `Ab1xyzwq` | `Ab1!xyzw` |
| TC-GS-PROFILE-80 | "Password cannot contain spaces" | `Ab1! xyzw` | `Ab1!xyzw` |

- Halaman dipakai berulang: TC-GS-PROFILE-75 sampai 82 hanya mengetik dan mengamati tanpa submit, jadi memakai satu pembukaan modal dengan New Password dikosongkan di antara kasus. TC-GS-PROFILE-83 mengirim [Save] dan berada di akhir spec.
- State global yang berubah: TC-GS-PROFILE-83 mengubah password akun #7 menjadi `Spectra.env.PROFILE_PASSWORD_72`. Pemulihan ke `Passw0rd!Old` dan counter 0 dilakukan hook `after` suite (Hook suite 7). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [Change Password]
### Checklist real-time per baris (TC-GS-PROFILE-75 sampai 80)
Untuk setiap baris tabel "Data checklist" (langkah 2 sampai 8), lakukan:
2. Ketik New Password dengan nilai kolom "New Password awal"
3. Verifikasi baris checklist pada kolom "Baris checklist" berwarna abu-abu (belum terpenuhi)
4. Verifikasi lima baris checklist lainnya berwarna hitam (terpenuhi)
5. Ubah New Password menjadi nilai kolom "New Password akhir"
6. Verifikasi baris checklist pada kolom "Baris checklist" berwarna hitam
7. Verifikasi perubahan warna terjadi saat mengetik tanpa menekan [Save]
8. Kosongkan isi New Password
### Isi checklist (TC-GS-PROFILE-81)
9. Ketik New Password `Ab1!xyzw`
10. Verifikasi checklist memuat enam baris: "Minimum 8 characters", "One uppercase (A-Z)", "One lowercase (a-z)", "One number (0-9)", "One special character", "Password cannot contain spaces"
11. Verifikasi semua baris checklist berwarna hitam
12. Verifikasi tidak ada baris "Max. 72 characters" pada checklist
13. Verifikasi tidak ada warna merah atau hijau pada checklist
14. Kosongkan isi New Password
### Melebihi 72 karakter (TC-GS-PROFILE-82)
15. Ketik New Password 73 karakter (`Ab1!` + 69 huruf `x`)
16. Verifikasi caption merah "Max. 72 characters" tampil di bawah New Password tanpa menekan [Save]
### Tepat 72 karakter diterima (TC-GS-PROFILE-83)
17. Ganti isi New Password dengan 72 karakter (`Spectra.env.PROFILE_PASSWORD_72`)
18. Verifikasi checklist Password Policy tampil dengan enam baris
19. Verifikasi tidak ada caption "Max. 72 characters" di bawah New Password
20. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
21. Ketik `Spectra.env.PROFILE_PASSWORD_72` di Confirm New Password
22. Klik [Save]
23. Verifikasi toast sukses: "Success, your password has been updated."

## Notes

- Pembagian TC: TC-GS-PROFILE-75 sampai 83 berada di spec ini. Langkah 2 sampai 8 adalah langkah yang diulang untuk enam baris tabel "Data checklist".
- Langkah penghubung (S-03): "Kosongkan isi New Password" di akhir tiap blok membersihkan state sebelum kasus berikutnya (S-09). Dua langkah `Verifikasi` sebelum [Save] pada TC-GS-PROFILE-83 (checklist enam baris tampil, lalu tidak ada caption "Max. 72 characters") dituliskan sebelum [Save] karena modal tertutup sesudah toast sukses; checklist enam baris adalah anchor positif untuk asersi absence caption (bagian 8b butir 2) dan tidak ada di Expected TC.
- Urutan: TC-GS-PROFILE-83 diletakkan paling akhir karena mengubah password dan menutup modal (bagian 3 prinsip 5 dan 6).
- Spec ini di atas smell 35 langkah (dengan ekspansi enam iterasi sekitar 60 langkah). Alasan: semua blok satu topik (checklist Password Policy di modal yang sama), satu kelas harness, tanpa submit kecuali blok terakhir; langkah terbanyak berasal dari enam iterasi satu pola dan satu `Verifikasi` per klausa Expected (S-01). Tiap iterasi mandiri karena field dikosongkan di antaranya.
- Temuan untuk QA:
  - TC-GS-PROFILE-83: Post Condition "Password akun berubah" tidak punya langkah observasi di TC, jadi tidak diasersi di spec ini.
