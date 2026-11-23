---
id: TC-AUTH-SES-E2E-080-keamanan-token-biometric-revoke-dan-integrity-token
title: "Keamanan Token Biometric: Pencabutan Kredensial User Lama dan integrityToken Kosong atau Invalid"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-334
  - TC-AUTH-SES-335
  - TC-AUTH-SES-336
coverage:
  mobile: automated
---

# Keamanan Token Biometric: Pencabutan Kredensial User Lama dan integrityToken Kosong atau Invalid

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric dan sidik jari terdaftar di OS). Semua TC memakai perangkat yang sama secara berurutan; tanpa sesi aktif di aplikasi saat spec dimulai.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, Tabel Data Uji Pre-setup #1, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #9: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-334: `Eka Saraswati` (`ekasaraswati+{runId}-080@qwertysystem.net`) dan `Indra Saputro` (`indrasaputro+{runId}-080@qwertysystem.net`, belum pernah login di perangkat Android uji B)
  - TC-AUTH-SES-335: `Joni Prasetyo` (`joniprasetyo+{runId}-080@qwertysystem.net`)
  - TC-AUTH-SES-336: `Melinda Putri` (`melindaputri+{runId}-080@qwertysystem.net`)
- Kondisi "sudah enroll biometric di perangkat Android uji B" dibuat sebagai langkah dengan alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14 dan 15; Tabel Data Uji Pre-setup #29) dengan data aplikasi yang bersih, karena token biometric lokal hanya dapat dibuat aplikasi di perangkat. Pada TC-AUTH-SES-334 sesi hasil login enroll dibiarkan Active (TC meminta sesi Active); pada TC-AUTH-SES-335 dan 336 sesi platform hasil login enroll diakhiri lewat API yang disediakan tim BE tanpa menghapus token biometric lokal (TC meminta tanpa sesi platform aktif).
- Suite berjalan serial (`parallel: false`); state global yang diubah: aturan proxy jaringan yang mengubah body request biometric re-login (TC-AUTH-SES-335 dan 336), data aplikasi dan token biometric lokal di perangkat Android uji B, serta kredensial biometric user uji. Aturan proxy dinonaktifkan lewat langkah eksplisit dan di hook `after`.
- Hook `after`: nonaktifkan semua aturan proxy jaringan; hapus data aplikasi pada perangkat Android uji B; akhiri semua sesi seed; hapus keempat user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor hanya di hook dan untuk pembacaan status dari backend.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness a: manipulasi token dan body request, dengan hardware biometrik kelas d sebagai prasyarat): driver otomasi Android (aplikasi native); simulasi sensor sidik jari pada OS biometric prompt Android (verifikasi lulus); menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; proxy jaringan (Tabel Data Uji Pre-setup #18) yang dapat membaca dan menyalin refresh token biometric dari lalu lintas app, membaca kode status respons dan body request biometric re-login, serta menjalankan aturan yang mengosongkan atau mengganti field `integrityToken` pada request biometric re-login; alat uji yang dapat mengirim request biometric re-login dengan refresh token dan ID device tertentu (Tabel Data Uji Pre-setup #18, TC-AUTH-SES-334); API yang disediakan tim BE untuk mengakhiri sesi platform tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29); pembacaan status kredensial biometric dan sesi user dari backend oleh akun aktor, disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-334: Enroll oleh user baru di perangkat yang sama mencabut kredensial biometric user lama

1. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `ekasaraswati+{runId}-080@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Enable] → OS biometric prompt muncul
6. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub dengan sesi mobile Active
7. Salin refresh token biometric `Eka Saraswati` lewat proxy jaringan sebelum logout
8. Di aplikasi mobile perangkat Android uji B buka menu Profile lalu pilih Log Out → form Login tampil
9. Ketik `indrasaputro+{runId}-080@qwertysystem.net` pada field Email
10. Ketik `Spectra.env.SES_PASSWORD` pada field Password
11. Klik [Login] → Prompt Enable Biometric muncul
12. Ketuk [Enable] → OS biometric prompt muncul
13. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
14. Verifikasi Enroll `Indra Saputro` sukses
15. Verifikasi Kredensial biometric `Eka Saraswati` pada perangkat Android uji B berstatus Revoked
16. Verifikasi Hanya kredensial `Indra Saputro` yang Active di perangkat Android uji B
17. Lewat alat uji kirim request biometric re-login memakai refresh token `Eka Saraswati` yang disalin pada langkah 7 dan ID device perangkat Android uji B
18. Verifikasi Request re-login dengan token `Eka Saraswati` ditolak
19. Verifikasi Tidak ada sesi baru untuk `Eka Saraswati`

### TC-AUTH-SES-335: Biometric re-login dengan integrityToken kosong ditolak 422 tanpa menghapus token lokal

20. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
21. Ketik `joniprasetyo+{runId}-080@qwertysystem.net` pada field Email
22. Ketik `Spectra.env.SES_PASSWORD` pada field Password
23. Klik [Login] → Prompt Enable Biometric muncul
24. Ketuk [Enable] → OS biometric prompt muncul
25. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
26. Akhiri sesi platform `joniprasetyo+{runId}-080@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29)
27. Hapus app dari recent apps
28. Aktifkan aturan proxy yang mengosongkan field `integrityToken` pada request biometric re-login
29. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil
30. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
31. Verifikasi Request biometric re-login langkah 30 ditolak `422`
32. Verifikasi toast error: "Error, failed to log in."
33. Verifikasi Tidak ada sesi baru untuk `Joni Prasetyo`
34. Verifikasi Screen biometric sign-in tetap tampil
35. Catat refresh token yang dikirim pada request biometric re-login langkah 30 dari proxy
36. Nonaktifkan aturan proxy
37. Hapus app dari recent apps
38. Buka kembali app → Screen biometric sign-in tampil
39. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
40. Verifikasi Token biometric lokal tidak dihapus dan tidak dirotasi: refresh token yang dikirim pada request biometric re-login langkah 39 sama dengan catatan langkah 35
41. Verifikasi Re-login langkah 39 berhasil masuk Portal — Product Hub

### TC-AUTH-SES-336: Biometric re-login dengan integrityToken invalid ditolak 422 tanpa menghapus token lokal

42. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
43. Ketik `melindaputri+{runId}-080@qwertysystem.net` pada field Email
44. Ketik `Spectra.env.SES_PASSWORD` pada field Password
45. Klik [Login] → Prompt Enable Biometric muncul
46. Ketuk [Enable] → OS biometric prompt muncul
47. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
48. Akhiri sesi platform `melindaputri+{runId}-080@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29)
49. Hapus app dari recent apps
50. Aktifkan aturan proxy yang mengganti nilai `integrityToken` dengan string acak pada request biometric re-login
51. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil
52. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
53. Verifikasi Request biometric re-login langkah 52 ditolak `422`
54. Verifikasi toast error: "Error, failed to log in."
55. Verifikasi Tidak ada sesi baru untuk `Melinda Putri`
56. Verifikasi Screen biometric sign-in tetap tampil
57. Catat refresh token yang dikirim pada request biometric re-login langkah 52 dari proxy
58. Nonaktifkan aturan proxy
59. Hapus app dari recent apps
60. Buka kembali app → Screen biometric sign-in tampil
61. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
62. Verifikasi Token biometric lokal tidak dihapus dan tidak dirotasi: refresh token yang dikirim pada request biometric re-login langkah 61 sama dengan catatan langkah 57
63. Verifikasi Re-login langkah 61 berhasil masuk Portal — Product Hub

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengelompokan: tiga TC keamanan token biometric dengan harness dominan yang sama (kelas a: request biometric re-login yang dimanipulasi lewat proxy atau dikirim alat uji, di atas perangkat biometric kelas d). TC-AUTH-SES-334 (Edge Case) digabung dengan TC-AUTH-SES-335 dan 336 (Security) karena objek ujinya sama, yaitu penolakan request biometric re-login yang tidak sah; caseType spec mengikuti alur dominan (Negative).
- Pembagian TC lintas spec (S-05): Expected d TC-AUTH-SES-335 dan 336 ("tidak ada entri log untuk percobaan langkah 2; hanya `Login with biometric` dari langkah 3") adalah asersi absence dan ditulis di spec absence `TC-AUTH-SES-E2E-070-absence-biometric` dengan user dan aksi sendiri (bagian absence, Expected d).
- Urutan mengikuti TC sumber (334, 335, 336); tidak ada penyimpangan (S-10). Tiap TC memakai user sendiri.
- Dependensi (S-04): TC-AUTH-SES-335 dan 336 bergantung pada TC-AUTH-SES-152 (biometric re-login sukses); alur enroll dan penyiapan tanpa sesi platform (langkah 20–27 dan 42–49) disalin di tiap TC. TC-AUTH-SES-334 menyalin alur enroll di langkah 1–6.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): hapus data aplikasi di awal tiap TC; blok enroll; menyalin dan mencatat refresh token dari proxy (langkah 7, 35, 57) sebagai pembanding asersi "tidak dirotasi" (S-14); mengaktifkan dan menonaktifkan aturan proxy; mengakhiri sesi platform lewat API tim BE; menghapus app dari recent apps lalu membukanya kembali.
- Jumlah langkah (63) melewati batas sekitar 35 langkah karena tiga TC masing-masing menyalin blok enroll berpola sendiri (langkah 1–6, 20–27, 42–49; tidak dihitung ke batas) dan TC-AUTH-SES-335 serta 336 masing-masing memuat dua percobaan re-login (dengan dan tanpa aturan proxy) yang dibandingkan; tanpa blok enroll jumlahnya sekitar 41. Memecah spec akan mengulang harness proxy dan perangkat yang sama tanpa mengurangi langkah per TC.
- Temuan untuk QA: (1) TC-AUTH-SES-334 precondition c menyebut refresh token biometric `Eka Saraswati` "disalin lewat proxy jaringan sebelum logout" tanpa menyebut request atau respons yang membawanya; spec menyalinnya dari lalu lintas app lewat proxy sebelum Log Out. (2) TC-AUTH-SES-334 langkah 3 tidak menyebut nilai `integrityToken` pada request alat uji; PRD §9.9 V-14 mewajibkan `integrityToken` valid, sehingga tanpa token integritas yang sah penolakan tidak membuktikan pencabutan kredensial (bisa ditolak karena V-14). QA perlu menentukan cara alat uji memperoleh `integrityToken` yang sah. (3) TC-AUTH-SES-334 Expected b dan c serta TC-AUTH-SES-335 dan 336 Expected a ("tidak ada sesi baru") tidak menyebut cara membaca status kredensial dan sesi; spec memakai pembacaan dari backend yang disediakan tim FE/BE tanpa endpoint karangan (S-13). (4) TC-AUTH-SES-334 langkah 1 menulis "Log Out" tanpa letak menu; spec memakai menu Profile lalu Log Out seperti TC-AUTH-SES-331. (5) TC-AUTH-SES-335 dan 336 Expected b menyebut "Screen biometric sign-in tetap tampil" sesudah penolakan langkah 2; spec mengasersinya sebelum aturan proxy dinonaktifkan (langkah 34 dan 56).
