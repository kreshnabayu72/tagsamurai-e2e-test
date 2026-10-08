---
id: TC-AUTH-OTP-E2E-012-validasi-kode-salah-kedaluwarsa-status-akun
title: "Validasi Kode Salah, Kedaluwarsa 5 Menit, Perubahan Status Akun, dan Independensi Lock"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-49
  - TC-AUTH-OTP-50
  - TC-AUTH-OTP-55
  - TC-AUTH-OTP-61
  - TC-AUTH-OTP-62
  - TC-AUTH-OTP-68
  - TC-AUTH-OTP-120
  - TC-AUTH-OTP-123
  - TC-AUTH-OTP-124
  - TC-AUTH-OTP-133
  - TC-AUTH-OTP-184
coverage:
  web: automated
---

# Validasi Kode Salah, Kedaluwarsa 5 Menit, Perubahan Status Akun, dan Independensi Lock

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Doni Handayani` (`donihandayani@qwertysystem.net`) profil BASE.
- User `Ayu Prasetyo` (`ayuprasetyo@qwertysystem.net`) profil BASE.
- User `Andi Kartika` (`andikartika@qwertysystem.net`) profil BASE.
- User `Hendra Prasetyo` (`hendraprasetyo@qwertysystem.net`) profil BASE (akan dinonaktifkan via GS saat sesi verify berjalan).
- User `Maya Purnama` (`mayapurnama@qwertysystem.net`) profil BASE (akan dihapus via GS saat sesi verify berjalan).
- User `Rudi Hartono` (`rudihartono@qwertysystem.net`) profil BASE (status akan dikembalikan ke Pending Activation sebelum kode diverifikasi).
- User `Yoga Wibowo` (`yogawibowo@qwertysystem.net`) profil BASE.
- Akun Total Control Global Settings aktif untuk memanipulasi status user dan memeriksa log.

## Test Steps

### Verifikasi kode OTP salah dan pengosongan kotak digit (NC-10)

1. Buka halaman Request OTP, masukkan `donihandayani@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
2. Pada halaman Verify OTP, ketik 6 digit salah "999999"
3. Verifikasi auto-submit memproses verifikasi
4. Verifikasi muncul caption error inline di bawah kotak digit: "Incorrect verification code. Please try again."
5. Verifikasi seluruh 6 kotak digit otomatis dikosongkan dan kursor kembali aktif di kotak 1
6. Buka tab admin Total Control, periksa `Global Settings > User > Detail (Doni Handayani) > User Log`
7. Verifikasi tercatat satu entri "Failed" dengan Note "Incorrect OTP"
8. Verifikasi pada `Global Settings > Activity Log > Session` tercatat entri identik dengan Note "Incorrect OTP"

### Verifikasi kode OTP kedaluwarsa (> 5 menit) (NC-10)

9. Buka halaman Request OTP, masukkan `ayuprasetyo@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
10. Tunggu atau simulasikan pergeseran waktu server hingga melewati 5 menit (contoh: 5 menit 30 detik)
11. Ambil kode asli dari mail-catcher dan masukkan ke kotak digit
12. Verifikasi verifikasi ditolak dengan caption error: "Verification code has expired. Please request a new one."
13. Verifikasi kotak digit otomatis dikosongkan dan kursor kembali ke kotak 1
14. Periksa log di User Log dan Activity Log Session: verifikasi tercatat entri "Failed" dengan Note "OTP expired"

### Evaluasi kode usang yang juga melewati 5 menit

15. Buka Request OTP untuk `andikartika@qwertysystem.net`, kirim kode pertama
16. Buka kembali Request OTP untuk menerbitkan kode kedua
17. Masukkan kode pertama yang sudah usang dan telah melewati 5 menit
18. Verifikasi sistem menolaknya dengan caption "Incorrect verification code. Please try again." (bukan kode kedaluwarsa, karena kode pertama sudah digantikan dan tidak lagi aktif)

### Perubahan status user menjadi Inactive saat layar Verify terbuka (NC-04)

19. Buka Request OTP untuk `hendraprasetyo@qwertysystem.net`, terima kode di mail-catcher
20. Pada tab admin terpisah, ubah Toggle Active user `Hendra Prasetyo` menjadi OFF (Inactive) di Global Settings > User
21. Kembali ke layar Verify OTP, masukkan kode OTP yang valid
22. Verifikasi verifikasi ditolak dengan caption error: "Your account is inactive"
23. Verifikasi kotak digit dikosongkan dan kursor kembali ke kotak 1
24. Periksa log: verifikasi tercatat entri "Failed" dengan Note "Account is inactive" di kedua surface

### Akun belum aktivasi (Pending Activation) saat Verify OTP (EC-49, TC-184)

25. Buka Request OTP untuk `rudihartono@qwertysystem.net`, terbitkan kode OTP yang valid
26. Sebelum kode dimasukkan, ubah status akun `Rudi Hartono` di database/GS menjadi Pending Activation
27. Masukkan 6 digit kode OTP yang benar pada layar Verify OTP
28. Verifikasi verifikasi ditolak tanpa membuat sesi baru dan kode OTP tidak di-consume
29. Verifikasi caption error inline di bawah kotak digit adalah "Your account has not been activated"
30. Verifikasi kotak digit dikosongkan dan kursor kembali aktif di kotak 1
31. Di sesi admin Total Control: buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail (Rudi Hartono) > User Log`
32. Verifikasi tercatat tepat 1 entri baru dengan Activity "Login", Status "Failed", dan Note "Account is not activated"

### Penghapusan user (Delete) saat layar Verify terbuka (NC-04)

33. Buka Request OTP untuk `mayapurnama@qwertysystem.net`, terima kode di mail-catcher
34. Pada tab admin terpisah, hapus akun `Maya Purnama` (Delete User) dari Global Settings > User
35. Kembali ke layar Verify OTP, masukkan kode OTP valid
36. Verifikasi verifikasi ditolak dengan caption error: "Email is not registered yet"
37. Verifikasi kotak digit dikosongkan
38. Periksa log: verifikasi TIDAK mencatat entri log baru di kedua surface karena subjek user sudah tidak ada di sistem

### Independensi lock: Kegagalan OTP tidak memicu lock pada Login with Password

39. Buka Request OTP untuk `yogawibowo@qwertysystem.net`
40. Masukkan kode OTP salah berturut-turut sebanyak 3 kali
41. Buka halaman `Auth > Login with Password` (`/login`)
42. Masukkan email `yogawibowo@qwertysystem.net` dan password yang benar
43. Selesaikan reCAPTCHA dan klik [Log in]
44. Verifikasi user berhasil login tanpa hambatan banner lock 15 menit
45. Verifikasi lock progression Login with Password berdiri sendiri dan tidak terpengaruh oleh kesalahan percobaan OTP

## Notes

- Sesuai konsensus NC-04, NC-10, dan PRD §9.4.2 EC-49:
  - Kode salah, kedaluwarsa, akun inactive, dan akun belum aktivasi (Pending Activation) otomatis mengosongkan kotak digit dan mengembalikan kursor ke kotak 1.
  - Akun yang berstatus Pending Activation saat Verify ditolak dengan caption "Your account has not been activated" dan dicatat Failed `Account is not activated` (TC-AUTH-OTP-184).
  - Akun yang dinonaktifkan di tengah alur dicatat sebagai Failed `Account is inactive`.
  - Akun yang dihapus di tengah alur memunculkan caption `Email is not registered yet` dan tidak dicatat log.
- Kegagalan memasukkan OTP tidak pernah menaikkan lock counter password.
