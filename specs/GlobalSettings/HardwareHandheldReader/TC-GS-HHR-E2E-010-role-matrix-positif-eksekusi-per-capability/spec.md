---
id: TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability
title: "Role Matrix Positif: Eksekusi Aksi Handheld Reader per Capability Manage hardware"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-43
  - TC-GS-HHR-44
  - TC-GS-HHR-45
  - TC-GS-HHR-46
  - TC-GS-HHR-47
  - TC-GS-HHR-48
  - TC-GS-HHR-49
coverage:
  web: automated
---

# Role Matrix Positif: Eksekusi Aksi Handheld Reader per Capability Manage hardware

## Prerequisites

- Mode: FE+BE. Suite `parallel: false` (spec mengubah state yang dipakai bersama: Seed Reader A, kuota Long Range Client A).
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk setiap akun pada tabel di bawah (lihat `suite.md`, Hook suite).
- Spec Role Matrix positif (bagian 3a konvensi): tiap capability menjalankan aksi yang berhak dilakukannya. Langkah tiap role berbeda (aksi berbeda), sehingga ditulis per blok role.

Role yang diuji (Tabel Data Uji Pre-setup #5 dan #6, Client A):

| Blok | TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| 1 | TC-GS-HHR-43, TC-GS-HHR-44, TC-GS-HHR-45, TC-GS-HHR-46, TC-GS-HHR-47 | Manage hardware (Update) | Agus Wijaya | `manageHardwareUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_HW_UPDATE_PASSWORD` |
| 2 | TC-GS-HHR-48, TC-GS-HHR-49 | Manage hardware (Delete) | Dewi Anggraini | `manageHardwareDelete_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_HW_DELETE_PASSWORD` |

- Login Manage hardware (Update) dilakukan di hook `before`; blok 2 memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Manage hardware (Delete), hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password hanya lewat env.
- Layar awal: Global Settings > Hardware > Handheld Reader dibuka di hook `beforeEach`.
- Data: Client A (plan Growth, toggle BYO aktif, alokasi `Short Range` 8 dan `Long Range` 6). Target aksi memakai Seed Reader A (Tabel Data Uji Dinamis TC): DD-01 (Available, Long Range, 30 dBm), DD-03 (Damaged), DD-05 (Waiting for Approval). Seed Reader A adalah Pre-setup bersama yang kuota `Long Range` sudah terpakai 5 dari 6, sehingga reader milik spec tidak bisa ditambahkan tanpa melampaui kuota; karena itu aksi mengubah Seed Reader A dan dipulihkan lewat fixture BE (disediakan tim FE, sesuai catatan Tabel Data Uji Dinamis TC: dipulihkan fixture backend sebelum tiap TC). Pemulihan dilakukan lewat langkah eksplisit di akhir tiap perubahan yang dibawa ke langkah berikutnya, dan hook `after` memulihkan sebagai cadangan.
- Data Dinamis: Alias Name `Reader Dock 01-{runId}-010` (suffix nomor spec 010).
- State global yang diubah: Seed Reader A (status, alias, Reader Power, jumlah reader), kuota `Long Range` Client A; dipulihkan oleh langkah pemulihan dan hook `after`.

## Test Steps

### Blok 1 - Manage hardware (Update): TC-GS-HHR-43 sampai TC-GS-HHR-47

1. Buka Overlay row action DD-01, klik `Edit Alias Name`
2. Isi `Alias Name` dengan `Reader Dock 01-{runId}-010`
3. Klik `[Save]`
4. Verifikasi muncul toast sukses "Success, Reader Dock 01-{runId}-010 has been updated."
5. Verifikasi kolom `Alias Name` baris DD-01 menampilkan `Reader Dock 01-{runId}-010`
6. Pulihkan Seed Reader A lewat fixture BE, lalu muat ulang halaman Handheld Reader
7. Buka Overlay row action DD-01, klik `Edit Reader Power`
8. Geser slider ke 25 dBm
9. Klik `[Save]`
10. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 1 has been updated."
11. Verifikasi kolom `Reader Power` baris DD-01 menampilkan `25 dBm`
12. Buka Overlay row action DD-01, klik `Mark as Damaged`
13. Klik `[Mark as Damaged]` pada dialog konfirmasi
14. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 1 has been marked as damaged."
15. Verifikasi Badge `Status` baris DD-01 menjadi `Damaged`
16. Pulihkan Seed Reader A lewat fixture BE, lalu muat ulang halaman Handheld Reader
17. Buka Overlay row action DD-01, klik `Mark as Missing`
18. Klik `[Mark as Missing]` pada dialog konfirmasi
19. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 1 has been marked as missing."
20. Verifikasi Badge `Status` baris DD-01 menjadi `Missing`
21. Buka Overlay row action DD-03, klik `Mark as Available`
22. Klik `[Mark as Available]` pada dialog konfirmasi
23. Verifikasi muncul toast sukses "Success, Zebra Mobile Reader - 1 has been marked as available."
24. Verifikasi Badge `Status` baris DD-03 menjadi `Available`
25. Pulihkan Seed Reader A lewat fixture BE, lalu muat ulang halaman Handheld Reader

### Blok 2 - Manage hardware (Delete): TC-GS-HHR-49 lalu TC-GS-HHR-48

26. Logout, lalu login sebagai Dewi Anggraini (Manage hardware level Delete)
27. Buka Global Settings > Hardware > Handheld Reader
28. Buka Overlay row action DD-05, klik `Cancel Request`
29. Klik `[Cancel Request]` pada dialog konfirmasi
30. Verifikasi muncul toast sukses "Success, Chainway C72 - 1 request has been canceled."
31. Verifikasi baris DD-05 hilang dari tabel
32. Buka Overlay row action DD-01, klik `Delete`
33. Klik `[Delete]` pada dialog konfirmasi
34. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 1 has been deleted."
35. Verifikasi baris DD-01 hilang dari tabel
36. Pulihkan Seed Reader A lewat fixture BE

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 2). Kelas harness: Role Matrix positif (bagian 3a), tanpa simulator USB. Setiap capability hanya menjalankan aksi yang berhak dilakukannya; kombinasi role x aksi lain tidak ditambahkan karena belum punya TC sumber. TC-GS-HHR-42 (aktor Create) ada di spec 017.
- Spec ditulis per blok role karena langkah tiap role berbeda (aksi berbeda) dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Spec sekitar 35 langkah (36 langkah nominal, tanpa perulangan). Alasan: seluruh langkah satu kelas (Role Matrix positif) dan blok Delete berdiri sendiri dengan login ulang di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna. Aksi mutasi Seed Reader A dipulihkan fixture BE di antara aksi yang saling bergantung (langkah 6, 16, 25), sehingga kegagalan satu aksi Update tidak menghilangkan makna aksi berikutnya.
- Urutan TC sumber diubah: Delete berada di blok terakhir dan TC-GS-HHR-49 (Cancel Request) dijalankan sebelum TC-GS-HHR-48 (Delete) agar aksi penghapus berada paling akhir (bagian 3 prinsip 5).
- Pengecualian S-12 Population Seed Reader A HHR: Seed Reader A bernama literal tanpa suffix `{runId}`; pemulihan lewat fixture BE (hook `before` dan `after`, serta langkah penghubung antar aksi) dan suite serial dinyatakan di `suite.md`. Alias Name hasil edit tetap bersuffix.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): pemulihan Seed Reader A lewat fixture BE (langkah 6, 16, 25, 36); logout lalu login ke role Delete (langkah 26); membuka halaman Handheld Reader setelah ganti akun (langkah 27).
- Pemulihan pada langkah 6 mengembalikan `Alias Name` DD-01 ke `—` sebelum TC-GS-HHR-44 dan TC-GS-HHR-45 (toast memakai nama `Zebra RFID Reader - 1`); pemulihan pada langkah 16 mengembalikan DD-01 ke Available sebelum TC-GS-HHR-46. Pemulihan pada langkah 25 dan 36 menyiapkan kondisi bersih sesudah aksi terakhir tiap blok.
- Temuan untuk QA:
  - TC-GS-HHR-43 sampai TC-GS-HHR-49 memakai Seed Reader A bersama sebagai target aksi tulis (S-06). Reader milik spec tidak ditambahkan karena kuota `Long Range` Client A sudah terpakai 5 dari 6; spec memulihkan Seed Reader A lewat fixture BE.
  - TC-GS-HHR-43 menulis `Alias Name` literal `Reader Dock 01`; spec memakai nilai bersuffix per run (`Reader Dock 01-{runId}-010`) dan toast memuat nilai bersuffix yang sama.
  - TC-GS-HHR-44 sampai TC-GS-HHR-49 memakai ekspektasi nama toast `Zebra RFID Reader - 1` dan sejenisnya dari Seed Reader A; bila fixture BE menghasilkan nama lain, asersi toast mengikuti nama tersebut.
