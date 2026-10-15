---
id: TC-AUTH-LP-E2E-028-resilience-provider-failure-injection
title: "Ketahanan Login terhadap Kegagalan Penyedia: reCAPTCHA, Geo-IP, dan Versi Privacy Policy"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-100
  - TC-AUTH-LP-155
  - TC-AUTH-LP-157
coverage:
  web: automated
---

# Ketahanan Login terhadap Kegagalan Penyedia: reCAPTCHA, Geo-IP, dan Versi Privacy Policy

## Prerequisites

- Seeding: setiap user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`; autentikasi API, bukan sesi browser). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-028` (contoh `gilangramadhan+{runId}-028@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis (disediakan tim BE sebagai failure injection di sisi server, tidak bisa di-intercept di browser): (a) membuat layanan verifikasi reCAPTCHA tidak dapat dijangkau server, (b) mematikan geo-IP service, (c) membuat versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi; ditambah simulasi koneksi penguji dari lokasi yang berjarak lebih dari 100 km dari lokasi login terakhir (TC-AUTH-LP-155); jendela privat baru per TC; reCAPTCHA mode uji di environment.
- Pemulihan state global: pemicu (a), (b), dan (c) beserta simulasi lokasi dipulihkan pada akhir tiap TC dan di hook `after` (tetap jalan walau spec gagal), supaya spec lain tidak terpengaruh. State global yang diubah spec ini (layanan reCAPTCHA, geo-IP service, versi Privacy Policy aktif yang terbaca, lokasi koneksi penguji) dipakai bersama seluruh suite, sehingga suite berjalan serial (`parallel: false`).
- Mode: FE+BE
- TC-AUTH-LP-100: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-100: User `Joko Susilo` (`jokosusilo+{runId}-028@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0; layanan verifikasi reCAPTCHA tidak dapat dijangkau server (failure injection)
- TC-AUTH-LP-100 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-155: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-155: User `Gilang Ramadhan` (`gilangramadhan+{runId}-028@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; bukan login pertama dan tidak idle; login terakhir dari lokasi A; tidak ada gate Agreement; koneksi penguji dari lokasi B yang berjarak lebih dari 100 km; geo-IP service dimatikan (di-seed lewat API dan fixture BE di hook `before`)
- TC-AUTH-LP-155 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-157: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-157: User `Siti Rahmawati` (`sitirahmawati+{runId}-028@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi (fixture BE)
- TC-AUTH-LP-157 data: Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-100: Penyedia reCAPTCHA tidak dapat dijangkau server

1. Pemicu (fixture BE): jadikan layanan verifikasi reCAPTCHA tidak dapat dijangkau server
2. Buka jendela privat baru (tanpa sesi login)
3. Buka halaman Login with Password
4. Isi Email `jokosusilo+{runId}-028@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
5. Selesaikan reCAPTCHA
6. Klik [Log in]
7. Verifikasi Toast error "Error, failed to log in." tampil
8. Verifikasi tidak ada sesi dibuat
9. Verifikasi browser tidak menuju Portal — Product Hub
10. Pemulihan (fixture BE): pulihkan layanan verifikasi reCAPTCHA
11. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-155: Geo-IP service tidak tersedia: trigger lokasi dilewati, login lanjut tanpa MFA

12. Pemicu (fixture BE): matikan geo-IP service dan hubungkan penguji dari lokasi B yang berjarak lebih dari 100 km dari lokasi login terakhir
13. Buka jendela privat baru (tanpa sesi login)
14. Buka halaman Login with Password
15. Isi Email `gilangramadhan+{runId}-028@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
16. Selesaikan reCAPTCHA
17. Klik [Log in]
18. Verifikasi browser menuju Portal — Product Hub
19. Verifikasi halaman MFA tidak tampil
20. Verifikasi tidak ada error atau toast gagal
21. Pemulihan (fixture BE): hidupkan kembali geo-IP service dan kembalikan koneksi penguji ke lokasi semula
22. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-157: Password benar tetapi versi Privacy Policy aktif tidak dapat ditentukan: login diblok

23. Pemicu (fixture BE): buat versi Privacy Policy aktif tidak ter-resolve atau tanpa versi terpublikasi
24. Buka jendela privat baru (tanpa sesi login)
25. Buka halaman Login with Password
26. Isi Email `sitirahmawati+{runId}-028@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
27. Selesaikan reCAPTCHA
28. Klik [Log in]
29. Verifikasi Toast gagal "Error, failed to log in." tampil
30. Verifikasi layar Confirm to Continue tidak tampil
31. Verifikasi browser tidak menuju Portal — Product Hub
32. Verifikasi form Login tetap terbuka
33. Verifikasi nilai Email dipertahankan `sitirahmawati+{runId}-028@qwertysystem.net`
34. Pemulihan (fixture BE): kembalikan versi Privacy Policy aktif seperti semula

## Notes

- Mode: FE+BE (kegagalan sisi server/penyedia yang tidak bisa di-intercept di browser tetap FE+BE; pemicunya ditulis sebagai langkah eksplisit, bagian 6 konvensi). Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Kelas harness: fault injection (prinsip 13b), satu spec per kelas per modul untuk kegagalan sisi server/penyedia. Kegagalan yang bisa di-intercept di browser (500 dan timeout pada permintaan login atau konfirmasi Agreement) ada di spec `TC-AUTH-LP-E2E-027-resilience-submit-intercept`; kegagalan layanan penulisan log ada di spec `TC-AUTH-LP-E2E-041-resilience-log-write-failure`.
- TC-AUTH-LP-157 terbagi lintas spec: asersi "Tidak ada entri log baru untuk percobaan ini" (butir d) diuji di spec `TC-AUTH-LP-E2E-043-absence-state-based` (kelas g, prinsip 10, S-05) dan tidak ditulis di spec ini.
- Langkah "Pemicu" dan "Pemulihan" adalah langkah penghubung untuk state global (S-03, S-09); hook `after` menjadi cadangan pemulihan.
- Langkah 11 dan 22 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA:
  - Post Condition TC-AUTH-LP-157 ("Tidak ada sesi; counter percobaan gagal di-reset") tidak punya observasi UI atau langkah baca state counter di TC; spec tidak mengasersi bagian "tidak ada sesi" maupun reset counter (S-01); langkah 31 hanya mengasersi "tidak menuju Portal — Product Hub" sesuai Expected b.
  - TC-AUTH-LP-157 memakai user `sitirahmawati` yang di Tabel Data Uji Pre-setup bernilai "belum pernah login di web" (memicu Agreement/MFA), sementara precondition TC-AUTH-LP-157 hanya menyebut Activated dan Active; spec mengikuti precondition TC.
  - TC-AUTH-LP-155 tidak menyebut cara menghubungkan penguji dari "lokasi B"; spec menuliskannya sebagai kemampuan simulasi lokasi di Prerequisites tanpa mengarang mekanisme.
  - TC-AUTH-LP-100 tidak menyebut apakah hitungan gagal bertambah saat penyedia reCAPTCHA tidak dapat dijangkau; tidak diasersi.
