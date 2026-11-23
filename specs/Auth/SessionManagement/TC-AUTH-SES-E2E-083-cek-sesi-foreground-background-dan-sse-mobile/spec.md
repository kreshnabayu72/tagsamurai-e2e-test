---
id: TC-AUTH-SES-E2E-083-cek-sesi-foreground-background-dan-sse-mobile
title: "Cek Sesi Mobile di Foreground dan Background: Hitungan Mundur Lokal, SSE, dan Pembaruan Kedaluwarsa"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-344
  - TC-AUTH-SES-347
  - TC-AUTH-SES-348
coverage:
  web: automated
  mobile: automated
---

# Cek Sesi Mobile di Foreground dan Background: Hitungan Mundur Lokal, SSE, dan Pembaruan Kedaluwarsa

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji A (Tabel Data Uji Pre-setup #10). Semua TC memakai perangkat yang sama secara berurutan; tanpa sesi aktif di aplikasi saat spec dimulai.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, Tabel Data Uji Pre-setup #1, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-344: `Zahra Fitriani` (`zahrafitriani+{runId}-083@qwertysystem.net`)
  - TC-AUTH-SES-347: `Dian Marlina` (`dianmarlina+{runId}-083@qwertysystem.net`)
  - TC-AUTH-SES-348: `Erwin Susanto` (`erwinsusanto+{runId}-083@qwertysystem.net`)
- Sesi mobile tiap TC dibuat lewat login nyata di perangkat Android uji A dan ketuk [Not now] bila Prompt Enable Biometric muncul (Tabel Data Uji Pre-setup #28), sebagai langkah di awal bagian TC.
- Browser License (login di hook `before`): Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, Global Role Manage Global License), kredensial `Spectra.env.FA_MGL_PASSWORD`, membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) pada TC-AUTH-SES-344.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat (dimajukan bersama di tiap TC dan dipulihkan ke waktu nyata di akhir tiap TC), perangkat Android uji A yang dipakai bersama, pemantauan proxy jaringan.
- Hook `after`: pulihkan jam server dan jam browser/perangkat ke waktu nyata; hentikan pemantauan proxy; hapus data aplikasi pada perangkat Android uji A; akhiri semua sesi seed dan sesi-produk; tutup Browser License; hapus ketiga user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; Admin License pada Browser License; akun aktor Total Control hanya di hook.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Menunggu waktu nyata tidak dipakai; jeda dipenuhi dengan menggeser jam server dan jam browser/perangkat bersama.
- Kemampuan teknis: driver otomasi Android (aplikasi native; kirim app ke background tanpa menghapusnya dari recent apps, buka kembali dari recent apps, membiarkan app di foreground tanpa sentuhan); proxy jaringan (Tabel Data Uji Pre-setup #18) yang mencatat request perangkat Android uji A, koneksi SSE (buka dan tutup), serta respons cek sesi; jam server uji dan jam browser/perangkat yang dimajukan bersama dan dipulihkan ke waktu nyata (Tabel Data Uji Pre-setup #18); pembacaan read-only tabel `sessions` per `user_id` (kolom `status`, `expires_at`; karena expire bersifat lazy, sesi dibaca Expired bila `status = 'expired'` atau `status = 'active'` dengan `expires_at` ≤ waktu server; Tabel Data Uji Pre-setup #18); reCAPTCHA mode uji di environment (login ulang Browser License pada TC-AUTH-SES-344).

## Test Steps

### TC-AUTH-SES-344: Hitungan mundur lokal habis saat app di foreground memicu cek server, sesi Expired, dan seat langsung dilepas

1. Bersihkan state app mobile di perangkat Android uji A (hapus data aplikasi, tutup dialog yang masih tampil), lalu buka aplikasi mobile di perangkat Android uji A, login sebagai `zahrafitriani+{runId}-083@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] bila Prompt Enable Biometric muncul, dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
2. Di aplikasi mobile ketuk card Fixed Asset → Fixed Asset tampil (sesi-produk Fixed Asset Active, seat terpakai)
3. Mulai pemantauan request perangkat Android uji A di proxy jaringan
4. Biarkan app di foreground tanpa sentuhan layar dan majukan jam server uji dan jam browser/perangkat bersama 15 menit sampai hitungan mundur lokal habis
5. Amati request di proxy dan layar app
6. Verifikasi Saat hitungan habis app mengirim satu request cek sesi ke server tanpa sentuhan user
7. Verifikasi Dialog "Session Expired" tampil
8. Verifikasi Body Dialog "Session Expired": "Your session has expired due to inactivity."
9. Verifikasi Dialog "Session Expired" hanya memiliki satu tombol [OK]
10. Verifikasi Sesi mobile `Zahra Fitriani` berstatus Expired (dibaca dari tabel `sessions`, Tabel Data Uji Pre-setup #18)
11. Segera di Browser License login ulang sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MGL_PASSWORD` bila sesinya ikut berakhir karena jam dimajukan, lalu buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
12. Verifikasi `Zahra Fitriani` sudah tidak tercantum di daftar Concurrent User (seat dilepas tanpa menunggu sweep)
13. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-347: Koneksi SSE mobile hanya terbuka saat app di foreground

14. Bersihkan state app mobile di perangkat Android uji A (hapus data aplikasi, tutup dialog yang masih tampil), lalu buka aplikasi mobile di perangkat Android uji A, login sebagai `dianmarlina+{runId}-083@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] bila Prompt Enable Biometric muncul, dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
15. Catat titik awal pemantauan koneksi SSE perangkat Android uji A di proxy jaringan
16. Dengan app di foreground amati koneksi SSE
17. Verifikasi Saat foreground ada satu koneksi SSE terbuka
18. Kirim app ke background (tidak dihapus dari recent apps)
19. Majukan jam server uji dan jam browser/perangkat bersama 2 menit (jeda pengamatan 2 menit, seperti TC-AUTH-SES-64) lalu amati koneksi SSE pada proxy jaringan selama rentang itu
20. Verifikasi Setelah app masuk background koneksi SSE ditutup
21. Verifikasi Koneksi SSE tidak dibuka lagi selama app di background
22. Buka kembali app dari recent apps dan amati koneksi SSE
23. Verifikasi Setelah kembali ke foreground koneksi SSE dibuka kembali
24. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-348: Kembali ke foreground dengan sesi masih valid mengecek server satu kali dan memperbarui waktu kedaluwarsa

25. Bersihkan state app mobile di perangkat Android uji A (hapus data aplikasi, tutup dialog yang masih tampil), lalu buka aplikasi mobile di perangkat Android uji A, login sebagai `erwinsusanto+{runId}-083@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] bila Prompt Enable Biometric muncul, dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
26. Catat titik awal pemantauan request perangkat Android uji A di proxy jaringan
27. Kirim app ke background (tidak dihapus dari recent apps)
28. Majukan jam server uji dan jam browser/perangkat bersama 5 menit
29. Buka kembali app dari recent apps dan amati request di proxy serta layar app
30. Verifikasi App mengirim tepat satu request cek sesi ke server sebelum konten terlindungi tampil
31. Verifikasi Sesi valid: halaman terakhir sebelum background (Portal — Product Hub) tampil
32. Verifikasi Tidak ada dialog yang tampil
33. Verifikasi Respons cek sesi pada langkah 29 memuat waktu kedaluwarsa baru (15 menit sejak langkah 29)
34. Tanpa menyentuh layar, majukan jam server uji dan jam browser/perangkat bersama 12 menit sejak langkah 29, lalu amati request di proxy dan layar app
35. Verifikasi Setelah langkah 34 tidak ada request cek sesi, karena hitungan mundur lokal memakai waktu kedaluwarsa dari respons server, bukan sisa hitungan sebelum background (yang habis 10 menit setelah langkah 29)
36. Verifikasi Setelah langkah 34 tidak ada Dialog "Session Expired"
37. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengelompokan: tiga TC perilaku cek sesi mobile terhadap siklus foreground dan background dengan harness yang sama (perangkat Android uji A, proxy pengamat, jam dimajukan bersama). Pergeseran jam hanya menghabiskan jeda (hitungan mundur 15 menit, 2 menit, 5 menit, lalu 12 menit sesudah kembali ke foreground) dan bukan batas TTL yang diuji, sehingga spec ini bukan kelas d (P-2). Proxy dan Browser License hanya pengamat (P-6). Idle dan lifecycle mobile lain (TC-AUTH-SES-63 sampai 66) ada di spec `TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile`.
- Urutan mengikuti TC sumber (344, 347, 348); tidak ada penyimpangan (S-10). Tiap TC memakai user sendiri dan memulihkan jam di akhir bagiannya.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): login mobile di awal tiap TC (Pre-setup #28); membuka card Fixed Asset (langkah 2) untuk membentuk seat yang dilepas; memulai atau mencatat titik awal pemantauan proxy (langkah 3, 15, 26); mengamati proxy dan layar; memajukan dan memulihkan jam; login ulang Browser License (langkah 11).
- Pencatatan log tidak diasersikan di spec ini (S-05).
