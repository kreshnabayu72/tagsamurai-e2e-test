---
id: TC-AUTH-SES-E2E-075-biometric-agreement-token-ttl-boundary
title: "Re-login Biometric: Umur Token Pra-autentikasi Agreement 10 Menit (Kedaluwarsa dan Batas Eksak)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-165
  - TC-AUTH-SES-286
coverage:
  mobile: automated
---

# Re-login Biometric: Umur Token Pra-autentikasi Agreement 10 Menit (Kedaluwarsa dan Batas Eksak)

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS). Kedua TC memakai perangkat yang sama.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil BIOPOL milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #22 dan #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; berbasis profil BIO yang belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-165: `Intan Permata` (`intanpermata+{runId}-075@qwertysystem.net`)
  - TC-AUTH-SES-286: `Joko Wibowo` (`jokowibowo+{runId}-075@qwertysystem.net`)
- Kondisi BIOPOL (Principal sudah mempublish versi Privacy Policy lebih baru dari yang terakhir disetujui user) diterapkan BE pada langkah "Terapkan kondisi" sesudah enroll, supaya login password saat enroll tidak memicu Agreement.
- Kondisi awal tiap TC "sudah enroll biometric di perangkat Android uji B; tidak ada sesi platform aktif" (cara menyiapkan: Tabel Data Uji Pre-setup #29) dibuat di dalam TC dengan menyalin langkah enroll TC-AUTH-SES-145 (hapus data aplikasi, login, [Enable], lulus sidik jari, akhiri sesi platform hasil login enroll lewat BE tanpa menghapus token biometric lokal, hapus app dari recent apps), karena token biometric lokal dan status "sudah ditawari" disimpan di perangkat dan hanya dapat dibuat oleh aplikasi.
- Suite berjalan serial (`parallel: false`); state global yang diubah dan pemulihannya di hook `after`: jam server dan jam browser/perangkat (diatur bersama, dimajukan pada TC-AUTH-SES-165 dan 286; dikembalikan ke waktu nyata, juga bila spec gagal di tengah sebelum langkah pemulihan); perangkat Android uji B dipakai bersama (data aplikasi dihapus di hook `after`).
- Hook `after`: pulihkan jam server dan jam browser/perangkat ke waktu nyata, hapus data aplikasi pada perangkat Android uji B, akhiri semua sesi seed, lalu hapus kedua user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; tanpa akun aktor di langkah.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik dan time-travel): driver otomasi Android (aplikasi native); simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus); menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; jam server dan jam browser/perangkat dapat diatur bersama, dimajukan, diset absolut dengan presisi detik, dan dipulihkan ke waktu nyata (Tabel Data Uji Pre-setup #18); pembacaan status sesi user uji dari sisi backend (langkah 17), disediakan tim FE/BE; penerapan kondisi profil BIOPOL per user oleh BE (langkah 9, 27, dan 37), disediakan tim FE/BE; mengakhiri sesi platform hasil login enroll (langkah 7 dan 25) dan sesi platform hasil Continue pada umur token 10:00 (langkah 35) lewat BE (API yang disediakan BE, tanpa menghapus token biometric lokal; Tabel Data Uji Pre-setup #29), disediakan tim FE/BE, tanpa endpoint.
- Titik waktu: umur token pra-autentikasi Agreement dihitung sejak OS biometric prompt lulus dan Screen Confirm to Continue tampil; tiap TC mengukurnya pada TC-nya sendiri.

## Test Steps

### TC-AUTH-SES-165: Token pra-autentikasi Agreement kedaluwarsa memaksa fallback ke Login penuh

1. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `intanpermata+{runId}-075@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Enable] → OS biometric prompt muncul
6. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
7. Akhiri sesi platform hasil login enroll `Intan Permata` lewat BE (token biometric lokal tidak dihapus)
8. Hapus app dari recent apps
9. Terapkan kondisi profil BIOPOL untuk `Intan Permata` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
10. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
11. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Screen Confirm to Continue tampil
12. Biarkan Screen Confirm to Continue terbuka dan majukan jam server dan jam browser/perangkat bersama 10 menit 30 detik
13. Centang checkbox "I have read and agree to the Privacy Policy *"
14. Ketuk [Continue ➔]
15. Verifikasi Request ditolak karena token pra-autentikasi kedaluwarsa
16. Verifikasi App diarahkan ke halaman Login penuh
17. Verifikasi Tidak ada sesi baru untuk `Intan Permata`
18. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-286: Token pra-autentikasi Agreement masih valid pada menit ke-10 dan ditolak sesudahnya

19. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
20. Ketik `jokowibowo+{runId}-075@qwertysystem.net` pada field Email
21. Ketik `Spectra.env.SES_PASSWORD` pada field Password
22. Klik [Login] → Prompt Enable Biometric muncul
23. Ketuk [Enable] → OS biometric prompt muncul
24. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
25. Akhiri sesi platform hasil login enroll `Joko Wibowo` lewat BE (token biometric lokal tidak dihapus)
26. Hapus app dari recent apps
27. Terapkan kondisi profil BIOPOL untuk `Joko Wibowo` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
28. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
29. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Screen Confirm to Continue tampil
30. Atur jam server dan jam browser/perangkat bersama secara absolut ke waktu terbit token pra-autentikasi + 10 menit 00 detik
31. Centang checkbox "I have read and agree to the Privacy Policy *"
32. Ketuk [Continue ➔]
33. Verifikasi Pada umur token 10:00 Continue berhasil
34. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
35. Akhiri sesi platform `Joko Wibowo` hasil Continue pada umur token 10:00 lewat BE (token biometric lokal tidak dihapus)
36. Hapus app dari recent apps
37. Terapkan ulang kondisi profil BIOPOL untuk `Joko Wibowo` (di-seed BE)
38. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
39. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Screen Confirm to Continue tampil
40. Atur jam server dan jam browser/perangkat bersama secara absolut ke waktu terbit token pra-autentikasi baru + 10 menit 01 detik
41. Centang checkbox "I have read and agree to the Privacy Policy *"
42. Ketuk [Continue ➔]
43. Verifikasi Pada umur token 10:01 request ditolak
44. Verifikasi Pada umur token 10:01 app diarahkan ke halaman Login penuh
45. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan di spec ini TC-AUTH-SES-165, 286 (urutan TC sumber sama). TC-AUTH-SES-286 bergantung pada TC-AUTH-SES-165, sehingga 165 tampil lebih dulu; keduanya menggeser jam dan memulihkannya sebelum TC berikutnya.
- TC-AUTH-SES-165 dan 286 (umur token pra-autentikasi sebagai objek uji, kelas d) ada di spec ini; TC-AUTH-SES-166, 167, 325 ada di spec `TC-AUTH-SES-E2E-048-biometric-token-agreement-dan-privacy-policy`.
- Ukuran: spec memuat 45 langkah. Blok enroll biometric yang identik antar-TC (hapus data aplikasi sampai hapus app dari recent apps, langkah 1 sampai 8 dan 19 sampai 26) tidak dihitung ke batas sekitar 35 langkah (konvensi bagian 3), sehingga langkah yang dihitung 29. Tiap TC punya user dan sesi sendiri, jadi bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal.
- Dependensi (S-04): TC-AUTH-SES-286 bergantung pada TC-AUTH-SES-165; langkah 28 sampai 29 menyalin langkah pembuka TC-AUTH-SES-165 (langkah 10 sampai 11). Kedua TC bergantung pada enroll (TC-AUTH-SES-145): langkah enroll disalin di awal tiap TC.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): "Hapus data aplikasi" di awal tiap TC (S-09); "Akhiri sesi platform hasil login enroll" dan "Terapkan kondisi profil" sesudah enroll; langkah 35 sampai 39 pada TC-AUTH-SES-286 mengulang alur dari awal (akhiri sesi platform hasil Continue 10:00 lewat BE supaya perangkat kembali tanpa sesi platform aktif sesuai prakondisi, hapus app, terapkan ulang kondisi BIOPOL karena persetujuan Agreement pada percobaan 10:00 sudah tercatat, buka app, lulus biometric) supaya percobaan 10:01 memakai token pra-autentikasi baru.
- Jam diatur bersama (server dan browser/perangkat) dan dipulihkan di langkah 18, 34, dan 45 sebelum percobaan atau TC berikutnya; pada TC-AUTH-SES-286 batas eksak 10:00 dan 10:01 diset absolut (bukan digeser relatif) terhadap waktu terbit token pra-autentikasi tiap percobaan, dan jam dipulihkan di langkah 34 supaya token percobaan 10:01 terbit pada waktu nyata. Spec ini tidak membuka Activity Log atau User Log.
- Temuan untuk QA: (1) TC sumber menulis login dan enroll tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] (label tombol login mobile tidak disebut TC). (2) Profil BIOPOL menuntut versi Privacy Policy yang lebih baru dari yang disetujui, tetapi kondisi itu tidak boleh sudah berlaku saat enroll lewat login password; TC tidak menyebut urutannya, sehingga spec menambah langkah "Terapkan kondisi profil" sesudah enroll. (3) TC-AUTH-SES-286 langkah 4 ("Ulangi dari awal") tidak menyebut bahwa persetujuan pada percobaan pertama membuat Agreement tidak terpicu lagi; spec menerapkan ulang kondisi BIOPOL. (4) TC-AUTH-SES-165/286 tidak menyebut apakah sesi mobile idle (15 menit) terpengaruh oleh pergeseran jam 10 menit 30 detik; spec mengikuti TC. (5) TC-AUTH-SES-165 Expected b ("tidak ada sesi baru") tidak memberi cara cek; spec memakai pembacaan status sesi dari sisi backend (Prerequisites) tanpa menyebut endpoint. (6) TC-AUTH-SES-286 langkah 3-4 menyebut "majukan" tanpa menyatakan jam diatur absolut dan dipulihkan di antara dua percobaan; spec mengatur jam absolut terhadap waktu terbit token (konvensi bagian 6) dan memulihkannya sebelum percobaan 10:01. (7) Pre-setup #29 menyebut sesi hasil login enroll diakhiri lewat API yang disediakan BE tanpa nama API; spec menulisnya sebagai kemampuan disediakan tim FE/BE tanpa endpoint. (8) TC-AUTH-SES-286 Langkah 4 ("Ulangi dari awal") tidak menyebut bahwa sesi platform hasil Continue pada umur token 10:00 harus diakhiri, padahal prakondisi b mensyaratkan perangkat tanpa sesi platform aktif; spec mengakhirinya lewat BE (Pre-setup #29) di langkah 35 sebelum mengulang.
