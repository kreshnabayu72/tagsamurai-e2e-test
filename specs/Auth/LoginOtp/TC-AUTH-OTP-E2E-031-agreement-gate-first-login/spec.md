---
id: TC-AUTH-OTP-E2E-031-agreement-gate-first-login
title: "Layar Confirm to Continue: Pemicu Login Pertama, Checkbox, Tautan Privacy Policy, dan Konfirmasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-97
  - TC-AUTH-OTP-101
  - TC-AUTH-OTP-102
  - TC-AUTH-OTP-104
  - TC-AUTH-OTP-109
coverage:
  web: automated
---

# Layar Confirm to Continue: Pemicu Login Pertama, Checkbox, Tautan Privacy Policy, dan Konfirmasi

## Prerequisites

- Mode: FE+BE (backend nyata; token pra-autentikasi, persetujuan, dan log dibuktikan lewat perilaku UI dan log Global Settings).
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Password user uji dari `Spectra.env.OTP_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD`.
- Hook `before` membuka browser admin dan login sebagai akun aktor Total Control (Global Settings); langkah uji hanya berpindah konteks ke browser itu (TC-AUTH-OTP-102 dan TC-AUTH-OTP-109). Hook `after` mengembalikan sesi admin ke akun default suite.
- Hook `before`: Principal menerbitkan versi Privacy Policy terbaru sebelum user profil POLICY di-seed. Lalu hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-031`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - Profil FIRST (Activated, Active ON; belum pernah menyelesaikan login di platform web; Authenticator belum terdaftar; Agreement dan MFA terpicu):
    - TC-AUTH-OTP-97: `Dewi Hakim` (`dewihakim+{runId}-031@qwertysystem.net`)
  - Profil POLICY (Activated, Active ON; sudah login sukses dalam 30 hari terakhir; persetujuan Privacy Policy versi terbaru belum ada karena Principal (hook `before`) sudah menerbitkan versi yang lebih baru; hanya Agreement terpicu):
    - TC-AUTH-OTP-101: `Rina Aditya` (`rinaaditya+{runId}-031@qwertysystem.net`)
    - TC-AUTH-OTP-104: `Fajar Cahyono` (`fajarcahyono+{runId}-031@qwertysystem.net`)
    - TC-AUTH-OTP-109: `Intan Nasution` (`intannasution+{runId}-031@qwertysystem.net`)
    - TC-AUTH-OTP-102: `Hendra Maulana` (`hendramaulana+{runId}-031@qwertysystem.net`)
- Baseline log: hook `before` mencatat jumlah baris `Hendra Maulana` di `Global Settings > Activity Log > Session` dan di `Global Settings > User > Detail > User Log`; "tepat satu baris baru" pada langkah 62 dan 64 dihitung terhadap baseline itu (S-12). Baseline `Intan Nasution` (TC-AUTH-OTP-109) dicatat di langkah 33.
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP; klien HTTP yang mengirim permintaan Verify OTP langsung ke server tanpa melalui UI dengan email dan kode OTP yang sudah dipakai (TC-AUTH-OTP-109); versi baru Privacy Policy diterbitkan Principal di hook `before` sebelum profil POLICY dipakai; dua konteks browser (browser admin dan jendela privat publik); konteks browser persisten yang sama dipakai bersama antar tab dalam satu TC, yaitu menutup tab lalu membuka tab baru tanpa menutup konteks sehingga tidak ada sesi tersisa (TC-AUTH-OTP-109) dan membuka Portal — Product Hub di tab lain (TC-AUTH-OTP-97); tab baru dari tautan "Read the full Privacy Policy" dan kembali ke tab semula (TC-AUTH-OTP-104); reCAPTCHA mode uji.
- State global: versi Privacy Policy terbaru yang diterbitkan hook `before` tidak ditarik kembali oleh hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AUTH-OTP-101: Checkbox Agreement tidak pernah tampil di halaman Request OTP walau user memenuhi kondisi Agreement

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Verifikasi halaman Request OTP tidak memiliki checkbox "I have read and agree to the Privacy Policy *" sebelum email diketik
3. Ketik `rinaaditya+{runId}-031@qwertysystem.net` pada field Email
4. Amati halaman Request OTP
5. Verifikasi halaman Request OTP tidak memiliki checkbox "I have read and agree to the Privacy Policy *" sesudah email diketik
6. Centang widget reCAPTCHA "I'm not a robot"
7. Klik button [Request OTP]
8. Amati halaman Verify OTP
9. Verifikasi halaman Verify OTP juga tidak memiliki checkbox Agreement
10. Ketik 6 digit kode OTP dari email pada kotak digit
11. Verifikasi checkbox "I have read and agree to the Privacy Policy *" hanya muncul pada layar Confirm to Continue setelah kode OTP benar

### TC-AUTH-OTP-97: Login pertama memicu layar Confirm to Continue setelah OTP benar

12. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `dewihakim+{runId}-031@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Klik button [Request OTP]
16. Ketik 6 digit kode OTP dari email pada kotak digit
17. Verifikasi layar Confirm to Continue tampil dengan Title "Confirm to Continue" (kondisi login pertama)
18. Verifikasi layar Product Hub dan halaman MFA belum tampil
19. Buka Portal — Product Hub langsung di tab lain
20. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login

### TC-AUTH-OTP-104: Tautan Read the full Privacy Policy pada layar Agreement membuka dokumen di tab baru tanpa me-reset centang

21. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
22. Ketik `fajarcahyono+{runId}-031@qwertysystem.net` pada field Email
23. Centang widget reCAPTCHA "I'm not a robot"
24. Klik button [Request OTP]
25. Ketik 6 digit kode OTP dari email pada kotak digit
26. Centang checkbox "I have read and agree to the Privacy Policy *"
27. Klik tautan "Read the full Privacy Policy" pada Content Box
28. Verifikasi dokumen Privacy Policy versi aktif terbuka di tab baru
29. Kembali ke tab semula
30. Verifikasi layar Confirm to Continue tetap terbuka di tab semula
31. Verifikasi checkbox "I have read and agree to the Privacy Policy *" tetap tercentang
32. Verifikasi teks "Privacy Policy" pada label checkbox bukan tautan

### TC-AUTH-OTP-109: Menutup layar Confirm to Continue tanpa Continue membatalkan upaya login tanpa sesi

33. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Intan Nasution`, lalu catat baris teratas masing-masing sebagai baseline
34. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
35. Ketik `intannasution+{runId}-031@qwertysystem.net` pada field Email
36. Centang widget reCAPTCHA "I'm not a robot"
37. Klik button [Request OTP]
38. Ketik 6 digit kode OTP dari email pada kotak digit
39. Tutup tab browser tanpa mencentang checkbox dan tanpa klik Continue
40. Buka tab baru dan buka Portal — Product Hub langsung
41. Verifikasi Portal — Product Hub tidak terbuka; browser dialihkan ke halaman login
42. Verifikasi tidak ada sesi aktif untuk `Intan Nasution` pada browser
43. Ganti konteks ke browser admin dan muat ulang `Global Settings > Activity Log > Session` serta `Global Settings > User > Detail > User Log` untuk `Intan Nasution`
44. Verifikasi tidak ada baris baru untuk percobaan ini di `Global Settings > Activity Log > Session` dibanding baseline
45. Verifikasi tidak ada baris baru untuk percobaan ini di `Global Settings > User > Detail > User Log` dibanding baseline
46. Verifikasi tidak ada entri log untuk penutupan layar di kedua surface log
47. Kirim permintaan Verify OTP langsung ke server dengan email `intannasution+{runId}-031@qwertysystem.net` dan kode OTP yang sama yang sudah dipakai pada langkah 38
48. Verifikasi permintaan Verify OTP dengan kode yang sudah dipakai ditolak server
49. Verifikasi tidak ada sesi yang dibuat

### TC-AUTH-OTP-102: Klik Continue tanpa mencentang checkbox ditolak server dengan caption dan token tetap valid

50. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
51. Ketik `hendramaulana+{runId}-031@qwertysystem.net` pada field Email
52. Centang widget reCAPTCHA "I'm not a robot"
53. Klik button [Request OTP]
54. Ketik 6 digit kode OTP dari email pada kotak digit
55. Biarkan checkbox "I have read and agree to the Privacy Policy *" tidak dicentang
56. Klik button [Continue ➔]
57. Verifikasi permintaan konfirmasi ditolak server
58. Verifikasi caption error: "You need to agree to the Privacy Policy to continue"
59. Verifikasi button [Continue ➔] tetap enabled
60. Verifikasi layar Confirm to Continue tetap tampil
61. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan cari entri untuk `Hendra Maulana`
62. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Consent not given` di `Global Settings > Activity Log > Session`
63. Buka `Global Settings > User > Detail > User Log` untuk `Hendra Maulana`
64. Verifikasi tepat satu baris baru dibanding baseline hook `before` dengan Activity `Login`, Status `Failed`, Note `Consent not given` di `Global Settings > User > Detail > User Log`
65. Ganti konteks kembali ke jendela publik pada layar Confirm to Continue
66. Centang checkbox "I have read and agree to the Privacy Policy *"
67. Klik button [Continue ➔]
68. Verifikasi token pra-autentikasi masih valid dan persetujuan diterima: browser dialihkan ke Portal — Product Hub
69. Verifikasi sesi aktif untuk `Hendra Maulana`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini melebihi sekitar 35 langkah karena memuat lima TC dengan login penuh masing-masing; tiap TC memakai user dan jendela privat sendiri sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `caseType` `Positive`: TC sumber campuran (Positive: TC-97 dan TC-104; Negative: TC-101, TC-102, dan TC-109) dan prioritas tertinggi (P0) dimiliki TC-97 (Positive) dan TC-102 (Negative), sehingga spec mengikuti tujuan akhir alur (bagian 8): alur ditutup oleh TC-102 yang berakhir dengan Continue diterima dan sesi aktif.
- Urutan TC di dalam spec berbeda dari urutan TC sumber (97, 101, 102, 104, 109): screening tanpa aksi (checkbox tidak pernah tampil di halaman publik) di awal, kasus menutup layar (109) sebelum aksi yang berakhir dengan sesi aktif (102) (prinsip 3: screening → blokir → aksi sukses di akhir, S-10).
- Pengecualian P-1 (state berat): asersi absence TC-AUTH-OTP-109 (Expected c dan Post Condition b: "tidak ada baris baru untuk percobaan ini di kedua surface log" dan "tidak ada entri log untuk penutupan layar") tetap di spec ini dan tidak dipindah ke spec absence E2E-040, karena bergantung pada state Agreement (token pra-autentikasi yang baru diterbitkan dan layar Confirm to Continue yang ditutup) yang baru dibangun di blok ini. Asersi pencatatan `Consent not given` pada TC-AUTH-OTP-102 tetap di sini dan dicakup juga oleh TC-AUTH-OTP-126 di spec pencatatan.
- Pengecualian P-2 (pemicu bukan objek uji): langkah 47 memutar ulang kode yang sudah terpakai langsung ke server hanya sebagai langkah observasi Expected d dan Post Condition a TC-AUTH-OTP-109 ("kode OTP yang sudah dipakai tidak dapat dipakai lagi"), bukan sebagai objek uji replay (kelas a).
- Langkah 65 adalah langkah penghubung untuk kembali ke jendela publik setelah memeriksa log di browser admin (S-03). Langkah 33 (baseline) dan langkah 43 sampai 46 (ganti konteks dan verifikasi) pada TC-AUTH-OTP-109 ditambahkan di sekitar Expected c dan Post Condition b (diamati sebelum Verify langsung pada langkah 47, sesuai TC); TC sumber hanya memuat langkah membuka log tanpa baseline (S-03, S-14). Langkah 2 memenuhi bagian "sebelum" dari Expected a TC-AUTH-OTP-101 ("sebelum maupun sesudah email diketik"); langkah 5 memenuhi bagian "sesudah".
- Tab dokumen pada TC-AUTH-OTP-104 hanya memuat URL dokumen Privacy Policy dan tidak bertindak lintas tab dengan tab semula (bukan konteks kedua kelas c). Centang pada langkah 26 tidak disusul Continue, sehingga persetujuan `Fajar Cahyono` tidak tersimpan.
- Temuan untuk QA:
  - TC-AUTH-OTP-104 tidak menyebut judul atau URL dokumen Privacy Policy yang diharapkan di tab baru; asersi langkah 28 memakai "dokumen Privacy Policy versi aktif terbuka di tab baru" sesuai Expected TC.
  - TC-AUTH-OTP-109 langkah 9 mengirim Verify OTP langsung dengan kode terpakai saat user berada di layar Confirm to Continue yang ditutup. Penolakan server pada keadaan itu diasumsikan; di PRD baru terbukti untuk kode terpakai setelah login sukses (TC-AUTH-OTP-155). Mohon QA mengonfirmasi bahwa PRD juga menetapkannya pada keadaan ini.
  - TC-AUTH-OTP-102 Expected d menyebut "persetujuan tersimpan", tetapi tidak ada langkah observasinya; spec hanya memverifikasi hasil yang teramati (dialihkan ke Portal — Product Hub dengan sesi aktif). Bukti persistensi persetujuan ada pada TC-AUTH-OTP-142.
  - TC-AUTH-OTP-97 Post Condition menyebut token pra-autentikasi diterbitkan 10 menit dan kode OTP terpakai tanpa langkah observasi; spec tidak menambah asersi (batas 10 menit dicakup spec kedaluwarsa token).
  - TC-AUTH-OTP-109 langkah 6–7 menutup tab lalu membuka tab baru; spec mengasumsikan konteks browser yang sama sehingga tidak ada sesi tersisa. TC tidak menyebut konteks bersama ini secara eksplisit.
  - TC-AUTH-OTP-101 Pre-condition memakai profil POLICY, tetapi Expected tidak membedakan profil; spec memakai profil POLICY sesuai sumber.
