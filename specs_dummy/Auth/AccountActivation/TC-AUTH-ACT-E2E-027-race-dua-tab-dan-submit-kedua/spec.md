---
id: TC-AUTH-ACT-E2E-027-race-dua-tab-dan-submit-kedua
title: "Race dua tab pada token yang sama dan submit dengan token tidak dikenal"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-121
  - TC-AUTH-ACT-122
  - TC-AUTH-ACT-127
  - TC-AUTH-ACT-131
coverage:
  web: automated
---

# Race dua tab pada token yang sama dan submit dengan token tidak dikenal

## Prerequisites

- Browser publik tanpa sesi login, dengan kemampuan membuka dua tab pada jendela yang sama.
- Pemantauan request jaringan untuk memastikan hanya satu set password yang tersimpan dan tidak ada set password kedua.
- Kemampuan menyelesaikan reCAPTCHA pada form login (test key otomatis lolos) untuk pemeriksaan login pada TC-AUTH-ACT-122.
- 2 user seeding milik automation, dibuat lewat API di hook `before` (email unik per run), berstatus Pending Activation dengan token Active: user A untuk TC-AUTH-ACT-121 dan TC-AUTH-ACT-127, user B untuk TC-AUTH-ACT-122; TC-AUTH-ACT-131 memakai token acak yang tidak pernah diterbitkan (fixture BE) tanpa user; hook `after` membersihkan user.
- Akses API read-only untuk memverifikasi password tersimpan dan status token.

## Test Steps

### Screening: dua tab membuka link aktivasi yang sama (TC-AUTH-ACT-121)

1. Buka link aktivasi user A di tab 1 dan tab 2.
2. Verifikasi kedua tab menampilkan halaman `Auth > Account Activation > Set Password`.

### Submit kedua diarahkan ke Invalid Link varian Used (TC-AUTH-ACT-121)

3. Di tab 1, isi `Aman#Sandi8` pada kedua field lalu klik button "Set Password".
4. Verifikasi halaman Activation Success tampil di tab 1.
5. Di tab 2, isi `Aman#Sandi9` pada kedua field lalu klik button "Set Password".
6. Verifikasi tab 2 diarahkan ke halaman Invalid Link varian Used (Title "Link Already Used", CTA "Go to Login").
7. Verifikasi tidak ada toast error dan tidak ada set password kedua yang terkirim.

### Link yang sama tidak dapat dipakai lagi setelah dialihkan (TC-AUTH-ACT-127)

8. Buka kembali link aktivasi user A yang sama.
9. Verifikasi halaman Invalid Link varian Used tampil dan form Set Password tidak ditampilkan.
10. Buka link tersebut sekali lagi di tab baru.
11. Verifikasi halaman Invalid Link varian Used tetap tampil pada pembukaan kedua.

### Submit kedua tidak mengubah password yang sudah ditetapkan (TC-AUTH-ACT-122)

12. Buka link aktivasi user B di tab 1 dan tab 2.
13. Di tab 1, set password `Aman#Sandi8`.
14. Verifikasi halaman Activation Success tampil di tab 1.
15. Di tab 2, submit password `Aman#Sandi9`.
16. Verifikasi tab 2 diarahkan ke halaman Invalid Link.
17. Buka `Auth > Login > Login with Password`, login dengan email user B dan Password `Aman#Sandi8`, selesaikan reCAPTCHA, lalu klik [Log in].
18. Verifikasi pesan "Your account has not been activated" tidak tampil dan kredensial diterima (alur berlanjut ke tahap berikutnya milik modul Login).
19. Login ulang dengan email user B dan Password `Aman#Sandi9`.
20. Verifikasi pesan "Incorrect email or password" tampil (password dari submit kedua tidak pernah tersimpan).
21. Verifikasi via API bahwa password user B tetap `Aman#Sandi8`.

### Submit dengan token tidak dikenal dijawab 404 (TC-AUTH-ACT-131)

22. Kirim request Set Password langsung ke server dengan token `tokenacaktidakdikenal123`, Password dan Confirm Password `Aman#Sandi8`.
23. Verifikasi server menjawab 404 (bukan 409).
24. Verifikasi FE mengarahkan ke halaman Invalid Link varian Expired untuk token tersebut.
25. Verifikasi tidak ada data yang berubah.

## Notes

- Blok dua tab (user A lalu user B) didahulukan karena menjadi inti race; kasus token tidak dikenal (tanpa user) diletakkan terakhir.
- Kebutuhan dua tab, pemantauan request, reCAPTCHA, dan fixture token dicatat di Prerequisites.
