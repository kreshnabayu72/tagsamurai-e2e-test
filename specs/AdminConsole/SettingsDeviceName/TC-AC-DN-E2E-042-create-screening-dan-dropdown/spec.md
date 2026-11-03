---
id: TC-AC-DN-E2E-042-create-screening-dan-dropdown
title: "Create Device Name: Screening Popup dan Dropdown Measurement/Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-73
  - TC-AC-DN-74
  - TC-AC-DN-586
  - TC-AC-DN-75
  - TC-AC-DN-76
  - TC-AC-DN-77
  - TC-AC-DN-78
coverage:
  web: automated
---

# Create Device Name: Screening Popup dan Dropdown Measurement/Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement Principal `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori (`Hardware` > `BLE Gateway`; `Handheld Reader` > `UHF Handheld`; `Smart Fixed Reader` > `Antenna`; `TAG` > `BLE`; `GPS`; `NFC` > `Accessory`, `Perangkat Pemindai Kode Batang Industri`, `Tag`; `RFID`); #24 Measurement master `Liter` (ada di master, belum dipakai Device Name mana pun).
- Data Dinamis: tidak ada record yang dibuat; tidak ada [Submit] yang dikirim.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-73: Screening popup form Create Device Name

1. Klik tombol `+ Device Name` pada toolbar
2. Verifikasi Header: judul popup `Create Device Name` tampil di sisi kiri atas
3. Verifikasi Header: icon close `[✕]` tampil di sudut kanan atas popup
4. Verifikasi Body: field `Device Name` berada paling atas berupa input teks kosong dengan placeholder "Enter device name"
5. Verifikasi Body: field `Measurement` berada di bawah `Device Name` berupa dropdown kosong dengan placeholder "Select measurement"
6. Verifikasi Body: field `Category` berada di bawah `Measurement` berupa TreeSelect kosong dengan placeholder "Select category"
7. Verifikasi Body: tidak ada helper text di bawah ketiga field
8. Verifikasi Footer: checkbox `Stay on this form after submitting` tampil tidak tercentang, rata kanan tepat di atas tombol
9. Verifikasi Footer: tombol `[Clear Field]` (teks, primary) dan `[Submit]` (filled, success) berdampingan rata kanan
10. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-AC-DN-74: Dropdown Measurement menampilkan opsi dari master Measurement Principal

11. Klik field Measurement
12. Verifikasi daftar opsi memuat `Unit`, `Meter`, dan `Box`
13. Verifikasi field Device Name tidak berubah (tetap kosong dengan placeholder "Enter device name")
14. Verifikasi field Category tidak berubah (tetap kosong dengan placeholder "Select category")

### TC-AC-DN-586: Dropdown Measurement memuat Measurement master yang belum dipakai

15. Verifikasi daftar opsi Measurement yang masih terbuka memuat `Unit`, `Meter`, `Box`, dan `Liter`

### TC-AC-DN-75: Dropdown Category menampilkan pohon dengan Hardware dan TAG tidak dapat dipilih

16. Klik field Category
17. Expand `Hardware`, `Handheld Reader`, `Smart Fixed Reader`, `TAG`, lalu `NFC`
18. Verifikasi pohon memuat `Hardware` > (`BLE Gateway`; `Handheld Reader` > `UHF Handheld`; `Smart Fixed Reader` > `Antenna`) dan `TAG` > (`BLE`; `GPS`; `NFC` > (`Accessory`, `Perangkat Pemindai Kode Batang Industri`, `Tag`); `RFID`)
19. Verifikasi `Hardware` dan `TAG` tampil untuk konteks tanpa dapat dipilih
20. Verifikasi `Handheld Reader`, `Smart Fixed Reader`, dan `NFC` (punya anak) tampil sebagai node yang dapat dipilih
21. Verifikasi `BLE Gateway`, `UHF Handheld`, `Antenna`, `BLE`, `GPS`, `RFID`, `Accessory`, `Tag`, dan `Perangkat Pemindai Kode Batang Industri` tampil sebagai node yang dapat dipilih

### TC-AC-DN-76: Klik root Hardware dan TAG tidak memilih node

22. Klik node `Hardware`
23. Verifikasi field Category tetap menampilkan placeholder "Select category"
24. Verifikasi `Hardware` tidak berstatus terpilih
25. Klik node `TAG`
26. Verifikasi field Category tetap menampilkan placeholder "Select category"
27. Verifikasi `TAG` tidak berstatus terpilih

### TC-AC-DN-77: Klik node Handheld Reader yang punya anak memilih node

28. Klik node `Hardware` untuk expand sehingga anak node tampil
29. Klik node `Handheld Reader`
30. Verifikasi field Category menampilkan `Handheld Reader` dan placeholder hilang
31. Verifikasi dropdown pohon tertutup

### TC-AC-DN-78: Pilih leaf tiga level UHF Handheld

32. Klik field Category, expand `Hardware` lalu `Handheld Reader`
33. Pilih leaf `UHF Handheld`
34. Verifikasi field Category menampilkan `UHF Handheld` dan placeholder hilang
35. Verifikasi dropdown pohon tertutup
36. Klik `[Clear Field]`
37. Klik icon close `[✕]` pada popup

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. TC 73, 76, 77, dan 78 bertanda FE Test "UI Only"; TC 74, 75, dan 586 "Need API" (opsi dari master Measurement dan pohon Category).
- Alasan lebih dari sekitar 35 langkah (prinsip 13 bagian 3, "Halaman yang sama dipakai berulang"): ketujuh TC hanya mengamati dan memilih nilai tanpa [Submit], sehingga memakai satu pembukaan popup dengan satu kelas harness dan tidak membuat record. Jumlah langkah (37) berasal dari pemecahan `Verifikasi` per klausa (S-01), bukan dari pembukaan ulang form. Tiap bagian tetap bermakna bila bagian sebelumnya gagal karena memakai data Pre-setup yang sama.
- Penyimpangan urutan (S-10): urutan TC dipertahankan seperti pada `sourceTc` (screening, dropdown Measurement, lalu dropdown Category dari yang tidak dapat dipilih ke yang dapat dipilih). Langkah 1 dan langkah penutup 37 menjadi satu pasang buka-tutup popup.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 28 (expand ulang `Hardware` yang tertutup oleh klik di langkah 22 supaya `Handheld Reader` terlihat seperti pada langkah TC-AC-DN-77), serta langkah 36 dan 37 (pemulihan form dirty sesuai S-09: [Clear Field] lalu `[✕]` pada form kosong tanpa dialog `Unsaved Changes`).
- TC-AC-DN-74 dan TC-AC-DN-586 memakai satu pembukaan daftar Measurement yang sama (langkah 11); langkah 15 mengasersi opsi `Liter` pada daftar yang sama tanpa menutup dan membuka ulang.
- Temuan untuk QA:
  - TC-AC-DN-76 menyebut klik `Hardware` dan `TAG` "berubah expand atau collapse"; keadaan akhir (expand atau collapse) tidak dinyatakan, sehingga langkah 28 mengasumsikan `Hardware` tertutup setelah langkah 22.
  - TC-AC-DN-78 tidak menyatakan apakah dropdown Category mengingat keadaan expand dari pembukaan sebelumnya; langkah 32 menulis expand `Hardware` lalu `Handheld Reader` mengikuti TC.
  - TC-AC-DN-586 menulis Expected daftar opsi `Unit`, `Meter`, `Box`, `Liter` tanpa menyatakan urutannya; urutan tidak diasersi.
