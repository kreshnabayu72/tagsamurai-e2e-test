---
id: TC-AUTH-LP-E2E-019-mobile-play-integrity-invalid
title: "Login Mobile dengan Token Play Integrity Kosong atau Invalid Ditolak"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-75
coverage:
  mobile: automated
---

# Login Mobile dengan Token Play Integrity Kosong atau Invalid Ditolak

## Prerequisites

- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Login aktor observer `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` di browser kedua dilakukan di hook `before`.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: aplikasi native Android TAG Samurai Mobile (perangkat atau emulator); browser kedua untuk observer; failure injection oleh tim BE agar token Play Integrity yang dikirim aplikasi kosong atau invalid, dengan pemulihan injeksi di hook `after` yang tetap jalan walau spec gagal di tengah.
- Mode: FE+BE.
- Spec ini serial (`parallel: false`) bersama spec log lain di suite. Baris Activity Log Session dikenali lewat nama tampilan "Joko S" dari TC (bukan email dengan suffix run), sehingga asersi "tepat 1 baris baru" memakai baseline jumlah baris sebelum aksi (S-12).
- TC-AUTH-LP-75: User `Joko Susilo` (`jokosusilo+{runId}-019@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (mobile); aplikasi native Android TAG Samurai Mobile; token Play Integrity kosong atau invalid (failure injection)
- TC-AUTH-LP-75: Login sbg Role: Total Control (Global Settings) di browser kedua: `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`
- TC-AUTH-LP-75 data: Email `jokosusilo+{runId}-019@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-75: Login di aplikasi mobile dengan token Play Integrity kosong atau invalid

1. Pada `Global Settings > Activity Log > Session` (browser kedua): catat jumlah baris untuk user "Joko S" sebagai pembanding
2. Buka layar Login with Password di aplikasi
3. Ketik email `jokosusilo+{runId}-019@qwertysystem.net` di field Email
4. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
5. Pastikan token Play Integrity yang dikirim aplikasi kosong atau invalid (failure injection BE)
6. Ketuk [Log in]
7. Verifikasi Toast error: "Error, failed to log in." tampil
8. Verifikasi tidak ada sesi dibuat
9. Verifikasi aplikasi tetap di layar Login
10. Pada `Global Settings > Activity Log > Session` (browser kedua): muat ulang daftar sampai baris terbaru untuk user "Joko S" tampil
11. Verifikasi tepat 1 baris baru dibanding langkah 1 dengan Activity "Login", Status "Failed", Note "Captcha not completed"
12. Pulihkan failure injection token Play Integrity

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah 1 (pencatatan jumlah baris pembanding) dan langkah 12 (pemulihan injeksi) adalah langkah penghubung tanpa awalan `Verifikasi` (S-03); langkah 1 dibutuhkan agar "tepat 1 baris baru" dapat diasersi.
- Temuan untuk QA: TC memakai nama tampilan tetap "Joko S" untuk mengenali baris log, bukan email dengan suffix run; user lain bernama sama dari run atau spec lain dapat mengaburkan hitungan, sehingga spec dijalankan serial dengan baseline.
- Temuan untuk QA: TC-AUTH-LP-75 bertanda Manual Only namun bagian Precondition-nya memuat kondisi yang bisa dibuat lewat failure injection; spec tetap dirancang untuk otomasi dan kebutuhan injeksi ditulis di Prerequisites. TC tidak menyebut cara pembanding "baris baru" ditentukan; spec memakai jumlah baris sebelum aksi.
