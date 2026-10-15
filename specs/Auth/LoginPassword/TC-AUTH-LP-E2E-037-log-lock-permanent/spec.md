---
id: TC-AUTH-LP-E2E-037-log-lock-permanent
title: "Pencatatan Log Lock Permanent pada Kegagalan Pertama di Hari ke-8"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-113
coverage:
  web: automated
---

# Pencatatan Log Lock Permanent pada Kegagalan Pertama di Hari ke-8

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dan dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Hook `before` login akun aktor di browser kedua (jendela terpisah dari browser pertama) dan sesi itu tetap terbuka sepanjang spec; browser pertama dipakai subjek sebagai guest.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua browser terpisah (subjek dan aktor pengamat log); reCAPTCHA mode uji di environment; fixture BE untuk membentuk riwayat lock 1 jam pada 7 hari kalender berturut-turut; pergeseran jam server uji oleh tim BE ke hari ke-8 (tanpa percobaan pada hari itu).
- Pencarian baris log memakai nama tampilan dari TC ("Qori R"; kolom User menampilkan nama singkat, bukan email) dan dibedakan antar run lewat baseline jumlah baris awal (langkah 1 dan 2, S-12). Karena suite serial (lihat State global), tidak ada spec lain yang menulis baris untuk nama yang sama selama spec ini berjalan.
- State global: jam server uji digeser maju; suite berjalan serial (`parallel: false`) karena jam server adalah state global. Pemulihan: langkah 5 mengembalikan jam server ke waktu nyata sebelum aktor membuka log, hook `after` mengembalikannya lagi sebagai cadangan, dan sesi aktor di browser kedua dibuat ulang bila kedaluwarsa akibat pergeseran jam.
- TC-AUTH-LP-113: Tanpa login (guest); browser web
- TC-AUTH-LP-113: User `Qori Ramadhan` (`qoriramadhan+{runId}-037@qwertysystem.net`) mencapai lock 1 jam pada 7 hari kalender berturut-turut; waktu server uji sudah dimajukan ke hari ke-8 oleh tim BE
- TC-AUTH-LP-113 data: Email `qoriramadhan+{runId}-037@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### Jumlah baris log awal

1. Ganti akun: beralih ke browser kedua (sesi akun aktor Total Control Global Settings dari hook `before`), buka `Global Settings > Activity Log > Session`, lalu catat jumlah baris awal untuk user "Qori R"
2. Buka `Global Settings > User > Detail > User Log` untuk user "Qori R", lalu catat jumlah baris awal

### TC-AUTH-LP-113: Pencatatan lock Permanent pada kegagalan pertama di hari ke-8

3. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
4. Isi Email "qoriramadhan+{runId}-037@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in]
5. Pulihkan jam server uji ke waktu nyata
6. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Qori R" tampil
7. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Qori R", Activity "Login", Status "Failed" (teks biasa), Note "Account locked"
8. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
9. Buka `Global Settings > User > Detail > User Log` untuk user "Qori R", buka tab User Log, lalu cari baris terbaru
10. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Account locked"
11. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji
12. Verifikasi tanpa baris tambahan dengan Note "Incorrect password" untuk percobaan yang sama di kedua surface

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah penghubung (S-03): langkah 1 dan 2 mencatat jumlah baris awal sebagai acuan "tepat 1 baris baru".
- Kelas harness d (geser jam server): spec berdiri sendiri karena memakai state global jam server. Perilaku UI lock Permanent (Alert, tautan [Reset password]) diuji di spec `TC-AUTH-LP-E2E-014-lock-permanent-escalation`; spec ini hanya memeriksa pencatatan log.
- Langkah 12 hanya memuat klausa baru Expected c ("tanpa baris tambahan dengan Note "Incorrect password" untuk percobaan yang sama"); klausa "tepat 1 baris" sudah diasersi di langkah 7 dan 10 (S-03). Klausa itu diperlakukan sebagai asersi jumlah, bukan asersi absence kelas g (konvensi §3 prinsip 13g).
- Langkah "Ganti akun" memakai dua browser yang tetap terbuka (subjek guest dan aktor pengamat); sesi aktor dibuat di hook `before` (S-07).
- Langkah 5 (pulihkan jam server uji) adalah langkah penghubung tanpa awalan `Verifikasi` (S-09): jam dipulihkan sebelum akun aktor membuka Activity Log atau User Log; hook `after` tetap menjadi cadangan.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC memakai nama tampilan tetap ("Qori R") untuk mencari baris log; nama itu tidak unik antar run atau antar spec. Spec memakai baseline (S-12) dan suite serial; usulan: TC menyebut penanda unik per run bila kolom log memuatnya.
  - TC-AUTH-LP-113 menyatakan jam server sudah dimajukan ke hari ke-8 sebagai precondition, tetapi tidak menyebut apakah sesi aktor pengamat log (browser kedua) tetap valid setelah pergeseran jam; spec memakai sesi hook `before` dan membuatnya ulang bila perlu (dicatat di Prerequisites).
  - Nilai "terisi sesuai perangkat uji" pada IP Address dan Device / Browser tidak menyebut nilai pasti; asersi memeriksa kolom terisi dan sesuai perangkat runner.
