---
id: TC-GS-USER-E2E-002-create-users-success-flow-stay-open
title: Buat user dengan Access berbeda, field opsional, dan Temporary User dalam satu sesi modal
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-13
  - TC-GS-USER-20
  - TC-GS-USER-469
  - TC-GS-USER-471
  - TC-GS-USER-473
  - TC-GS-USER-191
  - TC-GS-USER-440
  - TC-GS-USER-341
  - TC-GS-USER-489
  - TC-GS-USER-468
  - TC-GS-USER-470
  - TC-GS-USER-472
  - TC-GS-USER-474
  - TC-GS-USER-476
  - TC-GS-USER-420
  - TC-GS-USER-65
  - TC-GS-USER-346
  - TC-GS-USER-21
  - TC-GS-USER-143
  - TC-GS-USER-405
coverage:
  web: automated
---

# Buat user dengan Access berbeda, field opsional, dan Temporary User dalam satu sesi modal

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Client berlisensi Fixed Asset (FAMS)
- Position "Staff" dan Division "Finance" ada di master data
- Custom Field "Blood Type" didefinisikan sebagai Required, sehingga setiap Create mengisinya
- Berkas foto berukuran di bawah 1MB tersedia
- Kolom Toggle Active, Position, Division, Employee ID, Access, Temporary User, Temporary Until, dan TAG terlihat lewat Setup Column
- Permintaan Create untuk user pertama ditunda, dan percobaan pertamanya dibuat gagal dengan error server

## Test Steps

### User 1: semua field terisi, Access Global Settings

1. Klik `[+ User]` untuk membuka modal Create
2. Centang "Stay on this form after submitting"
3. Isi First Name "Budi", Last Name "Santoso", Email unik, Position "Staff", Division "Finance", Employee ID unik, dan "Blood Type"
4. Unggah foto berukuran di bawah 1MB dan pilih Access "Global Settings" saja
5. Klik `[Submit]` saat permintaan Create gagal dengan error server
6. Verifikasi `[Submit]` menampilkan spinner loading dan Disabled selama permintaan berjalan, lalu aktif kembali setelah gagal
7. Verifikasi modal tetap terbuka dengan nilai yang sudah diisi
8. Klik dua kali `[Submit]` dengan cepat saat permintaan Create berhasil
9. Verifikasi `[Submit]` menampilkan spinner loading dan Disabled selama permintaan berjalan
10. Verifikasi toast sukses "User created successfully." muncul dan modal tetap terbuka dengan form kosong

### User 2: Access FAMS, hanya field wajib, nama 120 karakter

11. Isi First Name tepat 120 karakter, Last Name tepat 120 karakter, Email unik, Division "Finance", dan "Blood Type"
12. Biarkan Position, Employee ID, foto, Set as Temporary User, dan User TAG tidak tersentuh
13. Pilih Access "FAMS" saja
14. Klik `[Submit]`
15. Verifikasi toast sukses "User created successfully." muncul dan modal tetap terbuka dengan form kosong

### User 3: Temporary User, menutup modal

16. Isi First Name, Last Name, dan Email yang unik, Division "Finance", dan "Blood Type"
17. Pilih Access "Global Settings" saja
18. Centang `[x] Set as Temporary User` dan biarkan Temporary Until kosong
19. Klik `[Submit]` dan verifikasi error inline "Temporary Until must not be empty" muncul serta form tidak terkirim
20. Pilih Temporary Until hari ini + 7 hari
21. Hapus centang "Stay on this form after submitting"
22. Klik `[Submit]`
23. Verifikasi toast sukses "User created successfully." muncul dan modal tertutup

### Verifikasi di User List

24. Verifikasi User List memuat tepat 1 baris untuk User 1
25. Verifikasi User 1 menampilkan badge "Pending Activation", Toggle Active [Global] ON, role User Basic, dan tepat 1 badge Access dark "Global Settings"
26. Verifikasi User 1 menampilkan Position "Staff", Division "Finance", Employee ID sesuai input, Temporary User No, Temporary Until "—", TAG "—", dan thumbnail foto yang diunggah, bukan avatar inisial
27. Verifikasi User 2 menampilkan tepat 1 badge Access dark "Fixed Asset", bukan "FAMS", dan Toggle Active [Global] ON
28. Verifikasi User 2 menampilkan Position "—", Employee ID "—", TAG "—", Temporary User No, Temporary Until "—", dan avatar inisial default
29. Buka User Detail User 2, buka Tab Role, dan verifikasi role FAMS adalah "User Basic"
30. Verifikasi User 3 menampilkan Temporary User Yes dan Temporary Until berupa tanggal yang dipilih, bukan "—"
31. Buka User Detail User 3 dan verifikasi tampil "Temporary until [date]" dengan tanggal yang dipilih

### Audit log User 1

32. Buka Changelog User 1
33. Verifikasi ada baris dengan Action "Create", Field "Name", Old Value "—", New Value "Budi Santoso", dan Modified By admin yang login
34. Buka System Log admin yang login (User Detail admin, Tab System Log)
35. Verifikasi ada baris Create, Object User, Name "Budi Santoso", Field "Name", Old Value "—", New Value "Budi Santoso"
36. Buka Global Settings > Activity Log dan verifikasi baris Create yang sama ada dengan Modified By admin yang login
37. Buka User Log admin yang login dan verifikasi hanya memuat event login dan sesi, tanpa entri Create

## Notes

- Satu spec mencakup satu sesi modal. "Stay on this form after submitting" tetap tercentang untuk User 1 dan 2 supaya modal hanya dibuka sekali, dan dihapus centangnya untuk User 3 supaya submit terakhir menutup modal.
- Script tidak boleh mengasumsikan checkbox Stay mempertahankan statusnya setelah modal ditutup.
- Error server di langkah 5 tidak bisa dipicu dengan aman di backend nyata, jadi script menyimulasikannya. Intersepsi hanya boleh memengaruhi user pertama dan harus dilepas sesudahnya. Kasus kegagalan Create dicakup juga di `TC-GS-USER-E2E-120-create-gagal-server` (`Mode: mock`).
- TC-GS-USER-420 terbagi di dua spec. Penerimaan tepat 120 karakter dicakup di sini dan penolakan 121 karakter dicakup di TC-GS-USER-E2E-001.
- TC-GS-USER-13 juga mengharapkan email undangan terkirim. Pengiriman email berada di luar browser, jadi spec ini tidak mengujinya. TC itu juga mengharapkan tidak ada notifikasi in-app untuk user lain, yang butuh sesi user kedua dan tidak dicakup di sini.
- Klik ganda di langkah 8 sensitif terhadap waktu. Script harus menunda respons Create secara deterministik.
- Ketiga user harus dihapus saat pembersihan, meski spec gagal di tengah jalan.
- TC-GS-USER-143 dan 405: Create tercatat di Changelog, System Log aktor, dan Activity Log (parity penuh, user.md bagian 8.6), tetapi tidak di User Log.
