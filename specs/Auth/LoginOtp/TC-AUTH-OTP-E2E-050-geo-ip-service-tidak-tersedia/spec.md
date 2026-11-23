---
id: TC-AUTH-OTP-E2E-050-geo-ip-service-tidak-tersedia
title: "Geo-IP Service Tidak Tersedia: Trigger Jarak Dilewati, Trigger Negara dari Header Edge Tetap Berlaku"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-192
  - TC-AUTH-OTP-195
coverage:
  web: manual
---

# Geo-IP Service Tidak Tersedia: Trigger Jarak Dilewati, Trigger Negara dari Header Edge Tetap Berlaku

## Prerequisites

- Mode: FE+BE (backend nyata; kegagalan penyedia Geo-IP tidak dapat di-intercept di browser sehingga dipicu di sisi server/penyedia, sesuai bagian 6 konvensi). Sesi dan email alert dibuktikan lewat perilaku UI dan mail-catcher.
- Tidak ada password atau token di spec atau fixture.
- Environment variable: `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-050a` dan `+{runId}-050b` (kedua TC memakai nama `Herlina Saputra`, jadi email dibedakan dengan huruf), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Berprofil seperti BASE (Activated, Active ON; device dikenali; bukan login pertama dan tidak idle; Agreement tidak terpicu; Authenticator sudah terdaftar) dengan riwayat login terakhir yang diatur lewat seed data lokasi:
  - TC-AUTH-OTP-192: `Herlina Saputra` (`herlinasaputra+{runId}-050a@qwertysystem.net`); login terakhir dari lokasi A dan koneksi penguji dari lokasi B yang berjarak lebih dari 100 km
  - TC-AUTH-OTP-195: `Herlina Saputra` (`herlinasaputra+{runId}-050b@qwertysystem.net`); login terakhir dari negara A; koneksi penguji dari negara B (header edge `X-Country-Code` menunjuk negara B); pasangan negara A–B belum tersimpan sebagai pasangan tepercaya
- Kemampuan teknis: koneksi penguji dengan lokasi Geo-IP yang dapat dikendalikan per TC (TC-AUTH-OTP-192: lokasi B berjarak lebih dari 100 km dari lokasi login terakhir; TC-AUTH-OTP-195: negara B lewat header edge `X-Country-Code`); seed data lokasi login terakhir per user; geo-IP service dapat dimatikan dan dinyalakan kembali (failure injection sisi penyedia); mail-catcher lingkungan uji untuk membaca kode OTP dan memeriksa email alert login tak biasa; jendela privat publik; reCAPTCHA mode uji.
- State global: lokasi koneksi penguji (langkah 1 dan 11) dan geo-IP service dimatikan (langkah 2, tetap mati sampai langkah 21). Suite berjalan serial (`parallel: false`) karena kedua state berlaku untuk seluruh koneksi dari environment uji. Hook `after` menyalakan kembali geo-IP service dan mengembalikan lokasi koneksi penguji ke lokasi semula, dan tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-192: Geo-IP service tidak tersedia: trigger jarak dan negara dilewati, Verify OTP lanjut ke Portal tanpa MFA

1. Atur koneksi penguji ke lokasi B (berjarak lebih dari 100 km dari lokasi login terakhir `herlinasaputra+{runId}-050a@qwertysystem.net`)
2. Matikan geo-IP service (failure injection)
3. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
4. Ketik `herlinasaputra+{runId}-050a@qwertysystem.net` pada field Email
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Request OTP]
7. Ketik 6 digit kode OTP dari email pada kotak digit
8. Verifikasi browser menuju Portal — Product Hub tanpa halaman MFA
9. Verifikasi tidak ada error atau toast gagal
10. Verifikasi email alert login tak biasa tidak terkirim ke mail-catcher `herlinasaputra+{runId}-050a@qwertysystem.net`

### TC-AUTH-OTP-195: Geo-IP service tidak tersedia dengan negara berbeda: trigger negara tetap berlaku dan Verify OTP diarahkan ke MFA

11. Atur koneksi penguji ke negara B (header edge `X-Country-Code` menunjuk negara B, berbeda dari negara login terakhir `herlinasaputra+{runId}-050b@qwertysystem.net`; geo-IP service tetap mati dari langkah 2)
12. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `herlinasaputra+{runId}-050b@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Klik button [Request OTP]
16. Ketik 6 digit kode OTP dari email pada kotak digit
17. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code` tanpa halaman pilihan metode
18. Verifikasi email alert login tak biasa diterima di mail-catcher `herlinasaputra+{runId}-050b@qwertysystem.net` (isi email dimiliki modul mfa)
19. Buka Portal — Product Hub langsung di tab lain
20. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login
21. Nyalakan kembali geo-IP service
22. Kembalikan koneksi penguji ke lokasi semula

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness b (fault injection sisi penyedia): geo-IP service dimatikan adalah kondisi yang diuji (hasilnya diasersi), bukan pemicu state UI, sehingga TC-AUTH-OTP-192 dan TC-AUTH-OTP-195 berada di spec ini, terpisah dari spec `TC-AUTH-OTP-E2E-035-handoff-mfa-geo-ip`. Kedua TC berbagi kondisi geo-IP service mati yang dimatikan sekali di langkah 2 dan dinyalakan kembali sekali di langkah 21.
- Langkah 1, 2, dan 11 (mengatur lokasi koneksi penguji dan mematikan geo-IP service) adalah langkah penghubung/kondisi dari Pre-condition TC sumber (S-03, S-11); langkah 21 dan 22 memulihkan keduanya dan hook `after` menjadi cadangan. Langkah 12 membuka jendela privat baru karena jendela TC-AUTH-OTP-192 sudah memegang sesi Portal (S-09). Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC-AUTH-OTP-192 dan 195 (`Manual Only` di TC sumber) membutuhkan koneksi penguji dengan lokasi Geo-IP terkendali, seed lokasi login terakhir, dan geo-IP service yang dapat dimatikan; tidak disebut bagaimana semuanya dikendalikan (proxy, mock Geo-IP, atau fixture BE). Kebutuhan ini dicatat di Prerequisites sebagai kemampuan teknis untuk tim FE.
  - TC-AUTH-OTP-192 dan 195 hanya menyebut profil seperti BASE; spec mengasumsikan Authenticator sudah terdaftar pada user (Prerequisites) sehingga lompatan melewati MFA berarti trigger dilewati, bukan MFA tidak aktif; asumsi ini tidak ada di TC. Mohon QA menambah precondition Authenticator terdaftar.
  - TC-AUTH-OTP-192 Expected tidak menyebut asersi sesi; spec memverifikasi sesuai Expected a sampai c. Post Condition a (satu entri Success tercatat) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi (S-01). Mohon QA menambah langkah observasinya di TC.
  - TC-AUTH-OTP-195 Post Condition a (entri Success `Login with OTP` belum ditulis) tidak punya langkah observasi di TC sumber; spec tidak menambah asersi (S-01).
  - TC-AUTH-OTP-192 tidak menyebut apakah lokasi B satu negara dengan lokasi A, sedangkan TC-AUTH-OTP-195 menyatakan trigger negara dari header edge `X-Country-Code` tetap berlaku saat geo-IP service mati. Judul TC-AUTH-OTP-192 ("trigger jarak dan negara dilewati") hanya konsisten dengan TC-AUTH-OTP-195 bila lokasi B satu negara dengan lokasi A; spec mengikuti TC-AUTH-OTP-192 apa adanya. Mohon QA menegaskan negara lokasi B pada TC-AUTH-OTP-192.
