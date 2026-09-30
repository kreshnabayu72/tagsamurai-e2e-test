---
id: TC-GS-USER-E2E-008-toggle-active-user
title: Toggle Active user secara single dan bulk pada berbagai kondisi data
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-44
  - TC-GS-USER-45
  - TC-GS-USER-42
  - TC-GS-USER-435
  - TC-GS-USER-41
  - TC-GS-USER-447
  - TC-GS-USER-43
  - TC-GS-USER-446
  - TC-GS-USER-46
  - TC-GS-USER-480
  - TC-GS-USER-91
  - TC-GS-USER-443
  - TC-GS-USER-47
  - TC-GS-USER-445
  - TC-GS-USER-444
  - TC-GS-USER-449
coverage:
  web: automated
---

# Toggle Active user secara single dan bulk pada berbagai kondisi data

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Siti Rahmawati" Active di semua produk yang dilisensikan, termasuk FAMS
- User "Fajar Ramadhan" berstatus Pending Activation dan belum pernah login
- User "Yanti Kusuma" Active dan punya approval task yang sedang berjalan
- User "Zainal Arifin" Active tanpa approval yang sedang berjalan
- User "Umar Fauzi" Active dan punya approval task yang sedang berjalan
- User "Agus Salim", "Bayu Permana", dan "Candra Wijaya" semuanya Active
- Semua user di atas adalah Login User hasil seeding automation

## Test Steps

### Screening: guard Default User dan akun sendiri

1. Verifikasi Toggle Active pada baris Default User Disabled dengan tooltip "Default User cannot be modified."
2. Verifikasi Toggle Active pada baris akun yang sedang login Disabled dengan tooltip "You can't manage your own account from here."

### Toggle Active single

3. Di User Detail "Siti Rahmawati", matikan Toggle Active per-produk `FAMS`
4. Verifikasi hanya toggle `FAMS` yang OFF, Toggle Active [Global] tetap ON, dan toggle produk lain tetap ON
5. Di User List, klik Toggle Active [Global] pada baris "Siti Rahmawati" untuk mematikannya
6. Verifikasi dialog "Deactivate User" muncul dengan isi "• Siti Rahmawati\nThis will deactivate user across all products. Are you sure you want to deactivate it?"
7. Klik `[Cancel]` pada dialog
8. Verifikasi dialog tertutup dan Toggle Active [Global] "Siti Rahmawati" kembali ON
9. Klik Toggle Active [Global] pada baris "Siti Rahmawati" untuk mematikannya lagi
10. Klik `[Deactivate]` pada dialog
11. Verifikasi toast "Success, user has been deactivated." muncul dan semua toggle per-produk "Siti Rahmawati", termasuk `FAMS`, OFF
12. Klik Toggle Active [Global] pada baris "Siti Rahmawati" untuk menyalakannya
13. Verifikasi dialog "Activate User" muncul dengan isi "• Siti Rahmawati\nThis will activate user across all products. Are you sure you want to activate it?"
14. Klik `[Cancel]` pada dialog
15. Verifikasi dialog tertutup dan Toggle Active [Global] "Siti Rahmawati" tetap OFF
16. Klik Toggle Active [Global] pada baris "Siti Rahmawati" untuk menyalakannya lagi
17. Klik `[Activate]` pada dialog
18. Verifikasi toast "Success, user has been activated." muncul
19. Verifikasi toggle per-produk `FAMS` "Siti Rahmawati" tetap OFF karena dimatikan manual sebelum Global dimatikan, sedangkan toggle produk lain kembali ON
20. Klik Toggle Active [Global] pada baris "Fajar Ramadhan" untuk mematikannya, lalu konfirmasi pada dialog
21. Verifikasi toast "Success, user has been deactivated." muncul dan badge "Pending Activation" tetap tampil bersama status Inactive
22. Klik Toggle Active [Global] pada baris "Yanti Kusuma" untuk mematikannya
23. Verifikasi dialog menampilkan baris tambahan bahwa "Yanti Kusuma" punya approval task yang sedang berjalan dan perlu diselesaikan oleh admin Total Control
24. Klik `[Deactivate]` pada dialog
25. Verifikasi toast "Success, user has been deactivated." muncul

### Bulk Deactivate dan Bulk Activate

26. Centang checkbox "Agus Salim", "Bayu Permana", dan "Candra Wijaya"
27. Klik bulk action `Deactivate`
28. Verifikasi dialog "Deactivate Users" muncul dengan daftar bullet ketiga nama dan isi "They will be deactivated across all products. Are you sure you want to deactivate them?"
29. Klik `[Cancel]` pada dialog
30. Verifikasi dialog tertutup dan ketiga user tetap Active
31. Klik bulk action `Deactivate` lagi, lalu klik `[Deactivate]` pada dialog
32. Verifikasi toast "Success, user has been deactivated." muncul dan ketiga user menjadi Inactive
33. Centang checkbox "Agus Salim", "Bayu Permana", dan "Candra Wijaya" lagi
34. Klik bulk action `Activate`
35. Verifikasi dialog "Activate Users" muncul dengan daftar bullet ketiga nama dan isi "They will be activated across all products. Are you sure you want to activate them?"
36. Klik `[Cancel]` pada dialog
37. Verifikasi dialog tertutup dan ketiga user tetap Inactive
38. Klik bulk action `Activate` lagi, lalu klik `[Activate]` pada dialog
39. Verifikasi toast "Success, user has been activated." muncul dan ketiga user menjadi Active
40. Centang checkbox "Zainal Arifin" dan "Umar Fauzi", lalu klik bulk action `Deactivate`
41. Verifikasi dialog menampilkan baris tambahan bahwa sebagian user terpilih punya approval task yang sedang berjalan dan perlu diselesaikan oleh admin Total Control
42. Klik `[Deactivate]` pada dialog
43. Verifikasi toast "Success, user has been deactivated." muncul

## Notes

- Toggle Active dipisah dari Delete dan Remove Access karena topiknya berbeda dan kondisi datanya bervariasi (`docs/e2e-conventions.md` bagian 3, prinsip 1).
- Langkah 3–19 berantai pada user yang sama ("Siti Rahmawati") supaya TC-GS-USER-43 (state per-produk yang dimatikan manual dipertahankan saat Global dinyalakan kembali) bisa dibuktikan.
- Langkah 40 memakai "Umar Fauzi" dan bukan "Yanti Kusuma" untuk sisi approval TC-GS-USER-449, karena "Yanti Kusuma" sudah Inactive sejak langkah 22–25.
- TC-GS-USER-48, 448, 458, 459, dan 398 (error server yang hanya bisa dipicu mock, serta perilaku tampilan bulk bar) tidak dicakup di sini dan menjadi tanggung jawab lapisan frontend (TC-GS-USER-FE-104, 102, 098, 099, 105).
- Spec ini tidak menghapus data. User seeding yang berubah status dibersihkan atau di-seed ulang sebelum run berikutnya.
