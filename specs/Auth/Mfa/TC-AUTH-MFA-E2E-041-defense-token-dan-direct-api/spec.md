---
id: TC-AUTH-MFA-E2E-041-defense-token-dan-direct-api
title: "Defense-in-Depth: Token Pre-auth dan Request Langsung ke Endpoint MFA"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-188
  - TC-AUTH-MFA-189
  - TC-AUTH-MFA-190
  - TC-AUTH-MFA-193
coverage:
  web: automated
---

# Defense-in-Depth: Token Pre-auth dan Request Langsung ke Endpoint MFA

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password user `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-188: `Eko Santoso` (`ekosantoso+{runId}-041@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, device browser uji B belum ada di daftar trusted device, Authenticator sudah terdaftar dengan secret yang dikenali aplikasi authenticator uji).
  - TC-AUTH-MFA-190: `Budi Rahmawati` (`budirahmawati+{runId}-041@qwertysystem.net`), profil NEWDEVE.
  - TC-AUTH-MFA-193: `Nur Wijaya` (`nurwijaya+{runId}-041@qwertysystem.net`), profil NEWDEVE.
  - TC-AUTH-MFA-189: `Intan Santoso` (`intansantoso+{runId}-041@qwertysystem.net`), profil BASE (Tabel Data Uji Pre-setup #2). User ini tidak login; ia dipakai hanya sebagai subjek pengecekan log (Langkah Uji TC hanya mengirim request dengan token pre-auth palsu).
- Hook `after`: hapus keempat user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk keempat TC. Tiap TC berbrowser dimulai di jendela privat baru (browser uji B, ID device belum dikenali). Pengecekan log di TC-AUTH-MFA-189 dan TC-AUTH-MFA-190 memakai jendela sesi akun aktor Total Control (Global Settings) yang dibuka di hook `before` (kredensial `Spectra.env.GS_TC_PASSWORD`).
- Baseline log (S-12): penanda waktu T0-189 dicatat pada langkah 1 (TC-AUTH-MFA-189), sesudah seeding dan sebelum request pertama; penanda waktu T0 dicatat pada langkah 38 (TC-AUTH-MFA-190), sesudah seeding dan sebelum login `Budi Rahmawati`. Asersi log hanya menghitung baris yang bertanda waktu sesudah penanda masing-masing dan dicari lewat email bersuffix, jadi tidak bergantung pada seeding menghasilkan atau tidak menghasilkan entri Login dan tidak bentrok dengan entri nama yang sama dari run lain.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Client HTTP untuk request langsung ke endpoint MFA `POST /v2/iam/auth/mfa/otp/verify`, `POST /v2/iam/auth/mfa/authenticator/verify`, dan `POST /v2/iam/auth/mfa/authenticator/enroll` (nama endpoint dan field `preAuthToken`, `otpCode`, `totpCode` dari `auth/mfa/API/openapi.yaml`).
  - Pembacaan token sesi pre-auth dari respons request faktor-1 yang dikirim browser (alat uji API).
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk kode TOTP valid, termasuk kode valid periode berikutnya (TC-AUTH-MFA-190).
  - Seeding state BE per user: profil BASE (`Intan Santoso`) sesuai Tabel Data Uji Pre-setup #2; profil NEWDEVE tanpa ID device browser uji B di daftar trusted device dan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - reCAPTCHA mode uji di environment.
- Pemulihan state global: tidak ada (spec tidak mengubah jam server, geo-IP, email service, atau counter rate limit).

## Test Steps

### TC-AUTH-MFA-189: Verifikasi faktor-2 tanpa sesi pre-auth yang valid ditolak

1. Catat penanda waktu T0-189 (waktu server uji saat ini) sebelum request pertama; asersi log pada langkah 9 dan 11 hanya menghitung baris bertanda waktu sesudah T0-189
2. Kirim request `POST /v2/iam/auth/mfa/otp/verify` (client HTTP) dengan `preAuthToken` berupa nilai acak tidak dikenal dan `otpCode` `123456`
3. Verifikasi Request `otp/verify` ditolak karena sesi pre-auth tidak valid
4. Verifikasi Tidak ada sesi penuh yang dibuat oleh request `otp/verify` (respons tidak memuat token sesi dan tidak menyetel cookie sesi)
5. Kirim request `POST /v2/iam/auth/mfa/authenticator/verify` (client HTTP) dengan `preAuthToken` berupa nilai acak tidak dikenal yang sama dan `totpCode` `123456`
6. Verifikasi Request `authenticator/verify` ditolak karena sesi pre-auth tidak valid
7. Verifikasi Tidak ada sesi penuh yang dibuat oleh request `authenticator/verify` (respons tidak memuat token sesi dan tidak menyetel cookie sesi)
8. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri untuk `Intan Santoso` (email bersuffix `intansantoso+{runId}-041@qwertysystem.net`) yang bertanda waktu sesudah T0-189
9. Verifikasi Tidak ada entri log baru untuk `Intan Santoso` pada Activity Log > Session sesudah T0-189
10. Buka `Global Settings > User > Detail > User Log` untuk `Intan Santoso` dan cari entri yang bertanda waktu sesudah T0-189
11. Verifikasi Tidak ada entri log baru untuk `Intan Santoso` pada User Log sesudah T0-189

### TC-AUTH-MFA-188: Server menolak kode faktor-2 yang salah walau request dikirim langsung tanpa melalui UI

12. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
13. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
14. Ketik `ekosantoso+{runId}-041@qwertysystem.net` pada field Email
15. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
16. Centang widget reCAPTCHA "I'm not a robot"
17. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
18. Ambil token sesi pre-auth dari respons faktor-1 (alat uji API)
19. Pilih opsi "Authenticator app", lalu klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
20. Kirim langsung request `POST /v2/iam/auth/mfa/authenticator/verify` (client HTTP) dengan `preAuthToken` yang diambil dan `totpCode` `000000`, tanpa melalui halaman
21. Verifikasi Request ditolak dengan hasil gagal (outcome failed)
22. Verifikasi Tidak ada sesi penuh yang dibuat
23. Verifikasi Browser tetap pada halaman Authenticator Verification (UI tidak menjadi satu-satunya gate)

### TC-AUTH-MFA-193: Secret Authenticator yang sudah aktif tidak dapat ditampilkan ulang lewat sesi pre-auth baru

24. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
25. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
26. Ketik `nurwijaya+{runId}-041@qwertysystem.net` pada field Email
27. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
28. Centang widget reCAPTCHA "I'm not a robot"
29. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
30. Simpan token sesi pre-auth dari respons faktor-1 (alat uji API)
31. Kirim langsung request enrollment `POST /v2/iam/auth/mfa/authenticator/enroll` (client HTTP) dengan token tersebut
32. Verifikasi Request enrollment ditolak
33. Verifikasi Tidak ada QR code, URI otpauth, maupun secret key yang dikembalikan (enrollment sudah aktif)
34. Verifikasi Tidak ada sesi penuh yang dibuat (respons tidak memuat token sesi dan tidak menyetel cookie sesi)
35. Pilih opsi "Authenticator app", lalu klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil (bukan Enrollment Authenticator)
36. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `nurwijaya+{runId}-041@qwertysystem.net` (secret yang sama dengan sebelum request) pada kotak digit, lalu klik button [Login] → Portal — Product Hub tampil
37. Verifikasi Enrollment Authenticator `Nur Wijaya` tetap aktif dengan secret yang sama (kode TOTP dari secret awal diterima)

### TC-AUTH-MFA-190: Sesi pre-auth yang sudah dikonsumsi tidak dapat dipakai ulang

38. Catat penanda waktu T0 (waktu server uji saat ini) sebelum login `Budi Rahmawati`; asersi log pada langkah 53 dan 55 hanya menghitung baris bertanda waktu sesudah T0
39. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
40. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
41. Ketik `budirahmawati+{runId}-041@qwertysystem.net` pada field Email
42. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
43. Centang widget reCAPTCHA "I'm not a robot"
44. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
45. Simpan token sesi pre-auth dari respons faktor-1 (alat uji API)
46. Pilih opsi "Authenticator app", lalu klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
47. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `budirahmawati+{runId}-041@qwertysystem.net` pada kotak digit, lalu klik button [Login] → Portal — Product Hub tampil
48. Verifikasi Login final pertama berhasil dan Portal — Product Hub tampil
49. Kirim ulang request `POST /v2/iam/auth/mfa/authenticator/verify` (client HTTP) dengan token yang sama dan kode TOTP valid berikutnya (periode 30 detik berikutnya) dari aplikasi authenticator uji
50. Verifikasi Pengiriman ulang ditolak karena sesi pre-auth sudah dikonsumsi
51. Verifikasi Tidak ada sesi kedua yang dibuat (respons tidak memuat token sesi dan tidak menyetel cookie sesi)
52. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri untuk `Budi Rahmawati` yang bertanda waktu sesudah T0
53. Verifikasi Tepat satu entri Status "Success" untuk `Budi Rahmawati` bertanda waktu sesudah T0 pada Activity Log Session (tidak ada entri Success ganda)
54. Buka `Global Settings > User > Detail > User Log` untuk `Budi Rahmawati`
55. Verifikasi Tepat satu entri Success login final untuk `Budi Rahmawati` bertanda waktu sesudah T0 pada User Log (tidak ada entri Success ganda)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- `P-1`: asersi "tidak ada entri log untuk `Intan Santoso`" (TC-AUTH-MFA-189 Expected b) tetap di spec ini sebagai `Verifikasi` (langkah 9 dan 11) dengan baseline penanda waktu T0-189 (S-12, S-05). TC-AUTH-MFA-189 tidak masuk `sourceTc` spec absence `TC-AUTH-MFA-E2E-035-absence-pencatatan-log`, dan asersi itu terikat pada request langsung tak valid yang dikirim TC ini sendiri.
- Urutan TC menyimpang dari TC sumber (188, 189, 190, 193): TC-AUTH-MFA-189 dipindah ke awal karena tidak memakai browser atau user login, dan TC-AUTH-MFA-190 dipindah ke akhir karena menyelesaikan login final sungguhan (aksi yang mengubah state paling berat) (S-05, S-10).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC berbrowser, memilih "Authenticator app" lalu [Login] sebelum request langsung pada TC-AUTH-MFA-188 dan TC-AUTH-MFA-190, pengecekan Enrollment tetap aktif pada TC-AUTH-MFA-193, pencatatan penanda waktu T0-189 pada langkah 1 dan T0 pada langkah 38, pindah ke jendela aktor dan membuka Activity Log dan User Log pada langkah 8 dan 10) bukan asersi tambahan (S-03).
- Baseline log (S-12): langkah 1 mencatat T0-189 dan langkah 38 mencatat T0 sebelum aksi; kata "tidak ada entri log baru" pada langkah 9 dan 11 berarti tidak ada baris bertanda waktu sesudah T0-189 untuk email bersuffix `Intan Santoso`; kata "tepat satu entri" pada langkah 53 dan 55 berarti satu baris di antara baris bertanda waktu sesudah T0, bukan jumlah seluruh baris nama itu.
- Asersi entri log pada TC-AUTH-MFA-190 (langkah 53 dan 55) hanya memakai Status "Success"; kolom Activity tidak diasersi karena Expected b TC-AUTH-MFA-190 hanya menyebut "tidak ada entri Success ganda" tanpa menyebut Activity.
- Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01): ditolak, tidak ada sesi penuh (daftar token sesi dan cookie sesi yang sama-sama tidak ada tetap satu `Verifikasi`), serta tidak ada QR code, URI otpauth, dan secret key (daftar utuh).
- Jumlah langkah 55; tiga prefix login faktor-1 (langkah 12-17, 24-29, 39-44) tidak dihitung sehingga ±37 langkah (sedikit di atas smell ±35 karena pengecekan log TC-AUTH-MFA-189 dan TC-AUTH-MFA-190); keempat TC independen sehingga spec tidak dipecah.
- Temuan untuk QA: (1) TC-AUTH-MFA-188 menyebut "Tetap Authenticator Verification pada browser", tetapi Langkah Uji berhenti di Choose Verification Method; spec menambah langkah memilih "Authenticator app" lalu [Login] sebelum request langsung (S-14, S-15). (2) TC-AUTH-MFA-190 Langkah 7 kembali ke Authenticator Verification tanpa langkah memilih metode; spec menambah langkah itu. (3) TC-AUTH-MFA-189 menulis "verifikasi OTP/Authenticator" tanpa menentukan endpoint; spec mengirim ke kedua endpoint (`otp/verify` dan `authenticator/verify`). (4) TC-AUTH-MFA-189 mencantumkan user `Intan Santoso` profil BASE di Precondition tetapi Langkah Uji tidak memakainya; spec men-seed user itu dengan email bersuffix hanya sebagai subjek pengecekan log Expected b, dan Post Condition "Tidak ada sesi untuk `Intan Santoso`" (state BE tanpa langkah observasi) tidak diasersi. (5) TC-AUTH-MFA-188 dan TC-AUTH-MFA-190 tidak mencantumkan akun Total Control di Precondition walau Post Condition menyebut entri log; spec memakai akun aktor hook untuk TC-AUTH-MFA-190 dan tidak mengasersi pencatatan TC-AUTH-MFA-188: Post Condition "Percobaan dicatat Failed `Incorrect OTP` (detail pada TC Logging)" tidak punya Expected padanan maupun langkah observasi di TC, sehingga tidak diasersi di spec ini dan spec tidak menambah langkah observasi log. QA dapat menambah Expected atau langkah observasi log di TC-AUTH-MFA-188. (6) TC-AUTH-MFA-193 Post Condition "secret yang sama" tidak punya cara pengecekan di Langkah Uji; spec memakai login dengan kode TOTP dari secret awal. (7) TC-AUTH-MFA-188 Post Condition "tidak ada sesi penuh" sudah ada pada Expected a; TC-AUTH-MFA-190 Post Condition "Satu sesi web aktif untuk `Budi Rahmawati`" teramati sebagai Portal — Product Hub tampil (langkah 48) dan tidak diasersi terpisah. (8) Mekanisme seeding state BE per user (profil NEWDEVE: trusted device, Authenticator dengan secret dikenal) belum ada di Pre-setup TC (#20/#21).
