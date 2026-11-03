---
id: TC-AC-DN-E2E-049-create-checkbox-stay-on-form
title: "Create Device Name: Checkbox Stay on this form, Form Dikosongkan, dan Create Dua Device Name Berurutan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-84
  - TC-AC-DN-85
  - TC-AC-DN-86
coverage:
  web: automated
---

# Create Device Name: Checkbox Stay on this form, Form Dikosongkan, dan Create Dua Device Name Berurutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori (leaf `Antenna` di `Hardware` > `Smart Fixed Reader`).
- Data Dinamis (dibuat lewat form Create): `Batch Antenna 1 {runId}-049` (`Unit`), `Batch Antenna 2 {runId}-049` (`Unit`), `Batch Antenna 3 {runId}-049` (`Meter`), dan `Mobile Antenna Dua {runId}-049` (`Unit`), semuanya Category `Antenna`. Hook `after` menghapus keempat record lewat fixture BE (kemampuan hapus record Device Name disediakan tim FE/BE; pembersihan tidak berasumsi setup berhasil penuh).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-84: Create dengan checkbox Stay tercentang mengosongkan form dan membiarkan popup terbuka

1. Klik tombol `+ Device Name` pada toolbar
2. Centang checkbox `Stay on this form after submitting`
3. Ketik `Batch Antenna 1 {runId}-049` pada field Device Name
4. Klik field Measurement lalu pilih `Unit`
5. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
6. Klik `[Submit]`
7. Verifikasi toast sukses: "Success, device name has been created."
8. Verifikasi popup form Create tetap terbuka
9. Verifikasi field Device Name kosong dengan placeholder "Enter device name"
10. Verifikasi field Measurement kembali ke placeholder "Select measurement" (pilihan `Unit` tidak dipertahankan)
11. Verifikasi field Category kembali ke placeholder "Select category" (pilihan `Antenna` tidak dipertahankan)
12. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
13. Verifikasi tidak ada pesan error pada field

### TC-AC-DN-85: Create dua Device Name berurutan dengan checkbox Stay tercentang

14. Ketik `Batch Antenna 2 {runId}-049` pada field Device Name
15. Klik field Measurement lalu pilih `Unit`
16. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
17. Klik `[Submit]`
18. Verifikasi toast sukses: "Success, device name has been created."
19. Tunggu toast pertama hilang sendiri
20. Ketik `Batch Antenna 3 {runId}-049` pada field Device Name
21. Klik field Measurement lalu pilih `Meter`
22. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
23. Klik `[Submit]`
24. Verifikasi toast sukses kedua: "Success, device name has been created."
25. Klik icon close `[✕]` pada popup
26. Ketik Search `Batch Antenna`, tekan Enter
27. Verifikasi List memuat baris `Batch Antenna 2 {runId}-049` dengan Measurement `Unit`
28. Verifikasi List memuat baris `Batch Antenna 3 {runId}-049` dengan Measurement `Meter`

### TC-AC-DN-86: Checkbox Stay tidak tercentang secara default sehingga popup menutup setelah Submit

29. Klik tombol `+ Device Name` pada toolbar
30. Verifikasi checkbox `Stay on this form after submitting` tampil tidak tercentang sebelum Submit
31. Ketik `Mobile Antenna Dua {runId}-049` pada field Device Name
32. Klik field Measurement lalu pilih `Unit`
33. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
34. Klik `[Submit]`
35. Verifikasi popup form tertutup
36. Verifikasi toast sukses: "Success, device name has been created."

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Ketiga TC bertanda FE Test "Need API".
- Alasan sekitar 35 langkah (satu topik, satu dataset, satu kelas harness): ketiga TC menguji perilaku checkbox `Stay on this form after submitting` pada Create sukses dengan record milik spec sendiri; tiap bagian tetap bermakna bila bagian sebelumnya gagal. Jumlah langkah (36) berasal dari pemecahan `Verifikasi` per klausa (S-01).
- Penyimpangan dari langkah TC (S-04): TC-AC-DN-85 membuka popup baru dan mencentang checkbox pada langkahnya. Spec melanjutkan popup TC-AC-DN-84 yang checkbox-nya masih tercentang (Expected c TC-AC-DN-84), sehingga langkah centang dan pembukaan popup TC-AC-DN-85 tidak diulang; mengulang klik centang justru melepas centang. TC-AC-DN-86 membuka popup baru setelah popup ditutup pada langkah 25, sehingga default tidak tercentang juga teruji setelah sesi Stay sebelumnya.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 19 (menunggu toast pertama hilang sendiri, sekitar 4 detik, sebelum toast kedua diasersi), langkah 25 (menutup popup dengan form kosong tanpa dialog `Unsaved Changes`), dan langkah 26 (Search untuk menemukan baris target, R-16).
- Temuan untuk QA:
  - TC-AC-DN-85 Expected b ("Setelah popup ditutup, List memuat baris ...") tidak menyebut cara menemukan baris; spec memakai Search.
  - Post Condition "Record ... tersimpan" pada TC-AC-DN-84 dan TC-AC-DN-86 tidak punya langkah observasi di TC sehingga tidak diasersi.
