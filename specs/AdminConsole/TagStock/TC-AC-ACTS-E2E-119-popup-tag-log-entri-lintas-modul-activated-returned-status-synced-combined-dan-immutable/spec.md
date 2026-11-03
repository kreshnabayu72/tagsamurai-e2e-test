---
id: TC-AC-ACTS-E2E-119-popup-tag-log-entri-lintas-modul-activated-returned-status-synced-combined-dan-immutable
title: "Popup TAG Log Entri Lintas Modul: Activated, Returned to Stock, Delete Jalur B, Status Synced, Combined dan Separated, Delete Stock, dan Entri Immutable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-973
  - TC-AC-ACTS-974
  - TC-AC-ACTS-975
  - TC-AC-ACTS-976
  - TC-AC-ACTS-978
  - TC-AC-ACTS-979
  - TC-AC-ACTS-980
coverage:
  web: automated
---

# Popup TAG Log Entri Lintas Modul: Activated, Returned to Stock, Delete Jalur B, Status Synced, Combined dan Separated, Delete Stock, dan Entri Immutable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: Detail SKU `RFID-ASSET-CORE-R5` > Tab Available (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Unit milik spec disiapkan seeding fixture BE (disediakan tim FE/BE) pada SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12): unit baru diaktivasi Client `PT Maju Bersama` via Activate TAG Official (TC-AC-ACTS-973), unit Jalur A yang aktivasinya dihapus Client (TC-AC-ACTS-974), unit In Use Jalur B (TC-AC-ACTS-975), unit In Use Status Available (TC-AC-ACTS-976), RFID R1 dan NFC N1 Available (TC-AC-ACTS-978), unit Available U1 dengan beberapa entri (TC-AC-ACTS-979), dan unit berentri `Registered` (TC-AC-ACTS-980). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Pelaku Client (hapus aktivasi, kirim event Condition) memakai sesi API aktor, disediakan tim FE/BE; akun tidak ada di Pre-setup TC. Kemampuan memicu Combine dan Separate di TAG > Combine & Separate, penggantian Device Name SKU di Settings > Device > Name disediakan tim FE/BE; langkah UI modul lain tidak dirinci di TC.
- Device Name SKU `RFID-ASSET-CORE-R5` dicatat sebelum TC-AC-ACTS-980 dan dikembalikan ke nilai awal di hook `after` (pemulihan cadangan bila langkah pemulihan eksplisit tidak tercapai).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-973: Activate TAG di Global Settings menulis entri Activated dengan Client

1. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
2. Klik (⋯) > `TAG Log` pada unit yang diaktivasi Client PT Maju Bersama
3. Verifikasi entri berjudul `TAG Activated by [pelaku user Client yang mengaktivasi]` dengan Description `Client: PT Maju Bersama`
4. Verifikasi entri `TAG Activated by ...` tampil di atas `TAG Registered by ...`
5. Tutup popup lewat (X)

### TC-AC-ACTS-974: Delete TAG Jalur A mengembalikan unit ke Available dan menulis entri Returned to Stock

6. Buka Tab Available, klik (⋯) > `TAG Log` pada unit yang kembali Available setelah Client menghapus aktivasi Jalur A
7. Verifikasi entri berjudul `TAG Returned to Stock by [pelaku user Client yang menghapus aktivasi]` dengan Description `Client: PT Maju Bersama`
8. Verifikasi entri `TAG Activated by ...` sebelumnya tetap ada
9. Tutup popup lewat (X)

### TC-AC-ACTS-976: Event Condition Global Settings menulis entri Status Synced dengan PIC System

10. Buka Tab In Use
11. Client mengirim event Condition Damaged/Missing hingga tersimpan (sesi API aktor)
12. Muat ulang Tab In Use setiap 5 detik sampai event diproses (batas tunggu 2 menit)
13. Klik (⋯) > `TAG Log` pada unit In Use Status `Available`
14. Verifikasi entri berjudul `TAG Status Synced by System` dengan Description `Status: Available → Damaged/Missing`
15. Tutup popup lewat (X)

### TC-AC-ACTS-978: Combine dan Separate menulis entri Combined dan Separated pada kedua unit

16. Buka Tab Available
17. Combine R1 dan N1 di TAG > Combine & Separate hingga tersimpan (fixture BE)
18. Separate R1 dan N1 di TAG > Combine & Separate hingga tersimpan (fixture BE)
19. Klik (⋯) > `TAG Log` pada R1
20. Verifikasi R1 memuat entri `TAG Combined by [pelaku admin pelaku]` dengan `Combined With` NFC dan kode N1
21. Verifikasi R1 memuat entri `TAG Separated by [pelaku admin pelaku]` dengan `Separated From` NFC dan kode N1
22. Tutup popup lewat (X)
23. Klik (⋯) > `TAG Log` pada N1
24. Verifikasi N1 memuat entri `TAG Combined by [pelaku admin pelaku]` dan `TAG Separated by [pelaku admin pelaku]` dengan RFID dan kode R1
25. Tutup popup lewat (X)

### TC-AC-ACTS-980: Entri TAG Log immutable sedangkan header mengikuti nilai terkini

26. Klik (⋯) > `TAG Log` pada unit berentri `Registered`, catat judul dan isi entri `Registered`
27. Tutup popup lewat (X)
28. Ganti Device Name SKU `RFID-ASSET-CORE-R5` di Settings > Device > Name hingga tersimpan (fixture BE)
29. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
30. Klik (⋯) > `TAG Log` pada unit berentri `Registered` yang sama
31. Verifikasi header menampilkan Device Name terkini
32. Verifikasi judul dan isi entri `Registered` sama dengan yang dicatat sebelum penggantian Device Name
33. Tutup popup lewat (X)
34. Kembalikan Device Name SKU ke nilai awal (fixture BE)

### TC-AC-ACTS-979: Delete Stock menghapus unit sehingga TAG Log tidak bisa dibuka lagi

35. Klik (⋯) > `TAG Log` pada unit Available U1 dan catat entrinya
36. Tutup popup lewat (X)
37. Klik (⋯) > `Delete` pada U1, klik `[Delete]` pada dialog `Delete Unit`
38. Cari U1 di Tab Available
39. Verifikasi Tab Available memuat sedikitnya satu baris
40. Verifikasi U1 tidak tampil di Tab Available
41. Klik (⋯) > `TAG Log` pada unit lain
42. Verifikasi TAG Log unit lain tampil tanpa entri `Delete` dan tanpa riwayat U1
43. Tutup popup lewat (X)

### TC-AC-ACTS-975: Delete TAG Jalur B menghapus unit sehingga TAG Log ikut hilang

44. Buka Tab In Use
45. Client menghapus aktivasi unit Jalur B di Global Settings hingga tersimpan (sesi API aktor)
46. Muat ulang Tab In Use setiap 5 detik sampai event diproses (batas tunggu 2 menit)
47. Cari unit Jalur B itu di Tab In Use
48. Verifikasi Tab In Use memuat sedikitnya satu baris
49. Verifikasi unit Jalur B tidak tampil di Tab In Use

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (49 langkah); alasan: semua blok satu halaman sumber (Popup TAG Log) dan satu dataset, hanya membaca data kecuali pemicu lintas modul, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Kegagalan menulis entri TAG Log (TC-AC-ACTS-981, resilience kelas b) ada di spec 266.
- Urutan TC: TC-AC-ACTS-979 (Delete) dan TC-AC-ACTS-975 (Delete Jalur B) diletakkan di akhir karena mengubah atau menghapus data; TC-AC-ACTS-980 mengembalikan Device Name ke nilai awal dengan langkah eksplisit (S-09).
- Langkah penghubung tanpa Verifikasi (S-03): menutup popup lewat (X), memuat ulang tiap 5 detik memakai idiom baku "polling worker commit" (bagian 6, batas tunggu 2 menit), memicu Combine dan Separate lewat fixture BE. Pelaku Client ditulis "hingga tersimpan" (R-20).
- Absence unit pada TC-AC-ACTS-975 dan TC-AC-ACTS-979 didahului anchor positif (baris lain pada tabel yang sama; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-979 menyebut "tidak ada entri `Delete` di TAG Log unit lain" tanpa unit pembanding; spec memakai satu unit lain yang memiliki entri.
  - TC-AC-ACTS-975 menyebut TAG Log unit ikut terhapus; tidak diasersi karena TAG Log unit yang sudah terhapus tidak dapat dibuka dari UI. Spec mengasersi unit Jalur B tidak tampil di Tab In Use.
  - TC-AC-ACTS-974 dan TC-AC-ACTS-973 menyebut pelaku "[pelaku user Client ...]" sebagai nilai dinamis; disediakan seeding.
