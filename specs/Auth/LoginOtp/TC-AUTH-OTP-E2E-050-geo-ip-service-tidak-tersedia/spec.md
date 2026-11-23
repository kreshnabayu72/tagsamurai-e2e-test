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

- Mode: FE+BE (backend nyata; kegagalan penyedia Geo-IP tidak dapat di-intercept di browser sehingga dipicu di sisi server/penyedia, sesuai bagian 6 konvensi). Handoff MFA dan email alert dibuktikan lewat perilaku UI dan mail-catcher, entri Success lewat Activity Log Session.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1); password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`; dipakai hanya untuk membaca `Global Settings > Activity Log > Session`.
- Tidak ada password atau token di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-050`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Berprofil seperti BASE (Activated, Active ON; device dikenali; bukan login pertama dan tidak idle; Agreement tidak terpicu; Authenticator sudah terdaftar) dengan lokasi dan negara login terakhir di-seed lewat fixture BE (Tabel Data Uji Pre-setup #18):
  - TC-AUTH-OTP-192: `Herlina Saputra` (`herlinasaputra+{runId}-050@qwertysystem.net`, Tabel Data Uji Dinamis #177); login terakhir dari lokasi A dan koneksi penguji dari lokasi B yang berjarak lebih dari 100 km di negara yang sama dengan lokasi A (header `X-Country-Code` sama, sehingga trigger negara tidak terpicu)
  - TC-AUTH-OTP-195: `Yosef Pardede` (`yosefpardede+{runId}-050@qwertysystem.net`, Tabel Data Uji Dinamis #181); login terakhir dari negara A; koneksi penguji dari negara B (header edge `X-Country-Code` menunjuk negara B); pasangan negara A–B belum tersimpan sebagai pasangan tepercaya
- Kemampuan teknis: kendali lokasi login (Tabel Data Uji Pre-setup #18): header edge `X-Country-Code` disuntikkan proxy uji per request (negara), IP penguji dipetakan ke koordinat lewat mock Geo-IP lingkungan uji (jarak), dan geo-IP service dapat dimatikan dan dinyalakan kembali (failure injection); lokasi B ditentukan per TC (TC-AUTH-OTP-192: lokasi B berjarak lebih dari 100 km dari lokasi login terakhir dengan `X-Country-Code` sama; TC-AUTH-OTP-195: negara B lewat header edge `X-Country-Code`); seed lokasi dan negara login terakhir per user lewat fixture BE; dua konteks browser (jendela privat publik dan browser admin); mail-catcher lingkungan uji untuk membaca kode OTP dan memeriksa email alert login tak biasa; reCAPTCHA mode uji.
- Baseline log: hook `before` mencatat jumlah entri Success `Login with OTP` per user uji (`Herlina Saputra`, `Yosef Pardede`) di `Global Settings > Activity Log > Session` sesudah kedua user di-seed; asersi "tepat satu entri baru" pada langkah 12 dan "belum ada entri baru" pada langkah 24 dihitung terhadap baseline itu (S-12).
- State global: lokasi koneksi penguji (langkah 1 dan 13) dan geo-IP service dimatikan (langkah 2, tetap mati sampai langkah 25). Suite berjalan serial (`parallel: false`) karena kedua state berlaku untuk seluruh koneksi dari environment uji. Hook `after` menyalakan kembali geo-IP service dan mengembalikan lokasi koneksi penguji ke lokasi semula, dan tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-192: Geo-IP service tidak tersedia: trigger jarak dilewati (negara sama), Verify OTP lanjut ke Portal tanpa MFA

1. Atur koneksi penguji ke lokasi B (berjarak lebih dari 100 km dari lokasi login terakhir `herlinasaputra+{runId}-050@qwertysystem.net`, di negara yang sama dengan lokasi A: header `X-Country-Code` sama; Tabel Data Uji Pre-setup #18)
2. Matikan geo-IP service (failure injection, Tabel Data Uji Pre-setup #18)
3. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
4. Ketik `herlinasaputra+{runId}-050@qwertysystem.net` pada field Email
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Request OTP]
7. Ketik 6 digit kode OTP dari email pada kotak digit
8. Verifikasi browser menuju Portal — Product Hub tanpa halaman MFA
9. Verifikasi tidak ada error atau toast gagal
10. Verifikasi email alert login tak biasa tidak terkirim ke mail-catcher `herlinasaputra+{runId}-050@qwertysystem.net`
11. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan cari entri `Herlina Saputra`
12. Verifikasi tepat satu entri Success `Login with OTP` baru untuk `Herlina Saputra` dibanding baseline hook `before`

### TC-AUTH-OTP-195: Geo-IP service tidak tersedia dengan negara berbeda: trigger negara tetap berlaku dan Verify OTP diarahkan ke MFA

13. Atur koneksi penguji ke negara B (header edge `X-Country-Code` menunjuk negara B, berbeda dari negara login terakhir `yosefpardede+{runId}-050@qwertysystem.net`; geo-IP service tetap mati dari langkah 2; Tabel Data Uji Pre-setup #18)
14. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
15. Ketik `yosefpardede+{runId}-050@qwertysystem.net` pada field Email
16. Centang widget reCAPTCHA "I'm not a robot"
17. Klik button [Request OTP]
18. Ketik 6 digit kode OTP dari email pada kotak digit
19. Verifikasi browser berpindah ke halaman MFA `Enter authenticator code` tanpa halaman pilihan metode
20. Verifikasi email alert login tak biasa diterima di mail-catcher `yosefpardede+{runId}-050@qwertysystem.net` (isi email dimiliki modul mfa)
21. Buka Portal — Product Hub langsung di tab lain
22. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login
23. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session` dan cari entri `Yosef Pardede`
24. Verifikasi belum ada entri Success `Login with OTP` baru untuk `Yosef Pardede` dibanding baseline hook `before` (entri ditulis saat login final di alur MFA)
25. Nyalakan kembali geo-IP service
26. Kembalikan koneksi penguji ke lokasi semula

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness b (fault injection sisi penyedia): geo-IP service dimatikan adalah kondisi yang diuji (hasilnya diasersi), bukan pemicu state UI, sehingga TC-AUTH-OTP-192 dan TC-AUTH-OTP-195 berada di spec ini, terpisah dari spec `TC-AUTH-OTP-E2E-035-handoff-mfa-geo-ip`. Kedua TC berbagi kondisi geo-IP service mati yang dimatikan sekali di langkah 2 dan dinyalakan kembali sekali di langkah 25.
- Langkah 1, 2, dan 13 (mengatur lokasi koneksi penguji dan mematikan geo-IP service) adalah langkah penghubung/kondisi dari Pre-condition TC sumber (S-03, S-11); langkah 25 dan 26 memulihkan keduanya dan hook `after` menjadi cadangan. Langkah 11 dan 23 (ganti konteks ke browser admin) adalah langkah 6 TC sumber dan langkah penghubung tanpa `Verifikasi`. Langkah 14 membuka jendela privat baru karena jendela TC-AUTH-OTP-192 sudah memegang sesi Portal (S-09). Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Expected d TC-AUTH-OTP-195 ("belum ada entri Success") adalah asersi jumlah dengan baseline, bukan asersi absence kelas g (prinsip 13g), sehingga diasersi di spec ini (S-12).
