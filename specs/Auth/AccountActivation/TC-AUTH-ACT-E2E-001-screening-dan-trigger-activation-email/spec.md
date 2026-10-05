---
id: TC-AUTH-ACT-E2E-001-screening-dan-trigger-activation-email
title: Screening trigger Activation Email, template email, snapshot nama, token hash, dan expiry 24 jam
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-1
  - TC-AUTH-ACT-2
  - TC-AUTH-ACT-3
  - TC-AUTH-ACT-4
  - TC-AUTH-ACT-5
  - TC-AUTH-ACT-6
  - TC-AUTH-ACT-7
  - TC-AUTH-ACT-8
  - TC-AUTH-ACT-9
  - TC-AUTH-ACT-93
coverage:
  web: automated
---

# Screening trigger Activation Email, template email, snapshot nama, token hash, dan expiry 24 jam

## Prerequisites

- Administrator login ke Global Settings > User atau Admin Console dengan akses pembuatan user.
- Environment run adalah environment terisolasi khusus otomasi. Hook `before`/`after` menyiapkan dan membersihkan data user yang dibuat selama spec ini.
- `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD` tersedia untuk login admin (tidak ditulis eksplisit di spec).
- Fixture `Fixture.authAccountActivation.data.emailPrefix` atau mekanisme pembuatan email unik per run (`<prefix>+<timestamp>+<rand>@example.com`) digunakan untuk mencegah duplikasi data.
- Akses ke mailbox uji atau inspeksi email (jika tersedia) untuk memverifikasi isi Activation Email sesuai template.
- Akses DB/read-only untuk verifikasi `activation_token` (hash SHA-256 64 hex), raw token di link email (43 karakter Base64URL), `expires_at = created_at + 24h`, `status=active`, `consumed_at=null`, dan snapshot `full_name`.
- Tidak ada sesi lain yang memakai user target bersamaan dengan spec ini.

## Test Steps

### A. Trigger via Global Settings > User

1. Login sebagai admin dan buka halaman Global Settings > User.
2. Buat user baru melalui form Create User dengan data unik (email, first_name, last_name) yang dibuat oleh hook.
3. Verifikasi Activation Email terkirim ke alamat email user yang baru dibuat.
4. Verifikasi subject email adalah `"Activate your TAG Samurai account"`.
5. Verifikasi isi email memuat greeting `"Hi [Full Name],"` (menggunakan Full Name snapshot saat pembuatan user).
6. Verifikasi body email memuat kalimat instruksi aktivasi sesuai template: `"An account has been created for you on TAG Samurai. Click the button below to set your password and activate your account."`.
7. Verifikasi tombol `[Activate Account]` muncul dengan link berformat `/activate?token={token}`.
8. Verifikasi body email memuat kalimat validitas link: `"This link is valid for 24 hours and can only be used once."`.
9. Verifikasi fallback link teks (versi URL mentah) muncul dengan format yang sama dengan link tombol `[Activate Account]`.
10. Verifikasi closing paragraph: `"To keep your data secure, please don't forward this email to anyone. If you didn't create this account, just ignore this email."`.
11. Verifikasi signoff `"— TAG Samurai"`.
12. Verifikasi raw token pada link email memiliki panjang 43 karakter dan hanya terdiri dari alfabet `A-Za-z0-9-_` (tanpa `+`, `/`, `=`).

### B. Trigger via Admin Console (identik dengan jalur GS > User)

13. Login sebagai admin dan buka Admin Console (area settings-user atau jalur pembuatan Default User sesuai skenario yang diuji).
14. Buat user baru melalui jalur Admin Console dengan data unik berbeda dari langkah 2-12.
15. Verifikasi Activation Email terkirim ke alamat email user tersebut dengan konten yang identik dengan hasil verifikasi pada langkah 4-11 (subject, greeting, body, tombol, fallback link, closing, signoff).
16. Verifikasi raw token pada link email dari jalur Admin Console memenuhi kriteria 43 karakter Base64URL.

### C. Verifikasi token di database (hash, expiry, state)

17. Untuk user yang dibuat pada langkah 2, ambil raw token dari email dan hitung SHA-256 hash-nya (64 karakter hex).
18. Verifikasi kolom `token` pada record `activation_token` terkait user tersebut adalah hash SHA-256 yang cocok persis dengan hasil perhitungan pada langkah 17.
19. Verifikasi `status = active`, `consumed_at = null` pada record token tersebut.
20. Verifikasi `expires_at = created_at + 24 jam` (toleransi waktu yang wajar untuk eksekusi otomatis).
21. Verifikasi tepat 1 baris token dengan `status=active` untuk user tersebut (tidak ada token aktif lain).

### D. Snapshot Full Name & zero-logging

22. Buat user baru dengan `first_name="Budi"`, `last_name="Santoso"`, simpan email/token yang terkirim.
23. Ubah `first_name`/`last_name` user tersebut menjadi `"Budiman"/"Santoso"` melalui Global Settings > User sebelum membuka email (atau setelah email terkirim).
24. Verifikasi isi email yang terkirim sebelumnya tetap menampilkan `Hi Budi Santoso,` (snapshot lama, tidak berubah retroaktif).
25. Verifikasi tidak ada entri baru terkait trigger pembuatan token/pengiriman Activation Email pada keempat surface log: Activity Log, User Log, System Log, dan Changelog.
26. Lakukan verifikasi zero-logging pada skenario pembuatan via Admin Console (langkah 14-16) dengan membandingkan jumlah entri sebelum/sesudah pembuatan user.

## Notes

- Email, first_name, last_name dibuat unik per run melalui hook `before` untuk menghindari konflik dengan data existing.
- Verifikasi DB untuk hash token dan expiry bersifat wajib karena melibatkan aspek security (token disimpan sebagai hash, bukan plaintext).
- Raw token 43 karakter Base64URL (A-Za-z0-9-_) sesuai spesifikasi di TC-AUTH-ACT-4.
- Snapshot Full Name diuji untuk memastikan email yang sudah terkirim tidak terpengaruh perubahan data user pasca-kirim.
- Zero-logging untuk trigger Activation Email (TC-AUTH-ACT-8) diverifikasi lintas keempat surface log.
- Kedua jalur trigger (GS > User dan Admin Console) diuji dalam satu spec karena perilakunya identik (satu alur Auth yang sama) dan topik aksi sama (trigger activation email).
