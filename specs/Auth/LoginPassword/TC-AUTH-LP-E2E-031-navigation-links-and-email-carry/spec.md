---
id: TC-AUTH-LP-E2E-031-navigation-links-and-email-carry
title: "Navigasi ke Login with OTP dan Reset Password serta Pembawaan Email"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-05
  - TC-AUTH-LP-93
  - TC-AUTH-LP-94
  - TC-AUTH-LP-95
  - TC-AUTH-LP-96
coverage:
  web: automated
---

# Navigasi ke Login with OTP dan Reset Password serta Pembawaan Email

## Prerequisites

- Seeding: user Activated dan Active untuk TC-AUTH-LP-05 dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`; autentikasi API, bukan sesi browser). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-031` (contoh `budisantoso+{runId}-031@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama. Email uji format `john@` (TC-AUTH-LP-94) tetap literal.
- Environment variable: `GS_TC_PASSWORD`. Spec ini tidak mengisi password.
- Kemampuan teknis: membuka dan menutup tab browser; halaman Login with OTP, Reset Password, dan Login with Password tersedia di environment; permintaan kode OTP dari halaman Login with OTP diproses backend nyata (TC-AUTH-LP-05); kotak masuk email tidak dibuka.
- Mode: FE+BE (TC-AUTH-LP-05 membutuhkan backend nyata; TC-AUTH-LP-93 s.d. 96 adalah tampilan murni tanpa API)
- TC-AUTH-LP-93: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-93 data: Email: `budisantoso+{runId}-031@qwertysystem.net` (hanya diketik, tidak dikirim)
- TC-AUTH-LP-94: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-94 data: Email: `john@` (literal, format belum valid)
- TC-AUTH-LP-95: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-95 data: Email: `budisantoso+{runId}-031@qwertysystem.net` (hanya diketik, tidak dikirim)
- TC-AUTH-LP-96: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-96 data: Email: `budisantoso+{runId}-031@qwertysystem.net` (hanya diketik, tidak dikirim)
- TC-AUTH-LP-05: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-05: User `Budi Santoso` (`budisantoso+{runId}-031@qwertysystem.net`) berstatus Activated dan Active (di-seed lewat API di hook `before`); halaman Login with OTP tersedia
- TC-AUTH-LP-05 data: Email: `budisantoso+{runId}-031@qwertysystem.net`

## Test Steps

### TC-AUTH-LP-93: Link [Log in with OTP] membawa Email yang sudah diketik

1. Buka halaman Login with Password
2. Ketik Email `budisantoso+{runId}-031@qwertysystem.net`
3. Klik link [Log in with OTP]
4. Verifikasi halaman Login with OTP terbuka
5. Verifikasi field Email pada halaman Login with OTP terisi `budisantoso+{runId}-031@qwertysystem.net`

### TC-AUTH-LP-94: Link [Log in with OTP] membawa Email yang formatnya belum valid

6. Buka halaman Login with Password
7. Kosongkan field Email
8. Ketik Email `john@`
9. Klik link [Log in with OTP]
10. Verifikasi halaman Login with OTP terbuka
11. Verifikasi field Email pada halaman Login with OTP terisi `john@`
12. Verifikasi Caption error format Email tidak tampil saat perpindahan halaman

### TC-AUTH-LP-95: Link [Reset here] membawa Email yang sudah diketik

13. Buka halaman Login with Password
14. Kosongkan field Email
15. Ketik Email `budisantoso+{runId}-031@qwertysystem.net`
16. Klik link [Reset here]
17. Verifikasi halaman Reset Password terbuka
18. Verifikasi field Email pada halaman Reset Password terisi `budisantoso+{runId}-031@qwertysystem.net`

### TC-AUTH-LP-96: Email yang dibawa tidak tersimpan setelah tab ditutup

19. Buka halaman Login with Password
20. Kosongkan field Email
21. Ketik Email `budisantoso+{runId}-031@qwertysystem.net`
22. Klik link [Log in with OTP]
23. Tutup tab
24. Buka halaman Login with Password di tab baru
25. Verifikasi field Email pada halaman Login with Password di tab baru kosong dan menampilkan placeholder "Enter your email"

### TC-AUTH-LP-05: Email terisi otomatis saat kembali dari Login with OTP lewat Edit email

26. Buka halaman Login with OTP
27. Isi Email `budisantoso+{runId}-031@qwertysystem.net` lalu lanjutkan ke tahap kode OTP
28. Klik "Edit email"
29. Pindah ke halaman Login with Password dari halaman Login with OTP
30. Verifikasi field Email pada halaman Login with Password terisi `budisantoso+{runId}-031@qwertysystem.net`
31. Verifikasi field Email masih dapat diubah (tidak read-only)

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Urutan: kasus tanpa API (TC-AUTH-LP-93, 94, 95, 96) lebih dulu, lalu TC-AUTH-LP-05 yang memanggil backend nyata, sehingga kasus tampilan murni tidak ikut gagal bila request OTP bermasalah (S-10). Urutan ini berbeda dari nomor TC.
- TC-AUTH-LP-93, 94, 95, dan 96 dimulai dengan "Buka halaman Login with Password", sedangkan TC-AUTH-LP-05 dimulai dengan "Buka halaman Login with OTP" karena memang diuji dari halaman itu; membuka Login with Password sesudah TC sebelumnya bisa membawa Email yang masih terisi dari halaman itu, sehingga TC-AUTH-LP-94, 95, dan 96 mengosongkan field Email lebih dulu (lihat butir langkah penghubung); tab tambahan pada TC-AUTH-LP-96 ditutup oleh langkah TC sendiri.
- Langkah penghubung (S-03): "Kosongkan field Email" sebelum mengetik Email pada TC-AUTH-LP-94, 95, dan 96 (tab yang sama dengan TC sebelumnya, tempat Email dibawa dari halaman Login with Password) agar Ketik tidak menambah ke isian yang terbawa; tanpa asersi.
- Temuan untuk QA:
  - TC-AUTH-LP-05 langkah 4 ("Pindah ke halaman Login with Password dari halaman Login with OTP") tidak menyebut tautan atau cara berpindah, dan langkah 2 tidak menyebut tombol untuk "lanjutkan ke tahap kode OTP"; spec memakai deskripsi TC apa adanya tanpa mengarang label.
  - TC-AUTH-LP-94: mengetik `john@` lalu mengklik link berpotensi memicu blur pada field Email sehingga Caption "Email format is incorrect" (TC-AUTH-LP-14) tampil di halaman Login with Password; Expected TC tidak menyebut halaman mana yang dimaksud, sehingga spec mengasersi hanya pada halaman Login with OTP.
  - TC-AUTH-LP-96 tidak menyebut apakah penutupan tab dan pembukaan tab baru dilakukan pada jendela yang sama atau konteks yang sama; sessionStorage tab lama tidak terbawa.
