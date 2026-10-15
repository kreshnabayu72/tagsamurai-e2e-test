---
id: TC-AUTH-ACT-E2E-015-invalid-link-varian-expired-dan-used
title: "Invalid Link: token tidak dikenal, kosong, terpotong, dan varian Used"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-09
  - TC-AUTH-ACT-79
  - TC-AUTH-ACT-80
  - TC-AUTH-ACT-81
  - TC-AUTH-ACT-82
  - TC-AUTH-ACT-83
  - TC-AUTH-ACT-84
coverage:
  web: automated
---

# Invalid Link: token tidak dikenal, kosong, terpotong, dan varian Used

## Prerequisites

- Browser publik tanpa sesi login.
- 2 user seeding milik automation, dibuat lewat API di hook `before` (email unik per run):
  - User A berstatus Pending Activation dengan token Active, untuk kasus token terpotong (TC-AUTH-ACT-82); token aslinya harus tetap dipertahankan untuk verifikasi.
  - User B berstatus Pending Activation dengan token Active, untuk diaktivasi pada langkah varian Used (TC-AUTH-ACT-83 dan TC-AUTH-ACT-84); hook `after` menghapus user B.
- Akses API read-only untuk memverifikasi token user A tetap Active setelah link terpotong dibuka.

## Test Steps

### Screening: token tidak dikenal menampilkan varian Expired (TC-AUTH-ACT-79, TC-AUTH-ACT-09)

1. Buka link aktivasi dengan token `unknown-token-12345`.
2. Susuri halaman Invalid Link dari atas ke bawah.
3. Verifikasi **Header**: Card (Elevated) single-column dengan ilustrasi 404/expired.
4. Verifikasi **Body**: Title "Activation Link Expired" dan Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
5. Verifikasi **Footer**: tidak ada CTA (tidak ada button "Go to Login") dan form Set Password tidak ditampilkan.
6. Verifikasi tidak ada toast, dialog, halaman akses ditolak (forbidden), maupun redirect ke Login.

### Link tanpa parameter token (TC-AUTH-ACT-80)

7. Buka alamat halaman aktivasi tanpa parameter token (mis. `/activate`).
8. Verifikasi halaman Invalid Link varian Expired tampil: Title "Activation Link Expired" dan Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
9. Verifikasi tidak ada button CTA (tidak ada "Go to Login") dan form Set Password tidak ditampilkan.

### Link dengan parameter token kosong (TC-AUTH-ACT-81)

10. Buka alamat halaman aktivasi dengan parameter token kosong (mis. `/activate?token=`).
11. Verifikasi halaman Invalid Link varian Expired tampil: Title "Activation Link Expired" dan Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
12. Verifikasi tidak ada button CTA (tidak ada "Go to Login") dan form Set Password tidak ditampilkan.

### Token terpotong menampilkan varian Expired (TC-AUTH-ACT-82)

13. Buka link aktivasi user A → halaman Set Password tampil (link asli valid).
14. Salin link aktivasi, lalu potong 5 karakter terakhir dari nilai parameter `token`.
15. Buka link yang sudah dipotong.
16. Verifikasi halaman Invalid Link varian Expired tampil: Title "Activation Link Expired" dan Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
17. Verifikasi tidak ada button CTA dan form Set Password tidak ditampilkan.
18. Verifikasi via API bahwa token asli user A tetap Active.

### Link terpakai menampilkan varian Used (TC-AUTH-ACT-83)

19. Buka link aktivasi user B → Set Password → ketik `Aman#Sandi8` pada kedua field → klik button "Set Password" sampai halaman Activation Success tampil.
20. Buka kembali link aktivasi user B yang sudah dipakai (token Consumed).
21. Verifikasi halaman Invalid Link varian Used tampil: Title "Link Already Used", Body "This activation link has already been used. Your account has been activated.", dan CTA "Go to Login".
22. Verifikasi form Set Password tidak ditampilkan.
23. Verifikasi Title dan Body berbeda dari varian Expired (varian Used hanya untuk token Consumed).

### Klik Go to Login pada varian Used (TC-AUTH-ACT-84)

24. Pada halaman Invalid Link varian Used, klik CTA "Go to Login".
25. Verifikasi halaman Login with Password tampil.

## Notes

- Kasus non-destruktif (token tidak dikenal, kosong, terpotong) didahulikan; aktivasi user B untuk varian Used diletakkan setelahnya karena mengonsumsi token.
- Kebutuhan kedua user seeding dicatat di Prerequisites.
