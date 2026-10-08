---
id: TC-AUTH-LP-E2E-006-lock-progression-tahap-15-menit
title: Lock progression tahap 15 menit dan evaluasi selama window aktif
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-29
  - TC-AUTH-LP-30
  - TC-AUTH-LP-38
  - TC-AUTH-LP-39
  - TC-AUTH-LP-40
  - TC-AUTH-LP-41
  - TC-AUTH-LP-42
  - TC-AUTH-LP-43
  - TC-AUTH-LP-138
  - TC-AUTH-LP-151
coverage:
  web: automated
---

# Lock progression tahap 15 menit dan evaluasi selama window aktif

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `rinaputri@qwertysystem.net` berstatus Activated dan Active dengan `failed_count=0` dan tidak dalam kondisi terkunci di awal pengujian.
- Pengaturan General Settings entitas: Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` dan Time Format `HH:mm`.
- Kemampuan penyesuaian waktu server uji atau API seeding untuk verifikasi akhir masa lock (TC-AUTH-LP-151).

## Test Steps

### Kegagalan password ke-1 dan ke-2 tanpa lock

1. Buka halaman Login with Password di browser web
2. Masukkan email `rinaputri@qwertysystem.net` dan password salah `SalahPass#1`
3. Selesaikan reCAPTCHA lalu klik tombol [Log in] (percobaan ke-1)
4. Verifikasi Alert Danger "Incorrect email or password" tampil di atas tombol [Log in]
5. Verifikasi caption lock tidak tampil dan field Password dikosongkan otomatis
6. Masukkan kembali password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (percobaan ke-2)
7. Verifikasi Alert Danger "Incorrect email or password" tetap tampil dan caption lock tidak tampil

### Kegagalan password ke-3 memicu Lock 15 Menit

8. Masukkan kembali password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (percobaan ke-3)
9. Verifikasi Alert Danger menampilkan pesan: "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}."
10. Verifikasi format `{time}` pada pesan hanya berupa jam (Time Format `HH:mm`) tanpa tanggal, sesuai waktu zona entitas
11. Verifikasi tautan [Reset password] tidak tampil di dalam Alert Danger (hanya link di footer yang ada)
12. Verifikasi field Email, field Password, dan tombol [Log in] tetap dalam status enabled
13. Simpan nilai `{time}` yang ditampilkan untuk pembanding langkah berikutnya

### Stabilitas pesan lock dan ketiadaan countdown

14. Tunggu selama 70 detik tanpa melakukan refresh halaman
15. Verifikasi teks pada Alert Danger tetap menampilkan nilai `{time}` yang sama persis
16. Verifikasi tidak ada mekanisme countdown (hitung mundur detik/menit) pada Alert

### Percobaan submit selama window lock 15 menit aktif

17. Masukkan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
18. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tetap tampil dengan nilai `{time}` yang tidak bertambah
19. Masukkan password yang benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
20. Verifikasi login tetap ditolak dengan pesan lock 15 menit yang sama dan user tidak dialihkan ke Portal

### Urutan evaluasi: Lock mendahului Password kosong dan reCAPTCHA

21. Kosongkan field Password, selesaikan reCAPTCHA, lalu klik tombol [Log in]
22. Verifikasi Alert Danger lock 15 menit tetap tampil dan caption "Password must not be empty" tidak tampil
23. Masukkan password `QaLogin#2026` tanpa menyelesaikan widget reCAPTCHA, lalu klik tombol [Log in]
24. Verifikasi Alert Danger lock 15 menit tetap tampil dan caption "Please verify that you are not a robot" tidak tampil, membuktikan evaluasi status lock aktif mendahului validasi password kosong dan reCAPTCHA

### Sinkronisasi format Time Format General Settings

25. Melalui sesi terpisah / hook API, ubah pengaturan Time Format di General Settings menjadi `hh:mm a`
26. Muat ulang halaman login dan masukkan kembali email `rinaputri@qwertysystem.net` dengan password salah `SalahPass#1`
27. Selesaikan reCAPTCHA lalu klik tombol [Log in]
28. Verifikasi nilai `{time}` pada pesan lock kini berformat 12 jam dengan penanda `AM` atau `PM` (misal `03:45 PM`)
29. Kembalikan pengaturan Time Format ke `HH:mm`

### Evaluasi submit saat masa lock berakhir

30. Majukan waktu sistem server uji hingga tepat melewati batas waktu `{time}` berakhirnya lock
31. Muat ulang halaman login
32. Masukkan email `rinaputri@qwertysystem.net` dan password benar `QaLogin#2026`
33. Selesaikan reCAPTCHA lalu klik tombol [Log in]
34. Verifikasi login berhasil dan browser dialihkan ke Portal — Product Hub

## Notes

- Sesuai NC-01, pemeriksaan lock aktif dilakukan di awal (setelah validasi format email dasar) mendahului validasi password kosong dan reCAPTCHA.
- Parameter `{time}` lock mengikuti Time Format dan Time Zone General Settings entitas dan hanya menyajikan informasi jam tanpa tanggal (NC-10, NC-11).
