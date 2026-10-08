---
id: TC-AUTH-MFA-E2E-011-deteksi-lokasi-jarak-dan-baseline-user
title: "Deteksi Lokasi Jarak >100 km (Haversine) dan Baseline Login Terakhir User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-33
  - TC-AUTH-MFA-51
  - TC-AUTH-MFA-208
coverage:
  web: automated
---
# Deteksi Lokasi Jarak >100 km (Haversine) dan Baseline Login Terakhir User

## Prerequisites

- Browser uji A (device dikenali), browser uji B, dan browser uji C (ID device belum dikenali).
- User `Bagas Firmansyah` (`bagasfirmansyah@qwertysystem.net`) profil FAR (login terakhir Jakarta ID, login saat ini dari IP Surabaya ID, jarak >100 km, negara sama).
- User `Dewi Wijaya` (`dewiwijaya@qwertysystem.net`) profil TWODEV (memiliki dua trusted device: browser uji A login 1 hari lalu dari Jakarta, browser uji B login 20 hari lalu dari Surabaya).
- User `Maria Ulfa` (`mariaulfa@qwertysystem.net`) profil NOLOC (tanpa catatan lokasi login terakhir di platform).
- IP uji geo-IP Jakarta dan Surabaya aktif.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Login dari lokasi >100 km memicu MFA dan email alert

1. Buka browser uji A pada halaman `Auth > Login with Password` (`/login`)
2. Konfigurasikan koneksi request menggunakan alamat IP uji Surabaya (ID)
3. Masukkan kredensial `bagasfirmansyah@qwertysystem.net` dan password valid lalu klik [Log in]
4. Verifikasi sistem menghitung jarak dari login terakhir (Jakarta) ke login saat ini (Surabaya) menggunakan formula Haversine (>100 km)
5. Verifikasi halaman `Auth > MFA > Choose Verification Method` tampil
6. Periksa kotak masuk mail-catcher untuk `bagasfirmansyah@qwertysystem.net`
7. Verifikasi email alert anomali login terkirim dengan informasi lokasi kota Surabaya

### Baseline lokasi adalah login terakhir user di platform (bukan per device)

8. Gunakan akun `dewiwijaya@qwertysystem.net` yang memiliki riwayat:
   - Login terakhir user: 1 hari yang lalu dari Jakarta menggunakan browser uji A
   - Login terakhir device B: 20 hari yang lalu dari Surabaya menggunakan browser uji B
9. Buka browser uji B (device B) dan simulasikan login dari IP Surabaya
10. Masukkan email `dewiwijaya@qwertysystem.net` dan password valid lalu klik [Log in]
11. Verifikasi sistem membandingkan lokasi login saat ini (Surabaya) dengan catatan login terakhir user di platform (Jakarta, 1 hari lalu), BUKAN dengan login terakhir device B
12. Verifikasi jarak Jakarta ke Surabaya >100 km sehingga MFA terpicu dan email alert terkirim

### User tanpa catatan lokasi login terakhir: kriteria >100 km dilewati, device baru tetap memicu MFA (TC-208)

13. Gunakan akun `mariaulfa@qwertysystem.net` yang belum memiliki catatan lokasi login terakhir (profil NOLOC)
14. Pada browser uji A (device dikenali), konfigurasikan IP uji Surabaya (ID) lalu lakukan login dengan kredensial valid
15. Verifikasi kriteria jarak >100 km dilewati karena belum ada catatan lokasi terdahulu, halaman MFA tidak muncul, dan browser langsung mendarat di Portal — Product Hub
16. Verifikasi lokasi Surabaya (ID) kini tersimpan sebagai catatan lokasi login terakhir
17. Logout dari Portal, lalu buka browser uji C (ID device belum dikenali) dengan IP Surabaya yang sama
18. Lakukan login dengan `mariaulfa@qwertysystem.net`
19. Verifikasi kriteria device baru tetap dievaluasi: halaman `Auth > MFA > Choose Verification Method` tampil dan email alert login baru terkirim ke kotak masuk

## Notes

- Sesuai `AUTHMFA-LOGIC-02c` dan keputusan NC-01, baseline lokasi dan negara adalah satu catatan login terakhir per user + platform, bukan per trusted device.
- Formula jarak yang digunakan adalah Haversine great-circle distance.
- Sesuai PRD §9.2 F-AUTHMFA-02 dan `AUTHMFA-LOGIC-02c`, kriteria jarak >100 km dilewati bila user belum memiliki catatan lokasi login terakhir, namun kriteria login pertama/device baru tetap aktif dievaluasi.
