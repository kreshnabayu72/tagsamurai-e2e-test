---
id: TC-AUTH-ACT-E2E-021-multi-tab-same-token
title: "Submit dari Dua Tab dan Resend saat Form Terbuka"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-121
  - TC-AUTH-ACT-122
  - TC-AUTH-ACT-123
coverage:
  web: automated
---

# Submit dari Dua Tab dan Resend saat Form Terbuka

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: dua tab browser untuk satu link; jendela privat browser terpisah dari browser admin.
- Hook `before` (lewat API, email bersuffix per run): buat user Pending Activation dengan token Active dan ambil link aktivasinya lewat API seeding:
  - TC-AUTH-ACT-121: `Ilham Wibowo` (`ilhamwibowo+{runId}-021@qwertysystem.net`).
  - TC-AUTH-ACT-122: `Wulan Yulianti` (`wulanyulianti+{runId}-021@qwertysystem.net`).
  - TC-AUTH-ACT-123: `Darma Aditya` (`darmaaditya+{runId}-021@qwertysystem.net`), cooldown Resend ditunggu eksplisit di langkah sebelum Resend.
- Hook `after`: hapus ketiga user dan logout sesi Login yang terbentuk.
- Password diambil dari environment variable `ACT_PASSWORD` dan `ACT_PASSWORD_ALT` (`Spectra.env.ACT_PASSWORD`, `Spectra.env.ACT_PASSWORD_ALT`; dua nilai berbeda yang sama-sama lolos kebijakan password). Kredensial akun aktor Total Control (Global Settings) diambil dari environment variable `GS_TC_PASSWORD` (`Spectra.env.GS_TC_PASSWORD`).
- TC-AUTH-ACT-121 dan 122: tanpa login (halaman publik). TC-AUTH-ACT-123: form dibuka di jendela privat, Resend dari browser admin yang login sbg Role: Total Control (Global Settings).

## Test Steps

### TC-AUTH-ACT-121: Submit dari dua tab untuk token yang sama: submit kedua diarahkan ke halaman Invalid Link varian Used

1. Buka link aktivasi user `Ilham Wibowo` di tab 1 dan tab 2 (keduanya menampilkan `Auth > Account Activation > Set Password`)
2. Di tab 1, isi `Spectra.env.ACT_PASSWORD` di kedua field lalu klik button "Set Password" → `Auth > Account Activation > Activation Success` tampil
3. Di tab 2, isi `Spectra.env.ACT_PASSWORD_ALT` di kedua field lalu klik button "Set Password"
4. Verifikasi Tab 2 diarahkan ke `Auth > Account Activation > Invalid Link` varian Used (Title "Link Already Used", CTA "Go to Login")
5. Verifikasi Tidak ada toast error dan tidak ada set password kedua
6. Verifikasi Token user `Ilham Wibowo` Consumed dan status user Activated (satu kali)

### TC-AUTH-ACT-122: Submit kedua dengan token consumed tidak mengubah password yang sudah ditetapkan

7. Buka link aktivasi user `Wulan Yulianti` di tab 1 dan tab 2
8. Di tab 1, set password `Spectra.env.ACT_PASSWORD` → `Auth > Account Activation > Activation Success` tampil
9. Di tab 2, submit password `Spectra.env.ACT_PASSWORD_ALT` → diarahkan ke `Auth > Account Activation > Invalid Link`
10. Buka `Auth > Login > Login with Password`, login dengan Email `wulanyulianti+{runId}-021@qwertysystem.net` dan Password `Spectra.env.ACT_PASSWORD`
11. Verifikasi Pesan "Your account has not been activated" tidak tampil dan kredensial diterima: halaman `Auth > Login > Login with Password` ditinggalkan dan user diarahkan ke Confirm Agreement, MFA, atau Portal — Product Hub sesuai konfigurasi akun
12. Hapus sesi yang terbentuk (logout atau bersihkan cookie), lalu buka lagi `Auth > Login > Login with Password`
13. Login dengan Email `wulanyulianti+{runId}-021@qwertysystem.net` dan Password `Spectra.env.ACT_PASSWORD_ALT`
14. Verifikasi Pesan "Incorrect email or password" tampil (password dari submit kedua tidak pernah tersimpan)
15. Verifikasi Password user `Wulan Yulianti` tetap `Spectra.env.ACT_PASSWORD`

### TC-AUTH-ACT-123: Resend saat form terbuka: submit dengan token lama diarahkan ke halaman Invalid Link

16. Di jendela privat, buka link aktivasi user `Darma Aditya` → halaman `Auth > Account Activation > Set Password` tampil
17. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
18. Tunggu cooldown Resend Activation Email (60 detik) sejak email terakhir dikirim untuk user `Darma Aditya`
19. Pindah ke browser admin: login sbg Role: Total Control (Global Settings), buka `Global Settings > User > Login User`, klik Resend Activation Email untuk user `Darma Aditya`
20. Pindah kembali ke jendela privat dan klik button "Set Password"
21. Verifikasi Tab form diarahkan ke `Auth > Account Activation > Invalid Link` varian Expired (Title "Activation Link Expired")
22. Verifikasi Tidak ada set password yang tersimpan; tidak ada toast
23. Verifikasi Token lama user `Darma Aditya` Superseded dan token baru Active; status user tetap Pending Activation

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness c (multi-konteks: dua tab, jendela privat dan browser admin). TC-AUTH-ACT-123 berasal dari E2E-026.
- Langkah pembersihan sesi di TC-AUTH-ACT-122 ditambahkan supaya login kedua tidak memakai sesi login pertama; tidak mengubah makna TC-AUTH-ACT-122.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
