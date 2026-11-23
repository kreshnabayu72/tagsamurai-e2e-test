---
id: TC-AUTH-SES-E2E-048-biometric-token-agreement-dan-privacy-policy
title: "Re-login Biometric: Navigasi Back pada Confirm to Continue, Kegagalan Server Confirm Agreement, dan Privacy Policy Tidak Ter-resolve"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-166
  - TC-AUTH-SES-167
  - TC-AUTH-SES-325
coverage:
  mobile: automated
---

# Re-login Biometric: Navigasi Back pada Confirm to Continue, Kegagalan Server Confirm Agreement, dan Privacy Policy Tidak Ter-resolve

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS). Semua TC memakai perangkat yang sama.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil BIOPOL milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #22 dan #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; berbasis profil BIO yang belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-167: `Citra Pratama` (`citrapratama+{runId}-048@qwertysystem.net`)
  - TC-AUTH-SES-166: `Joko Lestari` (`jokolestari+{runId}-048@qwertysystem.net`)
  - TC-AUTH-SES-325: `Bayu Kusuma` (`bayukusuma+{runId}-048@qwertysystem.net`)
- Kondisi BIOPOL (state per-user: versi Privacy Policy yang terakhir disetujui user lebih lama dari versi aktif; tanpa mempublish Privacy Policy global) diterapkan BE pada langkah "Terapkan kondisi" sesudah enroll, supaya login password saat enroll tidak memicu Agreement.
- Kondisi awal tiap TC "sudah enroll biometric di perangkat Android uji B; tidak ada sesi platform aktif" dibuat di dalam TC dengan menyalin langkah enroll TC-AUTH-SES-145 (hapus data aplikasi, login, [Enable], lulus sidik jari), lalu mengakhiri sesi platform hasil login enroll lewat Manual Logout di aplikasi (menu Profile → Log Out; logout mobile tidak menghapus token biometric lokal dan tidak mencabut kredensial di server) dan menghapus app dari recent apps sehingga pembukaan berikutnya menampilkan Screen "Sign in with biometrics" (cara menyiapkan mengikuti Tabel Data Uji Pre-setup #29), karena token biometric lokal dan status "sudah ditawari" disimpan di perangkat dan hanya dapat dibuat oleh aplikasi.
- Suite berjalan serial (`parallel: false`), juga karena perangkat Android uji B dipakai bersama; state global yang diubah dan pemulihannya di hook `after`: (a) failure injection 5xx pada request Confirm Agreement (TC-AUTH-SES-166; dinonaktifkan); (b) fixture BE versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi (TC-AUTH-SES-325; dipulihkan ke versi terpublikasi).
- Hook `after`: pulihkan kedua state global di atas, hapus data aplikasi pada perangkat Android uji B, akhiri semua sesi seed, lalu hapus ketiga user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; tanpa akun aktor di langkah.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik; kelas b: failure injection): driver otomasi Android (aplikasi native); simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus); menekan tombol back OS; menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; failure injection 5xx pada request Confirm Agreement (Tabel Data Uji Pre-setup #18); fixture BE untuk versi Privacy Policy aktif tidak ter-resolve; pembacaan status sesi user uji dan rotasi refresh token biometric dari sisi backend (langkah 49, 50), disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-167: Navigasi back OS tidak menutup Screen Confirm to Continue

1. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `citrapratama+{runId}-048@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Enable] → OS biometric prompt muncul
6. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
7. Buka menu Profile lalu pilih Log Out → form Login tampil (Manual Logout mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal dan tanpa mencabut kredensial biometric; Tabel Data Uji Pre-setup #29)
8. Hapus app dari recent apps
9. Terapkan kondisi profil BIOPOL untuk `Citra Pratama` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
10. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
11. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Screen Confirm to Continue tampil
12. Tekan tombol back OS pada Screen Confirm to Continue
13. Verifikasi Screen Confirm to Continue tetap tampil
14. Verifikasi Tidak ada tombol Cancel atau Back

### TC-AUTH-SES-166: Kegagalan server saat Confirm Agreement menampilkan toast error dan token tetap valid

15. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
16. Ketik `jokolestari+{runId}-048@qwertysystem.net` pada field Email
17. Ketik `Spectra.env.SES_PASSWORD` pada field Password
18. Klik [Login] → Prompt Enable Biometric muncul
19. Ketuk [Enable] → OS biometric prompt muncul
20. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
21. Buka menu Profile lalu pilih Log Out → form Login tampil (Manual Logout mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal dan tanpa mencabut kredensial biometric; Tabel Data Uji Pre-setup #29)
22. Hapus app dari recent apps
23. Terapkan kondisi profil BIOPOL untuk `Joko Lestari` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
24. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
25. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Screen Confirm to Continue tampil
26. Aktifkan failure injection 5xx pada request Confirm Agreement
27. Centang checkbox "I have read and agree to the Privacy Policy *"
28. Ketuk [Continue ➔]
29. Verifikasi toast error: "Error, failed to confirm agreement."
30. Verifikasi Screen Confirm to Continue tetap tampil
31. Nonaktifkan failure injection
32. Ketuk [Continue ➔] lagi
33. Verifikasi Percobaan kedua berhasil memakai token pra-autentikasi yang sama
34. Verifikasi App masuk Portal — Product Hub

### TC-AUTH-SES-325: Biometric Re-login diblok saat versi Privacy Policy aktif tidak dapat ditentukan

35. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
36. Ketik `bayukusuma+{runId}-048@qwertysystem.net` pada field Email
37. Ketik `Spectra.env.SES_PASSWORD` pada field Password
38. Klik [Login] → Prompt Enable Biometric muncul
39. Ketuk [Enable] → OS biometric prompt muncul
40. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
41. Buka menu Profile lalu pilih Log Out → form Login tampil (Manual Logout mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal dan tanpa mencabut kredensial biometric; Tabel Data Uji Pre-setup #29)
42. Hapus app dari recent apps
43. Terapkan kondisi profil BIOPOL untuk `Bayu Kusuma` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
44. Atur versi Privacy Policy aktif menjadi tidak ter-resolve atau belum ada versi terpublikasi (fixture BE)
45. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
46. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
47. Verifikasi Toast gagal tampil
48. Verifikasi Screen Confirm to Continue tidak tampil
49. Verifikasi Tidak ada sesi baru di perangkat
50. Verifikasi Refresh token biometric tidak dirotasi
51. Pulihkan versi Privacy Policy aktif sehingga dapat ditentukan (fixture BE)
52. Hapus app dari recent apps
53. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
54. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
55. Verifikasi Relogin biometric berikutnya berjalan normal: Screen Confirm to Continue tampil

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-167, 166, 325 (urutan TC sumber 166, 167, 325). Screening tanpa state (167) didahulukan, kegagalan server (166) berikutnya, dan TC yang mengubah state global versi Privacy Policy (325) ditaruh paling akhir.
- Pengecualian `P-5` (b): TC-AUTH-SES-166 (satu kegagalan 5xx pada Confirm Agreement, kelas b) dan TC-AUTH-SES-325 (satu kegagalan fixture versi Privacy Policy tidak ter-resolve, kelas b) adalah dua TC objek-uji ringan tanpa harness eksternal tambahan, pada layar Confirm to Continue yang sama dengan TC lain di spec ini; ketiga TC berbagi enroll biometric dan Screen Confirm to Continue sebagai kondisi awal.
- TC-AUTH-SES-165 dan 286 (umur token pra-autentikasi, time-travel) ada di spec `TC-AUTH-SES-E2E-075-biometric-agreement-token-ttl-boundary`.
- Dependensi (S-04): TC-AUTH-SES-167, 325 bergantung pada TC-AUTH-SES-16 (membuka app, lulus OS biometric prompt, Screen Confirm to Continue tampil); langkah itu disalin pada langkah 10-11 dan 45-46. Semua TC bergantung pada enroll (TC-AUTH-SES-145): langkah enroll disalin di awal tiap TC, termasuk langkah mengakhiri sesi platform hasil login enroll lewat Manual Logout di aplikasi (menu Profile → Log Out) lalu menghapus app dari recent apps (Pre-setup #29); logout mobile tidak menghapus token biometric lokal dan tidak mencabut kredensial biometric.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): "Hapus data aplikasi" di awal tiap TC (S-09); "Terapkan kondisi profil" sesudah enroll; langkah 51-54 pada TC-AUTH-SES-325 memulihkan versi Privacy Policy lalu mengulang relogin.
- Pembagian TC lintas spec: asersi "tidak ada entri log baru" untuk percobaan yang diblok (TC-AUTH-SES-325 Expected c) tidak ditulis di spec ini dan berada di spec absence `TC-AUTH-SES-E2E-070-absence-biometric` (kelas g, S-05).
- Jumlah langkah (55) melewati sekitar 35 karena tiga TC, masing-masing dengan user dan sesi sendiri, menyalin prefix enroll per TC (S-04); tiap TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal. Blok enroll tidak dihitung ke batas ±35.
- Temuan untuk QA: (1) TC sumber menulis login dan enroll tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] (label tombol login mobile tidak disebut TC). (2) Profil BIOPOL menuntut versi Privacy Policy yang lebih baru dari yang disetujui, tetapi kondisi itu tidak boleh sudah berlaku saat enroll lewat login password; TC tidak menyebut urutannya, sehingga spec menambah langkah "Terapkan kondisi profil" sesudah enroll. Sifat kondisi BIOPOL (per-user atau publish Privacy Policy global) tidak ditetapkan TC dan PRD; spec memperlakukannya sebagai state per-user. (3) TC-AUTH-SES-325 Expected a ("toast gagal") tidak menyebut teks toast; Expected d ("berjalan normal") tidak menyebut layar yang diharapkan; spec mengasersi Screen Confirm to Continue tampil. (4) TC-AUTH-SES-325 Expected b ("refresh token tidak dirotasi") tidak menyebut cara mengamatinya; spec mengasersinya sebagaimana tertulis.
