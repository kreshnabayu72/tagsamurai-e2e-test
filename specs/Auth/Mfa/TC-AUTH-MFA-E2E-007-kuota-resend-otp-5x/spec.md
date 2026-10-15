---
id: TC-AUTH-MFA-E2E-007-kuota-resend-otp-5x
title: "Kuota Resend OTP 5 Kali per Sesi Pre-Auth"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-79
  - TC-AUTH-MFA-82
coverage:
  web: automated
---

# Kuota Resend OTP 5 Kali per Sesi Pre-Auth

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, sudah pernah login sukses di web, Authenticator belum terdaftar; TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B; login dari browser uji B memicu MFA karena ID device belum dikenali; tanpa layar Confirm to Continue), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-79: `Jihan Aulia` (`jihanaulia+{runId}-007@qwertysystem.net`)
  - TC-AUTH-MFA-82: `Misbah Fauzi` (`misbahfauzi+{runId}-007@qwertysystem.net`)
- Hook `after`: pulihkan jam server uji dan jam browser uji ke waktu nyata, lalu hapus kedua user (beserta sesi web yang terbentuk dari TC-AUTH-MFA-82). Hook ini tetap jalan walau spec gagal di tengah, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk kedua TC. TC kedua dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kuota Resend: tiap TC menghabiskan seluruh kuota 5 kali Resend dalam satu sesi pre-auth, sehingga tiap user harus berupa user dan sesi pre-auth baru. Hitung mundur 60 detik antar Resend dan penantian 2 menit pada TC-AUTH-MFA-79 dipenuhi dengan mengatur jam (konvensi bagian 6), bukan menunggu waktu nyata: jam server uji dan jam browser uji dimajukan bersama, karena hitung mundur UI berjalan di jam klien dan memajukan jam server saja tidak mengaktifkan `[Resend code]`. Total pergeseran per TC adalah 5 × 60 detik ditambah 2 menit pada TC-AUTH-MFA-79 (7 menit) dan 5 × 60 detik pada TC-AUTH-MFA-82 (5 menit), keduanya di bawah TTL sesi pre-auth 10 menit. Kode OTP terakhir diterbitkan pada Resend ke-5 sehingga masih berusia di bawah TTL kode 5 menit pada tiap asersi. Jam server dan jam browser dipulihkan ke waktu nyata di akhir tiap TC (langkah eksplisit), dengan hook `after` sebagai cadangan.
- Kemampuan teknis: jendela privat; reCAPTCHA mode uji di environment; pengaturan jam server uji dan jam browser uji (dimajukan bersama dan dipulihkan ke waktu nyata); mail-catcher lingkungan uji untuk menghitung jumlah email OTP faktor-2 per user (baseline jumlah email sebelum aksi, 6 email baru setelah 5 Resend) dan membaca kode terakhir.
- Kemampuan teknis, seeding state BE per user: status Activated dan Active ON, sudah pernah login sukses di web (lokasi dan waktu login terakhir, logout web terakhir kurang dari 30 hari), consent sudah disetujui sehingga tanpa layar Confirm to Continue, dan Authenticator belum terdaftar. Mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji dan jam browser uji; hook `after` memulihkan jam server uji dan jam browser uji.

## Test Steps

### TC-AUTH-MFA-79: Resend dibatasi 5 kali per sesi pre-auth lalu disabled sampai sesi berakhir

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `jihanaulia+{runId}-007@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email" pada halaman Choose Verification Method
7. Catat jumlah email di mail-catcher untuk `jihanaulia+{runId}-007@qwertysystem.net` sebagai baseline
8. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `jihanaulia+{runId}-007@qwertysystem.net`
9. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-1)
10. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-2)
11. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-3)
12. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-4)
13. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-5)
14. Amati button Resend setelah Resend ke-5
15. Verifikasi Button Resend disabled
16. Verifikasi Button [Resend code] tanpa hitung mundur
17. Verifikasi Button [Resend code] menampilkan teks statis: "You've used all your resend attempts. Use a different method."
18. Majukan jam server uji dan jam browser uji 2 menit lalu amati button Resend
19. Verifikasi Button Resend tetap disabled (tidak aktif kembali selama sesi pre-auth yang sama)
20. Verifikasi Email OTP faktor-2 yang diterima di `jihanaulia+{runId}-007@qwertysystem.net` sejak baseline berjumlah 6 (1 pengiriman awal + 5 Resend)
21. Verifikasi Tidak ada email ke-7 (jumlah email sejak baseline tetap 6)
22. Pulihkan jam server uji dan jam browser uji ke waktu nyata

### TC-AUTH-MFA-82: Memilih OTP via email lagi setelah kuota Resend habis tidak mengirim OTP baru

23. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
24. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
25. Ketik `misbahfauzi+{runId}-007@qwertysystem.net` pada field Email
26. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
27. Centang widget reCAPTCHA "I'm not a robot"
28. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
29. Pilih opsi "OTP via email" pada halaman Choose Verification Method
30. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `misbahfauzi+{runId}-007@qwertysystem.net`
31. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-1)
32. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-2)
33. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-3)
34. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-4)
35. Majukan jam server uji dan jam browser uji 60 detik sehingga hitung mundur selesai, lalu klik button [Resend code] (Resend ke-5)
36. Catat jumlah email di mail-catcher untuk `misbahfauzi+{runId}-007@qwertysystem.net` sebagai baseline (setelah Resend ke-5)
37. Klik button Text [Use a different method]
38. Pilih opsi "OTP via email" lalu klik button [Login]
39. Verifikasi Halaman `Auth > MFA > OTP Verification` tampil
40. Verifikasi Button Resend tetap disabled
41. Verifikasi Tidak ada email OTP baru di `misbahfauzi+{runId}-007@qwertysystem.net` (jumlah email tetap sama dengan baseline)
42. Ketik 6 digit kode OTP terakhir (dari Resend ke-5) pada kotak digit
43. Verifikasi Kode terakhir yang masih berlaku dapat dipakai untuk verifikasi: browser dialihkan ke Portal — Product Hub
44. Pulihkan jam server uji dan jam browser uji ke waktu nyata

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal TC kedua; mengetik kode OTP terakhir pada TC-AUTH-MFA-82 yang diperlukan Expected b; mencatat baseline jumlah email; mengatur dan memulihkan jam) bukan asersi tambahan (S-03, S-09, S-12).
- Kelas harness e (volume data khusus: kuota Resend). Kedua TC tidak digabung dengan spec cooldown (spec 006) karena kuota 5 kali menghabiskan sesi pre-auth. Urutan mengikuti TC sumber; TC-AUTH-MFA-82 berujung login sukses sehingga diletakkan paling akhir (S-10).
- Dasar `Verifikasi` langkah 20-21: Expected c TC-AUTH-MFA-79 menyebut dua klausa, "total 6 email (1 pengiriman awal + 5 resend)" dan "tidak ada email ke-7"; tiap klausa diasersi sendiri terhadap baseline langkah 7. Keduanya bukan tambahan spec.
- Jam: hanya jam server uji dan jam browser uji yang diubah, dimajukan bersama pada tiap langkah Resend dan dipulihkan di akhir tiap TC. Tidak ada penantian waktu nyata.
- Temuan untuk QA: (1) TC-AUTH-MFA-82 Expected b ("kode terakhir ... dapat dipakai untuk verifikasi selama belum expired") tidak punya langkah pengecekan di Langkah Uji; spec menambahkan langkah mengetik kode terakhir dan memverifikasi login berhasil. (2) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi (S-01): TC-AUTH-MFA-79 "Kode OTP terakhir tetap valid sampai 5 menit setelah dikirim; hitungan resend sesi ini 5" dan TC-AUTH-MFA-82 "Hitungan resend sesi pre-auth ini tetap 5"; validitas kode terakhir hanya teramati lewat Expected b TC-AUTH-MFA-82. (3) TC-AUTH-MFA-79 Langkah Uji 8 ("Tunggu hitung mundur selesai") dan 10 ("Tunggu 2 menit") serta TC-AUTH-MFA-82 Langkah Uji 8 menyebut penantian waktu nyata dan TC-AUTH-MFA-79 bertanda Manual Only; spec memakai pengaturan jam (konvensi bagian 6), TC perlu disesuaikan. (4) Pre-setup TC (#20/#21) belum memuat mekanisme seeding state BE per user (login terakhir, consent, logout web terakhir); mekanisme seed disediakan tim FE/BE.
