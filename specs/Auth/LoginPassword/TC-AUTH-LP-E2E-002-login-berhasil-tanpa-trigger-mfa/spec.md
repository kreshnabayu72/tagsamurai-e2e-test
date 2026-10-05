---
id: TC-AUTH-LP-E2E-002-login-berhasil-tanpa-trigger-mfa
title: Login berhasil tanpa trigger Agreement maupun MFA
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-8
  - TC-AUTH-LP-10
  - TC-AUTH-LP-47
  - TC-AUTH-LP-51
  - TC-AUTH-LP-88
  - TC-AUTH-LP-89
coverage:
  web: automated
---

# Login berhasil tanpa trigger Agreement maupun MFA

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- `Spectra.env.AUTH_PASSWORD` berisi password user uji aktif. Nilai ini tidak ditulis di spec maupun fixture.
- `Fixture.authLoginPassword.users.routine` berisi user berstatus Activated dan Active yang sudah pernah login sebelumnya, sudah menerima Privacy Policy versi terbaru, dan `last_logout_at`-nya kurang dari 30 hari. User ini bukan Default User dan login dari device serta lokasi yang sama seperti login sebelumnya, sehingga tidak ada anomali yang terdeteksi.
- `Fixture.authLoginPassword.users.maxLengthEmail` berisi user aktif yang panjang emailnya tepat 120 karakter dan sudah melewati seluruh gate.
- `Fixture.authLoginPassword.users.routine.emailTrimmed` berisi salinan email `Fixture.authLoginPassword.users.routine.email` dengan spasi di awal dan di akhir.
- `Fixture.authLoginPassword.users.routine` dipakai juga pada skenario dua perangkat, sehingga session di perangkat kedua milik user yang sama.
- Hook `before` menyiapkan konteks browser kedua yang terpisah dari browser utama, sehingga satu user dapat login dari dua perangkat sekaligus tanpa saling menimpa session.
- `Fixture.authLoginPassword.entities.plans` berisi daftar entity dengan plan Starter, Growth, Professional, Enterprise, dan Custom, serta entity Client, Distributor, Partner, dan Principal.
- Untuk setiap entity dan plan pada daftar di atas, tersedia satu user aktif yang email dan password-nya diketahui.
- Target environment e2e sudah ditentukan dan `spectra.config.ts` sudah diarahkan ke sana. PRD belum menetapkan target ini.

## Test Steps

### Login dengan email yang di-trim

1. Isi field Email dengan `Fixture.authLoginPassword.users.routine.emailTrimmed` dan field Password dengan `Spectra.env.AUTH_PASSWORD`
2. Verifikasi reCAPTCHA diselesaikan sampai tercentang
3. Klik "Log in"
4. Verifikasi caption "Email is not registered yet" tidak muncul, sehingga email di-trim sebelum lookup
5. Verifikasi caption "Incorrect email or password" tidak muncul, sehingga nilai yang sama dikenali sebagai akun terdaftar
6. Verifikasi tidak ada caption lock yang muncul
7. Verifikasi browser berpindah ke Portal — Product Hub
8. Verifikasi sesi aktif terbentuk

### Login dengan email tepat 120 karakter

9. Logout dari Portal sehingga session kosong
10. Isi field Email dengan `Fixture.authLoginPassword.users.maxLengthEmail` yang panjangnya 120 karakter, dan field Password dengan `Spectra.env.AUTH_PASSWORD`
11. Verifikasi caption "Max. 120 characters" tidak muncul pada email sepanjang 120 karakter
12. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
13. Verifikasi submit diproses normal dan tidak ditolak karena panjang email
14. Verifikasi browser berpindah ke Portal — Product Hub
15. Logout dari Portal sehingga session kosong kembali

### Kredensial benar tanpa satu pun kondisi pemicu

16. Isi field Email dengan `Fixture.authLoginPassword.users.routine.email` dan field Password dengan `Spectra.env.AUTH_PASSWORD`
17. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
18. Verifikasi tidak ada layar "Confirm to Continue" yang muncul
19. Verifikasi tidak ada layar MFA yang muncul, sehingga device biasa, jarak di bawah 100 km, bukan login pertama, dan bukan idle 30 hari lolos dalam satu langkah
20. Verifikasi browser berpindah langsung ke Portal — Product Hub
21. Verifikasi sesi penuh dibuat
22. Logout dari Portal sehingga session kosong kembali

### Identik di semua plan dan entity

23. Untuk setiap entity dan plan pada `Fixture.authLoginPassword.entities.plans`, logout dari Portal sehingga session kosong
24. Isi Email dan Password dengan user aktif milik entity dan plan tersebut, selesaikan reCAPTCHA, lalu klik "Log in"
25. Verifikasi tidak ada gating, upsell, maupun tampilan berbeda dari login web biasa
26. Verifikasi browser berpindah ke Portal — Product Hub dengan tampilan sesuai entity
27. Verifikasi seluruh percobaan pada daftar entity selesai tanpa error

### Penyerahan sesi ke Session Management

28. Login dari browser utama dengan `Fixture.authLoginPassword.users.routine.email` lalu verifikasi browser berpindah ke Portal — Product Hub
29. Verifikasi sesi pada perangkat pertama tercatat aktif
30. Buka browser kedua yang sudah disiapkan hook, lalu login dengan `Fixture.authLoginPassword.users.routine.email` yang sama
31. Verifikasi browser kedua berpindah ke Portal — Product Hub
32. Verifikasi sesi pada perangkat kedua terbentuk normal, sehingga login kedua tidak ditolak oleh password
33. Verifikasi kedua sesi tercatat sebagai milik user yang sama
34. Verifikasi limit sesi pada modul Session Management dievaluasi setelah sesi dibuat, bukan pada langkah password
35. Verifikasi tidak ada gating maupun pesan limit sesi yang muncul di dalam modul ini
36. Tutup kedua browser sehingga tidak ada session tersisa

## Notes

- Spec ini menggabungkan enam TC dengan tema yang sama, yaitu login berhasil tanpa pemicu Agreement maupun MFA. Email trimmed, email batas 120 karakter, dan seluruh plan serta entity adalah variasi kondisi user yang sama, jadi digabung di satu spec sesuai e2e-conventions.md bagian 3 prinsip 4.
- Email tepat 120 karakter diuji di sini, sedangkan penolakan 121 karakter diuji di TC-AUTH-LP-E2E-001. Kedua batas itu sengaja dipisah supaya nilai yang diuji tidak bentrok, sesuai e2e-conventions.md bagian 3 prinsip 9.
- Spec ini membuat sesi lalu logouting di setiap akhir bagian. Aksi ini sekaligus berfungsi sebagai pembersihan, sehingga tidak ada data yang tertinggal.
- TC-AUTH-LP-88 berstatus `Manual Only` di TC granular. Menurut e2e-conventions.md bagian 2, label tersebut bukan alasan mengeluarkan TC, sehingga tetap ditulis di sini. Yang diuji hanya handoff-nya; perilaku Duplicate Login Attempt adalah milik modul Session Management.
- Target environment e2e belum ditetapkan di PRD maupun konvensi. Selama `spectra.config.ts` masih menunjuk demo app bawaan TestSpectra, spec ini belum bisa dijalankan. Ini kebutuhan environment, bukan alasan mengeluarkan TC.
- Seluruh akun pada banyak entity dan plan adalah data pre-setup di environment otomasi, bukan data yang dibuat spec ini.
- Placeholder `{time}` pada caption lock tidak dipakai di spec ini karena tidak ada lock aktif.