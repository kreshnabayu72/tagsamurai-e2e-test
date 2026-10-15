---
id: TC-AUTH-LP-E2E-025-agreement-token-ttl
title: "Masa Berlaku Token Pra-Autentikasi pada Layar Confirm to Continue"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-88
  - TC-AUTH-LP-89
coverage:
  web: automated
---

# Masa Berlaku Token Pra-Autentikasi pada Layar Confirm to Continue

## Prerequisites

- Seeding: setiap user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`; autentikasi API, bukan sesi browser). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-025` (contoh `hadigunawan+{runId}-025@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: pengaturan jam server absolut (token pra-autentikasi berlaku 10 menit dan dihitung murni di server, tidak diamati lewat UI, sehingga hanya jam server yang diatur, bukan jam browser): jam server diset ke waktu terbit token ditambah 11 menit (TC-AUTH-LP-88) atau ditambah 9 menit (TC-AUTH-LP-89), bukan digeser relatif; tidak ada waktu tunggu nyata dan tidak ada kebutuhan timeout run panjang; waktu terbit token dapat dibaca atau ditentukan tim FE/BE (TC tidak menyebut mekanismenya, tanpa mengarang endpoint); jendela privat baru per TC; reCAPTCHA mode uji di environment; fixture BE yang menyiapkan kondisi versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui user, device terpercaya, dan tidak memicu MFA.
- State global: jam server diubah oleh spec ini dan memengaruhi seluruh tenant, sehingga suite berjalan serial (`parallel: false`). Jam server dipulihkan segera sesudah asersi tiap TC (langkah 14 dan 25) dan hook `after` memulihkan jam walau spec gagal di tengah.
- Mode: FE+BE
- TC-AUTH-LP-88: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-88: User `Hadi Gunawan` (`hadigunawan+{runId}-025@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; layar Confirm to Continue tampil setelah password benar (di-seed lewat API di hook `before`)
- TC-AUTH-LP-88 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-89: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-89: User `Ika Pertiwi` (`ikapertiwi+{runId}-025@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA (di-seed lewat API di hook `before`)
- TC-AUTH-LP-89 data: Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-88: Token pra-autentikasi kedaluwarsa mengembalikan user ke halaman Login

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman Login with Password
3. Isi Email `hadigunawan+{runId}-025@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
4. Selesaikan reCAPTCHA
5. Klik [Log in] → layar Confirm to Continue tampil
6. Atur jam server ke waktu terbit token pra-autentikasi ditambah 11 menit (absolut) tanpa interaksi di layar Confirm to Continue
7. Centang checkbox persetujuan
8. Klik [Continue ➔]
9. Verifikasi browser kembali ke halaman Login with Password (user harus mengulang dari password)
10. Verifikasi browser tidak menuju Portal — Product Hub
11. Verifikasi browser tidak menuju halaman MFA
12. Verifikasi tidak ada toast, Alert, atau pesan lain yang tampil
13. Verifikasi field Email kosong dan menampilkan placeholder "Enter your email"
14. Pulihkan jam server ke waktu nyata
15. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-89: Konfirmasi Agreement sebelum token pra-autentikasi habis tetap berhasil

16. Buka jendela privat baru (tanpa sesi login)
17. Buka halaman Login with Password
18. Isi Email `ikapertiwi+{runId}-025@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
19. Selesaikan reCAPTCHA
20. Klik [Log in] → layar Confirm to Continue tampil
21. Atur jam server ke waktu terbit token pra-autentikasi ditambah 9 menit (absolut) tanpa interaksi di layar Confirm to Continue
22. Centang checkbox persetujuan
23. Klik [Continue ➔]
24. Verifikasi browser menuju Portal — Product Hub
25. Pulihkan jam server ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Urutan TC mengikuti nomor TC. Jeda 11 menit dan 9 menit dipenuhi dengan mengatur jam server absolut (waktu terbit token + N menit; konvensi bagian 6), bukan menunggu; kedua TC memakai user terpisah supaya tiap TC mandiri.
- Langkah login pada TC sumber ("Login dengan Email … sampai layar Confirm to Continue tampil") disalin utuh menjadi langkah 2–5 dan 17–20 (S-04). Langkah "Buka jendela privat baru" dan langkah pemulihan jam server (14 dan 25) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai tanpa sesi dan jam normal (S-03; S-09).
- Kelas harness: harness eksternal / TTL (prinsip 13d), satu spec untuk TTL token pra-autentikasi.
- Langkah 15 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA:
  - TC-AUTH-LP-88 dan TC-AUTH-LP-89 tidak menyebut cara menyiapkan kondisi "versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui" selain lewat precondition; spec menuliskannya sebagai kemampuan fixture BE di Prerequisites tanpa endpoint (S-13).
  - TC-AUTH-LP-88 dan TC-AUTH-LP-89 menyebut jeda 11 dan 9 menit dalam menit nyata dan tidak menyebut cara mengatur jam server atau membaca waktu terbit token; spec memakai kemampuan pengaturan jam server absolut yang disediakan tim FE/BE (Prerequisites).
  - TC-AUTH-LP-88 tidak menyebut nilai TTL; angka 10 menit diambil dari judul skenario TC-AUTH-LP-89 dan PRD F-AUTHLP-05 yang dirujuk kolom Sumber PRD.
