---
id: TC-AUTH-MFA-E2E-014-fail-open-geo-ip-dan-kombinasi-alert
title: "Fail-Open Evaluasi Geo-IP dan Konsolidasi Multi-Anomali pada Email Alert"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-45
  - TC-AUTH-MFA-46
  - TC-AUTH-MFA-52
  - TC-AUTH-MFA-209
coverage:
  web: automated
---
# Fail-Open Evaluasi Geo-IP dan Konsolidasi Multi-Anomali pada Email Alert

## Prerequisites

- Browser uji A (dikenali) dan browser uji B (device baru).
- User `Gilang Ramadhan` (`gilangramadhan@qwertysystem.net`) profil NORM.
- User `Hendra Saputra` (`hendrasaputra@qwertysystem.net`) profil IDLE_NEW (idle ≥30 hari, login dari device baru, lokasi jarak jauh).
- User `Rangga Putra` (`ranggaputra@qwertysystem.net`) profil XC2 (login terakhir Batam ID, hitungan pasangan negara ID-SG awal: 2 kali, belum mencapai threshold 3).
- Mock kontrol ketersediaan layanan Geo-IP service.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Fail-open Geo-IP: Layanan down tidak memblokir login normal

1. Konfigurasikan mock Geo-IP service dalam kondisi down / network timeout
2. Buka browser uji A dan lakukan login dengan akun `gilangramadhan@qwertysystem.net`
3. Verifikasi sistem menerapkan kebijakan fail-open: deteksi jarak dan negara dilewati tanpa memicu error 500
4. Verifikasi login berjalan single-step menuju Portal — Product Hub
5. Verifikasi sesuai keputusan NC-17, data `last_login_location` dan negara sebelumnya tidak ditimpa kosong melainkan dipertahankan

### Fail-open Geo-IP tidak mengirimkan email alert lokasi palsu

6. Periksa kotak masuk mail-catcher untuk `gilangramadhan@qwertysystem.net`
7. Verifikasi TIDAK ADA email alert yang terkirim selama geo-IP mengalami gangguan

### Konsolidasi multi-anomali dalam satu email alert

8. Aktifkan kembali layanan Geo-IP
9. Buka browser uji B (device baru) dan login dengan akun `hendrasaputra@qwertysystem.net` dari IP Surabaya (anomali gabungan: idle ≥30 hari + device baru + jarak >100 km)
10. Verifikasi halaman MFA Choose Verification Method tampil
11. Periksa kotak masuk mail-catcher untuk `hendrasaputra@qwertysystem.net`
12. Verifikasi tepat satu email alert diterima yang merangkum informasi detail login tak biasa tersebut secara lengkap

### Geo-IP service tidak tersedia tidak menambah hitungan pasangan negara (TC-209 & EC-44)

13. Gunakan akun `ranggaputra@qwertysystem.net` (profil XC2, login terakhir Batam ID, pasangan ID-SG hitungan 2 dari ambang batas 3)
14. Matikan layanan Geo-IP service (simulasi down)
15. Dari browser uji A dengan alamat IP Singapura (SG), lakukan login
16. Verifikasi kriteria beda negara dilewati karena fail-open, halaman MFA tidak muncul, dan Portal — Product Hub tampil
17. Pulihkan layanan Geo-IP, lalu lakukan logout dari Portal
18. Dari browser uji A dengan IP Singapura (SG) yang sama, ulangi login
19. Verifikasi halaman `Auth > MFA > Choose Verification Method` tampil dan email alert diterima (karena login saat geo-IP down tidak menambah hitungan pasangan negara sehingga status masih belum trusted)
20. Selesaikan verifikasi MFA dengan Authenticator app hingga login berhasil
21. Verifikasi setelah MFA sukses, hitungan pasangan ID-SG bertambah menjadi 3 dan status pasangan negara menjadi trusted
22. Logout lalu login kembali dari browser uji A dengan IP Batam (ID)
23. Verifikasi login langsung berhasil (single-step) ke Portal tanpa MFA karena pasangan ID-SG sudah berstatus trusted

## Notes

- Sesuai `AUTHMFA-LOGIC-02e` dan PRD §11, kegagalan penyedia Geo-IP bersifat fail-open demi menjamin ketersediaan login pengguna.
- Sesuai keputusan NC-17, catatan lokasi terakhir tidak ditimpa null saat geo-IP gagal.
- Sesuai PRD §9.4.2 EC-44 dan §9.2 F-AUTHMFA-08, login saat layanan Geo-IP down tidak menambah counter pasangan negara; penambahan counter hanya terjadi saat login sukses dengan evaluasi Geo-IP aktif atau pasca-verifikasi MFA berhasil.
