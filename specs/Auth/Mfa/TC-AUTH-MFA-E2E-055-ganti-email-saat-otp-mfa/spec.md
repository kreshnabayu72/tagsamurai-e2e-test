---
id: TC-AUTH-MFA-E2E-055-ganti-email-saat-otp-mfa
title: "Ganti Email User Saat OTP Faktor Kedua MFA Berlangsung"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-75
  - TC-AUTH-MFA-161
coverage:
  web: automated
---

# Ganti Email User Saat OTP Faktor Kedua MFA Berlangsung

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user Activated, Active ON, profil NEWDEV (Tabel Data Uji Pre-setup #4), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi BE yang di-seed: seperti BASE, yaitu sudah pernah login sukses di web dari browser uji A (ID device browser uji A tercatat sebagai trusted device), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari; Authenticator belum terdaftar. Login dilakukan dari browser uji B (ID device belum ada di daftar trusted device) sehingga MFA terpicu.
  - TC-AUTH-MFA-75: `Dara Ayuningtyas` (`daraayuningtyas+{runId}-055@qwertysystem.net`); email baru `daraayuningtyas.baru+{runId}-055@qwertysystem.net` (belum dipakai user lain, dapat dibaca lewat mail-catcher)
  - TC-AUTH-MFA-161: `Sofia Rahma` (`sofiarahma+{runId}-055@qwertysystem.net`); email baru `sofiarahma.baru+{runId}-055@qwertysystem.net` (belum dipakai user lain, dapat dibaca lewat mail-catcher)
- Aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_TC_PASSWORD`) login satu kali di hook `before` pada browser kedua (konteks browser terpisah dari browser user uji) dan sesinya dipakai sepanjang spec untuk mengubah email user lewat `Global Settings > User > Detail` serta membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` (TC-AUTH-MFA-161). Login akun aktor tidak memicu MFA. Browser kedua tidak memegang sesi user uji; fungsinya hanya mengubah state user target dan membaca log.
- Hook `after`: hapus kedua user yang dibuat spec ini (termasuk yang emailnya sudah diganti) dan tutup browser kedua. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding atau langkah spec berhasil penuh.
- Akun yang dipakai: user uji tanpa login (halaman publik; tidak ada sesi aktif di browser) di jendela privat baru pada browser pertama (browser uji B, ID device belum dikenali); akun aktor Total Control (Global Settings) di browser kedua.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua konteks browser terpisah (browser pertama untuk user uji, browser kedua untuk akun aktor); mail-catcher lingkungan uji untuk email OTP faktor-2 ke email lama dan email konfirmasi perubahan email ke email baru; reCAPTCHA mode uji di environment; IP uji yang dikenal untuk asersi kolom IP Address (TC-AUTH-MFA-161). Seeding state BE per user: trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir, dan logout web terakhir; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- State global: tidak ada yang diubah selain data user milik spec ini.

## Test Steps

### TC-AUTH-MFA-75: Kode OTP faktor-2 ditolak setelah email akun diganti dan dikonfirmasi admin di sesi lain

1. Buka jendela privat baru di browser pertama (tanpa sesi login)
2. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
3. Ketik `daraayuningtyas+{runId}-055@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "OTP via email" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `daraayuningtyas+{runId}-055@qwertysystem.net`
9. Beralih ke browser kedua (sesi Total Control Global Settings) lalu buka `Global Settings > User` dan cari `daraayuningtyas+{runId}-055@qwertysystem.net` pada User List
10. Buka `Global Settings > User > Detail` untuk `Dara Ayuningtyas`
11. Ubah Email ke `daraayuningtyas.baru+{runId}-055@qwertysystem.net` lalu klik button [Save]
12. Buka tautan konfirmasi perubahan email dari email konfirmasi di mail-catcher `daraayuningtyas.baru+{runId}-055@qwertysystem.net`
13. Beralih ke browser pertama (halaman OTP Verification)
14. Ketik 6 digit kode OTP faktor-2 dari email `daraayuningtyas+{runId}-055@qwertysystem.net` (kode yang dikirim ke email lama) pada kotak digit
15. Verifikasi Caption error "Invalid code" tampil (sama dengan kode salah)
16. Verifikasi Caption error berada di bawah kotak digit
17. Verifikasi Tidak ada sesi yang dibuat untuk `Dara Ayuningtyas`
18. Verifikasi Halaman tetap OTP Verification

### TC-AUTH-MFA-161: Pencatatan OTP setelah email diganti dicatat Failed OTP invalid — email changed

19. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
20. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
21. Ketik `sofiarahma+{runId}-055@qwertysystem.net` pada field Email
22. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
23. Centang widget reCAPTCHA "I'm not a robot"
24. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
25. Pilih opsi "OTP via email" pada halaman Choose Verification Method
26. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `sofiarahma+{runId}-055@qwertysystem.net`
27. Beralih ke browser kedua (sesi Total Control Global Settings) lalu buka `Global Settings > User` dan cari `sofiarahma+{runId}-055@qwertysystem.net` pada User List
28. Buka `Global Settings > User > Detail` untuk `Sofia Rahma`
29. Ubah Email ke `sofiarahma.baru+{runId}-055@qwertysystem.net` lalu klik button [Save]
30. Buka tautan konfirmasi perubahan email dari email konfirmasi di mail-catcher `sofiarahma.baru+{runId}-055@qwertysystem.net`
31. Catat penanda waktu sesudah perubahan email dikonfirmasi sebagai acuan entri log baru untuk `Sofia Rahma`
32. Beralih ke browser pertama (halaman OTP Verification)
33. Ketik 6 digit kode OTP faktor-2 dari email `sofiarahma+{runId}-055@qwertysystem.net` (kode yang dikirim ke email lama) pada kotak digit
34. Beralih ke browser kedua (sesi Total Control Global Settings)
35. Buka `Global Settings > Activity Log > Session` lalu cari entri untuk `Sofia Rahma` dengan email bersuffix `sofiarahma.baru+{runId}-055@qwertysystem.net` (email akun sesudah perubahan dikonfirmasi) yang dibuat sesudah penanda waktu langkah 31
36. Verifikasi Tampil satu entri baru untuk `Sofia Rahma` pada Activity Log > Session sesudah penanda waktu langkah 31
37. Verifikasi Activity entri tersebut `Login`
38. Verifikasi Status entri tersebut `Failed`
39. Verifikasi Note entri tersebut `OTP invalid — email changed`
40. Verifikasi IP Address entri tersebut berisi IP uji
41. Verifikasi Tanggal dan waktu percobaan tampil pada entri tersebut
42. Verifikasi Tidak ada entri log tambahan pada Activity Log > Session (tepat satu entri sesudah penanda waktu langkah 31)
43. Buka `Global Settings > User > Detail > User Log` untuk `Sofia Rahma` lalu cari entri yang dibuat sesudah penanda waktu langkah 31
44. Verifikasi Tampil satu entri baru pada User Log dengan Activity `Login` dan Status `Failed`
45. Verifikasi Note entri User Log tersebut `OTP invalid — email changed`
46. Verifikasi IP Address entri User Log tersebut sama dengan IP Address entri Activity Log > Session
47. Verifikasi Tidak ada entri log tambahan pada User Log (tepat satu entri sesudah penanda waktu langkah 31)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Akun aktor Total Control login satu kali di hook `before` di browser kedua dan hanya mengubah state user target (ubah email) serta membaca log; ini bukan konteks kedua yang menjadi objek asersi, sehingga tidak butuh butir `P-2`. Asersi log TC-AUTH-MFA-161 adalah asersi pencatatan (Status dan Note spesifik) dan asersi jumlah dengan baseline (S-12), bukan asersi absence kelas g, sehingga tidak butuh butir `P-1`. Pembacaan email di mail-catcher adalah langkah rutin spec fungsional.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Pembagian lintas spec: TC-AUTH-MFA-75 dan 161 berada di spec ini, bukan di `TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa`, karena topik aksinya berbeda (ubah email versus Deactivate dan Delete, prinsip 1). Urutan TC mengikuti sumber (75 lalu 161) dan tiap TC memakai user sendiri.
- Pencatatan: TC-AUTH-MFA-161 memuat asersi log Failed `OTP invalid — email changed` (Activity Log > Session dan User Log) karena skenarionya sama dengan TC-AUTH-MFA-75. Post Condition TC-AUTH-MFA-75 ("Percobaan dicatat Failed `OTP invalid — email changed`") tidak punya Expected padanan maupun langkah observasi di TC-AUTH-MFA-75, sehingga tidak diasersi pada TC-AUTH-MFA-75 (lihat Temuan untuk QA butir 6); skenario yang sama diasersi sebagai Expected TC-AUTH-MFA-161. Asersi log memakai penanda waktu sesudah langkah 31 sebagai baseline dan pencarian lewat email bersuffix dan penanda waktu, bukan nama user literal saja, karena nama `Sofia Rahma` dapat muncul pada log run lain.
- Melewati ±35 langkah (47 langkah, ±37 netto setelah langkah prefix login faktor-1 tidak dihitung) karena asersi log TC-AUTH-MFA-161 yang dipecah per klausa (S-01) pada dua surface log; kedua TC independen (user, jendela privat, dan email baru sendiri; entri log dibatasi penanda waktu), sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal dan spec tidak dipecah.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru di awal tiap TC; beralih antara browser pertama dan kedua; cari user pada User List; catat penanda waktu; tanpa klik tambahan setelah mengetik kode OTP) bukan asersi tambahan (S-03). Pencarian user memakai email bersuffix karena nama user yang sama dipakai spec lain dalam satu run.
- Temuan untuk QA: (1) TC-AUTH-MFA-75 langkah 9 dan TC-AUTH-MFA-161 langkah 9 hanya menyebut mengetik kode OTP dan tidak menyebut klik [Login]; spec mengikuti teks TC dan hanya mengetik (langkah 14 dan 33). (2) TC-AUTH-MFA-75 dan 161 menyebut "ubah email di `Global Settings > User > Detail`" sedangkan TC `global-settings/user` mengubah email lewat (⋯) lalu `Edit`; spec memakai kata TC apa adanya, QA perlu memastikan lokasi ubah email. (3) TC-AUTH-MFA-75 dan 161 tidak menjelaskan halaman yang tampil setelah tautan konfirmasi dibuka dan alamat email baru. (4) TC-AUTH-MFA-161 tidak menjelaskan kolom identitas user pada Activity Log > Session dan User Log setelah email diganti (email lama, email baru, atau nama); spec mencari lewat email bersuffix email baru (email akun sesudah perubahan dikonfirmasi) dan penanda waktu; pilihan email baru adalah asumsi spec. (5) Mekanisme seeding state BE per user (trusted device ber-ID device, lokasi dan waktu login terakhir) belum ada di Pre-setup (#20/#21) TC; spec tidak menyebut endpoint. (6) Post Condition TC-AUTH-MFA-75 "Percobaan dicatat Failed `OTP invalid — email changed`" tidak punya Expected padanan maupun langkah observasi di Langkah Uji TC-AUTH-MFA-75, sehingga tidak diasersi pada TC-AUTH-MFA-75 dan spec tidak menambah langkah observasi log di sana; pencatatan skenario yang sama diasersi lewat Expected TC-AUTH-MFA-161. QA dapat menambah Expected atau langkah observasi log di TC-AUTH-MFA-75.
