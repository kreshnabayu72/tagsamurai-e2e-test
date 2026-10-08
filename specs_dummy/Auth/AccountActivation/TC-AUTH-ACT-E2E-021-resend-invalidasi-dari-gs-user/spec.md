---
id: TC-AUTH-ACT-E2E-021-resend-invalidasi-dari-gs-user
title: "Resend Activation Email dari Global Settings > User: link lama invalid, status tetap Pending, dan masa berlaku token baru"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-85
  - TC-AUTH-ACT-99
  - TC-AUTH-ACT-102
  - TC-AUTH-ACT-103
  - TC-AUTH-ACT-104
  - TC-AUTH-ACT-105
coverage:
  web: automated
---

# Resend Activation Email dari Global Settings > User: link lama invalid, status tetap Pending, dan masa berlaku token baru

## Prerequisites

- Sesi login Role: Total Control (Global Settings) di browser admin, untuk row action Resend Activation Email dan Popup Edit User.
- Jendela privat tanpa sesi login untuk membuka link aktivasi.
- Akses mailbox uji (mail catcher atau inbox riil) untuk mengambil link aktivasi dari email pertama sampai ketiga tiap user.
- Kemampuan menunggu atau meng-mock cooldown Resend Activation Email, dan time-travel/fixture waktu server uji untuk TC-AUTH-ACT-105.
- 5 user seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run) untuk blok TC-AUTH-ACT-99 (+85), 102, 103, 104, dan 105; satu alamat email cadangan unik disediakan hook sebagai tujuan ubah-email pada blok TC-AUTH-ACT-104; hook `after` membersihkan seluruh user.
- Akses API read-only untuk memverifikasi status token (Active/Superseded) dan status user.

## Test Steps

### Resend membuat link lama invalid dan link baru valid (TC-AUTH-ACT-99, TC-AUTH-ACT-85)

1. Ambil link aktivasi dari email pertama user blok 99 (link A).
2. Pada `Global Settings > User > Login User`, klik row action Resend Activation Email untuk user tersebut.
3. Verifikasi toast sukses: "Success, activation email has been sent."
4. Ambil link aktivasi dari email baru (link B).
5. Buka link A.
6. Verifikasi halaman Invalid Link varian Expired tampil (Title "Activation Link Expired") untuk link A walau belum 24 jam.
7. Buka link B.
8. Verifikasi halaman Set Password tampil dengan Subtitle "Set a password to log in for <email user blok 99>."
9. Verifikasi via API bahwa token A Superseded, token B Active, dan status user tetap Pending Activation.

### Dua kali Resend berturut-turut hanya menyisakan token terakhir (TC-AUTH-ACT-102)

10. Ambil link dari email pertama user blok 102 (link A).
11. Klik Resend Activation Email, lalu ambil link dari email kedua (link B).
12. Tunggu cooldown Resend berakhir, klik Resend Activation Email lagi, lalu ambil link dari email ketiga (link C).
13. Buka link A, lalu link B.
14. Verifikasi masing-masing menampilkan halaman Invalid Link varian Expired.
15. Buka link C.
16. Verifikasi halaman Set Password tampil dengan Subtitle "Set a password to log in for <email user blok 102>."
17. Verifikasi via API bahwa hanya token C yang Active, sedangkan token A dan B Superseded.

### Resend tidak mengubah status user (TC-AUTH-ACT-103)

18. Pada `Global Settings > User > Login User`, klik row action Resend Activation Email untuk user blok 103.
19. Muat ulang tabel dan cari user tersebut.
20. Verifikasi user tetap berbadge Pending Activation pada tabel (status tidak berubah akibat Resend).

### Mengubah email memicu pengiriman ulang dan membuat link lama invalid (TC-AUTH-ACT-104)

21. Ambil link aktivasi dari email pertama user blok 104 (link A).
22. Pada `Global Settings > User > Login User`, buka Popup Edit User untuk user tersebut, ubah Email menjadi alamat email cadangan unik dari hook, lalu klik [Save].
23. Ambil link aktivasi dari email baru yang tiba di alamat email cadangan (link B).
24. Buka link A.
25. Verifikasi halaman Invalid Link varian Expired tampil untuk link A.
26. Buka link B.
27. Verifikasi halaman Set Password tampil dengan Subtitle "Set a password to log in for <alamat email cadangan>."
28. Verifikasi via API bahwa token A Superseded, token B Active, dan status user tetap Pending Activation.

### Link hasil Resend berlaku 24 jam sejak token baru diterbitkan (TC-AUTH-ACT-105)

29. Ambil link A dari email pertama user blok 105 (diterbitkan pada T0).
30. Majukan waktu server uji ke T0 + 23 jam, lakukan Resend Activation Email, lalu ambil link B.
31. Majukan waktu server uji ke T0 + 30 jam.
32. Buka link A.
33. Verifikasi halaman Invalid Link varian Expired tampil untuk link A.
34. Buka link B.
35. Verifikasi halaman Set Password tampil (30 jam sejak T0 tetapi 7 jam sejak token B diterbitkan; masa berlaku dihitung dari penerbitan token B).
36. Verifikasi via API bahwa token A Superseded dan token B Active.

## Notes

- Screening (toast resend pertama) didahulukan; seluruh kasus tidak mengonsumsi token sehingga urutan blok bebas dari dependensi aktivasi.
- Time-travel pada blok terakhir diletakkan paling akhir agar penggeseran waktu tidak memengaruhi blok lain.
- Kebutuhan mailbox, cooldown, dan fixture waktu dicatat di Prerequisites.
