---
id: TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability
title: "Role Matrix Positif: Eksekusi Aksi Handheld Reader per Capability Manage hardware"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-42
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

- Mode: FE+BE. Suite `parallel: false` (spec mengubah state yang dipakai bersama: Seed Reader A, kuota Long Range Client A, counter nomor urut Device Name).
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk setiap akun pada tabel di bawah (lihat `suite.md`, Hook suite).
- Spec Role Matrix positif (bagian 3a konvensi): tiap capability menjalankan aksi yang berhak dilakukannya. Langkah tiap role berbeda (aksi berbeda), sehingga ditulis per blok role.

Role yang diuji (Tabel Data Uji Pre-setup #4 s.d. #6, Client A):

| Blok | TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| 1 | TC-GS-HHR-42 | Manage hardware (Create) | Rina Lestari | `manageHardwareCreate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| 2 | TC-GS-HHR-43, TC-GS-HHR-44, TC-GS-HHR-45, TC-GS-HHR-46, TC-GS-HHR-47 | Manage hardware (Update) | Agus Wijaya | `manageHardwareUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| 3 | TC-GS-HHR-48, TC-GS-HHR-49 | Manage hardware (Delete) | Dewi Anggraini | `manageHardwareDelete_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |

- Login Manage hardware (Create) dilakukan di hook `before`; blok 2 dan blok 3 memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Manage hardware (Delete), hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password hanya lewat env.
- Layar awal: Global Settings > Hardware > Handheld Reader dibuka di hook `beforeEach`.
- Data: Client A (plan Growth, toggle BYO aktif, alokasi `Short Range` 8 dan `Long Range` 6). Target aksi memakai Seed Reader A (Tabel Data Uji Dinamis TC): DD-01 (Available, Long Range, 30 dBm), DD-03 (Damaged), DD-05 (Waiting for Approval). Seed Reader A adalah Pre-setup bersama yang kuota `Long Range` sudah terpakai 5 dari 6, sehingga reader milik spec tidak bisa ditambahkan tanpa melampaui kuota; karena itu aksi mengubah Seed Reader A dan dipulihkan lewat fixture BE (disediakan tim FE, sesuai catatan Tabel Data Uji Dinamis TC: dipulihkan fixture backend sebelum tiap TC). Pemulihan dilakukan lewat langkah eksplisit di akhir tiap perubahan yang dibawa ke langkah berikutnya, dan hook `after` memulihkan sebagai cadangan.
- Stok Hardware Stock Principal HS-01 (`SN-HHR-00201`, SKU `SKU-HHR-01` Zebra RFID Reader, Long Range, Current Power 22 dBm, nomor urut unit 2) tersedia dengan status `Available` untuk aktivasi Jalur A pada blok 1. Device Name bawaan hasil aktivasi `Zebra RFID Reader - 2` mengikuti nomor urut unit stok dan counter `N` Device Name tersebut pada kondisi Seed Reader A.
- Kemampuan teknis: simulator reader USB/driver yang tersambung ke komputer penguji dan membaca `SN-HHR-00201` pada `[Sync]` (reader USB berisi unit HS-01). Mekanismenya tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA); disediakan tim FE.
- Data Dinamis: Alias Name `Reader Dock 01-{runId}-010` (suffix nomor spec 010).
- State global yang diubah: Seed Reader A (status, alias, Reader Power, jumlah reader), kuota `Long Range` Client A; dipulihkan oleh langkah pemulihan dan hook `after`.

## Test Steps

### Blok 1 - Manage hardware (Create): TC-GS-HHR-42

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Klik `[Sync]`
4. Klik `[Submit]`
5. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 2 has been activated."
6. Verifikasi baris `Zebra RFID Reader - 2` tampil dengan Status `Available`
7. Pulihkan Seed Reader A lewat fixture BE (menghapus reader hasil aktivasi dan memulihkan kuota `Long Range`)

### Blok 2 - Manage hardware (Update): TC-GS-HHR-43 sampai TC-GS-HHR-47

8. Logout, lalu login sebagai Agus Wijaya (Manage hardware level Update)
9. Buka Global Settings > Hardware > Handheld Reader
10. Buka Overlay row action DD-01, klik `Edit Alias Name`
11. Isi `Alias Name` dengan `Reader Dock 01-{runId}-010`
12. Klik `[Save]`
13. Verifikasi muncul toast sukses "Success, Reader Dock 01-{runId}-010 has been updated."
14. Verifikasi kolom `Alias Name` baris DD-01 menampilkan `Reader Dock 01-{runId}-010`
15. Pulihkan Seed Reader A lewat fixture BE, lalu muat ulang halaman Handheld Reader
16. Buka Overlay row action DD-01, klik `Edit Reader Power`
17. Geser slider ke 25 dBm
18. Klik `[Save]`
19. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 1 has been updated."
20. Verifikasi kolom `Reader Power` baris DD-01 menampilkan `25 dBm`
21. Buka Overlay row action DD-01, klik `Mark as Damaged`
22. Klik `[Mark as Damaged]` pada dialog konfirmasi
23. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 1 has been marked as damaged."
24. Verifikasi Badge `Status` baris DD-01 menjadi `Damaged`
25. Pulihkan Seed Reader A lewat fixture BE, lalu muat ulang halaman Handheld Reader
26. Buka Overlay row action DD-01, klik `Mark as Missing`
27. Klik `[Mark as Missing]` pada dialog konfirmasi
28. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 1 has been marked as missing."
29. Verifikasi Badge `Status` baris DD-01 menjadi `Missing`
30. Buka Overlay row action DD-03, klik `Mark as Available`
31. Klik `[Mark as Available]` pada dialog konfirmasi
32. Verifikasi muncul toast sukses "Success, Zebra Mobile Reader - 1 has been marked as available."
33. Verifikasi Badge `Status` baris DD-03 menjadi `Available`
34. Pulihkan Seed Reader A lewat fixture BE, lalu muat ulang halaman Handheld Reader

### Blok 3 - Manage hardware (Delete): TC-GS-HHR-49 lalu TC-GS-HHR-48

35. Logout, lalu login sebagai Dewi Anggraini (Manage hardware level Delete)
36. Buka Global Settings > Hardware > Handheld Reader
37. Buka Overlay row action DD-05, klik `Cancel Request`
38. Klik `[Cancel Request]` pada dialog konfirmasi
39. Verifikasi muncul toast sukses "Success, Chainway C72 - 1 request has been canceled."
40. Verifikasi baris DD-05 hilang dari tabel
41. Buka Overlay row action DD-01, klik `Delete`
42. Klik `[Delete]` pada dialog konfirmasi
43. Verifikasi muncul toast sukses "Success, Zebra RFID Reader - 1 has been deleted."
44. Verifikasi baris DD-01 hilang dari tabel
45. Pulihkan Seed Reader A lewat fixture BE

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 2). Kelas harness: Role Matrix positif (bagian 3a). Setiap capability hanya menjalankan aksi yang berhak dilakukannya; kombinasi role x aksi lain tidak ditambahkan karena belum punya TC sumber.
- Spec melewati sekitar 35 langkah (45 langkah nominal, tanpa perulangan). Alasan: seluruh langkah satu kelas (Role Matrix positif) dan tiap blok role berdiri sendiri dengan login ulang di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna. Aksi mutasi Seed Reader A dipulihkan fixture BE di antara aksi yang saling bergantung (langkah 15 dan 25), sehingga kegagalan satu aksi Update tidak menghilangkan makna aksi berikutnya.
- Urutan TC sumber diubah: Delete berada di blok terakhir dan TC-GS-HHR-49 (Cancel Request) dijalankan sebelum TC-GS-HHR-48 (Delete) agar aksi penghapus berada paling akhir (bagian 3 prinsip 5).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): pemulihan Seed Reader A lewat fixture BE (langkah 7, 15, 25, 34, 45); logout lalu login ke role berikutnya (langkah 8, 35); membuka halaman Handheld Reader setelah ganti akun.
- Pemulihan pada langkah 15 mengembalikan `Alias Name` DD-01 ke `—` sebelum TC-GS-HHR-44 dan TC-GS-HHR-45 (toast memakai nama `Zebra RFID Reader - 1`); pemulihan pada langkah 25 mengembalikan DD-01 ke Available sebelum TC-GS-HHR-46. Pemulihan pada langkah 34 dan 45 menyiapkan kondisi bersih sesudah aksi terakhir tiap blok.
- Temuan untuk QA:
  - TC-GS-HHR-42 berlabel Manual Only (b): membaca reader USB fisik lewat driver lokal. Mekanisme simulator USB/driver tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau mekanisme.
  - TC-GS-HHR-42 menetapkan Device Name bawaan `Zebra RFID Reader - 2` yang bergantung pada counter `N` Device Name `Zebra RFID Reader`; TC tidak menyebut mekanisme reset counter. Seed Reader A memuat `Zebra RFID Reader - 1` (DD-01 dan DD-06).
  - TC-GS-HHR-43 sampai TC-GS-HHR-49 memakai Seed Reader A bersama sebagai target aksi tulis (S-06). Reader milik spec tidak ditambahkan karena kuota `Long Range` Client A sudah terpakai 5 dari 6; spec memulihkan Seed Reader A lewat fixture BE.
  - TC-GS-HHR-43 menulis `Alias Name` literal `Reader Dock 01`; spec memakai nilai bersuffix per run (`Reader Dock 01-{runId}-010`) dan toast memuat nilai bersuffix yang sama.
  - TC-GS-HHR-42 sampai TC-GS-HHR-49 memakai ekspektasi nama toast `Zebra RFID Reader - 1` dan sejenisnya dari Seed Reader A; bila fixture BE menghasilkan nama lain, asersi toast mengikuti nama tersebut.
