---
id: TC-AC-DN-E2E-051-create-clear-field-dan-saving-state
title: "Create Device Name: Clear Field dan Saving State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-108
  - TC-AC-DN-109
coverage:
  web: automated
---

# Create Device Name: Clear Field dan Saving State

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata: respons penyimpanan ditunda pada TC-AC-DN-109).
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori (leaf `Antenna` di `Hardware` > `Smart Fixed Reader`); #16 Device Name inti `Cable Tester` (target duplikat TC-AC-DN-108, [Submit] ditolak sehingga tidak diubah).
- Data Dinamis: `Saving Gateway {runId}-051` (`Unit`, `Antenna`) dibuat lewat form pada TC-AC-DN-109. Hook `after` menghapus record itu lewat fixture BE (kemampuan hapus record Device Name disediakan tim FE/BE; pembersihan tidak berasumsi setup berhasil penuh).
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons request penyimpanan selama 5 detik (TC-AC-DN-109); intercept dilepas sesudah respons diterima.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-108: Clear Field mengosongkan seluruh field dan error tanpa menutup popup

1. Klik tombol `+ Device Name` pada toolbar
2. Centang checkbox `Stay on this form after submitting`
3. Ketik `Cable Tester` pada field Device Name
4. Klik field Measurement lalu pilih `Meter`
5. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
6. Klik `[Submit]`
7. Verifikasi error inline duplikat "Device name already exists" tampil di bawah field Device Name
8. Klik `[Clear Field]`
9. Verifikasi field Device Name kosong dengan placeholder "Enter device name"
10. Verifikasi field Measurement kembali ke placeholder "Select measurement"
11. Verifikasi field Category kembali ke placeholder "Select category"
12. Verifikasi pesan error inline dihapus dari semua field
13. Verifikasi border merah dihapus dari semua field
14. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
15. Verifikasi popup tetap terbuka
16. Verifikasi fokus kursor berada di field Device Name
17. Verifikasi tidak ada dialog konfirmasi
18. Klik icon close `[✕]` pada popup

### TC-AC-DN-109: Tombol Submit menampilkan saving state dan mengunci kontrol saat request berjalan

19. Klik tombol `+ Device Name` pada toolbar
20. Ketik `Saving Gateway {runId}-051` pada field Device Name
21. Klik field Measurement lalu pilih `Unit`
22. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
23. Tunda respons request penyimpanan selama 5 detik lewat intercept jaringan
24. Klik `[Submit]`
25. Verifikasi tombol `[Submit]` menampilkan indikator loading
26. Verifikasi tombol `[Submit]` berstatus disabled (tetap tampil)
27. Verifikasi tombol `[Clear Field]`, icon close `[✕]`, dan semua field berstatus disabled (tetap tampil)
28. Tunggu respons yang ditahan diterima, lalu lepas intercept jaringan
29. Verifikasi popup tertutup
30. Verifikasi toast sukses: "Success, device name has been created."

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. TC-AC-DN-108 bertanda FE Test "UI Only"; TC-AC-DN-109 "Need API". Penundaan respons pada TC-AC-DN-109 hanya untuk mengamati state saving dan bukan kegagalan yang dipaksakan, sehingga kelas harness tetap fungsional.
- TC-AC-DN-110 dan TC-AC-DN-127 ada di spec 054.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 18 (menutup popup dengan form kosong tanpa dialog `Unsaved Changes`, sesuai S-09; popup TC-AC-DN-109 dibuka baru supaya checkbox `Stay on this form after submitting` kembali tidak tercentang dan popup menutup setelah respons), langkah 28 (menunggu respons ditahan selesai dan melepas intercept, S-09).
- Asersi tambahan (S-03): langkah 7 mengasersi error duplikat yang disebut pada langkah TC-AC-DN-108 ("error duplikat tampil") sebagai anchor positif sebelum asersi error dihapus.
- Langkah 25 sampai 27 diasersi selama respons ditahan (state sementara, bagian 8b butir 5), sebelum respons diterima.
- Temuan untuk QA:
  - TC-AC-DN-108 Data Uji memakai nama `Cable Tester` literal dari Pre-setup #16 sebagai target duplikat (hanya dibaca).
  - Post Condition TC-AC-DN-109 tidak ada; Expected c mengasersi popup tertutup dan toast sukses, sedangkan record yang tersimpan tidak diasersi di List.
