---
id: TC-GS-USER-E2E-009-remove-access-user
title: Remove Access lewat Modal Edit pada berbagai kondisi data
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-52
  - TC-GS-USER-51
  - TC-GS-USER-31
  - TC-GS-USER-49
  - TC-GS-USER-352
  - TC-GS-USER-425
  - TC-GS-USER-351
  - TC-GS-USER-387
  - TC-GS-USER-50
coverage:
  web: automated
---

# Remove Access lewat Modal Edit pada berbagai kondisi data

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Sari Handayani" punya Access `[FAMS]` saja (satu Access)
- User "Eka Wijaya" punya Access `[Global Settings, FAMS]`, tanpa aset atau approval di FAMS
- User "Denny Kurniawan" punya Access `[Global Settings, FAMS]`, Borrowed Asset aktif, dan approval task yang sedang berjalan, keduanya di FAMS
- User "Rendi Saputra" punya Access `[Global Settings, FAMS]` dan sedang `access_level = Total Control` di Role & Permission
- Semua user di atas adalah Login User hasil seeding automation

## Test Steps

### Screening: guard Default User

1. Buka Modal Edit pada baris Default User
2. Verifikasi checkbox Access Disabled dengan tooltip "Default User cannot be modified."
3. Klik `✕` untuk menutup modal

### Validasi yang diblokir

4. Buka Modal Edit "Sari Handayani"
5. Hilangkan centang `FAMS` di field Access, satu-satunya Access yang tersisa
6. Klik `[Save]`
7. Verifikasi error inline "Access must not be empty" muncul, Modal Edit tetap terbuka, tidak ada dialog Remove Access, dan Access "Sari Handayani" tidak berubah
8. Klik `✕` dan pilih `[Leave]` pada dialog unsaved changes

### Remove Access berhasil

9. Buka Modal Edit "Eka Wijaya"
10. Hilangkan centang `FAMS` di field Access
11. Klik `[Save]`
12. Verifikasi tidak ada dialog tambahan, toast "Success, user has been updated." muncul, dan Access "Eka Wijaya" menjadi `[Global Settings]`
13. Buka Modal Edit "Denny Kurniawan"
14. Hilangkan centang `FAMS` di field Access
15. Klik `[Save]`
16. Verifikasi dialog peringatan muncul yang menyebut bahwa mencabut akses Fixed Asset akan berdampak pada borrowed asset dan pending approval "Denny Kurniawan", data historis tetap tersimpan, tetapi user kehilangan akses fungsional
17. Klik `[Cancel]` pada dialog
18. Verifikasi Modal Edit tetap terbuka dan centang `FAMS` di field Access masih hilang (belum tersimpan)
19. Klik `[Save]` lagi
20. Verifikasi dialog peringatan yang sama muncul
21. Konfirmasi dialog
22. Verifikasi toast "Success, user has been updated." muncul dan Access "Denny Kurniawan" menjadi `[Global Settings]`
23. Buka Modal Edit "Rendi Saputra"
24. Hilangkan centang `Global Settings` di field Access
25. Klik `[Save]`
26. Verifikasi dialog peringatan muncul dengan isi "• Rendi Saputra\nThis user currently has Total Control in Role & Permission. Removing Global Settings access will also revoke it. Are you sure you want to remove it?"
27. Konfirmasi dialog
28. Verifikasi toast "Success, user has been updated." muncul, Access "Rendi Saputra" menjadi `[FAMS]`, dan `access_level` tidak lagi Total Control
29. Buka Global Settings > Role & Permission, Tab Total Control
30. Verifikasi "Rendi Saputra" tidak lagi muncul di Tab Total Control

## Notes

- Remove Access dipisah dari Delete dan Toggle Active karena topiknya berbeda dan kondisi datanya bervariasi (`docs/e2e-conventions.md` bagian 3, prinsip 1).
- Remove Access tidak punya row action. Titik masuknya adalah menghilangkan centang Access di Modal Edit (`GAP-239`).
- TC-GS-USER-49 dan TC-GS-USER-352 menjelaskan hasil yang sama (tanpa dialog tambahan) dan diverifikasi bersama pada langkah 9–12.
- Langkah 8 memakai `[Leave]` karena Modal Edit sedang dirty. `✕` pada form yang berisi perubahan memunculkan dialog unsaved changes.
- TC-GS-USER-387 dan TC-GS-USER-50 menjelaskan peringatan khusus Global Settings yang sama dan diverifikasi bersama pada langkah 23–30. TC-GS-USER-50 dikoreksi pada 2026-09-29 karena user yang hanya punya Access `[Global Settings]` tidak bisa kehilangan Global Settings (minimal 1 Access, `TC-GS-USER-51`), jadi user "Rendi Saputra" memakai `[Global Settings, FAMS]`.
- TC-GS-USER-53 (error server yang hanya bisa dipicu mock) tidak dicakup di sini dan menjadi tanggung jawab lapisan frontend (TC-GS-USER-FE-110).
- Spec ini mengubah data user seeding secara permanen (Access berkurang, `access_level` dicabut), jadi user harus di-seed ulang sebelum run berikutnya.
