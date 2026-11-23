---
id: TC-AUTH-SES-E2E-081-toggle-biometric-sign-in-resilience
title: "Toggle Biometric Sign-in: Disabled Selama Request, Kegagalan Server, dan Cancel Prompt"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-338
  - TC-AUTH-SES-339
  - TC-AUTH-SES-340
coverage:
  mobile: automated
---

# Toggle Biometric Sign-in: Disabled Selama Request, Kegagalan Server, dan Cancel Prompt

## Prerequisites

- Mode: FE+BE. Kegagalan 5xx pada TC-AUTH-SES-339 dipaksakan di sisi server lewat failure injection (Tabel Data Uji Pre-setup #18); aplikasi mobile tidak dapat memakai `Spectra.intercept()`, sehingga spec tetap berjalan terhadap backend nyata.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric dan sidik jari terdaftar di OS). Semua TC memakai perangkat yang sama secara berurutan; tanpa sesi aktif di aplikasi saat spec dimulai.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, Tabel Data Uji Pre-setup #1, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #9: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-338: `Oki Firmansyah` (`okifirmansyah+{runId}-081@qwertysystem.net`)
  - TC-AUTH-SES-339: `Putu Ariani` (`putuariani+{runId}-081@qwertysystem.net`)
  - TC-AUTH-SES-340: `Rudi Hartanto` (`rudihartanto+{runId}-081@qwertysystem.net`)
- Kondisi "sesi mobile aktif setelah memilih [Not now]" dibuat sebagai langkah di awal tiap TC (login nyata lalu ketuk [Not now], alur TC-AUTH-SES-146) dengan data aplikasi yang bersih.
- Suite berjalan serial (`parallel: false`); state global yang diubah: aturan proxy jaringan yang menunda respons request enroll (TC-AUTH-SES-338), failure injection 5xx pada request enroll (TC-AUTH-SES-339), data aplikasi dan token biometric lokal di perangkat Android uji B, serta kredensial biometric user uji. Aturan proxy dan failure injection dinonaktifkan lewat langkah eksplisit dan di hook `after`.
- Hook `after`: nonaktifkan aturan proxy dan failure injection; hapus data aplikasi pada perangkat Android uji B; akhiri semua sesi seed; hapus ketiga user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor hanya di hook.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik; TC-AUTH-SES-339 memakai kelas b): driver otomasi Android (aplikasi native); simulasi sensor sidik jari pada OS biometric prompt Android (verifikasi lulus) dan pembatalan OS biometric prompt; menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; pembacaan state enabled atau disabled toggle "Biometric sign-in"; proxy jaringan (Tabel Data Uji Pre-setup #18) yang dapat menunda respons request enroll 5 detik dan mencatat jumlah request enroll; failure injection 5xx pada request enroll yang dapat diaktifkan dan dinonaktifkan dari alat uji.

## Test Steps

### TC-AUTH-SES-338: Toggle Biometric sign-in disabled selama request enroll berjalan

1. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `okifirmansyah+{runId}-081@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Not now] → app masuk Portal — Product Hub
6. Aktifkan aturan proxy yang menunda respons request enroll 5 detik
7. Buka Settings > Security
8. Nyalakan toggle "Biometric sign-in" → OS biometric prompt muncul
9. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
10. Selama respons tertunda ketuk toggle "Biometric sign-in" berulang kali
11. Verifikasi Toggle "Biometric sign-in" disabled selama request berjalan
12. Verifikasi Ketukan tambahan tidak memicu request baru
13. Tunggu respons request enroll selesai
14. Verifikasi Proxy hanya mencatat satu request enroll
15. Verifikasi Setelah respons sukses toggle "Biometric sign-in" On
16. Verifikasi toast sukses: "Success, biometric enabled."
17. Nonaktifkan aturan proxy

### TC-AUTH-SES-339: Kegagalan server saat enroll lewat toggle mengembalikan toggle ke Off dengan toast error

18. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
19. Ketik `putuariani+{runId}-081@qwertysystem.net` pada field Email
20. Ketik `Spectra.env.SES_PASSWORD` pada field Password
21. Klik [Login] → Prompt Enable Biometric muncul
22. Ketuk [Not now] → app masuk Portal — Product Hub
23. Aktifkan failure injection 5xx pada request enroll
24. Buka Settings > Security
25. Nyalakan toggle "Biometric sign-in" → OS biometric prompt muncul
26. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
27. Verifikasi toast error: "Error, failed to enable biometric."
28. Verifikasi Toggle "Biometric sign-in" kembali Off
29. Nonaktifkan failure injection
30. Buka menu Profile lalu pilih Log Out → form Login tampil
31. Hapus app dari recent apps
32. Buka kembali app
33. Verifikasi Setelah app dibuka kembali form Login tampil
34. Verifikasi Screen biometric sign-in tidak tampil

### TC-AUTH-SES-340: Cancel OS biometric prompt saat menyalakan toggle mengembalikan toggle ke Off tanpa error

35. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
36. Ketik `rudihartanto+{runId}-081@qwertysystem.net` pada field Email
37. Ketik `Spectra.env.SES_PASSWORD` pada field Password
38. Klik [Login] → Prompt Enable Biometric muncul
39. Ketuk [Not now] → app masuk Portal — Product Hub
40. Mulai pemantauan request enroll di proxy jaringan
41. Buka Settings > Security
42. Nyalakan toggle "Biometric sign-in" → OS biometric prompt muncul
43. Batalkan (cancel) OS biometric prompt
44. Verifikasi Toggle "Biometric sign-in" kembali Off
45. Verifikasi Tidak ada toast error
46. Verifikasi Tidak ada request enroll yang terkirim
47. Buka menu Profile lalu pilih Log Out → form Login tampil
48. Hapus app dari recent apps
49. Buka kembali app
50. Verifikasi Setelah app dibuka kembali form Login tampil
51. Verifikasi Screen biometric sign-in tidak tampil

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengelompokan: tiga TC jalur gagal atau batas pada toggle "Biometric sign-in" di Settings > Security dengan harness dominan yang sama (perangkat biometric, kelas d). Jalur sukses toggle (TC-AUTH-SES-315) ada di spec `TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll`; kegagalan server saat enroll lewat Prompt (TC-AUTH-SES-150) ada di spec `TC-AUTH-SES-E2E-052-resilience-biometric-enroll-login-disable`.
- Pengecualian P-5(b): TC-AUTH-SES-339 (failure injection 5xx, kelas b ringan) ditaruh di spec fungsional ini karena harness dominannya sama (perangkat biometric) dan hanya satu TC kelas b di spec ini.
- Penundaan respons 5 detik lewat proxy pada TC-AUTH-SES-338 hanya dipakai untuk mengamati state toggle selama request berjalan, sehingga bukan kelas b. Pemantauan request di proxy pada TC-AUTH-SES-340 bersifat pengamat (P-6).
- Urutan mengikuti TC sumber (338, 339, 340); tidak ada penyimpangan (S-10). Tiap TC memakai user sendiri.
- Dependensi (S-04): ketiga TC bergantung pada TC-AUTH-SES-146 ([Not now] pada Prompt Enable Biometric); langkah 1–5, 18–22, dan 35–39 menyalin login sampai [Not now]. Prefix login ini tidak dihitung ke batas sekitar 35 langkah.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): hapus data aplikasi di awal tiap TC (S-09); mengaktifkan dan menonaktifkan aturan proxy serta failure injection; memulai pemantauan proxy (langkah 40); membuka Settings > Security; menunggu respons (langkah 13); Log Out, menghapus app dari recent apps, lalu membukanya kembali (langkah 30–32 dan 47–49).
- Temuan untuk QA: (1) TC-AUTH-SES-339 dan 340 langkah 2 menulis "Log Out" tanpa letak menu; spec memakai menu Profile lalu Log Out seperti TC-AUTH-SES-331. (2) TC-AUTH-SES-338 tidak menyebut kapan aturan penundaan proxy diaktifkan; spec mengaktifkannya sebelum membuka Settings > Security. (3) TC-AUTH-SES-340 precondition c "proxy memantau request enroll" tidak menyebut titik awal pemantauan; spec memulai pemantauan sebelum membuka Settings > Security (langkah 40), sehingga asersi "tidak ada request enroll" mencakup jendela toggle sampai pembatalan. (4) TC sumber menulis "password yang benar" atau "login" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD`.
