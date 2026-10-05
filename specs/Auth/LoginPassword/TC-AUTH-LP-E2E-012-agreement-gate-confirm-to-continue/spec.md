---
id: TC-AUTH-LP-E2E-012-agreement-gate-confirm-to-continue
title: Agreement gate pada layar Confirm to Continue, dari screening sampai checkbox tidak dicentang
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-19
  - TC-AUTH-LP-20
  - TC-AUTH-LP-21
  - TC-AUTH-LP-22
  - TC-AUTH-LP-23
  - TC-AUTH-LP-24
  - TC-AUTH-LP-90
coverage:
  web: automated
---

# Agreement gate pada layar Confirm to Continue, dari screening sampai checkbox tidak dicentang

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan lima user uji, dibuat lewat API Global Settings > User dan direstore di `afterEach`:
  - `Fixture.authLoginPassword.users.firstLogin` dengan `first_login_at` kosong, sehingga login pertama sejak aktivasi
  - `Fixture.authLoginPassword.users.idle30Days` dengan `last_logout_at` lebih dari 30 hari lalu
  - `Fixture.authLoginPassword.users.staleConsent` dengan `user_privacy_consent.accepted_version` lebih lama dari versi Privacy Policy aktif
  - `Fixture.authLoginPassword.users.currentConsent` yang sudah menerima versi Privacy Policy aktif, `last_logout_at` kurang dari 30 hari, dan `first_login_at` terisi
  - `Fixture.authLoginPassword.users.deviceKnown` yang `device` dan `geolokasi`-nya sudah tercatat sehingga login tidak memicu MFA
- Kelima user bukan Default User. Password asli masing-masing tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.users.staleConsent.newPolicyVersion` berisi versi Privacy Policy baru yang dipakai untuk memperbarui `platform_privacy_policy`.
- Hook `before` mengembalikan `platform_privacy_policy` ke versi semula di `afterEach`, supaya spec ini tidak mengubah kondisi global bagi spec lain.
- `Fixture.authLoginPassword.captions.agreementRequired` berisi caption error agreement belum dicentang.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Editor Privacy Policy ada di Admin Console > Settings > Privacy Policy untuk langkah 14 dan 15.

## Test Steps

### Agreement terpicu oleh login pertama

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.firstLogin.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
3. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
4. Verifikasi browser berpindah ke layar "Confirm to Continue"
5. Verifikasi judul layar adalah "Confirm to Continue"
6. Verifikasi ada content box ringkasan perubahan dengan teks yang menjelaskan persetujuan terhadap Terms of Service dan Privacy Policy
7. Verifikasi checkbox agreement tampil dengan label "I have read and agree to the Terms of Service and Privacy Policy"
8. Verifikasi checkbox agreement dalam keadaan unchecked secara default
9. Verifikasi tombol "Continue to Dashboard ➔" tampil dalam keadaan enabled
10. Verifikasi tidak ada tombol "Log in" yang tersisa di layar ini
11. Verifikasi belum ada entri "Success" di User Log, sehingga sesi belum dibuat penuh
12. Verifikasi belum ada entri "Consent not given", sehingga upaya login belum dianggap gagal

### Klik Continue tanpa mencentang checkbox

13. Klik "Continue to Dashboard ➔" tanpa mencenang checkbox
14. Verifikasi border checkbox berubah menjadi merah
15. Verifikasi caption error di bawah checkbox adalah "You need to agree to the Privacy Policy to continue"
16. Verifikasi tidak ada request confirm-agreement yang dikirim ke server, sehingga penolakan ini murni di sisi klien
17. Verifikasi jumlah entri di User Log tidak berubah, sehingga tidak ada entri log baru
18. Verifikasi layar "Confirm to Continue" tetap terbuka

### Centang dan lanjutkan

19. Centang checkbox agreement
20. Verifikasi border checkbox kembali normal dan caption error hilang
21. Klik "Continue to Dashboard ➔"
22. Verifikasi consent user untuk versi Privacy Policy aktif tersimpan
23. Verifikasi browser berpindah ke layar MFA atau ke Portal — Product Hub, sesuai hasil evaluasi tahap berikutnya
24. Verifikasi jumlah entri di User Log bertambah satu setelah login final tuntas, dengan Status "Success" dan Note "Login with password"
25. Verifikasi tidak ada Note terpisah untuk langkah confirm agreement itu sendiri

### Agreement terpicu oleh idle lebih dari 30 hari

26. Logout bila ada sesi, lalu buka `/login`
27. Isi Email dengan `Fixture.authLoginPassword.users.idle30Days.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
28. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
29. Verifikasi browser berpindah ke layar "Confirm to Continue"
30. Verifikasi judul layar adalah "Confirm to Continue" dan checkbox dalam keadaan unchecked
31. Centang checkbox lalu klik "Continue to Dashboard ➔"
32. Verifikasi browser berpindah ke layar MFA atau ke Portal — Product Hub sesuai hasil evaluasi tahap berikutnya

### Agreement terpicu oleh Privacy Policy versi baru

33. Logout bila ada sesi
34. Login sebagai Principal pada Admin Console > Settings > Privacy Policy
35. Terbitkan versi Privacy Policy baru dengan nomor versi dari `Fixture.authLoginPassword.users.staleConsent.newPolicyVersion`
36. Verifikasi versi baru tercatat sebagai versi aktif
37. Logout dari akun Principal sehingga session kosong
38. Buka `/login` lalu isi Email dengan `Fixture.authLoginPassword.users.staleConsent.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
39. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
40. Verifikasi browser berpindah ke layar "Confirm to Continue"
41. Verifikasi judul layar adalah "Confirm to Continue" dan checkbox dalam keadaan unchecked
42. Centang checkbox lalu klik "Continue to Dashboard ➔"
43. Verifikasi browser berpindah ke layar MFA atau ke Portal — Product Hub
44. Verifikasi nomor versi consent user kini sama dengan versi aktif, sehingga penyebab versi policy tidak memicu gate lagi bagi user ini

### Tanpa kondisi trigger, layar di-skip total

45. Logout bila ada sesi
46. Buka `/login` lalu isi Email dengan `Fixture.authLoginPassword.users.currentConsent.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
47. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
48. Verifikasi layar "Confirm to Continue" tidak pernah muncul
49. Verifikasi browser berpindah langsung ke Portal — Product Hub
50. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"

## Notes

- Layar ini hanya muncul setelah password terbukti benar dan sebelum evaluasi MFA. Checkbox agreement tidak pernah dirender di halaman Login itu sendiri, dan itu sudah diuji di TC-AUTH-LP-E2E-001 langkah 8.
- Copy label checkbox dan tombol mengikuti PRD §4.5, yaitu "I have read and agree to the Terms of Service and Privacy Policy" dan "Continue to Dashboard ➔". TC-AUTH-LP-90 menuliskan copy yang berbeda; konflik ini dicatat di `gap-spec/gap-tc.md`.
- Spec ini menggabungkan tiga kondisi pemicu dan kondisi tidak-terpicu. Semuanya menghasilkan layar yang sama dengan aksi yang sama, jadi satu spec sesuai e2e-conventions.md bagian 3 prinsip 4.
- User untuk tiap kondisi dibuat lewat API Global Settings > User dan direstore di `afterEach`. Hook juga mengembalikan versi Privacy Policy aktif ke semula, karena itu perubahan global yang bisa memengaruhi spec lain.
- Handoff ke MFA setelah confirm agreement ada di TC-AUTH-LP-E2E-014. Di sini hanya dibuktikan bahwa evaluation tahap berikutnya dijalankan, tanpa menelusuri alur MFA.
- Spec ini tidak ditutup dengan meninggalkan layar dalam keadaan setengah jadi. Bagian terakhir justru membuktikan kasus tidak-terpicu, sehingga tidak ada preAuthToken yang menggantung dari spec ini. Kasus tutup layar dan token kedaluwarsa ada di TC-AUTH-LP-E2E-013.
- Login dengan email yang dihapus dan email yang belum terdaftar menghasilkan caption yang sama, dan itu diuji di TC-AUTH-LP-E2E-011.