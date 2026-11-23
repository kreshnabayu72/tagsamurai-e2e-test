---
id: TC-AUTH-OTP-E2E-035-handoff-mfa-geo-ip
title: "Handoff ke MFA berdasarkan Jarak dan Negara Login serta Pasangan Negara Tepercaya"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-190
  - TC-AUTH-OTP-191
  - TC-AUTH-OTP-199
coverage:
  web: automated
---

# Handoff ke MFA berdasarkan Jarak dan Negara Login serta Pasangan Negara Tepercaya

## Prerequisites

- Mode: FE+BE (backend nyata; handoff MFA dan email alert dibuktikan lewat perilaku UI dan mail-catcher, entri Success lewat Activity Log Session, sesi web TC-AUTH-OTP-199 lewat pembacaan tabel `sessions`).
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1); password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`; dipakai hanya untuk membaca `Global Settings > Activity Log > Session` pada ketiga TC.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-035`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Semuanya berprofil seperti BASE (Activated, Active ON; device dikenali; bukan login pertama dan tidak idle; Agreement tidak terpicu; Authenticator sudah terdaftar) dengan lokasi dan negara login terakhir di-seed lewat fixture BE (Tabel Data Uji Pre-setup #18):
  - TC-AUTH-OTP-190: `Sekar Widodo` (`sekarwidodo+{runId}-035@qwertysystem.net`); login terakhir dari lokasi A dan koneksi penguji dari lokasi B yang berjarak lebih dari 100 km di negara yang sama
  - TC-AUTH-OTP-191: `Gunawan Lubis` (`gunawanlubis+{runId}-035@qwertysystem.net`); login terakhir dari negara A dan koneksi penguji dari negara B yang berjarak 100 km atau kurang dari lokasi login terakhir (pasangan negara A–B tidak punya baris `known_country_pairs` dengan `is_trusted = true`; pasangan menjadi tepercaya setelah muncul 3 kali atau lebih dalam window 90 hari, `auth/mfa/PRD/mfa.md` F-AUTHMFA-08)
  - TC-AUTH-OTP-199: `Hendra Siregar` (`hendrasiregar+{runId}-035@qwertysystem.net`, Tabel Data Uji Dinamis #180); login terakhir dari negara A; pasangan negara A–B sudah tersimpan sebagai pasangan tepercaya (owner `mfa`, belum lewat masa 180 hari; di-seed lewat fixture BE: baris `known_country_pairs` A–B dengan `is_trusted = true` dan terakhir terlihat kurang dari 180 hari lalu); koneksi penguji dari negara B yang berjarak 100 km atau kurang dari lokasi login terakhir
- Kemampuan teknis: kendali lokasi login (Tabel Data Uji Pre-setup #18): header edge `X-Country-Code` disuntikkan proxy uji per request (negara) dan IP penguji dipetakan ke koordinat lewat mock Geo-IP lingkungan uji (jarak); lokasi B ditentukan per TC (TC-AUTH-OTP-190 lokasi B berjarak lebih dari 100 km dari lokasi login terakhir di negara yang sama; TC-AUTH-OTP-191 dan 199 negara B berbeda dengan jarak 100 km atau kurang); seed lokasi login terakhir per user dan baris `known_country_pairs` lewat fixture BE; pembacaan read-only tabel `sessions` per `user_id` (kolom `status`, `platform`, `created_at`) di DB lingkungan uji (Tabel Data Uji Pre-setup #20) untuk TC-AUTH-OTP-199; dua konteks browser (jendela privat publik dan browser admin); mail-catcher lingkungan uji untuk membaca kode OTP dan email alert login tak biasa; reCAPTCHA mode uji.
- Baseline log: hook `before` mencatat jumlah entri Success `Login with OTP` per user uji (`Sekar Widodo`, `Gunawan Lubis`, `Hendra Siregar`) di `Global Settings > Activity Log > Session` sesudah semua user di-seed; asersi "belum ada entri" pada TC-AUTH-OTP-190 dan 191 serta "tepat satu baris baru" pada TC-AUTH-OTP-199 dihitung terhadap baseline itu (S-12).
- State global: lokasi koneksi penguji diubah pada langkah 1, 14, dan 27. Suite berjalan serial (`parallel: false`) karena lokasi koneksi penguji berlaku untuk seluruh koneksi dari environment uji. Hook `after` mengembalikan lokasi koneksi penguji ke lokasi semula dan tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-190: Verify OTP dari lokasi lebih dari 100 km dari login sebelumnya (negara sama) mengalihkan ke halaman MFA

1. Atur koneksi penguji ke lokasi B (berjarak lebih dari 100 km dari lokasi login terakhir `Sekar Widodo`, negara sama; Tabel Data Uji Pre-setup #18)
2. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
3. Ketik `sekarwidodo+{runId}-035@qwertysystem.net` pada field Email
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Request OTP]
6. Ketik 6 digit kode OTP dari email pada kotak digit
7. Verifikasi layar Confirm to Continue tidak tampil
8. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code` tanpa halaman pilihan metode
9. Verifikasi email alert login tak biasa diterima di mail-catcher `sekarwidodo+{runId}-035@qwertysystem.net` (isi email dimiliki modul mfa)
10. Buka Portal — Product Hub langsung di tab lain
11. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login
12. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan cari entri `Sekar Widodo`
13. Verifikasi belum ada entri Success `Login with OTP` baru untuk `Sekar Widodo` dibanding baseline hook `before` (entri ditulis saat login final di alur MFA)

### TC-AUTH-OTP-191: Verify OTP dari negara berbeda walau jarak 100 km atau kurang mengalihkan ke halaman MFA

14. Atur koneksi penguji ke negara B (berjarak 100 km atau kurang dari lokasi login terakhir `Gunawan Lubis`, negara berbeda dari negara login terakhir; Tabel Data Uji Pre-setup #18)
15. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
16. Ketik `gunawanlubis+{runId}-035@qwertysystem.net` pada field Email
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Request OTP]
19. Ketik 6 digit kode OTP dari email pada kotak digit
20. Verifikasi layar Confirm to Continue tidak tampil
21. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code` tanpa halaman pilihan metode
22. Verifikasi email alert login tak biasa diterima di mail-catcher `gunawanlubis+{runId}-035@qwertysystem.net` (isi email dimiliki modul mfa)
23. Buka Portal — Product Hub langsung di tab lain
24. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login
25. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session` dan cari entri `Gunawan Lubis`
26. Verifikasi belum ada entri Success `Login with OTP` baru untuk `Gunawan Lubis` dibanding baseline hook `before` (entri ditulis saat login final di alur MFA)

### TC-AUTH-OTP-199: Pasangan negara yang sudah tersimpan sebagai tepercaya tidak memicu trigger negara

27. Atur koneksi penguji ke negara B (berjarak 100 km atau kurang dari lokasi login terakhir `Hendra Siregar`; pasangan negara A–B sudah tersimpan sebagai tepercaya; Tabel Data Uji Pre-setup #18)
28. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
29. Ketik `hendrasiregar+{runId}-035@qwertysystem.net` pada field Email
30. Centang widget reCAPTCHA "I'm not a robot"
31. Klik button [Request OTP]
32. Ketik 6 digit kode OTP dari email pada kotak digit
33. Verifikasi layar Confirm to Continue tidak tampil
34. Verifikasi browser langsung menuju Portal — Product Hub tanpa halaman MFA
35. Verifikasi tidak ada email alert login tak biasa di mail-catcher `hendrasiregar+{runId}-035@qwertysystem.net`
36. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session` dan cari entri `Hendra Siregar`
37. Verifikasi tepat satu baris baru Activity `Login`, Status `Success`, Note `Login with OTP` untuk `Hendra Siregar` dibanding baseline hook `before`
38. Baca sesi `Hendra Siregar` di tabel `sessions` (Tabel Data Uji Pre-setup #20)
39. Verifikasi satu sesi web aktif untuk `Hendra Siregar` (`status` aktif, `platform` web, `created_at` sesudah langkah 32)

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-AUTH-OTP-192 (Geo-IP service dimatikan, kelas b) dipindah ke spec `TC-AUTH-OTP-E2E-050-geo-ip-service-tidak-tersedia` supaya spec ini tidak memuat kegagalan penyedia yang dipaksa sebagai objek uji.
- Langkah 1, 14, dan 27 (mengatur lokasi koneksi penguji) adalah langkah penghubung/kondisi dari Pre-condition TC sumber (S-03, S-11); pemulihan lokasi koneksi dilakukan di hook `after`. Langkah 12, 25, dan 36 (ganti konteks ke browser admin) adalah langkah 6 TC sumber dan langkah penghubung tanpa `Verifikasi`. Langkah 38 adalah langkah 6 TC-AUTH-OTP-199.
- Akun aktor Total Control (Global Settings) hanya dipakai pada langkah 12–13, 25–26, dan 36–37 lewat Step ganti konteks eksplisit; tiap blok membuka jendela privat sendiri dengan user sendiri sehingga blok TC-AUTH-OTP-199 tetap bermakna walau blok TC-AUTH-OTP-190 dan 191 gagal (konvensi bagian 3, beda akun kasus b). Expected e TC-AUTH-OTP-190 dan 191 ("belum ada entri Success") adalah asersi jumlah dengan baseline, bukan asersi absence kelas g (prinsip 13g), sehingga diasersi di spec ini (S-12).
- Spec ini 39 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena ketiga blok satu topik dan satu harness (kendali lokasi Geo-IP Tabel Data Uji Pre-setup #18), tiap blok memakai user dan jendela privat sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tambahan langkah berasal dari langkah 6 TC sumber (pembacaan Activity Log dan tabel `sessions`).
- TC-AUTH-OTP-199 ditaruh terakhir karena satu-satunya TC yang menyelesaikan login sampai Portal dan menambah baris log serta sesi (S-10).
