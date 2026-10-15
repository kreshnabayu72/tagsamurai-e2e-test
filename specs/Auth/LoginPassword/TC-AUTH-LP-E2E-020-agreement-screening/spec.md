---
id: TC-AUTH-LP-E2E-020-agreement-screening
title: "Screening Layar Confirm to Continue dan Checkbox Agreement"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-07
  - TC-AUTH-LP-08
  - TC-AUTH-LP-91
  - TC-AUTH-LP-77
coverage:
  web: automated
---

# Screening Layar Confirm to Continue dan Checkbox Agreement

## Prerequisites

- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: seeding user subjek dengan versi Privacy Policy yang disetujui lebih lama dari versi aktif (relatif, lihat aturan State global Privacy Policy); fixture BE untuk device terpercaya (tidak memicu MFA); tombol Tab keyboard; jendela privat baru; tab baru dari tautan; reCAPTCHA mode uji di environment.
- Mode: FE+BE.
- State global Privacy Policy: publish bersifat append-only dan immutable tanpa restore (`ACPP-LOGIC-01`), sehingga versi aktif tidak dipulihkan dan naik pada setiap run; suite berjalan serial. Seeding user Agreement selalu relatif terhadap versi aktif saat hook `before` (versi yang disetujui user = versi sebelum versi aktif), tanpa nomor versi absolut.
- TC-AUTH-LP-07: User `Tono Kurniawan` (`tonokurniawan+{runId}-020@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini; device terpercaya (tidak memicu MFA)
- TC-AUTH-LP-07: User belum login (guest); browser web
- TC-AUTH-LP-07 data: Email `tonokurniawan+{runId}-020@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-08: User dan data sama seperti TC-AUTH-LP-07 (user belum login, jendela privat baru)
- TC-AUTH-LP-91: User dan data sama seperti TC-AUTH-LP-07 (user belum login, jendela privat baru)
- TC-AUTH-LP-77: User `Tono Kurniawan` (`tonokurniawan+{runId}-020@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini
- TC-AUTH-LP-77: User belum login (guest); browser web
- TC-AUTH-LP-77 data: Email `tonokurniawan+{runId}-020@qwertysystem.net`; Password salah nilai `Spectra.env.LP_PASSWORD_WRONG`
- Layar Confirm to Continue ditinggalkan tanpa Continue pada tiap TC, sehingga persetujuan user tidak pernah tersimpan di spec ini.

## Test Steps

### TC-AUTH-LP-07: Screening layar Confirm to Continue setelah password benar

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman Login with Password
3. Ketik email `tonokurniawan+{runId}-020@qwertysystem.net` di field Email
4. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
5. Selesaikan reCAPTCHA
6. Klik [Log in]
7. Susuri layar yang tampil dari atas ke bawah tanpa klik apa pun
8. Verifikasi **Header**: Title "Confirm to Continue"
9. Verifikasi **Body**: Content Box scrollable berisi teks persetujuan "By accessing TAG Samurai, you agree to comply with our Privacy Policy. Please read the full document before continuing. Your continued use of the platform means you accept the terms described in the Privacy Policy."
10. Verifikasi **Body**: Content Box berisi tautan "Read the full Privacy Policy"
11. Verifikasi **Body**: Checkbox berstatus unchecked dengan label "I have read and agree to the Privacy Policy *"
12. Verifikasi **Footer**: Button [Continue ➔] (solid, primary, lebar penuh, enabled)
13. Verifikasi field Email, field Password, dan Button [Log in] tidak tampil
14. Verifikasi sesi penuh belum dibuat
15. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-08: Urutan Tab keyboard pada layar Confirm to Continue

16. Buka jendela privat baru (tanpa sesi login)
17. Buka halaman Login with Password
18. Ketik email `tonokurniawan+{runId}-020@qwertysystem.net` di field Email
19. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
20. Selesaikan reCAPTCHA
21. Klik [Log in] sampai layar Confirm to Continue tampil
22. Tekan Tab berulang kali sambil mencatat elemen yang fokus
23. Verifikasi urutan fokus: Checkbox persetujuan, tautan dokumen, Button [Continue ➔]
24. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-91: Tautan baca dokumen penuh pada layar Confirm to Continue

25. Buka jendela privat baru (tanpa sesi login)
26. Buka halaman Login with Password
27. Ketik email `tonokurniawan+{runId}-020@qwertysystem.net` di field Email
28. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
29. Selesaikan reCAPTCHA
30. Klik [Log in] sampai layar Confirm to Continue tampil
31. Klik tautan "Read the full Privacy Policy" pada Content Box
32. Verifikasi dokumen Privacy Policy versi aktif terbuka di tab baru
33. Verifikasi layar Confirm to Continue tetap terbuka di tab semula
34. Verifikasi checkbox pada layar Confirm to Continue di tab semula berstatus unchecked
35. Tutup tab dokumen Privacy Policy
36. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-77: Checkbox Agreement tidak dirender di form Login walau akun wajib Agreement

37. Buka jendela privat baru (tanpa sesi login)
38. Buka halaman Login with Password
39. Ketik email `tonokurniawan+{runId}-020@qwertysystem.net` di field Email tanpa mengisi Password
40. Verifikasi Checkbox Agreement tidak tampil di form Login
41. Ketik password nilai `Spectra.env.LP_PASSWORD_WRONG` di field Password
42. Selesaikan reCAPTCHA
43. Klik [Log in]
44. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
45. Verifikasi Checkbox Agreement tetap tidak tampil
46. Verifikasi layar Confirm to Continue tidak tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Urutan: screening layar Confirm to Continue (TC-AUTH-LP-07, 08, 91) lebih dulu, lalu validasi diblokir (TC-AUTH-LP-77), sesuai prinsip 2 dan 3. Layar Confirm to Continue hanya dapat dicapai lewat login ulang, sehingga setiap TC dimulai di jendela privat baru (langkah penghubung, S-03; S-09), termasuk TC-AUTH-LP-77 yang tidak boleh mewarisi sesi pra-auth TC sebelumnya.
- TC-AUTH-LP-141 (sesi penuh tidak dibuat sebelum Agreement dikonfirmasi) diuji di spec defense-in-depth sesi pra-auth, bukan di sini.
- Langkah 35 (menutup tab dokumen) adalah langkah penghubung tanpa awalan `Verifikasi` (S-03).
- Langkah 15, 24, dan 36 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA: TC-AUTH-LP-91 tidak menyebut judul atau URL dokumen Privacy Policy yang diharapkan di tab baru; asersi langkah 32 memakai "dokumen Privacy Policy versi aktif terbuka di tab baru" sesuai Expected TC. Expected TC-AUTH-LP-08 tidak menyebut apakah Button [Continue ➔] termasuk urutan Tab saat checkbox unchecked; spec mengikuti urutan yang tertulis.
