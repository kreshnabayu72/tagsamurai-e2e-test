---
id: TC-AUTH-ACT-E2E-009-validasi-submit-kosong-dan-mismatch
title: "Validasi Set Password saat submit: field kosong, urutan evaluasi, dan Confirm Password tidak sama"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-38
  - TC-AUTH-ACT-39
  - TC-AUTH-ACT-40
  - TC-AUTH-ACT-41
  - TC-AUTH-ACT-42
  - TC-AUTH-ACT-43
  - TC-AUTH-ACT-44
  - TC-AUTH-ACT-53
  - TC-AUTH-ACT-54
  - TC-AUTH-ACT-55
  - TC-AUTH-ACT-56
coverage:
  web: automated
---

# Validasi Set Password saat submit: field kosong, urutan evaluasi, dan Confirm Password tidak sama

## Prerequisites

- Browser publik tanpa sesi login.
- User seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run).
- Pemantauan request jaringan (DevTools/network log) untuk memastikan tidak ada request Set Password yang dikirim pada tiap kasus diblokir.
- Akses API read-only untuk memverifikasi token tetap Active dan status user tetap Pending Activation setelah seluruh spec (tidak ada submit yang diterima server).

## Test Steps

### Screening: error belum muncul sebelum submit (TC-AUTH-ACT-53, TC-AUTH-ACT-54)

1. Buka link aktivasi user seeding → halaman Set Password tampil.
2. Klik field Password lalu pindahkan fokus ke field Confirm Password tanpa mengetik apa pun.
3. Klik di luar kedua field.
4. Verifikasi tidak ada inline error "Password must not be empty" maupun "Confirm password must not be empty".
5. Ketik `Aman#Sandi8` pada field Password.
6. Ketik `Aman#Sandi9` pada field Confirm Password.
7. Verifikasi tidak ada pesan "Passwords do not match" selama mengetik dan sebelum button "Set Password" ditekan.

### Password kosong, Confirm terisi (TC-AUTH-ACT-39)

8. Kosongkan field Password (Confirm tetap `Aman#Sandi9`).
9. Klik button "Set Password".
10. Verifikasi inline error "Password must not be empty" tampil di bawah field Password.
11. Verifikasi tidak ada error "Passwords do not match" pada Confirm Password (mismatch tidak dievaluasi selama Password kosong).
12. Verifikasi tidak ada request set password yang dikirim ke server.

### Kedua field kosong (TC-AUTH-ACT-38, TC-AUTH-ACT-55)

13. Kosongkan kedua field, lalu klik button "Set Password".
14. Verifikasi inline error "Password must not be empty" di bawah Password dan "Confirm password must not be empty" di bawah Confirm Password.
15. Verifikasi halaman tetap `Auth > Account Activation > Set Password` dan tidak ada request yang dikirim.
16. Ketik `a` pada field Password.
17. Verifikasi error "Password must not be empty" hilang seketika dan error "Confirm password must not be empty" tetap tampil.

### Password valid, Confirm kosong (TC-AUTH-ACT-40, TC-AUTH-ACT-56)

18. Kosongkan field Password, ketik `Aman#Sandi8` pada field Password, lalu kosongkan field Confirm Password.
19. Klik button "Set Password".
20. Verifikasi inline error "Confirm password must not be empty" tampil, tidak ada error "Passwords do not match", dan tidak ada error pada field Password.
21. Verifikasi tidak ada request set password yang dikirim ke server.
22. Ketik `x` pada field Confirm Password.
23. Verifikasi error "Confirm password must not be empty" hilang seketika setelah field diedit.
24. Klik button "Set Password".
25. Verifikasi inline error "Passwords do not match" tampil di bawah Confirm Password (dievaluasi ulang saat submit).

### Confirm Password tidak sama (TC-AUTH-ACT-41, TC-AUTH-ACT-42, TC-AUTH-ACT-43)

26. Setel field Password `Aman#Sandi8` dan field Confirm Password `Aman#Sandi9`, lalu klik button "Set Password".
27. Verifikasi inline error "Passwords do not match" tampil di bawah Confirm Password.
28. Verifikasi halaman tetap di Set Password, tidak ada request yang dikirim, dan tidak ada toast.
29. Ganti field Confirm Password menjadi `aman#sandi8` (hanya berbeda huruf besar-kecil), lalu klik button "Set Password".
30. Verifikasi inline error "Passwords do not match" tetap tampil dan tidak ada request yang dikirim.
31. Ganti field Confirm Password menjadi `Aman#Sandi8 ` (satu spasi di akhir), lalu klik button "Set Password".
32. Verifikasi inline error "Passwords do not match" tetap tampil dan tidak ada request yang dikirim.

### Policy belum terpenuhi sekaligus Confirm berbeda (TC-AUTH-ACT-44)

33. Setel field Password `abc` dan field Confirm Password `xyz`.
34. Klik button "Set Password".
35. Verifikasi inline error "Passwords do not match" tampil di bawah Confirm Password (Password terisi sehingga mismatch dievaluasi).
36. Verifikasi tidak ada request yang dikirim, baris checklist yang belum terpenuhi tetap abu-abu (disabled) + ○, dan tidak ada toast.

## Notes

- Seluruh kasus berbagi satu sesi form karena tidak ada submit yang diterima server, sehingga data tidak berubah dan urutan kasus bebas dari dependensi cleanup.
- Urutan disusun dari screening (belum ada submit) ke submit yang diblokir, sesuai aturan urutan dalam spec.
- Kebutuhan pemantauan request dan verifikasi API dicatat di Prerequisites.
