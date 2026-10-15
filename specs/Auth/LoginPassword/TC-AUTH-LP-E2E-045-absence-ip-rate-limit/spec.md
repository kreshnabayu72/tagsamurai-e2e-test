---
id: TC-AUTH-LP-E2E-045-absence-ip-rate-limit
title: "Tidak Ada Pencatatan Log untuk Penolakan IP Rate Limit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-123
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log untuk Penolakan IP Rate Limit

## Prerequisites

- Mode: FE+BE.
- Seeding: user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`), lalu dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before`; browser kedua ditutup di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua sesi browser bersamaan; reCAPTCHA mode uji di environment; 20 submit login dalam 1 menit dari IP yang sama (batas IP rate limit endpoint login 20 request per menit per IP dan semua request dihitung); browser observer memakai IP berbeda atau kuotanya tidak terpengaruh. State global: counter rate limit per IP berubah oleh 21 submit; suite berjalan serial (`parallel: false`). Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah) memakai fixture BE untuk mengatur ulang counter rate limit IP, atau memajukan jam server uji melewati jendela 1 menit (jam server saja, bukan jam browser, karena jendela dihitung server; konvensi §6) lalu mengembalikannya ke waktu nyata; spec tidak menunggu 1 menit nyata.
- TC-AUTH-LP-123: User `Joko Susilo` (`jokosusilo+{runId}-045@qwertysystem.net`) berstatus Activated dan Active; sudah punya baris log sebelumnya (anchor, fixture BE); hitungan gagal user = 0; email `tidakterdaftar@qwertysystem.net` belum terdaftar
- TC-AUTH-LP-123 data: Email 1 "tidakterdaftar@qwertysystem.net" dengan Password `Spectra.env.LP_PASSWORD` (20 kali); Email 2 `jokosusilo+{runId}-045@qwertysystem.net` dengan Password `Spectra.env.LP_PASSWORD` (1 kali)

## Test Steps

### TC-AUTH-LP-123: Penolakan IP rate limit tidak dicatat

1. Buka halaman Login with Password di browser pertama
2. Ketik "tidakterdaftar@qwertysystem.net" di field Email
3. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in] (submit ke-1 dalam 1 menit dari IP yang sama)
6. Ulangi langkah 3 sampai 5 sampai total 20 submit dalam 1 menit dari IP yang sama, dengan Email "tidakterdaftar@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`
7. Ketik "jokosusilo+{runId}-045@qwertysystem.net" di field Email
8. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
9. Selesaikan reCAPTCHA
10. Klik [Log in] (submit ke-21 dalam menit yang sama)
11. Verifikasi Alert Danger "Too many requests. Please try again later." tampil pada submit ke-21
12. Pindah ke browser kedua (sesi aktor Total Control Global Settings), buka `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Joko S" yang dibuat sesudah langkah 1 dimulai
13. Verifikasi tidak ada baris baru untuk user "Joko S" di `Global Settings > Activity Log > Session` (anchor: baris login sebelumnya tetap tampil)
14. Buka `Global Settings > User > Detail > User Log` untuk user "Joko S", buka tab User Log, dan cari baris yang dibuat sesudah langkah 1 dimulai
15. Verifikasi tidak ada baris baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)

## Notes

- Sumber: `auth/login-password/TestCases/tc-login-password.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: asersi absence (prinsip 13g) dengan flood rate limit (kelas c).
- P-2: flood 20 submit (kelas c) hanya pemicu state rate limit dan bukan objek uji spec ini; objek uji adalah tidak adanya baris log (kelas g). Satu-satunya asersi di sisi flood adalah Alert pada submit ke-21 (Expected c TC-AUTH-LP-123), yang menandai bahwa penolakan terjadi. Asersi bukti penolakan untuk 20 submit pertama dan pesan rate limit pada submit ke-21 untuk percobaan murni diuji di spec `TC-AUTH-LP-E2E-034-rate-limit-ip` (TC-AUTH-LP-101 dan TC-AUTH-LP-104).
- Langkah penghubung (S-03): pengisian ulang field dan penyelesaian reCAPTCHA pada tiap submit (langkah 6), perpindahan antar browser, dan pemuatan ulang daftar log hanya menyiapkan konteks.
- Temuan untuk QA:
  - TC-AUTH-LP-123 langkah 2 tidak menyebut reCAPTCHA pada tiap submit, padahal submit web memerlukannya (TC-AUTH-LP-36); spec menyelesaikan reCAPTCHA mode uji pada tiap submit, dan TC tidak menyebut apakah 20 submit dalam 1 menit dikirim lewat UI atau pengirim request lain.
  - TC-AUTH-LP-123 mencantumkan "hitungan gagal user = 0" pada precondition tanpa Post Condition atau Expected untuk hitungan itu; spec tidak mengasersinya.
  - Hitungan "20 submit pertama" tidak mencantumkan asersi (hanya keterangan "ditolak, tidak dicatat" di langkah); tidak ada Verifikasi untuk 20 submit pertama di Expected, sehingga spec tidak menambahkannya (S-03).
