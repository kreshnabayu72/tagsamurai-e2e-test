---
id: TC-AUTH-OTP-E2E-027-ttl-token-pra-autentikasi-10-menit
title: "Masa Berlaku Token Pra-Autentikasi 10 Menit pada Layar Confirm to Continue"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-107
  - TC-AUTH-OTP-111
  - TC-AUTH-OTP-108
coverage:
  web: automated
---

# Masa Berlaku Token Pra-Autentikasi 10 Menit pada Layar Confirm to Continue

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1); password dari `Spectra.env.GS_TC_PASSWORD`. Dipakai untuk membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` pada TC-AUTH-OTP-107 dan TC-AUTH-OTP-111.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `AC_PRINCIPAL_PP_PASSWORD` (Principal penerbit Privacy Policy), `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; dipakai langkah 40 untuk Login with Password).
- Tanpa login (halaman publik, tidak ada sesi aktif di browser) untuk semua langkah publik. reCAPTCHA memakai mode uji environment.
- Kemampuan teknis:
  - Mail-catcher lingkungan uji untuk membaca email dan kode OTP 6 digit.
  - Manipulasi jam server uji (memajukan waktu). Langkah "Tunggu ..." dipenuhi dengan memajukan jam server sebesar durasi yang tertulis, dihitung sejak layar Confirm to Continue tampil (token pra-autentikasi berlaku 10 menit sejak OTP terverifikasi, NC-11). Masa berlaku token dihitung murni di server dan tidak diamati lewat UI, sehingga hanya jam server yang diatur; jam browser tidak diubah (konvensi bagian 6).
  - Dua konteks browser: jendela privat publik dan browser admin.
- State global: jam server (dimajukan kumulatif pada langkah 7, 24, 26, dan 34) dan versi Privacy Policy aktif (diterbitkan hook `before`, tidak ditarik kembali). Suite berjalan serial (`parallel: false`) karena jam server digeser dan profil POLICY bergantung pada versi Privacy Policy global; jam server dipulihkan di hook `after`.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Prasyarat Agreement: akun Principal di atas menerbitkan di hook `before` versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui tiap user profil POLICY (Tabel Data Uji Pre-setup #5), sehingga hanya layar Confirm to Continue yang terpicu setelah OTP benar.
- Hook `before`: login akun aktor Total Control (Global Settings) di browser admin; lalu Principal menerbitkan versi Privacy Policy terbaru; lalu (seeding API, email bersuffix per run) buat user Activated dengan Toggle Active ON, profil POLICY (seperti profil BASE, versi Privacy Policy terakhir yang disetujui lebih lama dari versi aktif):
  - TC-AUTH-OTP-107: `Lestari Kartika` (`lestarikartika+{runId}-027@qwertysystem.net`).
  - TC-AUTH-OTP-111: `Sari Pratama` (`saripratama+{runId}-027@qwertysystem.net`).
  - TC-AUTH-OTP-108: `Bayu Firmansyah` (`bayufirmansyah+{runId}-027@qwertysystem.net`).
- Baseline log: hook `before` mencatat jumlah baris awal tiap user uji di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`; "tidak ada baris baru" pada langkah 17 dan 27 dihitung terhadap baseline itu (S-12).
- Hook `after`: kembalikan jam server uji ke waktu nyata, tutup sesi login yang terbentuk (TC-AUTH-OTP-108), dan hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-107: Continue setelah token pra-autentikasi kedaluwarsa kembali ke halaman Login with Password

1. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
2. Ketik `lestarikartika+{runId}-027@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ketik 6 digit kode OTP dari email pada kotak digit
6. Centang checkbox "I have read and agree to the Privacy Policy *"
7. Tunggu 10 menit 30 detik tanpa mengklik Continue
8. Verifikasi layar Confirm to Continue tetap terbuka tanpa perubahan dan tanpa pesan
9. Klik button [Continue ➔]
10. Verifikasi permintaan konfirmasi ditolak server
11. Verifikasi browser kembali ke halaman `Auth > Login with Password` dengan Title "Login with Password"
12. Verifikasi halaman Login with Password tampil tanpa pesan error
13. Verifikasi field Email pada halaman Login with Password kosong
14. Verifikasi tidak ada sesi yang dibuat
15. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`)
16. Buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Lestari Kartika`
17. Verifikasi tidak ada baris baru untuk percobaan ini di kedua surface log dibanding baseline hook `before`

### TC-AUTH-OTP-111: Token pra-autentikasi yang kedaluwarsa tanpa Confirm tidak menulis entri log

18. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
19. Ketik `saripratama+{runId}-027@qwertysystem.net` pada field Email
20. Centang widget reCAPTCHA "I'm not a robot"
21. Klik button [Request OTP]
22. Ketik 6 digit kode OTP dari email pada kotak digit
23. Tutup tab tanpa mengklik Continue
24. Tunggu 10 menit 30 detik sejak layar Confirm to Continue tampil
25. Ganti konteks ke browser admin dan buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Sari Pratama`
26. Majukan jam server 2 menit, lalu segarkan kedua surface log
27. Verifikasi tidak ada baris baru untuk percobaan ini di kedua surface log dibanding baseline hook `before`, termasuk tidak ada Note `Consent not given`

### TC-AUTH-OTP-108: Continue pada menit ke-9 setelah OTP benar masih diterima

28. Ganti konteks ke jendela privat baru (tanpa sesi) dan buka halaman `Auth > Login with OTP > Request OTP`
29. Ketik `bayufirmansyah+{runId}-027@qwertysystem.net` pada field Email
30. Centang widget reCAPTCHA "I'm not a robot"
31. Klik button [Request OTP]
32. Ketik 6 digit kode OTP dari email pada kotak digit
33. Centang checkbox "I have read and agree to the Privacy Policy *"
34. Tunggu 9 menit tanpa mengklik Continue
35. Klik button [Continue ➔]
36. Verifikasi konfirmasi diterima dan browser dialihkan ke Portal — Product Hub
37. Verifikasi sesi aktif untuk `Bayu Firmansyah`
38. Logout dari Portal — Product Hub
39. Buka halaman `Auth > Login with Password`
40. Login dengan email `bayufirmansyah+{runId}-027@qwertysystem.net` dan password yang benar dari `Spectra.env.OTP_PASSWORD`
41. Verifikasi Login with Password berhasil
42. Verifikasi layar Confirm to Continue tidak tampil karena persetujuan versi aktif sudah tersimpan

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Urutan di sumber (107, 108, 111) berubah menjadi 107, 111, 108 mengikuti bagian 3: kasus ditolak lebih dulu, kasus yang membuat sesi dan menyimpan persetujuan di akhir.
- Pengecualian P-1 (state berat): TC-111 pada dasarnya asersi absence dan TC-107 memuat Expected e (tidak ada baris baru di log), keduanya bergantung pada state berat (token pra-autentikasi yang sudah kedaluwarsa setelah 10 menit 30 detik dan geser jam server), sehingga tetap di spec ini dan tidak dipindah ke spec absence E2E-040. Sumber pembagian dicatat juga di Notes E2E-040.
- Langkah penghubung (S-03): langkah 15, 18, 25, 28 (ganti konteks eksplisit antara browser admin dan jendela privat). Langkah 26 (memajukan jam server 2 menit lalu menyegarkan log, pengganti menunggu 2 menit nyata; konvensi bagian 6) mengikuti TC-111 langkah 8, dan langkah 38 sampai 40 (logout, membuka Login with Password, dan login) mengikuti TC-108 langkah 9 dan 10 sebagai pengamatan Expected b; keempatnya langkah TC, bukan langkah penghubung.
- Jam server maju kumulatif sekitar 32 menit (langkah 7, 24, 26, dan 34); bila lingkungan menerapkan idle timeout pada sesi browser admin, login ulang akun aktor sebelum langkah 15 dan sebelum langkah 25 (langkah 15 sampai 17 dan 25 sampai 27 memakai browser admin).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC-107 langkah 7 menyebut "Tunggu 10 menit 30 detik", tetapi Precondition TC-107 tidak menyebut cara membentuk profil POLICY; spec menerbitkan versi baru lewat Principal di hook `before` dan tidak mengarang cara menariknya kembali (publish bersifat global dan memengaruhi user lain).
  - TC-107 Expected b ("permintaan konfirmasi ditolak server") tidak menyebut kode atau caption; spec hanya mengasersi akibat yang terlihat (kembali ke Login with Password tanpa pesan, tanpa sesi).
  - TC-111 mengamati log selama 2 menit sedangkan NC-12 sudah menyatakan `Consent not given` hanya dicatat saat Continue tanpa centang ditolak; asersi "tidak ada baris baru" mengikuti TC.
  - TC-108 Post Condition a ("Persetujuan Privacy Policy tersimpan") diamati lewat Expected b (layar Confirm to Continue tidak tampil pada Login with Password); spec tidak menambah asersi terpisah (S-01).
