---
id: TC-GS-BRAND-E2E-021-edit-sukses-no-op-saving-state-dan-double-click
title: "Edit Brand Sukses, No-Op, Saving State, dan Klik Ganda Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-70
  - TC-GS-BRAND-73
  - TC-GS-BRAND-75
  - TC-GS-BRAND-78
  - TC-GS-BRAND-79
  - TC-GS-BRAND-87
  - TC-GS-BRAND-88
coverage:
  web: automated
---

# Edit Brand Sukses, No-Op, Saving State, dan Klik Ganda Save

## Prerequisites

- Mode: FE+BE, dengan intercept parsial di atas backend nyata (TC-GS-BRAND-87).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data pre-setup (data environment tetap): brand Client A `Orion Tech` (bebas relasi); dipakai TC-GS-BRAND-78 dan TC-GS-BRAND-79 hanya untuk Save No-Op sehingga tidak berubah. Fixture belum ada; tim FE menyiapkan `fixtures/brand.json` dengan kunci `orionTech`.
- Data dinamis (seeding lewat API di hook `before`, setara TC-GS-BRAND-56, TC-GS-BRAND-64, dan TC-GS-BRAND-65; tidak menumpang spec lain): `Tidal Co {runId}-021` (D-11), `Vesper Co {runId}-021` (D-12), dan `Wren Co {runId}-021` (D-13), dan `Edit Co {runId}-021` (brand bebas relasi untuk TC-GS-BRAND-87; pengganti Orion Tech pada TC sumber agar data Pre-setup tidak termutasi).
- Nama 120 karakter (D-15) dibangun oleh helper sehingga panjang total, termasuk akhiran ` {runId}-021`, tepat 120 karakter.
- Cleanup di hook `after` (tidak berasumsi seeding atau rename berhasil penuh): hapus lewat API brand `Tidal Co {runId}-021`, `Tidal Group {runId}-021`, `Tidal One {runId}-021`, `Vesper Co {runId}-021`, nama 120 karakter D-15, `Wren Co {runId}-021`, `Wren Labs {runId}-021`, `Edit Co {runId}-021`, dan `Edit Co Plus {runId}-021`.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons request Edit Brand selama 3 detik (TC-GS-BRAND-87) lalu melepasnya; mengakses halaman Changelog Brand untuk menghitung entri.
- State global yang diubah: tidak ada. TC-GS-BRAND-87 memakai brand milik spec sendiri, sehingga Last Updated data Pre-setup tidak berubah.

## Test Steps

### TC-GS-BRAND-78: Save Edit tanpa perubahan nilai adalah No-Op

1. Buka Global Settings > Master Reference > Brand, lalu cari baris Orion Tech (lewat pagination atau Search)
2. Catat nilai Last Updated baris Orion Tech
3. Klik `⋯` baris Orion Tech > Edit → modal Edit Brand terbuka
4. Klik [Save] tanpa mengubah nilai
5. Verifikasi toast netral: "No changes to save."
6. Verifikasi modal tertutup
7. Verifikasi Last Updated Orion Tech tidak berubah

### TC-GS-BRAND-79: Edit yang hanya mengubah huruf besar kecil atau spasi tepi adalah No-Op

8. Klik `⋯` baris Orion Tech > Edit
9. Ubah isi field Brand Name menjadi " ORION TECH " (huruf besar dan spasi di tepi)
10. Klik [Save]
11. Verifikasi toast netral: "No changes to save."
12. Verifikasi tabel tetap menampilkan `Orion Tech`
13. Verifikasi Last Updated tidak berubah

### TC-GS-BRAND-87: Saving state tombol Save pada Edit

14. Pasang intercept yang menahan respons request Edit Brand selama 3 detik
15. Klik `⋯` baris `Edit Co {runId}-021` > Edit
16. Ubah isi field Brand Name menjadi `Edit Co Plus {runId}-021`
17. Klik [Save]
18. Verifikasi [Save] menampilkan spinner
19. Verifikasi [Save] disabled sampai respons diterima
20. Verifikasi field Brand Name disabled sampai respons diterima
21. Verifikasi [Clear Field] disabled sampai respons diterima
22. Verifikasi toast sukses: "Success, brand has been updated."
23. Lepas intercept respons Edit Brand
24. Klik `⋯` baris `Edit Co Plus {runId}-021` > Edit
25. Ubah isi field Brand Name kembali menjadi `Edit Co {runId}-021`
26. Klik [Save]
27. Verifikasi toast sukses: "Success, brand has been updated."

### TC-GS-BRAND-70: Edit nama Brand berhasil

28. Cari baris `Tidal Co {runId}-021`, lalu klik `⋯` > Edit
29. Ubah isi field Brand Name menjadi `Tidal Group {runId}-021`
30. Klik [Save]
31. Verifikasi toast sukses: "Success, brand has been updated."
32. Verifikasi modal tertutup
33. Verifikasi baris menjadi `Tidal Group {runId}-021` dengan Last Updated sesuai waktu Save

### TC-GS-BRAND-88: Klik ganda Save Edit hanya memproses satu request

34. Klik `⋯` baris `Tidal Group {runId}-021` > Edit
35. Ubah isi field Brand Name menjadi `Tidal One {runId}-021`
36. Klik [Save] dua kali cepat
37. Verifikasi tepat satu toast sukses: "Success, brand has been updated."
38. Verifikasi tabel menampilkan baris `Tidal One {runId}-021`
39. Buka Changelog Brand
40. Verifikasi Changelog mencatat tepat satu entri Edit untuk perubahan `Tidal Group {runId}-021` menjadi `Tidal One {runId}-021`
41. Kembali ke Global Settings > Master Reference > Brand

### TC-GS-BRAND-73: Edit Brand Name tepat 120 karakter berhasil

42. Cari baris `Vesper Co {runId}-021`, lalu klik `⋯` > Edit
43. Ganti isi field Brand Name dengan string tepat 120 karakter (D-15, akhiran ` {runId}-021`)
44. Klik [Save]
45. Verifikasi toast sukses: "Success, brand has been updated."

### TC-GS-BRAND-75: Edit memangkas spasi tepi pada nama baru

46. Cari baris `Wren Co {runId}-021`, lalu klik `⋯` > Edit
47. Ubah isi field Brand Name menjadi "  Wren Labs {runId}-021  " (spasi di kedua tepi)
48. Klik [Save]
49. Verifikasi toast sukses: "Success, brand has been updated."
50. Verifikasi tabel menampilkan `Wren Labs {runId}-021` tanpa spasi tepi

## Notes

- Mode: FE+BE (intercept parsial untuk TC-GS-BRAND-87). Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan nomor TC sumber, mengikuti bagian 3 konvensi: kasus No-Op (TC-78, TC-79) yang tidak mengubah data lebih dulu, lalu saving state (TC-87), kemudian rangkaian rename sukses; TC-88 sengaja sesudah TC-70 karena bergantung pada hasilnya (`Tidal Group`), sesuai kolom Dependensi TC sumber.
- Dependensi data TC-70 (TC-56), TC-73 (TC-64), dan TC-75 (TC-65) disiapkan spec ini sendiri lewat API di hook `before`; spec tidak menumpang spec lain.
- Asersi "tidak ada entri log baru" untuk TC-78 dan TC-79 (Post Condition) tidak ditulis di spec ini (kelas g, bagian 3 prinsip 13g; TC terbelah, prinsip 10); keduanya dirujuk di sourceTc spec `TC-GS-BRAND-E2E-062-log-absence-no-op-skip-cancel-dan-import`.
- Asersi "Changelog mencatat satu entri Edit" pada TC-88 tetap di sini karena itu hitungan tepat satu entri (presence), bukan asersi absence.
- TC-GS-BRAND-87 memakai `Edit Co {runId}-021` (bukan Orion Tech Pre-setup) supaya Last Updated data Pre-setup tidak berubah dan asersi Last Updated di spec lain tidak terganggu. Langkah 4 TC-87 sumber ("Edit kembali, [Save]") ditulis dengan intercept sudah dilepas (langkah 23), karena TC tidak menyebut apakah respons masih ditahan.
- Langkah penghubung: langkah 23 (lepas intercept respons Edit Brand sebelum Edit kedua TC-87) dan langkah 41 (kembali ke Brand setelah membuka Changelog). Langkah 14 (pasang intercept) adalah langkah 1 TC-87.
