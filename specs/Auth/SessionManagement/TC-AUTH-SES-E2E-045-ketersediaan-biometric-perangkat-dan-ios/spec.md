---
id: TC-AUTH-SES-E2E-045-ketersediaan-biometric-perangkat-dan-ios
title: "Ketersediaan Biometric Perangkat Android (Prompt dan Toggle) serta Enroll Ulang"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-147
  - TC-AUTH-SES-148
  - TC-AUTH-SES-149
  - TC-AUTH-SES-337
coverage:
  mobile: automated
---

# Ketersediaan Biometric Perangkat Android (Prompt dan Toggle) serta Enroll Ulang

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di tiga perangkat uji (Tabel Data Uji Pre-setup #10): Android uji C (tanpa hardware biometric, TC-AUTH-SES-147 dan 337), Android uji D (hardware biometric, tanpa sidik jari atau wajah terdaftar di OS, TC-AUTH-SES-148 dan 337), dan Android uji B (hardware biometric dan sidik jari terdaftar, TC-AUTH-SES-149). Tanpa sesi aktif di aplikasi pada semua perangkat saat spec dimulai.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #9 dan #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-147: `Tari Kusuma` (`tarikusuma+{runId}-045@qwertysystem.net`), perangkat Android uji C
  - TC-AUTH-SES-148: `Budi Ramadhan` (`budiramadhan+{runId}-045@qwertysystem.net`), perangkat Android uji D
  - TC-AUTH-SES-337: `Nanda Wirawan` (`nandawirawan+{runId}-045@qwertysystem.net`), perangkat Android uji C lalu D
  - TC-AUTH-SES-149: `Siti Wulandari` (`sitiwulandari+{runId}-045@qwertysystem.net`), perangkat Android uji B
- Token biometric lokal hanya dapat dibuat oleh aplikasi di perangkat, sehingga enroll pertama yang menjadi kondisi awal TC-AUTH-SES-149 dijalankan sebagai langkah (alur enroll TC-AUTH-SES-145; cara menyiapkan token biometric lokal mengikuti Tabel Data Uji Pre-setup #29) dengan data aplikasi yang bersih.
- Suite berjalan serial (`parallel: false`) karena perangkat Android uji B, C, dan D dipakai bersama; state yang diubah pada perangkat itu (data aplikasi, status "sudah ditawari", token biometric lokal, kredensial biometric user uji) dibersihkan di hook `after`.
- Hook `after`: hapus data aplikasi pada perangkat Android uji B, C, dan D, akhiri semua sesi seed, lalu hapus keempat user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor hanya di hook.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik): driver otomasi Android (aplikasi native) pada perangkat B, C, dan D; simulasi sensor sidik jari pada OS biometric prompt Android (verifikasi lulus); menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; membuka Settings > Security dan membaca ada atau tidaknya toggle "Biometric sign-in" (TC-AUTH-SES-337); REST client alat uji yang dapat mengirim request langsung ke `POST /v2/iam/auth/biometric/enroll` (header `X-Session-ID` berisi ID sesi mobile aktif milik `Siti Wulandari`, body `deviceId` perangkat Android uji B) untuk TC-AUTH-SES-149 dan membaca status kredensial biometric user; penolakan token biometric lama (langkah 42) dari sisi backend, disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-147: Prompt Enable Biometric tidak muncul pada perangkat tanpa hardware biometric

1. Buka aplikasi mobile di perangkat Android uji C → halaman Login tampil
2. Ketik `tarikusuma+{runId}-045@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login]
5. Verifikasi App masuk Portal — Product Hub tanpa Prompt Enable Biometric
6. Hapus app dari recent apps
7. Buka kembali app → halaman Login tampil
8. Ketik `tarikusuma+{runId}-045@qwertysystem.net` pada field Email
9. Ketik `Spectra.env.SES_PASSWORD` pada field Password
10. Klik [Login]
11. Verifikasi Prompt Enable Biometric tidak muncul pada login berikutnya

### TC-AUTH-SES-148: Prompt Enable Biometric tidak muncul pada perangkat yang belum punya biometric terdaftar di OS

12. Buka aplikasi mobile di perangkat Android uji D → halaman Login tampil
13. Ketik `budiramadhan+{runId}-045@qwertysystem.net` pada field Email
14. Ketik `Spectra.env.SES_PASSWORD` pada field Password
15. Klik [Login]
16. Verifikasi App masuk Portal — Product Hub tanpa Prompt Enable Biometric

### TC-AUTH-SES-337: Toggle Biometric sign-in tidak tampil di perangkat tanpa hardware biometric atau tanpa enrollment

17. Hapus data aplikasi di perangkat Android uji C lalu buka aplikasi mobile → halaman Login tampil
18. Ketik `nandawirawan+{runId}-045@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.SES_PASSWORD` pada field Password
20. Klik [Login] → app masuk Portal — Product Hub
21. Buka Settings > Security
22. Verifikasi Di perangkat Android uji C toggle "Biometric sign-in" tidak tampil
23. Buka menu Profile lalu pilih Log Out → form Login tampil
24. Hapus data aplikasi di perangkat Android uji D lalu buka aplikasi mobile → halaman Login tampil
25. Ketik `nandawirawan+{runId}-045@qwertysystem.net` pada field Email
26. Ketik `Spectra.env.SES_PASSWORD` pada field Password
27. Klik [Login] → app masuk Portal — Product Hub
28. Buka Settings > Security
29. Verifikasi Di perangkat Android uji D toggle "Biometric sign-in" tidak tampil

### TC-AUTH-SES-149: Enroll ulang tanpa disable membuat token baru dan mencabut token lama

30. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
31. Ketik `sitiwulandari+{runId}-045@qwertysystem.net` pada field Email
32. Ketik `Spectra.env.SES_PASSWORD` pada field Password
33. Klik [Login] → Prompt Enable Biometric muncul
34. Ketuk [Enable] → OS biometric prompt muncul
35. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub dengan sesi platform mobile aktif
36. Kirim request enroll biometric kedua (`POST /v2/iam/auth/biometric/enroll`) dari perangkat yang sama dengan sesi valid `Siti Wulandari` tanpa menonaktifkan kredensial pertama
37. Hapus app dari recent apps
38. Buka kembali app
39. Lulus verifikasi biometric pada OS biometric prompt
40. Verifikasi Re-login berhasil memakai token baru
41. Verifikasi Hanya satu kredensial biometric Active milik `Siti Wulandari` pada perangkat Android uji B
42. Verifikasi Token lama sudah ditolak

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Ditahan: TC-AUTH-SES-260 dan 261 (iOS) bertanda `[Ditahan PRD §12 #4: iOS di luar scope rilis pertama]` di TC sumber. Mengikuti pola "Ditahan" (`docs/e2e-conventions-prd.md` bagian 2 dan 8), keduanya tidak ditulis ke spec ini dan dicantumkan di tabel `## Ditahan` pada `docs/coverage/AuthSessionManagement.md`; keduanya kembali ditulis bila Open Item PRD §12 #4 ditutup. Id spec ini tetap memuat "ios" agar rujukan dari dokumen lain tidak putus; judulnya sudah disesuaikan.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-147, 148, 337, 149 (urutan TC sumber 147, 148, 149, 337). TC yang memakai perangkat tanpa biometric yang siap pakai (C dan D) didahulukan, dan TC-AUTH-SES-149 yang menimpa kredensial lewat request langsung ditaruh paling akhir.
- Dependensi (S-04): langkah 30–35 pada TC-AUTH-SES-149 menyalin alur enroll TC-AUTH-SES-145 untuk membuat enroll pertama.
- Pengecualian P-2 (pemicu bukan objek uji): request enroll kedua yang dikirim langsung ke `POST /v2/iam/auth/biometric/enroll` lewat alat uji (langkah 36, kelas harness a) hanya memicu state "enroll ulang tanpa disable"; yang diasersi adalah hasilnya pada aplikasi dan backend (langkah 40 sampai 42), bukan perilaku endpoint enroll itu sendiri, sehingga spec ini tetap berkelas d (hardware biometrik).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): hapus data aplikasi di awal TC-AUTH-SES-337 (langkah 17 dan 24; perangkat C dan D masih memegang sesi user TC-AUTH-SES-147 dan 148) dan TC-AUTH-SES-149 (status "sudah ditawari" dan token biometric lokal disimpan per perangkat); membuka Settings > Security (langkah 21 dan 28); Log Out di perangkat C (langkah 23); langkah 6–11 pada TC-AUTH-SES-147 (menghapus app lalu login lagi) ditambahkan supaya Expected b "Prompt tidak pernah muncul pada login berikutnya" punya `Verifikasi` (S-14).
- Pencatatan log tidak diasersikan di spec ini (S-05).
- Jumlah langkah (42) melewati batas sekitar 35 langkah karena empat TC, masing-masing dengan user dan perangkat sendiri, menyalin prefix login mobile identik dan alur enroll per TC (S-04); tiap TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal.
- Temuan untuk QA: (1) TC sumber menulis "login ... dan password yang benar" (TC-AUTH-SES-337: tanpa password sama sekali) tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password `Spectra.env.SES_PASSWORD`, klik [Login] (label tombol login mobile tidak disebut TC). (2) TC-AUTH-SES-149: Expected a menyebut re-login berhasil "memakai token baru", tetapi langkah 36 (langkah 1 TC-AUTH-SES-149) mengirim enroll lewat alat uji (token plaintext baru dikembalikan ke alat uji, bukan disimpan ke secure storage perangkat), sehingga app tetap memakai token lama; selain itu TC tidak menyebut cara alat uji memperoleh ID sesi mobile aktif (header `X-Session-ID`) dan cara membaca "hanya satu kredensial Active" serta "token lama sudah ditolak". Spec mengikuti TC. (3) TC-AUTH-SES-337 langkah 2 menyebut "Log Out" tanpa letak menunya; spec memakai menu Profile lalu Log Out seperti TC-AUTH-SES-331 dan 332. TC-AUTH-SES-337 juga tidak menyebut bahwa perangkat C dan D sudah dipakai login user lain di TC-AUTH-SES-147 dan 148; spec menghapus data aplikasi sebelum login `Nanda Wirawan` di tiap perangkat.
