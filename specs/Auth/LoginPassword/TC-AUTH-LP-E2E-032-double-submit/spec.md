---
id: TC-AUTH-LP-E2E-032-double-submit
title: "Klik Ganda pada Continue dan Log in Hanya Diproses Satu Kali"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-148
  - TC-AUTH-LP-150
coverage:
  web: automated
---

# Klik Ganda pada Continue dan Log in Hanya Diproses Satu Kali

## Prerequisites

- Seeding: setiap user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`; autentikasi API, bukan sesi browser). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-032` (contoh `sriwahyuni+{runId}-032@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: klik ganda cepat pada satu tombol; pemantauan request jaringan (menghitung request konfirmasi Agreement); jendela privat baru per TC; reCAPTCHA mode uji di environment; fixture BE untuk kondisi per user (lihat daftar TC di bawah).
- Mode: FE+BE
- TC-AUTH-LP-148: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-148: User `Sri Wahyuni` (`sriwahyuni+{runId}-032@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA (di-seed lewat API dan fixture BE di hook `before`)
- TC-AUTH-LP-148 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-150: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-150: User `Intan Permata` (`intanpermata+{runId}-032@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (web) (di-seed lewat API di hook `before`)
- TC-AUTH-LP-150 data: Password salah: nilai `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### TC-AUTH-LP-148: Klik ganda [Continue ➔] hanya diproses satu kali

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman Login with Password
3. Isi Email `sriwahyuni+{runId}-032@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
4. Selesaikan reCAPTCHA
5. Klik [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan
7. Pantau request jaringan, lalu klik ganda cepat [Continue ➔]
8. Verifikasi browser menuju Portal — Product Hub satu kali
9. Verifikasi tidak ada pesan error
10. Verifikasi hanya satu request konfirmasi Agreement yang dikirim ke server
11. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-150: Klik ganda [Log in] dengan password salah dihitung satu kali

12. Buka jendela privat baru (tanpa sesi login)
13. Buka halaman Login with Password
14. Isi Email `intanpermata+{runId}-032@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD_WRONG`
15. Selesaikan reCAPTCHA
16. Klik ganda cepat [Log in]
17. Verifikasi satu Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
18. Isi Email `intanpermata+{runId}-032@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD_WRONG`
19. Selesaikan reCAPTCHA
20. Klik [Log in] (percobaan berikutnya)
21. Verifikasi Alert Danger "Incorrect email or password" tampil
22. Verifikasi caption lock tidak tampil
23. Isi Email `intanpermata+{runId}-032@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD_WRONG`
24. Selesaikan reCAPTCHA
25. Klik [Log in] (percobaan berikutnya lagi)
26. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil (kegagalan ke-3; klik ganda dihitung satu kali)

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Kelas harness: concurrency satu konteks (klik ganda), digabung dalam satu spec "double-submit" untuk Agreement dan Login; multi-tab dan race antar-sesi ada di spec `TC-AUTH-LP-E2E-033-concurrency-multitab`.
- Langkah login pada TC-AUTH-LP-148 ("Login dengan Email … sampai layar Confirm to Continue tampil") disalin utuh menjadi langkah 2–5 (S-04). Langkah 10 (hanya satu request dikirim) memverifikasi arti judul skenario "diproses satu kali" dan tidak ada di kolom Expected Result; dicatat di sini sebagai asersi tambahan beralasan (S-03).
- Urutan: TC-AUTH-LP-148 (berakhir sukses di Portal) lebih dulu, lalu TC-AUTH-LP-150 yang mengakhiri akun di status Locked 15 menit (S-10); keduanya memakai user terpisah.
- Langkah 11 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA:
  - Post Condition TC-AUTH-LP-148 ("Satu persetujuan Privacy Policy tersimpan untuk versi aktif") tidak punya cara observasi di UI; spec hanya mengasersi satu request lewat pemantauan jaringan, bukan jumlah persetujuan tersimpan.
  - TC-AUTH-LP-150 tidak menyebut apakah klik ganda menghasilkan satu atau dua request ke server; keluaran yang diasersi hanya jumlah Alert dan hitungan lock pada percobaan ketiga.
