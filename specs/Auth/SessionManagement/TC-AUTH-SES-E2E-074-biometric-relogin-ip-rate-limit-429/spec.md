---
id: TC-AUTH-SES-E2E-074-biometric-relogin-ip-rate-limit-429
title: "Re-login Biometric: Melampaui IP Rate Limit Ditolak dengan Toast Too Many Requests"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-175
coverage:
  mobile: automated
---

# Re-login Biometric: Melampaui IP Rate Limit Ditolak dengan Toast Too Many Requests

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #9 dan #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`:
  - TC-AUTH-SES-175: `Nadia Damayanti` (`nadiadamayanti+{runId}-074@qwertysystem.net`)
- Kondisi awal "sudah enroll biometric di perangkat Android uji B; tidak ada sesi platform aktif" (cara menyiapkan: Tabel Data Uji Pre-setup #29) dibuat di dalam TC dengan menyalin langkah enroll TC-AUTH-SES-145 (hapus data aplikasi, login, [Enable], lulus sidik jari, akhiri sesi platform hasil login enroll lewat BE tanpa menghapus token biometric lokal, hapus app dari recent apps), karena token biometric lokal dan status "sudah ditawari" disimpan di perangkat dan hanya dapat dibuat oleh aplikasi.
- Suite berjalan serial (`parallel: false`); state global yang diubah dan pemulihannya di hook `after`: counter IP rate limit relogin biometric yang dipakai bersama oleh alat uji dan perangkat dari IP yang sama (nilai awal nol; di-reset ke nol oleh kemampuan reset counter di hook `before` dan `after`, disediakan tim FE/BE, tanpa menunggu jendela berakhir).
- Hook `after`: pulihkan counter IP rate limit ke nol, hapus data aplikasi pada perangkat Android uji B, akhiri sesi seed, lalu hapus user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: `Nadia Damayanti` pada aplikasi mobile dan request langsung; tanpa akun aktor di langkah.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: rate limit; kelas d: hardware biometrik): driver otomasi Android (aplikasi native); simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus); menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; menutup aplikasi lalu membukanya kembali dan mengamati layar (langkah 13); mengakhiri sesi platform hasil login enroll lewat BE (API yang disediakan BE, tanpa menghapus token biometric lokal; Tabel Data Uji Pre-setup #29), disediakan tim FE/BE, tanpa endpoint; REST client alat uji yang dapat mengirim request langsung ke `POST /v2/iam/auth/biometric/relogin`; alat uji dan perangkat Android uji B keluar dari IP yang sama sehingga memakai kunci IP rate limit yang sama (threshold IP rate limit lingkungan uji diketahui, Precondition c TC-AUTH-SES-175); reset counter IP rate limit ke nol (disediakan tim FE/BE).

## Test Steps

### TC-AUTH-SES-175: Biometric re-login yang melampaui IP rate limit ditolak

1. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `nadiadamayanti+{runId}-074@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Enable] → OS biometric prompt muncul
6. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
7. Akhiri sesi platform hasil login enroll `Nadia Damayanti` di perangkat Android uji B lewat BE (token biometric lokal tidak dihapus)
8. Hapus app dari recent apps
9. Kirim request relogin biometric (`POST /v2/iam/auth/biometric/relogin`) berulang dari IP yang sama sampai batas IP rate limit terlampaui
10. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
11. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt (satu request relogin lagi dari IP yang sama)
12. Verifikasi toast error: "Too many requests. Please try again later."
13. Tutup aplikasi lalu buka kembali di perangkat Android uji B dan amati layar
14. Verifikasi Token lokal tidak dihapus: Screen biometric sign-in masih tampil

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-SES-175 (IP rate limit, kelas c) ada di spec ini; TC-AUTH-SES-170, 171, 176, 257, 258 ada di spec `TC-AUTH-SES-E2E-049-biometric-keamanan-penolakan-server`. Counter IP rate limit adalah state global bersama, sehingga spec ini dijalankan terpisah dan counter di-reset sebelum dan sesudahnya.
- Dependensi (S-04): tidak ada TC dependensi di kolom Dependensi; kondisi "sudah enroll" dibuat dengan menyalin langkah enroll TC-AUTH-SES-145 di awal TC.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): "Hapus data aplikasi" di awal TC (S-09); mengakhiri sesi platform hasil login enroll lewat BE (langkah 7); langkah 10, yaitu membuka aplikasi mobile supaya langkah 11 dapat mengirim request relogin terakhir lewat app; langkah 13, yaitu menutup lalu membuka kembali aplikasi untuk mengamati layar pada Expected b TC-AUTH-SES-175.
- Pembagian TC lintas spec: asersi "tidak ada entri log" (TC-AUTH-SES-175 Expected b) tidak ditulis di spec ini dan berada di spec absence `TC-AUTH-SES-E2E-070-absence-biometric` (kelas g, S-05).
- Temuan untuk QA: (1) TC sumber menulis login dan enroll tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] (label tombol login mobile tidak disebut TC). (2) TC-AUTH-SES-175: Data Uji "Threshold: belum ditetapkan"; langkah 2 TC mengirim request terakhir lewat aplikasi, sama dengan spec (langkah 10 dan 11); kunci IP rate limit mengandaikan alat uji dan perangkat berbagi IP. (3) TC-AUTH-SES-175 tidak menyebut mekanisme reset counter IP rate limit maupun nilai awalnya; spec mengandalkan kemampuan reset counter ke nol (Prerequisites) dan mengasumsikan nilai awal nol. (4) Pre-setup #29 menyebut sesi hasil login enroll diakhiri lewat API yang disediakan BE tanpa nama API; spec menulisnya sebagai kemampuan disediakan tim FE/BE tanpa endpoint.
