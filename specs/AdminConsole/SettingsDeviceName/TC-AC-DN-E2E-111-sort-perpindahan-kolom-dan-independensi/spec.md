---
id: TC-AC-DN-E2E-111-sort-perpindahan-kolom-dan-independensi
title: "Sort List: Pindah Kolom, Tanpa Ikon Sort, Collation en-US, dan Tidak Mereset Search/Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-324
  - TC-AC-DN-325
  - TC-AC-DN-326
  - TC-AC-DN-327
coverage:
  web: automated
---

# Sort List: Pindah Kolom, Tanpa Ikon Sort, Collation en-US, dan Tidak Mereset Search/Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (leaf `Accessory` di `TAG` > `NFC`); #16 Device Name inti (`Field Radio` ber-Measurement `Box`); #17 seed 120 baris; #19 riwayat Changelog yang menentukan Last Modified; #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta).
- Data Dinamis (milik spec, dibuat lewat form Create pada TC-AC-DN-326): `anggur sensor {runId}-111` dan `Apel sensor {runId}-111` (Measurement `Unit`, Category `Accessory`, tanpa SKU). Keduanya dihapus lewat API pada langkah 27 dan di hook `after` sebagai cadangan (kemampuan penghapusan record disediakan tim FE/BE). `{runId}` hanya digit.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Sort, Search, dan Filter dikembalikan ke netral di akhir spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-324: Berpindah kolom sort mengembalikan kolom sebelumnya ke netral

1. Klik header `Device Name` dua kali (descending)
2. Klik header `Measurement` sekali
3. Verifikasi indikator sort pada `Device Name` netral
4. Verifikasi `Measurement` ascending (panah naik)
5. Verifikasi baris pertama Field Radio
6. Klik header `Measurement` dua kali (netral)

### TC-AC-DN-325: Kolom checkbox dan kolom Actions tidak memiliki ikon sort

7. Verifikasi header kolom checkbox tidak memiliki ikon sort
8. Verifikasi header kolom Actions `⋯` tidak memiliki ikon sort
9. Klik header kolom Actions `⋯`
10. Verifikasi Overlay Column Visibility terbuka
11. Verifikasi urutan tabel tidak berubah (default Device Name A-Z): halaman 1 menampilkan Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002
12. Tekan Esc (menutup overlay)

### TC-AC-DN-326: Sort alfabetis tidak membedakan huruf besar-kecil (collation en-US)

13. Klik `+ Device Name`
14. Ketik `anggur sensor {runId}-111` pada field Device Name
15. Klik field Measurement lalu pilih `Unit`
16. Klik field Category, expand `TAG` lalu `NFC`, pilih leaf `Accessory`
17. Centang `Stay on this form after submitting`
18. Klik `[Submit]`
19. Ketik `Apel sensor {runId}-111` pada field Device Name
20. Klik field Measurement lalu pilih `Unit`
21. Klik field Category, expand `TAG` lalu `NFC`, pilih leaf `Accessory`
22. Hapus centang `Stay on this form after submitting`
23. Klik `[Submit]`
24. Klik header `Device Name`
25. Verifikasi urutan teratas: `anggur sensor {runId}-111`, `Apel sensor {runId}-111`, Barcode Station (huruf kecil `anggur` sebelum `Apel` karena perbandingan tidak membedakan huruf besar-kecil)
26. Klik header `Device Name` dua kali (netral)

### TC-AC-DN-327: Mengubah sort tidak mereset Search dan Filter

27. Hapus `anggur sensor {runId}-111` dan `Apel sensor {runId}-111` lewat API hingga terhapus
28. Ketik Search `a`, tekan Enter
29. Klik ikon Filter, klik field `Measurement`, centang `Unit`, lalu klik `[Apply]`
30. Klik header `Last Modified`
31. Verifikasi kata kunci `a` tetap terisi di kolom pencarian
32. Klik ikon Filter
33. Verifikasi chip `Unit` tetap ada di Filter Panel
34. Verifikasi Last Modified ascending (panah naik) dan sedikitnya satu baris tampil
35. Verifikasi seluruh baris yang tampil ber-Measurement `Unit` (irisan Search dan Filter)
36. Klik `[Clear Field]`, lalu klik `[Apply]`
37. Klik `(←)` pada kotak Search
38. Klik header `Last Modified` dua kali (netral)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 6, 26, dan 38 mengembalikan sort ke netral; langkah 12 menutup overlay; langkah 27 menghapus record milik spec supaya hasil irisan TC-AC-DN-327 tidak bercampur dengan record uji; langkah 36 dan 37 membersihkan Filter dan Search.
- Record milik spec (S-06, S-12): TC sumber membuat `anggur sensor` dan `Apel sensor` tanpa suffix; spec memakai nama bersuffix `{runId}-111` yang tetap berurutan sama terhadap `Barcode Station`. Cleanup tidak kontradiktif: record tidak berada di daftar kembalikan.
- Ukuran spec (38 langkah, di atas smell 35 langkah, kode R3): satu topik (Sort List dan independensinya), satu dataset 130 baris, satu kelas harness; tiap blok TC memulai dari sort netral dan record uji dihapus di antara blok, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc; TC-AC-DN-326 (aksi Create) berada sebelum TC-AC-DN-327 dengan penghapusan record di antaranya.
- Temuan untuk QA:
  - TC-AC-DN-326 tidak mengasersi toast sukses Create dan menyatakan `Device Name` hasil Create dipulihkan automation baseline sebagai Post Condition tanpa langkah observasi; spec tidak mengasersi toast.
  - TC-AC-DN-327 Expected c ("irisan Search dan Filter dengan urutan Last Modified menaik") tidak menyebut daftar baris; spec mengasersi arah sort dan Measurement `Unit` tanpa daftar baris.
