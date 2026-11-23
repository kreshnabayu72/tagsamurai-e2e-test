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

- Mode: FE+BE (backend nyata; sesi dan email alert dibuktikan lewat perilaku UI dan mail-catcher, entri Success TC-AUTH-OTP-199 lewat Activity Log Session).
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1); password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`; dipakai hanya untuk membaca `Global Settings > Activity Log > Session` pada TC-AUTH-OTP-199.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-035`, `+{runId}-035a`, dan `+{runId}-035b` (TC-AUTH-OTP-191 dan 199 memakai nama `Gunawan Lubis`, jadi email dibedakan dengan huruf), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Semuanya berprofil seperti BASE (Activated, Active ON; device dikenali; bukan login pertama dan tidak idle; Agreement tidak terpicu; Authenticator sudah terdaftar) dengan riwayat login terakhir yang diatur lewat seed data lokasi:
  - TC-AUTH-OTP-190: `Sekar Widodo` (`sekarwidodo+{runId}-035@qwertysystem.net`); login terakhir dari lokasi A dan koneksi penguji dari lokasi B yang berjarak lebih dari 100 km di negara yang sama
  - TC-AUTH-OTP-191: `Gunawan Lubis` (`gunawanlubis+{runId}-035a@qwertysystem.net`); login terakhir dari negara A dan koneksi penguji dari negara B yang berjarak 100 km atau kurang dari lokasi login terakhir (bukan pasangan negara bolak-balik yang tersimpan)
  - TC-AUTH-OTP-199: `Gunawan Lubis` (`gunawanlubis+{runId}-035b@qwertysystem.net`); login terakhir dari negara A; pasangan negara A–B sudah tersimpan sebagai pasangan tepercaya (owner `mfa`, belum lewat masa 180 hari; seed data); koneksi penguji dari negara B yang berjarak 100 km atau kurang dari lokasi login terakhir
- Kemampuan teknis: koneksi penguji dengan lokasi Geo-IP yang dapat dikendalikan per TC (lokasi B ditentukan per TC: TC-AUTH-OTP-190 lokasi B berjarak lebih dari 100 km dari lokasi login terakhir di negara yang sama; TC-AUTH-OTP-191 dan 199 negara B berbeda dengan jarak 100 km atau kurang); seed data lokasi login terakhir per user; seed pasangan negara tepercaya (owner `mfa`) untuk TC-AUTH-OTP-199; dua konteks browser (jendela privat publik dan browser admin); mail-catcher lingkungan uji untuk membaca kode OTP dan email alert login tak biasa; reCAPTCHA mode uji.
- Baseline log: hook `before` mencatat jumlah baris `Gunawan Lubis` di `Global Settings > Activity Log > Session` sesudah semua user di-seed; "tepat satu baris baru" pada TC-AUTH-OTP-199 dihitung terhadap baseline itu (S-12).
- State global: lokasi koneksi penguji diubah pada langkah 1, 12, dan 23. Suite berjalan serial (`parallel: false`) karena lokasi koneksi penguji berlaku untuk seluruh koneksi dari environment uji. Hook `after` mengembalikan lokasi koneksi penguji ke lokasi semula dan tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-190: Verify OTP dari lokasi lebih dari 100 km dari login sebelumnya (negara sama) mengalihkan ke halaman MFA

1. Atur koneksi penguji ke lokasi B (berjarak lebih dari 100 km dari lokasi login terakhir `Sekar Widodo`, negara sama)
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

### TC-AUTH-OTP-191: Verify OTP dari negara berbeda walau jarak 100 km atau kurang mengalihkan ke halaman MFA

12. Atur koneksi penguji ke negara B (berjarak 100 km atau kurang dari lokasi login terakhir `gunawanlubis+{runId}-035a@qwertysystem.net`, negara berbeda dari negara login terakhir)
13. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
14. Ketik `gunawanlubis+{runId}-035a@qwertysystem.net` pada field Email
15. Centang widget reCAPTCHA "I'm not a robot"
16. Klik button [Request OTP]
17. Ketik 6 digit kode OTP dari email pada kotak digit
18. Verifikasi layar Confirm to Continue tidak tampil
19. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code` tanpa halaman pilihan metode
20. Verifikasi email alert login tak biasa diterima di mail-catcher `gunawanlubis+{runId}-035a@qwertysystem.net` (isi email dimiliki modul mfa)
21. Buka Portal — Product Hub langsung di tab lain
22. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login

### TC-AUTH-OTP-199: Pasangan negara yang sudah tersimpan sebagai tepercaya tidak memicu trigger negara

23. Atur koneksi penguji ke negara B (berjarak 100 km atau kurang dari lokasi login terakhir `gunawanlubis+{runId}-035b@qwertysystem.net`; pasangan negara A–B sudah tersimpan sebagai tepercaya)
24. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
25. Ketik `gunawanlubis+{runId}-035b@qwertysystem.net` pada field Email
26. Centang widget reCAPTCHA "I'm not a robot"
27. Klik button [Request OTP]
28. Ketik 6 digit kode OTP dari email pada kotak digit
29. Verifikasi layar Confirm to Continue tidak tampil
30. Verifikasi browser langsung menuju Portal — Product Hub tanpa halaman MFA
31. Verifikasi tidak ada email alert login tak biasa di mail-catcher `gunawanlubis+{runId}-035b@qwertysystem.net`
32. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` untuk `Gunawan Lubis`
33. Verifikasi tepat satu baris baru Activity `Login`, Status `Success`, Note `Login with OTP` dibanding baseline hook `before`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-AUTH-OTP-192 (Geo-IP service dimatikan, kelas b) dipindah ke spec `TC-AUTH-OTP-E2E-050-geo-ip-service-tidak-tersedia` supaya spec ini tidak memuat kegagalan penyedia yang dipaksa sebagai objek uji.
- Langkah 1, 12, dan 23 (mengatur lokasi koneksi penguji) adalah langkah penghubung/kondisi dari Pre-condition TC sumber (S-03, S-11); pemulihan lokasi koneksi dilakukan di hook `after`. Langkah 32 (ganti konteks ke browser admin) adalah langkah penghubung tanpa `Verifikasi`.
- Akun aktor Total Control (Global Settings) hanya dipakai pada langkah 32 dan 33 lewat Step ganti konteks eksplisit; blok TC-AUTH-OTP-199 tetap bermakna walau blok TC-AUTH-OTP-190 dan 191 gagal (konvensi bagian 3, beda akun kasus b). Expected d TC-AUTH-OTP-199 (satu entri Success) adalah Expected eksplisit TC, sehingga diasersi di spec ini dengan baseline (S-12).
- TC-AUTH-OTP-199 ditaruh terakhir karena satu-satunya TC yang menyelesaikan login sampai Portal dan menambah baris log (S-10).
- Temuan untuk QA:
  - TC-AUTH-OTP-190, 191, dan 199 (`Manual Only` di TC sumber) membutuhkan koneksi penguji dengan lokasi Geo-IP terkendali dan seed lokasi login terakhir; tidak disebut bagaimana lokasi dikendalikan (proxy, mock Geo-IP, atau fixture BE). Kebutuhan ini dicatat di Prerequisites sebagai kemampuan teknis untuk tim FE.
  - TC-AUTH-OTP-190 dan 191 hanya menyebut profil seperti BASE, sedangkan Expected TC-190 dan TC-191 menuju halaman MFA `Enter authenticator code` dan MFA pada BASE tidak aktif. Spec mengasumsikan Authenticator sudah terdaftar pada kedua user (Prerequisites) agar halaman itu dapat tampil; asumsi ini tidak ada di TC. Mohon QA menambah precondition Authenticator terdaftar.
  - TC-AUTH-OTP-191 Pre-condition menyebut "bukan pasangan negara bolak-balik yang tersimpan" tanpa menjelaskan aturan pasangan negara tersimpan; spec mengikuti sumber.
  - TC-AUTH-OTP-190 dan TC-AUTH-OTP-191 Post Condition (Success belum ditulis) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi (S-01). Mohon QA menambah langkah observasinya di TC.
  - TC-AUTH-OTP-199 hanya menyebut profil seperti BASE; spec mengasumsikan Authenticator sudah terdaftar (sama dengan TC-AUTH-OTP-190 dan 191) sehingga Portal tanpa halaman MFA berarti trigger negara tidak terpicu, bukan MFA tidak aktif. Mohon QA menambah precondition Authenticator terdaftar.
  - TC-AUTH-OTP-199 tidak menyebut cara pasangan negara tepercaya disiapkan (owner `mfa`); spec memakai seed data di hook `before`.
  - TC-AUTH-OTP-191 dan 199 memakai nama tampilan yang sama (`Gunawan Lubis`) sehingga baris Activity Log Session kedua user tidak dapat dibedakan lewat kolom User; spec memakai baseline jumlah baris sesudah seeding (S-12). Mohon QA memberi nama berbeda pada salah satu user.
  - TC-AUTH-OTP-199 Post Condition a (satu sesi web aktif) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi (S-01).
