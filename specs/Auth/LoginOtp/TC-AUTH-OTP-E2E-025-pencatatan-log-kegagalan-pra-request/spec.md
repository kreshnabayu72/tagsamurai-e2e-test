---
id: TC-AUTH-OTP-E2E-025-pencatatan-log-kegagalan-pra-request
title: "Pencatatan Log pada Berbagai Kondisi Kegagalan Pra-Request dan Struktur Dua Surface"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-116
  - TC-AUTH-OTP-117
  - TC-AUTH-OTP-118
coverage:
  web: automated
---

# Pencatatan Log pada Berbagai Kondisi Kegagalan Pra-Request dan Struktur Dua Surface

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Log Recaptcha` (`logrecaptcha@qwertysystem.net`) profil BASE.
- User `Log Pending` (`logpending@qwertysystem.net`) profil PENDING.
- User `Log Inactive` (`loginactive@qwertysystem.net`) profil INACTIVE.
- Akun admin Total Control Global Settings disiapkan untuk memeriksa pencatatan Activity Log Session dan User Log.

## Test Steps

### Kegagalan validasi reCAPTCHA di client tidak pernah menghasilkan log

1. Buka halaman Request OTP di browser
2. Masukkan email `logrecaptcha@qwertysystem.net` ke field Email
3. Biarkan widget reCAPTCHA kosong (tidak dicentang)
4. Klik button [Request OTP]
5. Verifikasi caption "Please verify that you are not a robot" tampil
6. Buka sesi Total Control di tab terpisah
7. Periksa `Global Settings > Activity Log > Session`
8. Verifikasi tidak ada penambahan entri log baru dari percobaan tersebut
9. Periksa `Global Settings > User > Detail (Log Recaptcha) > tab User Log`
10. Verifikasi tidak ada entri log baru yang tercatat karena aksi terhenti di sisi antarmuka klien

### Pencatatan log kegagalan akun belum aktivasi pada dua surface

11. Buka kembali Request OTP, masukkan email `logpending@qwertysystem.net` (profil PENDING)
12. Centang reCAPTCHA dan klik button [Request OTP]
13. Verifikasi muncul pesan "Your account has not been activated yet"
14. Pada tab admin Total Control, periksa `Global Settings > User > Detail (Log Pending) > tab User Log`
15. Verifikasi terdapat penambahan tepat satu entri baru dengan:
    - Status: "Failed"
    - Method / Action: "Login with OTP"
    - Note: "Account not activated"
    - IP Address: sesuai IP klien uji
16. Periksa `Global Settings > Activity Log > Session`
17. Verifikasi entri yang sama tercatat secara sinkron pada log sesi sistem

### Pencatatan log kegagalan akun inactive pada dua surface

18. Buka Request OTP, masukkan email `loginactive@qwertysystem.net` (profil INACTIVE)
19. Centang reCAPTCHA dan klik button [Request OTP]
20. Verifikasi muncul pesan "Your account is inactive"
21. Pada tab admin Total Control, periksa User Log milik `Log Inactive`
22. Verifikasi terdapat penambahan tepat satu entri baru dengan Status "Failed" dan Note "Account is inactive"
23. Periksa Activity Log > Session dan verifikasi tercatat entri identik pada surface audit sistem

## Notes

- TAG Samurai menerapkan audit trail ketat pada setiap interaksi autentikasi yang mencapai backend:
  - Validasi yang gagal di sisi klien (seperti reCAPTCHA belum dicentang atau format email rusak) tidak mengirim request ke server sehingga tidak menghasilkan log.
  - Penolakan status akun yang dievaluasi server wajib dicatat secara simetris di dua surface: `Activity Log > Session` dan `User Detail > User Log`.
