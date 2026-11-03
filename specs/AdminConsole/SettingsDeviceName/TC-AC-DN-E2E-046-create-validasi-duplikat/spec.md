---
id: TC-AC-DN-E2E-046-create-validasi-duplikat
title: "Create Device Name: Error Duplikat (Persis, Huruf Besar-Kecil, Spasi Ujung) dan Duplikat setelah Create Berurutan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-93
  - TC-AC-DN-94
  - TC-AC-DN-95
  - TC-AC-DN-577
coverage:
  web: automated
---

# Create Device Name: Error Duplikat (Persis, Huruf Besar-Kecil, Spasi Ujung) dan Duplikat setelah Create Berurutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca, tidak diubah dan Last Modified tidak berubah karena semua [Submit] ditolak): #13 master Measurement `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori (leaf `Antenna` dan `UHF Handheld`); #16 Device Name inti `Cable Tester` (target duplikat TC-AC-DN-93 dan TC-AC-DN-95) dan `RFID Reader` (target duplikat huruf besar-kecil TC-AC-DN-94).
- Data Dinamis: `Batch One {runId}-046` dibuat lewat form (TC-AC-DN-577); varian huruf kecil `batch one {runId}-046` hanya diketik. Hook `after` menghapus record `Batch One {runId}-046` lewat fixture BE (kemampuan hapus record Device Name disediakan tim FE/BE; pembersihan tidak berasumsi setup berhasil penuh).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-93: Device Name sama persis dengan record lain

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik `Cable Tester` pada field Device Name, lalu tunggu sekitar 500 ms tanpa memindahkan fokus dari field
3. Verifikasi error inline "Device name already exists" muncul di bawah field Device Name setelah jeda sekitar 500 ms, tanpa klik di luar field
4. Klik field Measurement lalu pilih `Unit`
5. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
6. Klik `[Submit]`
7. Verifikasi error inline "Device name already exists" tetap tampil
8. Verifikasi popup form tetap terbuka
9. Verifikasi tidak ada toast

### TC-AC-DN-94: Device Name hanya berbeda huruf besar-kecil

10. Klik `[Clear Field]`
11. Ketik `rfid reader` pada field Device Name, lalu tunggu sekitar 500 ms tanpa memindahkan fokus
12. Verifikasi error inline "Device name already exists" muncul di bawah field Device Name
13. Klik field Measurement lalu pilih `Unit`
14. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih leaf `UHF Handheld`
15. Verifikasi popup form tetap terbuka

### TC-AC-DN-95: Duplikat disertai spasi di ujung

16. Klik `[Clear Field]`
17. Ketik dua spasi, `Cable Tester`, lalu dua spasi pada field Device Name, kemudian tunggu sekitar 500 ms tanpa memindahkan fokus
18. Verifikasi error inline "Device name already exists" muncul di bawah field Device Name karena pengecekan memakai nilai ter-trim

### TC-AC-DN-577: Create berurutan dengan Stay on this form, nama berikutnya duplikat

19. Klik `[Clear Field]`
20. Centang checkbox `Stay on this form after submitting`
21. Ketik `Batch One {runId}-046` pada field Device Name
22. Klik field Measurement lalu pilih `Unit`
23. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
24. Klik `[Submit]`
25. Verifikasi toast sukses pertama: "Success, device name has been created."
26. Verifikasi form kembali kosong (Device Name, Measurement, dan Category menampilkan placeholder)
27. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
28. Ketik `batch one {runId}-046` pada field Device Name, lalu tunggu 1 detik
29. Verifikasi error inline "Device name already exists" tampil di bawah field Device Name
30. Klik field Measurement lalu pilih `Unit`
31. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
32. Klik `[Submit]`
33. Verifikasi form tetap terbuka
34. Klik `[Clear Field]`
35. Klik icon close `[✕]` pada popup
36. Ketik Search `Batch One {runId}-046`, tekan Enter
37. Verifikasi List memuat tepat satu baris `Batch One {runId}-046`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Keempat TC bertanda FE Test "Need API" (pengecekan keunikan memanggil backend). Error duplikat pada TC-AC-DN-93, TC-AC-DN-94, dan TC-AC-DN-95 adalah respons validasi normal dan bukan kegagalan server yang dipaksakan, sehingga spec ini satu kelas fungsional.
- Alasan lebih dari sekitar 35 langkah (prinsip 13 bagian 3, "Halaman yang sama dipakai berulang"): keempat TC memakai form Create yang sama dan satu kelas harness; tiga TC pertama hanya mengetik tanpa record baru sehingga satu pembukaan popup dipakai bersama, dan tiap bagian tetap bermakna bila bagian sebelumnya gagal. Jumlah langkah (37) berasal dari pemecahan `Verifikasi` per klausa (S-01) dan pengisian ulang Measurement dan Category pada TC-AC-DN-577.
- Target duplikat memakai data Pre-setup in-use yang hanya dibaca (S-06, pengecualian target aksi ditolak); tidak ada record Pre-setup yang diubah.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 10, 16, dan 19 (`[Clear Field]` menghapus error dan isian TC sebelumnya, S-09 dan R-12), langkah 34 dan 35 (pemulihan form dirty lalu menutup form kosong tanpa dialog `Unsaved Changes`), serta langkah 36 (Search untuk menemukan baris target, R-16).
- Asersi tambahan (S-03): langkah 36 dan 37 membuktikan Expected d TC-AC-DN-577 ("Submit kedua tidak membuat Device Name baru") karena TC tidak memberi langkah pengecekan List; Search tidak peka huruf besar-kecil sehingga satu baris berarti varian huruf kecil tidak tersimpan.
- Langkah 33 mengasersi form tetap terbuka tanpa asersi absence toast karena toast sukses pertama (langkah 25) masih dapat tampil saat Submit kedua dikirim.
- Penyimpangan urutan: TC-AC-DN-577 diletakkan terakhir karena membuat record (aksi sukses) setelah semua validasi diblokir (S-10); popup yang sama dipakai tanpa dibuka ulang (prinsip 13, "Halaman yang sama dipakai berulang").
- Temuan untuk QA:
  - TC-AC-DN-94 dan TC-AC-DN-95 tidak menyertakan langkah [Submit] sehingga hanya error saat mengetik yang diasersi.
  - TC-AC-DN-577 Data Uji menyebut nama literal `Batch One` dan `batch one`; spec memakai nama bersuffix (S-12) dengan huruf besar-kecil yang sama pada bagian dasar.
  - Post Condition "Tidak ada record baru tersimpan" (TC-AC-DN-93, TC-AC-DN-94, TC-AC-DN-95) tidak punya langkah observasi di TC sehingga tidak diasersi.
