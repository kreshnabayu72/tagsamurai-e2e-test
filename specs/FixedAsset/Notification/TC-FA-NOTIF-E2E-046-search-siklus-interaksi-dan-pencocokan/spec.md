---
id: TC-FA-NOTIF-E2E-046-search-siklus-interaksi-dan-pencocokan
title: "Search Notification Center: Siklus Interaksi, Pencocokan, Enter, dan Trim Spasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-188
  - TC-FA-NOTIF-189
  - TC-FA-NOTIF-190
  - TC-FA-NOTIF-191
coverage:
  web: automated
---

# Search Notification Center: Siklus Interaksi, Pencocokan, Enter, dan Trim Spasi

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi) milik akun aktor, dipulihkan fixture BE pemulih di hook `before` dan `after`. Spec hanya membaca data. Nilai (kata Search, judul item) dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-188: Siklus interaksi Search: reveal, auto-focus, tooltip, clear, dan collapse

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Hover icon Search
3. Verifikasi tooltip `Search` tampil
4. Klik icon Search
5. Verifikasi input Search melebar
6. Verifikasi kursor fokus pada input Search
7. Verifikasi placeholder input Search `Search title, body...`
8. Ketik `repaired` pada input Search tanpa menekan Enter
9. Verifikasi icon `(✕)` muncul pada input Search
10. Verifikasi list belum tersaring (item `Waiting for your approval` masih tampil)
11. Tekan Enter
12. Verifikasi item `Asset has been repaired` tampil pada list
13. Verifikasi list tersaring (item `Waiting for your approval` tidak tampil)
14. Klik icon `(✕)`
15. Verifikasi input Search kosong
16. Verifikasi kursor tetap fokus pada input Search
17. Verifikasi list tetap tersaring (item `Asset has been repaired` tampil dan item `Waiting for your approval` tidak tampil)
18. Tekan Enter pada input kosong
19. Verifikasi list kembali menampilkan semua data (item `Waiting for your approval` tampil)
20. Ketik Search `repaired`, tekan Enter
21. Klik icon `(←)`
22. Verifikasi search box tertutup
23. Verifikasi list langsung reset (item `Waiting for your approval` tampil)
24. Klik icon Search
25. Verifikasi input Search kosong (keyword dikosongkan)
26. Klik icon `(←)` untuk menutup search box

### TC-FA-NOTIF-189: Search mencocokkan Title dan Body secara substring tidak case-sensitive

27. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
28. Ketik Search `REPAIRED`, tekan Enter
29. Verifikasi item `Asset has been repaired` tampil (cocok Title N-03)
30. Ganti isi kotak search dengan `ast-2024-0141`, tekan Enter
31. Verifikasi item yang Body-nya memuat `AST-2024-0141` tampil
32. Ganti isi kotak search dengan `has been repaired`, tekan Enter
33. Verifikasi item `Asset has been repaired` tampil

### TC-FA-NOTIF-190: Search dijalankan saat Enter, bukan saat mengetik

34. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
35. Klik icon Search
36. Ketik `found` pada input Search tanpa menekan Enter
37. Verifikasi list belum tersaring (item `Waiting for your approval` masih tampil)
38. Tekan Enter
39. Scroll sampai akhir list hingga seluruh item termuat
40. Verifikasi list memuat sedikitnya satu item
41. Verifikasi setiap item pada list memuat `found` (item `Waiting for your approval` tidak tampil)

### TC-FA-NOTIF-191: Search men-trim spasi awal dan akhir saat Enter tanpa mengubah isi input

42. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
43. Ketik Search `  repaired  ` (spasi awal dan akhir), tekan Enter
44. Verifikasi isi input Search tetap `  repaired  `
45. Scroll sampai akhir list hingga seluruh item termuat, lalu catat daftar item hasil
46. Ganti isi kotak search dengan `repaired`, tekan Enter
47. Scroll sampai akhir list hingga seluruh item termuat
48. Verifikasi daftar item hasil sama dengan daftar yang dicatat pada langkah 45 (hasil sama dengan pencarian `repaired`)
49. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 27, 34, 42, 49 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 24 dan 26 (membuka lalu menutup input Search untuk membaca keyword sesudah `(←)`), 35 (membuka input Search), 39, 45, 47 (memuat seluruh item agar asersi universal mencakup semua item), 20 (mengisi ulang keyword untuk TC-188 langkah 8).
- Asersi tambahan di luar Expected TC (S-03): langkah 10, 13, 37 (item pembanding sebelum dan sesudah penyaringan, 8b butir 2), langkah 40 (item pembanding sebelum asersi universal), langkah 25 (keyword kosong sesudah `(←)`, klausa "mengosongkan keyword" TC-188 butir e).
- Urutan langkah 44 sebelum 48 menyimpang dari urutan Expected TC-191 (butir b sebelum a) karena `Verifikasi` isi input harus dilakukan sebelum isi diganti (8b butir 5).
- Topik Search dipisah dari spec 052 dan 053 meski memakai seed N-01 sampai N-37 yang sama: objek ujinya perilaku dasar Search (siklus input, pencocokan, Enter, trim), seed hanya dibaca, dan tiap blok diawali reset lewat `[Show All]`, sehingga tidak ada keadaan yang dibawa antar spec.
- Spec ini di atas sekitar 35 langkah (49 langkah): keempat TC satu topik (perilaku dasar Search), memakai seed N-01 sampai N-37 yang sama, dan tiap blok diawali reset lewat `[Show All]` sehingga berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-188 butir c menulis "list TETAP tersaring" dan butir d "Enter pada input kosong me-reset list" tanpa menyebut item yang menjadi pembanding; spec memakai `Asset has been repaired` (N-03) dan `Waiting for your approval` (N-01) dari Pre-setup #17.
  - TC-189 langkah 3 menyebut "item yang Body-nya memuat `AST-2024-0141`" tanpa judul item; spec tidak menyebut judul.
  - TC-190 butir b ("list tersaring hanya item yang memuat `found`") tidak menyebut judul item hasil; spec memakai asersi universal terhadap seluruh item yang dimuat.
