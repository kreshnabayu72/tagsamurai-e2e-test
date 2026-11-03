---
id: TC-FA-LIC-E2E-024-banner-renewal-muat-ulang-saat-pindah-tab-fokus-jendela
title: "Banner Renewal: Muat Ulang saat Pindah Tab, Fokus Jendela, dan Tab Browser Baru"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-475
  - TC-FA-LIC-476
  - TC-FA-LIC-479
coverage:
  web: automated
---

# Banner Renewal: Muat Ulang saat Pindah Tab, Fokus Jendela, dan Tab Browser Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Kelas multi-konteks (tab atau jendela): tab browser kedua pada login yang sama dipakai untuk memindahkan fokus dan membuka License; tab kedua adalah objek uji (perilaku banner saat fokus kembali dan di tab baru), bukan pemicu.
- Jumlah panggilan ke endpoint banner dapat dihitung lewat `Spectra.intercept()` (Pre-setup #15).
- Jam browser (klien) dikendalikan lewat fake timer (disediakan tim FE) untuk memenuhi jeda 60 detik dan jeda idle; jam server tidak digeser.
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-475: Throttle muat ulang banner: buka halaman selalu memanggil; pindah tab/fokus memakai jeda 60 detik

1. Atur tanggal fixture hari ini ke `01/12/26` lewat fixture BE
2. Pasang penghitung panggilan endpoint banner lewat intercept dan kendalikan jam browser lewat fake timer
3. Buka License > All License (panggilan 1)
4. Catat jumlah panggilan endpoint banner
5. Majukan jam browser 30 detik
6. Klik Tab `Allocation Quota`
7. Verifikasi jumlah panggilan endpoint banner tidak bertambah dari yang dicatat (hasil terakhir dipakai)
8. Majukan jam browser hingga detik ke-59 sejak panggilan 1
9. Buka tab browser kedua pada login yang sama
10. Pindahkan fokus ke tab browser kedua, lalu fokuskan ulang jendela License
11. Verifikasi jumlah panggilan endpoint banner tidak bertambah dari yang dicatat (hasil terakhir dipakai)
12. Majukan jam browser 1 detik (detik ke-60 sejak panggilan 1)
13. Pindahkan fokus ke tab browser kedua, lalu fokuskan ulang jendela License tepat pada detik ke-60
14. Verifikasi jumlah panggilan endpoint banner bertambah satu (jeda minimal 60 detik terpenuhi; hanya fokus yang lebih cepat dari 60 detik dilewati)
15. Catat jumlah panggilan endpoint banner
16. Majukan jam browser 5 detik
17. Buka halaman License baru
18. Verifikasi jumlah panggilan endpoint banner bertambah satu (pembukaan halaman tidak tunduk pada jeda)

### TC-FA-LIC-476: Banner dimuat ulang saat jendela kembali fokus dan perubahan stage muncul tanpa reload manual

19. Atur tanggal fixture hari ini ke `01/12/26`; stage Notice lewat fixture BE
20. Buka License > All License
21. Atur tanggal fixture hari ini ke `24/12/26`; stage Reminder di sisi server lewat fixture BE
22. Majukan jam browser 61 detik lewat fake timer
23. Pindahkan fokus ke tab browser kedua, lalu fokuskan ulang jendela License
24. Verifikasi banner berganti ke stage Reminder tanpa reload manual
25. Verifikasi pergantian banner tanpa skeleton atau kedip

### TC-FA-LIC-479: Dismiss bertahan setelah refresh dan di tab browser baru pada login yang sama, hilang saat login baru

26. Tutup tab browser kedua
27. Atur tanggal fixture hari ini ke `01/12/26`; stage Notice lewat fixture BE
28. Buka License > All License
29. Klik `[×]` pada banner Notice
30. Tekan `F5`
31. Verifikasi Tabs Bar tampil
32. Verifikasi banner tetap tertutup setelah `F5`
33. Buka tab browser baru pada login yang sama, lalu buka License > All License
34. Verifikasi Tabs Bar tampil di tab baru
35. Verifikasi banner tetap tertutup di tab baru
36. Tutup tab browser baru
37. Logout
38. Login kembali sebagai Total Control dengan `Spectra.env.FA_TC_PASSWORD`
39. Buka License > All License
40. Verifikasi banner Notice tampil lagi setelah login baru

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): penyetelan tanggal fixture, pemasangan intercept dan fake timer, "Catat jumlah panggilan", "Majukan jam browser" (TC menulis "dalam 30 detik", "detik ke-59", "detik ke-60", dan "lebih dari 60 detik", dipenuhi dengan fake timer, bukan menunggu), "Buka tab browser kedua" dan "Tutup tab browser kedua" (tab kedua dipakai memindahkan fokus pada TC-FA-LIC-475 dan TC-FA-LIC-476; TC tidak menyebut cara memfokuskan ulang jendela, lihat Temuan untuk QA), "Tutup tab browser baru", serta Logout dan login kembali akun yang sama sesuai TC-FA-LIC-479 (bukan Ganti akun).
- Spec kelas multi-konteks (tab/jendela); tab kedua bukan pemicu sehingga `P-2` tidak dipakai, dan tidak ada simulator USB sehingga `P-7` tidak dipakai.
- Asersi "banner tetap tertutup" didahului `Verifikasi Tabs Bar tampil` sebagai anchor positif.
- Spec di atas 35 langkah (40 langkah): ketiganya satu kelas harness (multi-konteks tab/jendela) atas perilaku muat ulang dan dismiss banner yang sama, dan setiap blok menyetel tanggal fixture sendiri serta berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-LIC-475 langkah 3 sampai 5 tidak menyebut cara "memfokuskan ulang jendela" (fokus ke jendela lain); spec memakai tab browser kedua pada login yang sama, dibuka sebagai langkah penghubung sebelum fokus dipindahkan pertama kali dan ditutup sesudah TC-FA-LIC-476.
  - TC-FA-LIC-476 Expected memuat "tanpa reload manual" tanpa penanda teknis; spec mengasersinya sebagai tidak ada muat ulang halaman selama langkah berjalan.
