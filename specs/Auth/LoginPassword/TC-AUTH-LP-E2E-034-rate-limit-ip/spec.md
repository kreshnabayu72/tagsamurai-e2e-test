---
id: TC-AUTH-LP-E2E-034-rate-limit-ip
title: "Penolakan IP Rate Limit 20 Request per Menit pada Login"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-101
  - TC-AUTH-LP-104
coverage:
  web: automated
---

# Penolakan IP Rate Limit 20 Request per Menit pada Login

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek TC-AUTH-LP-104 dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dan dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: pengiriman 20 submit login dalam 1 menit dari satu IP (reCAPTCHA mode uji di environment agar tiap submit dapat diselesaikan dalam jendela 1 menit); fixture BE untuk menetapkan lock 1 jam (web) pada user subjek; pengaturan jam server absolut (jendela 1 menit dihitung di server; jam browser tidak diatur) untuk melewati jendela tanpa menunggu nyata, dengan waktu terbit diacu ke penanda waktu submit pertama jendela tersebut (tim FE/BE menyediakan kemampuan ini; TC tidak menyebut mekanismenya).
- State global: counter IP rate limit endpoint login (20 request per menit per IP, semua request dihitung, jendela tetap 1 menit). Suite berjalan serial (`parallel: false`) dan spec tidak boleh berjalan bersamaan dengan spec lain dari IP yang sama. Jam server juga diubah spec ini. Pemulihan: hook `after` memulihkan jam server ke waktu nyata dan memastikan counter rate limit IP kembali bersih sebelum suite berikutnya berjalan (tetap jalan walau spec gagal).
- TC-AUTH-LP-101: Tanpa login (guest); browser web
- TC-AUTH-LP-101: Email `tidakada@qwertysystem.net` belum terdaftar
- TC-AUTH-LP-101 data: Email `tidakada@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-104: Tanpa login (guest); browser web
- TC-AUTH-LP-104: User `Vina Melati` (`vinamelati+{runId}-034@qwertysystem.net`) berstatus Activated dan Active, sedang terkunci 1 jam di web
- TC-AUTH-LP-104 data: Email `vinamelati+{runId}-034@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### TC-AUTH-LP-101: Melampaui 20 request per menit dari satu IP ditolak dengan pesan rate limit

1. Buka halaman Login with Password
2. Dari IP yang sama kirim 20 submit login dalam 1 menit dengan Email "tidakada@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD` (reCAPTCHA diselesaikan pada tiap submit)
3. Verifikasi pada setiap dari 20 submit: caption "Email is not registered yet" tampil di bawah field Email
4. Kirim submit ke-21 dalam menit yang sama
5. Verifikasi Alert Danger "Too many requests. Please try again later." tampil di atas Button [Log in]
6. Verifikasi field Email, field Password, dan Button [Log in] tetap enabled
7. Atur jam server ke waktu submit pertama pada langkah 2 ditambah 61 detik (absolut) sehingga jendela 1 menit berlalu
8. Kirim submit lagi dengan Email dan Password yang sama (reCAPTCHA diselesaikan)
9. Verifikasi caption "Email is not registered yet" tampil lagi di bawah field Email

### TC-AUTH-LP-104: Percobaan saat lock aktif ikut dihitung ke batas 20 request per menit per IP

10. Atur jam server ke waktu submit pada langkah 8 ditambah 61 detik (absolut) sehingga jendela 1 menit berlalu
11. Buka halaman Login with Password
12. Dari IP yang sama kirim 20 submit login dalam 1 menit dengan Email "vinamelati+{runId}-034@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG` (reCAPTCHA diselesaikan pada tiap submit)
13. Verifikasi pada setiap dari 20 submit: Alert Danger "Too many failed login attempts. Your account is locked for 1 hour. You can try again at {time}." tampil dengan {time} = jam berakhirnya lock
14. Kirim submit ke-21 dalam menit yang sama
15. Verifikasi Alert Danger "Too many requests. Please try again later." tampil di atas Button [Log in]
16. Verifikasi Alert lock 1 jam tidak tampil pada submit ke-21
17. Pulihkan jam server ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah penghubung (S-03, S-09): langkah 17 memulihkan jam server ke waktu nyata setelah pemakaian terakhir (hook `after` menjadi cadangan); langkah 7 dan 10 mengatur jam server absolut (bukan menunggu nyata; konvensi bagian 6) supaya jendela 1 menit berlalu dan submit tambahan di langkah 8 tidak ikut dihitung ke 20 submit TC-AUTH-LP-104.
- Asersi "penolakan rate limit tidak dicatat" (TC-AUTH-LP-123) diuji di spec `TC-AUTH-LP-E2E-045-absence-ip-rate-limit` (kelas g, prinsip 10).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC-AUTH-LP-101 dan TC-AUTH-LP-104 tidak menyebut cara melewati jendela 1 menit; spec memakai pengaturan jam server absolut (kemampuan disediakan tim FE/BE, Prerequisites) tanpa mengarang endpoint.
  - TC-AUTH-LP-101 langkah 4 ("kirim submit lagi") tidak menyebut Email dan Password yang dipakai; spec memakai data yang sama dengan langkah 2.
  - TC-AUTH-LP-101 dan TC-AUTH-LP-104 mensyaratkan 20 submit lengkap dengan reCAPTCHA dalam 1 menit; hal ini hanya terjangkau dengan reCAPTCHA mode uji (dicatat di Prerequisites).
