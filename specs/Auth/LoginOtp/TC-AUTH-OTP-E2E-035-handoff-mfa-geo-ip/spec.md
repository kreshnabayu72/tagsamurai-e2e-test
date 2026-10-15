---
id: TC-AUTH-OTP-E2E-035-handoff-mfa-geo-ip
title: "Handoff ke MFA berdasarkan Jarak dan Negara Login"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-190
  - TC-AUTH-OTP-191
coverage:
  web: automated
---

# Handoff ke MFA berdasarkan Jarak dan Negara Login

## Prerequisites

- Mode: FE+BE (backend nyata; sesi dan email alert dibuktikan lewat perilaku UI dan mail-catcher).
- Environment variable: `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-035`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Semuanya berprofil seperti BASE (Activated, Active ON; device dikenali; bukan login pertama dan tidak idle; Agreement tidak terpicu; Authenticator sudah terdaftar) dengan riwayat login terakhir yang diatur lewat seed data lokasi:
  - TC-AUTH-OTP-190: `Sekar Widodo` (`sekarwidodo+{runId}-035@qwertysystem.net`); login terakhir dari lokasi A dan koneksi penguji dari lokasi B yang berjarak lebih dari 100 km di negara yang sama
  - TC-AUTH-OTP-191: `Gunawan Lubis` (`gunawanlubis+{runId}-035@qwertysystem.net`); login terakhir dari negara A dan koneksi penguji dari negara B yang berjarak 100 km atau kurang dari lokasi login terakhir (bukan pasangan negara bolak-balik yang tersimpan)
- Kemampuan teknis: koneksi penguji dengan lokasi Geo-IP yang dapat dikendalikan per TC (lokasi B ditentukan per TC: TC-AUTH-OTP-190 lokasi B berjarak lebih dari 100 km dari lokasi login terakhir di negara yang sama; TC-AUTH-OTP-191 negara B berbeda dengan jarak 100 km atau kurang); seed data lokasi login terakhir per user; mail-catcher lingkungan uji untuk membaca kode OTP dan email alert login tak biasa; reCAPTCHA mode uji.
- State global: lokasi koneksi penguji diubah pada langkah 1 dan 12. Suite berjalan serial (`parallel: false`) karena lokasi koneksi penguji berlaku untuk seluruh koneksi dari environment uji. Hook `after` mengembalikan lokasi koneksi penguji ke lokasi semula dan tetap jalan walau spec gagal di tengah.

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

12. Atur koneksi penguji ke negara B (berjarak 100 km atau kurang dari lokasi login terakhir `Gunawan Lubis`, negara berbeda dari negara login terakhir)
13. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
14. Ketik `gunawanlubis+{runId}-035@qwertysystem.net` pada field Email
15. Centang widget reCAPTCHA "I'm not a robot"
16. Klik button [Request OTP]
17. Ketik 6 digit kode OTP dari email pada kotak digit
18. Verifikasi layar Confirm to Continue tidak tampil
19. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code` tanpa halaman pilihan metode
20. Verifikasi email alert login tak biasa diterima di mail-catcher `gunawanlubis+{runId}-035@qwertysystem.net` (isi email dimiliki modul mfa)
21. Buka Portal — Product Hub langsung di tab lain
22. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-AUTH-OTP-192 (Geo-IP service dimatikan, kelas b) dipindah ke spec `TC-AUTH-OTP-E2E-050-geo-ip-service-tidak-tersedia` supaya spec ini tidak memuat kegagalan penyedia yang dipaksa sebagai objek uji.
- Langkah 1 dan 12 (mengatur lokasi koneksi penguji) adalah langkah penghubung/kondisi dari Pre-condition TC sumber (S-03, S-11); pemulihan lokasi koneksi dilakukan di hook `after`.
- Temuan untuk QA:
  - TC-AUTH-OTP-190 dan 191 (`Manual Only` di TC sumber) membutuhkan koneksi penguji dengan lokasi Geo-IP terkendali dan seed lokasi login terakhir; tidak disebut bagaimana lokasi dikendalikan (proxy, mock Geo-IP, atau fixture BE). Kebutuhan ini dicatat di Prerequisites sebagai kemampuan teknis untuk tim FE.
  - TC-AUTH-OTP-190 dan 191 hanya menyebut profil seperti BASE, sedangkan Expected TC-190 dan TC-191 menuju halaman MFA `Enter authenticator code` dan MFA pada BASE tidak aktif. Spec mengasumsikan Authenticator sudah terdaftar pada kedua user (Prerequisites) agar halaman itu dapat tampil; asumsi ini tidak ada di TC. Mohon QA menambah precondition Authenticator terdaftar.
  - TC-AUTH-OTP-191 Pre-condition menyebut "bukan pasangan negara bolak-balik yang tersimpan" tanpa menjelaskan aturan pasangan negara tersimpan; spec mengikuti sumber.
  - TC-AUTH-OTP-190 dan TC-AUTH-OTP-191 Post Condition (Success belum ditulis) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi (S-01). Mohon QA menambah langkah observasinya di TC.
