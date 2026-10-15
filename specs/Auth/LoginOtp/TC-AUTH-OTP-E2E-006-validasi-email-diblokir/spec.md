---
id: TC-AUTH-OTP-E2E-006-validasi-email-diblokir
title: "Validasi Field Email pada Request OTP yang Diblokir: Kosong, Format, dan Batas 120 Karakter"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-11
  - TC-AUTH-OTP-12
  - TC-AUTH-OTP-13
  - TC-AUTH-OTP-167
  - TC-AUTH-OTP-16
  - TC-AUTH-OTP-168
  - TC-AUTH-OTP-17
coverage:
  web: automated
---

# Validasi Field Email pada Request OTP yang Diblokir: Kosong, Format, dan Batas 120 Karakter

## Prerequisites

- Mode: FE+BE (web). Tanpa sesi login; spec berjalan di konteks browser bersih. reCAPTCHA mode uji di environment.
- Kemampuan teknis: mail-catcher lingkungan uji dapat dibaca untuk alamat yang diketik (membuktikan tidak ada email OTP terkirim).
- Tidak ada user yang dibuat atau dipakai: semua input ditolak sebelum atau tanpa menemukan akun. Input uji berikut ditulis literal karena submit-nya diblokir dan tidak ada data tercipta:
  - TC-AUTH-OTP-12: `budisantoso.qwertysystem.net` (tanpa `@`)
  - TC-AUTH-OTP-13: `budisantoso@qwertysystem.c` (1 karakter setelah titik)
  - TC-AUTH-OTP-167: 121 karakter `y` tanpa `@`
  - TC-AUTH-OTP-16: `batasemail121@ccccccccccccccccccccccccccccccccccccccccccccccc.dddddddddddddddddddddddddddddddddddddddddd.qwertysystem.net` (121 karakter: local-part `batasemail121` 13 karakter, domain 107 karakter dengan label 47 huruf `c`, label 42 huruf `d`, `qwertysystem`, `net`; tiap label DNS maksimal 63 karakter), tidak terdaftar di Global Settings > User
  - TC-AUTH-OTP-168: `xxxxxxxxxxxxxxxxxxxx@eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.fffffffffffffffffffffffffffffffffffffffff.qwertysystem.net` (121 karakter: local-part 20 karakter `x`, domain 100 karakter dengan label 41 huruf `e`, label 41 huruf `f`, `qwertysystem`, `net`; tiap label DNS maksimal 63 karakter), tidak terdaftar di Global Settings > User
  - TC-AUTH-OTP-17: `batasemail120@gggggggggggggggggggggggggggggggggggggggggggg.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.qwertysystem.net` (120 karakter: local-part `batasemail120` 13 karakter, domain 106 karakter dengan label 44 huruf `g`, label 44 huruf `h`, `qwertysystem`, `net`; tiap label DNS maksimal 63 karakter), lalu ditambah `t` di akhir menjadi 121 karakter, lalu `t` dihapus kembali menjadi 120 karakter
- Tidak ada state global yang diubah dan tidak ada data yang perlu dibersihkan.

## Test Steps

### TC-AUTH-OTP-11: Request OTP dengan field Email kosong

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser
2. Biarkan field Email kosong
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi caption error di bawah field Email: "Email must not be empty"
6. Verifikasi halaman tetap di Request OTP
7. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-12: Request OTP dengan email tanpa tanda @

8. Buka ulang halaman `Auth > Login with OTP > Request OTP`
9. Ketik `budisantoso.qwertysystem.net` pada field Email
10. Centang widget reCAPTCHA "I'm not a robot"
11. Klik button [Request OTP]
12. Verifikasi caption error di bawah field Email: "Email format is incorrect"
13. Verifikasi halaman tetap di Request OTP
14. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-13: Request OTP dengan email yang hanya memiliki 1 karakter setelah titik

15. Buka ulang halaman `Auth > Login with OTP > Request OTP`
16. Ketik `budisantoso@qwertysystem.c` pada field Email
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Request OTP]
19. Verifikasi caption error di bawah field Email: "Email format is incorrect"
20. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-167: Email 121 karakter tanpa tanda @ menampilkan caption format, bukan caption batas panjang

21. Buka ulang halaman `Auth > Login with OTP > Request OTP`
22. Ketik 121 karakter `y` tanpa tanda @ pada field Email
23. Centang widget reCAPTCHA "I'm not a robot"
24. Klik button [Request OTP]
25. Verifikasi caption error di bawah field Email: "Email format is incorrect"
26. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-16: Request OTP dengan email 121 karakter ditolak dengan caption batas panjang

27. Buka ulang halaman `Auth > Login with OTP > Request OTP`
28. Ketik `batasemail121@ccccccccccccccccccccccccccccccccccccccccccccccc.dddddddddddddddddddddddddddddddddddddddddd.qwertysystem.net` (121 karakter, format valid) pada field Email
29. Centang widget reCAPTCHA "I'm not a robot"
30. Klik button [Request OTP]
31. Verifikasi caption error di bawah field Email: "Max. 120 characters"
32. Verifikasi nilai 121 karakter tetap utuh di field (tidak dipotong)
33. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-168: Email tak terdaftar 121 karakter menampilkan caption batas panjang, bukan caption belum terdaftar

34. Buka ulang halaman `Auth > Login with OTP > Request OTP`
35. Ketik `xxxxxxxxxxxxxxxxxxxx@eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.fffffffffffffffffffffffffffffffffffffffff.qwertysystem.net` (121 karakter, berformat valid, tidak terdaftar) pada field Email
36. Centang widget reCAPTCHA "I'm not a robot"
37. Klik button [Request OTP]
38. Verifikasi caption error di bawah field Email: "Max. 120 characters"
39. Verifikasi caption "Email is not registered yet" tidak tampil
40. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-17: Caption batas panjang email muncul saat karakter ke-121 diketik dan hilang saat kembali ke 120

41. Buka ulang halaman `Auth > Login with OTP > Request OTP`
42. Ketik `batasemail120@gggggggggggggggggggggggggggggggggggggggggggg.hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.qwertysystem.net` (120 karakter) pada field Email
43. Verifikasi tidak ada caption pada field Email
44. Ketik 1 karakter tambahan `t` di akhir sehingga menjadi 121 karakter, tanpa mengklik [Request OTP]
45. Verifikasi caption "Max. 120 characters" muncul langsung tanpa klik [Request OTP]
46. Verifikasi karakter ke-121 tetap tampil di field
47. Hapus karakter `t` sehingga kembali 120 karakter
48. Verifikasi caption "Max. 120 characters" hilang seketika

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Urutan TC di spec: 11, 12, 13, 167, 16, 168, 17 (validasi paling dasar dulu, lalu urutan evaluasi format sebelum panjang, TC tanpa submit di akhir). Urutan ini berbeda dari nomor TC sumber.
- Langkah 8, 15, 21, 27, 34, dan 41 adalah langkah penghubung (membuka ulang halaman Request OTP agar tiap TC mulai dari field kosong dan widget reCAPTCHA dalam state awal), tanpa asersi (S-03).
- Spec ini melewati sekitar 35 langkah (48 langkah) karena tujuh TC; tiap TC berdiri sendiri lewat buka ulang halaman sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal (batas ukuran bagian 3).
- Asersi absence TC-AUTH-OTP-11, 12, 13, 16, 167, dan 168 ("tidak ada entri log baru di `Global Settings > Activity Log > Session` maupun `Global Settings > User > Detail > User Log`") dipindah ke E2E-040 (kelas g). Pembagian TC dicatat juga di Notes E2E-040. Akun admin Total Control (Pre-setup #1) sebab itu tidak dipakai di spec ini.
- Temuan untuk QA:
  - TC-AUTH-OTP-11, 12, 13, 16, 167, dan 168 mencentang reCAPTCHA sebelum klik [Request OTP], tetapi TC tidak menyatakan apakah penolakan validasi sisi klien (kosong, format, panjang) me-reset widget reCAPTCHA (NC-09 hanya mengatur respons server). Spec membuka ulang halaman per TC agar state awal pasti.
  - TC-AUTH-OTP-16 tidak menyebut apakah email 121 karakter itu terdaftar; spec memakai alamat dari TC itu dan mengasumsikan tidak terdaftar di Global Settings > User (sama seperti TC-AUTH-OTP-168).
  - Hanya TC-AUTH-OTP-167 yang berbeda bentuk: memakai 121 karakter `y` tanpa `@` (tanpa local-part dan domain), sedangkan TC-AUTH-OTP-15, 16, 17, dan 168 memakai local-part maksimal 64 karakter dan domain panjang. Spec mengikuti TC; mohon QA mengonfirmasi bentuk TC-AUTH-OTP-167 disengaja karena yang diuji urutan cek format sebelum panjang.
