---
id: TC-AC-DN-E2E-100-search-siklus-interaksi-dan-kolom
title: "Search List: Siklus Interaksi, Placeholder, dan Kolom Device Name/Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-272
  - TC-AC-DN-273
  - TC-AC-DN-274
  - TC-AC-DN-275
  - TC-AC-DN-276
coverage:
  web: automated
---

# Search List: Siklus Interaksi, Placeholder, dan Kolom Device Name/Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti (`Barcode Station`, `Cable Tester`, `Door Antenna`, `Field Radio`, `Gate Antenna`, `Legacy Scanner`, `NFC Tag`, `RFID Reader`, `Tag Reel`), #17 seed `Seed Device 001` sampai `Seed Device 120`, dan #23 nama panjang; total 130 baris. Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- Kemampuan teknis: mengetik, menekan Enter dan Tab, hover, dan fokus keyboard pada ikon Search.
- State global: tidak ada yang diubah. Kotak Search dikosongkan di akhir spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-272: Siklus interaksi Search

1. Klik icon Search di toolbar
2. Verifikasi kursor fokus di dalam input pencarian
3. Ketik `rfid` tanpa menekan Enter
4. Verifikasi ikon `(✕)` muncul di sisi kanan dalam input
5. Verifikasi tabel belum tersaring: halaman 1 tetap menampilkan Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002
6. Tekan Enter
7. Verifikasi tabel menampilkan 1 baris: RFID Reader
8. Klik ikon `(✕)`
9. Verifikasi teks input kosong
10. Verifikasi kolom pencarian tetap terbuka dengan kursor fokus
11. Verifikasi tabel belum reset (tetap 1 baris RFID Reader)
12. Tekan Enter pada input yang kosong
13. Verifikasi tabel reset ke 130 baris
14. Verifikasi halaman 1 menampilkan Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002
15. Ketik Search `rfid`, tekan Enter
16. Klik ikon panah `(←)` di kiri toolbar
17. Verifikasi kolom pencarian menutup menjadi ikon Search
18. Verifikasi tabel langsung reset ke 130 baris

### TC-AC-DN-273: Tooltip ikon Search

19. Arahkan kursor ke ikon Search di toolbar
20. Verifikasi tooltip `Search` tampil di dekat ikon (hover)
21. Pindahkan kursor menjauh lalu fokuskan ikon Search dengan tombol Tab
22. Verifikasi tooltip `Search` tampil di dekat ikon (fokus keyboard)

### TC-AC-DN-274: Placeholder default kolom pencarian

23. Klik ikon Search di toolbar
24. Verifikasi input pencarian yang masih kosong menampilkan placeholder `Search by device name, brand, or model/type`
25. Ketik `r` di input
26. Verifikasi placeholder hilang
27. Klik ikon `(✕)`
28. Verifikasi placeholder `Search by device name, brand, or model/type` tampil kembali

### TC-AC-DN-275: Search kolom Device Name

29. Ketik Search `rfid`, tekan Enter
30. Verifikasi tabel menampilkan 1 baris: RFID Reader (keyword `rfid`)
31. Ganti isi kotak search dengan `FID R`, tekan Enter
32. Verifikasi tabel menampilkan 1 baris: RFID Reader (keyword `FID R`, potongan tengah nama)
33. Ganti isi kotak search dengan `RFID READER`, tekan Enter
34. Verifikasi tabel menampilkan 1 baris: RFID Reader (keyword `RFID READER`, huruf besar)

### TC-AC-DN-276: Search kolom Category

35. Ganti isi kotak search dengan `handheld`, tekan Enter
36. Verifikasi tabel menampilkan 2 baris: Legacy Scanner dan RFID Reader
37. Verifikasi baris Legacy Scanner dan RFID Reader menampilkan Category `UHF Handheld` (cocok pada kolom Category, bukan pada Device Name)
38. Ganti isi kotak search dengan `HF HANDH`, tekan Enter
39. Verifikasi tabel menampilkan 2 baris: Legacy Scanner dan RFID Reader (keyword `HF HANDH`, potongan tengah, huruf besar)
40. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 15 (Search `rfid` sebelum `(←)`) menyiapkan keadaan yang ditutup oleh TC-AC-DN-272; langkah 40 mengosongkan Search di akhir spec.
- Ukuran spec (40 langkah, di atas smell 35 langkah, kode R3): satu topik (siklus interaksi dan kolom Search), satu dataset 130 baris yang hanya dibaca, satu kelas harness (e); tiap blok TC berdiri sendiri karena memulai dari kotak Search yang dikosongkan, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc; siklus interaksi (TC-AC-DN-272) di awal, lalu tooltip dan placeholder, lalu kecocokan kolom.
- Temuan untuk QA:
  - TC-AC-DN-272 langkah 2 menyebut kolom pencarian melebar saat ikon Search diklik, tetapi Expected hanya memuat fokus kursor; spec tidak menambahkan asersi lebar.
  - TC-AC-DN-272 hingga TC-AC-DN-276: jumlah total 130 baris dan urutan halaman 1 mengikuti Pre-setup #16 dan #17; TC tidak menyebut cara membaca total baris di layar, spec mengasersi jumlah baris yang terbaca dari pagination/tabel.
