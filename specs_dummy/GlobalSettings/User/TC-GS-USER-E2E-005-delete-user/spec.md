---
id: TC-GS-USER-E2E-005-delete-user
title: Hapus user lewat row action, lalu Select All dan Bulk Delete
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-36
  - TC-GS-USER-37
  - TC-GS-USER-433
  - TC-GS-USER-33
  - TC-GS-USER-353
  - TC-GS-USER-453
  - TC-GS-USER-34
  - TC-GS-USER-35
  - TC-GS-USER-258
  - TC-GS-USER-38
  - TC-GS-USER-434
  - TC-GS-USER-145
  - TC-GS-USER-406
  - TC-GS-USER-164
  - TC-GS-USER-168
  - TC-GS-USER-367
coverage:
  web: automated
---

# Hapus user lewat row action, lalu Select All dan Bulk Delete

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Environment adalah environment khusus automation yang disiapkan dan diisolasi tim FE, sehingga Select All dan Bulk Delete boleh bekerja pada seluruh hasilnya
- Spec ini harus dijalankan sesudah spec lain selesai dan tidak paralel dengan spec lain, karena Select All lalu Bulk Delete menghapus semua user kecuali Default User dan akun yang login, termasuk user seeding milik spec lain
- Ada lebih dari 10 user yang tersebar di minimal 2 halaman User List dengan status campuran Active dan Inactive
- User "Budi Santoso" ada, tanpa borrowed asset, tanpa pending approval, dan tanpa foto profil
- User "Doni Pratama" ada dan punya Borrowed Asset aktif di Fixed Asset (FAMS)
- User "Wulan Setiawan" ada dan punya foto profil kustom (bukan avatar default)
- User "Gilang Pratama", "Hesti Wulandari", dan "Ivan Setiadi" ada, semuanya Active tanpa borrowed asset dan tanpa pending approval
- Semua user di atas adalah Login User hasil seeding automation
- User "Wulan Setiawan" punya satu foto aktif dan dua foto historis di Recycle Bin File Manager (total tiga foto)
- "Doni Pratama" terlibat di Fixed Asset sebagai peminjam (Borrow), assignee (Assignment), dan approver (Approvals, minimal satu riwayat)
- Email "Budi Santoso" diketahui dan belum pernah dipakai user lain

## Test Steps

### Screening: guard Default User dan akun sendiri

1. Verifikasi row action `Delete` pada baris Default User Disabled dengan tooltip "Default User cannot be modified."
2. Verifikasi row action `Delete` pada baris akun yang sedang login Disabled dengan tooltip "You can't manage your own account from here."

### Delete satu user lewat row action

3. Klik `Delete` pada baris "Budi Santoso"
4. Verifikasi dialog berjudul "Delete User" dengan isi "• Budi Santoso\nHistorical transaction data will be preserved.\nThis action cannot be undone. Are you sure you want to delete it?" serta tombol `[Cancel]` dan `[Delete]`
5. Klik `[Cancel]` pada dialog
6. Verifikasi dialog tertutup dan baris "Budi Santoso" masih ada
7. Klik `Delete` pada baris "Budi Santoso" lagi
8. Klik dua kali berturut-turut dengan cepat `[Delete]` pada dialog
9. Verifikasi `[Delete]` langsung nonaktif dan menampilkan loading sesudah klik pertama, dan klik kedua tidak memicu request tambahan
10. Verifikasi toast "Success, user has been deleted." muncul, hanya satu user yang terhapus tanpa error atau efek ganda, dan tidak ada error terkait file foto
11. Verifikasi baris "Budi Santoso" tidak lagi muncul di User List
12. Klik `Delete` pada baris "Doni Pratama"
13. Verifikasi dialog menampilkan peringatan tambahan bahwa "Doni Pratama" masih punya aset terkait dan disarankan mengembalikannya dulu, sementara `[Delete]` tetap aktif
14. Klik `[Delete]` pada dialog
15. Verifikasi toast "Success, user has been deleted." muncul dan baris "Doni Pratama" tidak lagi muncul di User List
16. Klik `Delete` pada baris "Wulan Setiawan", lalu klik `[Delete]` pada dialog
17. Verifikasi toast "Success, user has been deleted." muncul
18. Verifikasi foto profil "Wulan Setiawan" terhapus permanen dari storage, bukan sekadar disembunyikan dari list

### Bulk Delete lewat checkbox

19. Centang checkbox "Gilang Pratama", "Hesti Wulandari", dan "Ivan Setiadi"
20. Klik bulk action `Delete`
21. Verifikasi dialog konfirmasi menampilkan daftar bullet ketiga nama
22. Klik `[Cancel]` pada dialog
23. Verifikasi dialog tertutup, ketiga baris masih tercentang, bulk action bar masih tampil, dan tidak ada baris yang terhapus
24. Klik bulk action `Delete` lagi, lalu klik `[Delete]` pada dialog
25. Verifikasi toast "Success, user has been deleted." muncul
26. Verifikasi ketiga baris tidak lagi muncul di User List

### Select All lalu Bulk Delete

27. Verifikasi tombol "Select All ({N} records)" menampilkan `{N}` sama dengan total user yang cocok dengan filter aktif
28. Klik "Select All ({N} records)"
29. Verifikasi seluruh baris di semua halaman tercentang, kecuali baris Default User dan baris akun yang login yang tetap tidak tercentang
30. Verifikasi tombol berubah menjadi "Unselect All"
31. Klik bulk action `Delete`
32. Verifikasi dialog konfirmasi menampilkan daftar user yang terpilih
33. Klik `[Delete]` pada dialog
34. Verifikasi toast "Success, user has been deleted." muncul
35. Verifikasi seluruh baris yang tadi terpilih tidak lagi muncul di User List, kecuali Default User dan akun yang login

### Verifikasi log, File Manager, dan FAMS setelah Delete

36. Buka Changelog dari toolbar User List dan filter ke "Budi Santoso"
37. Verifikasi riwayat "Budi Santoso" tetap terlihat walau barisnya sudah tidak ada di User List, termasuk baris Action "Delete", Field "Name", Old Value "Budi Santoso", New Value "—", dan Modified By admin yang login
38. Buka Global Settings > Activity Log dan verifikasi entri Delete untuk "Wulan Setiawan" melampirkan detail photosDeletedCount = 3 (satu foto aktif dan dua foto historis)
39. Buka File Manager dan Recycle Bin, lalu verifikasi ketiga foto "Wulan Setiawan" tidak ada di keduanya (sudah hard-delete, tidak menunggu auto-purge 30 hari)
40. Buka Fixed Asset > Borrow, tab Borrowed (By Borrower), dan cari "Doni Pratama"
41. Verifikasi nama "Doni Pratama" tetap tampil
42. Buka Fixed Asset > Assignment dan verifikasi nama "Doni Pratama" tetap tampil di kolom Assignee / Custodian
43. Buka Fixed Asset > Approvals, tab History, dan verifikasi nama "Doni Pratama" tetap tampil sebagai approver
44. Klik `[+ User]` dan buat user baru "Budi Pengganti" dengan email yang sama dengan email "Budi Santoso" sebelum dihapus
45. Verifikasi Create berhasil tanpa error email duplikat
46. Buka Changelog dan Activity Log "Budi Santoso" lama, lalu verifikasi email lama tetap tercatat dan tidak bentrok dengan "Budi Pengganti"
47. Hapus "Budi Pengganti" lewat row action `Delete` dan konfirmasi dialog

## Notes

- Delete user dipisah dari Toggle Active dan Remove Access karena topiknya berbeda dan kondisi datanya bervariasi (`docs/e2e-conventions.md` bagian 3, prinsip 1).
- Bulk Delete dipakai dalam dua cara: lewat checkbox pada user tertentu (langkah 19–26, TC-GS-USER-434 untuk jalur Cancel dan TC-GS-USER-38 untuk jalur konfirmasi), dan lewat Select All (langkah 27–35). Jalur Cancel tidak diulang di Select All karena dialognya sama.
- Select All lalu Bulk Delete (langkah 27–35) ada di akhir karena menghapus semua user kecuali Default User dan akun yang login. Sebagai efek sampingnya, langkah ini juga membersihkan user seeding yang masih tersisa.
- TC-GS-USER-258 dan TC-GS-USER-38 dijalankan lewat satu klik Select All yang sama (langkah 27–30), karena keduanya menjelaskan aksi yang sama.
- TC-GS-USER-33, 353, dan 453 memakai satu user ("Budi Santoso") karena user tanpa foto dan tanpa keterikatan data cukup untuk ketiganya.
- Bila spec gagal sebelum langkah 27, Select All dan Bulk Delete tidak berjalan, sehingga user seeding yang tersisa harus dibersihkan satu per satu.
- TC-GS-USER-39, 40, 451, dan 452 (error, race, atau perubahan izin di tengah aksi yang hanya bisa dipicu mock) tidak dicakup di sini dan menjadi tanggung jawab lapisan frontend (TC-GS-USER-FE-082, 083, 084, 085).
- Langkah verifikasi setelah Delete ditaruh sesudah Select All karena tidak butuh baris yang masih ada: Changelog, Activity Log, File Manager, dan Fixed Asset menyimpan snapshot user yang sudah terhapus (TC-GS-USER-145, 164, 168). Pembuatan "Budi Pengganti" (TC-GS-USER-367) dihapus lagi di langkah terakhir supaya tidak meninggalkan data.
