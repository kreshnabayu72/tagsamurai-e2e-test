---
id: TC-AUTH-OTP-E2E-004-mobile-attestation-play-integrity
title: "Token Attestation Play Integrity pada Request OTP dan Resend di Aplikasi Mobile"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-185
  - TC-AUTH-OTP-180
coverage:
  mobile: automated
---

# Token Attestation Play Integrity pada Request OTP dan Resend di Aplikasi Mobile

## Prerequisites

- Mode: FE+BE (mobile Android, ditambah satu konteks browser admin). Aplikasi mobile TAG Samurai terpasang pada perangkat Android dengan Play Integrity yang valid, belum login.
- Kemampuan teknis (kelas harness eksternal): kemampuan mengganti token attestation yang dikirim aplikasi menjadi kosong atau invalid lewat failure injection, lalu memulihkannya menjadi valid; pengaturan jam server dan jam perangkat/emulator Android bersama (countdown Resend berjalan di jam perangkat, bagian 6 konvensi); mail-catcher lingkungan uji dapat dibaca.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Hook `before` membuka browser admin dan login sebagai akun aktor itu; langkah uji hanya berpindah konteks ke browser itu.
- State global yang diubah: jam server dan jam perangkat/emulator. Suite berjalan serial (`parallel: false`).
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `OTP_PASSWORD` (password user uji Activated yang di-seed). Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-185: `Tari Wicaksono` (`tariwicaksono+{runId}-004@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-180: `Rizky Santoso` (`rizkysantoso+{runId}-004@qwertysystem.net`), profil BASE
- Pemulihan state: hook `after` mengembalikan token attestation aplikasi ke valid, memulihkan jam server dan jam perangkat/emulator ke waktu nyata, mengakhiri sesi login di aplikasi mobile (bila spec berhenti sebelum langkah logout), dan menutup sesi browser admin (tetap jalan walau spec gagal di tengah).

## Test Steps

### TC-AUTH-OTP-185: Aplikasi mobile dengan attestation invalid ditolak sebagai captcha kosong pada Request OTP dan Resend

1. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session`, dan catat jumlah entri user `Tari Wicaksono` sebagai baseline
2. Ganti konteks ke aplikasi mobile
3. Atur token attestation yang dikirim aplikasi menjadi kosong atau invalid (failure injection)
4. Buka halaman Request OTP di aplikasi mobile
5. Ketik `tariwicaksono+{runId}-004@qwertysystem.net` pada field Email
6. Ketuk button [Request OTP]
7. Verifikasi toast error "Error, failed to log in." tampil
8. Verifikasi tidak ada email OTP terkirim ke `tariwicaksono+{runId}-004@qwertysystem.net` di mail-catcher
9. Verifikasi aplikasi tetap di halaman Request OTP
10. Ganti konteks ke browser admin
11. Buka `Global Settings > Activity Log > Session` dan muat ulang daftar entri user `Tari Wicaksono`
12. Verifikasi jumlah entri user `Tari Wicaksono` bertambah 1 dibanding baseline
13. Verifikasi entri baru itu memuat Activity "Login", Status "Failed", dan Note "Captcha not completed"
14. Ganti konteks ke aplikasi mobile dan pulihkan token attestation menjadi valid
15. Buka halaman Request OTP di aplikasi mobile
16. Ketik `tariwicaksono+{runId}-004@qwertysystem.net` pada field Email
17. Ketuk button [Request OTP]
18. Verifikasi halaman Verify OTP tampil
19. Ambil kode OTP 6 digit dari email yang masuk ke mail-catcher untuk `tariwicaksono+{runId}-004@qwertysystem.net`
20. Atur kembali token attestation menjadi kosong atau invalid
21. Majukan jam server dan jam perangkat/emulator bersama sebesar 60 detik sehingga countdown Resend selesai
22. Ketuk [Resend code]
23. Verifikasi toast error "Error, failed to send the code." tampil
24. Pulihkan jam server dan jam perangkat/emulator ke waktu nyata
25. Ganti konteks ke browser admin dan muat ulang `Global Settings > Activity Log > Session`
26. Verifikasi jumlah entri user `Tari Wicaksono` tetap sama dengan jumlah pada langkah 12 (tidak ada entri log baru setelah Resend yang ditolak)
27. Ganti konteks ke aplikasi mobile
28. Ketik 6 digit kode OTP dari langkah 19 pada kotak digit
29. Verifikasi kode lama tetap valid dan diterima
30. Verifikasi login berhasil
31. Pulihkan token attestation menjadi valid
32. Keluar (logout) dari akun di aplikasi mobile sehingga aplikasi kembali belum login

### TC-AUTH-OTP-180: Aplikasi mobile dengan token attestation valid meminta OTP tanpa reCAPTCHA

33. Buka halaman Request OTP di aplikasi mobile (token attestation valid)
34. Ketik `rizkysantoso+{runId}-004@qwertysystem.net` pada field Email
35. Ketuk button [Request OTP]
36. Verifikasi toast sukses "Success, the code has been sent." tampil
37. Verifikasi halaman Verify OTP tampil
38. Verifikasi tidak ada caption reCAPTCHA
39. Verifikasi email OTP diterima di `rizkysantoso+{runId}-004@qwertysystem.net` di mail-catcher

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`. Kedua TC bertanda Automation `Manual Only` di sumber; kebutuhan failure injection attestation dan perangkat Android ditulis di Prerequisites sesuai bagian 2 konvensi.
- Urutan TC di spec: 185 lebih dulu, lalu 180, karena penolakan (alur diblokir) ditempatkan sebelum alur sukses (prinsip 3 bagian 3). Urutan ini berbeda dari urutan nomor sumber.
- Langkah penghubung tanpa asersi (S-03): langkah 1 sampai 3 dan 10 (baseline jumlah entri log, pindah konteks, pengaturan attestation), langkah 11 (muat ulang daftar log), langkah 14 dan 31 (pemulihan attestation), langkah 19 (membaca kode OTP dari mail-catcher untuk dipakai di langkah 28), langkah 20 dan 21 (attestation invalid kembali dan pemajuan jam), langkah 24 (pemulihan jam server dan jam perangkat/emulator setelah Resend), serta langkah 32 (logout dari aplikasi mobile: TC-AUTH-OTP-185 mengakhiri langkah 30 dengan login berhasil, sedangkan TC-AUTH-OTP-180 mensyaratkan aplikasi belum login). Langkah 28 sampai 30 menambah pembuktian "kode lama tetap valid" (Expected c) dengan mengetik kode lama; ini satu-satunya cara memverifikasi klausa itu.
- Pengecualian P-1 (state berat, termasuk asersi absence kelas g milik TC itu): asersi TC-AUTH-OTP-185 butir c ("tidak ada entri log baru" setelah Resend yang ditolak, langkah 26) tetap di spec ini dan tidak dipindah ke spec absence E2E-040, karena bergantung pada state attestation invalid dan sesi Verify OTP yang baru dibangun lewat failure injection. Langkah 25 dan 27 adalah langkah penghubung (S-03) pindah konteks ke browser admin dan kembali; asersi dilakukan sebelum kode lama diketik supaya entri Success login tidak ikut terhitung.
- Panjang spec (sekitar 39 langkah, melewati smell 35) beralasan: TC-AUTH-OTP-185 satu alur kontinu yang berurutan (Request OTP ditolak, log dibaca, attestation dipulihkan, sesi Verify OTP dibangun, Resend ditolak, kode lama dipakai) dan tidak bisa dipotong tanpa membangun ulang state berat; TC-AUTH-OTP-180 memakai konteks aplikasi mobile yang sama (P-1).
- Jam: countdown Resend berjalan di jam perangkat, sehingga langkah 21 memajukan jam server dan jam perangkat/emulator bersama; keduanya dipulihkan di langkah 24 dan, sebagai cadangan, di hook `after`.
- Mode reCAPTCHA tidak relevan: aplikasi mobile tidak merender reCAPTCHA.
- Spec ini memadukan dua kelas harness eksternal: failure injection token attestation pada aplikasi mobile dan satu konteks browser admin untuk membaca Activity Log. Pemisahan tidak dilakukan karena asersi log TC-AUTH-OTP-185 bergantung pada state attestation invalid yang baru dibangun (lihat pengecualian P-1 di atas); kedua TC memakai konteks aplikasi mobile yang sama.
- Temuan untuk QA:
  - TC-AUTH-OTP-185 Post Condition "Tidak ada kode OTP baru yang aktif" tidak punya langkah observasi di TC (email di mail-catcher tidak dicek di Expected c, hanya "tidak ada entri log baru"); spec tidak mengasersikannya. Mohon QA menambah langkah atau Expected padanan bila cakupan ini diinginkan.
  - TC-AUTH-OTP-185 Post Condition menyebut "Tidak ada kode OTP baru yang aktif dari langkah 3 dan 5", sedangkan langkah 5 (setelah attestation dipulihkan) menerbitkan kode OTP yang valid dan Expected c menyatakan "kode lama tetap valid". Spec mengartikan kode yang diterbitkan pada langkah 5 tetap aktif dan hanya Resend yang tidak menerbitkan kode baru; mohon QA mengonfirmasi redaksi Post Condition.
  - TC-AUTH-OTP-185 Expected b menulis Activity "Login", sedangkan TC pencatatan lain memakai Activity `Login with OTP`; spec mengikuti redaksi TC ini.
  - TC-AUTH-OTP-185 langkah 5 memuat banyak aksi dalam satu butir (ulangi 1–3, kembalikan attestation, ketuk Resend setelah cooldown); spec menguraikannya satu aksi per langkah.
