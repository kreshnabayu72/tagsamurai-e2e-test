---
id: TC-FA-FAAC-E2E-123-setup-column-geser-dan-pin
title: "Setup Column Tabel Asset Class: Geser Urutan Kolom, Pin dan Unpin Kolom, dan Tidak Memengaruhi Tabel Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-399
  - TC-FA-FAAC-400
  - TC-FA-FAAC-401
  - TC-FA-FAAC-402
  - TC-FA-FAAC-407
coverage:
  web: automated
---

# Setup Column Tabel Asset Class: Geser Urutan Kolom, Pin dan Unpin Kolom, dan Tidak Memengaruhi Tabel Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Seed disediakan tim FE/BE (lihat `suite.md`).
- Kondisi awal konfigurasi kolom: bawaan (sembilan kolom tampil, Modified By dan Last Updated tersembunyi); preferensi kolom browser bersih sebelum spec dimulai.
- Kemampuan teknis: viewport dapat dipersempit sehingga tabel dapat digeser horizontal (langkah 16, 21, 26, dan 29). Lebar viewport tidak disebut TC dan ditentukan tim FE.
- Tabel "Kolom yang di-Pin" (parameter langkah 15 sampai 22): Active, Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Accounts, Asset Names, Assets.
- State yang diubah spec: konfigurasi kolom tabel disimpan di browser (Column Visibility, localStorage). Dipulihkan oleh langkah 35 dan oleh hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-399: Geser urutan kolom yang tampil secara bawaan

1. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
2. Seret kolom Assets ke posisi pertama, lalu Asset Names, Accounts, Capitalization Threshold, Fiscal, Commercial, Class Name, Class Code berturut-turut ke posisi di bawah kolom yang sebelumnya digeser sehingga urutan terbalik
3. Verifikasi tabel di balik modal (sebelum Save) menampilkan urutan Assets | Asset Names | Accounts | Capitalization Threshold | Fiscal | Commercial | Class Name | Class Code | Active
4. Klik `[Save]`
5. Verifikasi tabel menampilkan urutan yang sama setelah Save
6. Refresh halaman
7. Verifikasi urutan tetap sama setelah refresh

### TC-FA-FAAC-400: Geser urutan kolom Modified By dan Last Updated

8. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
9. Klik `[Reset to Default]`
10. Centang Modified By dan Last Updated
11. Seret Last Updated ke posisi pertama dan Modified By ke posisi kedua
12. Klik `[Save]`
13. Verifikasi tabel menampilkan urutan Last Updated | Modified By | Active | Class Code dan seterusnya

### Pemulihan sebelum TC-FA-FAAC-401

14. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`), klik `[Reset to Default]`, lalu klik `[Save]`

### TC-FA-FAAC-401: Pin dan Unpin kolom yang tampil secara bawaan

Untuk setiap kolom pada tabel "Kolom yang di-Pin" di Prerequisites (langkah 15 sampai 22):

15. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`), klik icon Pin pada kolom itu, klik `[Save]`
16. Geser tabel secara horizontal pada lebar layar sempit
17. Verifikasi kolom itu membeku (tetap terlihat) saat tabel digeser horizontal
18. Refresh halaman
19. Verifikasi status pin kolom itu tetap setelah refresh
20. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`), klik icon Pin pada kolom itu lagi untuk Unpin, klik `[Save]`
21. Geser tabel secara horizontal pada lebar layar sempit
22. Verifikasi kolom itu ikut bergeser bersama tabel

### TC-FA-FAAC-402: Pin dan Unpin kolom Modified By dan Last Updated

23. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`), centang Modified By dan Last Updated
24. Klik icon Pin pada Modified By lalu pada Last Updated
25. Klik `[Save]`
26. Geser tabel secara horizontal pada lebar layar sempit
27. Verifikasi Modified By dan Last Updated membeku saat tabel digeser
28. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`), Unpin keduanya, klik `[Save]`
29. Geser tabel secara horizontal pada lebar layar sempit
30. Verifikasi Modified By dan Last Updated ikut bergeser bersama tabel

### TC-FA-FAAC-407: Konfigurasi kolom tabel Asset Class tidak memengaruhi tabel Changelog

31. Sembunyikan kolom Class Name lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, hilangkan centang Class Name), klik `[Save]`
32. Klik icon Changelog
33. Verifikasi modal `Changelog: Asset Class` tetap menampilkan ketujuh kolom Date | Action | Class Code | Field | Old Value | New Value | Modified By
34. Tutup modal Changelog

### Pemulihan

35. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`), klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Spec berlangkah 35 tertulis, tetapi dengan ekspansi langkah 15 sampai 22 untuk sembilan kolom jumlahnya sekitar 100 langkah, jauh di atas smell 35 langkah. Alasan: seluruh blok satu topik (modal Setup Column pada tabel yang sama), langkah ulang berparameter di tabel Prerequisites (8b butir 7), `Verifikasi` tetap satu per klausa, data hanya dibaca, dan blok berdiri sendiri (kegagalan satu kolom tidak membuat kolom lain kehilangan makna).
- Langkah penghubung (S-03): langkah 9 dan 14 (mengembalikan konfigurasi bawaan lewat `[Reset to Default]` supaya blok berikutnya mulai dari kondisi awal; pemulihan hook tetap dengan menghapus preferensi kolom), langkah 34 (menutup modal Changelog), langkah 35 (memulihkan konfigurasi kolom, S-09).
- Pembagian TC-FA-FAAC-401 per kolom: tabel Prerequisites. Langkah 18 dan 19 (Refresh dan `Verifikasi` status pin tetap) ditambahkan karena Expected TC-FA-FAAC-401 butir a memuat "status pin tetap setelah refresh" sedangkan Langkah Uji TC tidak memuat refresh (lihat Temuan untuk QA).
- Langkah 3 mengamati tabel di balik modal sebelum Save sebagai state sementara (8b butir 5).
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena data hanya dibaca (S-06, S-12).
- Temuan untuk QA: (1) TC-FA-FAAC-401 Expected butir a menyebut "status pin tetap setelah refresh" tetapi Langkah Uji tidak memuat refresh. (2) TC-FA-FAAC-401 dan 402 menyebut "lebar layar sempit" tanpa angka viewport. (3) Preferensi Pin TC-FA-FAAC-399 dan 400 tidak disebut dibersihkan antar TC; spec memulihkan lewat `[Reset to Default]` sebagai langkah penghubung.
