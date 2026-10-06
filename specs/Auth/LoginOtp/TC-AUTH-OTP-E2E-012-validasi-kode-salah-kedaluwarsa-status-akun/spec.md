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

### Penghapusan user (Delete) saat layar Verify terbuka (NC-04)

25. Buka Request OTP untuk `mayapurnama@qwertysystem.net`, terima kode di mail-catcher
26. Pada tab admin terpisah, hapus akun `Maya Purnama` (Delete User) dari Global Settings > User
27. Kembali ke layar Verify OTP, masukkan kode OTP valid
28. Verifikasi verifikasi ditolak dengan caption error: "Email is not registered yet"
29. Verifikasi kotak digit dikosongkan
30. Periksa log: verifikasi TIDAK mencatat entri log baru di kedua surface karena subjek user sudah tidak ada di sistem

### Independensi lock: Kegagalan OTP tidak memicu lock pada Login with Password

31. Buka Request OTP untuk `yogawibowo@qwertysystem.net`
32. Masukkan kode OTP salah berturut-turut sebanyak 3 kali
33. Buka halaman `Auth > Login with Password` (`/login`)
34. Masukkan email `yogawibowo@qwertysystem.net` dan password yang benar
35. Selesaikan reCAPTCHA dan klik [Log in]
36. Verifikasi user berhasil login tanpa hambatan banner lock 15 menit
37. Verifikasi lock progression Login with Password berdiri sendiri dan tidak terpengaruh oleh kesalahan percobaan OTP

## Notes

- Sesuai konsensus NC-04 dan NC-10:
  - Kode salah, kedaluwarsa, dan akun inactive mengosongkan kotak digit secara otomatis.
  - Akun yang dinonaktifkan di tengah alur dicatat sebagai Failed `Account is inactive`.
  - Akun yang dihapus di tengah alur memunculkan caption `Email is not registered yet` dan tidak dicatat log.
- Kegagalan memasukkan OTP tidak pernah menaikkan lock counter password.
