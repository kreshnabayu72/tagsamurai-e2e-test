---
id: TC-AUTH-RST-E2E-015-ip-counter-types-and-window
title: "Counter per IP: Jenis Request yang Dihitung dan Jendela Bergulir 1 Jam"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-37
  - TC-AUTH-RST-138
coverage:
  web: automated
---

# Counter per IP: Jenis Request yang Dihitung dan Jendela Bergulir 1 Jam

## Prerequisites

- Mode: FE+BE (kelas e: volume 20 Request per jam; kelas d: geser waktu server).
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD` untuk user Active (`U01`–`U14` dan subjek TC-AUTH-RST-138); `I01`–`I03` diseed Inactive dan `N01`–`N04` tidak diseed; tanpa percobaan reset dalam 24 jam. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: fixture BE untuk counter per IP penguji (nol, atau 20 Request dengan cap waktu tertentu) dan pemulihannya di hook `after`; pengatur jam server uji dan jam browser/perangkat (countdown Resend di tiga tab berjalan di jam klien, sehingga keduanya dimajukan bersama pada langkah 10; langkah TC-AUTH-RST-138 hanya menggeser jam server karena jendela 1 jam dihitung di server; jam server dan jam browser dipulihkan ke waktu nyata sebagai langkah aksi di antara kedua bagian, yaitu langkah 19, sehingga TC-AUTH-RST-138 mulai dari jam browser nyata); mail-catcher dengan pembacaan jumlah email per alamat (baseline jumlah email); reCAPTCHA mode uji; beberapa tab browser (kunci Resend pada tiga tab Email Sent! sekaligus).
- State global yang diubah: counter per IP, jam server uji, dan jam browser/perangkat. Suite berjalan serial (`parallel: false`). Pemulihan: jam server dan jam browser dipulihkan sebagai langkah aksi sesudah TC-AUTH-RST-37 (langkah 19), dan ketiganya dipulihkan di hook `after` yang tetap berjalan walau spec gagal di tengah.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE. Spec ini mengatur counter-nya sendiri sesudah reset itu (langkah 1 dan 20).
- TC-AUTH-RST-37, TC-AUTH-RST-138: User belum login (guest); browser web.
- TC-AUTH-RST-37: counter IP penguji = 0 Request dalam 1 jam terakhir. Email berbeda: 14 user Active `U01`–`U14` (`user01+{runId}-015a@qwertysystem.net` ... `user14+{runId}-015a@qwertysystem.net`), 4 email tidak terdaftar `N01`–`N04` (`tak01+{runId}-015a@qwertysystem.net` ... `tak04+{runId}-015a@qwertysystem.net`), dan 3 user Inactive `I01`–`I03` (`nonaktif01+{runId}-015a@qwertysystem.net` ... `nonaktif03+{runId}-015a@qwertysystem.net`), sehingga tiap Request tidak terkena cooldown dan batas per email.
- TC-AUTH-RST-138: counter IP penguji = 20 Request dalam 1 jam terakhir: satu pada T0 dan sembilan belas pada T0+59 menit (fixture BE). T0 ditetapkan di hook `before` sebagai waktu nyata saat itu, dipakai sebagai argumen fixture di langkah 20 dan sebagai acuan langkah 21. User `Budi Santoso` (`budisantoso+{runId}-015b@qwertysystem.net`) Active tanpa percobaan dalam 24 jam.

## Test Steps

### TC-AUTH-RST-37: Jenis Request yang menaikkan counter per IP dalam jendela 1 jam

1. Atur counter IP penguji menjadi 0 Request dalam 1 jam terakhir (fixture BE)
2. Buka jendela privat baru lalu buka halaman Reset Password (Request)
3. Kirim 3 Request valid (reCAPTCHA terselesaikan) untuk `U01`, `U02`, dan `U03`, masing-masing di tab sendiri, dan biarkan ketiga tab berada di halaman Email Sent!
4. Verifikasi ketiga tab menampilkan halaman Email Sent!
5. Kirim Request valid untuk `U04` sampai `U10` (7 Request), `N01` sampai `N04` (4 Request), dan `I01` sampai `I03` (3 Request) dari IP yang sama sehingga total 17 Request
6. Verifikasi tiap Request Active menampilkan halaman Email Sent!
7. Verifikasi tiap Request email tidak terdaftar menampilkan caption "Email is not registered yet"
8. Verifikasi tiap Request Inactive menampilkan caption "Your account is inactive"
9. Verifikasi tidak ada Request di antara 17 Request yang ditolak 429
10. Majukan jam server dan jam browser 61 detik lalu klik [Resend email] di setiap tab (3 Resend dari akun Active)
11. Kirim Request ke-18, ke-19, dan ke-20 untuk `U11`, `U12`, dan `U13`
12. Verifikasi Request ke-18 menampilkan halaman Email Sent! tanpa penolakan 429
13. Verifikasi Request ke-19 menampilkan halaman Email Sent! tanpa penolakan 429
14. Verifikasi Request ke-20 menampilkan halaman Email Sent! tanpa penolakan 429
15. Verifikasi Request ke-20 masih diproses tanpa penolakan 429 (Resend pada langkah sebelumnya tidak menambah counter)
16. Kirim Request ke-21 untuk `U14`
17. Verifikasi Request ke-21 ditolak dengan Alert Danger di atas Button [Reset Password]
18. Verifikasi Request ke-21 ditolak dengan Alert Danger bertuliskan "Too many requests. Please try again later."
19. Pulihkan jam server dan jam browser ke waktu nyata

### TC-AUTH-RST-138: Jendela per IP bergulir: Request tertua melewati 1 jam

20. Atur counter IP penguji menjadi 20 Request dalam 1 jam terakhir: satu pada T0 dan sembilan belas pada T0+59 menit (fixture BE)
21. Majukan jam server (tanpa jam browser) ke T0+1 jam 1 menit
22. Buka halaman Reset Password (Request) di jendela privat baru
23. Periksa mail-catcher dan catat jumlah email untuk `budisantoso+{runId}-015b@qwertysystem.net` sebagai baseline B1
24. Ketik `budisantoso+{runId}-015b@qwertysystem.net` pada field Email
25. Selesaikan reCAPTCHA (centang "I'm not a robot")
26. Klik Button [Reset Password]
27. Verifikasi browser menuju halaman Email Sent!
28. Verifikasi tidak ada toast
29. Verifikasi Request tidak ditolak 429 (jendela bergulir, Request tertua sudah keluar dari 1 jam)
30. Periksa mail-catcher
31. Verifikasi jumlah email untuk `budisantoso+{runId}-015b@qwertysystem.net` bertambah satu dibanding baseline B1 (email reset baru masuk)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Request pada langkah 3 dan 11 TC-AUTH-RST-37 menjadi bagian dari 20 Request; 3 tab Email Sent! dipertahankan sampai Resend (langkah 10). Countdown Resend dipenuhi dengan memajukan jam server dan jam browser 61 detik (bukan menunggu nyata).
- Titik tepat tepi jendela 1 jam tidak diuji: ditahan oleh `GAP-467` di TC sumber.
- Counter IP, jam server, dan jam browser dipulihkan di hook `after`.
- P-4 (state global bersama): TC-AUTH-RST-37 (kelas e) dan TC-AUTH-RST-138 (kelas d) berbagi counter Request per IP penguji dan membangunnya berurutan; hook `beforeEach` suite me-reset counter itu sebelum spec dan state awal tiap bagian ditulis di `## Prerequisites` (langkah 1 dan 20). Geser jam server dan jam browser pada TC-AUTH-RST-37 hanya memenuhi countdown Resend (rutin, bukan objek uji); satu-satunya objek uji kelas d adalah jendela 1 jam pada TC-AUTH-RST-138.
- Langkah penghubung (S-03): membuka jendela privat baru (langkah 2 dan 22) dan memulihkan jam server dan jam browser ke waktu nyata antara kedua TC (langkah 19; S-09) bukan asersi TC.
- Langkah Resend TC-AUTH-RST-37 tetap sebagai aksi (langkah 10); asersi "Resend tidak menambah counter" adalah Expected b TC-AUTH-RST-37 dan diasersi pada langkah 15 (Request ke-20 masih diproses). Expected a untuk Request ke-18 sampai ke-20 diasersi pada langkah 12 sampai 14.
- Temuan untuk QA: Post Condition TC-AUTH-RST-138 ("Token reset aktif baru terbit untuk Budi") tidak punya langkah observasi di TC sehingga tidak diasersi; email baru di mail-catcher tidak membuktikan status token (S-01, S-15).
