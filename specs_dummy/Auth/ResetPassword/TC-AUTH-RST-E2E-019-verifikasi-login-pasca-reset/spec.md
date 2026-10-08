---
id: TC-AUTH-RST-E2E-019-verifikasi-login-pasca-reset
title: "Verifikasi login dengan password baru, penolakan password lama, sifat case-sensitive, dan pengakhiran sesi aktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-111
  - TC-AUTH-RST-112
  - TC-AUTH-RST-113
coverage:
  web: automated
---

# Verifikasi login dengan password baru, penolakan password lama, sifat case-sensitive, dan pengakhiran sesi aktif

## Prerequisites

- User `budisantoso@qwertysystem.net` baru saja menyelesaikan reset password dengan password baru `QaBaru!2027` (password lama sebelumnya adalah `QaReset!2026`).
- Sebelum reset dilakukan, user Budi Santoso memiliki sesi login aktif di browser lain / perangkat lain.
- Browser berada di halaman Login with Password (`/login`).

## Test Steps

### Penolakan login dengan password lama

1. Buka halaman Login with Password di browser web
2. Masukkan email "budisantoso@qwertysystem.net" pada field Email
3. Masukkan password lama "QaReset!2026" pada field Password
4. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Log in]
5. Verifikasi login ditolak dengan alert "Incorrect email or password"
6. Verifikasi tidak ada sesi login yang dibuat

### Sifat Case-Sensitivity pada password baru

7. Masukkan password baru dengan casing huruf kecil semua "qabaru!2027" pada field Password
8. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Log in]
9. Verifikasi login ditolak dengan alert "Incorrect email or password", membuktikan password baru bersifat case-sensitive

### Login sukses dengan password baru

10. Masukkan password baru yang presisi "QaBaru!2027" pada field Password
11. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Log in]
12. Verifikasi login berhasil dan pengguna dialihkan menuju dashboard Portal Product Hub

### Pengakhiran (Terminasi) otomatis seluruh sesi aktif lama

13. Buka tab browser lain yang sebelumnya masih memegang sesi login aktif sebelum reset
14. Lakukan navigasi atau refresh halaman pada tab tersebut
15. Verifikasi sesi lama telah dianulir (invalidated) oleh server
16. Verifikasi pengguna di sesi lama otomatis diarahkan keluar (logged out) ke halaman Login dengan pesan sesi telah berakhir

## Notes

- Sesuai PRD §9.2 F-AUTHRST-04 langkah 4, §9.7 baris 3, `AUTHSES-LOGIC-07`, dan keputusan NC-02, submit password baru yang sukses secara otomatis meng-invalidate seluruh sesi aktif user di semua perangkat demi mencegah penyalahgunaan akun yang telah diambil alih kembali oleh pemilik aslinya.
