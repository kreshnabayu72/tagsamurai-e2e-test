---
id: TC-AUTH-LP-E2E-033-concurrency-multitab
title: "Konsistensi Hitungan Gagal Lintas Tab dan Submit Password Salah Bersamaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-146
  - TC-AUTH-LP-147
coverage:
  web: automated
---

# Konsistensi Hitungan Gagal Lintas Tab dan Submit Password Salah Bersamaan

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), berstatus Activated dan Active. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua tab dan tiga tab browser dalam satu konteks browser; klik [Log in] pada tiga tab dengan selisih kurang dari 1 detik (pengiriman serentak); reCAPTCHA mode uji di environment; fixture BE untuk menetapkan hitungan gagal 0 (web) pada user subjek.
- Pemulihan state: lock yang terpicu pada kedua user dibersihkan dengan menghapus user di hook `after`.
- TC-AUTH-LP-146: Tanpa login (guest); browser web
- TC-AUTH-LP-146: User `Fitri Handayani` (`fitrihandayani+{runId}-033@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (web)
- TC-AUTH-LP-146 data: Email `fitrihandayani+{runId}-033@qwertysystem.net`; Password salah `Spectra.env.LP_PASSWORD_WRONG`; Password benar `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-147: Tanpa login (guest); browser web
- TC-AUTH-LP-147: User `Galih Pratama` (`galihpratama+{runId}-033@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (web)
- TC-AUTH-LP-147 data: Email `galihpratama+{runId}-033@qwertysystem.net`; Password salah `Spectra.env.LP_PASSWORD_WRONG`; Password benar `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-146: Hitungan gagal konsisten lintas tab pada akun yang sama

1. Buka halaman Login with Password pada dua tab browser (tab A dan tab B)
2. Pada tab A: isi Email "fitrihandayani+{runId}-033@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in] (salah ke-1)
3. Verifikasi pada tab A: Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
4. Pada tab B: isi Email "fitrihandayani+{runId}-033@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in] (salah ke-2)
5. Verifikasi pada tab B: Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
6. Pada tab A: isi Email "fitrihandayani+{runId}-033@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in] (salah ke-3)
7. Verifikasi pada tab A: Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil
8. Pada tab B: isi Email "fitrihandayani+{runId}-033@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
9. Verifikasi pada tab B: Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil
10. Verifikasi pada tab B: login tidak berhasil

### TC-AUTH-LP-147: Tiga submit password salah bersamaan dari tiga tab menghasilkan satu lock

11. Tutup tab A dan tab B dari TC-AUTH-LP-146
12. Buka halaman Login with Password pada tiga tab browser (tab A, tab B, tab C)
13. Pada tiap tab: isi Email "galihpratama+{runId}-033@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA
14. Klik [Log in] pada ketiga tab sebisa mungkin bersamaan (selisih kurang dari 1 detik)
15. Catat Alert pada setiap tab
16. Verifikasi tepat satu tab menampilkan Alert "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}."
17. Verifikasi dua tab lainnya menampilkan Alert "Incorrect email or password" di atas Button [Log in]
18. Pada salah satu tab: isi ulang Password `Spectra.env.LP_PASSWORD` (benar), selesaikan reCAPTCHA, klik [Log in]
19. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil
20. Verifikasi login tidak berhasil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah penghubung (S-03): langkah 11 (menutup tab sisa TC-AUTH-LP-146 agar TC-AUTH-LP-147 mulai dari tiga tab bersih, S-09).
- Dua user dipakai terpisah supaya hitungan gagal tiap TC dimulai dari 0 dan penyebab kegagalan jelas (S-06).
- Asersi "login tidak berhasil" (langkah 10 dan 20) mengikuti Expected TC apa adanya; klausa tambahan tentang halaman tetap di Login atau tidak menuju Portal tidak ada di TC sehingga tidak diasersi (S-03).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC-AUTH-LP-147 langkah 2 ("sebisa mungkin bersamaan") tidak memberi toleransi yang bisa diukur selain "selisih kurang dari 1 detik"; tab mana yang menampilkan Alert lock tidak ditentukan, sehingga asersi hanya pada jumlah tab (satu lock, dua Incorrect).
  - TC-AUTH-LP-146 dan TC-AUTH-LP-147 tidak menyebut apakah reCAPTCHA harus diselesaikan ulang pada tiap submit; spec mengikuti TC-AUTH-LP-29 (widget kembali Unsolved setelah respons gagal) dan menyelesaikannya pada tiap submit.
