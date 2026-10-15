---
id: TC-AUTH-OTP-E2E-022-resend-kuota-habis-dan-cooldown-10-menit
title: "Resend Sampai Kuota Habis, Cooldown 10 Menit, dan State Exhausted"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-79
  - TC-AUTH-OTP-80
  - TC-AUTH-OTP-181
  - TC-AUTH-OTP-82
  - TC-AUTH-OTP-81
coverage:
  web: automated
---

# Resend Sampai Kuota Habis, Cooldown 10 Menit, dan State Exhausted

## Prerequisites

- Mode: FE+BE.
- Tanpa login (halaman publik, tidak ada sesi aktif di browser). reCAPTCHA memakai mode uji environment.
- Kemampuan teknis:
  - Mail-catcher lingkungan uji untuk membaca email dan kode OTP 6 digit.
  - Percepatan jam (§6): langkah "Tunggu countdown 60 detik selesai" dan "Tunggu countdown 10 menit selesai" dipenuhi dengan memajukan jam server uji dan jam browser (countdown UI berjalan di jam klien) bersama sebesar durasi itu, lalu menunggu UI menyegarkan state tombol Resend. Jam server dan jam browser diatur bersama dan tidak ada tunggu waktu nyata. Jam tidak dimajukan antara langkah 18 dan langkah 30 supaya sisa hitung mundur 10 menit yang dicatat pada langkah 18 dapat dibandingkan di langkah 30. Spec ini mengubah state global (jam, kuota Resend), sehingga suite berjalan serial (`parallel: false`), dan hook `after` memulihkan jam.
  - Pengiriman permintaan Resend langsung ke server (klien HTTP dari IP yang sama dengan browser uji) untuk TC-AUTH-OTP-181 (langkah 19 spec ini), tanpa melalui tombol UI.
- Environment variable: `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Hook `before` (seeding API, email bersuffix per run) membuat satu user Activated dengan Toggle Active ON, profil BASE (sudah login web dalam 30 hari terakhir pada device dikenal, persetujuan Privacy Policy versi terbaru ada, MFA tidak aktif; Tabel Data Uji Pre-setup #2): `Citra Hidayati` (`citrahidayati+{runId}-022@qwertysystem.net`).
- Hook `after`: kembalikan jam server dan jam browser uji ke waktu nyata dan hapus user `Citra Hidayati`. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-79: Resend ke-1 sampai ke-4 mengikuti countdown 60 detik yang sama

1. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
2. Ketik `citrahidayati+{runId}-022@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ulangi empat kali (Resend ke-1 sampai ke-4), pada tiap pengulangan:
   - Tunggu countdown 60 detik selesai
   - Verifikasi button [Resend code] kembali enabled
   - Klik [Resend code]
   - Verifikasi toast sukses: "Success, the code has been sent."
   - Verifikasi area Resend kembali ke "Resend code in (00:59)"
   - Verifikasi area Resend dalam keadaan disabled
6. Verifikasi setelah Resend ke-4 tidak muncul teks "Resend code in (09:59)" maupun teks Exhausted
7. Periksa mail-catcher untuk `citrahidayati+{runId}-022@qwertysystem.net` dan hitung jumlah email OTP
8. Verifikasi mail-catcher memuat tepat 5 email OTP (1 dari Request OTP dan 4 dari Resend)

### TC-AUTH-OTP-80: Resend ke-5 menghabiskan kuota dan mengunci tombol selama 10 menit

9. Catat kode OTP terbaru dari email (kode sebelum Resend ke-5)
10. Tunggu countdown 60 detik selesai
11. Klik [Resend code] (Resend ke-5)
12. Verifikasi toast sukses: "Success, the code has been sent."
13. Verifikasi area Resend menampilkan "Resend code in (09:59)" (State C)
14. Verifikasi area Resend State C dalam keadaan disabled
15. Verifikasi email OTP baru diterima di mail-catcher `citrahidayati+{runId}-022@qwertysystem.net`
16. Ketik kode OTP yang dicatat pada langkah 9 pada kotak digit
17. Verifikasi kode sebelumnya ditolak: caption error di bawah kotak digit "Invalid code"

### TC-AUTH-OTP-181: Resend dan Request OTP saat cooldown 10 menit berjalan ditolak tanpa menambah jumlah resend

18. Catat sisa hitung mundur pada area Resend dan catat jumlah email OTP di mail-catcher untuk `citrahidayati+{runId}-022@qwertysystem.net` (jumlah N)
19. Pada fase "Resend code in (09:59)" kirim permintaan Resend langsung ke server
20. Verifikasi Resend langsung ditolak server
21. Verifikasi tidak ada email OTP baru di mail-catcher
22. Klik tautan [Back to Login with Password]
23. Klik tautan [Log in with OTP]
24. Centang widget reCAPTCHA "I'm not a robot"
25. Klik button [Request OTP]
26. Verifikasi Request OTP ditolak dengan Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
27. Verifikasi layar tetap di Request OTP
28. Verifikasi tidak ada email OTP baru di mail-catcher
29. Tekan tombol Back browser sampai layar Verify OTP tampil
30. Verifikasi cooldown 10 menit tidak diperpanjang oleh penolakan: sisa hitung mundur tidak melebihi sisa yang dicatat sebelum penolakan
31. Verifikasi jumlah resend tidak bertambah oleh penolakan: jumlah email OTP di mail-catcher tetap N yang dicatat pada langkah 18 (tidak ada email baru dari langkah 19 dan 25)

### TC-AUTH-OTP-82: Pada state Exhausted tautan Edit email tetap tersedia sebagai jalan keluar

32. Tunggu countdown 10 menit selesai
33. Verifikasi tautan [Edit email] di bawah Subtitle tampil
34. Verifikasi tautan [Edit email] dalam keadaan enabled
35. Verifikasi button [Resend code] disabled
36. Verifikasi button [Resend code] menampilkan teks Exhausted

### TC-AUTH-OTP-81: Setelah cooldown 10 menit selesai tombol Resend tetap disabled dengan teks Exhausted

37. Klik button [Resend code]
38. Verifikasi button [Resend code] tetap disabled (tidak enabled kembali)
39. Verifikasi teks statis di area Resend: "You've used all your resend attempts for this code. Edit your email to request a new one."
40. Verifikasi klik button disabled tidak mengirim email baru di mail-catcher
41. Verifikasi klik button disabled tidak memunculkan toast

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Pengecualian P-1 (state berat) dan P-3 (user berurutan) dari `docs/e2e-conventions.md` §3: kelima TC memakai lima user berbeda di sumber (`Citra Hidayati`, `Joko Anggraini`, `Nur Lestari`, `Bagas Ramadhan`, `Anisa Gunawan`) dan masing-masing mengulang 5 Resend plus tunggu 10 menit. Spec memakai satu user (`Citra Hidayati`) dengan urutan 79, 80, 181, 82, 81 supaya kuota 5 Resend dan cooldown 10 menit dibangun sekali. Urutan 181 sebelum 82 dan 81 karena 181 hanya valid pada fase cooldown 10 menit (09:59), sedangkan 82 dan 81 menguji setelah cooldown selesai. Urutan di sumber (79, 80, 81, 82, 181) berubah mengikuti alasan ini.
- Langkah penghubung (S-03): langkah 9 (mencatat kode sebelum Resend ke-5 supaya Expected c TC-80 dapat diasersi), langkah 29 (Back browser untuk kembali ke layar Verify OTP setelah penolakan Request OTP, cara yang sama dengan TC-179).
- Asersi tambahan (dicatat sesuai S-03): langkah 16 dan 17 (kode lama ditolak "Invalid code") menurunkan Expected c TC-80 "Kode sebelumnya tidak dapat dipakai lagi" memakai caption NC-01; langkah 18 (mencatat sisa hitung mundur sebagai baseline dan jumlah email N di mail-catcher) dan 30 menurunkan Expected c TC-181 "tidak memperpanjang cooldown 10 menit"; langkah 31 menurunkan Expected c TC-181 "tidak menambah jumlah resend" lewat hitungan email di mail-catcher.
- Tidak ada asersi pencatatan log pada spec ini; entri log sesi untuk percobaan ditolak dan Resend tidak dicatat dicakup spec absence E2E-040.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC-181 langkah 15 ("kirim permintaan Resend langsung ke server") tidak menyebut mekanisme request langsung; spec menulis kemampuan klien HTTP di Prerequisites tanpa menyebut endpoint. Langkah ini sebenarnya kelas defense-in-depth (a) yang tetap di spec ini karena bergantung pada state cooldown 10 menit yang berat.
  - TC-81 dan TC-82 Expected menyebut button disabled dengan teks "Exhausted" sedangkan TC-81 juga menulis teks statis "You've used all your resend attempts for this code. Edit your email to request a new one."; tidak jelas apakah kata "Exhausted" tampil sebagai label tombol atau hanya nama state. Spec mengasersi keduanya sebagaimana ditulis TC (langkah 36 dan 39).
  - TC-81 Post Condition a ("Jumlah resend sesi tetap 5") tidak punya langkah observasi di TC, sedangkan Expected c (klik button disabled tidak mengirim email) sudah diasersi di langkah 40 dan 41; spec tidak menambah langkah observasi sendiri (S-01). Mohon QA menambah langkah observasi jumlah resend di TC-81.
  - TC-79, 80, 81, 82, 181 di sumber berdiri sendiri dengan lima user, dan TC tidak menyatakan bahwa kelimanya dijalankan berurutan pada satu sesi email-request dengan kuota yang dibangun sekali; spec mengasumsikan urutan itu (P-3).
