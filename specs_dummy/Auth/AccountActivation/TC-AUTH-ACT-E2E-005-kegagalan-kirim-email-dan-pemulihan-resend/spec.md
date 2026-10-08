---
id: TC-AUTH-ACT-E2E-005-kegagalan-kirim-email-dan-pemulihan-resend
title: "Kegagalan pengiriman Activation Email tidak membatalkan user dan pemulihan lewat Resend"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-17
  - TC-AUTH-ACT-18
coverage:
  web: automated
---

# Kegagalan pengiriman Activation Email tidak membatalkan user dan pemulihan lewat Resend

## Prerequisites

- Login sebagai Total Control Global Settings (`Spectra.env.ADMIN_USERNAME` / `Spectra.env.ADMIN_PASSWORD`).
- Kemampuan failure injection pada email provider uji lingkungan automation: memblokir pengiriman (bounce/tanpa kirim) dan mengembalikannya ke kondisi normal pada tengah sesi.
- Mailbox uji dapat dibaca untuk memastikan email tidak tiba saat pengiriman diblokir dan untuk membaca email hasil Resend.
- Nama dan email user dibuat unik per run oleh fixture; user dibuat lewat UI Create User pada langkah pertama.
- Akses API read-only untuk memverifikasi token tetap Active dan status user selama pengiriman diblokir.
- Toleransi waktu tunggu 15 menit untuk observasi tanpa retry otomatis.

## Test Steps

### Pengiriman gagal tidak membatalkan pembuatan user (TC-AUTH-ACT-17)

1. Aktifkan simulasi kegagalan pengiriman email pada email provider uji.
2. Buka `Global Settings > User > Login User`, klik [+ User], isi First Name dan Last Name unik (hasil fixture), pilih Division, isi Email unik (hasil fixture), dan centang Access minimal satu produk, lalu klik [Submit].
3. Verifikasi user baru tetap muncul pada tabel dengan badge Pending Activation (pembuatan user tidak dibatalkan).
4. Verifikasi token aktivasi user tersebut berstatus Active dan status user tetap Pending Activation.
5. Tunggu 15 menit, lalu periksa inbox user tersebut dan notifikasi admin.
6. Verifikasi tidak ada Activation Email yang tiba selama 15 menit (tidak ada retry otomatis).
7. Verifikasi tidak ada notifikasi dari Auth kepada admin tentang kegagalan pengiriman.

### Pemulihan lewat Resend Activation Email (TC-AUTH-ACT-18)

8. Pulihkan email provider uji ke kondisi normal.
9. Pada `Global Settings > User > Login User`, klik row action Resend Activation Email untuk user tersebut.
10. Verifikasi toast sukses berbunyi "Success, activation email has been sent.".
11. Buka inbox user tersebut.
12. Verifikasi email aktivasi baru diterima.
13. Klik [Activate Account] pada email baru.
14. Verifikasi halaman `Auth > Account Activation > Set Password` tampil dengan subtitle "Set a password to log in for <email user>.".

## Notes

- TC-AUTH-ACT-18 bergantung pada kondisi yang dibuat TC-AUTH-ACT-17 (pengiriman awal gagal), sehingga keduanya berurutan dalam satu spec.
- Kebutuhan failure injection provider email dan waktu tunggu 15 menit dicatat di Prerequisites sebagai kebutuhan environment, bukan sebagai alasan pengcualian.
- Aksi Resend ditempatkan setelah seluruh verifikasi kegagalan karena menjadi langkah pemulihan akhir alur.
