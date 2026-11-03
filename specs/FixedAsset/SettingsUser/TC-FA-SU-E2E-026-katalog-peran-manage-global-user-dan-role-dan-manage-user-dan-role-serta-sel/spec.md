---
id: TC-FA-SU-E2E-026-katalog-peran-manage-global-user-dan-role-dan-manage-user-dan-role-serta-sel
title: "Katalog Peran Manage global user & role dan Manage user & role, serta Sel Kapabilitas Role Matrix"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-84
  - TC-FA-SU-85
coverage:
  web: automated
---

# Katalog Peran Manage global user & role dan Manage user & role, serta Sel Kapabilitas Role Matrix

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Lina Marlina, Pre-setup #1, akun default suite, `Spectra.env.FA_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite. Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji: hanya Total Control; tidak ada ganti akun.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan tier serta penugasan (#23). Target Detail: Budi Santoso.
- Data Dinamis: tidak ada.
- Kemampuan teknis: klik checkbox yang Disabled (percobaan uncheck inline).
- State global: tidak ada yang diubah; data Pre-setup tidak diubah (percobaan uncheck ditolak oleh UI).

## Test Steps

### TC-FA-SU-84: Katalog peran Manage global user & role dan Manage user & role

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Global Role)
3. Verifikasi baris `Manage global user & role` tampil dengan Create `—`, Read dan Update berupa checkbox, dan Delete `—`
4. Buka Sub-tab Group Role
5. Verifikasi baris `Manage user & role` tampil dengan kolom Read dan Update

### TC-FA-SU-85: Role matrix, sel kapabilitas tidak berlaku tampil `—`, Read terkunci

6. Buka Sub-tab Global Role
7. Verifikasi sel Create dan Delete baris `Manage global license` tampil `—` tanpa checkbox
8. Verifikasi checkbox Read baris `Import Data` tercentang dan Disabled
9. Klik checkbox Read baris `Import Data` (percobaan uncheck)
10. Verifikasi checkbox Read baris `Import Data` tetap tercentang

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16).
- Langkah 9 adalah aksi TC ("Coba uncheck Read"); langkah 10 adalah Expected b ("tidak dapat di-uncheck inline").
- Temuan untuk QA:
  - TC-FA-SU-84 Expected b ("kecuali disembunyikan saat Global Role-nya aktif") adalah klausa bersyarat tanpa langkah dan tanpa data uji dengan Global Role Manage global user & role aktif pada Budi Santoso; klausa itu tidak diasersi. Spec hanya mengasersi kondisi baris tampil.
  - TC-FA-SU-85 Expected a menyebut "Create dan Delete pada Manage global license" sebagai contoh; sel tidak berlaku pada baris `Import Data` tidak disebut, sehingga tidak diasersi.
  - TC-FA-SU-85 Expected b mensyaratkan role aktif ("selama role aktif"), tetapi Pre-setup #20 dan #23 tidak menyebut penugasan Global Role aktif untuk Budi Santoso (yang disebut memiliki Global Role Import Data adalah Gita Permata dan Rudi Hartono). Spec tetap memakai Budi Santoso sesuai langkah TC; QA perlu memastikan target yang memiliki role aktif pada baris `Import Data`.
  - TC-FA-SU-85 Expected c ("pengguna tanpa penugasan role aktif tidak memperoleh akses apa pun") tidak punya langkah observasi dan tidak ada akun pengguna tanpa penugasan di Pre-setup; tidak diasersi.
