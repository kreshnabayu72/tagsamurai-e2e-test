---
id: TC-AC-CS-E2E-044-form-state-submitting-dan-klik-ganda-add-dan-activate-trial
title: "Form: State Submitting dan Klik Ganda Add dan Activate Trial"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-171
  - TC-AC-CS-522
  - TC-AC-CS-621
  - TC-AC-CS-523
coverage:
  web: automated
---

# Form: State Submitting dan Klik Ganda Add dan Activate Trial

## Prerequisites

- Mode: FE+BE (`Spectra.intercept()` parsial untuk menahan respons endpoint Submit di atas backend nyata; endpoint Submit Add dan Activate Trial tidak dinamai TC dan ditentukan tim FE; tahanan dilepas segera setelah asersi state sementara, S-09).
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`, beserta term dan trial yang dibuat spec): Client `Client Tanpa Subscription A+{runId}-044` (TC-AC-CS-171), `B+{runId}-044` (TC-AC-CS-522), `C+{runId}-044` (TC-AC-CS-621), dan `D+{runId}-044` (TC-AC-CS-523) (padanan Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, tanpa term dan tanpa trial).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah term dan trial Client seed serta Reserve atau Capture lewat fixture BE (asersi hitungan pada TC-AC-CS-522 dan TC-AC-CS-523).
- Ceiling Trial 60 hari, 200 assets, 50 users (Pre-setup #25) tidak diubah; nilai awal form 30 hari, 50 assets, 10 users dipakai apa adanya.

## Test Steps

### TC-AC-CS-171: State submitting menonaktifkan tombol dan kontrol form

1. Tahan respons endpoint Submit Add Subscription
2. Klik `[+ Subscription]`
3. Pilih Client `Client Tanpa Subscription A+{runId}-044`, Product `SAMS`, Plan `Growth`, isi Duration `1`, Start Date `19/08/26`
4. Klik `[Submit]`
5. Verifikasi `[Submit]` menampilkan loading dan Disabled
6. Verifikasi kontrol input, `[Clear Field]`, dan `[✕]` Disabled selama permintaan berjalan
7. Lepas tahanan respons endpoint Submit Add Subscription
8. Verifikasi modal tertutup
9. Verifikasi toast sukses "Success, subscription has been added." muncul

### TC-AC-CS-522: Klik ganda Submit pada Add Subscription

10. Tahan respons endpoint Submit Add Subscription
11. Klik `[+ Subscription]`
12. Pilih Client `Client Tanpa Subscription B+{runId}-044`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
13. Klik dua kali cepat pada `[Submit]`
14. Verifikasi `[Submit]` Disabled dan Loading setelah klik pertama
15. Lepas tahanan respons endpoint Submit Add Subscription
16. Tunggu aksi selesai (dialog/modal tertutup)
17. Ketik Search `Client Tanpa Subscription B+{runId}-044`, tekan Enter
18. Verifikasi hanya satu request Submit yang diproses (satu term dan satu Reserve atau Capture terbentuk, dibaca lewat fixture BE)
19. Verifikasi tepat satu baris term tampil untuk Client itu
20. Klik `(←)` pada kotak Search

### TC-AC-CS-621: State submitting Activate Trial menonaktifkan tombol dan kontrol form

21. Tahan respons endpoint Submit Activate Trial
22. Klik `[+ Activate Trial]`
23. Pilih Client `Client Tanpa Subscription C+{runId}-044`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
24. Klik `[Submit]`
25. Verifikasi `[Submit]` menampilkan loading dan Disabled
26. Verifikasi kontrol input, `[Clear Field]`, dan `[✕]` Disabled selama permintaan berjalan
27. Lepas tahanan respons endpoint Submit Activate Trial
28. Verifikasi modal tertutup
29. Verifikasi toast sukses "Success, trial has been activated for Client Tanpa Subscription C+{runId}-044 — Growth, 30 days." muncul

### TC-AC-CS-523: Klik ganda Submit pada Activate Trial

30. Tahan respons endpoint Submit Activate Trial
31. Klik `[+ Activate Trial]`
32. Pilih Client `Client Tanpa Subscription D+{runId}-044`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
33. Klik dua kali cepat pada `[Submit]`
34. Lepas tahanan respons endpoint Submit Activate Trial
35. Verifikasi toast sukses Activate Trial muncul tepat satu kali
36. Tunggu aksi selesai (dialog/modal tertutup)
37. Ketik Search `Client Tanpa Subscription D+{runId}-044`, tekan Enter
38. Verifikasi hanya satu trial terbentuk (tepat satu baris trial tampil)
39. Klik `(←)` pada kotak Search

## Notes

- Penahanan respons pada TC-AC-CS-171 dan 621 hanya untuk mengamati state submitting (bukan kelas b); pada TC-AC-CS-522 dan 523 klik ganda adalah objek uji (kelas c ringan, satu sesi) dengan tahanan sebagai pemicu (P-2). `P-2`: tahanan respons (intercept parsial) hanya berfungsi sebagai pemicu state UI yang diuji dan bukan objek asersi; intercept dilepas segera (langkah 7, 15, 27, 34).
- Langkah penghubung (S-03): pasang dan lepas tahanan respons, Search untuk menemukan baris target (R-16; langkah 17, 37), dan `(←)` pada kotak Search (langkah 20, 39).
- `Tunggu aksi selesai (dialog/modal tertutup)` sesudah tahanan dilepas pada TC-AC-CS-522 (langkah 16) dan sesudah toast pada TC-AC-CS-523 (langkah 36), sebelum Search dan pembacaan BE (8b.8).
- Asersi state sementara (langkah 5 dan 6, 14, 25 dan 26) ditulis sebelum tahanan dilepas (butir 8b.5); asersi hasil (langkah 8 dan 9, 28 dan 29, 35) sesudah tahanan dilepas (butir 8b.11).
- Ukuran: 39 langkah, di atas 35 langkah. Alasan: empat blok satu kelas (state submitting dan klik ganda) dengan Client seed terpisah per blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-CS-522 Expected b menyebut "satu Reserve atau Capture" padahal aktor Principal tidak punya Wallet (TC-AC-CS-145); spec hanya mengasersi satu term.
  - TC-AC-CS-522 dan 523 Langkah 1 tidak menyebut endpoint yang ditunda dan Langkah 3 menyebut "tombol konfirmasi" tanpa nama; ditulis `[Submit]`.
  - TC-AC-CS-523 Expected b ("Tidak ada pesan duplikat") diasersi sebagai tepat satu toast sukses; teks toast tidak disebut di TC-AC-CS-523 (TC-AC-CS-621 menyebutnya).
