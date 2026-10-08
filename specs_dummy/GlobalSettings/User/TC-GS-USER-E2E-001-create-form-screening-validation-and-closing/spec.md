---
id: TC-GS-USER-E2E-001-create-form-screening-validation-and-closing
title: Screening form Create, validasi, dan perilaku penutupan modal
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-14
  - TC-GS-USER-15
  - TC-GS-USER-25
  - TC-GS-USER-457
  - TC-GS-USER-16
  - TC-GS-USER-17
  - TC-GS-USER-19
  - TC-GS-USER-192
  - TC-GS-USER-420
  - TC-GS-USER-18
  - TC-GS-USER-340
  - TC-GS-USER-347
  - TC-GS-USER-482
  - TC-GS-USER-431
  - TC-GS-USER-22
  - TC-GS-USER-487
  - TC-GS-USER-169
coverage:
  web: automated
---

# Screening form Create, validasi, dan perilaku penutupan modal

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Position "Intern" ada di master data dan belum dipakai user mana pun
- Division "Finance" ada di master data
- Custom Field "Blood Type" didefinisikan sebagai Required
- User "Doni Pratama" sudah ada dan emailnya diketahui
- Employee ID "EMP-001" sudah dipakai user lain di entity ini
- Ada satu Non-Login User dan emailnya diketahui

## Test Steps

### Screening

1. Buka Filter Panel di User List, buka dropdown Position, lalu verifikasi "Intern" tidak ada dalam daftar
2. Tutup Filter Panel
3. Klik `[+ User]` untuk membuka modal Create
4. Verifikasi form menampilkan Photo (opsional), First Name, Last Name, Email, Position (opsional), Division, Employee ID (opsional), grup checkbox Access, User TAG (opsional), Set as Temporary User, dan Custom Field "Blood Type"
5. Verifikasi First Name, Last Name, Email, Division, dan Access ditandai wajib diisi
6. Verifikasi footer menampilkan checkbox "Stay on this form after submitting", `[Clear Field]`, dan `[Submit]`, serta tidak ada tombol `[Cancel]`
7. Verifikasi opsi Access memuat setiap produk yang dilisensikan untuk Client ditambah "Global Settings"
8. Buka dropdown Position di modal dan verifikasi "Intern" ada dalam daftar
9. Centang `[x] Set as Temporary User`, verifikasi field Temporary Until muncul, lalu hapus centang

### Validasi

10. Klik `[Submit]` tanpa mengisi apa pun
11. Verifikasi submit diblokir dan error inline muncul: "First Name must not be empty", "Last Name must not be empty", "Email must not be empty", "Division must not be empty", "Access must not be empty", dan "Blood Type must not be empty" untuk Custom Field Required
12. Isi First Name, Last Name, Division "Finance", Email "budi.santoso@@invalid", dan pilih Access "Global Settings"
13. Klik `[Submit]` dan verifikasi error inline "Invalid email format" muncul serta form tidak terkirim
14. Ganti Email dengan email valid yang unik lalu hapus centang semua opsi Access
15. Klik `[Submit]` dan verifikasi error inline "Access must not be empty" muncul serta form tidak terkirim
16. Pilih Access "Global Settings" sehingga semua field valid kecuali Custom Field "Blood Type" yang tetap kosong
17. Klik `[Submit]` dan verifikasi error inline "Blood Type must not be empty" muncul sebagai satu-satunya error serta form tidak terkirim
18. Isi "Blood Type", lalu ketik "Budi 😊" ke First Name dan Last Name, dan verifikasi emoji tidak pernah masuk ke field serta tidak ada error yang muncul
19. Ketik "Budi-O'Neil" ke First Name dan Last Name dan verifikasi simbol diterima dan tetap ada di kedua field
20. Kembalikan nilai valid untuk First Name dan Last Name
21. Untuk masing-masing First Name, Last Name, dan Employee ID, masukkan 121 karakter sementara field lain tetap valid, verifikasi error inline "Max. 120 characters" langsung muncul saat mengetik, lalu klik `[Submit]` dan verifikasi submit diblokir
22. Kembalikan nilai maksimal 120 karakter
23. Ganti Email dengan email milik "Doni Pratama" yang sudah ada
24. Verifikasi error inline "Email already exists" langsung muncul saat mengetik (debounce sekitar 500 ms), lalu klik `[Submit]` dan verifikasi submit diblokir serta data tidak tersimpan
25. Ganti Email dengan email valid yang unik dan masukkan Employee ID "EMP-001"
26. Verifikasi error inline "Employee ID already exists" langsung muncul saat mengetik (debounce sekitar 500 ms), lalu klik `[Submit]` dan verifikasi submit diblokir serta data tidak tersimpan
27. Klik `[Clear Field]` dan verifikasi semua field, termasuk Custom Field "Blood Type", dikosongkan dan modal tetap terbuka
28. Klik `[Submit]` pada form kosong untuk memunculkan error validasi dan verifikasi border merah serta error inline muncul
29. Klik `[Clear Field]` dan verifikasi semua field dikosongkan, border merah dan error inline hilang, dan modal tetap terbuka

### Penutupan modal

30. Isi First Name dengan sebuah nilai
31. Klik `✕`
32. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" muncul dengan `[Leave]` dan `[Cancel]`
33. Klik `[Cancel]` pada dialog dan verifikasi dialog tertutup, modal tetap terbuka, dan First Name masih berisi nilainya
34. Klik `✕` lagi lalu klik `[Leave]` pada dialog
35. Verifikasi modal tertutup dan tidak ada user baru di User List dari submit mana pun di atas
36. Klik `[+ User]` lagi dan verifikasi semua field kosong, artinya tidak ada draft yang tersimpan
37. Klik `✕` tanpa mengisi field apa pun
38. Verifikasi modal langsung tertutup dan dialog unsaved changes tidak muncul

### Email yang sama dengan Non-Login User

39. Klik `[+ User]` lagi dan isi semua field wajib dengan nilai valid
40. Ganti Email dengan email Non-Login User yang sudah ada
41. Verifikasi error inline "Email already exists" langsung muncul saat mengetik, lalu klik `[Submit]` dan verifikasi submit diblokir serta data tidak tersimpan
42. Klik `✕` lalu klik `[Leave]` pada dialog

## Notes

- Satu spec mencakup dua sesi modal. Langkah 3 sampai 34 berjalan di sesi pertama yang diakhiri dengan `[Leave]`. Langkah 36 sampai 38 berjalan di sesi kedua, karena kasus penutupan tanpa perubahan butuh modal yang baru dibuka.
- TC-GS-USER-15 terbagi di dua spec. Bagian Client dicakup di sini dan bagian Principal dicakup di TC-GS-USER-E2E-003.
- TC-GS-USER-420 terbagi di dua spec. Penolakan 121 karakter dicakup di sini dan penerimaan tepat 120 karakter dicakup di TC-GS-USER-E2E-002.
- Custom Field Required divalidasi seperti field wajib lain, sehingga errornya juga muncul saat submit kosong (langkah 11) dan diverifikasi sendirian di langkah 17. Teksnya mengikuti pola global "[Field] must not be empty" yang muncul setelah Submit (prd-conventions.md, konvensi pesan error), dan TC-GS-USER-16 serta TC-GS-USER-25 menyebutnya secara eksplisit.
- Aksi menutup adalah `✕` di header. `Esc` juga menutup modal. Modal Create tidak punya tombol `[Cancel]` (prd-conventions.md bagian 24.1). `[Cancel]` hanya ada di dialog unsaved changes.
- Aturan emoji mengikuti prd-conventions.md "Karakter yang Diizinkan (Name Fields)": hanya emoji yang diblokir, simbol diizinkan.
- Spec ini tidak membuat data, sehingga tidak butuh pembersihan.
- TC-GS-USER-169: batasan keunikan email mencakup Login dan Non-Login User dalam satu tabel, sehingga langkah untuk kasus ini berjalan di sesi modal ketiga di akhir.
